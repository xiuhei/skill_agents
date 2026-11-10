---
name: ui-design
description: Use when designing, implementing, refactoring, or reviewing web, desktop, tablet, and mobile UIs. Enforce a restrained black-white-gray visual style, consistent icons (never use Emoji as UI icons), minimal and authentic UI copy, separation of requirements from visible content, and desktop 12×12 / tablet 9×9 / mobile 4×12 grids. Covers component reuse, design tokens, interaction, responsiveness, accessibility, and pre-delivery review.
---

# UI Design

## 0. Constraints

This Skill applies to creating UIs from scratch, modifying existing UIs, implementing designs, and reviewing screenshots or code. By default, deliver product interfaces that are **clean, professional, credible, and useful**. Explicit user branding requirements and established product guidelines take precedence; any deviation must have a genuine business rationale.

**Four mandatory gates before delivery:**

1. **Icon gate:** In AI-designed interfaces, never use Emoji, colorful emoticons, or Emoji fonts as icons for buttons, menus, navigation, feature cards, notifications, or other UI elements. Use the project's existing SVG/icon components; if none exist, adopt one established, stylistically consistent icon set. Preserve Emoji in actual user input, chat messages, usernames, and content explicitly requested for display.
2. **Color gate:** Default to neutral black, white, and gray tones (usually near-black and off-white, avoiding large areas of absolute black or white). Do not arbitrarily add purple, blue-purple gradients, fluorescent colors, colored cards, rainbow backgrounds, colored icons, or decorative “tech” effects. Use brand colors only when explicitly requested or required by existing guidelines. Semantic error/success/warning colors may be used sparingly, never as decoration.
3. **Copy gate:** Every piece of **visible text** must serve a clear product purpose: identifying location, explaining data, supporting an action, communicating status, or conveying necessary business content. Do not fill interfaces with design commentary, implementation ideas, restated requirements, prompts, decorative subtitles, meaningless labels, fabricated statistics, placeholder marketing copy, or debug information.
4. **Layout gate:** Use three baseline grids: desktop `12×12`, tablet `9×9`, and mobile `4×12`. Some grid dimensions can be adjusted, generally using 4, 6, 8, 9, or 12. Columns govern horizontal layout; rows serve only as logical divisions of the initial viewport or workspace. Scrolling content grows naturally.

---

## 1. Workflow: Inherit, Design, Review

1. **Inspect the project.** Identify the tech stack, current screens, real business data, navigation, existing tokens, icon and component libraries, fonts, themes, and interaction conventions. Prefer stable existing project standards.
2. **Reuse mature solutions.** Prefer existing components; when needed, use established platform-appropriate component/icon systems such as Radix, shadcn/ui, Ant Design, Fluent, Material, or native Apple components. Do not reimplement accessible menus, focus traps, dialogs, or selectors.
3. **Separate requirements from UI copy.** Classify user instructions into `functional requirements`, `visual rules`, `interaction constraints`, `explicitly requested visible text`, and `real business data`. The first three guide implementation only and must not be directly rendered. Do not add explanatory copy that the user did not request.
4. **Define the content inventory first.** Identify the navigation labels, field labels, buttons, states, and essential business text actually needed on the screen. List primary actions and error/empty states. Identify explanatory paragraphs and empty cards that can be removed.
5. **Choose the visual language and grid.** Default to neutral grayscale; select one of the three grids based on workspace width, establish minimal tokens and a consistent icon family, and then implement components.
6. **Implement complete interactions.** Handle business states, keyboard/touch operation, error recovery, resizing, scrolling, responsiveness, and dark mode when enabled.
7. **Review before delivery.** Inspect the rendered interface and visible copy. Fix Emoji icons, inappropriate colors, prompt leakage, unnecessary text, and layout problems first. When possible, run the application and review screenshots or actual interactions. Report verification results accurately.

> Design reasoning, grid explanations, color rationale, and component recommendations belong in the AI response, design documentation, or development comments; by default, they must not appear in the product UI.

---

## 2. Strict Visual Rules: Clean Grayscale Interfaces

### 2.1 Default Color Palette

Use the following starter values only when a project has no existing theme and the user has not specified brand colors. Use semantic tokens rather than scattering raw color values throughout components.

