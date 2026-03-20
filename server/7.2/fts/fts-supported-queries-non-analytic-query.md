---
title: Non-Analytic Queries
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-non-analytic-query.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-supported-queries-non-analytic-query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-supported-queries-non-analytic-query.html)

# Non-Analytic Queries

Non-analytic queries do not support analysis on their inputs. This means that only exact matches are returned.

The following queries are non-Analytic queries:

* [Term](fts-supported-queries-term.md)
* [Phrase](fts-supported-queries-phrase.md)
* [Prefix](fts-supported-queries-prefix-query.md)
* [Regexp](fts-supported-queries-regexp.md)
* [Fuzzy](fts-supported-queries-fuzzy.md)
* [Wildcard](fts-supported-queries-wildcard.md)

For information on analyzers, see [Understanding Analyzers](fts-index-analyzers.md).