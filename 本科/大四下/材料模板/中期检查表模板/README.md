# 中期检查表模板

## 编译

```bash
latexmk -xelatex -shell-escape -interaction=nonstopmode -halt-on-error main.tex
```

## 填写入口

- 编辑 `main.tex` 顶部“基本信息”区域。
- `\进展情况内容`：填写已完成工作、阶段成果和下一步安排。
- `\主要存在的问题`：填写当前存在的问题、困难或风险。
- `\工作建议`：填写指导教师建议；若先由学生整理草稿，正式版提交前请按教师意见更新。

## 勾选框说明

- 所有勾选框默认是空白方框。
- 若某项需要勾选，把对应宏从 `\FZUCheckboxEmpty` 改为 `\FZUCheckboxChecked`。
- 例如：`\newcommand{\文献综述已完成框}{\FZUCheckboxChecked}`
