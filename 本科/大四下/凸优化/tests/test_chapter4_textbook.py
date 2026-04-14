from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_chapter04_is_textbook_prose_not_control_card_boxes():
    chapter = read("正文/chapters/chapter-04.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章先修要求", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter


def test_section41_contains_convex_set_targets():
    content = read("正文/sections/section-4.1.tex")
    assert r"\label{def:convex-set}" in content
    assert r"\label{def:affine-set}" in content
    assert r"\label{def:convex-cone}" in content
    assert r"\label{prop:convex-closure}" in content
    assert r"\label{prop:convex-hull-properties}" in content
    assert r"\ref{prop:closure-net}" in content or r"\ref{def:hilbert-space}" in content
    assert r"\subsection*{有限维对照}" in content
    assert "Boyd" in content


def test_section42_contains_core_and_relative_interior_targets():
    content = read("正文/sections/section-4.2.tex")
    assert r"\label{def:algebraic-interior}" in content
    assert r"\label{def:relative-interior}" in content
    assert r"\label{prop:ri-convex-properties}" in content
    assert r"\label{prop:core-separation-bridge}" in content
    assert r"\ref{def:convex-set}" in content or r"\ref{def:polish-space}" in content
    assert r"\subsection*{有限维对照}" in content
    assert "Boyd" in content


def test_section43_contains_hahn_banach_targets():
    content = read("正文/sections/section-4.3.tex")
    assert r"\label{def:sublinear-functional}" in content
    assert r"\label{thm:hahn-banach-analytic}" in content
    assert r"\label{thm:hahn-banach-geometric}" in content
    assert r"\label{thm:strict-separation}" in content
    assert r"\label{prop:supporting-hyperplane}" in content
    assert r"\ref{def:adjoint-operator}" in content or r"\ref{def:weak-topology}" in content
    assert r"\subsection*{有限维对照}" in content
    assert "Boyd" in content


def test_section44_contains_extreme_point_targets():
    content = read("正文/sections/section-4.4.tex")
    assert r"\label{def:extreme-point}" in content
    assert r"\label{thm:krein-milman}" in content
    assert r"\label{cor:finite-dimensional-polytope-extreme}" in content
    assert "Krein-Milman" in content
    assert "极点" in content
    assert r"\ref{thm:hahn-banach-geometric}" in content or r"\ref{def:convex-set}" in content
    assert r"\subsection*{有限维对照}" in content
    assert "Boyd" in content
