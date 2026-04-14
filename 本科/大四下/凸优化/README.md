# 明日方舟孤星Latex模板

## 0.特别声明

仓库内美术素材版权归明日方舟所有，仅供学习交流使用，本人无任何盈利行为；严禁商业用途，否则后果自负  

仓库里附上了AI源文件，不过本人接触AI不到一个月，水平很有限，里面的素材还是挺粗糙的...  

其余的请博士们随意(如自用或拼团)，也可以根据个人喜好修改里面素材，本人不会有任何意见  

XHS:Mikukawaii2

## 1.封面相关设置

(PS:封面代码有点麻烦，想要实现原本排版但是元素对齐代码我个人实现不了，  

就改了现在的这一版，简单但是和我原本的排版思路有差别)  

<div style="display: flex; gap: 10px; flex-wrap: wrap;">
  <img width="200" alt="封面草稿图" src="https://github.com/user-attachments/assets/07af5237-7f33-47db-886e-c5e92e9533b7" style="object-fit: contain;">
  <img width="200" alt="封面" src="https://github.com/user-attachments/assets/ede1a88c-0c20-4229-afdc-ba3266bcc4ee" style="object-fit: contain;">
   <img width="200" alt="122" src="https://github.com/user-attachments/assets/d8bbf982-1c6a-4c60-9035-23b49e028bac" style="object-fit: contain;">
</div>  

如左图所示，在封面有三个地方需要进行设置。特别提醒一下需要根据内容自行调整，对应文件为cover.tex

封面标题

```tex
\newcommand{\TitleText}{
	\fontsize{36}{12}\selectfont\color{qiancheng}\XeTeXinterchartokenstate=0
	\AvantGarde\addfontfeatures{LetterSpace=-5} Measure Theory 
	\SSS \\[8pt] 
	\SiYuan 测度论
}

 \node[
   anchor=north west,
   minimum width=280pt,
   minimum height=100pt,
   text width=280pt,
   inner sep=0pt,
   outer sep=0pt,
   align=left,
   %align=center,
   ] at ($(current page.north west) + (10.096cm,-5.4467cm)$) {\TitleText};

%=====================================代码说明================================
在代码\fontsize{36}{12}\selectfont\color{qiancheng}\XeTeXinterchartokenstate=0中  
\fontsize{36}{12}是调整标题字体大小(目前36pt)  
\selectfont\color{qiancheng}让字体是橙色  
\XeTeXinterchartokenstate=0这个是解除宏包冲突的  

在代码\AvantGarde\addfontfeatures{LetterSpace=-5} Measure Theory里面的  
\AvantGarde\addfontfeatures{LetterSpace=-5}应用AvantGarde字体并且让字距缩小

代码\SSS \\[8pt] 是对标题进行分割线，然后上下文本间距扩大的(8pt)，也可以不使用

代码\SiYuan 测度论 是对[测度论]应用思源黑体的

最后下面的代码只需要注意align=left是让标题左对齐，你也可以用align=center让标题居中对齐

%===================================注意事项==============================
标题的排版只能说看你习惯了，能够拆为两行最好(长标题直接拆，短标题可以加标题的中文翻译等等)
默认左对齐和加入分割线\SSS，你可以删除分割线以及让标题居中
有时候需要手动调整标题字体大小，还是挺麻烦的
追求版面则可以加一些小元素让标题长短对齐(如最后一行加:到行尾等等)...
```

作者

```tex
\newcommand{\AuthorText}{
	\fontsize{15}{16}\selectfont\color{qiancheng}\XeTeXinterchartokenstate=0
	\AvantGarde\addfontfeatures{LetterSpace=-5} @Mikukawaii
}

%===================================注意事项==============================
相关代码和标题里面的差不多，默认了居中
如果名字过长可以修改字体大小
```

参考部分

```tex
\newcommand{\ReferenceText}{
	\FFF \\[14pt]
	\fontsize{9}{7}\selectfont\color{qiancheng}\AvantGarde\XeTeXinterchartokenstate=0 Reference: \\
	\fontsize{6}{7}\selectfont\color{heise}\AvantGarde\XeTeXinterchartokenstate=0 1.Jech."Set Theory".3rd ed,Springer,2003 \\
	\fontsize{6}{7}\selectfont\color{heise}\AvantGarde\XeTeXinterchartokenstate=0 2.Kechris."Classical Descriptive Set Theory".Springer,1995 \\
	\fontsize{6}{7}\selectfont\color{heise}\AvantGarde\XeTeXinterchartokenstate=0 3.Engelking."General Topology".Heldermann Veriag,1989 \\[12pt]
	\fontsize{9}{7}\selectfont\color{qiancheng}\AvantGarde\XeTeXinterchartokenstate=0 Acknowledgements: \\
	\fontsize{6}{7}\selectfont\color{heise}\AvantGarde\XeTeXinterchartokenstate=0 \#.Rhine Lab Pioneer Project \\
	}

%===================================注意事项==============================
相关代码结构也和标题里面的差不多，默认了左对齐，字体大小应该这样就可以
然后让标题是橙色的，而正文是黑色的
这里我觉得参考可以写多一点，让整个封面的左下角有点内容，看着就不会空
可以加一些莫名其妙的东西，把老师名字放进去也没有问题...
```

上面设置完后就是右图的效果

## 2.目录相关设置

<div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;">
  <img width="200" alt="233" src="https://github.com/user-attachments/assets/80b4aa1c-ad6e-4320-8232-4d3500a5007f" style="object-fit: contain;">
  <img width="200" alt="目录" src="https://github.com/user-attachments/assets/d4a88a7d-d5dc-4123-adc7-e8722058a870" style="object-fit: contain;">
