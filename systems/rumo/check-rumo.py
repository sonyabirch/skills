#!/usr/bin/env python3
"""
Rumo design system compliance checker.

Usage:  python3 check-rumo.py /path/to/unzipped/bundle

Greps a returned bundle against the design system spec and the preserve list.
Exits 0 if clean, 1 if anything failed. Reports counts, not opinions.
"""
import sys, os, re, glob

# ---- the system, as specified -------------------------------------------
RAMP = {
    "#FEFDFC": "n-0",   "#FAF8F3": "n-50",  "#F3F0E8": "n-100", "#E7E4DA": "n-200",
    "#CECAC0": "n-300", "#A9A69E": "n-400", "#908C82": "n-500", "#747269": "n-600",
    "#5D5B54": "n-700", "#4A4843": "n-800", "#34332F": "n-850", "#2C2B28": "n-900",
    "#1C1C1A": "n-925", "#121212": "n-950",
}
ACCENT  = {"#C6F235": "accent", "#9DC81A": "accent-hover"}
DANGER  = {"#E4573D": "danger", "#F0997B": "danger-text"}
ALLOWED_HEX = {**RAMP, **ACCENT, **DANGER}

TYPE_SCALE    = {12, 13, 14, 16, 18, 20, 24}
SPACING_SCALE = {0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 96}
# values exempt from the spacing scale: hairlines, rings, and tuned offsets
SPACING_EXEMPT = {1, 2, 3, 70, 107, 36}

PRESERVE = [
    ('data-netlify="true"',            "Netlify form detection"),
    ('netlify-honeypot="company"',     "honeypot field"),
    ('name="form-name"',               "hidden form-name input"),
    ('action="/thank-you"',            "form redirect"),
    ('application/ld+json',            "JSON-LD structured data"),
    ('property="og:',                  "Open Graph tags"),
    ('name="twitter:',                 "Twitter Card tags"),
    ('rel="icon"',                     "favicon link"),
    ('id="hero-space"',                "hero canvas element"),
    ('id="replay"',                    "replay button"),
    ('prefers-reduced-motion',         "reduced motion handling"),
    ('scroll-margin-top',              "tuned scroll offsets"),
    ('zoom: 1.25',                     "1200px zoom rule"),
    (':focus-visible',                 "focus ring"),
]
# which files each preserve item must appear in: 'any' = at least one file
PRESERVE_ANY = {"Netlify form detection", "honeypot field", "hidden form-name input",
                "form redirect", "hero canvas element", "replay button",
                "1200px zoom rule", "tuned scroll offsets", "focus ring",
                "reduced motion handling"}

CANVAS_CONSTS = {"INK": "#121212", "STONE": "#908C82", "LIME": "#C6F235"}

# Embedded product demos carry their own palettes on purpose and are not
# part of the Rumo system. Skipped for palette, type and spacing checks.
EXCLUDE = ["projects/eventplanning"]

fails = []
def ok(msg):   print(f"  ok    {msg}")
def bad(msg):  print(f"  FAIL  {msg}"); fails.append(msg)
def note(msg): print(f"  note  {msg}")

