from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_theorem_environments_are_section_numbered_and_refstepcounter_based():
    content = read("setting2.tex")
    assert r"\newcounter{definition}[section]" in content
    assert r"\newcounter{theorem}[section]" in content
    assert r"\refstepcounter{definition}" in content
    assert r"\refstepcounter{theorem}" in content


def test_chapter01_is_textbook_prose_not_control_card_boxes():
    chapter = read("正文/chapters/chapter-01.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章先修要求", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter
    assert "函数、测度或轨道" in chapter or "变量是函数" in chapter
    assert "序列、闭球、连续映射" in chapter or "序列不再足够" in chapter


def test_section11_contains_standard_labels_and_refs():
    content = read("正文/sections/section-1.1.tex")
    assert r"\label{def:directed-set}" in content
    assert r"\label{def:net-convergence}" in content
    assert r"\label{prop:closure-net}" in content
    assert r"\label{prop:continuity-net}" in content
    assert "弱拓扑" in content
    assert "序列就不再足够" in content or "不能只谈序列" in content
    assert r"\ref{thm:banach-alaoglu}" in content


def test_section12_to_14_contain_core_reference_targets():
    sec12 = read("正文/sections/section-1.2.tex")
    sec13 = read("正文/sections/section-1.3.tex")
    sec14 = read("正文/sections/section-1.4.tex")

    assert r"\label{thm:baire-complete}" in sec12
    assert r"\label{prop:baire-equivalent}" in sec12
    assert r"\label{def:polish-space}" in sec13
    assert r"\label{thm:gdelta-polish}" in sec13
    assert r"\label{def:lusin-space}" in sec14
    assert r"\label{prop:polish-lusin-suslin}" in sec14

    assert r"\ref{thm:baire-complete}" in sec13 or r"\ref{prop:baire-equivalent}" in sec13
    assert r"\ref{def:polish-space}" in sec14
