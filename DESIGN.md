---
name: Besace
description: A bookmark library laid out like a gleaner's desk, paper folders on a Constable sky.
colors:
  bg: "light-dark(#e9e9f0, #17181a)"
  fg: "light-dark(#1e1e24, #e8e6e0)"
  muted: "light-dark(#5f6070, #a09c93)"
  line: "light-dark(#cfd0dc, #2c2d30)"
  accent: "light-dark(#4d6531, #a7c78a)"
  accent-ink: "light-dark(#f5f2ea, #17181a)"
  lavender: "light-dark(#e6e0f4, #2b2740)"
  paper: "light-dark(#f2f2f6, #222325)"
  paper-design: "light-dark(#e6e0f4, #2b2740)"
  paper-dev: "light-dark(#dfe8d0, #253021)"
  paper-ressources: "light-dark(#dfe6ee, #26303a)"
  postit: "light-dark(#fff4a8, #c9b84a)"
  verre: "light-dark(rgb(240 240 247 / 0.55), rgb(23 24 26 / 0.55))"
  verre-bord: "light-dark(rgb(255 255 255 / 0.6), rgb(255 255 255 / 0.1))"
typography:
  display:
    fontFamily: "Atkinson Hyperlegible Next, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(2rem, 1.7rem + 1.2vw, 2.75rem)"
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: "normal"
  headline:
    fontFamily: "Atkinson Hyperlegible Next, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(1.625rem, 1.45rem + 0.7vw, 2rem)"
    fontWeight: 700
    lineHeight: 1.1
  title:
    fontFamily: "Atkinson Hyperlegible Next, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(1.25rem, 1.16rem + 0.38vw, 1.5rem)"
    fontWeight: 650
    lineHeight: 1.2
  body:
    fontFamily: "Atkinson Hyperlegible Next, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(1rem, 0.96rem + 0.18vw, 1.125rem)"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Atkinson Hyperlegible Next, ui-sans-serif, system-ui, sans-serif"
    fontSize: "clamp(0.875rem, 0.84rem + 0.12vw, 0.9375rem)"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "normal"
rounded:
  none: "0"
spacing:
  3xs: "calc(var(--space-base) * 0.25)"
  2xs: "calc(var(--space-base) * 0.5)"
  xs: "calc(var(--space-base) * 0.75)"
  s: "var(--space-base)"
  m: "calc(var(--space-base) * 1.5)"
  l: "calc(var(--space-base) * 2)"
  xl: "calc(var(--space-base) * 3)"
  2xl: "calc(var(--space-base) * 4)"
components:
  tag:
    backgroundColor: "{colors.lavender}"
    textColor: "{colors.fg}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "{spacing.3xs} {spacing.xs}"
  tag-hover:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
  tag-pressed:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
  filter-category:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.label}"
    padding: "{spacing.3xs} 0"
  filter-category-pressed:
    textColor: "{colors.fg}"
  card:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.fg}"
    rounded: "{rounded.none}"
    padding: "calc(1.75rem + {spacing.s}) {spacing.m} {spacing.m}"
  search:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.fg}"
    typography: "{typography.label}"
    padding: "{spacing.2xs} {spacing.s}"
  tool-button:
    backgroundColor: "transparent"
    textColor: "{colors.fg}"
    size: "2.5rem"
---

# Design System: Besace

## Overview

**Creative North Star: "Le bureau du glaneur"**

Besace is a gleaner's desk. Every bookmark is a manila folder with a cut tab, laid on a table under a Constable sky. Some folders carry a stapled print, tilted a few degrees; some carry a yellow post-it with the extra note. Opening one slides a full sheet of paper in from the right, still slightly askew, which settles flat. The interface is made of things you could pick up, and it is allowed to be playful: a dice throws you at a random folder, the tab lifts when hovered, the photo tilts a random angle each time.

The density is high on purpose. Five hundred folders share one board, the columns run edge to edge, and the zoom lets the visitor step back until only tabs and titles remain, or lean in until a single folder fills a third of the screen. Nothing decorates: no rounded corners, no borders, no gradients on text. Colour does one job, telling the category of a folder, and every category is also carried by a small drawn icon on its tab, so the board still reads in black and white.

