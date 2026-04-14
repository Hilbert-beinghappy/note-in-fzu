# 论文模板

## 编译

```bash
latexmk -xelatex -shell-escape -interaction=nonstopmode -halt-on-error main.tex
```

## 填写入口

- `sections/frontcover.tex`：封面题目、姓名、学号、学院、专业、年级、指导教师、日期。
- `sections/00_abstract.tex`：中文摘要、中文关键词、英文摘要、英文关键词。
- `sections/01_intro.tex` 到 `sections/06_conclusion.tex`：正文章节。
- `sections/acknowledgements.tex`：致谢。
- `bib/note.bib`：参考文献库。

## 使用建议

- 先替换占位内容，再按需要增加图表、公式和参考文献。
- 若题目较长，可先测试封面是否跑版，再适当换行或压缩长度。
- 正文占位章节只是最小骨架，可根据学院要求自行增删章节。
