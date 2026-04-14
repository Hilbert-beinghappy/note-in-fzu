%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% fzuthesis
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{style/fzuthesis}[2024/07/12 FZU Thesis Class]


% 加载 ctexart 类，有关该类简单说明，see https://www.overleaf.com/learn/latex/Chinese
% 该类提供包括但不限于 \heiti \zihao 等指令
\LoadClass[UTF8,a4paper,fontset=fandol]{ctexart}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 若你想要用句点（．）替换句号（。）
% 可以打开下面的注释
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% \catcode`\。=\active
% \newcommand{。}{\ifmmode\text{．}\else ．\fi}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% 设置页边距
\setlength{\headheight}{43pt}
\RequirePackage[a4paper]{geometry}


% 重新定义 \cleardoublepage 命令
\let\origdoublepage\cleardoublepage
\newcommand{\clearemptydoublepage}{
	\clearpage
	{\pagestyle{empty}\origdoublepage}
}
\let\cleardoublepage\clearemptydoublepage


% fancybox 提供了创建各种框架的命令，如\shadowbox、\doublebox、\ovalbox 等
\RequirePackage{fancybox}

% 设置有序列表与无序列表格式
\RequirePackage{enumerate} % 下面用到了 enumerate
\RequirePackage[inline]{enumitem}
\RequirePackage{circledsteps} % 用于带圆圈的数字

\setlistdepth{2}

\setlist[enumerate]{nosep,labelsep=0pt}
\setlist[enumerate,1]{label=（\arabic*）,left=2em,nosep,labelsep=0pt,wide=\parindent}
\setlist[enumerate,2]{label=\Circled{\arabic*},nosep,labelsep=0pt,labelwidth=1em,listparindent=0pt}

\setlist[itemize]{nosep}
\setlist[itemize,1]{wide=\parindent}
\setlist[itemize,2]{wide=2\parindent}



% 设置目录格式
\RequirePackage[titles,subfigure]{tocloft}
% 修改目录编号与文字的间距，默认为 1em，强制修改为 0.5em
\makeatletter
\renewcommand{\numberline}[1]{%
	\settowidth\@tempdimb{#1\hspace{0.5em}}%
	\hb@xt@\@tempdimb{\@cftbsnum #1\@cftasnum\hfil}\@cftasnumb}
\makeatother
% 在上述修改基础上，符合模板标题对齐要求
\renewcommand{\cftdot}{$\cdot$}
\renewcommand{\cftdotsep}{1}
\setlength{\cftsecindent}{0em} % 符合毕业设计模板（理工类）一级标题顶格要求
\setlength{\cftsubsecindent}{1em} % 符合毕业设计模板（理工类）二级标题对齐一级标题文字要求
\setlength{\cftsubsubsecindent}{4em} % 符合毕业设计模板（理工类）三级标题对齐一级标题第四字要求
\setlength{\cftbeforesecskip}{0pt}  % 5?
\setlength{\cftbeforesubsecskip}{0pt}  % 3?
\setlength{\cftbeforesubsubsecskip}{0pt}
\renewcommand{\contentsname}{\zihao{4}\heiti\textmd{目~~录}}
\renewcommand{\cftsecfont}{\songti\zihao{5}}
\renewcommand{\cftsubsecfont}{\songti\zihao{5}}
\renewcommand{\cftsubsubsecfont}{\songti\zihao{5}}
\renewcommand{\cftsecleader}{\cftdotfill{\cftsecdotsep}}
\renewcommand{\cftsecdotsep}{\cftdotsep}
\renewcommand{\cftsecpagefont}{\zihao{5}}
\renewcommand{\cftsubsecpagefont}{\zihao{5}}
\renewcommand{\cftsubsubsecpagefont}{\zihao{5}}


% 设置图表编号和章节相关联
% see https://tex.stackexchange.com/questions/28333/continuous-v-per-chapter-section-numbering-of-figures-tables-and-other-docume
\RequirePackage{chngcntr}
\counterwithin{figure}{section}
\counterwithin{table}{section}


% 设置浮动体的 caption 位置
\RequirePackage{float}
\floatstyle{plaintop}       % 表格的 caption 在表格上方，这里仅设置了 table 环境，longtable 环境默认 plaintop
\restylefloat{table}
\RequirePackage{algorithm}	% 引入 listing
\floatstyle{plain}
\restylefloat{listing}      % listing 环境默认为 ruled，修改为 plain，将 caption 放在下方
\sloppy


% 有关字体的设置
% 五号 = 10.5 pt
% 小四 = 12.0 pt
% 四号 = 14.0 pt
% 字号对应单倍行距大小 = 字号磅数 * 1.3（如小四对应单倍行距为 15.6 pt）
% 提供 spacing 环境以灵活改变环境内行间距，同时提供一系列有关 space 的指令
% see https://github.com/rf-latex/setspace/blob/main/setspace.sty
\RequirePackage{setspace}
\setstretch{1.5}                                % 设置全文行距为 1.5
\RequirePackage[T1]{fontenc}					% 使得 ctexart 可对英文加粗
\newcommand{\xiaoer}{\fontsize{18pt}{18pt}\selectfont}
% 表格内所有字体均为小五：\zihao{-5}
% AtBeginEnvironment 在 etoolbox 里
\RequirePackage{etoolbox}
\AtBeginEnvironment{table}{\zihao{-5}}
\AtBeginEnvironment{tabular}{\zihao{-5}}
\AtBeginEnvironment{tabularx}{\zihao{-5}}


% 设置摘要与目录页样式（如页眉、页脚等）
\RequirePackage{fancyhdr}
\fancypagestyle{firststyle}{
	\fancyhf{}
	\pagenumbering{Roman}                    	% 页数使用罗马数字
	\if@twoside
		\fancyhead[LO,RE]{}   % 页眉左侧不显示 logo
		\fancyhead[RO,LE]{\large ~毕业设计（论文）~\\}
	\else
		\fancyhead[L]{}
		\fancyhead[R]{\large ~毕业设计（论文）~\\}
	\fi
	\fancyfoot[C]{\large \thepage}
	\renewcommand{\headrulewidth}{1.8pt}     	% 页眉横线
	\renewcommand{\footrulewidth}{0pt}
}


% 设置正文页样式（如页眉、页脚等）
\RequirePackage{lastpage}						% 标定最后一页，提供 LastPage
\fancypagestyle{mainstyle}{
	\fancyhf{}
	\pagenumbering{arabic}
	\if@twoside
		\fancyhead[LO,RE]{}   % 页眉左侧不显示 logo
		\fancyhead[RO,LE]{\large ~毕业设计（论文）~\\}
		\fancyfoot[RO]{{\large 共\quad \pageref{LastPage}\quad 页\quad 第\quad \thepage \quad 页}}
		\fancyfoot[LE]{{\large 第\quad \thepage \quad 页\quad 共\quad \pageref{LastPage}\quad 页}}
	\else
		\fancyhead[L]{}
		\fancyhead[R]{\large ~毕业设计（论文）~\\}
		\fancyfoot[R]{{\large 共\quad \pageref{LastPage}\quad 页\quad 第\quad \thepage \quad 页}}
	\fi
	\renewcommand{\headrulewidth}{1.8pt}     	% 页眉横线
	\renewcommand{\footrulewidth}{1.8pt}     	% 页脚横线
}


% 设置正文页内章节标题格式
\ctexset{
	section={% 一级标题
	  format={\centering\heiti\zihao{4}}, % 格式：四号黑体居中
	  aftername={\quad}, % 序号与题名间空 4 格
	  beforeskip={.5\baselineskip}, % 段前 0.5 行
	  afterskip={.5\baselineskip}, % 段后 0.5 行
	 },
	subsection={% 二级标题
			format={\heiti\zihao{5}}, % 格式：五号黑体
			aftername={\space}, % 序号与题名间空 1 格
			beforeskip={.5\baselineskip}, % 段前 0.5 行
			afterskip={.5\baselineskip}, % 段后 0.5 行
		},
	subsubsection={% 三级标题
			format={\heiti\zihao{5}}, % 格式：五号黑体
			aftername={\space}, % 序号与题名间空 1 格
			beforeskip={.5\baselineskip}, % 段前 0.5 行
			afterskip={.5\baselineskip}, % 段后 0.5 行
			indent={2em}, % 缩进 2 个汉字符
		},
	paragraph={% 四级标题
			format={\heiti\zihao{5}}, % 格式：五号黑体
			numbering=true, % 启用编号
			number={\Alph{paragraph}}, % 编号格式：使用大写字母作为四级标题
			aftername={.\space}, % 序号后带点和一个空格
			beforeskip={0pt}, % 段前 0 行
			afterskip={0pt}, % 段后 0 行
			indent={2em}, % 缩进 2 个汉字符
			aftertitle={\par}, % 标题后添加一个空行
		},
	subparagraph={% 五级标题
			format={\heiti\zihao{5}}, % 格式：五号黑体
			numbering=true, % 启用编号
			number={\alph{subparagraph}}, % 编号格式：使用小写字母作为五级标题
			aftername={.\space}, % 序号后带点和一个空格
			beforeskip={0pt}, % 段前 0 行
			afterskip={0pt}, % 段后 0 行
			indent={2em}, % 缩进 2 个汉字符
			aftertitle={\par}, % 标题后添加一个空行
		}
}

\setcounter{secnumdepth}{5}

% 设置参考文献格式
\RequirePackage[
	backend=biber,
	style=gb7714-2015,
	natbib=true,
]{biblatex}
\addbibresource{bib/note.bib}

\defbibheading{fzubib}[参考文献]{%
	\clearpage
	\phantomsection
	\addcontentsline{toc}{section}{#1}
	{\centering\heiti\zihao{4}#1\par}
	\vspace{30pt}
}

\renewcommand*{\bibfont}{\songti\fontsize{10.5pt}{17pt}\selectfont}
\setlength{\bibitemsep}{3pt}
\AtBeginBibliography{%
	\songti\fontsize{10.5pt}{17pt}\selectfont
	\setlength{\parskip}{3pt}
	\interlinepenalty=10000
	\clubpenalty=10000
	\widowpenalty=10000
}

\makeatletter
\AtBeginDocument{\let\c@listing\c@figure}
\makeatother


% 设置封面信息盒子（information 环境）
\RequirePackage{array}
\newcolumntype{M}[1]{>{\centering\arraybackslash}m{#1}}
\let\oldtabular\tabular
\let\endoldtabular\endtabular
\newenvironment{information}[1][h!]{
	\renewcommand{\arraystretch}{1.5}
	\setlength{\tabcolsep}{8pt}
	\zihao{-3}\oldtabular[#1]
}{\renewcommand{\arraystretch}{1.2}\endoldtabular
}

\RequirePackage{ulem,calc}
\newlength{\covertextwidth}
\newlength{\covermaxwidth}

\newcommand{\ulinecentered}[1]{
	\setlength{\covertextwidth}{\widthof{#1}}
	\setlength{\covermaxwidth}{20em} % Set the maximum width you allow
	\ifthenelse{\lengthtest{\covertextwidth > \covermaxwidth}}{
		% Calculate scale factor and scale down text if too wide
		\pgfmathsetmacro{\scalefactor}{\covermaxwidth/\covertextwidth}
		\uline{\makebox[\covermaxwidth][c]{\scalebox{\scalefactor}[1]{#1}}}
	}{
		\uline{\makebox[\covermaxwidth][c]{#1}} % Use normal text if within the limit
	}
}


% 加载包部分结束，此后开始定义内容 Layout
\AtEndOfPackage{
	\InputIfFileExists{style/fzuthesis.cfg}{}{}
}

% 论文基本信息配置
\newcommand{\school}[1]{\def\fzuschool{#1}}
\newcommand{\major}[1]{\def\fzumajor{#1}}
\newcommand{\student}[3]{\def\fzuauthornumber{#1}\def\fzuauthor{#2}\def\fzugrade{#3}}
\newcommand{\thesistitle}[2]{\def\fzuthesistitle{#1}\def\fzuthesissubtitle{#2}}
\newcommand{\thesistitleeng}[2]{\def\fzuthesistitleeng{#1}\def\fzuthesissubtitleeng{#2}}
\newcommand{\thesisadvisor}[2]{\def\fzuthesisadvisor{#1}\def\fzuthesisadvisoroutschool{#2}}
\newcommand{\thesisdate}[3]{\def\fzuthesisyear{#1}\def\fzuthesismonth{#2}\def\fzuthesisday{#3}}


% 设置封面
\newcommand{\MakeCover}[0]{
	\begin{titlepage}
		\begin{center}
			\thisfancyput(-0.75cm,-13cm){}
			\vspace*{\fill}

			% \includegraphics[height=2.25cm]{figures/logo.pdf} % 封面不显示 logo
			\vskip 40pt

			% 符合毕业设计模板（理工类），标题使用宋体一号
			\zihao{-1}\songti{本科生毕业设计（论文）}
			\vskip 60pt

			% 依据 11.福州大学本科生毕业设计（论文）封面格式要求，此处使用宋体三号
			\begin{information}{M{5em}M{21em}}
				\zihao{-3}\songti{题\quad{}\quad{}目：} & \ulinecentered{\fzuthesistitle} \\
				\zihao{-3} & \ulinecentered{\fzuthesistitle} \\
				\zihao{-3}\songti{姓\quad{}\quad{}名：} & \ulinecentered{\fzuauthor} \\
				\zihao{-3}\songti{学\quad{}\quad{}号：} & \ulinecentered{\fzuauthornumber} \\
				\zihao{-3}\songti{学\quad{}\quad{}院：} & \ulinecentered{\fzuschool} \\
				\zihao{-3}\songti{专\quad{}\quad{}业：} & \ulinecentered{\fzumajor} \\
				\zihao{-3}\songti{年\quad{}\quad{}级：} & \ulinecentered{\fzugrade} \\
				\zihao{-3}\songti{日\quad{}\quad{}期：} & \ulinecentered{\fzuthesisyear{}年\fzuthesismonth{}月\fzuthesisday{}日} \\
			\end{information}

			% \fzuthesisadvisor

			\vspace*{\fill}
		\end{center}
	\end{titlepage}
}


% 设置中文摘要页
\newcommand{\MakeAbstract}[2]{
	\begin{center}\bf\heiti\xiaoer
		\ \\
		\fzuthesistitle
	\end{center}
	\vspace{1pt}
	\begin{center}\heiti\zihao{4}
		摘要
	\end{center}
	\vspace{-0.5em}

	\begin{spacing}{1.5}
		\heiti\songti{#1}
		\par
	\end{spacing}

	\vskip 5mm
	\noindent{\songti\zihao{5}{%
			\textbf{关键词：}#2
		}}~\\
}


% 设置英文摘要页
\newcommand{\MakeAbstractEng}[2]{
	\clearpage
	\begin{center}\heiti\xiaoer
		\ \\
		\textbf{\fzuthesistitleeng}
	\end{center}
	\vspace{1pt}
	\begin{center}\heiti\zihao{4}
		\textbf{ABSTRACT}
	\end{center}
	\vspace{-0.5em}

	\begin{spacing}{1.5}
		#1
		\par
	\end{spacing}

	\vskip 13.65pt % 小五字体单倍行距 13.65pt
	\noindent{\heiti\zihao{5}
		\textbf{Key words: }#2
	}
	\par
}
