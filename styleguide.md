# Couchbase Style Guide

This file consolidates the key rules and guidelines from the Couchbase Style Guide for use when generating or editing Couchbase documentation.

---

## 1. General Principles

- **American English** spelling throughout. Use Merriam-Webster's Collegiate Dictionary, Eleventh Edition, as the reference.
- **Present tense** only. Never write in past or future tense.
  - ✅ Couchbase Capella deploys your cluster.
  - ❌ Couchbase Capella will deploy your cluster.
- **Second person** (`you`). Do not use first person (`we`, `our`, `us`, `let's`) or third-person gendered pronouns.
- **Active voice**. Start sentences with verbs or address the user directly. Identify the actor. Avoid forms of `be`, `occur`, and `happen` as the main verb. Use passive voice only when active voice loses the correct emphasis or doesn't make sense.
- **Plain language**. Avoid jargon when a simpler word works. Use contractions (with restrictions — see Contractions section).
  - ✅ You can set a Bucket name.
  - ❌ You can configure a Bucket name.
- **Short sentences and paragraphs**. Keep sentences under 25 words. Avoid more than 2 commas per sentence. Do not write walls of text — break content up with headings, paragraphs, and lists.

---

## 2. Voice and Tone

The Couchbase voice is **confident**, **reassuring and empathetic**, **approachable**, and **opinionated and visionary**.

**Avoid:**

| Avoid | Why | Example to avoid |
|---|---|---|
| Humor | Distracts; doesn't translate | *It's not CRUDDY to use CRUD operations!* |
| Personal opinions | Keep statements objective and accurate | *Couchbase Server 7.1 is the best version.* |
| Colloquial language and topical expressions | Culture-specific; becomes outdated | *It's lit!* / *It's daft to set your memory too low.* |
| Aspirational statements | Write about what the product does now | *Someday, Couchbase may support this feature.* |
| Marketing or selling the product | Show users how to use features; don't advertise | *Couchbase's Storage Auto-Expansion is designed to handle your ever-growing data needs.* |
| Only describing features | Write about what the user can do, not just feature descriptions | *A Full Text Search Response Object is itself composed of multiple child-objects.* |

Aim for a neutral, helpful tone. Think about what drove the user to the documentation and give them what they need to be successful.

---

## 3. Capitalization

- Capitalize the first word of every sentence, proper nouns, days of the week, months, holidays, country/nationality/language names, trademarks, and SQL/SQL++ clauses.
- Follow **official capitalization** for brand names, companies, software, products, services, and other terms defined by companies or open-source communities.
- Do **not** use unnecessary capitalization. Do not use all-caps except for official names, abbreviations, or code that uses all caps.
- Do **not** use camelCase unless the name or code being referenced uses it.
- For specific terms, refer to the A-Z Word List (Section 20).

**Headings** use **title case** per the Chicago Manual of Style:
- Always capitalize the first word.
- Capitalize main nouns, verbs, and adjectives.
- Leave articles, coordinating conjunctions, and prepositions lowercase (`and`, `the`, `to`, `of`).

---

## 4. Headings

- Use headings to split content and aid scanning.
- **Title case** for all headings (Chicago Manual of Style rules).
- Keep headings **short and to the point** — ideally fit in a single line.
- Add a heading whenever starting a new thought or highlighting something new. Always include content between any two consecutive headings.
- Maximum heading depth: **H4**. Do not go deeper.
- Do **not** add parentheses to headings.

**H1 heading style by content type:**

| Content Type | Heading Style | Examples |
|---|---|---|
| Concept topic | Single noun (or short noun phrase) accurately describing the concept | Clusters; Indexes |
| How-to or Tutorial topic | Short imperative phrase starting with a verb | Delete a Cluster; Create an Index; Explore Your Data |
| Reference topic | Short phrase stating what kind of reference content the user finds | Audit Events; Error Messages; Rebalance Reports |

---

## 5. Contractions

Use contractions to keep writing plain and approachable, with the following restrictions:

**Do NOT use:**
- Negative contractions (`can't`, `don't`, `couldn't`, `shouldn't`, `isn't`, etc.) — write them out in full.
- Informal contractions (`wanna`, `gonna`).
- Complex contractions (`could've`, `might've`, `should've`, `we've`, `who'd`, `would've`, `you've`, etc.).

**Acceptable contractions only:**

