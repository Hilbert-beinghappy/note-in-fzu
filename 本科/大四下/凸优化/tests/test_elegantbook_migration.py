from pathlib import Path
import re


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")
BODY_ROOT = REPO_ROOT / "正文"


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def tex_files() -> list[Path]:
    return sorted(BODY_ROOT.rglob("*.tex"))


def test_main_uses_elegantbook_entrypoint():
    main = read("main.tex")
    assert r"\documentclass[lang=cn,a4paper,newtx,section]{elegantbook}" in main
    assert r"\input{setting.tex}" not in main
    assert r"\input{setting2.tex}" not in main
    assert r"\input{cover.tex}" not in main
    assert r"\input{contents.tex}" not in main


def test_main_sets_elegantbook_metadata_and_native_structure():
    main = read("main.tex")
    assert r"\title{凸优化}" in main
    assert r"\logo{figure/logo-blue.jpg}" in main
    assert r"\cover{figure/cover.jpg}" in main
    assert r"\maketitle" in main
    assert r"\frontmatter" in main
    assert r"\tableofcontents" in main
    assert r"\mainmatter" in main


def test_body_removes_bookfield_and_legacy_prove_environment():
    for path in tex_files():
        content = path.read_text(encoding="utf-8")
        assert r"\begin{bookfield}" not in content, path
        assert r"\end{bookfield}" not in content, path
        assert r"\begin{prove}" not in content, path
        assert r"\end{prove}" not in content, path


def test_body_uses_elegantbook_example_and_exercise_signatures():
    legacy_pattern = re.compile(r"\\begin\{(?:example|exercise)\}\{")
    for path in tex_files():
        content = path.read_text(encoding="utf-8")
        assert legacy_pattern.search(content) is None, path


def test_body_removes_titled_remark_bracket_syntax():
    legacy_pattern = re.compile(r"\\begin\{remark\}\[")
    for path in tex_files():
        content = path.read_text(encoding="utf-8")
        assert legacy_pattern.search(content) is None, path


def test_compilation_log_has_no_elegantbook_novalue_labels():
    log = read("main.log")
    assert "NoValue" not in log
