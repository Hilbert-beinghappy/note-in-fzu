from pathlib import Path
import importlib.util


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")
GENERATOR_PATH = REPO_ROOT / "tools" / "generate_monograph_latex.py"


def load_generator():
    assert GENERATOR_PATH.exists(), f"missing generator: {GENERATOR_PATH}"
    spec = importlib.util.spec_from_file_location("generate_monograph_latex", GENERATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_generator_exposes_expected_book_shape():
    module = load_generator()
    assert len(module.PARTS) == 7
    assert len(module.CHAPTERS) == 13
    assert sum(len(ch["sections"]) for ch in module.CHAPTERS) == 50


def test_generator_declares_expected_core_outputs():
    module = load_generator()
    outputs = module.expected_outputs()
    required = {
        REPO_ROOT / "main.tex",
        REPO_ROOT / "正文" / "book.tex",
        REPO_ROOT / "正文" / "parts" / "part-01.tex",
        REPO_ROOT / "正文" / "chapters" / "chapter-00.tex",
        REPO_ROOT / "正文" / "sections" / "section-0.1.tex",
    }
    assert required.issubset(set(outputs))


def test_generator_uses_relative_paths_only():
    module = load_generator()
    rendered = module.render_main_tex()
    assert "/Users/" not in rendered
    assert "D:/" not in rendered
