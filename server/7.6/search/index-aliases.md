---
title: Create Search Index Aliases
description: A Search index alias lets you run a Search query against a Search
  index without using the original Search index name.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/index-aliases.adoc
  xref: xref:7.6@server:search:index-aliases.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/search/index-aliases.html)

# Create Search Index Aliases

> A Search index alias lets you run a Search query against a Search index without using the original Search index name. 

You can also use a Search index alias to run a Search query across multiple buckets, scopes, or Search indexes. The Search Service runs the Search query on each Search index in the alias, and returns a merged set of results.

Search index aliases are useful when you need to update an existing Search index.

For example, say you had a Search index, `old-index`, and an alias, `my-alias`.

If you wanted to make updates to `old-index`, you could add it to the alias `my-alias`. If you created a clone of `old-index`, then made your updates, you could replace `old-index` in the alias `my-alias`.

Using a Search index alias lets you edit `old-index` without any downtime.

For more information about how to create a Search index alias, see [Create a Search Index Alias with the Web Console](create-search-index-alias.md) or [Create a Search Index Alias with the REST API](create-search-index-alias-rest-api.md).

## [](#see-also)See Also

* [Create a Search Index Alias with the Web Console](create-search-index-alias.md)
* [Create a Search Index Alias with the REST API](create-search-index-alias-rest-api.md)
* [Import a Search Index Definition with the Web Console](import-search-index.md)