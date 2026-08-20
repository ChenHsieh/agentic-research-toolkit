---
name: tikz-figures
description: >
  Build publication-quality figures with TikZ/pgfplots - manuscript figures whose fonts must
  match the body text, pipeline and architecture schematics, or any figure that should
  regenerate from a data file instead of being redrawn by hand. Routes to a reusable template
  directory rather than writing pgfplots boilerplate from scratch, and front-loads the failure
  modes that produce silently wrong figures. Trigger on "TikZ", "pgfplots", "LaTeX figure",
  "make a schematic/flowchart/pipeline diagram", "vector figure for the manuscript",
  "figure fonts don't match the paper", or pdflatex compile errors in a figure.
allowed-tools: Read Write Edit Bash Glob
---

# TikZ / pgfplots figures

**Work from a template directory. Do not write pgfplots boilerplate from scratch** — every
figure in a manuscript should share one preamble, one build rule, and one visual language.

Two things TikZ gives you that a plotting library does not: vector output whose fonts are
*identical* to the manuscript body text, and a figure that regenerates from a data file
when the analysis changes. If you need neither, use matplotlib and move on.

---

## Step 0 — find or create the template directory

Look for an existing one first. Common locations, and whatever the project's own docs name:

```bash
ls "${TIKZ_TEMPLATES:-$HOME/tikz}" 2>/dev/null || ls ./figures ./tex 2>/dev/null
```

If one exists, **copy the closest template**, rename it `fig_<name>.tex`, point it at a new
`data/<name>.dat`, and run `make`. If none exists, bootstrap the layout below once — it pays
for itself at the second figure.

```
tikz/
  preamble.tex       shared packages + style; edit here to restyle every figure at once
  Makefile           per-figure dependencies, PDF and PNG targets
  data/              one .dat per figure, written by the analysis
  fig_scatter.tex    xy + least-squares fit
  fig_bars.tex       grouped bars with error bars
  fig_heatmap.tex    matrix + colorbar
  fig_flow.tex       pipeline schematic (no data file)
```

`preamble.tex` — the minimum that avoids the failure modes below:

```latex
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{pgfplotstable}   % required for linear regression; pgfplots alone is not enough
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta, positioning, shapes.geometric}
% Uncomment once the manuscript has more than ~5 figures:
% \usepgfplotslibrary{external}\tikzexternalize
\pgfplotsset{
  every axis/.append style={
    tick align=outside, tick pos=left,
    label style={font=\small}, tick label style={font=\footnotesize},
    legend style={draw=none, fill=none, font=\footnotesize},
  },
}
```

`Makefile` — rebuild only what changed:

```make
TEX  := $(wildcard fig_*.tex)
PDF  := $(TEX:.tex=.pdf)
PNG  := $(TEX:.tex=.png)
# Keep font caches off a quota-limited $HOME. TMPDIR is unset on most Linux
# systems, and make folds trailing whitespace into a variable, so no inline comments here.
TMPDIR ?= /tmp
export TEXMFVAR := $(TMPDIR)/texmfvar

all: $(PDF)
png: $(PNG)

%.pdf: %.tex preamble.tex $(wildcard data/*.dat)
	pdflatex -interaction=nonstopmode -halt-on-error $<

%.png: %.pdf
	pdftoppm -png -r 300 -singlefile $< $*

clean:
	rm -f *.aux *.log *.pdf *.png
.PHONY: all png clean
```

Each `fig_*.tex` is a `standalone` document that inputs the shared preamble:

```latex
\documentclass[border=2pt]{standalone}
\input{preamble}
\begin{document}
\begin{tikzpicture}
  \begin{axis}[xlabel={Predicted}, ylabel={Observed}]
    \addplot[only marks, mark size=1.2pt] table[x=pred, y=obs] {data/scatter.dat};
    \addplot[thick] table[y={create col/linear regression={y=obs}}] {data/scatter.dat};
  \end{axis}
\end{tikzpicture}
\end{document}
```

