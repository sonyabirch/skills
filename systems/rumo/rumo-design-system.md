# Rumo design system

Version 1, extracted from `rumo.css` (387 lines) and the nine deployed HTML files. Every value below is either kept from the existing site or derived to fill a gap in it. Nothing here replaces the visual direction; it regularises what is already there.

---

## What the site already gets right

Name these first so nobody optimises them away.

**Radius is zero, everywhere, with no drift.** Ten `border-radius` declarations in the file, all `0`. That consistency is the spine of the look and the thing that makes the square vocabulary read as deliberate rather than incidental.

**The focus ring is designed, not defaulted.** `2px solid ink` at `3px` offset, overridden to chartreuse on the dark contact section so it stays visible there. Most sites either remove the ring or leave the browser default.

**Reduced motion is handled in four places**: the global CSS block, the status dot, the back-to-top button, and the hero canvas script. That is thorough.

**The secondary text colour is well chosen.** `#5C5B55` on paper measures 6.42:1, comfortably above the 4.5:1 floor, and still reads as clearly softer than the primary ink.

**The square in four states is the brand.** Filled ink, hollow, stone, chartreuse. It does semantic work across four problem cards, four method steps, the work-points list, the fit-check list and the hero canvas. This is more distinctive than the paper-and-hairlines substrate it sits on, and it is what a visitor will actually remember.

One piece of honest context on that last point. Warm off-white background, zero radius, hairline rules and a single acid accent is a combination that has become a recognisable house style, and a visitor who reads a lot of design-forward B2B sites has seen it. What separates this site from that pattern is the square system and the sorting animation, neither of which is generic. The design work should therefore lean further into the squares rather than further into the paper.

---

## Root causes

Five problems, four causes. Fixing the causes retires the symptoms.

**Cause 1: six neutrals doing the work of a fourteen-step ramp.** The palette defines `paper`, `paper-2`, `ink`, `ink-2`, `stone` and `mist`. Any value that is not one of those six was written as a literal hex, and there are now ten of them scattered through the file (`#A8A69E`, `#76746D`, `#4A4A46`, `#4A4A44`, `#34342F`, `#2C2C29`, `#1C1C1A`, `#000`, plus `#fff` eight times and `#8C8C86` duplicating `--stone`). Two of them, `#4A4A46` and `#4A4A44`, are 0.4% apart in lightness and exist only because they were picked separately on different days.

The ramp also drifts in hue. The light end sits at hue 43 to 48 and reads warm. The dark end sits at hue 60 and reads olive. `#121212` is hue 0 at zero saturation, a pure neutral black with no warmth at all. And there is a 24-point lightness hole between `mist` at 88% and `#A8A69E` at 64%, which is exactly where a visible border or a disabled surface would live.

**Cause 2: no type scale, so sizes were chosen by eye.** Twelve distinct sizes: 12, 13, 14, 14.5, 15, 15.5, 16, 17, 18, 19, 20 and 22. The half-pixel values are the fingerprint of ad-hoc choice.

**Cause 3: no spacing unit.** Thirty-four distinct pixel values across `gap`, `padding` and `margin`. Roughly half sit on a 4px grid and the rest sit two pixels off it, which makes the effective grid 2px, which is the same as no grid.

**Cause 4: chartreuse is treated as a colour rather than as a fill.** Ink on chartreuse measures 14.41:1. Chartreuse on paper measures 1.22:1. The accent is excellent as a background and unusable as a foreground, and the site currently does both.

---

## Verified failures

Measured, not estimated. Each ratio computed from the hex values in the file.

| Where | Pair | Ratio | Needs | Effect |
|---|---|---|---|---|
| Projects card, hover | `#9DC81A` on `#fff`, 13px | **1.96:1** | 4.5:1 | The "read more" link goes from 18.73:1 to near-invisible when you hover it. Hover makes it harder to read. |
| Nav links, hover | `#C6F235` on paper, 2px rule | **1.22:1** | 3:1 | The underline is the only hover signal on the main nav, and it cannot be seen. The nav effectively has no hover state. |
| Contact form fields | `#34342F` border on `#1C1C1A` | **1.36:1** | 3:1 | The field boundary is invisible. |
| Contact form fields | `#1C1C1A` surface on `#121212` section | **1.10:1** | 3:1 | The field surface is invisible too, so nothing marks where to type. |
| Method step numbers | `#8C8C86` on `#F3F0E8`, 12px | **2.97:1** | 4.5:1 | Fails on the tinted sections. |
| FAQ plus and minus | `#8C8C86` on `#fff` | 3.38:1 | 3:1 as UI | Passes as a control, fails as text. Acceptable because the summary text sits beside it. |
| Contact fine print | `#76746D` on ink, 13px | **4.00:1** | 4.5:1 | Marginal fail. |

