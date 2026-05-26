# 量子力学逐节审校计划

目标：逐节检查 `量子力学.tex`，覆盖 LaTeX 排版、公式、物理概念、符号一致性、明显文字错误。
原则：不重写内容；只修复可证明确认的错误；不确定项先记录为待确认。

## 状态规则

- `todo`: 尚未检查
- `checking`: 正在检查
- `fixed`: 已确认并修复
- `ok`: 已检查未发现明确错误
- `needs_user`: 需要用户确认或需要外部教材依据

## 章节清单

| ID | 层级 | 行范围 | 标题 | 状态 | 证据/备注 |
|---|---|---:|---|---|---|
| S001 | chapter | 38-38 | `基本概念` | ok | 仅章节标题，无正文错误。 |
| S002 | section | 39-50 | `何为量子` | ok | 读过 39-50；未发现确定性公式/LaTeX错误，表述偏概念化但不强改。 |
| S003 | section | 51-51 | `简单历史` | ok | 仅章节标题。 |
| S004 | subsection | 52-135 | `经典理论遇到的问题——黑体辐射` | fixed | 修复 Boltzmann 拼写、Boltzmann 因子漏 a、`\mu T`、Planck 公式分子符号。 |
| S005 | subsection | 136-158 | `Einstein和光电效应` | fixed | 修复能量-动量关系量纲错误。 |
| S006 | subsection | 159-159 | `波粒二象性` | ok | 仅章节标题。 |
| S007 | subsubsection | 160-174 | `Compton效应` | fixed | 修复 Compton 拼写；内容未发现确定性公式错误。 |
| S008 | subsubsection | 175-179 | `实物粒子的波粒二象性——de Broglie波` | fixed | 修复 de Broglie 拼写与波长公式 `h/p`。 |
| S009 | subsection | 180-230 | `Schrödinger方程` | fixed | 修复自由粒子二阶导推导符号。 |
| S010 | subsection | 231-236 | `波函数的意义` | fixed | 修复归一化积分缺少 `dx`。 |
| S011 | subsection | 237-237 | `态叠加原理\texorpdfstring{$\&$}{和}量子态的坍缩` | ok | 仅章节标题。 |
| S012 | subsubsection | 238-243 | `电子枪式双缝` | ok | 仅图片与一句现象描述，未发现确定性错误。 |
| S013 | subsubsection | 244-248 | `水波双缝` | ok | 仅图片。 |
| S014 | subsubsection | 249-335 | `电子双缝干涉` | fixed | 修复模平方、干涉项竖线、被测路径强度、错字。 |
| S015 | subsubsection | 336-339 | `延迟选择` | ok | 表述简略但未发现确定性公式错误。 |
| S016 | subsubsection | 340-422 | `概率振幅解释` | fixed | 修复概率幅/密度混写、多缝路径求和重复与索引错误、双层双缝漏加号。 |
| S017 | subsection | 423-423 | `Bohr的氢原子模型` | fixed | 修复上一节收尾“单班x处”错字。 |
| S018 | subsubsection | 424-452 | `Bohr之前的原子模型` | fixed | 修复 Thomson 拼写和 Rutherford 金箔实验靶材。 |
| S019 | subsubsection | 453-512 | `氢原子光谱和Bohr原子模型` | fixed | 修复谱线波数符号 `\tilde{\nu}`。 |
| S020 | subsection | 513-555 | `矩阵力学` | fixed | 修复 Heisenberg 拼写和“能级差”。 |
| S021 | section | 556-556 | `线性代数回顾` | ok | 仅章节标题。 |
| S022 | subsection | 557-599 | `线性矢量空间` | fixed | 修复数乘冒号、线性相关/无关判据、`n维`与 basis 标点。 |
| S023 | subsection | 600-614 | `内积空间` | fixed | 修复内积正定性为 `A\cdot A\ge0`。 |
| S024 | subsubsection | 615-688 | `Dirac符号` | fixed | 修复内积求和下标、行向量矩阵排版、归一化定义。 |
| S025 | subsection | 689-689 | `正交归一基` | ok | 仅章节标题。 |
| S026 | subsubsection | 690-725 | `矢量在一组正交归一基下的展开` | fixed | 修复展开系数推导、投影算符定义和求和指标。 |
| S027 | subsubsection | 726-745 | `Schmidt正交化` | fixed | 修复投影应沿归一化后的 `|I\rangle`、`|II\rangle`。 |
| S028 | subsection | 746-807 | `线性算符` | fixed | 修复外积矩阵、外积文字、伴随乘积次序。 |
| S029 | subsubsection | 808-815 | `厄米算符\texorpdfstring{$\&$}{和}反厄米算符` | fixed | 修复“反厄米”文字。 |
| S030 | subsubsection | 816-823 | `幺正算符` | ok | 已检查，未发现确定性公式错误。 |
| S031 | subsection | 824-856 | `本征值和本征矢量` | fixed | 修复单位算符和特征方程行列式写法。 |
| S032 | subsubsection | 857-864 | `厄米算符的对角化` | fixed | 修复重复字和 Hermitian 用词。 |
| S033 | chapter | 865-865 | `理论基础` | ok | 仅章节标题。 |
| S034 | section | 866-892 | `Stern-Gerlach实验` | fixed | 修复 Stern-Gerlach/Goudsmit/自旋、磁矩 z 分量、自旋 z 分量与 ket 符号。 |
| S035 | subsection | 893-914 | `级联S-G实验` | fixed | 修复“通过z方向SG”和“在第一步”文字错误。 |
| S036 | section | 915-932 | `用线性代数的语言来描述力学量` | fixed | 修复标题、Schrödinger 方程通解、力学量算符符号和厄米矩阵表述。 |
| S037 | subsection | 933-963 | `拓展到无穷维` | fixed | 修复文字错误和基矢重复等号。 |
| S038 | subsection | 964-999 | `内积` | fixed | 修复连续内积极限、积分变量和完备关系单位算符。 |
| S039 | subsection | 1000-1057 | `Dirac归一化` | fixed | 修复连续基展开推导、delta 积分变量和错字。 |
| S040 | subsubsection | 1058-1084 | `Dirac-\texorpdfstring{$\delta$}{delta}函数的性质` | fixed | 修复 delta 偶函数表述、导数积分性质、傅里叶等号和阶跃函数错字。 |
| S041 | subsection | 1085-1112 | `无穷维下的算符` | fixed | 修复求导算符、ket、矩阵元和 `f'(x)` 写法。 |
| S042 | subsubsection | 1113-1117 | `位置算符\texorpdfstring{$\hat{X}$}{X}` | fixed | 修复位置算符帽号一致性。 |
| S043 | subsubsection | 1118-1123 | `无限维下的厄米算符` | fixed | 修复文字错误、`\hat{K}` 和厄米共轭判据表述。 |
| S044 | subsubsection | 1124-1180 | `力学量的平均值` | fixed | 修复平均值记号、自由粒子速度推导中的 `\hbar`、二阶导与分部积分项。 |
| S045 | subsubsection | 1181-1189 | `量子力学五大假设` | ok | 已检查，未发现确定性公式错误。 |
| S046 | section | 1190-1366 | `自旋\texorpdfstring{$\frac{1}{2}$}{1/2}系统的矩阵形式` | fixed | 修复自旋矩阵投影、bra-ket 外积、相因子、Sy 约束和 Levi-Civita。 |
| S047 | subsection | 1367-1456 | `(不)相容力学量和对易关系` | fixed | 修复 `|-\rangle` 展开、对易子括号、Jacobi 恒等式和哈密顿量对易例题。 |
| S048 | subsubsection | 1457-1497 | `力学量完全集` | fixed | 修复 CSCO 段落文字错误。 |
| S049 | subsubsection | 1498-1560 | `不确定性原理和Ehrenfest定理` | fixed | 修复 Ehrenfest 拼写、不确定度定义和复数不等式写法。 |
| S050 | subsubsection | 1561-1714 | `表象变换` | fixed | 修复幺正变换、矩阵元、本征方程、Sx 例子和矩阵变换推导。 |
| S051 | subsubsection | 1715-1873 | `不同表象的波函数` | fixed | 修复 x/p 表象展开、动量本征方程、傅里叶核和归一化推导。 |
| S052 | subsubsection | 1874-1959 | `p表象下的x算符` | fixed | 修复 `X_{p'p}`、积分变量、`i\hbar` 和 p 表象算符形式。 |
| S053 | subsubsection | 1960-2067 | `p表象下的能量本征方程` | fixed | 修复 p 表象能量方程和势能矩阵元。 |
| S054 | subsubsection | 2068-2137 | `空间平移与动量算符` | fixed | 修复平移算符指数符号、无穷小形式和对位置本征态的作用。 |
| S055 | chapter | 2138-2138 | `量子动力学` | ok | 仅章节标题。 |
| S056 | section | 2139-2170 | `时间平移与时间演化算符` | fixed | 修复 Noether 拼写、无穷小时间平移作用和 `U(t,t0)` 指数括号。 |
| S057 | section | 2171-2243 | `自旋\texorpdfstring{$s=\frac{1}{2}$}{s=1/2}体系中的时间演化` | fixed | 修复自旋哈密顿量写法和 `S_x` 期望值中间符号。 |
| S058 | section | 2244-2362 | `绘景` | fixed | 修复 Heisenberg 方程推导中的期望值符号误用和对易子次序。 |
| S059 | chapter | 2363-2363 | `一维问题` | ok | 仅章节标题。 |
| S060 | section | 2364-2464 | `定态Schrödinger 方程` | fixed | 修复简并定态线性组合示例中的本征函数和系数写法。 |
| S061 | section | 2465-2510 | `virial定理和F-H定理` | fixed | 修复 virial 对易子乘法规则、动量算符下标和三维梯度项。 |
| S062 | section | 2511-2637 | `一维无限深方势阱` | fixed | 修复势阱外区间端点、相邻能级差表述和相对间隔公式。 |
| S063 | subsection | 2638-2690 | `三维无限深方势阱` | fixed | 修复势能分段条件和分离变量后的能量分量。 |
| S064 | subsection | 2691-2708 | `束缚态和散射态` | ok | 图片示意和定性说明未发现确定性错误。 |
| S065 | subsection | 2709-2937 | `一维定态的几个基本命题` | fixed | 修复 Wronskian 记号、简并度证明常数和宇称证明比例关系。 |
| S066 | section | 2938-2938 | `一维有限深方势阱` | ok | 仅章节标题。 |
| S067 | subsection | 2939-3110 | `束缚态` | fixed | 修复有限深势阱奇偶宇称边界条件和奇态方程。 |
| S068 | subsection | 3111-3248 | `散射态` | fixed | 修复势阱内波数、边界条件、透射振幅和透射率公式。 |
| S069 | section | 3249-3368 | `自由粒子` | fixed | 修复 k/p 表象归一化、含时相位、波包群速度推导。 |
| S070 | subsection | 3369-3461 | `概率流密度` | fixed | 修复概率流推导符号、积分守恒式和平面波流密度。 |
| S071 | section | 3462-3651 | `一维有限高方势垒\texorpdfstring{$\&$}{和}量子隧穿` | fixed | 修复有限高势垒三种能区公式、边界条件、矩阵和透射率。 |
| S072 | section | 3652-3788 | `\texorpdfstring{$\delta$}{delta}势阱/势垒` | fixed | 修复 delta 势阱导数跃变条件、束缚态符号和散射流密度。 |
| S073 | section | 3789-4073 | `简谐振子` | fixed | 修复势能、哈密顿量、升降算符、基态波函数和粒子数表象矩阵。 |
| S074 | chapter | 4053-4053 | `角动量理论` | ok | 仅章节标题。 |
| S075 | section | 4054-4241 | `角动量的一般理论` | fixed | 修复转动定义、小转动矩阵乘法、量子转动占位式和角动量对易推导相关符号。 |
| S076 | section | 4242-4498 | `角动量的本征值和本征矢` | fixed | 修复本征值量纲、升降算符推导、最高/最低权分支、归一化系数和 spin-1 矩阵/本征矢。 |
| S077 | section | 4499-4772 | `轨道角动量` | fixed | 修复轨道角动量分量、共同本征函数标题、球谐函数推导、拉普拉斯角向部分和坐标-球谐关系。 |
| S078 | section | 4773-4950 | `自旋角动量和pauli算符` | fixed | 修复 Pauli 矩阵命名、自旋对易关系、CSO/CSCO 选择、连续基完备性、旋量归一化和例题概率。 |
| S079 | section | 4951-5022 | `电子自旋在任意方向的投影` | fixed | 修复任意方向负本征态旋量。 |
| S080 | section | 5023-5023 | `角动量的合成` | ok | 仅章节标题。 |
| S081 | subsection | 5024-5058 | `两个一般角动量的合成` | fixed | 修复总角动量取值表述中的投影/量子数符号混用。 |
| S082 | subsection | 5059-5089 | `双自旋\texorpdfstring{$\frac{1}{2}$}{1/2}粒子` | ok | 三重态/单态列举未发现确定性公式错误。 |
| S083 | section | 5090-5115 | `耦合表象` | fixed | 修复总角动量守恒对易关系方向和单粒子角动量不守恒表述。 |
| S084 | subsection | 5116-5178 | `自旋-轨道耦合(L-S耦合与J-J耦合)` | fixed | 修复自旋-轨道耦合中守恒量表述，限定为分量一般不守恒。 |
| S085 | subsection | 5179-5202 | `非耦合表象` | fixed | 修复非耦合表象 CSCO 和基矢标记，应为 `J_1^2,J_{1z},J_2^2,J_{2z}`。 |
| S086 | subsection | 5203-5220 | `耦合表象` | fixed | 修复耦合表象中 `j=j_1+j_2` 的过强表述，改为总角动量量子数。 |
| S087 | subsection | 5221-5297 | `双自旋\texorpdfstring{$\frac{1}{2}$}{1/2}系统非耦合表象和耦合表象的联系` | fixed | 修复 `m=0` 成分排除条件、总降算符系数、单态推导和文末无关串稿图。 |
