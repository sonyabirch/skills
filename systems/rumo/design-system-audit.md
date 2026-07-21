# Extracting a design system from a site that already existed

I have been running rumoconsulting.com as hand-written static HTML with a single stylesheet since launch. No framework, no build step, one CSS file. The look was fine. What it did not have was a system, and the difference between those two things turned out to be measurable.

## What was actually there

I started by measuring rather than redesigning, because a live site that looks coherent can still be held together by nothing but consistent taste. The 387-line stylesheet contained:

- 17 distinct hex values, of which 10 were written inline rather than as tokens. Two of them, `#4A4A46` and `#4A4A44`, sat 0.4% apart in lightness and existed only because they were picked separately on different days.
- 34 distinct pixel values across `gap`, `padding` and `margin`. Roughly half sat on a 4px grid and the rest sat two pixels off it, which makes the effective grid 2px, which is the same as no grid.
- 12 font sizes, including 14.5px and 15.5px. Half-pixel type sizes are the fingerprint of choosing by eye.
- Three near-identical box shadows.
- Zero `disabled` rules and zero `invalid` rules across the entire file.

One thing was completely consistent: ten `border-radius` declarations, all zero. That turned out to be the only part of the visual language that had been decided rather than accumulated.

## The failures that were not visible

Measuring contrast ratios rather than looking at them changed what I found. Four things were broken in ways that reading the page would not surface:

The "read more" link on project cards was ink at rest and turned chartreuse on hover, going from 18.73:1 to 1.96:1. Hovering it made it unreadable, at exactly the moment of interaction.

The main navigation had no visible hover state at all. The only signal was a chartreuse underline measuring 1.22:1 against the paper background, which is invisible. The nav had been shipping without hover feedback since launch and I had never noticed, because I knew where the links were.

Contact form fields had a 1.36:1 border sitting on a surface that was 1.10:1 against the section behind it, so nothing marked where to type.

Method step numbers were 2.97:1 on the tinted sections, below the 4.5:1 floor for small text.

The pattern underneath all four: the accent colour was being used as both a fill and a foreground. Ink on chartreuse measures 14.41:1. Chartreuse on paper measures 1.22:1. That asymmetry is the whole rule, and once stated as "the accent is a fill and a marker, never an ink and never a hairline", three of the four failures resolve at once.

## Building the system

The ramp went from six neutrals to fourteen steps, hue held at 45 throughout, with five of the existing values kept unchanged so the site would not visibly shift. Every one of the ten inline hex values resolved to a step. Type went to seven fixed sizes plus two clamped headings. Spacing went to eleven steps on a 4px base. The four square sizes that carry the brand's visual vocabulary went from eight ad-hoc values to four tokens.

The tokens were generated in Claude Design from a written spec and then verified against it programmatically, all eighteen colour values checked by script rather than by eye. The CSS rewrite was also done in Claude Design. The specification, the contrast measurement and the verification were mine.

## The part that mattered more than the system

I wrote a checker. About 250 lines of Python, standard library only, that takes a deployed bundle and reports whether every hex resolves to a token, whether spacing sits on the scale, whether the required states exist, whether specific contrast pairs pass, whether the fragile things survived the rewrite, and whether the architecture is intact.

The fragile things were the point. Netlify form attributes, JSON-LD blocks, tuned scroll offsets, four `prefers-reduced-motion` blocks, and a canvas script that carries its own hardcoded copies of three colours instead of reading them from CSS. These are invisible in a rendered page and expensive to notice missing.

Then the checker found things my own audit had not.

Open Graph tags existed on three of nine pages. JSON-LD existed on one. No page had a canonical link. So six pages were sharing to LinkedIn as a bare URL, which I had not once checked in a year of running the site.

The primary call to action on the projects page pointed at `/demo/`, a directory that does not exist. The single button on the site that shows the work I do had been returning a 404, and I had never clicked it because I knew what was behind it.

Two files, `projects.html` and `projects/index.html`, both claimed the URL `/projects`. One was a superseded draft, identifiable because its navigation predated a submenu the other had.

None of these are subtle. All of them survived a careful manual review and a written audit, and were caught in under a second by a script that does nothing cleverer than resolve paths and compare strings.

## What the checker got wrong

It reported four failures that were not failures. It counted hex values inside CSS comments, read `border-radius: var(--radius)` as non-zero when `--radius` is zero, did not recognise `:user-invalid` because it was matching on `:invalid`, and flagged the form's thank-you page as unreachable because it is reached through a form `action` rather than an `href`.

The lesson I would take from that is not that the tool is unreliable. It is that a check which cannot come back negative is a ritual, and a check that comes back negative wrongly is at least visible enough to fix. The four false positives took ten minutes. The three real bugs would have stayed on the live site indefinitely.

## Where it ended up

Of the twenty failures in the original bundle, fifteen are fixed. The remaining five are a task not yet started (per-page head tags on six pages), one deferred cosmetic (the brand lockup keeps a 17px size that is off the type scale), and mobile spacing inside media queries that I chose not to touch in the same pass because it carries layout-regression risk.

The stylesheet is 363 lines, down from 387, and does more than it did.

The thing I would not have predicted going in: the value of a design system is not the document. It is that afterwards, adding an off-palette colour becomes a check that fails in one second, where before it was a hex value that worked.
