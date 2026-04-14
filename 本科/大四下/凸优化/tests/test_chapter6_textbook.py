from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_chapter06_is_textbook_prose_not_control_card_boxes():
    chapter = read("正文/chapters/chapter-06.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章先修要求", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter


def test_section61_contains_fenchel_conjugate_targets():
    content = read("正文/sections/section-6.1.tex")
    assert r"\label{def:fenchel-conjugate}" in content
    assert r"\label{prop:fenchel-young-inequality}" in content
    assert r"\label{prop:fenchel-young-equality-subgradient}" in content
    assert r"\label{ex:indicator-support-conjugate}" in content
    assert r"\label{ex:norm-dual-norm-conjugate}" in content
    assert r"\ref{def:subdifferential}" in content or r"\ref{thm:hahn-banach-geometric}" in content
    assert "Fenchel-Young" in content
    assert "共轭" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section62_contains_biconjugate_targets():
    content = read("正文/sections/section-6.2.tex")
    assert r"\label{def:biconjugate-functional}" in content
    assert r"\label{prop:biconjugate-below-function}" in content
    assert r"\label{prop:epigraph-biconjugate-closure}" in content
    assert r"\label{thm:fenchel-moreau}" in content
    assert r"\label{cor:indicator-support-bipolar}" in content
    assert r"\ref{def:lower-semicontinuity-functional}" in content or r"\ref{thm:direct-method-reflexive}" in content
    assert "双共轭" in content
    assert "Fenchel-Moreau" in content
    assert "闭凸" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section63_contains_infimal_convolution_targets():
    content = read("正文/sections/section-6.3.tex")
    assert r"\label{def:infimal-convolution}" in content
    assert r"\label{prop:infimal-convolution-convexity}" in content
    assert r"\label{thm:conjugate-infimal-convolution}" in content
    assert r"\label{def:moreau-envelope}" in content
    assert r"\label{prop:moreau-envelope-conjugate}" in content
    assert r"\ref{thm:moreau-rockafellar-sum}" in content or r"\ref{prop:subdifferential-linear-pullback}" in content
    assert "下确界卷积" in content
    assert "Moreau" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section64_contains_duality_targets():
    content = read("正文/sections/section-6.4.tex")
    assert r"\label{def:fenchel-primal-dual-pair}" in content
    assert r"\label{prop:fenchel-weak-duality}" in content
    assert r"\label{def:constraint-qualification-fenchel}" in content
    assert r"\label{thm:fenchel-rockafellar-duality}" in content
    assert r"\label{cor:fenchel-kkt-subdifferential}" in content
    assert r"\ref{thm:moreau-rockafellar-sum}" in content or r"\ref{def:subdifferential}" in content or r"\ref{thm:direct-method-reflexive}" in content
    assert "资格条件" in content
    assert "对偶间隙" in content
    assert "强对偶" in content
    assert "Fenchel-Rockafellar" in content
    assert "Boyd" in content
    assert "第 \\ref{sec:7-1} 节" in content or "第 \\ref{chap:07} 章" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content
