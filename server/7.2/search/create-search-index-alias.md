---
title: Create a Search Index Alias with the Web Console
description: Use a Search index alias to run a Search query across multiple
  buckets, scopes, or Search indexes.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/create-search-index-alias.adoc
  xref: xref:7.2@server:search:create-search-index-alias.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/search/create-search-index-alias.html)

# Create a Search Index Alias with the Web Console

> Use a Search index alias to run a Search query across multiple buckets, scopes, or Search indexes. 

For more information about Search index aliases, see [Create Search Index Aliases](index-aliases.md).

## [](#prerequisites)Prerequisites

* You have created at least one Search index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To create a Search index alias with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click **Add Alias**.
3. In the **Index Name** field, enter a name for your Search index alias.
4. In the **Target Indexes** list, use CTRL \+ click to select each Search index that you want to add to the index alias.
5. Click **Create Index Alias**.

## [](#next-steps)Next Steps

To customize a Search index, see [Customize a Search Index with the Web Console](customize-index.md).

To run a search and test the contents of your Search index or Search index alias, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).