Light and dark are two sets of paper, not two designs. The painting stays, the tints keep their hue and drop their lightness, the olive accent becomes a pale sage. A third mode, N&B, is pure black on white (or white on black) with hairline outlines, made for colour-blind readers and for the fun of it.

**Key Characteristics:**
- Folders with cut tabs as the only container, tinted by category.
- One accent (olive) used for pressed state, underlines and focus, nowhere else.
- Drawn SVG icons per category on the tab, never emoji or Unicode.
- Soft two-layer shadows under every sheet, always on.
- Tabular figures wherever numbers sit in a row.
- Full-bleed board, zoom from 0.4 to 1.4, timeline on the right edge, tools bottom right.

## Colors

Two tinted papers and an olive accent over a dimmed painting; the rest is ink and pencil.

### Primary
- **Vert olive** (`accent`): the only accent. Pressed filter tags, active category underline, focus rings, link underlines, the arrow after a domain, the active year's dot. In dark mode it becomes a pale sage so it stays readable on dark paper. Used on well under ten percent of any screen.
- **Encre d'accent** (`accent-ink`): the text colour on an olive fill, cream in light, near-black in dark.

### Neutral
- **Ciel** (`bg`): the page ground behind the painting, cool grey-lilac in light, warm near-black in dark. The painting sits on it at 32% opacity (30% and darkened in dark mode).
- **Encre** (`fg`): all primary text, the close button fill, the black-and-white mode's ink.
- **Crayon** (`muted`): descriptions, labels in the sheet, the tab icon, counts, inactive filters. Tinted towards the paper, never a pure grey.
- **Trait** (`line`): hairlines under the bar and between neighbours, the timeline's rail, disabled tags.

### Papers
- **Papier** (`paper`): the default folder and the sheet, and the search field.
- **Lavande** (`lavender` and `paper-design`): tags at rest, and the Design folder.
- **Papier vert** (`paper-dev`): the Développement folder.
- **Papier bleu** (`paper-ressources`): the Ressources folder.
- **Post-it** (`postit`): the second paragraph of a note, always yellow, keeps dark ink in both themes.
- **Verre** (`verre`, `verre-bord`): the bottom bar and the tools stack, translucent with `blur(18px) saturate(1.5)` and a light hairline on top.

Son, Jeu and Société have no tinted paper yet; they use the default paper and rely on their icon.

### Named Rules
**The One Ink Rule.** Olive is the only colour that means "active" or "clickable". Nothing else on the page is olive, so its presence always means something.
**The Tint Rule.** Category tints stay close in lightness to the default paper. They are a hint, not a code; the icon carries the code.
**The Paper Tag Rule.** On a tinted folder a tag takes 9% of the current ink over the paper, not the lavender, so it belongs to its folder.

## Typography

**Display Font:** Atkinson Hyperlegible Next, variable 200 to 800, self-hosted (`static/fonts/`)
**Body Font:** the same face
**Label Font:** the same face; no monospace anywhere

**Character:** One humanist sans made for low-vision readers, used across the whole range from a 300 display to a 650 card title. Hyperlegible's slashed zero and open forms give the tabular figures a quiet instrument-panel feel that suits counts and years.

### Hierarchy
- **Display** (300, `--step-4`, 1.1): the title on an opened sheet and on a tag or category page. Light weight is what makes the sheet read as a different object from the folders.
- **Headline** (700, `--step-3`, 1.1): the site name only.
- **Title** (650, `--step-2`, 1.2): folder titles. Balanced wrapping. Titles over 60 characters drop to `--step-1` and clamp at four lines.
- **Body** (400, `--step-1`, 1.5): descriptions in the sheet, post-it text.
- **Label** (600, `--step-0`, 1.2): tab domain, filters, tags at `--step-0` regular, the bar. Small labels at `--step--1` (0.75rem) are reserved for the timeline years (weight 300) and sheet field names.

### Named Rules
**The No Caps Rule.** Nothing is set in uppercase and nothing is letter-spaced. All-caps titles from imported data are converted to sentence case in the template.
**The Tabular Rule.** Any number that sits next to another number (counts, years, the tag counts in the panel) uses tabular figures.
**The Clamp Rule.** Descriptions on folders clamp at six lines, long titles at four. The sheet shows the full text.

