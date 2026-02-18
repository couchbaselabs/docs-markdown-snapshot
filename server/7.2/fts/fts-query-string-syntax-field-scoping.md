---
title: Field Scoping
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-query-string-syntax-field-scoping.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-query-string-syntax-field-scoping.html)

# Field Scoping

You can specify the field in which a search needs to be performed by prefixing the term with a field-name, separated by a colon.

The field-name may be a path to a field, using dot notation. The path must use Search syntax rather than [SQL++](#n1ql/n1ql-language-reference/index.html) syntax; in other words, you cannot specify array locations such as `[*]` or `[3]` in the path.

## [](#req-opt-exl)Required, Optional, and Exclusion

When a query string includes multiple items, by default these are placed into the SHOULD clause of a [boolean query](fts-supported-queries-boolean-field-query.md). You can adjust this by prefixing items with `+` or `-`.

* Prefixing with `+` places that item in the MUST portion of the boolean query.
* Prefixing with `-` places that item in the MUST NOT portion of the boolean query.

> [!TIP]
> You can use the preceding syntax to create [Compound Queries](fts-supported-queries-compound-query.md) in Search.

### [](#example)Example

For example, `description:pool` performs a [match query](fts-supported-queries-match.md) for the term `pool`, in the `description` field.

For example, `+description:pool -continental breakfast` performs a boolean query that MUST satisfy the match query for the term `pool` in the `description` field, MUST NOT satisfy the match query for the term `continental` in the `default` field, and SHOULD satisfy the match query for the term `breakfast` in the `default` field. Result documents satisfying the SHOULD clause score higher than those that do not.