| Contraction | Meaning |
|---|---|
| it's | it is; it has |
| that's | that is; that has |
| there's | there is; there has |
| they'd | they had; they would |
| they'll | they will; they shall |
| they're | they are |
| what's | what is; what has |
| where's | where is; where has |
| who's | who is; who has |
| you'd | you had; you would |
| you'll | you will; you shall |
| you're | you are |

---

## 6. Articles (a, an, the)

- Use **a** before consonant sounds; use **an** before vowel sounds.
  - an hour, an HTML file, a hotel, an umbrella, a union
- For abbreviations, the article depends on pronunciation: `an FAQ` (spelled out) / `a` (if pronounced as a word).
- Specific article guidance:
  - A SQL (database)
  - An FAQ

---

## 7. Numbers

**Always use numerals**, regardless of size. Do not spell out numbers as words (contrary to Google Style Guide).

- ✅ 1 or more, 2-day total, 3-node cluster
- Use commas to separate every group of 3 digits in large numbers (e.g., 1,000,000).

---

## 8. Text Formatting

### Bold (`**text**`)

Use bold to format:
- Single menu items
- Tab names
- Dialog names
- Button names (via the `btn:[]` macro)
- UI element names generally (page names, toggle names, option names, etc.)

Do **not** bold words just for emphasis in prose.

For buttons, use the `btn:[]` macro. For menu navigation, use the Menu UI Macro. For keyboard shortcuts, use the `kbd:[]` macro.

### Italics

**Do not use italics** in Couchbase documentation. Do not surround text with underscores (`_`) for emphasis.

### Monospace font (backticks)

Use monospace (`` `code` ``) for:
- Any code that appears outside a code block
- N1QL/SQL++ commands and function names
- API methods, classes, and calls
- File paths and filenames
- Any text a user must input

### Quotation Marks

Do **not** use quotation marks outside of inline code or code blocks. Use bold or monospace for emphasis instead.

---

## 9. Punctuation

### Colons
- Use to introduce examples (a code block, an image).
- Use to introduce ordered or unordered lists.

### Commas
- Use the **Oxford comma** for inline lists.
- If an inline list has more than 3 items, convert to a bulleted or numbered list.
- Avoid more than 2 commas per sentence (Vale flags this as a potential run-on).

### Dashes
- **Em dash** (—): Set off an aside or comment. Do not use parentheses or an en dash for this purpose.\
  Example: *An em dash is a great piece of punctuation — but it can be easily overused.*
- **En dash** (–): Represent a range of numbers, dates, or time.\
  Example: *choose a number in the range of 1–4*
- **Hyphen** (-): Join compound adjectives.\
  Example: *full-text search*

### Parentheses
- Use **sparingly**.
- Do **not** use to set off asides — use an em dash instead.
- **Must use** when defining an unfamiliar acronym for the first time: *the Alphabet Biscuit Club (ABC)*.
- Always acceptable inside code blocks.
- Do **not** add to headings.

### Semi-Colons
- Avoid semi-colons. Use a period and shorter sentences instead.
- For complex items in a list, convert to a numbered or bulleted list.

