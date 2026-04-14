from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_chapter07_is_textbook_prose_not_control_card_boxes():
    chapter = read("正文/chapters/chapter-07.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章先修要求", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter


def test_section71_contains_cone_order_targets():
    content = read("正文/sections/section-7.1.tex")
    assert r"\label{def:cone-induced-order}" in content
    assert r"\label{def:dual-cone}" in content
    assert r"\label{prop:dual-cone-closed-convex}" in content
    assert r"\label{prop:cone-order-dual-characterization}" in content
    assert r"\label{ex:positive-cone-measure-space}" in content
    assert r"\ref{def:convex-cone}" in content or r"\ref{thm:hahn-banach-geometric}" in content or r"\ref{def:fenchel-primal-dual-pair}" in content
    assert "闭凸锥" in content
    assert "对偶锥" in content
    assert "广义不等式" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section72_contains_standard_form_targets():
    content = read("正文/sections/section-7.2.tex")
    assert r"\label{def:abstract-cone-program}" in content
    assert r"\label{def:cone-lagrangian}" in content
    assert r"\label{prop:cone-dual-function-lower-bound}" in content
    assert r"\label{prop:abstract-standard-form-to-fenchel}" in content
    assert r"\label{remark:standard-form-interface}" in content
    assert r"\ref{def:fenchel-primal-dual-pair}" in content or r"\ref{prop:subdifferential-linear-pullback}" in content or r"\ref{cor:fenchel-kkt-subdifferential}" in content
    assert "标准型" in content
    assert "拉格朗日函数" in content
    assert "对偶函数" in content
    assert "Boyd" in content
    assert "Fenchel 共轭" in content
    assert "第 \\ref{sec:10-3} 节" in content or "第 \\ref{sec:10-1} 节" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section73_contains_slater_targets():
    content = read("正文/sections/section-7.3.tex")
    assert r"\label{def:generalized-slater-condition}" in content
    assert r"\label{prop:slater-implies-fenchel-qualification}" in content
    assert r"\label{prop:core-slater-variant}" in content
    assert r"\label{thm:slater-strong-duality-cone}" in content
    assert r"\label{remark:interior-vs-core-slater}" in content
    assert r"\ref{def:relative-interior}" in content or r"\ref{def:algebraic-interior}" in content
    assert r"\ref{thm:fenchel-rockafellar-duality}" in content
    assert "严格可行性" in content
    assert "资格条件" in content
    assert "强对偶" in content
    assert ("core" in content) or ("相对内部" in content)
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section74_contains_kkt_targets():
    content = read("正文/sections/section-7.4.tex")
    assert r"\label{def:kkt-cone-system}" in content
    assert r"\label{prop:cone-complementarity-dual-pair}" in content
    assert r"\label{thm:infinite-dimensional-kkt}" in content
    assert r"\label{cor:kkt-via-fenchel-subdifferential}" in content
    assert r"\label{ex:measure-valued-multiplier}" in content
    assert r"\ref{cor:fenchel-kkt-subdifferential}" in content or r"\ref{def:subdifferential}" in content or r"\ref{def:constraint-qualification-fenchel}" in content or r"\ref{thm:slater-strong-duality-cone}" in content
    assert "KKT" in content
    assert "互补松弛" in content
    assert ("乘子" in content) and (("测度" in content) or ("对偶空间" in content))
    assert "Boyd" in content
    assert "第 \\ref{sec:8-1} 节" in content or "第 \\ref{sec:10-3} 节" in content or "第 \\ref{chap:08} 章" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content