## Step 1 — build

```bash
make          # PDFs; rebuilds only figures whose .tex, .dat, or preamble changed
make png      # 300 dpi rasters for slides, or for showing the user
make clean
```

Compiles run on the order of a second per figure, so building interactively is fine.
Only submit a batch job if rendering hundreds of figures in a loop.

## Step 2 — keep the figure data-driven

The `.tex` reads `data/*.dat` at compile time. Have the analysis write a tab-separated file
with a header row, and the figure regenerates on `make` with **no edit to plotting code**.
Numbers that appear in the figure but not in a `.dat` — a hand-typed n, an annotation, a
threshold line — are the ones that go stale silently when the analysis is rerun. Push them
into the data file or into a macro defined next to it.

## Step 3 — verify the figure against the data

A TikZ figure that compiles cleanly can still be wrong. Before it goes in the manuscript:

- **Compare the rendered axis limits to the actual data range.** Most silent errors show up
  here first.
- **Count the marks, bars, or cells** against the number of rows in the `.dat`. See failure
  mode 1 — a dropped row is invisible.
- **Read the PNG yourself.** Do not report a figure as done on the strength of exit code 0.
- **Check units and orders of magnitude in the axis labels** against the source. A unit slip
  survives every downstream step, because the plot still looks fine.

---

## Failure modes — check these before believing a figure

1. **`surf, shader=flat corner` silently drops the last row and column.** A 12×12 matrix
   renders as 11×11, with no warning, and looks perfectly valid. Use
   `\addplot[matrix plot*, point meta=explicit]` with `table[...,meta=v]` instead, and
   verify the axis limits match the data extent.
2. **`create col/linear regression` needs `\usepackage{pgfplotstable}` explicitly.** Loading
   `pgfplots` alone fails with "Please load \usepackage{pgfplotstable}".
3. **`nodes near coords` collides with error bar caps** — labels get clipped. Use
   `nodes near coords style={yshift=6pt}`, or drop one of the two.
4. **`symbolic x coords` must exactly match column 1 of the `.dat`.** A mismatch gives an
   empty axis, not an error.
5. **Beyond roughly 5k scatter points**, pdfTeX gets slow and can hit memory limits. Thin the
   data before writing the `.dat`, or rasterize that layer.
6. **Past ~5 figures, enable `\usepgfplotslibrary{external}`** so a full build stops
   recompiling every figure every time.
7. **Font cache writes can blow a quota.** On a cluster or any quota-limited `$HOME`, point
   `TEXMFVAR` at scratch or `$TMPDIR` (the Makefile above does this).
8. **Pin the TeX distribution.** `module load texlive/<version>` or an equivalent lockfile —
   defaults drift, and a pgfplots major version bump changes rendering.

## Showing figures to the user

A headless node or remote shell has no image viewer (`DISPLAY` unset, no `imgcat`/`feh`).
Run `make png` and `Read` the PNG — it renders in the user's client. For a contact sheet:
`pdfjam --nup 2x2 --landscape --outfile all.pdf fig_*.pdf`.

## When NOT to use TikZ

- **Exploratory plotting.** Iteration is far slower than matplotlib. Prototype in matplotlib;
  switch to its `pgf` backend or port to a template only for the final figure.
- **Document and report layout.** TikZ is for figures. Use an HTML→PDF tool (weasyprint,
  Typst, or LaTeX proper) for the surrounding document.
- **Anything with a raster component** — microscopy, gels, screenshots. Composite those in
  the document, or place the image inside a TikZ overlay only for annotation.

---

**Cluster-specific setup** — module names, template directory paths, scratch locations, and
per-account shell quirks are deliberately left out of this skill. For a worked HPC example,
see [`sapelo2-boilerplate`](https://github.com/ChenHsieh/sapelo2-boilerplate).
