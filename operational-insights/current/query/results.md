---
title: Work with Query Results
description: The query results pane of the workbench provides options for
  displaying, copying, downloading, and otherwise working with the results of a
  query.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/query/pages/results.adoc
  xref: xref:enterprise-analytics:query:results.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/query/results.html)

# Work with Query Results

> The query results pane of the workbench provides options for displaying, copying, downloading, and otherwise working with the results of a query. 

## [](#prerequisites)Prerequisites

To use the Operational Insights UI, you need the `**Operational Insights Access**` role along with specific privileges.

## [](#results)Review JSON Formatted Results

When you execute a query, the results display in the query results pane. By default, the **JSON** tab displays in the query results pane, showing the results in JSON format.

You can expand and collapse objects and array values using the small arrow icons next to the line numbers.

## [](#review-tabular-formatted-results)Review Tabular Formatted Results

The **Table** tab presents the results in a tabular format. Operational Insights converts the JSON documents to HTML tables for this display, and presents sub-objects and sub-arrays as sub-tables. This format works well for queries that return an array of objects.

## [](#download-or-copy-results)Download or Copy Results

When you view query results on the **JSON** tab, click **Export** to download the results in JSON format. You can also click the copy button next to **Query Results** to copy the results in JSON format.

You can then use the file with the query results as needed, or paste the results into another tool such as a spreadsheet.

## [](#see-also)See Also

The query results pane also offers these options for working with results:

* [Visualize Results in Charts](charts.md)
* [View the Query Plan](metrics-plan.md#plan)