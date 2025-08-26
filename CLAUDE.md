# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Instructions for making a good slide (MUST FOLLOW!!!)

- **Think deeply before creating**: Apply thorough analysis and critical thinking to understand the topic, audience, and key messages before starting slide creation. Consider the logical flow and main takeaways.

- **Literature review workflow**: 
  - When tasked with reviewing multiple papers, use web search to identify and locate the specific references
  - If paper titles or authors are ambiguous, **ALWAYS confirm with the human user** which exact papers to review before proceeding
  - Download confirmed references to the local `references/` directory
  - Extract key figures, algorithms, or pseudocode blocks that clearly illustrate the paper's main contributions
  - Prioritize visual elements that demonstrate the essence of each paper's methodology or results

- **Content precision guidelines**:
  - Limit each slide to 1-3 key points maximum
  - Prefer figures, diagrams, and tables over dense text or complex equations
  - If equations are necessary, break them into digestible components across multiple slides
  - Use bullet points with clear, concise statements (maximum 2 lines per bullet)
  - Ensure each slide can be understood in 60-90 seconds

- **Visual emphasis strategies**:
  - Use **bold text** for key terms and critical findings
  - Apply color highlighting (red, blue, or green) to emphasize important results or differences
  - Use consistent formatting throughout the presentation
  - Highlight no more than 2-3 elements per slide to avoid visual overload

- **Quality assurance process**:
  - After completing the slides, compile with `pdflatex` to check for errors
  - Make sure there is **NO Latex compilation error** and **pdf slide aligns well with the source code**
  - Review the generated PDF for logical flow and clarity
  - **Ask the human user to review** the completed slides for technical accuracy and presentation flow
  - Address any feedback before final delivery

- **Technical requirements**:
  - Resolve all LaTeX compilation errors before submission
  - Ensure all figures display properly and are properly referenced
  - Verify that all citations and references are correctly formatted
  - Test that the PDF renders correctly on different viewers

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