import argparse

import pytest

import biosim_schema.utils.generate_artifacts as mod


def _args(command, **kwargs):
    base = {
        "schema_name": "biosim_schema",
        "command": command,
        "build_html": False,
        "include_docs": False,
    }
    base.update(kwargs)
    return argparse.Namespace(**base)


def test_verify_clean_no_existing_paths_does_not_call_run(monkeypatch, tmp_path):
    called = {"n": 0}

    def fake_run(*_args, **_kwargs):
        called["n"] += 1

    monkeypatch.setattr(mod, "run", fake_run)
    mod.verify_clean([tmp_path / "missing.json"], cwd=tmp_path)

    assert called["n"] == 0


def test_generate_docs_build_html_triggers_make(monkeypatch, tmp_path):
    paths = mod.ArtifactPaths(repo_root=tmp_path, schema_name="biosim_schema")
    calls = []

    monkeypatch.setattr(mod.shutil, "rmtree", lambda *a, **k: None)
    monkeypatch.setattr(mod, "fix_generated_docs", lambda p: calls.append(("fix", p)))
    monkeypatch.setattr(mod, "run", lambda cmd, cwd=None: calls.append((cmd, cwd)))

    mod.generate_docs(paths, build_html=True)

    assert calls[0][0][0] == "gen-doc"
    assert calls[1] == ("fix", paths.linkml_docs_dir)
    assert calls[2][0][:3] == ["make", "-C", str(paths.docs_dir)]


def test_main_dispatches_all(monkeypatch, tmp_path):
    monkeypatch.setattr(mod, "parse_args", lambda: _args("all", build_html=True))
    monkeypatch.setattr(mod, "repo_root", lambda: tmp_path)

    calls = []
    monkeypatch.setattr(mod, "generate_project", lambda p: calls.append("project"))
    monkeypatch.setattr(mod, "generate_derived", lambda p: calls.append("derived"))
    monkeypatch.setattr(
        mod,
        "generate_docs",
        lambda p, build_html=False: calls.append(("docs", build_html)),
    )

    mod.main()

    assert calls == ["project", "derived", ("docs", True)]


def test_main_verify_with_include_docs(monkeypatch, tmp_path):
    monkeypatch.setattr(mod, "parse_args", lambda: _args("verify", include_docs=True))
    monkeypatch.setattr(mod, "repo_root", lambda: tmp_path)

    paths = mod.ArtifactPaths(repo_root=tmp_path, schema_name="biosim_schema")
    paths.linkml_docs_dir.mkdir(parents=True, exist_ok=True)
    (paths.linkml_docs_dir / "x.md").write_text("x", encoding="utf-8")

    monkeypatch.setattr(mod, "generate_derived", lambda p: None)
    monkeypatch.setattr(mod, "generate_docs", lambda p, build_html=False: None)

    seen = {}
    monkeypatch.setattr(
        mod, "verify_clean", lambda files, cwd: seen.update(files=list(files), cwd=cwd)
    )

    mod.main()

    assert seen["cwd"] == tmp_path
    assert any(str(p).endswith("x.md") for p in seen["files"])


