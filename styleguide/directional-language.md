---
title: Directional Language
editUrl: https://github.com/couchbaselabs/docs-style-guide/edit/main/styleguide/modules/ROOT/pages/directional-language.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:styleguide::directional-language.adoc[]
---

[View original HTML](/styleguide/directional-language.html)

# Directional Language

Do not use directional language to describe where UI elements are located to the user. Directional language includes words like:

* up
* down
* left
* right
* above
* below

To avoid directional language, do not describe the UI visually, or in relation to other UI elements, where possible. Stick to button names or icons as much as possible.

If the automatic Vale rule flags a use of directional language:

* If the usage is describing values, such as `a value above 10` or `a value below 20`, rewrite the sentence to use `a value greater than 10` or `a value less than 20`, respectively.
* If the usage is in a valid phrase, such as `back up`, let the tooling team know so that an exception can be added to the rule.