def main(root):
    css_files  = glob.glob(os.path.join(root, "**", "*.css"), recursive=True)
    html_files = glob.glob(os.path.join(root, "**", "*.html"), recursive=True)
    def excluded(p):
        rel = os.path.relpath(p, root).replace(os.sep, "/")
        return any(rel.startswith(e) for e in EXCLUDE)
    skipped = [f for f in css_files + html_files if excluded(f)]
    css_files  = [f for f in css_files  if not excluded(f)]
    html_files = [f for f in html_files if not excluded(f)]
    if not css_files or not html_files:
        print(f"No CSS or HTML found under {root}"); return 1
    css = "\n".join(open(f, encoding="utf-8", errors="ignore").read() for f in css_files)
    html_blobs = {f: open(f, encoding="utf-8", errors="ignore").read() for f in html_files}
    all_html = "\n".join(html_blobs.values())
    src = css + "\n" + all_html

    print(f"\nbundle: {root}")
    print(f"        {len(css_files)} css, {len(html_files)} html")
    if skipped:
        print(f"        {len(skipped)} skipped (own palette): {', '.join(os.path.relpath(s, root) for s in skipped)}")
    print()

    # 1. palette ----------------------------------------------------------
    print("1. palette")
    nocomment = re.sub(r"/\*.*?\*/|<!--.*?-->", "", src, flags=re.S)
    found = re.findall(r"#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3}\b", nocomment)
    norm = []
    for h in found:
        h = h.upper()
        if len(h) == 4: h = "#" + "".join(c * 2 for c in h[1:])
        norm.append(h)
    stray = {}
    for h in norm:
        if h not in ALLOWED_HEX:
            stray[h] = stray.get(h, 0) + 1
    if stray:
        for h, n in sorted(stray.items(), key=lambda x: -x[1]):
            bad(f"off-palette hex {h} used {n}x")
    else:
        ok(f"every hex resolves to a token ({len(set(norm))} distinct, all allowed)")
    used_ramp = {RAMP[h] for h in set(norm) if h in RAMP}
    unused = sorted(set(RAMP.values()) - used_ramp, key=lambda s: int(s.split("-")[1]))
    if unused:
        note(f"ramp steps defined but unused: {', '.join(unused)}")

    # 2. type scale -------------------------------------------------------
    print("\n2. type scale")
    sizes = [float(x) for x in re.findall(r"font-size:\s*([0-9.]+)px", css)]
    offs = sorted({s for s in sizes if s not in TYPE_SCALE})
    if offs:
        bad(f"{len(offs)} off-scale font sizes: {', '.join(str(s).rstrip('0').rstrip('.') for s in offs)}px")
    else:
        ok(f"all {len(set(sizes))} font sizes on the seven-step scale")
    if re.search(r"font-size:\s*[0-9]+\.[0-9]+px", css):
        bad("fractional font sizes present (the ad-hoc fingerprint)")

    # 3. spacing ----------------------------------------------------------
    print("\n3. spacing")
    decls = re.findall(r"(?:^|[;{\s])(?:gap|padding|margin)(?:-top|-right|-bottom|-left)?:\s*([^;}]+)", css)
    vals = []
    for d in decls:
        vals += [int(v) for v in re.findall(r"(-?\d+)px", d)]
    offs = sorted({abs(v) for v in vals if abs(v) not in SPACING_SCALE and abs(v) not in SPACING_EXEMPT})
    if offs:
        bad(f"{len(offs)} off-scale spacing values: {', '.join(str(v) for v in offs)}px")
    else:
        ok(f"all spacing on the 4px scale ({len(set(abs(v) for v in vals))} distinct values)")

    # 4. radius -----------------------------------------------------------
    print("\n4. radius")
    radii = {r.strip() for r in re.findall(r"border-radius:\s*([^;}]+)", css)}
    zero_vars = set()
    m = re.search(r"--radius:\s*0(px)?\s*;", css)
    if m: zero_vars.add("var(--radius)")
    nonzero = {r for r in radii if r not in ("0", "0px") and r not in zero_vars}
    if nonzero:
        bad(f"non-zero radius: {', '.join(sorted(nonzero))}")
    else:
        ok(f"radius 0 everywhere ({len(re.findall(r'border-radius', css))} declarations)")

    # 5. states -----------------------------------------------------------
    print("\n5. states")
    for sel, label in [(r":disabled|\[disabled\]|\.is-disabled", "disabled"),
                       (r":user-invalid|:invalid|aria-invalid", "invalid / user-invalid"),
                       (r":focus-visible", "focus-visible"),
                       (r":hover", "hover"),
                       (r":active", "active")]:
        n = len(re.findall(sel, css))
        (ok if n else bad)(f"{label}: {n} rule(s)")

    # 6. shadows ----------------------------------------------------------
    print("\n6. elevation")
    shadows = {s.strip() for s in re.findall(r"box-shadow:\s*([^;}]+)", css)} - {"none"}
    if len(shadows) > 1:
        bad(f"{len(shadows)} distinct shadows, spec allows 1: {' | '.join(sorted(shadows))}")
    else:
        ok(f"{len(shadows)} shadow token")

    # 7. preserve list ----------------------------------------------------
    print("\n7. preserve list")
    for needle, label in PRESERVE:
        hits = sum(1 for b in html_blobs.values() if needle in b) + (1 if needle in css else 0)
        if hits == 0:
            bad(f"MISSING: {label}  ({needle})")
        elif label in PRESERVE_ANY:
            ok(f"{label} present")
        else:
            missing = [os.path.basename(f) for f, b in html_blobs.items() if needle not in b]
            if missing:
                bad(f"{label} missing from: {', '.join(sorted(missing))}")
            else:
                ok(f"{label} in all {len(html_blobs)} files")

    # 8. canvas constants -------------------------------------------------
    print("\n8. hero canvas colour constants")
    for name, expected in CANVAS_CONSTS.items():
        m = re.search(rf"{name}\s*=\s*['\"](#[0-9A-Fa-f]{{6}})['\"]", all_html)
        if not m:
            bad(f"{name} constant not found in canvas script")
        elif m.group(1).upper() != expected.upper():
            bad(f"{name} is {m.group(1)}, spec says {expected}")
        else:
            ok(f"{name} = {expected}")

    # 9. contrast of pairs actually used ----------------------------------
    print("\n9. contrast, computed")
    def lum(h):
        h = h.lstrip("#"); r, g, b = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
        f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        return .2126*f(r) + .7152*f(g) + .0722*f(b)
    def cr(a, b):
        l1, l2 = sorted([lum(a), lum(b)], reverse=True); return (l1 + .05) / (l2 + .05)
    pairs = [("#5D5B54", "#FAF8F3", 4.5, "secondary text on page"),
             ("#747269", "#FAF8F3", 4.5, "smallest grey on page"),
             ("#747269", "#FEFDFC", 4.5, "smallest grey on card"),
             ("#A9A69E", "#121212", 4.5, "secondary text on dark"),
             ("#747269", "#1C1C1A", 3.0, "field border on dark"),
             ("#121212", "#C6F235", 4.5, "button label on accent"),
             ("#121212", "#9DC81A", 4.5, "button label on accent hover"),
             ("#F0997B", "#121212", 4.5, "error message on dark")]
    for fg, bg, need, where in pairs:
        r = cr(fg, bg)
        (ok if r >= need else bad)(f"{r:5.2f}:1  need {need}  {where}")

    # 10. architecture ----------------------------------------------------
    print("\n10. architecture")
    if "rumo.css" not in {os.path.basename(f) for f in css_files}:
        bad("rumo.css missing: the single external stylesheet was not preserved")
    else:
        ok("rumo.css present")
    unlinked = [os.path.basename(f) for f, b in html_blobs.items() if "rumo.css" not in b]
    if unlinked:
        bad(f"not linking rumo.css: {', '.join(sorted(unlinked))}")
    else:
        ok(f"all {len(html_blobs)} pages link rumo.css")
    inlined = False
    for f, b in sorted(html_blobs.items()):
        bulk = sum(len(x.strip().splitlines())
                   for x in re.findall(r"<style[^>]*>(.*?)</style>", b, re.S))
        if bulk > 40:
            bad(f"{os.path.basename(f)}: {bulk} lines of inline CSS, the stylesheet was inlined")
            inlined = True
    if not inlined:
        ok("no page carries bulk inline CSS")

    # 11. internal links -------------------------------------------------
    print("\n11. internal links")
    targets = set()
    for b in html_blobs.values():
        targets |= set(re.findall(r'href="(/[^"#?]*)"', b))
    dead = []
    for t in sorted(targets):
        if t in ("/",):
            continue
        rel = t.lstrip("/")
        cands = [rel, rel + ".html", os.path.join(rel, "index.html"),
                 rel.rstrip("/") + ".html", os.path.join(rel.rstrip("/"), "index.html")]
        if not any(os.path.exists(os.path.join(root, c)) for c in cands):
            dead.append(t)
    if dead:
        for t in dead:
            where = sorted(os.path.basename(f) for f, b in html_blobs.items() if f'href="{t}"' in b)
            bad(f"dead link {t}  (in {', '.join(where)})")
    else:
        ok(f"all {len(targets)} internal link targets resolve")
    def url_forms(relpath):
        r = relpath.replace(os.sep, "/")
        forms = {"/" + r}
        if r.endswith("index.html"):
            d = r[:-len("index.html")]
            forms |= {"/" + d, "/" + d.rstrip("/")}
        if r.endswith(".html"):
            forms.add("/" + r[:-5])
        return {f for f in forms if f}
    linked = set()
    for b in html_blobs.values():
        linked |= set(re.findall(r'href="(/[^"#?]*)"', b))
        linked |= set(re.findall(r'action="(/[^"#?]*)"', b))
    claims = {}
    for f in html_blobs:
        rel = os.path.relpath(f, root)
        for u in url_forms(rel):
            claims.setdefault(u, []).append(rel)
    for u, fs in sorted(claims.items()):
        if len(fs) > 1:
            bad(f"URL collision: {u} is claimed by {' and '.join(sorted(fs))}")
    orphans = []
    for f in html_blobs:
        rel = os.path.relpath(f, root)
        if rel == "index.html":
            continue
        if not (url_forms(rel) & linked):
            orphans.append(rel)
    if orphans:
        for o in orphans:
            bad(f"orphan: {o} is not linked from any page")
    else:
        ok("every page is reachable by a link")

    print()
    if fails:
        print(f"{len(fails)} failure(s)\n")
        return 1
    print("clean\n")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
