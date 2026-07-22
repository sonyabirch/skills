# rumo

Design-system work for rumoconsulting.com. Not a rebuild, an extraction: measuring what the hand-written site already had, codifying it as a system, applying the system through Claude Design, and shipping a Python script that verifies the result rather than trusting it. Four artefacts, in reading order.

**[design-system-audit.md](design-system-audit.md).** The narrative account. Start here for the story of the audit and the surprises the verification script surfaced afterwards.

**[rumo-design-system.md](rumo-design-system.md).** The system itself. Fourteen-step neutral ramp anchored at hue 45. Seven-step type scale. Eleven-step spacing scale on a 4px base. Four-size square vocabulary in four states. Every value is either kept from the existing site or derived to fill a specific gap in it.

**[claude-design-brief.md](claude-design-brief.md).** The brief handed to Claude Design to apply the system. Contains the preserve list of small hard-won details that had to survive the rewrite, the four broken things that had to be fixed, and the output contract.

**[check-rumo.py](check-rumo.py).** Python 3, standard library only. Runs against a deployed bundle and reports pass or fail against the palette, type scale, spacing scale, required states, contrast pairs, canvas colour constants, preserve list, architecture, and internal links. This is the file that turned out to matter more than the design system itself.

More on [sonyabirch.com](https://sonyabirch.com).
