from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_chapter10_is_textbook_prose_not_control_card_boxes():
    chapter = read("正文/chapters/chapter-10.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章先修要求", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter


def test_section101_contains_forward_backward_targets():
    content = read("正文/sections/section-10.1.tex")
    assert r"\label{def:forward-backward-iteration}" in content
    assert r"\label{def:cocoercive-operator}" in content
    assert r"\label{prop:forward-backward-fixed-point}" in content
    assert r"\label{thm:forward-backward-convergence}" in content
    assert r"\label{cor:prox-gradient-specialization}" in content
    assert r"\ref{prop:prox-resolvent-subdifferential}" in content or r"\ref{cor:proximal-point-template}" in content or r"\ref{prop:subdifferential-linear-pullback}" in content or r"\ref{thm:riesz-representation-hilbert}" in content
    assert "前向-后向" in content
    assert "cocoercive" in content
    assert "prox-gradient" in content
    assert "收敛" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section102_contains_dr_targets():
    content = read("正文/sections/section-10.2.tex")
    assert r"\label{def:reflection-operator}" in content
    assert r"\label{def:douglas-rachford-iteration}" in content
    assert r"\label{prop:dr-fixed-point-zer-sum}" in content
    assert r"\label{thm:douglas-rachford-averaged}" in content
    assert r"\label{cor:dr-feasibility-special-case}" in content
    assert r"\ref{thm:minty-surjectivity}" in content or r"\ref{prop:resolvent-fixed-point-equivalence}" in content or r"\ref{def:monotone-inclusion-problem}" in content or r"\ref{def:maximal-monotone-operator}" in content
    assert "Douglas-Rachford" in content
    assert "反射算子" in content
    assert "可行性交" in content
    assert "固定点" in content
    assert "Boyd" in content
    assert "第 \\ref{sec:10-3} 节" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section103_contains_admm_targets():
    content = read("正文/sections/section-10.3.tex")
    assert r"\label{def:augmented-lagrangian-admm}" in content
    assert r"\label{def:admm-iteration}" in content
    assert r"\label{prop:admm-as-dr-splitting}" in content
    assert r"\label{thm:admm-primal-dual-convergence}" in content
    assert r"\label{cor:admm-kkt-limit}" in content
    assert r"\ref{def:kkt-cone-system}" in content or r"\ref{cor:kkt-via-fenchel-subdifferential}" in content or r"\ref{prop:abstract-standard-form-to-fenchel}" in content or r"\ref{def:monotone-inclusion-problem}" in content or r"\ref{def:douglas-rachford-iteration}" in content
    assert "增广拉格朗日" in content
    assert "ADMM" in content
    assert "原--对偶" in content
    assert "残差" in content
    assert "Boyd" in content
    assert "Douglas--Rachford" in content or "第 \\ref{sec:10-2} 节" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section104_contains_acceleration_targets():
    content = read("正文/sections/section-10.4.tex")
    assert r"\label{def:inertial-proximal-iteration}" in content
    assert r"\label{def:lyapunov-energy-accelerated}" in content
    assert r"\label{prop:accelerated-energy-descent}" in content
    assert r"\label{thm:hilbert-acceleration-template}" in content
    assert r"\label{remark:acceleration-limitations-infinite-dimensional}" in content
    assert r"\ref{thm:forward-backward-convergence}" in content or r"\ref{prop:moreau-envelope-gradient}" in content or r"\ref{cor:proximal-point-template}" in content or r"\ref{sec:11-1}" in content
    assert "加速" in content
    assert "惰性" in content
    assert "Lyapunov" in content
    assert "Hilbert 空间" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content
