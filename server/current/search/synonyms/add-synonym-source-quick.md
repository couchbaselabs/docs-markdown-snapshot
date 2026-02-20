---
title: Add a Synonym Source Using the Quick Editor
description: You can add a Synonym Source to set the collection where your
  synonym documents are stored with the Quick Editor.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/synonyms/add-synonym-source-quick.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:search:synonyms/add-synonym-source-quick.adoc[]
---

[View original HTML](/server/current/search/synonyms/add-synonym-source-quick.html)

# Add a Synonym Source Using the Quick Editor

> You can add a Synonym Source to set the collection where your synonym documents are stored with the Quick Editor. After you have set the synonym source for your Search index and any child fields, you can run any type of text-based Search query to return results with synonyms. 

For more information about synonym searches with the Search Service, see [Add Synonyms with the Quick Editor](synonyms-search-quick.md).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your database. For more information about how to deploy a new node and Services on your database, see [Manage Nodes and Clusters](../../manage/manage-nodes/node-management-overview.md).
* You have created an index with the Quick Editor. For more information, see [Create a Search Index with the Quick Editor](../create-quick-index.md).
* Your user account has the [Search Admin](../../learn/security/roles.md#search-admin) role for the bucket where you want to edit the Search index.
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To add a synonym source to a Search index with the Couchbase Server Web Console’s Quick Editor:

1. Go to **Search**.
2. Click the index where you want to add a new synonym source.
3. Click **Quick Edit**.
4. Do one of the following:

  1. To add synonyms to an existing text field, under **Mapped Fields**, click a text field mapping.
  2. To add synonyms to a new text field, click a text field in your sample document.
5. Click **Add Synonym Source**.
6. In the **Name** field, enter a name for your new synonym source. For example, you could call the source for a collection of English synonyms `synonyms_en`.
7. In the **Collection** list, select the collection where you stored your synonym documents for this specific synonym source.
8. In the **Language** list, select the language for your synonym collection. Choose the same language as the language or analyzer on the text field.
9. Click **Save**.
10. In the **Synonym Source** list, select the synonym source you added in the previous step.
11. If you added synonyms to an existing field mapping, click **Update**.
12. Click **Update Index**.

## [](#example-search-index-definition-with-synonyms)Example: Search Index Definition with Synonyms

For example, you could use the `travel-sample` dataset with the Quick Editor to create a Search index with synonyms.

First, create a new collection in the `travel-sample` bucket called `synonyms`. Include the following synonym documents:

```json
{
  "synonyms": [
    "cheap",
    "inexpensive",
    "affordable",
    "budget-friendly",
    "low-cost",
    "economical"
  ]
}
```

```json
{
  "synonyms": [
    "comfortable",
    "cozy",
    "relaxing",
    "snug",
    "pleasant",
    "restful"
  ]
}
```

Create a new Search index with the following field mappings:

* **Name**: Set to **Include in search results**.
* **Description**: Set to **Include in search results**, **Support highlighting**, and **Support phrase matching**.

Then, you could run the following Search query:

```json
{
  "explain": true,
  "fields": [
    "*"
  ],
  "highlight": {
    "style": "ansi"
  },
  "query": {
    "match": "cheap comfortable",
    "operator": "and",
    "field": "description"
  },
  "size": 40,
  "from": 0
}
```

The query would return results for hotels that include both `cheap` and `comfortable`, or one of their defined synonyms, like `affordable` in the `description` field. Results could include `hotel_18843` and `hotel_27821`.

## [](#next-steps)Next Steps

For more information about other features and options for Search indexes in the Quick Editor, see [Quick Index Field Options](../quick-index-field-options.md).