---
title: Query and Explore with the Workbench
description: The workbench for Operational Insights provides a graphical user
  interface for query development and data exploration.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/query/pages/workbench.adoc
  xref: xref:enterprise-analytics:query:workbench.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/query/workbench.html)

# Query and Explore with the Workbench

> The workbench for Operational Insights provides a graphical user interface for query development and data exploration. 

You use the workbench to manage your databases, scopes, and collections; create, run, and save SQL++ for Operational Insights queries; and view and save query results and metrics — all in a single window.

## [](#prerequisites)Prerequisites

To use the Operational Insights UI, you need the `**Operational Insights Access**` role along with specific privileges.

## [](#workbench-features)Workbench Features

Features of the workbench include:

* Controls for adding and managing databases, scopes, collections, links, and Iceberg catalogs. See [Data Model & Hierarchy](../sources/database-objects.md) and [sources:manage-external.adoc#iceberg-ui](../sources/manage-external.md#iceberg-ui).
* A single, integrated visual interface for query development and testing. The query editor offers multi-line formatting, copy-and-paste, and syntax coloring. See [Write and Run Queries](editor.md).
* Immediate display of metrics for executed queries and access to the query plan. See [View Query Metrics or Plan](metrics-plan.md).
* A query history for quick revision and re-execution. See [Use the Query History](history.md).
* Define query-specific settings, including a maximum time limit and positional parameters. See [Set Query Options](options.md).
* Options for displaying query results in JSON or table format, for copying or downloading query results in JSON format. See [Work with Query Results](results.md).
* Data visualization options for query results. See [Visualize Results in Charts](charts.md).
* Monitoring of active, completed, and open requests. See [Monitoring Queries](../sources/monitoring-queries.md).

## [](#accessing-the-workbench)Accessing the Workbench

To open the workbench, sign in to the Web Console and click **Workbench** in the navigation bar. The **Workbench** item is shown to users who can access the service.

The workbench has three tabs, across the top of the screen:

* **Workbench**: query development and data exploration, described on this page.
* **Monitor**: active, completed, and open requests, and service statistics. See [Monitoring Queries](../sources/monitoring-queries.md).
* **Samples**: sample data to load. See [Load Sample Data](#samples).

The **Workbench** tab has the following working panes:

* An explorer where you select, create, and manage links, catalogs, databases, scopes, and collections.
* The query editor.
* Options for reviewing query results and viewing query history.

## [](#samples)Load Sample Data

The **Samples** tab loads sample datasets, to give a quick-start example of Operational Insights capabilities.

The `travel-sample` dataset creates a database named `travel-sample`, with an `inventory` scope containing five collections: `airline`, `airport`, `hotel`, `landmark`, and `route`.

To load it:

1. In the workbench, click the **Samples** tab.
2. Select the **travel-sample** checkbox.
3. Click **Load Sample Data**.

A notification appears when loading starts, and another when it completes. Once a sample has been loaded, its checkbox is disabled.

For a walkthrough that uses this dataset, see [Quick Start Tutorial](../intro/connecting-to-data-sources.md).

## [](#see-also)See Also

* [Quick Start Tutorial](../intro/connecting-to-data-sources.md)
* [SELECT Statements](../sqlpp/3%5Fquery.md)