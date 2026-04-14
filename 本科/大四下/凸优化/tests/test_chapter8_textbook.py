from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_chapter08_is_textbook_prose_not_control_card_boxes():
    chapter = read("正文/chapters/chapter-08.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章先修要求", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter


def test_section81_contains_finite_dimensional_collapse_targets():
    content = read("正文/sections/section-8.1.tex")
    assert r"\label{prop:finite-dimensional-norm-equivalence}" in content
    assert r"\label{prop:finite-dimensional-weak-strong-equivalence}" in content
    assert r"\label{cor:finite-dimensional-compactness}" in content
    assert r"\label{thm:finite-dimensional-collapse-principle}" in content
    assert r"\ref{def:weak-topology}" in content or r"\ref{cor:hilbert-weak-compactness}" in content or r"\ref{def:kkt-cone-system}" in content
    assert ("弱拓扑" in content) or ("强拓扑" in content) or ("范数等价" in content)
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section82_contains_lp_qp_targets():
    content = read("正文/sections/section-8.2.tex")
    assert r"\label{def:linear-program-finite}" in content
    assert r"\label{def:quadratic-program-finite}" in content
    assert r"\label{prop:lp-dual-matrix-form}" in content
    assert r"\label{thm:lp-kkt-matrix}" in content
    assert r"\label{prop:qp-kkt-matrix}" in content
    assert r"\ref{def:abstract-cone-program}" in content or r"\ref{thm:infinite-dimensional-kkt}" in content or r"\ref{cor:kkt-via-fenchel-subdifferential}" in content
    assert "线性规划" in content
    assert "二次规划" in content
    assert "KKT" in content
    assert "互补松弛" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section83_contains_socp_sdp_targets():
    content = read("正文/sections/section-8.3.tex")
    assert r"\label{def:second-order-cone}" in content
    assert r"\label{def:positive-semidefinite-cone}" in content
    assert r"\label{prop:soc-self-dual}" in content
    assert r"\label{prop:trace-inner-product-duality}" in content
    assert r"\label{thm:spectral-collapse-symmetric-matrix}" in content
    assert r"\ref{def:dual-cone}" in content or r"\ref{thm:compact-selfadjoint-spectral}" in content or r"\ref{sec:3-4}" in content
    assert "二阶锥" in content
    assert "半正定锥" in content
    assert "迹内积" in content
    assert "特征值分解" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section84_contains_gp_targets():
    content = read("正文/sections/section-8.4.tex")
    assert r"\label{def:geometric-program}" in content
    assert r"\label{prop:gp-log-transform-convexity}" in content
    assert r"\label{def:log-sum-exp-gp}" in content
    assert r"\label{thm:gp-duality-fenchel}" in content
    assert r"\label{ex:power-control-gp}" in content
    assert r"\ref{thm:fenchel-rockafellar-duality}" in content or r"\ref{def:fenchel-conjugate}" in content
    assert "几何规划" in content
    assert "对数变换" in content
    assert "log-sum-exp" in content
    assert "对偶" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content
