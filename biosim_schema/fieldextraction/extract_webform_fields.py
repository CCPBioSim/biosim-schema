"""Utilities for converting a compiled LinkML schema into web form field definitions.

This module reads the generated JSON-LD schema and produces a nested form-schema
structure used by the BioSimDB web UI.
"""

import argparse
import json
import re
from dataclasses import dataclass, field


# =========================================================
# CONTEXT
# =========================================================
@dataclass
class RenderContext:
    """Mutable state passed through rendering to detect cycles and cache results.

    Attributes:
        visited: Set of slot names currently being rendered, used to detect
            circular references.
        cache: Rendered form field dicts keyed by slot name, to avoid re-rendering
            the same slot multiple times.
    """

    visited: set = field(default_factory=set)
    cache: dict = field(default_factory=dict)


# =========================================================
# MAIN EXTRACTOR
# =========================================================
class WebFormFieldExtractor:
    """Extracts UI form field definitions from a compiled LinkML JSON-LD schema.

    Traverses the schema class/slot/enum graph and renders each slot directly
    into a dict suitable for driving a web form (type, label, hint, options, constraints).
    """

    def __init__(self, filepath):
        """Args:
        filepath: Path to the compiled LinkML JSON-LD schema file.
        """
        self.filepath = filepath
        self.schema = {}
        self.class_index = {}
        self.slot_index = {}
        self.enum_index = {}
        self.PRIMITIVES = {"string", "integer", "float", "boolean"}

    # ----------------------------
    # ENTRY
    # ----------------------------
    def extract(self, root_class="SimulationMetadata"):
        """Load the schema and render form fields for all slots under root_class.

        Args:
            root_class: Name of the LinkML class to use as the form root.

        Returns:
            dict: Nested form field definitions keyed by slot name.
        """
        with open(self.filepath, "r") as f:
            self.schema = json.load(f)

        self._build_indexes()
        return self._render_class_fields(root_class)

    def _build_indexes(self):
        """Index classes, slots, and enums from the loaded schema by name for O(1) lookup."""
        self.class_index = {c["name"]: c for c in self.schema.get("classes", [])}
        self.slot_index = {s["name"]: s for s in self.schema.get("slots", [])}
        self.enum_index = {e["name"]: e for e in self.schema.get("enums", [])}

    # =========================================================
    # RENDERING
    # =========================================================

    def _render_class_fields(self, class_name, context=None):
        """Render all slots of a class as a dict of form field definitions.

        Args:
            class_name: Name of the class to render.
            context: Optional render context; a fresh one is created if not provided.

        Returns:
            dict: Form field definitions keyed by slot name.
        """
        if context is None:
            context = RenderContext()
        cls = self.class_index[class_name]
        return {s: self._render_slot(s, context) for s in cls.get("slots", [])}

    def _render_slot(self, slot_name, context):
        """Render a slot directly to a form field definition.

        Dispatches to the appropriate renderer based on the slot's range type.
        Uses context to cache results and detect circular references.

        Args:
            slot_name: Name of the slot to render.
            context: Active render context for cycle detection and caching.

        Returns:
            dict: A rendered form field definition.
        """
        if slot_name in context.cache:
            return context.cache[slot_name]
        if slot_name in context.visited:
            return {"type": "circular_ref"}

        context.visited.add(slot_name)
        slot = self.slot_index[slot_name]
        range_ = slot["range"]

        if self._is_primitive(range_):
            result = self._render_primitive(slot)
        elif self._is_enum(range_):
            result = self._render_enum(slot, self.enum_index[range_])
        elif self._is_quantity(range_):
            result = self._render_quantity(slot, context)
        elif self._is_class(range_):
            result = self._render_class_node(slot, context)
        else:
            result = {"type": "unknown"}

        if slot.get("ifabsent"):
            # strip the type wrapper: string(K) → K
            import re

            m = re.match(r"\w+\((.+)\)", slot["ifabsent"])
            result["default"] = m.group(1) if m else slot["ifabsent"]

        context.cache[slot_name] = result
        return result

    # ----------------------------
    # RENDERERS
    # ----------------------------

    def _render_primitive(self, slot):
        """Render a primitive slot (string, integer, float, boolean) as a form field.

        Applies type, label, hint, pattern, placeholder, min, max, units,
        and base_uri constraints from the slot definition.

        Args:
            slot: The slot dict from the schema.

        Returns:
            dict: A form field definition with at minimum 'type', 'label', and 'hint'.
        """
        result = {
            "type": "text",
            "label": self._get_label(slot),
            "typehint": slot["range"],
            "hint": slot.get("description"),
        }

        if slot["range"] == "boolean":
            result["type"] = "checkbox"
            result["label"] += "?"

        if self._get_annotation(slot, "textarea"):
            result["type"] = "textarea"

        example = self._get_annotation(slot, "example")
        if example:
            result["example"] = example[0]

        if "unit" in slot:
            symbol = slot["unit"]["symbol"]
            result["units"] = [symbol]
            result["label"] += f" ({symbol})"

        if "pattern" in slot:
            result["pattern"] = slot["pattern"]
        if "examples" in slot:
            result["placeholder"] = slot["examples"][0]["value"]

        if slot.get("minimum_value") is not None:
            result["min"] = slot["minimum_value"]
        # if slot.get("maximum_value") is not None: result["max"] = slot["maximum_value"]

        base_uri = self._get_annotation(slot, "base_uri")
        if base_uri:
            result["base_uri"] = base_uri

        return self._apply_ui_annotations(slot, result)

    def _render_enum(self, slot, enum):
        """Render an enum slot as a select form field.

        Args:
            slot: The slot dict from the schema.
            enum: The enum dict containing permissible_values.

        Returns:
            dict: A form field definition with type 'select' and an 'options' list.
        """
        result = {
            "type": "select",
            "label": self._to_title_words(slot["name"]),
            "hint": enum.get("description"),
            "options": [
                pv.get("aliases", [pv["text"]])[0] for pv in enum["permissible_values"]
            ],
            "multiple": slot.get("multivalued", False),
        }
        example = self._get_annotation(slot, "example")
        if example:
            result["example"] = example[0]
        return self._apply_ui_annotations(slot, result)

    def _render_class_node(self, slot, context):
        """Render a class-range slot as a nested form group.

        Includes 'multiple' to indicate whether multiple instances are allowed,
        and 'max' if a maximum_cardinality constraint is present on the slot.

        Args:
            slot: The slot dict from the schema.
            context: Active render context.

        Returns:
            dict: A form field definition with type 'class' and nested 'fields'.
        """
        result = {
            "type": "class",
            "label": self._get_label(slot),  # self._to_title_words(slot["name"]),
            "hint": slot.get("description"),
            "multiple": slot.get("multivalued", False),
            "fields": self._render_class_fields(slot["range"], context),
        }
        if slot.get("maximum_cardinality") is not None:
            result["max"] = slot["maximum_cardinality"]
        return result

    def _render_quantity(self, slot, context):
        """Render a quantity slot (value + value_unit) as a compound form field.

        Sub-slot names use their alias if present, falling back to the slot name.

        Args:
            slot: The slot dict from the schema.
            context: Active render context.

        Returns:
            dict: A form field definition with type 'quantity' and nested 'fields'.
        """
        quantity_class = self.class_index[slot["range"]]
        fields = {
            self.slot_index[s].get("alias", s): self._render_slot(s, context)
            for s in quantity_class.get("slots", [])
        }
        # Propagate example as placeholder on the value sub-field
        if "examples" in slot:
            raw = slot["examples"][0]["value"]  # e.g. "1.2 nm"
            m = re.match(r"^([+\-]?[\d.eE]+)", raw.strip())
            scalar_placeholder = m.group(1) if m else raw
            vector_placeholder = self._format_example(raw)

            if "value" in fields:
                fields["value"] = {**fields["value"], "placeholder": scalar_placeholder}
            elif "vector_value" in fields:
                fields["vector_value"] = {
                    **fields["vector_value"],
                    "placeholder": vector_placeholder,
                }

        result = {
            "type": "quantity",
            "label": self._get_label(slot),
            "hint": slot.get("description"),
            "fields": fields,
        }

        example = self._get_annotation(slot, "example")
        if example:
            result["example"] = example[0]

        return result

    # =========================================================
    # TYPE CHECKS
    # =========================================================

    def _is_primitive(self, range_):
        """Return True if range_ is one of the primitive types (string, integer, float, boolean).

        Args:
            range_: The range string from a slot definition.

        Returns:
            bool: True if the range is a primitive type.
        """
        return range_ in self.PRIMITIVES

    def _is_enum(self, range_):
        """Return True if range_ refers to a known enum in the schema.

        Args:
            range_: The range string from a slot definition.

        Returns:
            bool: True if the range is an enum.
        """
        return range_ in self.enum_index

    def _is_class(self, range_):
        """Return True if range_ refers to a known class in the schema.

        Args:
            range_: The range string from a slot definition.

        Returns:
            bool: True if the range is a class.
        """
        return range_ in self.class_index

    def _is_quantity(self, range_):
        """Return True if range_ is a class whose name contains 'Quantity'.

        Note: relies on a naming convention specific to the biosim schema.
        Any quantity class must have 'Quantity' in its name to be detected correctly.

        Args:
            range_: The range string from a slot definition.

        Returns:
            bool: True if the range is a quantity class.
        """
        return self._is_class(range_) and "Quantity" in range_

    # =========================================================
    # HELPERS
    # =========================================================

    def _to_title_words(self, text):
        """Convert snake_case slot names to display labels while preserving existing caps.

        Strips a double-underscore prefix (LinkML induced name) if present.

        Args:
            text: A slot name string.

        Returns:
            str: A human-readable title-case label.
        """
        if "__" in text:
            text = text.split("__")[-1]
        # return text.replace("_", " ").strip().title()
        words = text.replace("_", " ").strip().split()
        return " ".join(w[:1].upper() + w[1:] for w in words if w)

    def _get_label(self, slot):
        """Return the display label for a slot, preferring the first alias if present.

        Args:
            slot: The slot dict from the schema.

        Returns:
            str: The label string.
        """
        return slot.get("aliases", [self._to_title_words(slot["name"])])[0]

    def _get_annotation(self, slot, tag, default=None):
        """Look up a named annotation value on a slot.

        Args:
            slot: The slot dict from the schema.
            tag: The annotation tag name to look for.
            default: Value to return if the annotation is not found.

        Returns:
            The annotation value if found, otherwise default.
        """
        for ann in slot.get("annotations", []):
            if ann.get("tag") == tag:
                return ann.get("value")
        return default

    def _format_example(self, raw):
        """Normalize example values for UI placeholders.

        Converts vector-like examples into comma-separated text without square brackets,
        so values like [90, 90, 90] render as 90, 90, 90 in form placeholders.

        Args:
            raw: Example value from the schema. Can be a list or scalar/string.

        Returns:
            str: Formatted example string suitable for placeholder display.
        """
        if isinstance(raw, list):
            return ", ".join(str(x) for x in raw)
        s = str(raw).strip()
        return s[1:-1].strip() if s.startswith("[") and s.endswith("]") else s

    def _apply_ui_annotations(self, slot, result):
        """Apply UI-specific annotations from a LinkML slot to a rendered field.

        Args:
            slot: The source LinkML slot dictionary.
            result: The partially rendered field dictionary.

        Returns:
            dict: The same field dictionary with UI flags and provenance metadata added.
        """
        if self._get_annotation(slot, "extracted_only"):
            result["extracted_only"] = True
        if self._get_annotation(slot, "ui_readonly"):
            result["readonly"] = True
        source = self._get_annotation(slot, "source")
        if source:
            result["source"] = source
        return result


# =========================
# ENTRY POINT
# =========================


def parse_args():
    """Parse command-line arguments for schema-to-webform extraction.

    Returns:
        argparse.Namespace: Parsed command-line options.
    """
    parser = argparse.ArgumentParser(
        description="Extract engine mappings from a JSON-LD schema."
    )
    parser.add_argument("jsonldschema", help="Path to JSON-LD  schema file")
    parser.add_argument("--output", "-o", help="Output file path (default: stdout)")
    return parser.parse_args()


def main():
    """Run the extractor and write the rendered schema to JSON.

    Uses the input JSON-LD schema path from the CLI and writes either to the
    requested output file or stdout.
    """
    args = parse_args()

    extractor = WebFormFieldExtractor(args.jsonldschema)
    result = extractor.extract()

    if args.output:
        with open(args.output, "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
