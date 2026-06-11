"""Extract engine mappings from a JSON-LD schema.

This script walks the schema starting from a root class, collects slot-level
and enum-level `engine_mapping` annotations, and writes forward and reverse
lookup tables to `schema_enginemappings.json`.

The schema_enginemappings.json file is used to extract metadata from MD topology, trajectory, and log files via the biosim-extractor.
"""

import argparse
import json


class MappingsExtractor:
    """Extract forward and reverse engine mappings from a schema.

    The extractor indexes schema classes, slots, and enums, then traverses the
    class tree from a root class to build:
      - a forward map: schema path -> engine mapping entries
      - a reverse map: engine key -> schema path -> permissible values
    """

    def __init__(self, filepath):
        """Initialize the extractor.

        Args:
            filepath: Path to the JSON-LD schema file.
        """
        self.filepath = filepath
        self.schema = {}

        self.slot_index = {}
        self.class_index = {}
        self.enum_index = {}

        self.forward = {}
        self.reverse = {}

    # ----------------------------
    # Entry
    # ----------------------------
    def extract(self, root_class="SimulationMetadata"):
        """Extract mappings from the schema.

        Args:
            root_class: Name of the schema class to start traversal from.

        Returns:
            A dictionary with `forward` and `reverse` mapping tables.
        """
        with open(self.filepath) as f:
            self.schema = json.load(f)

        # Indexes
        self.slot_index = {s["name"]: s for s in self.schema.get("slots", [])}
        self.class_index = {c["name"]: c for c in self.schema.get("classes", [])}
        self.enum_index = {e["name"]: e for e in self.schema.get("enums", [])}

        self.forward = {}
        self.reverse = {}

        self._walk_class(root_class, path=root_class)

        return {"forward": self.forward, "reverse": self.reverse}

    # ----------------------------
    # Recursive traversal
    # ----------------------------
    def _walk_class(self, class_name, path):
        """Recursively walk a class and its nested slot ranges.

        Args:
            class_name: Class name to traverse.
            path: Dot-separated schema path for the current class.
        """
        cls = self.class_index.get(class_name, {})

        for slot_name in cls.get("slots", []):
            slot = self.slot_index[slot_name]
            slot_path = f"{path}.{slot_name}"

            self._handle_slot(slot_name, slot, slot_path)

            # Recurse into nested classes
            range_ = slot.get("range")
            if range_ in self.class_index:
                self._walk_class(range_, slot_path)

    # ----------------------------
    # Slot handler
    # ----------------------------
    def _handle_slot(self, slot_name, slot, path):
        """Collect mappings for a slot and its enum range, if any.

        Args:
            slot_name: Slot name.
            slot: Slot definition.
            path: Dot-separated schema path for the slot.
        """
        mappings = self._get_engine_mappings(slot)

        for m in mappings:
            for norm in self._normalise_mapping(m):
                self._add_mapping(path, norm)

        # Enum handling
        range_ = slot.get("range")
        is_multivalued = slot.get("multivalued", False)
        if range_ in self.enum_index:
            self._handle_enum(
                slot_name, self.enum_index[range_], path, multivalued=is_multivalued
            )

    # ----------------------------
    # Enum handler
    # ----------------------------
    def _handle_enum(self, slot_name, enum, path, multivalued):
        """Collect mappings for all permissible values of an enum.

        Args:
            slot_name: Slot name using the enum.
            enum: Enum definition.
            path: Dot-separated schema path for the slot.
        """
        for pv in enum.get("permissible_values", []):
            # don't use alias, can't validate against schema
            # pv_name = pv.get("aliases", [pv["text"]])[0]
            pv_name = pv["text"]

            mappings = self._get_engine_mappings(pv)

            for m in mappings:
                for norm in self._normalise_mapping(m):
                    self._add_mapping(
                        path, norm, enum_value=pv_name, multivalued=multivalued
                    )

    # ----------------------------
    # Extract engine mappings
    # ----------------------------
    def _get_engine_mappings(self, obj):
        """Return engine mappings declared in annotations.

        Args:
            obj: Schema object that may contain an `engine_mapping` annotation.

        Returns:
            A list of mapping dictionaries, or an empty list if none exist.
        """
        for ann in obj.get("annotations", []):
            if ann.get("tag") == "engine_mapping":
                return ann.get("value", [])
        return []

    # ----------------------------
    # NORMALISATION
    # ----------------------------
    def _normalise_mapping(self, mapping):
        """Normalize a raw mapping into one or more key/value/unit entries.

        Args:
            mapping: Raw engine mapping dictionary.

        Yields:
            Normalized mapping dictionaries with keys:
            `engine`, `key`, `value`, and optional `unit`.
        """
        keys = mapping.get("key")

        if keys is None:
            return []

        if not isinstance(keys, list):
            keys = [keys]

        for k in keys:
            yield {
                "engine": mapping["engine"],
                "key": k,
                "value": mapping.get("value"),
                "unit": mapping.get("unit"),
            }

    # ----------------------------
    # Add to forward + reverse maps
    # ----------------------------
    def _add_mapping(self, path, mapping, enum_value=None, multivalued=False):
        """Add a normalized mapping to the forward and reverse indexes.

        Args:
            path: Dot-separated schema path.
            mapping: Normalized mapping dictionary.
            enum_value: Optional enum permissible value associated with the mapping.
        """
        engine = mapping["engine"]
        key = mapping["key"]
        unit = mapping.get("unit")  # NEW

        # ============================
        # FORWARD MAP
        # ============================
        self.forward.setdefault(engine, {})

        entry = {"key": key, "value": mapping.get("value")}

        # only include unit if present
        if unit is not None:
            entry["unit"] = unit

        if enum_value:
            self.forward[engine].setdefault(path, {})
            self.forward[engine][path].setdefault(enum_value, [])
            self.forward[engine][path][enum_value].append(entry)
        else:
            self.forward[engine].setdefault(path, [])
            self.forward[engine][path].append(entry)

        # ============================
        # REVERSE MAP
        # ============================
        if engine not in self.reverse:
            self.reverse[engine] = {}

        if key not in self.reverse[engine]:
            self.reverse[engine][key] = {
                "by_path": {},
                "path_metadata": {},
            }

        rev = self.reverse[engine][key]
        rev["by_path"].setdefault(path, {})

        if multivalued:
            rev["path_metadata"].setdefault(path, {})
            rev["path_metadata"][path]["multivalued"] = True

        if enum_value:
            raw_value = mapping.get("value")

            if isinstance(raw_value, list):
                value_keys = raw_value
            else:
                value_keys = [raw_value]

            for vk in value_keys:
                vk = str(vk)
                rev["by_path"][path].setdefault(vk, [])

                if enum_value not in rev["by_path"][path][vk]:
                    rev["by_path"][path][vk].append(enum_value)


# =========================
# ENTRY POINT
# =========================


def parse_args():
    """Parse command-line arguments.

    Returns:
        Parsed ``argparse.Namespace`` object.
    """
    parser = argparse.ArgumentParser(
        description="Extract engine mappings from a JSON-LD schema."
    )
    parser.add_argument("jsonldschema", help="Path to JSON-LD  schema file")
    parser.add_argument("--output", "-o", help="Output file path (default: stdout)")
    return parser.parse_args()


def main():
    """Entry point: parse args, run extraction, and write output."""
    args = parse_args()

    extractor = MappingsExtractor(args.jsonldschema)
    result = extractor.extract()

    if args.output:
        with open(args.output, "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
