---
title: Create a Custom Character Filter
description: Create a custom character filter with the Couchbase Capella UI to
  remove unwanted characters from a Search query or the contents of a Search
  index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/create-custom-character-filter.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:search:create-custom-character-filter.adoc[]
---

[View original HTML](/cloud/search/create-custom-character-filter.html)

# Create a Custom Character Filter

> Create a custom character filter with the Couchbase Capella UI to remove unwanted characters from a Search query or the contents of a Search index. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have logged in to the Couchbase Capella UI.
* You have started to create or already created an index in [Advanced Mode Editing](create-search-indexes.md#advanced-mode).
* You have already created or started to create a [custom analyzer](create-custom-analyzer.md) in your Search index.

## [](#procedure)Procedure

To create a custom character filter with the Capella UI in Advanced Mode:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Search Service.
3. Go to **Data Tools** **Search**.
4. Do one of the following:

  1. To work with an existing Search index, click the name of the index where you want to create a custom character filter.
  2. To create a new Search index, click **Create Search Index**.
5. Make sure to select **Enable Advanced Options**.
6. Expand **Global Index Settings**.
7. Do one of the following:

  1. To create a new custom analyzer with a new character filter, click **Add Custom Analyzer**.
  2. To add a new custom character filter to use with an existing analyzer, expand the **Default Analyzer** list, and next to your custom analyzer, click **Edit**.
8. Click **Add Custom Character Filter**.
9. In the **Character Filter Name** field, enter a name for the character filter.  
> [!NOTE]  
> The Search Service supports only the **regexp** Type for character filters.
10. In the **Regular Expression** field, enter the regular expression for the character filter.  
Any analyzer that uses your character filter will remove any characters that match the regular expression from token results.  
For example, if you wanted to remove numeric characters from your tokens, you could use `[0-9]` as your regular expression.
11. (Optional) In the **Replacement** field, enter a string that replaces any matches for the regular expression.
12. Click **Add Custom Character Filter**.

## [](#next-steps)Next Steps

After you create a custom character filter, you can use it with [a custom analyzer](create-custom-analyzer.md).

To continue customizing your Search index, you can also:

* [Set a Document Filter](set-type-identifier.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Add Synonyms to a Search Index](synonyms/synonyms-search.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Capella UI](simple-search-ui.md).