Three states are absent from the stylesheet entirely: `disabled` appears zero times, `invalid` appears zero times, and there is no error styling of any kind. The contact form carries `required` on all three fields, so a bad submission currently produces the browser's native validation bubble, which is unstyled, positioned by the browser, and off-brand.

---

## The system

### Colour

**Neutral ramp.** Hue held at 45 throughout, saturation tapering from the paper end to the ink end. Five steps are the existing values unchanged.

| Step | Hex | Role |
|---|---|---|
| `--n-0` | `#FEFDFC` | Raised surface: cards, menus, popovers. Replaces `#fff`. |
| `--n-50` | `#FAF8F3` | Page background. Unchanged (`paper`). |
| `--n-100` | `#F3F0E8` | Tinted section background. Unchanged (`paper-2`). |
| `--n-200` | `#E7E4DA` | Hairline border, section divider. Unchanged (`mist`). |
| `--n-300` | `#CECAC0` | Strong border, hover edge, disabled surface. **New**, fills the hole. |
| `--n-400` | `#A9A69E` | Secondary text on dark. Absorbs `#A8A69E`. |
| `--n-500` | `#908C82` | Non-text greys only: rules, icons, decorative marks. |
| `--n-600` | `#747269` | Smallest grey that is legal as text on paper (4.54:1). Absorbs `#76746D`. |
| `--n-700` | `#5D5B54` | Secondary body text. Effectively unchanged (`ink-2`). |
| `--n-800` | `#4A4843` | Absorbs `#4A4A44` and `#4A4A46`. |
| `--n-850` | `#34332F` | Divider on dark. Absorbs `#34342F`. |
| `--n-900` | `#2C2B28` | Footer border. Absorbs `#2C2C29`. |
| `--n-925` | `#1C1C1A` | Field surface on dark. Unchanged. |
| `--n-950` | `#121212` | Ink. Unchanged, and the one deliberately cold value in the ramp. |

**Accent.** `--accent: #C6F235`, `--accent-hover: #9DC81A`. There is no accent text token, and that omission is the rule: the accent is a fill and a marker, never an ink and never a hairline. Ink on accent is 14.41:1 and on accent-hover 9.55:1, so a chartreuse block with an ink label is always safe. Chartreuse on paper is 1.22:1, so a chartreuse line or a chartreuse word on paper is never safe. This single rule fixes the nav hover, the projects card hover and the fit-check underline at once.

Where the current site uses the accent as a foreground, replace it with a filled square. That is truer to the brand's own vocabulary, which is built from squares rather than lines.

**Semantic.** The site has no error colour, which is why the form has no error state. Add one, warm enough to sit in this palette:

- `--danger: #E4573D` for the field border and the marker square
- `--danger-text: #F0997B` for the message on dark, 8.52:1 against `#121212` and 7.76:1 against the `#1C1C1A` field

Success needs no colour because completion is handled by navigating to `/thank-you`.

### Type

Space Grotesk, kept. Seven fixed steps plus two fluid.

| Token | Size | Weight | Line height | Use |
|---|---|---|---|---|
| `--t-micro` | 12px | 600 | 1.4 | Eyebrow, step number, tag |
| `--t-small` | 13px | 400 | 1.5 | Meta strip, footer, form label, fine print |
| `--t-compact` | 14px | 400 | 1.5 | Body inside cards and steps |
| `--t-body` | 16px | 400 | 1.55 | Base |
| `--t-lead` | 18px | 400 | 1.4 | Hero paragraph, fit list, FAQ question |
| `--t-h3` | 20px | 600 | 1.2 | Card and step headings |
| `--t-h3-lg` | 24px | 600 | 1.15 | Work-card heading |
| `--t-h2` | `clamp(28px, 3.4vw, 40px)` | 600 | 1.08 | Unchanged |
| `--t-h1` | `clamp(40px, 5.4vw, 64px)` | 600 | 1.02 | Unchanged |