| Semantic token | Light default | Dark default |
| --- | --- | --- |
| `canvas` page background | `#F7F8FA` | `#15171A` |
| `surface` panel | `#FFFFFF` | `#1E2125` |
| `surface-muted` secondary area | `#F0F2F4` | `#262A2F` |
| `text` primary text | `#1B1D21` | `#ECEEF1` |
| `text-secondary` secondary text | `#555B63` | `#B5BBC3` |
| `border` necessary divider | `#DFE2E6` | `#363C43` |
| `primary` primary action | `#26292E` | `#E9EBEE` |
| `on-primary` primary action text | `#F8F9FA` | `#1B1D21` |

- Do not default to large areas of pure black `#000000` or use pure white `#FFFFFF` as the sole background. Pure white can be appropriate for individual card surfaces. Use only as many colors as necessary for functionality; do not add colors merely to fill a “palette.”
- Emphasize primary buttons through neutral light-dark contrast; use text or low-contrast surfaces for secondary buttons. Do not assign a separate color to every card or navigation item.
- By default, distinguish chart series with grayscale values, line styles, textures, and direct labels. Introduce restrained, accessible accent colors only when distinction would otherwise be insufficient, and limit their number on a single screen. Never communicate data through color alone.
- Use status colors only for actual meanings: failure/danger, success, warning, or pending. Prefer text and icons together to communicate status; avoid high-saturation backgrounds covering entire cards.
- Do not generate blue-purple gradients, colorful glassmorphism, neon outlines, large glow effects, gradient headings, or meaningless colored light spots by default. Exceptions require an explicit user request or genuine brand requirement.
- Background shades, whitespace, and thin dividers can establish hierarchy. Avoid meaningless border accumulation through nested cards. Retain essential control boundaries and interactive focus indicators.

### 2.2 Icon Consistency

- **Priority:** Existing project icon library → existing native platform icons → one established icon library. Lucide or Heroicons are suitable web defaults; select one and use it consistently. Native clients should use native components or properly licensed SVG assets.
- Icons must match their meaning. Use `search` for search, `settings` for settings, and `folder` for directories. When no suitable icon exists, use a text-only button instead of substituting an Emoji.
- Within the same level, keep optical size, stroke weight, corner style, and alignment consistent. Common icon sizes are `16 / 18 / 20 / 24` platform units. Prefer the library's default stroke weight; avoid mixing filled, outline, photorealistic colorful, and 3D icons on one screen.
- Icons should inherit text color by default. Only status icons should use semantic colors. Use authentic, licensed logo/brand assets, never lookalike Emoji.
- Icon-only buttons need accessible names (such as `aria-label` on the web); purely decorative icons should be hidden from screen readers. Add short visible labels when an icon alone would make an action ambiguous.
- AI-generated static headings, sample data, empty states, and buttons must not use Emoji such as `🚀`, `✨`, `🔥`, `🎯`, or `📁` as illustrations or icons. Preserve Emoji in the original user data.
- Never rely on Unicode private-use characters, broken icon-font glyphs, or system Emoji fallback as an “icon solution.” When icon resources are missing, favor text and add a mature icon dependency.

### 2.3 Avoid Generic AI Template Aesthetics

- Do not automatically create the formulaic “small pill label + oversized headline + explanatory subtitle + three feature cards” layout.
- Do not decorate interfaces with meaningless `01 / 02 / 03`, `PRO`, `NEW`, `BETA`, `Smart`, or `Efficient` labels. Display them only when they represent real numbering, product states, or subscription tiers.
- Avoid giving every section a heading, description, divider, shadow, and card. Let content dictate local density. One visual focal point is usually sufficient.
- Avoid shadows on every button, text fade-ins on every paragraph, hover lift on every card, or background glows everywhere. Interaction feedback should be restrained and consistent.
- Prefer system or existing project fonts. Avoid mixing decorative heading fonts without a business reason. Achieve visual quality primarily through typography, spacing, alignment, and hierarchy.

---

## 3. Zero-Noise Rules for Visible Copy

### 3.1 Strictly Distinguish Three Information Types

| Information type | Example | Allowed in UI? |
| --- | --- | --- |
| User **design/development instructions** | “Use a 12×12 grid,” “Use minimal grayscale styling,” “Implement file synchronization” | **Do not display directly**; implementation requirements only |
| **Explicitly requested UI content** | “Show ‘My Devices’ as the page title,” “Label the button ‘Connect Device’” | **Display as requested** |
| **Real product data and required states** | File names, device names, connection status, form labels, errors, and recovery actions | **Display as needed by the task** |

