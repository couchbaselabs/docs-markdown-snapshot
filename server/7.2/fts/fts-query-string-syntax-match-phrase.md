---
title: Match Phrase
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-query-string-syntax-match-phrase.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-query-string-syntax-match-phrase.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-query-string-syntax-match-phrase.html)

# Match Phrase

Placing the search terms in quotes performs a match phrase query.

This query searches for terms in the target that occur in the positions and offsets indicated by the input: this depends on _term\_vectors_, which must have been included in the creation of the index used for the search.

## [](#example)Example

`"continental breakfast"` performs a [match phrase query](fts-supported-queries-match-phrase.md) for the phrase `continental breakfast`.