from __future__ import annotations

import re
from pathlib import Path
from textwrap import dedent


REPO_ROOT = Path("/Users/huangjiawei/Desktop/GitHub/-/本科/大四下/凸优化")
SOURCE_ROOT = Path("/Users/huangjiawei/Documents/Obsidian Vault/无穷维凸优化专著")

PARTS = [
    {"index": 1, "slug": "01", "source_dir": "01-导引篇", "title": "导引篇", "kind": "main"},
    {"index": 2, "slug": "02", "source_dir": "02-第一部分 无穷维的基石", "title": "第一部分 无穷维的基石", "kind": "main"},
    {"index": 3, "slug": "03", "source_dir": "03-第二部分 凸性、分离与微分", "title": "第二部分 凸性、分离与微分", "kind": "main"},
    {"index": 4, "slug": "04", "source_dir": "04-第三部分 Boyd坍缩", "title": "第三部分 Boyd 坍缩", "kind": "main"},
    {"index": 5, "slug": "05", "source_dir": "05-第四部分 算法", "title": "第四部分 算法", "kind": "main"},
    {"index": 6, "slug": "06", "source_dir": "06-第五部分 应用", "title": "第五部分 应用", "kind": "main"},
    {"index": 7, "slug": "07", "source_dir": "07-附录", "title": "附录", "kind": "appendix"},
]


def chapter_tex_name(number: int) -> str:
    return f"chapter-{number:02d}.tex"


def section_tex_name(section_id: str) -> str:
    return f"section-{section_id}.tex"


def part_tex_name(index: int) -> str:
    return f"part-{index:02d}.tex"


def appendix_tex_name(code: str) -> str:
    return f"appendix-{code.lower()}.tex"


def parse_markdown_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("missing markdown title")


def strip_chapter_prefix(title: str) -> str:
    return re.sub(r"^第\d+章\s*", "", title).strip()


def strip_section_prefix(title: str) -> str:
    return re.sub(r"^\d+\.\d+\s*", "", title).strip()


def strip_appendix_prefix(title: str) -> str:
    return re.sub(r"^附录[A-Z]\s*", "", title).strip()


def parse_heading_sections(text: str, heading_level: int = 2) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    prefix = "#" * heading_level + " "
    for line in text.splitlines():
        if line.startswith(prefix):
            current = line[len(prefix) :].strip()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line)
    return {key: "\n".join(value).strip() for key, value in sections.items()}


def parse_subsections(text: str) -> dict[str, str]:
    return parse_heading_sections(text, heading_level=3)


def load_section_cards(chapter_dir: Path) -> list[dict]:
    section_files = sorted(
        [p for p in chapter_dir.glob("*.md") if p.name != "README.md"],
        key=lambda p: [int(x) for x in re.match(r"(\d+)\.(\d+)", p.stem).groups()],
    )
    cards = []
    for path in section_files:
            title = parse_markdown_title(path.read_text(encoding="utf-8"))
            section_id = re.match(r"(\d+\.\d+)", title).group(1)
            cards.append(
                {
                    "id": section_id,
                    "title": strip_section_prefix(title),
                    "source_path": path,
                    "label": f"sec:{section_id.replace('.', '-')}",
                    "tex_path": REPO_ROOT / "正文" / "sections" / section_tex_name(section_id),
                }
        )
    return cards


def load_chapters() -> list[dict]:
    chapters = []
    for part in PARTS:
        if part["kind"] != "main":
            continue
        part_dir = SOURCE_ROOT / part["source_dir"]
        chapter_dirs = sorted(
            [path for path in part_dir.iterdir() if path.is_dir()],
            key=lambda p: int(re.match(r"第(\d+)章", p.name).group(1)),
        )
        for chapter_dir in chapter_dirs:
            match = re.match(r"第(\d+)章 (.+)", chapter_dir.name)
            number = int(match.group(1))
            title = match.group(2)
            chapters.append(
                {
                    "number": number,
                    "title": title,
                    "part_index": part["index"],
                    "part_title": part["title"],
                    "source_dir": chapter_dir,
                    "readme_path": chapter_dir / "README.md",
                    "label": f"chap:{number:02d}",
                    "tex_path": REPO_ROOT / "正文" / "chapters" / chapter_tex_name(number),
                    "sections": load_section_cards(chapter_dir),
                }
            )
    return chapters