By default, prevent requirement descriptions, system prompts, feature lists, tech stacks, layout rules, development plans, and response explanations from entering the DOM, desktop views, mobile screens, or design mockups. Even if such text appears in the user prompt, treat it as an instruction first. Display it only when **explicitly requested as UI copy**.

### 3.2 Allowed UI Copy

Keep and encourage:

- **Navigation and orientation:** Page names, menu labels, paths, and necessary section headings.
- **Actions:** Specific button verbs, control labels, options, and keyboard shortcuts.
- **Business information:** Actual user content, fields, quantities, units, dates/times, and data descriptions.
- **Status and recovery:** Loading, completion, empty states, failure reasons, retries, and undo actions.
- **Essential guidance:** High-risk confirmations, privacy/permission explanations, critical assistance for complex tasks, and accessibility text.

Do not automatically add “This feature helps you...” beneath a clear, self-explanatory control. If position, headings, icons, or interaction already convey the information, remove redundant sentences. When there is too much text, reorganize information, progressively disclose details, or improve components instead of shrinking all explanatory content to fit.

### 3.3 Prohibited UI Copy

**Do not display the following in the UI by default:**

- Design self-description: `Clean modern interface`, `Uses a 12×12 grid system`, `Carefully crafted interactions`, `Design principles`.
- AI self-reference: `As requested`, `I have implemented this for you`, `Here is the feature showcase`, `Here we will`.
- Restated requirements: Turning `Multi-device mesh networking, pluggable capabilities, LAN-first connectivity, cloud backups...` into a long homepage paragraph unless a product introduction page was explicitly requested.
- Fabricated promises or numbers: `300% productivity improvement`, `Over 100,000 users`, `99.99% availability` without real evidence.
- Development/testing language: `TODO`, `Placeholder`, `Demo`, `Mock Data`, `API not connected yet`, `Feature under development`, `Component showcase`. Show real states or hide unavailable features in production UI.
- Decorative filler: `Unlock endless possibilities`, `Delivering the ultimate experience`, `All-in-one intelligent management`, `Make work more efficient`, `Welcome to the future`, and unnecessary second-line subtitles.
- Redundant explanatory labels: Repeatedly describing each card or button, adding an eyebrow above every heading, or naming purely structural regions “Feature Area.”

**Separate source comments from UI copy:** Necessary code comments may remain in source files, but comments, debug strings, and developer metadata must never become visible UI. Proactively remove framework-generated demo pages, documentation sections, and boilerplate content.

### 3.4 Copy Length and Accuracy

- Use consistent product terminology: `Devices`, `Files`, `Connections`, `Settings`. Prefer short phrases for navigation and buttons, not complete explanatory sentences added to fill space.
- Use precise action labels such as `Copy to This Device`, `Delete`, or `Retry`. Avoid vague labels such as `Get Started`, `Learn More`, or `Submit` unless genuinely appropriate.
- An empty state usually needs only a title, optionally one necessary explanation/help line, and one action. Avoid motivational filler, Emoji, and oversized decorative illustrations.
- Make errors specific and actionable, such as `Connection failed. Check your network and retry.` Do not omit critical error or risk details in the name of brevity.
- Do not fabricate user records, team members, testimonials, partnerships, or statistics. When a prototype needs sample data, use explicitly separated fake data **only in the development/preview data layer**, and never represent it as real production data.
- If content is insufficient, use genuine empty states, skeletons, or a minimal functional structure. Do not add feature sections, marketing copy, or extra cards merely to occupy grid space.

### 3.5 Content Inventory Before Design and Word-by-Word Review Afterward

Before generating, internally compile a “visible copy inventory” (never place it on the page): `page name → navigation → fields → actions → states → essential help`. Any text outside that inventory and actual business data must have a clear justification or be removed.

Before delivery, inspect the **rendered UI** for every text node, button, placeholder, pseudo-element `content`, tooltip, empty state, and demo entry:

1. Is anything copied or paraphrased from the user's **task instructions**? Remove it unless explicitly requested for display.
2. Is there design commentary, promotional filler, or text added just to fill space? Remove it.
3. Are there fabricated data, unsupported claims, or demo placeholders? Replace them with real data or genuine empty states.
4. Would removing the text undermine task completion, error recovery, or accessibility? Restore only the shortest necessary correct version.

