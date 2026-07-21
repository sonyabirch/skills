# skills

Reusable text-format artefacts I use in my own work. Five [SKILL.md](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) files for Claude and Claude-compatible tools, plus a design-system extraction case study with the supporting script.

Fuller writeups for each item live at [sonyabirch.com/library](https://sonyabirch.com/library), where the pieces get the story and voice a folder listing can't.

## Skills

Written in the SKILL.md open format. Usable in Claude Code, Claude.ai, the Claude API, and Claude-compatible tools including Codex, Cursor, Gemini CLI, Antigravity and Windsurf.

- [`brand-naming/`](brand-naming/): voice and judgment of a senior brand manager who names things and defends the choice.
- [`pm-feature-audit/`](pm-feature-audit/): senior delivery lead auditing whether a project-management tool has the feature set to actually run projects.
- [`uiux-design-critique/`](uiux-design-critique/): senior UI/UX designer giving an opinion-led read on an interface or a screen.
- [`ux-functional-audit/`](ux-functional-audit/): senior UX designer running a thorough functional sweep of a product.
- [`visual-design-direction/`](visual-design-direction/): senior visual designer choosing and defending the look of a product.

Four of the five ship with a `references/` subfolder that the SKILL.md loads at the right point in its process. Publishing only the top-level file breaks the skill.

## Systems

Design-system work with the artefacts that made it checkable.

- [`systems/rumo/`](systems/rumo/): extraction and codification of a design system for rumoconsulting.com. Includes the spec, the Claude Design brief, a Python verification script, and the write-up of the process.

## Installing a skill

Clone and copy the folder into your agent's skills directory (Claude Code shown):

```
git clone https://github.com/sonyabirch/skills.git
cp -r skills/brand-naming ~/.claude/skills/
```

Outside Claude, each SKILL.md is a Markdown document you can read and adapt into your own workflow.

## Licence

Apache 2.0. Fork freely; keep the [LICENSE](LICENSE) file with what you take.
