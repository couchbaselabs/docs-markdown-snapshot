---
title: Create a Custom Date/Time Parser
description: Create a custom date/time parser with the Couchbase Server Web
  Console to tell the Search Service how to process a new date/time format.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/create-custom-date-time-parser.adoc
  xref: xref:7.6@server:search:create-custom-date-time-parser.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/search/create-custom-date-time-parser.html)

# Create a Custom Date/Time Parser

> Create a custom date/time parser with the Couchbase Server Web Console to tell the Search Service how to process a new date/time format. 

If you store date data in a format other than RFC-3339 (ISO-8601), then you need to create a date/time parser.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* You have created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To create a custom date/time parser with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the Search index where you want to create a custom date/time parser.
3. Click **Edit**.
4. Expand **Customize Index** **Date/Time Parsers**.
5. Click **Add Date/Time Parser**
6. In the **Name** field, enter a name for the date/time parser.
7. In the **Layout Style** list, choose the specific layout style you want to use for your date/time parser.  
For more information, see [Date/Time Parser Layout Styles](date-time-parser-layout-styles.md).
8. In the **Layout to be added** field, enter your date/time layout, based on your chosen Layout Style.
9. Click **Add**.
10. (Optional) To add an additional layout, repeat the previous steps.
11. Click **Save**.

## [](#next-steps)Next Steps

After you create a custom date/time parser, you can [set it as the default date/time parser](set-advanced-settings.md#date-time) for your Search index.

To continue customizing your Search index, you can also:

* [Set the Type Identifier for a Search Index](set-type-identifier.md)
* [Create a Type Mapping](create-type-mapping.md)
* [Create a Child Field](create-child-field.md)
* [Create a Child Mapping](create-child-mapping.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Wordlist](create-custom-wordlist.md)
* [Set Search Index Advanced Settings](set-advanced-settings.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).