</div>

目录其实没什么要改的，对应文件为contents.tex，不过有BUG需要注意一下

```tex
\renewcommand{\cftsecfont}{\SiYuan\fontsize{16pt}{20pt}\selectfont\bfseries\XeTeXinterchartokenstate=0}
\renewcommand{\cftsecpagefont}{\SiYuan\fontsize{16pt}{20pt}\selectfont\bfseries\XeTeXinterchartokenstate=0}
\renewcommand{\cftsubsecfont}{\SiYuan\fontsize{12pt}{20pt}\selectfont\bfseries\XeTeXinterchartokenstate=0}
\renewcommand{\cftsubsecpagefont}{\SiYuan\fontsize{12pt}{20pt}\selectfont\bfseries\XeTeXinterchartokenstate=0}

\newcommand{\invisibletext}{\phantom{占位本}}
\newcommand{\makecustomtoc}{%
	\BgThispage 
	\begin{adjustwidth}{100pt}{0pt}
		\begin{multicols}{2}
			\tableofcontents
			{\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\ {\invisibletext}\\
		\end{multicols}
	\end{adjustwidth}
	\AtBeginShipoutNext{\AtBeginShipoutDiscard}%
}

%==============================================================================
这里我启用了两栏的目录，主要说一下这里的代码问题：
1.有时候你的标题太长了，导致超出了目录的栏距，你可以通过
\renewcommand{\cftsubsecfont}{\SiYuan\fontsize{12pt}{20pt}\selectfont\bfseries\XeTeXinterchartokenstate=0}
修改上面的字体大小来对二级标题进行调整(也可以将标题简略)
2.因为实现不了蛇形目录(左边排满才排右边)，因此我用一些隐形的占位符进行占位
然后用\AtBeginShipoutNext{\AtBeginShipoutDiscard}将可能出现的新空白目录页删除
但是有时候你的新目录(不是空的)可能会删除，这时候用%注释掉\AtBeginShipoutNext{\AtBeginShipoutDiscard}即可
```

## 3.正文及其盒子的设置

<div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;">
  <img width="200" alt="正文" src="https://github.com/user-attachments/assets/cc3554ef-3bc5-4fd2-ba95-af5ceaf90e3b" style="object-fit: contain;">
  <img width="200" alt="7876" src="https://github.com/user-attachments/assets/c0ee4a47-0d95-4ad1-a5d5-b0d28c55924f" style="object-fit: contain;">
  <img width="200" alt="08" src="https://github.com/user-attachments/assets/bf248da5-da57-4a9e-be7b-8017f558e390" style="object-fit: contain;">
</div>

正文也没有什么需要手动调整的地方，对应文件为setting.tex，里面是页眉、页面文字的相关设置

左上角是一级标题，右上角是二级标题，不过有时候隔一页才会出现二级标题

主要还是得说说盒子的设置，对应文件为setting2.tex，如果有代码看不懂我的提议是去问GPT或gemini，其他的大模型我非常不推荐

通用盒子

```tex
% 通用三栏标题盒命令1（左右图片 + 中间自适应文字）
\newcommand{\TitleBoxI}[5]{%
	\setlength{\textwd}{0pt}%
	\sbox0{\fontsize{20}{22}\selectfont\SiYuan\XeTeXinterchartokenstate=0 #2}%
	\setlength{\textwd}{\widthof{\usebox0}}%
	\begin{tabular}[c]{@{}c@{}c@{}c@{}}
		\raisebox{-\height + 12pt}{%
			\resizebox{!}{24pt}{\includegraphics{#1}}%
		} &
		\raisebox{-\height + 12pt}{%
			\colorbox{#4}{%
				\parbox[c][18pt][c]{\textwd}{%
					\centering
					\fontsize{18}{22}\selectfont\SiYuan\XeTeXinterchartokenstate=0\color{#5} #2%
				}%
			}%
		} &
		\raisebox{-\height + 12pt}{%
			\resizebox{!}{24pt}{\includegraphics{#3}}%
		}
	\end{tabular}%
}

%===================================================================
我设置4个通用盒子，左右是图片，中间是随文字长度变化
通过\sbox0{\fontsize{20}{22}\selectfont\SiYuan\XeTeXinterchartokenstate=0 #2}%
修改里面的字体大小，可以让文字与左右间隔变大
\fontsize{18}{22}\selectfont\SiYuan\XeTeXinterchartokenstate=0\color{#5} #2%
这里可以修改字体大小
```

一些给定的盒子和自定义盒子

```tex
\begin{definition}{测试定义}
\end{definition}

\begin{theorem}{测试定理}
\end{theorem}

\begin{proposition}{测试命题}
\end{proposition}

\begin{corollary}{测试推论}
\end{corollary}

\begin{lemma}{测试引理}
\end{lemma}

\begin{example}{测试示例}
\end{example}

\begin{exercise}{练习}
\end{exercise}

\begin{prove}
\end{prove}

\begin{remark}
\end{remark}

\begin{box1}{测试}
\end{box1}

\begin{box2}{测试}
\end{box2}

\begin{box3}{测试}
\end{box3}

\begin{box4}{测试}
\end{box4}

%=========================================
上面是设置的一些数学盒子，调用代码同上面
这里box1-4是展示了一些可以自定义盒子的方法
在 素材库/正文 下面有一些素材可以按照同样的方法可以自定义盒子
我附上了AI文件，里面也有孤星的素材，会AI的可以在里面手搓
```

其实多用几次就会了...
