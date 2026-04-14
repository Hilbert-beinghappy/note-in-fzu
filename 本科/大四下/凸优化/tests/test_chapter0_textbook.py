from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_chapter00_is_reader_facing_prose_not_author_dashboard():
    chapter = read("正文/chapters/chapter-00.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter
    assert "控制变量是函数而不是向量" in chapter or "变量不再是向量" in chapter
    assert "u\\in L^2(0,T)" in chapter
    assert "二次规划" in chapter


def test_section01_builds_bridge_from_boyd_to_function_space():
    content = read("正文/sections/section-0.1.tex")
    forbidden = ["定位", "本节目标", "Boyd 对应", "习题池", "写作备注"]
    for item in forbidden:
        assert item not in content
    assert r"\label{sec:0-1}" in content
    assert "Boyd" in content
    assert "u\\in L^2(0,T)" in content
    assert "二次规划" in content
    assert "函数而不是向量" in content or "变量不再是向量" in content


def test_section02_explains_why_topology_and_duality_are_needed():
    content = read("正文/sections/section-0.2.tex")
    forbidden = ["定位", "本节目标", "Boyd 对应", "习题池", "写作备注"]
    for item in forbidden:
        assert item not in content
    assert r"\label{sec:0-2}" in content
    for keyword in ["拓扑", "弱收敛", "对偶", "算子"]:
        assert keyword in content
    assert "局部凸空间" in content
    assert "自反 Banach" in content
    assert "Hilbert" in content


def test_section03_is_prose_reading_guide_not_control_console():
    content = read("正文/sections/section-0.3.tex")
    forbidden = ["定位", "本节目标", "Boyd 对应", "习题池", "写作备注"]
    for item in forbidden:
        assert item not in content
    assert r"\label{sec:0-3}" in content
    assert "如果你主要关心" in content
    assert "纯数学" in content
    assert "算法" in content
    assert "管理科学" in content
