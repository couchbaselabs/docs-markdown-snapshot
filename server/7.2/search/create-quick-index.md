---
title: Create a Search Index with the Quick Editor
description: Use the Quick Index editor in Couchbase Server's Web Console to
  create a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/create-quick-index.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:search:create-quick-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/search/create-quick-index.html)

# Create a Search Index with the Quick Editor

> Use the Quick Index editor in Couchbase Server's Web Console to create a Search index. 

The Quick Index editor lets you select the fields that you want to add to a Search index with a document in your database.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your database.
* You have a bucket with scopes and collections in your database.
* Your user account has the **Search Admin** role for the bucket where you want to create the index.
* You've logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To use the Couchbase Server Web Console's Quick Editor to create a Search index:

1. Go to **Search**.
2. Click **Quick Index**.
3. In the **Index Name** field, enter a name for the index.
4. In the first **Keyspace** list, select the bucket where you want to create the index.
5. In the second **Keyspace** list, select the scope where you want to create the index.
6. In the third **Keyspace** list, select the collection where you want to create the index.
7. In the **Select Fields** box, click a field in the document that you want to add to the index.
8. In the **Type** list, select the field's data type.  
For more information about the available data types, see [Field Data Types](field-data-types-reference.md).
9. Set the field's options.  
For more information about the available field options, see [Quick Index Field Options](quick-index-field-options.md).
10. Click **Add**.
11. (Optional) Repeat the previous steps for each field you want to add to the Search index.
12. Click **Create Index**.

## [](#next-steps)Next Steps

You can [customize your index](customize-index.md) with the standard Search index editor to improve your Search index's performance and the quality of your search results.

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).