# Task Plan: 量子力学逐节审校

## Objective
逐节检查 `/Users/huangjiawei/Desktop/GitHub/-/本科/大三上/量子力学/量子力学.tex`，尽量保证没有明确的 LaTeX、公式、物理概念、符号和文字错误。

## Constraints
- 不改写原有表达和学习笔记结构。
- 只修复可证明确认的错误。
- 不确定或需要教材核对的点写入 `findings.md`，不强行改。
- 每一节都必须在 `section_audit.md` 中有状态和证据。
- 每轮修复后用 `latexmk` 编译验证。

## Phases
1. [x] 启动检查与章节抽取。
2. [x] 建立逐节审计文件和 STM。
3. [x] 第一章逐节审校与修复。
4. [x] 第二章逐节审校与修复。
5. [x] 第三章逐节审校与修复。
6. [x] 第四章逐节审校与修复。
7. [x] 第五章逐节审校与修复。
8. [x] 全文复扫、编译验证、审计交付。

## Verification Gates
- `section_audit.md` 所有节状态不是 `todo` 或 `checking`。
- `findings.md` 中没有未处理的确定性错误。
- `latexmk -g -xelatex -synctex=1 -interaction=nonstopmode -halt-on-error 量子力学.tex` 通过。
- 高风险日志搜索为空：LaTeX Error、Missing character、Overfull hbox、hyperref warning、Missing $、Extra }。

## Errors Encountered
| Error | Attempt | Resolution |
|---|---|---|
