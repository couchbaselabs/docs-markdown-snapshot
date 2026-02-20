---
title: "Child Field - Include in_all field:"
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-type-mappings-add-child-field-include-in-all-field.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-type-mappings-add-child-field-include-in-all-field.adoc[]
---

[View original HTML](/server/7.2/fts/fts-type-mappings-add-child-field-include-in-all-field.html)

# Child Field - Include in_all field:

When checked, the field is included in the definition of **\_all**, which is the field specified by default in the **Advanced** panel. When unchecked, the field is not included.

Inclusion means when _query strings_ are used to specify searches, the text in the current field is searchable without the field name requiring a prefix. For Example, a search on description:modern can be accomplished simply by specifying the word ‘modern’. This is applicable for all query types and not just limited to query string query type.

## [](#example)Example

![fts type mappings child field include in all](_images/fts-type-mappings-child-field-include-in-all.png) 

> [!NOTE]
> "include in \_all" will write a copy of the tokens generated for a particular field to the "\_all" composite field. When this checkbox is checked, the resulting index will proportionately increase in size.

Enabling this option results in larger indexes, so disable this option to always use field scoped queries in the search requests.