def test_fix_generated_docs_rewrites_known_patterns(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    md = docs_dir / "sample.md"
    md.write_text(
        "---\nsearch:\n  boost: 1.0\n---# Type: foo\n\n```puml\nA -> B\n```\n",
        encoding="utf-8",
    )

    mod.fix_generated_docs(docs_dir)

    out = md.read_text(encoding="utf-8")
    assert "\n---\n# Type: foo" in out
    assert "```text" in out
    assert "```puml" not in out


def test_verify_clean_calls_git_diff_with_relative_paths(monkeypatch, tmp_path):
    changed = tmp_path / "project" / "schema_summary.yaml"
    changed.parent.mkdir(parents=True)
    changed.write_text("x", encoding="utf-8")

    called = {}

    def fake_run(cmd, cwd=None):
        called["cmd"] = cmd
        called["cwd"] = cwd

    monkeypatch.setattr(mod, "run", fake_run)

    mod.verify_clean([changed], cwd=tmp_path)

    assert called["cwd"] == tmp_path
    assert called["cmd"][:4] == ["git", "diff", "--exit-code", "--"]
    assert called["cmd"][-1] == "project/schema_summary.yaml"


def test_generate_derived_calls_expected_generators(monkeypatch, tmp_path):
    paths = mod.ArtifactPaths(repo_root=tmp_path, schema_name="biosim_schema")
    calls = []

    monkeypatch.setattr(
        mod, "generate_webform_fields", lambda p: calls.append("webform")
    )
    monkeypatch.setattr(
        mod, "generate_engine_mappings", lambda p: calls.append("mappings")
    )
    monkeypatch.setattr(mod, "generate_summary", lambda p: calls.append("summary"))

    mod.generate_derived(paths)

    assert calls == ["webform", "mappings", "summary"]


def test_main_dispatches_jsonld(monkeypatch, tmp_path):
    monkeypatch.setattr(mod, "parse_args", lambda: _args("jsonld"))
    monkeypatch.setattr(mod, "repo_root", lambda: tmp_path)

    called = {"n": 0}
    monkeypatch.setattr(
        mod, "generate_jsonld", lambda p: called.__setitem__("n", called["n"] + 1)
    )

    mod.main()

    assert called["n"] == 1


def test_paths_and_write_json(tmp_path):
    p = mod.ArtifactPaths(repo_root=tmp_path, schema_name="biosim_schema")
    assert p.docs_dir == tmp_path / "docs"
    assert p.linkml_docs_dir == tmp_path / "docs" / "source" / "linkml"

    out = tmp_path / "x.json"
    mod.write_json(out, {"a": 1})
    assert out.read_text(encoding="utf-8").endswith("\n")


def test_generate_webform_and_mappings_use_extractors(monkeypatch, tmp_path):
    p = mod.ArtifactPaths(repo_root=tmp_path, schema_name="biosim_schema")
    seen = {}

    class FakeWeb:
        def __init__(self, path):
            seen["web_in"] = path

        def extract(self):
            return {"w": 1}

    class FakeMap:
        def __init__(self, path):
            seen["map_in"] = path

        def extract(self):
            return {"m": 1}

    monkeypatch.setattr(mod, "WebFormFieldExtractor", FakeWeb)
    monkeypatch.setattr(mod, "MappingsExtractor", FakeMap)
    monkeypatch.setattr(
        mod, "write_json", lambda path, payload: seen.setdefault(str(path), payload)
    )

    mod.generate_webform_fields(p)
    mod.generate_engine_mappings(p)

    assert seen["web_in"] == str(p.jsonld_path)
    assert seen["map_in"] == str(p.jsonld_path)


def test_generate_summary_writes_yaml_and_csv(monkeypatch, tmp_path):
    p = mod.ArtifactPaths(repo_root=tmp_path, schema_name="biosim_schema")
    p.webform_fields_path.parent.mkdir(parents=True, exist_ok=True)
    p.webform_fields_path.write_text("{}", encoding="utf-8")

    monkeypatch.setattr(mod, "extract_summary", lambda _: {"a": {"typehint": "string"}})
    called = {}
    monkeypatch.setattr(
        mod, "write_summary_csv", lambda s, out: called.update(s=s, out=out)
    )

    mod.generate_summary(p)

    assert p.summary_yaml_path.exists()
    assert called["out"] == str(p.summary_csv_path)


@pytest.mark.parametrize(
    "cmd,extra",
    [
        ("project", {}),
        ("derived", {}),
        ("docs", {"build_html": True}),
        ("verify", {"include_docs": False}),
    ],
)
def test_main_dispatches_commands(monkeypatch, tmp_path, cmd, extra):
    monkeypatch.setattr(mod, "repo_root", lambda: tmp_path)
    monkeypatch.setattr(mod, "parse_args", lambda: _args(cmd, **extra))

    calls = []
    monkeypatch.setattr(mod, "generate_project", lambda p: calls.append("project"))
    monkeypatch.setattr(mod, "generate_derived", lambda p: calls.append("derived"))
    monkeypatch.setattr(
        mod,
        "generate_docs",
        lambda p, build_html=False: calls.append(("docs", build_html)),
    )
    monkeypatch.setattr(mod, "verify_clean", lambda files, cwd: calls.append("verify"))

    mod.main()
    assert calls


def test_main_unknown_command_raises(monkeypatch, tmp_path):
    monkeypatch.setattr(mod, "repo_root", lambda: tmp_path)
    monkeypatch.setattr(mod, "parse_args", lambda: _args("nope"))
    with pytest.raises(ValueError):
        mod.main()
