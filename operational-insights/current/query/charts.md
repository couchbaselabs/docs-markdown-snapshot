---
title: Visualize Results in Charts
description: After you run a query, you can visualize its results in graphical format.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/query/pages/charts.adoc
  xref: xref:enterprise-analytics:query:charts.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/query/charts.html)

# Visualize Results in Charts

> After you run a query, you can visualize its results in graphical format. 

## [](#prerequisites)Prerequisites

To use the Operational Insights UI, you need the `**Operational Insights Access**` role along with specific privileges.

## [](#configure-graph-settings)Configure Graph Settings

When you select the **Chart** tab in the query results pane, you can visualize query results in graphical format.

You select the type of graph, and then choose the fields—JSON keys—to include. For example, to populate a bar or pie chart:

* For the first, x-axis selection you choose a field with a string-type value
* For the second, y-axis selection you choose a number-type value.

For an X-Y graph, on the other hand, both fields must have number-type values.

For more information about working with sample datasets, see [Quick Start Tutorial](../intro/connecting-to-data-sources.md).

## [](#see-also)See Also

* [SELECT Statements](../sqlpp/3%5Fquery.md)
* [Use Business Intelligence Tools](bi.md)