# Brief for Claude Design: Rumo site, design system pass

Paste this whole document as your first message. Attach `rumo-design-system.md` and the site zip alongside it.

---

## Who you are on this job

You are the visual designer holding a system that has already been decided. The palette, the type, the spacing, the states and the square vocabulary are settled and written down in the attached spec. Your job is to apply them faithfully and to build the components the site has been missing, not to reopen the direction.

That constraint is doing real work here. This site was built by hand, it is live, it ranks, and it carries a set of small hard-won details that look like mistakes and are not. A pass that improves the look while dropping one of those details is a net loss. Read the preserve list before you touch anything.

Where the spec is silent, choose the quieter option and say what you chose. Where you think the spec is wrong, say so in one line and apply it anyway; the person reading your output can overrule it faster than you can rebuild it.

---

## Preserve list, non-negotiable

These are invisible in a rendered page and expensive to notice missing. Losing one of them costs a day of debugging or a drop in search traffic. Carry them through every file untouched.

**In `<head>` of every page**
- All `<meta>` tags including Open Graph and Twitter Card. Note that these are not evenly distributed: Open Graph and Twitter Card exist only on `index.html`, `projects.html` and `projects/index.html`, and JSON-LD exists only on `index.html`. Preserve what is there and see step 3b about the rest.
- The JSON-LD `<script type="application/ld+json">` blocks
- Any Google Search Console verification tag
- `<link rel="icon" href="/favicon.svg">`

**Markup and behaviour**
- The contact form's exact attributes: `name="contact"`, `method="POST"`, `data-netlify="true"`, `netlify-honeypot="company"`, `action="/thank-you"`, the hidden `form-name` input, and the hidden company honeypot field. Netlify's form detection reads these literally; changing any of them silently breaks the form and you will not see an error.
- Every existing URL and path. `/projects`, `/projects/eventplanning/`, `/about`, `/why-rumo`, `/impressum`, `/privacy`, `/datenschutz`, `/thank-you`. These are in the sitemap and indexed.
- The hero canvas element `<canvas id="hero-space">` and the entire script that drives it, including the `#replay` button binding.
- `#contact { scroll-margin-top: -107px }` and `#problems, #method, #about { scroll-margin-top: -36px }`. The negative values look wrong and are tuned against the 70px sticky header. Leave them.
- `@media (min-width: 1200px) { body { zoom: 1.25 } }`. Deliberate, and deliberately not applied below 1200px because it causes horizontal scroll on narrow screens.
- Every `prefers-reduced-motion` block. There are four.
- The focus-visible rules, including the chartreuse override inside `.contact`.

**One coupling you have to handle**
The hero canvas script hardcodes three colours in JavaScript rather than reading them from CSS: `INK = '#121212'`, `STONE = '#8C8C86'`, `LIME = '#C6F235'`. When `stone` moves to `#908C82` in the ramp, update the JS constant to match, or the floating squares will sit at a different temperature from every other square on the page.

---

## The gate: build the style tile first

Before touching any site page, produce a single file, `style-tile.html`, and stop there for approval.

It must contain, on the real paper background and in Space Grotesk:

1. The full neutral ramp as labelled swatches, step name and hex under each
2. The accent shown three ways: as a fill with an ink label, as a hover fill, and as a small marker square on the dark ink surface
3. The nine type steps set in actual type, seven fixed at 12, 13, 14, 16, 18, 20 and 24 plus the two clamped headings, each labelled with its size and its use
4. The spacing scale as eleven blocks in ascending size
5. The four square sizes in all four states
6. A primary button in default, hover, focus, active and disabled
7. A ghost button in default, hover and disabled
8. A form field on the dark surface in default, focus and error, with the error message and its danger square
9. A card and a section divider

The reason for the gate is that a disagreement about the ramp costs one file to fix now and nine files to fix later. Do not proceed past this until the tile is approved.

---

## Then, in this order

**Step 1: rewrite `rumo.css` against the spec.** One stylesheet, same filename, same selector names. Put the full token set in `:root`. Replace every literal hex with its token. Replace every font size with a scale step. Move every spacing value onto the scale. Add the state rules and the error styling. Keep the file organised in the same section order it already uses, so a diff is readable.

**Step 2: fix the four things that are broken rather than merely inconsistent.** Each of these is a usability problem wearing a visual problem's clothes.

- The projects card "read more" turns `#9DC81A` on hover, which is 1.96:1 against the white card. It becomes unreadable at the moment of interaction. Keep it ink and let the card border darken instead.
- Main nav links have no hover feedback other than a chartreuse underline at 1.22:1, which cannot be seen. Darken the link text on hover from `--n-700` to ink, and keep the underline as decoration.
- Contact form fields have a 1.36:1 border on a 1.10:1 surface, so nothing marks where to type. Take the border to `--n-600`, which measures 3.54:1.
- Method step numbers are `#8C8C86` at 12px on the tinted background, 2.97:1. Take them to `--n-600`.

**Step 3: apply to the nine HTML files.** `index.html`, `about.html`, `why-rumo.html`, `projects.html`, `projects/index.html`, `thank-you.html`, `impressum.html`, `privacy.html`, `datenschutz.html`. Markup changes only where a state or a square size needs a class it does not have. Do not restructure sections, do not rewrite copy, do not add elements.

`projects/eventplanning/index.html` is the tenth HTML file in the bundle and is deliberately excluded. It is a standalone demo of a tool built for a client: it does not link `rumo.css`, it carries no Rumo header or footer, it runs its own palette of blues, teals and greens, and it is not in the sitemap. Restyling it to the Rumo system would misrepresent the client's product. Leave the file untouched.

**Step 3b: fill the head-tag gaps while the files are open.** This is not a design change and it is listed separately for that reason, but the marginal cost of doing it during a pass that already touches all nine files is close to zero.

Six pages carry no Open Graph or Twitter Card tags at all: `about.html`, `why-rumo.html`, `thank-you.html`, `impressum.html`, `privacy.html`, `datenschutz.html`. Give each one `og:title`, `og:description`, `og:url`, `og:image`, `og:type`, and the matching `twitter:card`, `twitter:title`, `twitter:description` and `twitter:image`, copying the pattern already in `index.html` and writing per-page titles and descriptions rather than repeating the homepage text. No page has a `<link rel="canonical">`, so add one to each pointing at its own clean URL. Leave JSON-LD alone; the Organization and Service blocks belong on the homepage and do not need repeating.

**Step 4: report the diff in words.** List every value that changed and every file touched. This is what gets checked, so make it specific enough to grep against.

---

## Output contract

- Plain static files, same names, same paths, ready to upload to Netlify without a build step
- No frameworks, no bundler, no npm, no Tailwind, no CSS-in-JS. The site is hand-written HTML and one stylesheet and stays that way.
- No `localStorage`, no external font CDN beyond the one already in use, no new dependencies
- Sentence case in any UI text you touch, British spelling, and no em dashes anywhere
- If you cannot do something without breaking a preserve-list item, stop and say which item

---

## What good looks like

The site loads and a person who knows it well cannot immediately say what changed. Then they hover a nav link and see it respond, tab through the contact form and see every field's edge, submit it empty and get an error in the site's own voice rather than a browser bubble, and open the stylesheet to find fourteen greys instead of fifteen strays, nine type sizes instead of fourteen, and one spacing scale instead of thirty-four numbers.
