#!/usr/bin/env python3
"""Render PAPER.md into the canonical Hermes Labs LaTeX/PDF format."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "PAPER.md"
TEX = ROOT / "PAPER.tex"
PDF = ROOT / "PAPER.pdf"

TITLE = (
    "Precise Records, Unstable Meanings:\\\\"
    "Measurement Validity and Unsupported Claims\\\\"
    "Derived from AI Agent Telemetry"
)
METADATA_TITLE = (
    "Precise Records, Unstable Meanings: Measurement Validity and "
    "Unsupported Claims Derived from AI Agent Telemetry"
)
METADATA_SUBJECT = (
    "A twelve-week naturalistic audit of measurement validity and "
    "unsupported claims derived from AI agent telemetry."
)
METADATA_KEYWORDS = (
    "AI agent telemetry; measurement validity; construct validity; agent "
    "evaluation; operational telemetry; telemetry provenance; agent "
    "observability; coding agents; Telemetry-to-Claim Gate"
)

PREAMBLE = r"""\documentclass[12pt]{article}
\pdfinfoomitdate=1
\pdfsuppressptexinfo=15
\pdftrailerid{}
\pdfobjcompresslevel=0
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage{titlesec}
\titleformat{\section}{\large\mdseries}{\thesection}{1em}{}
\titleformat{\subsection}{\normalsize\mdseries}{\thesubsection}{1em}{}
\titleformat{\subsubsection}{\normalsize\mdseries\itshape}{\thesubsubsection}{1em}{}
\usepackage{geometry}
\geometry{margin=1in}
\usepackage[hidelinks]{hyperref}
\hypersetup{
  pdftitle={__METADATA_TITLE__},
  pdfauthor={Rolando Bosch},
  pdfsubject={__METADATA_SUBJECT__},
  pdfkeywords={__METADATA_KEYWORDS__},
  pdflang={en}
}
\pdfcatalog{/Lang (en)}
\usepackage{url}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{calc}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{caption}
\usepackage[round]{natbib}
\newcounter{none}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcolumntype{R}[1]{>{\raggedleft\arraybackslash}p{#1}}
\setlength{\emergencystretch}{3em}
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}
\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\renewenvironment{abstract}
  {\par\small\begin{center}\bfseries\abstractname\end{center}\vspace{-0.45em}}
  {\par\normalsize}

\newgeometry{top=0.72in,bottom=0.72in,left=0.84in,right=0.84in}
\title{__TITLE__}
\author{Rolando Bosch\\
Hermes Labs --- San Francisco, California, USA\\
\href{mailto:roli@hermes-labs.ai}{\texttt{roli@hermes-labs.ai}}}
\date{July 30, 2026}

\begin{document}
\maketitle
"""


def pandoc(markdown: str) -> str:
    result = subprocess.run(
        [
            "pandoc",
            "--from=gfm+pipe_tables",
            "--to=latex",
            "--wrap=none",
        ],
        input=markdown,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def shift_and_clean_headings(markdown: str) -> str:
    output: list[str] = []
    for line in markdown.splitlines():
        match = re.match(r"^(#{2,4})\s+(?:\d+(?:\.\d+)*\.?\s+)?(.+)$", line)
        if match:
            hashes, title = match.groups()
            output.append(f"{hashes[1:]} {title}")
        else:
            output.append(line)
    return "\n".join(output).strip() + "\n"


def format_tables(tex: str) -> str:
    old = r"\begin{longtable}[]{@{}lll@{}}"
    new = (
        r"\footnotesize"
        "\n"
        r"\begin{longtable}[]{@{}L{0.30\textwidth}"
        r"L{0.49\textwidth}L{0.15\textwidth}@{}}"
    )
    if old not in tex:
        raise ValueError(f"expected generated table signature is missing: {old}")
    tex = tex.replace(old, new, 1)
    tex = tex.replace(
        r"\textbf{USABLE\_WITH\_CAVEATS}",
        r"\textbf{USABLE\_\allowbreak WITH\_\allowbreak CAVEATS}",
    )
    tex = tex.replace(
        r"\texttt{claim\_class=retrieved}",
        r"\texttt{claim\_\allowbreak class=\allowbreak retrieved}",
    )
    return tex


def split_source(text: str) -> tuple[str, str, str]:
    author_note_marker = (
        "## Author's Note on Method, Authorship, and AI-Mediated Research\n"
    )
    abstract_marker = "## Abstract\n"
    introduction_marker = "## 1. Introduction\n"
    if (
        abstract_marker not in text
        or author_note_marker not in text
        or introduction_marker not in text
    ):
        raise ValueError("PAPER.md does not contain the expected section markers")
    _, after_note = text.split(author_note_marker, 1)
    author_note, after_abstract = after_note.split(abstract_marker, 1)
    abstract, body = after_abstract.split(introduction_marker, 1)
    return abstract.strip(), author_note.strip(), introduction_marker + body


def compile_pdf() -> None:
    command = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        TEX.name,
    ]
    for _ in range(2):
        subprocess.run(
            command,
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
    log = TEX.with_suffix(".log")
    log_text = log.read_text(encoding="utf-8", errors="replace")
    if "Overfull \\hbox" in log_text or "Overfull \\vbox" in log_text:
        raise RuntimeError("LaTeX reported an overfull box; inspect PAPER.log")
    if not PDF.exists() or PDF.stat().st_size == 0:
        raise RuntimeError("pdflatex did not produce PAPER.pdf")
    for suffix in (".aux", ".out"):
        build_file = TEX.with_suffix(suffix)
        if build_file.exists():
            build_file.unlink()


def main() -> None:
    abstract_md, author_note_md, body_md = split_source(
        SOURCE.read_text(encoding="utf-8")
    )
    body_md = shift_and_clean_headings(body_md)
    tex = (
        PREAMBLE.replace("__TITLE__", TITLE)
        .replace("__METADATA_TITLE__", METADATA_TITLE)
        .replace("__METADATA_SUBJECT__", METADATA_SUBJECT)
        .replace("__METADATA_KEYWORDS__", METADATA_KEYWORDS)
    )
    tex += "\n\\thispagestyle{empty}\n"
    tex += "\\renewcommand{\\abstractname}{Abstract}\n"
    tex += "\\begin{abstract}\n"
    tex += "\\setlength{\\parskip}{0.25em}\n"
    tex += (
        "\\begin{list}{}{\\setlength{\\leftmargin}{0.30in}"
        "\\setlength{\\rightmargin}{0.30in}}\\item[]\n"
    )
    abstract_tex = pandoc(abstract_md)
    abstract_tex = abstract_tex.replace(
        "\n\n\\textbf{Keywords:}",
        "\n\n\\vspace{0.35em}\\noindent\\textbf{Keywords:}",
    )
    tex += abstract_tex
    tex += "\n\\end{list}"
    tex += "\n\\end{abstract}\n\n"
    tex += "\\clearpage\n"
    tex += "\\restoregeometry\n"
    tex += "\\setcounter{page}{1}\n"
    tex += "\\renewcommand{\\abstractname}{Author's Note on Method, Authorship, and AI-Mediated Research}\n"
    tex += "\n\\begin{abstract}\n"
    tex += pandoc(author_note_md)
    tex += "\n\\end{abstract}\n\n"
    tex += "\\vspace{0.75em}\n\n"
    tex += format_tables(pandoc(body_md))
    tex += "\n\n\\end{document}\n"
    TEX.write_text(tex, encoding="utf-8")
    compile_pdf()
    print(f"WROTE {TEX}")
    print(f"WROTE {PDF}")


if __name__ == "__main__":
    main()