def load_appendices() -> list[dict]:
    appendix_root = SOURCE_ROOT / "07-附录"
    appendices = []
    for path in sorted(appendix_root.glob("*/README.md")):
        code = re.match(r"附录([A-Z]) ", path.parent.name).group(1)
        title = parse_markdown_title(path.read_text(encoding="utf-8"))
        appendices.append(
            {
                "code": code,
                "title": strip_appendix_prefix(title),
                "source_path": path,
                "label": f"app:{code.lower()}",
                "tex_path": REPO_ROOT / "正文" / "appendices" / appendix_tex_name(code),
            }
        )
    return appendices


CHAPTERS = load_chapters()
APPENDICES = load_appendices()


def build_wikilink_map() -> dict[str, tuple[str, str]]:
    mapping: dict[str, tuple[str, str]] = {}
    for chapter in CHAPTERS:
        rel = chapter["readme_path"].relative_to(SOURCE_ROOT).as_posix()
        mapping[f"无穷维凸优化专著/{rel}"] = (chapter["label"], f"第{chapter['number']}章 {chapter['title']}")
        mapping[rel] = (chapter["label"], f"第{chapter['number']}章 {chapter['title']}")
        mapping[chapter["readme_path"].parent.name] = (chapter["label"], f"第{chapter['number']}章 {chapter['title']}")
        for section in chapter["sections"]:
            rel = section["source_path"].relative_to(SOURCE_ROOT).as_posix()
            title = f"{section['id']} {section['title']}"
            mapping[f"无穷维凸优化专著/{rel}"] = (section["label"], title)
            mapping[rel] = (section["label"], title)
            mapping[section["source_path"].stem] = (section["label"], title)
    root_readme = SOURCE_ROOT / "README.md"
    route_map = SOURCE_ROOT / "00-全书路线图与依赖图.md"
    mapping["无穷维凸优化专著/README.md"] = ("front:overview", "全书说明")
    mapping["README.md"] = ("front:overview", "全书说明")
    mapping["无穷维凸优化专著/00-全书路线图与依赖图.md"] = ("front:roadmap", "全书路线图与依赖图")
    mapping["00-全书路线图与依赖图.md"] = ("front:roadmap", "全书路线图与依赖图")
    for appendix in APPENDICES:
        rel = appendix["source_path"].relative_to(SOURCE_ROOT).as_posix()
        mapping[f"无穷维凸优化专著/{rel}"] = (appendix["label"], appendix["title"])
        mapping[rel] = (appendix["label"], appendix["title"])
        mapping[appendix["source_path"].parent.name] = (appendix["label"], appendix["title"])
    return mapping


WIKILINK_MAP = build_wikilink_map()


def escape_latex(text: str) -> str:
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "#": r"\#",
    }
    return "".join(replacements.get(char, char) for char in text)


