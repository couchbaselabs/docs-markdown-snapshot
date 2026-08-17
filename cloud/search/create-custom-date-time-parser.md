---
title: Create a Custom Date/Time Parser
description: Create a custom date/time parser with the Couchbase Capella UI to
  tell the Search Service how to process a new date/time format.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/create-custom-date-time-parser.adoc
  xref: xref:cloud:search:create-custom-date-time-parser.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/search/create-custom-date-time-parser.html)

# Create a Custom Date/Time Parser

> Create a custom date/time parser with the Couchbase Capella UI to tell the Search Service how to process a new date/time format. 

If you store date data in a format other than RFC-3339 (ISO-8601), then you need to create a date/time parser.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have logged in to the Couchbase Capella UI.
* You have started to create or already created an index in [Advanced Mode Editing](create-search-indexes.md#advanced-mode).

## [](#procedure)Procedure

To create a custom date/time parser with the Capella UI in Advanced Mode:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Search Service.
3. Go to **Data Tools** **Search**.
4. Do one of the following:

  1. To work with an existing Search index, click the name of the index where you want to create a custom date/time parser.
  2. To create a new Search index, click **Create Search Index**.
5. Make sure to select **Enable Advanced Options**.
6. Expand **Global Index Settings**.
7. Click **Add Custom Date/Time Parser**
8. In the **Date/Time Parser Name** field, enter a name for the date/time parser.
9. In the **New Date and Time** field, enter a date/time layout with Go syntax.  
For more information, see the documentation about the [Go Programming Language Time Package's Layout Constant](https://pkg.go.dev/time#pkg-constants).
10. (Optional) To add an additional layout, click **Add** and enter a new layout.
11. Click **Add Custom Date/Time Parser**.

## [](#next-steps)Next Steps

After you create a custom date/time parser, you can [set it as the default date/time parser](set-advanced-settings.md#date-time) for your Search index.

To continue customizing your Search index, you can also:

* [Set a Document Filter](set-type-identifier.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Add Synonyms to a Search Index](synonyms/synonyms-search.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Capella UI](simple-search-ui.md).