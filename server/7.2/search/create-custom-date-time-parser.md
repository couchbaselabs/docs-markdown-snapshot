---
title: Create a Custom Date/Time Parser
description: Create a custom date/time parser with the Couchbase Server Web
  Console to tell the Search Service how to process a new date/time format.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/create-custom-date-time-parser.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:search:create-custom-date-time-parser.adoc[]
---

[View original HTML](/server/7.2/search/create-custom-date-time-parser.html)

# Create a Custom Date/Time Parser

> Create a custom date/time parser with the Couchbase Server Web Console to tell the Search Service how to process a new date/time format. 

If you store date data in a format other than RFC-3339 (ISO-8601), then you need to create a date/time parser.

## [](#prerequisites)Prerequisites

* You’ve created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You’ve logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To create a custom date/time parser with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the Search index where you want to create a custom date/time parser.
3. Click **Edit**.
4. Expand **Customize Index** **Date/Time Parsers**.
5. Click **Add Date/Time Parser**
6. In the **Name** field, enter a name for the date/time parser.
7. In the **Layout to be added** field, enter a date/time layout with Go syntax.  
For more information, see the documentation about the [Go Programming Language Time Package’s Layout Constant](https://pkg.go.dev/time#pkg-constants).
8. Click **Add**.
9. (Optional) To add an additional layout, repeat the previous steps.
10. Click **Save**.

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