from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_chapter11_is_textbook_prose_not_control_card_boxes():
    chapter = read("正文/chapters/chapter-11.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章先修要求", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter


def test_section111_contains_control_targets():
    content = read("正文/sections/section-11.1.tex")
    assert r"\label{def:admissible-control}" in content
    assert r"\label{def:control-functional-standard-form}" in content
    assert r"\label{thm:optimal-control-existence}" in content
    assert r"\label{def:adjoint-state-control}" in content
    assert r"\label{thm:pontryagin-convex-necessary}" in content
    assert r"\ref{thm:direct-method-reflexive}" in content or r"\ref{def:gateaux-derivative}" in content or r"\ref{def:adjoint-operator}" in content or r"\ref{def:kkt-cone-system}" in content
    assert "可容许控制" in content
    assert "状态方程" in content
    assert "伴随" in content
    assert "Pontryagin" in content or "KKT" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section112_contains_finance_targets():
    content = read("正文/sections/section-11.2.tex")
    assert r"\label{def:self-financing-strategy}" in content
    assert r"\label{def:wealth-process-functional}" in content
    assert r"\label{def:convex-risk-measure}" in content
    assert r"\label{def:cvar-risk}" in content
    assert r"\label{prop:cvar-dual-representation}" in content
    assert r"\label{thm:portfolio-risk-duality}" in content
    assert r"\ref{def:probability-space}" in content or r"\ref{def:conditional-expectation}" in content or r"\ref{thm:fenchel-rockafellar-duality}" in content or r"\ref{cor:kkt-via-fenchel-subdifferential}" in content
    assert "自融资" in content
    assert "财富过程" in content
    assert "CVaR" in content or "风险度量" in content
    assert "对偶" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section113_contains_bellman_targets():
    content = read("正文/sections/section-11.3.tex")
    assert r"\label{def:value-function-stochastic-control}" in content
    assert r"\label{def:bellman-operator}" in content
    assert r"\label{thm:dynamic-programming-principle}" in content
    assert r"\label{prop:bellman-convexity-preservation}" in content
    assert r"\label{remark:hjb-limit-control}" in content
    assert r"\ref{def:self-financing-strategy}" in content or r"\ref{thm:forward-backward-convergence}" in content or r"\ref{thm:ito-formula}" in content or r"\ref{sec:11-2}" in content
    assert "Bellman" in content or "动态规划" in content
    assert "价值函数" in content
    assert "HJB" in content
    assert "Boyd" in content
    assert "时间序列逼近" not in content
    assert "RNN" not in content
    assert "LSTM" not in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content
