#!/usr/bin/env python
"""Generate derived BioSim schema artefacts and LinkML docs.

This module replaces ad hoc shell orchestration with a small Python CLI so the
same commands can be used locally, in CI, and in docs builds.

Examples:
    biosim-schema-generate project
    biosim-schema-generate derived
    biosim-schema-generate docs
    biosim-schema-generate all
    biosim-schema-generate verify --include-docs
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from biosim_schema.fieldextraction.extract_engine_mappings import MappingsExtractor
from biosim_schema.fieldextraction.extract_summary import (
    extract_summary,
    write_summary_csv,
)
from biosim_schema.fieldextraction.extract_webform_fields import WebFormFieldExtractor


@dataclass(frozen=True)
class ArtifactPaths:
    """Resolved repository paths used during generation."""

    repo_root: Path
    schema_name: str

    @property
    def schema_path(self) -> Path:
        return self.repo_root / "biosim_schema" / "schema" / f"{self.schema_name}.yaml"

    @property
    def project_dir(self) -> Path:
        return self.repo_root / "project" / "linkml"

    @property
    def jsonld_path(self) -> Path:
        return self.project_dir / "jsonld" / f"{self.schema_name}.jsonld"

    @property
    def docs_dir(self) -> Path:
        return self.repo_root / "docs"

    @property
    def linkml_docs_dir(self) -> Path:
        return self.docs_dir / "source" / "linkml"

    @property
    def webform_fields_path(self) -> Path:
        return self.repo_root / "project" / "schema_webformfields.json"

    @property
    def engine_mappings_path(self) -> Path:
        return self.repo_root / "project" / "schema_enginemappings.json"

    @property
    def summary_yaml_path(self) -> Path:
        return self.repo_root / "project" / "schema_summary.yaml"

    @property
    def summary_csv_path(self) -> Path:
        return self.summary_yaml_path.with_suffix(".csv")


def repo_root() -> Path:
    """Return the repository root based on this module location."""
    return Path(__file__).resolve().parents[2]


def run(cmd: list[str], cwd: Path | None = None) -> None:
    """Run a command and raise on failure."""
    print("$", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def write_json(path: Path, payload: dict) -> None:
    """Write JSON with stable formatting."""
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def generate_project(paths: ArtifactPaths) -> None:
    """Generate the full LinkML project artefacts."""
    run(
        [
            "gen-project",
            str(paths.schema_path),
            "-d",
            str(paths.project_dir),
            "--generator-arguments",
            "diagram-type: plantuml_class_diagram",
            "--exclude",
            "owl",
            "--exclude",
            "graphql",
            "--exclude",
            "excel",
        ],
        cwd=paths.repo_root,
    )


def generate_jsonld(paths: ArtifactPaths) -> None:
    """Generate only the JSON-LD project output needed by derived extractors."""
    run(
        [
            "gen-project",
            "-I",
            "jsonld",
            str(paths.schema_path),
            "-d",
            str(paths.project_dir),
            "--generator-arguments",
            "diagram-type: plantuml_class_diagram",
        ],
        cwd=paths.repo_root,
    )


def generate_webform_fields(paths: ArtifactPaths) -> None:
    """Generate schema_webformfields.json from compiled JSON-LD."""
    result = WebFormFieldExtractor(str(paths.jsonld_path)).extract()
    write_json(paths.webform_fields_path, result)


def generate_engine_mappings(paths: ArtifactPaths) -> None:
    """Generate schema_enginemappings.json from compiled JSON-LD."""
    result = MappingsExtractor(str(paths.jsonld_path)).extract()
    write_json(paths.engine_mappings_path, result)


def generate_summary(paths: ArtifactPaths) -> None:
    """Generate schema_summary.yaml and schema_summary.csv."""
    summary = extract_summary(str(paths.webform_fields_path))

    import yaml

    with paths.summary_yaml_path.open("w", encoding="utf-8") as handle:
        yaml.dump(
            summary,
            handle,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=True,
        )

    write_summary_csv(summary, str(paths.summary_csv_path))


def generate_derived(paths: ArtifactPaths) -> None:
    """Generate derived schema artefacts used by downstream tools."""

    generate_webform_fields(paths)
    generate_engine_mappings(paths)
    generate_summary(paths)


def fix_generated_docs(linkml_docs_dir: Path) -> None:
    """Apply small post-generation fixes for current LinkML doc output.

    Fixes:
        - malformed type headings where front matter closes as '---#'
        - PlantUML fences tagged as 'puml', which Sphinx does not lex by default
        - hidden Sphinx toctree helper page listing generated docs
    """
    for md_file in linkml_docs_dir.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        fixed = text.replace("\n---#", "\n---\n#")
        fixed = fixed.replace("```puml", "```text")
        if fixed != text:
            md_file.write_text(fixed, encoding="utf-8")


def generate_docs(paths: ArtifactPaths, build_html: bool = False) -> None:
    """Generate LinkML markdown docs and optionally build Sphinx HTML."""
    shutil.rmtree(paths.linkml_docs_dir, ignore_errors=True)

    run(
        [
            "gen-doc",
            "-d",
            str(paths.linkml_docs_dir),
            str(paths.schema_path),
            "--dialect",
            "myst",
            "--preserve-names",
            "--subfolder-type-separation",
        ],
        cwd=paths.repo_root,
    )

    fix_generated_docs(paths.linkml_docs_dir)

    if build_html:
        run(["make", "-C", str(paths.docs_dir), "clean", "html"], cwd=paths.repo_root)


def verify_clean(paths_to_check: Iterable[Path], cwd: Path) -> None:
    """Fail if tracked generated files differ from the working tree."""
    rel_paths = [
        path.relative_to(cwd).as_posix() for path in paths_to_check if path.exists()
    ]
    if not rel_paths:
        return
    run(["git", "diff", "--exit-code", "--", *rel_paths], cwd=cwd)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate BioSim schema artefacts and documentation."
    )
    parser.add_argument(
        "--schema-name",
        default="biosim_schema",
        help="Base schema name without extension.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("project", help="Generate full project artefacts.")
    subparsers.add_parser("jsonld", help="Generate JSON-LD artefacts only.")
    subparsers.add_parser(
        "derived", help="Generate webform, engine mapping, and summary files."
    )

    docs_parser = subparsers.add_parser("docs", help="Generate LinkML docs.")
    docs_parser.add_argument(
        "--build-html",
        action="store_true",
        help="Also build the Sphinx HTML docs.",
    )

    all_parser = subparsers.add_parser(
        "all", help="Generate project, derived files, and docs."
    )
    all_parser.add_argument(
        "--build-html",
        action="store_true",
        help="Also build the Sphinx HTML docs.",
    )

    verify_parser = subparsers.add_parser(
        "verify",
        help="Verify that generated artefacts are up to date.",
    )
    verify_parser.add_argument(
        "--include-docs",
        action="store_true",
        help="Also verify generated LinkML docs if they are committed.",
    )

    return parser.parse_args()


def main() -> None:
    """CLI entry point."""
    args = parse_args()
    paths = ArtifactPaths(repo_root=repo_root(), schema_name=args.schema_name)

    if args.command == "project":
        generate_project(paths)
        return

    if args.command == "jsonld":
        generate_jsonld(paths)
        return

    if args.command == "derived":
        generate_derived(paths)
        return

    if args.command == "docs":
        generate_docs(paths, build_html=args.build_html)
        return

    if args.command == "all":
        generate_project(paths)
        generate_derived(paths)
        generate_docs(paths, build_html=args.build_html)
        return

    if args.command == "verify":
        generate_derived(paths)
        files_to_check = [
            paths.webform_fields_path,
            paths.engine_mappings_path,
            paths.summary_yaml_path,
            paths.summary_csv_path,
        ]

        if args.include_docs:
            generate_docs(paths, build_html=False)
            if paths.linkml_docs_dir.exists():
                files_to_check.extend(paths.linkml_docs_dir.rglob("*"))

        verify_clean(files_to_check, cwd=paths.repo_root)
        return

    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
