# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Instructions for making a good slide (MUST FOLLOW)
- Use Ultrathink

- If you are required to make literature review on several paper, first search over
the internet to find the corresponding reference, if you are not sure which literature
is referred to, PLEASE CHECK WITH THE HUMAN USER to make sure you are reviewing the
correct reference. 

- After all references are confirmed, you can download them locally
in the references/ directory. Make sure to use those good figures or pseudocodes block
in the paper in your review if they are very informative and illustrate the essence of
the paper.

- Be precise in each slide, do not include too much equations or statements which is
hard for audience to follow. Figure and table are much better illuetrator.

- Highlight (boldface or diff colors) the part you want to emphasize

- After generating the slide, ask code reviewer or architecture to review the slide
to check if the logic flow and the details are explained clearly

- Make sure you have resolved all the latex compilation error before you hand in the the
human user

## Repository Overview

This is a LaTeX-based academic presentation repository containing slides for research talks, job interviews, and paper reviews. The repository uses Beamer for presentations with a custom style file (`essay-def.sty`).

## Build Commands

### Compiling LaTeX Presentations
```bash
# For any .tex file in a presentation directory:
cd "<presentation_directory>"
pdflatex main.tex

# For complete compilation with references (if needed):
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

### Common LaTeX Operations
- **Quick compile**: `pdflatex main.tex`
- **Clean auxiliary files**: `rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.synctex.gz`
- **View compilation errors**: Check the `.log` file in the same directory

## Project Structure

The repository follows a consistent structure where each presentation topic has its own directory containing:
- `main.tex` - The main LaTeX source file
- `essay-def.sty` - Common style definitions (copied per directory)
- `fig/` - Directory containing figures and images
- Generated PDF output (usually named after the date or topic)

Key directories:
- `paper slide/` - Academic paper presentations
- `review slide/` - Literature review presentations
- `job/` - Job interview presentations
- `LLM_dynamics/`, `Scientific ML/` - Topic-specific presentations

## Working with LaTeX Slides

When editing presentations:
1. Each slide directory is self-contained with its own copy of `essay-def.sty`
2. Beamer presentations use `\begin{frame}...\end{frame}` for individual slides
3. Common packages are already imported in the template
4. Figures should be placed in the `fig/` subdirectory of each presentation

## Special Considerations

- The repository uses `aspectratio=169` for widescreen presentations
- Custom colors and styles are defined in individual `.tex` files
- Some presentations may have associated `.bbl` files for bibliography
- The `.cursor/rules/` directory contains specific editing guidelines that should be followed when modifying slides