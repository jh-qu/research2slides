# research2slides — Project Context

## Purpose

A workflow for researching trending AI GitHub repos and producing
technical slide decks that help colleagues, managers, and enterprises
decide whether to adopt a tool.

## Workflow stages

1. **Source gathering** — collect the subject repo, related articles,
   and tool-generated analyses
2. **Analysis** — extract architecture, key concepts, strengths/limits,
   and adoption signals from source material
3. **Slide authoring** — Claude Code generates a Slidev deck in
   markdown, structured for a technical decision-making audience
4. **Review** — human reviews deck for accuracy and framing before
   sharing

## Glossary

| Term | Definition |
|------|-----------|
| **Subject repo** | The GitHub repository being researched |
| **Source material** | All inputs for a research run: the subject repo, analysis tool outputs, and reference articles |
| **Analysis tool** | External tool used to parse a GitHub repo (gitDiagram, gitIngest, DeepWiki, understand-anything, etc.) |
| **Slide deck** | The final Slidev presentation produced for a subject repo |
| **Adoption signal** | Evidence in the source material that suggests a tool is or isn't suitable for enterprise use |
| **Research run** | One end-to-end execution of the workflow for a single subject repo |

## Technology choices

- **Slides**: Slidev (markdown-based; Claude Code authors the `.md` files)
- **GitHub analysis**: gitDiagram, gitIngest, DeepWiki, understand-anything
- **Issue tracker**: GitHub Issues (see `docs/agents/issue-tracker.md`)

## Out of scope

- General-purpose slide creation unrelated to AI tool evaluation
- Deep code contribution to subject repos
