# 动手学深度学习 - 书籍版

本目录包含从 Beamer 演示文稿转换为 elegantbook 格式的书籍版本。

## 文件结构

```
book_version/
├── main.tex              # 主文件
├── elegantbook.cls       # elegantbook 文档类
├── chapter8/             # 第8章：循环神经网络
│   ├── section_8_1.tex   # 8.1节及其子节
│   ├── section_8_2.tex   # 8.2节及其子节
│   ├── section_8_3.tex
│   ├── section_8_4.tex
│   ├── section_8_5.tex
│   ├── section_8_6.tex
│   └── section_8_7.tex
├── chapter9/             # 第9章：现代循环神经网络
│   ├── section_9_1.tex
│   ├── section_9_2.tex
│   ├── section_9_4.tex
│   ├── section_9_5.tex
│   ├── section_9_6.tex
│   └── section_9_7.tex
└── pic/                  # 图片资源
```

## 编译方法

### 方法1：使用 XeLaTeX（推荐）

```bash
cd book_version
xelatex main.tex
xelatex main.tex  # 运行两次以解决交叉引用
```

### 方法2：使用 latexmk

```bash
cd book_version
latexmk -xelatex main.tex
```

## 内容说明

### 第8章：循环神经网络
- 8.1 序列模型（统计工具、训练）
- 8.2 文本预处理（读取数据集、词表、整合功能）
- 8.3 语言模型（学习语言模型、马尔可夫模型、自然语言统计、读取长序列数据）
- 8.4 循环神经网络（无隐状态、有隐状态、字符级语言模型、困惑度）
- 8.5 从零开始实现循环神经网络
- 8.6 简洁实现
- 8.7 通过时间反向传播

### 第9章：现代循环神经网络
- 9.1 门控循环单元（GRU）
- 9.2 长短期记忆网络（LSTM）
- 9.4 双向循环神经网络
- 9.5 机器翻译数据集
- 9.6 编码器-解码器架构
- 9.7 序列到序列学习

## 主要转换

从 Beamer 到 elegantbook 的转换包括：

1. **移除 Frame 结构**：所有 `\begin{frame}...\end{frame}` 已转换为章节结构
2. **环境转换**：
   - `block` → `definition`
   - `alertblock` → `theorem`
   - `exampleblock` → `example`
3. **布局调整**：移除 `columns` 环境和 `\pause` 命令
4. **保留内容**：
   - 所有 TikZ 图形
   - 所有代码列表（lstlisting）
   - 所有数学公式

## 生成的PDF

成功编译后将生成 `main.pdf`，约153页。

## 注意事项

1. 需要安装 elegantbook 文档类所需的依赖包
2. 某些字体可能需要根据系统调整
3. 如需修改单个章节，直接编辑相应的 `chapter*/section_*.tex` 文件
4. 修改后重新编译 `main.tex` 即可

## 作者

黄佳炜 - 福州大学物理与信息工程学院



