from pathlib import Path


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_chapter12_is_textbook_prose_not_control_card_boxes():
    chapter = read("正文/chapters/chapter-12.tex")
    forbidden = ["本章总目标", "本章核心定理链", "本章先修要求", "本章 Boyd 映射总表", "本章习题索引表"]
    for item in forbidden:
        assert item not in chapter


def test_section121_contains_rkhs_targets():
    content = read("正文/sections/section-12.1.tex")
    assert r"\label{def:positive-definite-kernel}" in content
    assert r"\label{def:rkhs}" in content
    assert r"\label{prop:rkhs-evaluation-continuity}" in content
    assert r"\label{thm:representer-theorem}" in content
    assert r"\label{ex:kernel-ridge-regression}" in content
    assert r"\ref{def:hilbert-space}" in content or r"\ref{thm:riesz-representation-hilbert}" in content or r"\ref{thm:direct-method-reflexive}" in content or r"\ref{def:subdifferential}" in content
    assert "RKHS" in content or "再生核" in content
    assert "Representer" in content
    assert "核岭回归" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section122_contains_graph_targets():
    content = read("正文/sections/section-12.2.tex")
    assert r"\label{def:graph-laplacian-operator}" in content
    assert r"\label{def:graph-dirichlet-energy}" in content
    assert r"\label{prop:graph-laplacian-positive}" in content
    assert r"\label{prop:message-passing-graph-filter}" in content
    assert r"\label{thm:graph-diffusion-learning-interface}" in content
    assert r"\ref{thm:compact-selfadjoint-spectral}" in content or r"\ref{def:proximal-mapping}" in content or r"\ref{def:forward-backward-iteration}" in content or r"\ref{def:moreau-envelope}" in content
    assert "图拉普拉斯" in content
    assert "消息传递" in content
    assert "Dirichlet" in content or "图平滑" in content
    assert "GNN" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section123_contains_embedding_targets():
    content = read("正文/sections/section-12.3.tex")
    assert r"\label{def:two-tower-embedding-model}" in content
    assert r"\label{def:pairwise-loss-functional}" in content
    assert r"\label{def:contrastive-risk-functional}" in content
    assert r"\label{prop:two-tower-representer}" in content
    assert r"\label{thm:embedding-duality-regularized}" in content
    assert r"\ref{thm:representer-theorem}" in content or r"\ref{thm:fenchel-rockafellar-duality}" in content or r"\ref{cor:kkt-via-fenchel-subdifferential}" in content or r"\ref{prop:subdifferential-linear-pullback}" in content
    assert "多塔" in content or "双塔" in content
    assert "对比学习" in content or "配对损失" in content
    assert "对偶" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content


def test_section124_contains_distributed_targets():
    content = read("正文/sections/section-12.4.tex")
    assert r"\label{def:distributed-consensus-model}" in content
    assert r"\label{def:sharded-embedding-problem}" in content
    assert r"\label{prop:consensus-admm-splitting}" in content
    assert r"\label{thm:distributed-recommendation-convergence}" in content
    assert r"\label{cor:graph-recommendation-distributed-template}" in content
    assert r"\ref{def:admm-iteration}" in content or r"\ref{prop:admm-as-dr-splitting}" in content or r"\ref{thm:admm-primal-dual-convergence}" in content or r"\ref{def:abstract-cone-program}" in content or r"\ref{cor:proximal-point-template}" in content
    assert "分布式" in content
    assert "共识" in content or "ADMM" in content
    assert "推荐系统" in content
    assert "Boyd" in content
    assert r"\subsection*{有限维对照}" in content
    assert r"\subsection*{习题（待补）}" in content