> Example: If the request is “Build a minimalist grayscale file manager with Copy to This Device, using a 12×12 grid,” the page may show `Files`, `Devices`, and `Copy to This Device`. It must not automatically display `Minimalist Grayscale File Manager`, `12×12 Grid Design`, or `This system uses a modern layout` as titles or descriptions.

---

## 4. Only Three Responsive Grids

Grid notation means “columns × rows.” **Columns form the actual horizontal alignment system; rows are a logical guide for organizing the initial viewport.** Never lock scrolling page row heights just to satisfy the grid convention.

| Available workspace width | Grid | Recommended outer margin | Column gap | Typical structure |
| --- | --- | --- | --- | --- |
| **Desktop ≥1024px** | **12×12** | 32px | 20px | Navigation spans 2–3 columns; main content 9–10 columns |
| **Tablet 600–1023px** | **9×9** | 24px | 16px | Main content spans 6–9 columns; secondary regions may collapse |
| **Mobile <600px** | **4×12** | 16px | 12px | Main flow spans 4 columns; occasional 2+2 side-by-side layout |

- Choose based on **actual available page/workspace width**. A narrow desktop app window may use the tablet or mobile layout. For split views, sidebars, and embedded containers, prefer container queries or equivalent platform mechanisms.
- Align headings, navigation, lists, tables, and cards to column lines. Components may span multiple columns; individual controls do not each need to fill one cell.
- Title bars, sidebars, footers, and overlays need not be forced into identical column spans. Components may use Flex/Stack and local layouts internally.
- The `12/9/12` rows serve as logical groupings for an initial viewport or fixed workspace. Long pages, chats, tables, and lists use natural heights and scrolling. Do not clip content to force a fixed row count.
- Never add empty cards, extra headings, descriptions, or decorations to fill the grid. The grid organizes existing information.