## Layout

The board breaks out of the content container to the viewport edges, minus the gutter (`clamp(1rem, 4vw, 1.5rem)`), and reserves 4rem on the right for the timeline on wide screens. It is a CSS multi-column layout, `columns: calc(20rem * --zoom)` with `--space-m` gaps, so folders pack by height. `--zoom` steps through 0.4, 0.55, 0.7, 0.85, 1, 1.2, 1.4 and scales each folder with the `zoom` property; below 0.7 the board is dense and hides descriptions, post-its and photos.

Header: site name and tagline left, a single underlined text link right. Content container 72rem, measure 62ch.

The bottom bar is fixed, one row on desktop: category filters, the tag panel toggle with count, search, the result count, and the Dossiers / Liste view switch. The tag panel folds up above it, grouped rows, capped at 40vh with its own scroll. The bar reports its height into `--barre-h`; the body padding and every fixed element above it use that value.

The timeline is fixed at the right edge, vertically centred: a 2px rail, one 6px dot per year, years at 0.75rem weight 300.

The tools stack (zoom in, zoom out, dice, N&B) is fixed bottom right on glass, 2.5rem square buttons.

The sheet is a fixed panel on the right, `min(100%, 46rem)` wide, full height, with the paper inset by `--space-s`.

Responsive: under 60rem the timeline becomes a horizontal glass row above the bar and the tools a horizontal row. Under 45rem the category filters scroll sideways with a fade at the edge and the search takes a full row. Under 45rem the sheet's field grid stacks to one column.

Spacing follows the piloti scale in `--space-*`, from 3xs (0.25 × base) to 2xl (4 × base), base being `--step-1`. Inside a folder, siblings are `--space-xs` apart; folders are `--space-m` apart.

## Elevation & Depth

Paper on a desk. Every sheet, folder and mini-folder carries a soft two-layer shadow at rest, offset downward, never a halo. The shadow lives on a `::after` inset below the tab so the tab area stays transparent and only the paper casts. Tabs carry a one-layer shadow of their own. The glass bar and tools stack are the only translucent surfaces, with a light hairline on top and a diffuse shadow under the tools. Photos and post-its cast their own smaller shadows, slightly darker, because they sit on top of the paper.

### Shadow Vocabulary
- **Papier** (`0 1px 2px rgb(0 0 0 / 0.12), 0 6px 12px rgb(0 0 0 / 0.1)`): folders and mini-folders at rest.
- **Feuille** (`0 1px 2px rgb(0 0 0 / 0.12), 0 8px 24px rgb(0 0 0 / 0.14)`): the opened sheet, and the empty-state card.
- **Onglet** (`0 1px 2px rgb(0 0 0 / 0.12)`): the tab.
- **Tirage** (`0 1px 4px rgb(0 0 0 / 0.25)`): the stapled photo; `0 2px 6px rgb(0 0 0 / 0.2)` on the sheet's larger print.
- **Post-it** (`0 2px 6px rgb(0 0 0 / 0.15)`).
- **Outils** (`0 1px 0 var(--verre-bord) inset, 0 4px 12px rgb(0 0 0 / 0.15)`): the glass tools stack.

### Named Rules
**The No Filter Rule.** Depth is `box-shadow`, never `filter: drop-shadow`. The latter repaints on every frame at this card count.
**The Always On Rule.** Shadows are part of the object, not a hover reward. Hover moves the object (a tilt, a 2px lift), it does not add a shadow.

## Shapes

Cut paper. Radius is zero everywhere: folders, tags, buttons, the search field, the sheet, the photo. The only non-rectangular forms are the folder tab, a polygon with its right end cut at an angle (`polygon(0 0, calc(100% - 0.9rem) 0, 100% 100%, 0 100%)`), and the timeline dots. Borders are hairlines (1px, `line`) or absent; the pressed category filter uses a 2px olive bottom border. Photos are square, 1:1, with a white paper margin wider at the bottom, rotated 2.5° at rest.

Tilt is the signature: the photo at 2.5°, the post-it at -0.6°, the empty-state card at -0.6°, the sheet entering at 1.2° and settling to 0°.

## Components

