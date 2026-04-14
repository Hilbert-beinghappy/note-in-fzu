from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_chapter09_is_textbook_prose_not_control_card_boxes():
    chapter = read("正文/chapters/chapter-09.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章先修要求", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter


def test_section91_contains_monotone_operator_targets():
    content = read("正文/sections/section-9.1.tex")
    assert r"\label{def:monotone-operator}" in content
    assert r"\label{def:maximal-monotone-operator}" in content
    assert r"\label{def:resolvent-monotone-operator}" in content
    assert r"\label{thm:minty-surjectivity}" in content
    assert r"\label{thm:subdifferential-maximal-monotone}" in content
    assert r"\ref{def:subdifferential}" in content or r"\ref{cor:normal-cone-indicator}" in content or r"\ref{thm:hahn-banach-geometric}" in content or r"\ref{thm:fenchel-rockafellar-duality}" in content
    assert "极大单调" in content
    assert "resolvent" in content
    assert "Minty" in content
    assert "次微分" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section92_contains_prox_targets():
    content = read("正文/sections/section-9.2.tex")
    assert r"\label{def:proximal-mapping}" in content
    assert r"\label{prop:prox-resolvent-subdifferential}" in content
    assert r"\label{prop:prox-optimality-condition}" in content
    assert r"\label{prop:prox-firm-nonexpansive}" in content
    assert r"\label{prop:moreau-decomposition-prox}" in content
    assert r"\ref{thm:orthogonal-projection}" in content or r"\ref{thm:riesz-representation-hilbert}" in content or r"\ref{thm:minty-surjectivity}" in content
    assert "邻近算子" in content
    assert "投影" in content
    assert "firm nonexpansive" in content
    assert "Moreau 分解" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section93_contains_moreau_yosida_targets():
    content = read("正文/sections/section-9.3.tex")
    assert r"\label{def:yosida-approximation}" in content
    assert r"\label{prop:moreau-envelope-gradient}" in content
    assert r"\label{prop:yosida-lipschitz}" in content
    assert r"\label{thm:moreau-yosida-regularization}" in content
    assert r"\label{cor:moreau-envelope-minimizers}" in content
    assert r"\ref{def:moreau-envelope}" in content or r"\ref{prop:moreau-envelope-conjugate}" in content or r"\ref{def:infimal-convolution}" in content or r"\ref{prop:moreau-decomposition-prox}" in content
    assert "Moreau-Yosida" in content
    assert "Yosida 正则化" in content
    assert "可微性" in content
    assert "Lipschitz" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section94_contains_monotone_inclusion_targets():
    content = read("正文/sections/section-9.4.tex")
    assert r"\label{def:monotone-inclusion-problem}" in content
    assert r"\label{prop:optimization-as-monotone-inclusion}" in content
    assert r"\label{prop:resolvent-fixed-point-equivalence}" in content
    assert r"\label{prop:variational-inequality-as-inclusion}" in content
    assert r"\label{cor:proximal-point-template}" in content
    assert r"\ref{thm:subdifferential-maximal-monotone}" in content or r"\ref{def:kkt-cone-system}" in content or r"\ref{cor:kkt-via-fenchel-subdifferential}" in content or r"\ref{def:abstract-cone-program}" in content
    assert "算子求根" in content
    assert "固定点" in content
    assert "单调包含" in content
    assert "proximal point" in content
    assert "Boyd" in content
    assert "第 \\ref{sec:10-1} 节" in content or "第 \\ref{chap:10} 章" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content