Tracking follows size, as it already does: `-0.035em` at h1, `-0.03em` at h2, `-0.015em` at h3, `0` at body, `+0.14em` on the 12px eyebrow.

The mapping from current values: 14.5 becomes 14, 15 and 15.5 become 16, 17 becomes 18, 19 becomes 20, 22 becomes 24. Three of those are visible changes and all three make the text slightly larger. If you would rather see no change at all, keep 17, 19 and 22 as the scale steps instead; the set is still closed and the drift is still gone. My preference is the version above because the steps are far enough apart to stay distinct, and 16 against 17 is too fine a difference to survive the next round of edits.

### Spacing

Base unit 4px. Scale: **4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 96**.

Eleven steps replace thirty-four values. Section padding stays at 96, page gutter stays at 48 falling to 24 below 720px, card padding lands on 24 or 32. Container padding should always exceed the gaps between the things inside it, so a card at 32 padding holds children at 16 or less.

### Squares

The brand's core element currently ships in eight sizes: 8, 9, 9, 10, 15, 16, 20 and 26px, of which exactly one is tokenised. Reduce to four:

| Token | Size | Use |
|---|---|---|
| `--sq-xs` | 8px | Inline marker, current-language dot, status dot |
| `--sq-sm` | 12px | List bullet in work-points |
| `--sq-md` | 16px | Card mark, fit-list box |
| `--sq-lg` | 24px | Hero canvas unit, placeholder mark |

Each square uses one of the four states, and the states carry meaning consistently: filled ink is default, hollow is pending or optional, stone is inactive, chartreuse is the one that matters. Do not introduce a fifth state.

### Borders, elevation, motion

One separation strategy, which the site already uses on light surfaces: a 1px border. Apply it on dark too rather than mixing in a surface shift that cannot be seen.

- Hairline: `1px solid var(--n-200)` on light, `1px solid var(--n-850)` on dark
- Interactive boundary, meaning anything you can click or type into: `1px solid var(--n-600)` minimum, which gives 3.54:1 on the dark field
- Elevation: one shadow, `0 12px 30px rgba(18,18,18,.10)`, replacing the three near-identical ones in the file
- Motion: 0.15s for colour and border, 0.25s for transform and layout, 0.7s for scroll reveals. All existing durations already sit near these.

### States

Every control gets five. This is the section the current stylesheet is missing.

| State | Primary button | Ghost button | Form field (dark) | Nav link |
|---|---|---|---|---|
| Default | `--accent` bg, ink label | `--n-500` 1px bottom border | `--n-925` bg, `--n-600` border | `--n-700` text |
| Hover | `--accent-hover` bg | ink border and text | `--n-500` border | **ink text**, plus the chartreuse rule |
| Focus | `2px solid ink`, 3px offset | same | `--accent` border, ring on dark | same |
| Active | `scale(.98)` | no change | no change | no change |
| Disabled | `--n-300` bg, `--n-600` label, no pointer | `--n-300` border and text | `--n-300` border, 60% label | not applicable |

Two notes on that table. The nav hover fix is to darken the link text, keeping the chartreuse rule as decoration rather than as the signal, which preserves the look and supplies the feedback that is currently missing. And the focus ring stays exactly as built, including the chartreuse override on the dark section.

**Error state**, which does not currently exist:

```
input:invalid:not(:placeholder-shown),
input[aria-invalid="true"] { border-color: var(--danger); }
```

with the message below the field at 13px in `--danger-text`, preceded by an 8px `--danger` square so the error is not carried by colour alone.

---

## What this changes on screen

Almost nothing, which is the point. The paper, the ink, the chartreuse, the zero radius, the hairlines, Space Grotesk, the layout and the animation are all unchanged. What moves: `#fff` surfaces warm very slightly, three text sizes go up by one or two pixels, spacing values shift by up to two pixels, the nav gains a visible hover, the projects card stops fading out on hover, the form fields gain a visible edge and an error state, and eleven stray hex values disappear into the ramp.