def inline_to_latex(text: str) -> str:
    text = text.strip()
    if not text:
        return ""

    tokens: list[tuple[str, str]] = []

    def stash(kind: str, value: str) -> str:
        tokens.append((kind, value))
        return f"@@TOKEN{len(tokens) - 1}@@"

    def repl_wikilink(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        label = match.group(2).strip()
        mapped = WIKILINK_MAP.get(target) or WIKILINK_MAP.get(Path(target).stem)
        if mapped:
            return stash("raw", rf"\hyperref[{mapped[0]}]{{{escape_latex(label)}}}")
        return stash("text", label)

    text = re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", repl_wikilink, text)
    text = re.sub(r"`([^`]+)`", lambda m: stash("raw", rf"\texttt{{{escape_latex(m.group(1))}}}"), text)
    text = re.sub(r"\*\*([^*]+)\*\*", lambda m: stash("raw", rf"\textbf{{{escape_latex(m.group(1))}}}"), text)
    text = escape_latex(text)

    for idx, (kind, value) in enumerate(tokens):
        placeholder = escape_latex(f"@@TOKEN{idx}@@")
        replacement = escape_latex(value) if kind == "text" else value
        text = text.replace(placeholder, replacement)
    return text


def render_itemize(items: list[str]) -> str:
    lines = ["\\begin{itemize}"]
    for item in items:
        lines.append(f"  \\item {inline_to_latex(item)}")
    lines.append("\\end{itemize}")
    return "\n".join(lines)


def render_markdown_table(lines: list[str]) -> str:
    rows = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [inline_to_latex(cell.strip()) for cell in stripped.strip("|").split("|")]
        rows.append(cells)
    if len(rows) < 2:
        return ""
    header = rows[0]
    body = rows[2:]
    cols = " | ".join([">{\\raggedright\\arraybackslash}X"] * len(header))
    out = [rf"\begin{{tabularx}}{{\textwidth}}{{{cols}}}", r"\toprule"]
    out.append(" & ".join(header) + r" \\")
    out.append(r"\midrule")
    for row in body:
        out.append(" & ".join(row) + r" \\")
    out.append(r"\bottomrule")
    out.append(r"\end{tabularx}")
    return "\n".join(out)


def render_code_block(lines: list[str]) -> str:
    code = "\n".join(lines)
    return "\\begin{verbatim}\n" + code + "\n\\end{verbatim}"


def render_paragraphs(lines: list[str]) -> str:
    paragraphs: list[str] = []
    current: list[str] = []
    for line in lines:
        if not line.strip():
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        current.append(line.strip())
    if current:
        paragraphs.append(" ".join(current))
    return "\n\n".join(inline_to_latex(paragraph) for paragraph in paragraphs)


def extract_list_items(text: str) -> list[str]:
    return [line.lstrip()[2:].strip() for line in text.splitlines() if line.lstrip().startswith("- ")]


def render_introduction(items: list[str], title: str = "内容提要") -> str:
    body = "\n".join(f"  \\item {item}" for item in items if item.strip())
    return dedent(
        f"""\
        \\begin{{introduction}}[{title}]
        {body}
        \\end{{introduction}}
        """
    ).strip()


def render_named_paragraph(title: str, body: str) -> str:
    rendered = render_markdown_block(body)
    return dedent(
        f"""\
        \\paragraph{{{inline_to_latex(title)}}}

        {rendered}
        """
    ).strip()


def render_unnumbered_subsection(title: str, body: str) -> str:
    rendered = render_markdown_block(body)
    return dedent(
        f"""\
        \\subsection*{{{inline_to_latex(title)}}}

        {rendered}
        """
    ).strip()


def render_markdown_block(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    lines = text.splitlines()
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return render_code_block(lines[1:-1])
    if all((not line.strip()) or line.lstrip().startswith("- ") for line in lines):
        items = [line.lstrip()[2:].strip() for line in lines if line.strip()]
        return render_itemize(items)
    if any(line.strip().startswith("|") for line in lines):
        return render_markdown_table(lines)
    if any(line.startswith("### ") for line in lines):
        chunks: list[str] = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if not line.strip():
                i += 1
                continue
            if line.startswith("### "):
                chunks.append(rf"\paragraph{{{inline_to_latex(line[4:].strip())}}}")
                i += 1
                continue
            if line.lstrip().startswith("- "):
                items: list[str] = []
                while i < len(lines) and lines[i].lstrip().startswith("- "):
                    items.append(lines[i].lstrip()[2:].strip())
                    i += 1
                chunks.append(render_itemize(items))
                continue
            if line.strip().startswith("|"):
                table_lines: list[str] = []
                while i < len(lines) and lines[i].strip().startswith("|"):
                    table_lines.append(lines[i])
                    i += 1
                chunks.append(render_markdown_table(table_lines))
                continue
            paragraph_lines: list[str] = []
            while i < len(lines):
                current = lines[i]
                if not current.strip() or current.startswith("### ") or current.lstrip().startswith("- ") or current.strip().startswith("|"):
                    break
                paragraph_lines.append(current)
                i += 1
            if paragraph_lines:
                chunks.append(render_paragraphs(paragraph_lines))
                continue
            i += 1
        return "\n\n".join(chunk for chunk in chunks if chunk.strip())
    return render_paragraphs(lines)


def render_field(title: str, body: str, env: str = "bookfield", *, raw: bool = False) -> str:
    rendered = body.strip() if raw else render_markdown_block(body)
    return dedent(
        f"""\
        \\begin{{{env}}}{{{title}}}
        {rendered}
        \\end{{{env}}}
        """
    ).strip()


def render_section_card(section: dict) -> str:
    blocks = parse_heading_sections(section["source_path"].read_text(encoding="utf-8"), 2)
    exercise_blocks = parse_subsections(blocks["习题池"])
    intro_items = [
        f"\\textbf{{定位}}：{inline_to_latex(blocks['定位'].strip())}",
        f"\\textbf{{本节目标}}：{'；'.join(inline_to_latex(item) for item in extract_list_items(blocks['本节目标']))}",
        f"\\textbf{{先修依赖}}：{'；'.join(inline_to_latex(item) for item in extract_list_items(blocks['先修依赖']))}",
    ]
    pieces = [
        rf"\section{{{inline_to_latex(section['title'])}}}",
        rf"\label{{{section['label']}}}",
        render_introduction(intro_items),
        render_field("核心定义", blocks["核心定义"], env="definition"),
        render_field("核心定理", blocks["核心定理"], env="theorem"),
        render_named_paragraph("证明角色", blocks["证明角色"]),
        render_named_paragraph("直观解释", blocks["直观解释"]),
        render_field("抽象例子", blocks["抽象例子"], env="example"),
        render_field("具体例子", blocks["具体例子"], env="example"),
        render_unnumbered_subsection("Boyd 对应", blocks["Boyd 对应"]),
    ]
    exercise_body = "\n\n".join(
        "\n\n".join(
            [
            rf"\textbf{{{inline_to_latex(title)}}}",
            render_markdown_block(body),
            ]
        )
        for title, body in exercise_blocks.items()
    )
    pieces.append(
        dedent(
            f"""\
            \\begin{{exercise}}[习题池]
            {exercise_body}
            \\end{{exercise}}
            """
        ).strip()
    )
    pieces.append(render_named_paragraph("写作备注", blocks["写作备注"]))
    return "\n\n".join(pieces) + "\n"


def render_chapter_readme(chapter: dict) -> str:
    blocks = parse_heading_sections(chapter["readme_path"].read_text(encoding="utf-8"), 2)
    section_nav = "；".join(
        f"\\hyperref[{section['label']}]{{{section['id']} {section['title']}}}"
        for section in chapter["sections"]
    )
    intro_items = [
        f"\\textbf{{本章目录}}：{section_nav}",
        f"\\textbf{{本章总目标}}：{'；'.join(inline_to_latex(item) for item in extract_list_items(blocks['本章总目标']))}",
        f"\\textbf{{本章先修要求}}：{'；'.join(inline_to_latex(item) for item in extract_list_items(blocks['本章先修要求']))}",
    ]
    pieces = [
        rf"\chapter{{{inline_to_latex(chapter['title'])}}}",
        rf"\label{{{chapter['label']}}}",
        render_introduction(intro_items),
        render_field("本章核心定理链", blocks["本章核心定理链"], env="theorem"),
        render_field("本章例子主线", blocks["本章例子主线"], env="example"),
        render_unnumbered_subsection("本章 Boyd 映射总表", blocks["本章 Boyd 映射总表"]),
        render_field("本章习题索引表", blocks["本章习题索引表"], env="exercise"),
    ]
    for section in chapter["sections"]:
        pieces.append(rf"\input{{正文/sections/{section_tex_name(section['id'])}}}")
    return "\n\n".join(pieces) + "\n"


def render_frontmatter_overview() -> str:
    path = SOURCE_ROOT / "README.md"
    title = parse_markdown_title(path.read_text(encoding="utf-8"))
    blocks = parse_heading_sections(path.read_text(encoding="utf-8"), 2)
    pieces = [
        rf"\chapter*{{{inline_to_latex(title)}}}",
        r"\label{front:overview}",
        r"\addcontentsline{toc}{chapter}{全书说明}",
    ]
    for heading, body in blocks.items():
        pieces.append(render_unnumbered_subsection(heading, body))
    return "\n\n".join(pieces) + "\n"


def render_frontmatter_roadmap() -> str:
    path = SOURCE_ROOT / "00-全书路线图与依赖图.md"
    title = parse_markdown_title(path.read_text(encoding="utf-8"))
    blocks = parse_heading_sections(path.read_text(encoding="utf-8"), 2)
    pieces = [
        rf"\chapter*{{{inline_to_latex(title)}}}",
        r"\label{front:roadmap}",
        r"\addcontentsline{toc}{chapter}{全书路线图与依赖图}",
    ]
    for heading, body in blocks.items():
        pieces.append(render_unnumbered_subsection(heading, body))
    return "\n\n".join(pieces) + "\n"


def render_appendix(appendix: dict) -> str:
    blocks = parse_heading_sections(appendix["source_path"].read_text(encoding="utf-8"), 2)
    intro_items = [
        f"\\textbf{{定位}}：{inline_to_latex(blocks['定位'].strip())}",
        f"\\textbf{{与正文接口}}：{'；'.join(inline_to_latex(item) for item in extract_list_items(blocks['与正文接口']))}",
    ]
    pieces = [
        rf"\chapter{{{inline_to_latex(appendix['title'])}}}",
        rf"\label{{{appendix['label']}}}",
        render_introduction(intro_items),
    ]
    for heading, body in blocks.items():
        if heading in {"定位", "与正文接口"}:
            continue
        env = "definition"
        if heading == "收录范围":
            env = "definition"
        elif heading == "使用时机":
            env = "example"
        pieces.append(render_field(heading, body, env=env))
    return "\n\n".join(pieces) + "\n"


def render_part_file(part: dict) -> str:
    lines = [rf"\part{{{part['title']}}}"]
    if part["kind"] == "main":
        for chapter in [ch for ch in CHAPTERS if ch["part_index"] == part["index"]]:
            lines.append(rf"\input{{正文/chapters/{chapter_tex_name(chapter['number'])}}}")
    else:
        lines.append(r"\appendix")
        for appendix in APPENDICES:
            lines.append(rf"\input{{正文/appendices/{appendix_tex_name(appendix['code'])}}}")
    return "\n".join(lines) + "\n"


def render_book_tex() -> str:
    part_inputs = "\n".join(rf"\input{{正文/parts/{part_tex_name(part['index'])}}}" for part in PARTS)
    return part_inputs + "\n"


def render_main_tex() -> str:
    return dedent(
        """\
        \\documentclass[lang=cn,a4paper,newtx,section]{elegantbook}

        \\title{凸优化}
        \\logo{figure/logo-blue.jpg}
        \\cover{figure/cover.jpg}

        \\setcounter{tocdepth}{2}

        \\usepackage{array}
        \\usepackage{tabularx}
        \\usepackage{tikz-cd}
        \\usepackage{mathtools}

        \\begin{document}

        \\maketitle

        \\frontmatter
        \\tableofcontents
        \\input{正文/frontmatter-overview.tex}
        \\input{正文/frontmatter-roadmap.tex}

        \\mainmatter

        \\input{正文/book.tex}

        \\end{document}
        """
    ).strip() + "\n"


def expected_outputs() -> list[Path]:
    outputs = [
        REPO_ROOT / "main.tex",
        REPO_ROOT / "正文" / "book.tex",
        REPO_ROOT / "正文" / "frontmatter-overview.tex",
        REPO_ROOT / "正文" / "frontmatter-roadmap.tex",
    ]
    outputs.extend(REPO_ROOT / "正文" / "parts" / part_tex_name(part["index"]) for part in PARTS)
    outputs.extend(chapter["tex_path"] for chapter in CHAPTERS)
    outputs.extend(section["tex_path"] for chapter in CHAPTERS for section in chapter["sections"])
    outputs.extend(appendix["tex_path"] for appendix in APPENDICES)
    return outputs


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def generate() -> None:
    write(REPO_ROOT / "main.tex", render_main_tex())
    write(REPO_ROOT / "正文" / "book.tex", render_book_tex())
    write(REPO_ROOT / "正文" / "frontmatter-overview.tex", render_frontmatter_overview())
    write(REPO_ROOT / "正文" / "frontmatter-roadmap.tex", render_frontmatter_roadmap())
    for part in PARTS:
        write(REPO_ROOT / "正文" / "parts" / part_tex_name(part["index"]), render_part_file(part))
    for chapter in CHAPTERS:
        write(chapter["tex_path"], render_chapter_readme(chapter))
        for section in chapter["sections"]:
            write(section["tex_path"], render_section_card(section))
    for appendix in APPENDICES:
        write(appendix["tex_path"], render_appendix(appendix))
    print(
        f"generated parts={len(PARTS)} chapters={len(CHAPTERS)} sections={sum(len(ch['sections']) for ch in CHAPTERS)} appendices={len(APPENDICES)}"
    )


if __name__ == "__main__":
    generate()
