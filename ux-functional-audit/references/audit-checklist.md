# Audit checklist

The coverage scaffold for the ux-functional-audit skill. Run against it so no category is skipped. It is a checklist to guarantee coverage rather than a script to recite back, so report findings in the user's terms, with severity and the cost to the user, the way SKILL.md describes. Not every item applies to every product; skip what's irrelevant and say so rather than padding the report.

## 1. Map the surface first

Before checking anything, enumerate it. You can't audit "all functions" without a list of them.
- Every user goal or job that the product is meant to support.
- Every flow (the ordered steps to reach each goal), from start to finish.
- Every screen, route, view, modal, and panel.
- Every interactive element: buttons, links, inputs, toggles, menus, drag targets, and gestures.
- Every input and the data behind each view.
- From code: every handler, route, conditional branch, and piece of state. Note branches and states that the code does *not* handle.

Write the map down. It is the proof of completeness and the verdict's evidence.

## 2. States, for every view

The populated, happy, online state is the one that gets demoed and the one that's already fine. Check the others:
- **Empty.** No data yet, first use, nothing saved, no results. Is there guidance on what goes here and how to start?
- **Loading.** Initial load, and slow load. Is there feedback? Skeleton or spinner? Does it block the whole screen unnecessarily?
- **Partial.** Some data loaded, some pending or failed. Mixed success.
- **Success.** Confirmed, completed, saved. Is completion unmistakable?
- **Error.** Request failed, validation failed, server error, timeout. Is the message specific and actionable, or a dead generic "something went wrong"?
- **Overflow.** Too much content, long text, many items, deep nesting.
- **Offline / poor connection.** Does it fail gracefully, queue, or just hang?
- **Unauthenticated / session expired.** What happens mid-task when the session dies?
- **Permission-denied.** Feature not allowed for this user or role.
- **Stale.** Data changed underneath the user since the page loaded.

## 3. Content and input edges

Real data breaks demo designs. Push:
- Counts: zero, one, two, many, far too many. Does pagination or virtualisation exist, or does it choke?
- Text length: empty, single character, and the longest plausible value (names, titles, descriptions). Does it truncate, wrap, or overflow and break layout?
- Characters: spaces-only, emoji, right-to-left, accented characters, HTML or script-looking input, leading or trailing whitespace.
- Numbers: zero, negative, very large, decimals, boundary values, wrong units.
- Malformed input: wrong format, partial input, pasted blobs.
- Timing: double-submit, rapid re-tap, submitting before load completes, back-button mid-submit, refresh mid-task.
- Required vs optional: what happens when required data is missing, and is "required" obvious before submitting?

## 4. Interaction contract

- **Feedback.** Every action produces a visible, timely response. Nothing happens silently.
- **Status visibility.** The user always knows what state the system is in: loading, saved, failed, in progress.
- **Reversibility.** There's always a way back and a way out. No dead ends and no traps.
- **Destructive actions.** Protected against accidental trigger, clearly labelled, and recoverable where possible (undo beats a confirm dialog; a confirm dialog beats nothing).
- **Confirmation vs friction.** Confirmations only where the cost is real, because overusing them trains people to click through blindly.
- **Defaults.** Sensible defaults that suit the common case; the user shouldn't have to configure what you could have guessed.
- **Forgiveness.** Input is preserved across errors; a validation failure never wipes the form.
- **Consistency of action.** The same control does the same thing everywhere; the same thing is done the same way everywhere.

## 5. Navigation and flow

- Can the user always tell where they are, where they can go, and how to get back?
- Browser back, forward, and refresh behave sanely at every step (especially in multi-step flows and SPAs).
- Deep links and direct entry to a sub-page work, or fail gracefully.
- Multi-step flows show progress and allow going back without data loss.
- Exit and cancel are available and don't silently discard work without warning.
- Dead ends: every screen has an onward or upward path.

## 6. Accessibility of use (a floor, not a feature)

- **Keyboard.** Every function operable without a mouse; logical tab order; no keyboard traps.
- **Focus.** Focus is visible, and moves sensibly (for example, into an opened modal and back out on close).
- **Screen reader.** Meaningful labels on controls and inputs; correct roles; dynamic changes announced (errors, loading, success).
- **Targets.** Tap or click targets large enough (around 44px) and not crowded.
- **Motion.** Respects reduced-motion; nothing essential is conveyed by motion alone.
- **Colour.** State and meaning are never carried by colour alone; they are paired with text, icon, or shape.
- **Contrast** (where it blocks use). Text and essential controls meet WCAG AA, so they can actually be seen and operated.
- **Zoom / text scaling.** Layout survives 200% zoom and larger system text.

## 7. Responsive and cross-context

- Smallest realistic viewport (around 375px): does anything overflow, overlap, or get pushed off-screen?
- Large viewport: does content stretch awkwardly or leave the layout broken?
- Touch vs pointer: are hover-only affordances reachable on touch? Are gestures discoverable?
- Orientation change, on-screen keyboard covering inputs, safe areas and notches.
- If relevant: light and dark modes, different browsers, slow devices.

## 8. Perceived performance

- Does the interface respond immediately to input, even if the result takes time (optimistic UI, immediate acknowledgement)?
- Are slow operations explained and, ideally, cancellable?
- Does the layout shift as content loads (jumpy, mis-taps), or hold its shape?
- First meaningful content fast, or a blank screen while everything loads?

## 9. Comprehension and content

- Labels, buttons, and messages in the user's language, not the system's or the team's internal jargon.
- Error messages say what went wrong *and* what to do about it.
- Instructions appear at the point of need, not buried in help.
- Microcopy is honest and specific ("Saved" vs a vague "Done"; "Card declined" vs "Error").
- The primary action on each screen is obvious and singular.

## 10. Data integrity and trust

- Does the user's work persist when expected (and is it clear when it won't)?
- Is autosave vs manual save unambiguous?
- Are irreversible or costly actions clearly distinguished from cheap ones?
- Does the system prevent the user from getting into an inconsistent or corrupt state?
- Is sensitive action (delete, pay, send) gated appropriately?

## Severity reminder

Tag every finding:
- **Blocker.** Core task broken or impossible. Fix before shipping.
- **Serious.** Completes but with real friction, confusion, error risk, or data-loss potential. Fix soon.
- **Minor.** Irritating inconsistency or friction that doesn't block. Fix when convenient.
- **Polish.** Optional refinement.

When several findings share a root cause, say so and name the cause. One fix should retire the cluster.
