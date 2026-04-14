from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_chapter05_is_textbook_prose_not_control_card_boxes():
    chapter = read("正文/chapters/chapter-05.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章先修要求", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter


def test_section51_contains_lsc_and_direct_method_targets():
    content = read("正文/sections/section-5.1.tex")
    assert r"\label{def:proper-functional}" in content
    assert r"\label{def:lower-semicontinuity-functional}" in content
    assert r"\label{def:coercive-functional}" in content
    assert r"\label{thm:weak-lsc-attainment}" in content
    assert r"\label{thm:direct-method-reflexive}" in content
    assert r"\ref{prop:closure-net}" in content or r"\ref{def:weak-topology}" in content or r"\ref{cor:hilbert-weak-compactness}" in content
    assert "弱下半连续" in content
    assert "强制性" in content
    assert "直接法" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content
    assert "Boyd" in content


def test_section52_contains_differential_targets():
    content = read("正文/sections/section-5.2.tex")
    assert r"\label{def:directional-derivative}" in content
    assert r"\label{def:gateaux-derivative}" in content
    assert r"\label{def:frechet-derivative}" in content
    assert r"\label{prop:frechet-implies-gateaux}" in content
    assert r"\label{def:hilbert-gradient}" in content
    assert r"\ref{thm:riesz-representation-hilbert}" in content or r"\ref{def:hilbert-space}" in content
    assert "Gâteaux" in content
    assert "Fréchet" in content
    assert "梯度" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content
    assert "Boyd" in content


def test_section53_contains_subdifferential_targets():
    content = read("正文/sections/section-5.3.tex")
    assert r"\label{def:subdifferential}" in content
    assert r"\label{prop:subgradient-optimality}" in content
    assert r"\label{prop:frechet-subdifferential-singleton}" in content
    assert r"\label{thm:subdifferential-nonempty-interior}" in content
    assert r"\label{prop:subdifferential-closed-graph}" in content
    assert r"\ref{thm:hahn-banach-geometric}" in content or r"\ref{prop:supporting-hyperplane}" in content
    assert "次微分" in content
    assert "最优性条件" in content
    assert "支撑超平面" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content
    assert "Boyd" in content


def test_section54_contains_calculus_targets():
    content = read("正文/sections/section-5.4.tex")
    assert r"\label{prop:subdifferential-sum-inclusion}" in content
    assert r"\label{thm:moreau-rockafellar-sum}" in content
    assert r"\label{prop:subdifferential-linear-pullback}" in content
    assert r"\label{cor:normal-cone-indicator}" in content
    assert r"\ref{def:subdifferential}" in content or r"\ref{thm:subdifferential-nonempty-interior}" in content
    assert "Moreau-Rockafellar" in content
    assert "和规则" in content
    assert "线性映射" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content
    assert "Boyd" in content