### Folder (`.fiche`)
The unit of the board. A tinted paper rectangle with a tab hanging off its top-left, the paper starting under the tab (a linear gradient, transparent for the tab's height).
- **Tab:** `--tab-h` (1.75rem) high, paper darkened 10% towards ink, cut corner, holds the category icon (0.75em mask, `muted`) and the domain as a link with an olive underline and an arrow after it.
- **Body:** title, description clamped at six lines, optional post-it for the rest of the note, optional photo floated top right, tags at the bottom.
- **Hover:** the photo tilts to a random angle set in JS (`--tilt`) and scales 1.06. The tab link turns olive.
- **Dense (`--zoom` < 0.7):** description, post-it and photo hidden.
- **List view (`data-vue="liste"`):** folders flatten into a two-column grid row on glass, hairline separators, no tab, no shadow.

### Sheet (`.dossier`)
The opened folder, on a fixed right panel or on its own page.
- **Title:** display, 300.
- **Fields:** a two-column `<dl>`, 7rem label column in `muted` at 0.75rem, values at body size. Année, Source (domain with arrow), Dossier, Étiquettes.
- **Photo:** 28% wide, floated right, tilted.
- **Neighbours:** mini-folders in a `minmax(12rem, 1fr)` grid, tab with icon and domain, 2px lift on hover, whole card clickable.
- **Close:** a 2.5rem ink square with a drawn cross, sticky top right.
- **Motion:** panel slides from 100% to 0 in 0.35s (`cubic-bezier(0.2, 0.8, 0.2, 1)`), the paper rotates from 1.2° to 0 in 0.5s with a 0.1s delay.

### Tags (`.tag`, tag panel buttons)
Stamps and labels: a flat lavender rectangle, `--space-3xs` by `--space-xs` padding, label size at regular weight.
- **Hover:** olive fill, accent-ink text, 0.15s.
- **Pressed:** olive fill, weight 600, count at 70% opacity.
- **Disabled:** 35% opacity, no hover change. Used when a tag would give zero results with the current filters.
- **On tinted paper:** 9% ink over the paper instead of lavender.

### Category filters
Text buttons in `muted`, weight 600, a 2px transparent bottom border that turns olive when pressed, text turning ink. Hover turns olive.

### Search
A paper field with a transparent 1px border that turns olive on focus, olive caret, placeholder in `muted`.

### Tools
Glass stack of 2.5rem squares: `+`, `−` in title weight, the dice (inline SVG, tilts -12° on hover, spins 360° with a 1.3 scale bounce on click), and the N&B square (a half-filled bordered square that rotates 180° when active).

### Timeline
Vertical rail with a dot per year. Hover and pressed turn the year to ink; the pressed dot grows 1.5× and turns olive.

### Empty state
A small paper card, tilted -0.6°, centred, `muted` text and an underlined ink button.

### Category icons
Six drawn 12×12 SVG masks in `currentColor`: diamond (design), braces (développement), note (son), d-pad (jeu), three dots (société), three lines (ressources). Used on the folder tab and the mini-folder tab.

## Do's and Don'ts

### Do:
- **Do** carry category with the icon first and the tint second; both must be present on any new folder-like element.
- **Do** keep every fixed element positioned from `--barre-h`, never from a hard-coded bar height.
- **Do** use `box-shadow` on a pseudo-element when a shape has a transparent region, so the shadow follows the paper and not the box.
- **Do** put tilt on objects that sit on paper (photo, post-it, sheet entering), 0.5° to 2.5°, never on the folder itself at rest.
- **Do** keep the N&B mode pure: white and black only, hairline outlines, photos in grayscale.
- **Do** use the piloti `--space-*` and `--step-*` scales for every new value.

### Don't:
- **Don't** add border-radius, letter-spacing, uppercase, gradient text, or a second accent colour.
- **Don't** use `filter: drop-shadow`, `content-visibility` inside the multi-column board, or per-card `backdrop-filter`.
- **Don't** use emoji or Unicode glyphs as icons; draw them as SVG masks in the same 12×12 stroke.
- **Don't** put an eyebrow or kicker above a title; the count goes under it.
- **Don't** add a hover shadow; move the object instead.
- **Don't** use a monospace face for numbers or "technical" feel; tabular figures of the one face do that job.
