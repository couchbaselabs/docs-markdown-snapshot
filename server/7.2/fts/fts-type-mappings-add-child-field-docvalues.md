---
title: Child Field DocValues
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-type-mappings-add-child-field-docvalues.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-type-mappings-add-child-field-docvalues.adoc[]
---

[View original HTML](/server/7.2/fts/fts-type-mappings-add-child-field-docvalues.html)

# Child Field DocValues

To include the value for each instance of the field in the index, the docvalues checkbox must be checked. This is essential for [Facets](fts-search-response-facets.md).

For sorting of search results based on field values: see [Sorting Query Results](fts-sorting.md).

By default, this checkbox is selected. If it is _unchecked_, the values are _not_ added to the index; and in consequence, neither Search Facets nor value-based result-sorting is supported.

## [](#example)Example

![fts type mappings child field docvalues](_images/fts-type-mappings-child-field-docvalues.png) 

> [!NOTE]
> When this checkbox is checked, the resulting index will increase proportionately in size.