**Minimal web implementation reference (prefer the project's existing layout system when available):**

```css
:root {
  --grid-cols: 4;
  --grid-rows-guide: 12;
  --page-margin: 16px;
  --grid-gap: 12px;
}
@media (min-width: 600px) {
  :root { --grid-cols: 9; --grid-rows-guide: 9; --page-margin: 24px; --grid-gap: 16px; }
}
@media (min-width: 1024px) {
  :root { --grid-cols: 12; --grid-rows-guide: 12; --page-margin: 32px; --grid-gap: 20px; }
}
.page-grid {
  display: grid;
  grid-template-columns: repeat(var(--grid-cols), minmax(0, 1fr));
  column-gap: var(--grid-gap);
  row-gap: var(--space-4, 16px);
  padding-inline: var(--page-margin);
}
.page-grid > * { min-width: 0; }
/* --grid-rows-guide is for planning only; do not use it as fixed grid-template-rows for ordinary scrolling containers. */
```

---

## 5. Typography, Tokens, Spacing, and Hierarchy

### 5.1 Simple, Semantic Tokens

Reuse existing project tokens first. For new projects, define at least:

```text
colors:  canvas / surface / surface-muted / text / text-secondary / border
         / primary / on-primary / focus / success / warning / danger
text:    title / section / body / meta / numeric
space:   4 / 8 / 12 / 16 / 24 / 32 / 48
radius:  none / small / medium / large
motion:  fast / normal / slow
layout:  columns / rows-guide / margin / gap
icons:   library / default-size / stroke-weight
```

- Base spacing on a 4- or 8-unit rhythm, allowing occasional fine adjustments. Use a consistent radius system instead of inventing a new radius for each card type.
- Keep typography levels limited (title, section, body, supporting text). Differentiate them with size, weight, line height, and spacing; avoid tiny low-contrast text.
- For Chinese body text, start with a line-height around `1.5–1.7`. Limit line length for long-form content. Use `tabular-nums` for numeric columns and changing numbers; truncate file names in the middle when necessary while preserving a way to view the full name.
- Recheck tonal steps, contrast, and typography in dark mode. Do not mechanically reduce all font weights by one level.
- For nested rounded shapes with uniform spacing, maintain visually concentric corners; an approximate outer radius of “inner radius + spacing” may help, but judge by the actual contours.
- Do not sacrifice control boundaries or visible focus indicators just to eliminate borders. `:focus-visible` outlines or double-ring shadows are acceptable if clearly distinguishable.

### 5.2 Information Hierarchy and Whitespace

- Identify the screen's primary task, primary action, and optional secondary actions. Let real functionality determine information density. Avoid gratuitous centering, oversized blank areas, and forced three-column layouts.
- Format similar information consistently; establish hierarchy through spacing, size, and necessary dividers rather than excessive nested cards.
- Dense admin interfaces, file managers, and developer tools may remain compact. A “premium” appearance does not require every container to have abundant whitespace.
- The less content a page has, the fewer components it should use. Do not explain away empty space with additional copy.

---

## 6. Components and Interaction Semantics

Prefer established components appropriate to the actual task:

| Purpose | Suggested component | Key checks |
| --- | --- | --- |
| Select field value | Select / Combobox / Radio | Selected value visible; search available for long option lists |
| Execute one of several actions | Dropdown Menu | Distinct from field selection; destructive actions prominent |
| Immediate toggle | Switch | On/off states clear; accessible name provided |
| Select multiple items | Checkbox | Label and click target aligned |
| Short decision/confirmation | Modal / Dialog | Focus handling, Escape, and cancellation behavior |
| Long settings/complex editing | Drawer / Full page | Avoid accidental closure and loss of input |
| Lightweight feedback | Toast | Does not obstruct actions; important errors remain accessible |
| Destructive action | Confirmation or undo mechanism | Accurate action label and explicit consequences |
| Additional information | Tooltip / Essential help | Keyboard-accessible on desktop; accessible on mobile |

- Components must support applicable `default`, `hover`, `focus`, `pressed`, `selected`, `disabled`, `loading`, `empty`, and `error` states. Do not hide all interactions behind hover.
- **IME:** Check `isComposing` and composition events before sending on Enter to avoid accidental submission during Pinyin candidate selection. Do not indiscriminately block all Enter presses for a fixed 500ms after `compositionend`.
- **Scrolling:** For streamed or incrementally loaded content, auto-follow only when the user is near the bottom. Pause when the user scrolls upward intentionally and provide a way to return to the bottom. Avoid per-character blur animation and costly compositing layers.
- **Dragging:** Use pointer capture or a mature library. Provide minimum panel widths, keyboard alternatives, and cancellation. Do not automatically close a panel when dragged past 80% unless requested.
- **Motion:** Transitions of approximately `100–300ms` are suitable for feedback and spatial changes. Avoid default staggered entrances, gratuitous bouncing, glows, and elaborate scroll animation. Respect reduced-motion preferences.
- **Copy is still subject to §3:** States, toasts, tooltips, and empty states must not contain AI self-reference, leaked prompts, filler, or Emoji.

---

## 7. Platform Differences and Accessibility

- **Web:** Use semantic HTML. Buttons perform actions; links navigate. Support font scaling and responsive layout. Fixed headers/footers must not conceal critical content. Avoid horizontal overflow at different widths.
- **Desktop:** Prioritize efficient workspaces, keyboard navigation, shortcuts, context menus, multiple panes, resizable layouts, and persistent layout preferences. Do not force mobile card patterns onto desktop software.
- **Tablet:** Support landscape/portrait orientation, touch, external keyboards, and split screen. Secondary navigation may collapse.
- **Mobile:** Provide adequately sized touch targets, safe-area and on-screen keyboard avoidance, and reachable primary actions. Avoid tiny complex overlays and deeply nested cards.
- **Accessibility:** For web, reference WCAG 2.2 AA: contrast ratio ≥4.5:1 for ordinary text/background and ≥3:1 for large text; visible focus, keyboard access, genuine form labels, accessible names for icon buttons, and error recovery. Never rely solely on color to convey states.
- **All platforms:** Support long text, localization, empty/loading/error states, and system font enlargement. Respect reduced-motion settings wherever animation is used.

---

## 8. Mandatory Pre-Delivery Review

**Do not inspect source code alone; prioritize the actual running UI, screenshots, and final visible content.** Where possible, validate representative desktop, tablet, and mobile widths.

### P0: Fix Immediately; Do Not Deliver

- [ ] AI-added Emoji used for navigation, buttons, features, illustrations, empty states, or prompts (except genuine user content).
- [ ] The interface renders user prompts, restated requirements, design/technical explanations, or internal system/developer information.
- [ ] The interface shows unauthorized realistic-looking statistics, fabricated customers/reviews/credentials, or unsupported marketing promises.
- [ ] Primary interactions are unusable, critical content is missing, severe accessibility barriers exist, or sensitive private information is exposed.

### P1: Visual and Usability Issues to Fix

- [ ] Unrequested blue-purple gradients, neon colors, colorful icons, meaningless strong accent colors, or arbitrary color coding.
- [ ] Unnecessary visible copy: decorative eyebrow labels, repeated subtitles, explanations of card functions, AI self-reference, and placeholder copy.
- [ ] Multiple inconsistent icon libraries, Emoji fallback glyphs, or misaligned/unclear icons.
- [ ] Violation of desktop `12×12` / tablet `9×9` / mobile `4×12` baselines, or content squeezed into fixed row counts.
- [ ] Missing essential states, inaccessible dialogs, invisible focus, accidental mobile touches, or layout overflow.

### P2: Detail Quality and Consistency

- [ ] Unnecessary multiple borders, shadows, nested cards, extra labels, or visual noise.
- [ ] Too many type levels, inappropriate line lengths, shifting numbers, or file names truncated so their extensions disappear.
- [ ] Excessive motion, scroll behavior overriding user control, unclear dark-mode hierarchy, or inadequate contrast.

**Review procedure:**

1. **Inspect icons:** Check navigation, buttons, states, cards, and empty states individually. Search newly written component strings for Emoji and inconsistent icon sources.
2. **Inspect colors:** Review CSS/theme variables and inline styles. For every non-neutral color, determine whether it is an existing brand color, a genuine semantic color, or explicitly requested by the user. Otherwise remove it.
3. **Inspect text:** Collect final visible text (DOM, screenshots, or native views) and check each item against the §3 blacklist for prompt leakage. Pay particular attention to `placeholder`, `title`, tooltips, pseudo-elements, and conditional branches.
4. **Inspect layout:** Check all three width classes, usable window width, scrolling content, long text, and empty states. Remove decorative regions added to fill the grid.
5. **Inspect behavior:** Test primary actions, keyboard, touch, loading/failure, dark mode if enabled, reduced motion, and accessible names.

If you cannot run the UI or capture screenshots, perform a static review and explicitly identify unverified areas. Never claim that visual acceptance testing has passed without verification.

---

## 9. Output Rules for Different Tasks

- **Generate UI:** Handle real content and primary flows first; follow §0–§8. Do not insert “design notes” or “development remarks” into the page. After implementation, briefly tell the user where changes were made, necessary technical decisions, and actual verification results.
- **Refactor UI:** Preserve existing business copy, real data, and core interactions. Remove redundant content, inappropriate colors, and incorrect icons only when supported by clear evidence. Do not indiscriminately erase a product's brand identity.
- **Review UI:** Report the most important issues as `location/evidence → severity → specific fix → verification method`. Do not assign unsupported “premium feel” scores or write review notes onto the page.
- **Explicit requests for strong branding, colorful illustration, marketing copy, or Emoji functionality:** Honor those requirements within their stated scope; maintain consistency, restraint, and accessibility elsewhere.

## References and Scope

The design principles of these projects have been selected, reorganized, and integrated into this Skill rather than copied verbatim from their original Skill files:

- Anthropic `frontend-design`: Practical purpose of UI content, avoidance of template-like layouts, and restrained motion. https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md
- `ui-ux-pro-max-skill`: Consistent icon style, SVG instead of Emoji, responsive layouts, and accessibility review. https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Vercel `web-interface-guidelines`: Icon-button labels, forms, focus, content overflow, and performance guidelines. https://github.com/vercel-labs/web-interface-guidelines
- SuperPlane `ui-copy`: Task-focused UI copy, actionable button labels, and removal of unnecessary text. https://github.com/superplanehq/superplane/blob/main/.agents/skills/ui-copy/SKILL.md
- `design-taste`: Avoidance of repetitive cards, exaggerated gradients, and default AI template patterns. https://github.com/madebymustafa/design-taste
- WCAG 2.2: https://www.w3.org/TR/WCAG22/

**Important:** The `12×12`, `9×9`, and `4×12` layouts are grid conventions specific to this Skill. Row counts are logical guides, not industry standards requiring web pages to have fixed row counts. The default grayscale palette and prohibition on AI-added Emoji and redundant copy are explicit design preferences of this project. Essential accessibility and business feedback always take priority.
