# Latexmk configuration for FZU Thesis
# 使用 XeLaTeX 编译，支持中文字体

$pdf_mode = 5;  # 使用 xelatex 生成 PDF (1=pdflatex, 4=lualatex, 5=xelatex)
$xelatex = 'xelatex -shell-escape -file-line-error -halt-on-error -interaction=nonstopmode -synctex=1 %O %S';
$bibtex_use = 2; # 强制 biblatex 走 biber，避免清理后误回退到 bibtex

# Biber 用于参考文献。通过项目内包装脚本规避本机 MacTeX biber 2.20
# 在 PAR 运行时上出现的 unicore/lipo 问题。
$biber = './scripts/biber_safe.sh --bblencoding=utf8 -u -U --output_safechars %O %S';

# 清理时删除额外的辅助文件
$clean_ext = 'synctex.gz acn acr alg aux bbl bcf blg brf fdb_latexmk glg glo gls idx ilg ind lof log lot out run.xml toc dvi';

# 输出目录
$out_dir = 'output';

# 确保输出目录存在
system("mkdir -p output");
