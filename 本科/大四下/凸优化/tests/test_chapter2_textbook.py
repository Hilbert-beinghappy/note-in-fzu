from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_chapter02_is_textbook_prose_not_control_card_boxes():
    chapter = read("正文/chapters/chapter-02.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章先修要求", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter


def test_section21_contains_measure_extension_targets():
    content = read("正文/sections/section-2.1.tex")
    assert r"\label{def:sigma-algebra}" in content
    assert r"\label{def:outer-measure}" in content
    assert r"\label{def:caratheodory-measurable}" in content
    assert r"\label{thm:caratheodory-extension}" in content


def test_section22_contains_integral_and_convergence_targets():
    content = read("正文/sections/section-2.2.tex")
    assert r"\label{def:lebesgue-integral}" in content
    assert r"\label{thm:monotone-convergence}" in content
    assert r"\label{lem:fatou}" in content
    assert r"\label{thm:dominated-convergence}" in content


def test_section23_contains_radon_and_riesz_targets():
    content = read("正文/sections/section-2.3.tex")
    assert r"\label{def:radon-measure}" in content
    assert r"\label{prop:radon-regularity}" in content
    assert r"\label{thm:riesz-representation}" in content
    assert r"\ref{def:polish-space}" in content or r"\ref{thm:gdelta-polish}" in content


def test_section24_contains_stochastic_analysis_targets():
    content = read("正文/sections/section-2.4.tex")
    assert r"\label{def:probability-space}" in content
    assert r"\label{def:conditional-expectation}" in content
    assert r"\label{def:martingale}" in content
    assert r"\label{def:brownian-motion}" in content
    assert r"\label{def:ito-integral}" in content
    assert r"\label{thm:ito-formula}" in content
    assert "Brownian motion" in content
    assert "Itô 积分" in content
    assert "Itô 公式" in content

