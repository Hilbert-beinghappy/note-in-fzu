from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_chapter03_is_textbook_prose_not_control_card_boxes():
    chapter = read("正文/chapters/chapter-03.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章先修要求", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter


def test_section31_contains_banach_hilbert_targets():
    content = read("正文/sections/section-3.1.tex")
    assert r"\label{def:normed-space}" in content
    assert r"\label{def:banach-space}" in content
    assert r"\label{def:hilbert-space}" in content
    assert r"\label{thm:orthogonal-projection}" in content
    assert r"\label{thm:riesz-representation-hilbert}" in content


def test_section32_contains_weak_topology_targets():
    content = read("正文/sections/section-3.2.tex")
    assert r"\label{def:weak-topology}" in content
    assert r"\label{def:weak-star-topology}" in content
    assert r"\label{def:reflexive-space}" in content
    assert r"\label{thm:banach-alaoglu}" in content
    assert r"\label{cor:hilbert-weak-compactness}" in content
    assert r"\ref{def:net-convergence}" in content or r"\ref{prop:closure-net}" in content or r"\ref{def:polish-space}" in content
    assert "Tychonoff" in content
    assert "拓扑嵌入" in content


def test_section33_contains_operator_adjoint_targets():
    content = read("正文/sections/section-3.3.tex")
    assert r"\label{def:bounded-linear-operator}" in content
    assert r"\label{prop:operator-space-banach}" in content
    assert r"\label{def:adjoint-operator}" in content
    assert r"\label{prop:adjoint-basic-properties}" in content
    assert r"\label{cor:hilbert-adjoint-via-riesz}" in content


def test_section34_contains_spectral_targets_and_keywords():
    content = read("正文/sections/section-3.4.tex")
    assert r"\label{def:spectrum-bounded-operator}" in content
    assert r"\label{def:compact-operator}" in content
    assert r"\label{def:self-adjoint-operator}" in content
    assert r"\label{def:positive-operator}" in content
    assert r"\label{thm:compact-selfadjoint-spectral}" in content
    assert "谱定理" in content
    assert "紧算子" in content
    assert "自伴算子" in content
    assert r"\ref{def:hilbert-space}" in content or r"\ref{def:adjoint-operator}" in content