### Slashes
- Avoid `/` and `\` outside inline code, code blocks, or file paths.
- Do **not** write `and/or` — choose `and` or `or`.

---

## 10. Grammar Rules

### Which vs. That

- Use **which** before a non-defining/non-essential clause (with a comma before it). Removing the clause does not change the core meaning.
  - *The Capella database, **which** you deployed yesterday, is healthy.*
- Use **that** before a defining/essential clause (no comma). Removing the clause changes the meaning.
  - *The Capella database **that** you deployed yesterday is healthy.*

### There is / There are

Do **not** start a sentence with `there` + a form of `to be` (`there is`, `there are`, `there were`, `there was`). These constructions hide the true subject and verb.

Instead:
- Remove the construction.
- Move the true subject and verb.
- Create a subject for the sentence.

  ❌ *There are multiple variables that store the result.*\
  ✅ *Multiple variables store the result.*\
  ✅ *You can store the result in multiple variables.*

### Only

Place **only** as close as possible to the word it modifies. Placement changes meaning:
- *Only deploy a Capella database this month.* (Do nothing else)
- *Deploy only a Capella database this month.* (No other database type)
- *Deploy a Capella database only this month.* (Only this month)

### Less vs. Fewer

- **Less**: For uncountable/mass nouns or quantities measured rather than counted (less time, less effort). Also for distances, sums of money, units of time/weight, and statistics.
- **Fewer**: For countable nouns (fewer databases, fewer indexes, fewer status updates).

### Latin Abbreviations

**Do not use** `e.g.`, `i.e.`, or `etc.` Use these alternatives:

| Instead of | Use |
|---|---|
| e.g. | for example |
| i.e. | specifically |
| etc. | and so on |

### Directional Language

Do **not** use directional words to describe UI element locations:
- Avoid: up, down, left, right, above, below.
- For values, use `greater than` or `less than` instead of `above` or `below`.

---

## 11. Headings and Page Structure

### Writing Concept Topics

A concept explains the *why* behind a procedure or reference material.

**Structure:**
- **`:description:` attribute**: A brief explanation of the concept goal at the top of the file.
- **Body**: Explain technical concepts/jargon; use headings; link to related procedures/references; cover only 1 focused topic; keep paragraphs to 5 sentences or fewer.
- **See Also** (required H2): An unordered list of links to related tasks, references, or concepts.

### Writing Procedure Topics (How-tos and Tutorials)

A **how-to guide** explains how to accomplish a goal with variable end results. A **tutorial** explains how to accomplish a goal with a defined end result.

**Required sections (all H2):**
1. **Prerequisites**: An unordered list of things the user must do or have before starting. Always link where appropriate.
2. **Procedure**: An ordered list of steps to complete the goal.
   - One action per step (exception: menu navigation with Menu UI Macro).
   - Start each step with the location where the action occurs.
   - Use `btn:[]` for buttons, `kbd:[]` for keyboard, monospace for code/file paths/user input, bold for menu items/tab names/dialog names.
   - Do not document obvious results or add lengthy explanations in steps — link to concept docs instead.
3. **Next Steps** (not "See Also"): An unordered list of links or running text for what the user does next. Always link.

### Writing Reference Topics

A reference provides detailed lookup information (API docs, UI option tables, property lists).

**Structure:**
- **`:description:` attribute**: Brief explanation of what the reference covers.
- **Body**: Use tables, description lists, and headings for scanability.
- **See Also** (required H2): An unordered list of links to related tasks, concepts, or references.

---

## 12. Lists

### Ordered Lists

Use when **order matters** (procedures, sequences of tasks). Must use for procedure steps. Can use in concepts when order matters.

- It's acceptable to have a procedure with only 1 step.

### Unordered Lists

Use when you have **3 or more items** and order does not matter. If you only have 2 items, write them out in a sentence.

Always use unordered lists for:
- Prerequisites sections
- See Also sections
- Navigation (`nav.adoc`) files
- Even if the section contains only a single item.

**Punctuation in unordered lists:**
- Add ending punctuation when each item is a complete sentence or a phrase of more than 3 words.
- No ending punctuation for simple 1–3 word noun phrases (e.g., Availability Zones, Database Option).

---

## 13. Links

- Introduce all links with: `For more information, see {link}.`
- Do **not** use: `Refer to`, `For more details`, or similar.
- Do not use the URL itself as the link text. Write descriptive link text.
- For **internal links** (within the Couchbase docs repos), use the `xref` syntax. Leave the link text blank to auto-use the page's H1 heading.
- For **external links**, follow Google Developer Style Guide guidance.
- When linking to SDK or API references, use **evergreen links** where possible.

---

## 14. Images and Diagrams

### Screenshots
- Use **strategically and sparingly** — they go out of date quickly.
- Use **PNG** format.
- **Concept topics**: Avoid screenshots; use Kroki diagrams. Add 1 screenshot only if a textual explanation would be insufficient.
- **How-tos/Tutorials**: Do not screenshot every step. Only add a screenshot for unexpected or hard-to-explain results.
- **Reference topics**: Avoid images.
- Frame images well — do not show unnecessary UI. Do not capture unstable UI.

**Annotations:** Use a transparent rectangle with a solid 5px Couchbase Red border (Hex: `#EA2328`). No rounded corners.

### Diagrams
- Use **Kroki** to generate diagrams to reduce static image maintenance.
- Save diagrams in **SVG format**.
- Use **PlantUML** language to generate diagrams.

### Alt Text (required on all images)

- **Describe** the image plainly, as if to someone who cannot see it.
- **Be concise** — give the most relevant details a sighted user would get at a glance.
- **End with a period**.
- Do **not** start with "image of" (screen readers add this automatically).
- Do **not** add alt text on icons that already have text labels, or on purely decorative images.

---

## 15. Admonitions

Do not use more than 2 admonitions back-to-back on a page. Do not overuse them. (If everything is important, nothing is.)

