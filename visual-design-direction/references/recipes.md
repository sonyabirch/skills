# Recipes and starting points

Reference material for the visual-design-direction skill. None of this is a default to apply blindly; it's raw material to assemble from. The method in SKILL.md decides, and this gives you dependable parts and a few worked examples of the method in action.

## Typefaces by role

All of these are free (most are open-source, on Google Fonts or similar) unless noted, and durable, so none of them is a passing trend. Pick *one* and use it fully before reaching for a second.

**System stacks: free, instant, evergreen.** When neutrality, speed, or zero-loading matters more than character. They look native and never go out of style.
- Sans: `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`
- Mono: `ui-monospace, "SF Mono", "Cascadia Code", Menlo, monospace`

**Workhorse sans: the safe spine of most UI.** Neutral, legible at small sizes, wide weight range.
- *Inter.* The default for a reason: clean, huge weight range, excellent at UI sizes. Slightly overused, which is the only thing against it.
- *Source Sans 3.* Warmer and a touch more humanist than Inter; ages well.
- *IBM Plex Sans.* An engineered character that doesn't shout; pairs with its serif and mono siblings.
- *Public Sans* and *Libre Franklin.* Sturdy American-grotesque feel, good for institutional or civic work.

**Humanist / warmer sans: when the content is personal.** Softer terminals, more open shapes; reads friendlier without losing seriousness.
- *Hanken Grotesk*, *Figtree*, and *Mulish.* All warm, modern, and unobtrusive.

**Serif text: for reading and editorial weight.** Use when long-form text or a literary register matters.
- *Source Serif 4*, *Newsreader*, *Lora*, and *Bitter.* All hold up at body sizes on screen.

**Display / character: headings only, and sparingly.** These carry personality, so never set body in them.
- *Fraunces.* A "soft serif" with adjustable character; excellent for warm, expressive headings.
- *Space Grotesk.* Geometric, slightly offbeat, modern-technical.
- *Playfair Display.* High-contrast and elegant, but fragile at small sizes and easy to overuse.

**Mono: code, data, tabular figures, or a technical accent.**
- *JetBrains Mono*, *IBM Plex Mono*, *Space Mono* (more characterful), *Fira Code*.

**Pairing, if you must use two.** Contrast the roles rather than just the names: a characterful serif or display face for headings against a neutral workhorse sans for text (for example Fraunces + Inter, or Newsreader + Source Sans). Never pair two faces that do the same job, because two neutral sans-serifs just look like a loading bug.

## Worked directions

Four assembled directions, each shown the way the skill delivers: intent, then tokens. They illustrate how the pieces compose. Derive from the constraints in front of you, and don't copy these onto an unrelated problem.

### 1. Calm editorial: reading-forward content, blogs, docs, content apps
Intent: get out of the way of the words; feel considered and unhurried.
- **Neutrals:** warm-grey ramp (a hint of yellow in the greys). Background `#FAFAF8`, surface `#FFFFFF`, border `#E7E5E0`, muted text `#6B6862`, body `#33312D`, headings `#1A1916`.
- **Accent:** a single muted ink-blue `#2D4A6B` on links and the rare primary action. Semantics kept low-saturation.
- **Type:** one serif for headings plus a neutral sans for text (Newsreader + Source Sans), or a single humanist sans throughout. 1.2 scale, which is calm, with small jumps.
- **Spacing:** 8px base, airy. Generous line-height (1.6 body). Measure capped around 68ch.
- **Radius / shadow:** 4px radius, effectively no shadow. Separate with whitespace and the occasional hairline border.

### 2. Dense utilitarian: dashboards, data tables, internal tools
Intent: maximise information per screen while staying scannable; efficient, not cramped.
- **Neutrals:** cool-grey ramp. Background `#F8FAFC`, surface `#FFFFFF`, border `#E2E8F0`, muted `#64748B`, body `#1E293B`, headings `#0F172A`.
- **Accent:** one functional blue `#2563EB` for primary actions and active states, plus a *full* semantic set (green, amber, red) because status matters here.
- **Type:** one workhorse sans (Inter), tabular figures on for numeric columns. 1.2 scale; smaller steps tolerated because density is the point, but body stays ≥14px, ideally 16.
- **Spacing:** 4px base, compact. Tight but consistent row rhythm.
- **Radius / shadow:** 4px radius; prefer 1px borders over shadows to divide a busy surface. Reserve shadow for things that genuinely float (dropdowns, popovers).

### 3. Warm cultural: arts, events, community, anything human and expressive
Intent: feel alive and inviting without becoming loud or chaotic; character lives in the type, discipline lives in the colour.
- **Neutrals:** warm ramp, slightly creamier than editorial. Background `#FBF8F3`, surface `#FFFFFF`, border `#EAE3D8`, muted `#736B5E`, body `#322C24`, headings `#1C1813`.
- **Accent:** one confident brand hue (a deep teal `#1F6F6B` or a warm clay `#B5532A`) used on primary actions and key moments, plus its tints for backgrounds. One hue, not a carnival.
- **Type:** a characterful display face for headings (Fraunces) against a clean text sans (Hanken Grotesk). Let the headings carry the personality so that the colour can stay restrained.
- **Spacing:** 8px base, medium-airy. Room to breathe without feeling sparse.
- **Radius / shadow:** 8px radius for a softer, more welcoming feel; soft, low shadow on cards if you want a little lift.

### 4. Premium minimal: marketing sites, brand pages, considered product
Intent: confident, quiet, expensive-feeling; hierarchy through space and weight rather than through ornament.
- **Neutrals:** near-monochrome, high range. Background `#FFFFFF`, surface `#FAFAFA`, border `#EBEBEB`, muted `#737373`, body `#262626`, headings `#0A0A0A`.
- **Accent:** a single restrained colour, often used only on the primary action and otherwise near-absent, so that the monochrome and the type do the work.
- **Type:** one high-quality sans across many weights, or a characterful display combined with a neutral text face. Large scale jumps (1.333 to 1.5) so that a single hero heading dominates and everything else recedes.
- **Spacing:** 8px base, very generous. Large section padding, and lots of air between blocks. Space *is* the luxury signal here.
- **Radius / shadow:** small radius (0 to 4px) for a sharp, modern edge; one subtle layered shadow, used rarely. Motion minimal and smooth.

## Contrast cheat (WCAG)

- **AA (ship this):** 4.5:1 for normal text; 3:1 for large text (≥24px, or ≥19px / around 14pt bold) and for UI components, icons, and meaningful graphics.
- **AAA (stricter):** 7:1 normal, 4.5:1 large.
- Never rely on colour alone to carry meaning; back it with text, icon, or shape. Check states too, because a muted placeholder or a disabled label still has a contrast floor if it must be read.
- A visible focus indicator is a contrast requirement too, because the focus ring needs 3:1 against whatever sits behind it, or it can't be seen.

## Modular scale cheat

Pick a ratio and apply it from a 16px base. Round to whole pixels.
- **1.2 (minor third):** calm, small steps, lots of sizes close together: 16 → 19 → 23 → 28 → 33 → 40.
- **1.25 (major third):** comfortable, balanced: 16 → 20 → 25 → 31 → 39 → 49.
- **1.333 (perfect fourth):** confident, clear jumps: 16 → 21 → 28 → 38 → 50 → 67.
- **1.5 (perfect fifth):** dramatic, big gaps, few sizes: 16 → 24 → 36 → 54.

Tighter ratios suit dense or editorial work; wider ratios suit marketing and hero-led pages. Keep the set to six to eight steps and resist adding "just one more" size.
