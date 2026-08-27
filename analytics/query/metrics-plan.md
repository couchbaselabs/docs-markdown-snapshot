---
title: View Query Metrics or Plan
description: The workbench for Capella Analytics provides metrics for each query
  you run, and a detailed query plan in both text and graphical format.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/query/pages/metrics-plan.adoc
  xref: xref:analytics:query:metrics-plan.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/query/metrics-plan.html)

# View Query Metrics or Plan

> The workbench for Capella Analytics provides metrics for each query you run, and a detailed query plan in both text and graphical format. 

## [](#prerequisites)Prerequisites

To use the workbench for Capella Analytics:

* You must have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role in your organization, or one of the following [project roles](../../cloud/projects/project-roles.md) for the project that contains your cluster:

  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Database Data Reader/Writer](../../cloud/projects/project-roles.md#project-cluster-data-reader-writer) (Allows queries that read and write data)
  * [Database Data Reader](../../cloud/projects/project-roles.md#project-cluster-data-reader) (Allows read-only queries)

## [](#review-query-metrics)Review Query Metrics

When a query finishes, metrics for that query appear on the workbench between the query editor and the query results panes. The metrics are:

* **Last Run** — The time at which the query was last executed.
* **Docs** — Shows the number of returned JSON documents.
* **Size** — Shows the size, in bytes, of the query result.
* **Elapsed** — Shows the overall query time.
* **Execution** — Shows the query execution time.

## [](#plan)View the Query Plan

Each time Capella Analytics executes a query, an EXPLAIN command automatically runs in the background to retrieve the query plan for that query.

You can view the query plan in the query results pane: select the **Plan** tab.

The **Plan** tab presents the query execution plan in a graphical format.

Capella Analytics uses rule-based optimization to query your collections until you run an `ANALYZE COLLECTION` statement on each collection involved in a query. The `ANALYZE` statement samples the data in a collection so that cost-based optimization (CBO) can be applied. As the data in a collection changes, you can run `ANALYZE COLLECTION` periodically to update the information used for CBO.

## [](#see-also)See Also

* [Query and Explore with the Workbench](workbench.md)
* [Cost-Based Optimizer for Capella Analytics Services](../sqlpp/5b%5Fcbo.md)
* [SQL++ for Capella Analytics](../sqlpp/1%5Fintro.md)