| Type | When to Use |
|---|---|
| **Note** | Non-critical information; something to keep in mind; highlight a specific point |
| **Tip** | Shortcut or optional step; useful but not critical; also mention when API accomplishes the same task as UI |
| **Warning** | Data loss or irreversible damage; irreversible actions |
| **Caution** | Code that is not extensively tested; something that might cause an error; deprecated features |
| **Important** | Cross-version changes; behavior that works differently than before; place at the top of a page or section |

---

## 16. Tables

- Use tables to show **relationships between information** (e.g., properties and their descriptions).
- Introduce the table with a phrase ending in a colon: *The following default options are available:*
- Make column names **short but descriptive**.
- If a table has more than 2 columns, set proportional column widths using the `[cols=""]` attribute.

---

## 17. Code Examples

- Add code examples where possible to show users how to work with Couchbase products.
- **Do:**
  - Make examples relevant and applicable to the explanation.
  - Ensure the code sample is functional and usable in real projects.
  - Put code examples in separate files (not inline in the `.adoc` file).
  - Use the correct [placeholder format](#18-code-placeholders).
- **Do not:**
  - Include cultural references.
  - Write code samples directly inside the `.adoc` file.

**Introducing examples:**
- Use `See the following example:` or `For an example of how to use X, see the following:`
- Do **not** use directional language like `above` or `below`. Use `preceding`, `previous`, or `following`.
- End the introducing phrase with a colon.

**Explaining code examples:**
- Avoid built-in callouts where possible.
- Use small code examples with surrounding text explanation.
- For larger examples: show the full example with a brief explanation, then progressively extract and explain smaller pieces.

---

## 18. Code Placeholders

| Context | Format | Example |
|---|---|---|
| curl / shell | `$` prefix + ALL_CAPS + underscores | `$DATABASE_NAME` |
| REST API path attributes | `{}` + ALL_CAPS + underscores | `{PORT}` |
| Other (if `{}` or `$` not supported) | `<>` + ALL_CAPS | `<YOUR_ATTRIBUTE>` |

---

## 19. Anchor Links

- Create your own anchor links — do **not** rely on Antora's auto-generated ones.
- Keep them **short** (3–5 words max), **unique** on the page, **all lowercase**, **words separated by dashes**, **no punctuation**.
  - Example: `[#generate-api-keys]`

| Element | Anchor Style |
|---|---|
| Headers, full tables, lists, other block elements | `[#anchor-link]` |
| Table entries, inline text | `[[anchor-link]]` |

- Link to another page: `xref:name-of-page.adoc#anchor-link`
- Link on the same page: `<<anchor-link,Link Text>>`

---

## 20. Filenames

- Use **dashes** to separate words (`-`).
- Use **lowercase** for all characters. Use capitals only for acronyms.
- Keep filenames **descriptive but concise** (4–5 words).
- Topic files: `.adoc` extension.
- Image files: `.png` extension.

**Image filename convention:** `[product]-[description]-[version].png`
- Example: `server-cluster-manager-architecture-7.1.png`
- Example: `capella-billing-usage-summary-7.0.png`

Do **not** retroactively rename published topic files (causes broken links and redirects).

---

## 21. UI Element Terminology

### Buttons
- Refer to by name only — do **not** add "button" after the name.
- Use the `btn:[]` macro: `btn:[Submit]` → **Submit**
- If the element navigates the user to a new location, use the Menu UI Macro instead.

### Menus
- Refer to as **[Name] menu** (bold name, plain "menu").
- Refer to menu items by name only — do **not** add "menu item".
- For tab + menu navigation sequences, use the **Menu UI Macro**: `menu:File[Save]` → **File** > **Save**

### Menu UI Macro
Use the Menu UI Macro for:
- Any selections that significantly change the page or navigate to a new page.
- Sequences of tab and menu navigation.
- The Profile menu.
- Hamburger or **More Options** menus (⋮ or …).

### Keyboard Macro
Use the `kbd:[]` macro for all keyboard interactions: `kbd:[ESC]`

### Tabs (UI)
- Refer to as **[Name] tab** (bold name, plain "tab").
- User **selects** a tab to open a page.

### Pages (UI)
- Refer to as **[Name] page** (bold name, plain "page").
- Bold the page name; do not bold "page".

### Dialogs
- Refer to as **[Name] dialog** (bold name, plain "dialog").
- Use the dialog title as it appears in the UI (match capitalization). Do not bold "dialog".

### Dropdowns/Lists
- Refer to as **[Name] list** (bold name, plain "list").
- Tell the user to "select x in the list."
- Example: *In the **Bucket** list, select a bucket.*

### Options (Radio buttons / cards)
- For the option set: **[Name] option** (bold name, plain "option"). Describe or link to the available options.
- For a specific option: Use the name directly — do **not** add "option".
  - ✅ *Under **Plan**, select **Basic**.*
  - ❌ *Select the Basic option under Plan.*

### Toggles
- Refer to as **[Name] toggle** (bold name, plain "toggle").
- Use `turn on` or `turn off` — not "enable/disable."

### More Options Menu (⋮)
- Refer to as **More Options** (⋮) menu.
- Use `&vellip;` for the HTML entity.
- Use the Menu UI Macro for navigation inside: **More Options** (⋮) > **Delete**.

### Mouse Over / Hover
- Do **not** use: mouse over, hover over, hover.
- Use `point to` instead: *Point to the collection you created and click **+**.*

### UI Links (clickable text in prose)
- Do **not** refer to clickable UI text as a "link."
- Just use the name: `Click Learn More` or `Click Edit on GitHub`.

### Describing Values
- Use `greater than` and `less than` for numerical comparisons.
- Do **not** use: higher, lower, above, below.

---

## 22. Tabbed Content in Documentation

Use tabbed content in procedures when presenting **2 distinct, branched paths** (e.g., AWS vs. GCP vs. Azure, or code samples in different languages).

**Use when:**
- Instructions differ across cloud service providers or user environment choices.
- Code samples in different languages accomplish the same task.
- Prerequisites differ based on environment.

**Do NOT use when:**
- The user must follow all tab content (tabs are not substitute for sequential steps).
- Tab content cannot stand alone without relying on other tabs.

---

## 23. Structural Elements to Avoid

- **Sidebars**: Avoid. Do not use `[sidebar]` or a line of 4 asterisks (`****`). Do not use sidebars for See Also sections.
- **Italics**: Do not use.
- **Quotation marks** (outside code): Do not use.
- **Semi-colons**: Avoid.
- **Latin abbreviations** (`e.g.`, `i.e.`, `etc.`): Do not use.
- **Directional language** (`above`, `below`, `left`, `right`): Do not use to describe UI locations.

---

## 24. A-Z Word List — Key Terms

This is a selection of important terms. For terms not listed here, refer to the [Google Developer Style Guide Word List](https://developers.google.com/style/word-list).

| Term | Rule |
|---|---|
| .NET | Include the period. Follow Microsoft capitalization. |
| Numbers | Always write as numerals (1, 2, 3…). Use commas every 3 digits. |
| a / an | See Articles section. `a SQL`, `an FAQ`. |
| about | Use "information about," not "information on," before a link. |
| admin | Do not use. Write out `administrator`. |
| ad hoc | Never hyphenate. Use `adhoc` for the SQL++ parameter. No italics. |
| adapter | Use `adapter`, not `adaptor`. |
| afterwards | Use `afterwards`, not `afterward`. |
| allowlist / denylist | One word each. No hyphen. Do not use whitelist/blacklist/blocklist/passlist/access list. |
| Analytics Service | Legacy. Use `Capella Analytics` or `Enterprise Analytics`. |
| API | Do not spell out on first use. |
| app / application | `app` for mobile; `application` for client software like Couchbase Server. |
| auto-failover | Hyphenate. Verb form: `automatically fails over`. |
| backend | Noun: `backend`; adjective: `back-end`. |
| backup | Noun/adjective: `backup`; verb: `back up`. |
| beta release | Use before the product name. Only `Beta` after the product name. |
| big data | Two words, no hyphen, no capitalization. |
| bytes | `kB/MB/GB/TB/PB` for decimal; `KiB/MiB/GiB` for binary. |
| Capella Analytics | Proper product name for analytics on Capella. Do not use `Columnar` or `Couchbase Columnar`. |
| cluster | Preferred term for Couchbase Server or Capella instances (not `instance` or `database`). |
| collection | Do not capitalize. |
| command line | Noun: `command line`; adjective: `command-line`. |
| config / configs | Do not use. Use `configuration` (noun) or `configure` (verb). |
| Couchbase Capella | Use `operational cluster` to specify vs. Capella Analytics. |
| Couchbase Server n.n | Full name first use. `Server n.n` afterwards. Never "the Couchbase Server." |
| cross datacenter replication (XDCR) | Spell out first use, lowercase, no hyphen. |
| curl | All lowercase. |
| data center | Two words, no hyphen. |
| database | Do not capitalize (Capella Analytics context). Do not use to refer to Capella operational clusters. |
| Deprecated | Use to indicate a feature will be removed in a future release. Specify that it will be removed. |
| different from | Use `different from`, not `different than` or `different to`. |
| disassociate | Preferred term. Do not use `dissociate` or `unassociate`. |
| e-commerce | Lowercase with hyphen. Capitalize as `E-commerce` only at start of sentence. |
| earlier / later | Use for software version comparisons. Not `older/newer` or `lower/higher`. |
| email | No hyphen. |
| end user | Noun: `end user`; adjective: `end-user`. |
| ensure | Do not use. Use `make sure`. |
| Enterprise Analytics | On-premises Couchbase Analytics product name. Not `Analytics Service` or `Columnar`. |
| eviction / ejection / expiration | Use precisely: eviction = removed entirely; ejection = removed from one layer but not the system; expiration = deleted after TTL. |
| FAQ | `An FAQ` (spelled out) or `a FAQ` if pronounced as a word. |
| failover | Noun: one word. Verb: two words (`fail over`). |
| fewer | For countable nouns. |
| filename | One word, no hyphen. |
| full-text indexes | Hyphenate. Use `Search Service`, not `Full-Text Search (FTS)`. |
| GitHub | Follow official capitalization. |
| hard-coded / hard-wired | Hyphenate both. |
| hostname | One word. |
| indexes | Do not use `indices`. |
| in-memory | Hyphenate. |
| install | Verb: `install`; noun: `installation`. |
| instance | Do not use. See `cluster`. |
| Internet | Capitalize as a proper noun. |
| Internet of Things (IoT) | Spell out first use. Lowercase `o` in `of`. |
| key-value | Hyphenate. |
| less | For uncountable nouns and measured quantities. |
| log in | Verb: `log in`; adjective: `log-in`; noun: `login`. |
| master / slave | Do not use. Use `primary / secondary`. |
| metadata | One word, no hyphen. |
| microservices | One word, no hyphen. |
| N1QL | Old term for SQL++. Do not use except in legacy documentation. |
| note that | Do not use. |
| on demand | Noun: `on demand`; adjective: `on-demand`. |
| on-premises | Noun: `on premises`; adjective: `on-premises`. |
| one can | Do not use. Address the user directly with `you`. |
| open source | No hyphen. |
| page | Use to refer to what a user accesses from a menu or tab. |
| peer to peer | Noun: no hyphens; adjective: `peer-to-peer`. |
| plug in | Noun: `plugin`; adjective: `plug-in`; verb: `plug in`. |
| primary / secondary | Use instead of master/slave. |
| real time | Noun: two words; adjective: `real-time`. |
| rebalance | One word, no hyphen. |
| refer to | Do not use. Use `see`. |
| repo | Do not use. Write out `repository`. |
| Role-Based Access Control (RBAC) | Spell out first use. Capitalize as proper product name. |
| schema-less | Hyphenate. Lowercase. Or use `flexible schema`. |
| SDK | Do not spell out on first use. Pluralized as `SDKs`. |
| see | Use instead of `refer to` for introducing links. |
| setup | Noun: `setup`; adjective: `set-up`; verb: `set up`. |
| sign up | Verb: `sign up`; adjective: `sign-up`. |
| SQL++ | The Couchbase query language. Pronounced "sequel plus plus". Use `a SQL++`. |
| time series | Two words, sentence case, no hyphen. |
| time to live (TTL) | Lowercase. Spell out on first use. |
| towards | Use `towards`, not `toward`. |
| Transactions | Use `Distributed ACID Transactions` on first use. `Distributed Transactions` or `Transactions` on subsequent uses. |
| under construction | Use for incomplete/in-progress pages. Do not use `wip` or `work in progress`. |
| vBucket | Lowercase `v`, capitalize `Bucket`. |
| web | Do not use all caps. |
| web page | Do not use. Use `page`. If must use, two words, no hyphen. |
| whitepaper | One word, no hyphen. |
| Wi-Fi | Hyphenate. Capitalize `W` and `F`. Do not use `wifi` or `WiFi`. |
| XDCR | Cross Data Center Replication. Spell out on first use. |
| yellow | Use `amber` for traffic lights or health warning colors. |

---

## 25. Data Insights Area (Capella UI)

- Capitalize `Data Insights`, but do **not** bold it. Do not bold or capitalize `area`.
- Top-level items in the area: **buckets**, then **collections**, then **scopes**, then **schemas**.

---

*This style guide is based on the Couchbase documentation style guide. For terms not covered here, refer to the [Google Developer Style Guide](https://developers.google.com/style/).*
