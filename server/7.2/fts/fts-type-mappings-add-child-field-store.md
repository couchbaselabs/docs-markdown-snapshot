---
title: Child Field Store
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-type-mappings-add-child-field-store.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-type-mappings-add-child-field-store.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-type-mappings-add-child-field-store.html)

# Child Field Store

When the child field 'store' option is checked, the original field content is included in the FTS index, enabling the retrieval of stored field values during a search operation.

When unchecked, the original field content is not included in the FTS index. Storing the field within the index is necessary to support highlighting, which also needs "term vectors” for the field to be indexed.

## [](#example)Example

![fts type mappings child field store](_images/fts-type-mappings-child-field-store.png) 

Ideally, enabling this 'Child Field Store' option has a sizing aspect to the index definition. This option also permits highlighting of search texts in the returned results, so that matched expressions can be easily seen. However, enabling this option also results in larger indexes and slightly longer indexing times. The field content will show up in queries (when the index has the store option checked) only when requested. There is a ‘fields’ section in the query for it.

{
"query": {...},
"fields": ["store_field_name"]
}
Setting "fields" to ["*"] will include the contents of all stored fields in the index.

> [!NOTE]
> "store" - writes a copy of the field content into the index. When this checkbox is checked, the resulting index will proportionately increase in size.