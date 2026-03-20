---
title: Query and Explore with the Workbench
description: The workbench for Capella Analytics provides a graphical user
  interface for query development and data exploration.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/query/pages/workbench.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:analytics:query:workbench.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/query/workbench.html)

# Query and Explore with the Workbench

> The workbench for Capella Analytics provides a graphical user interface for query development and data exploration. 

You use the workbench to manage your databases, scopes, and collections; create, run, and save SQL++ for Capella Analytics queries; and view and save query results and metrics — all in a single window.

![The Capella Analytics workbench. The organizational pane lists the databases, scopes, and collections currently in the cluster. The query editor shows a query context of the travel-sample database and the inventory scope. The most recent query displays in the editor, with results displayed below in JSON format. To the other side is the History and iQ tabs.](_images/workbench.png)

## [](#prerequisites)Prerequisites

To use the workbench for Capella Analytics:

* You must have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role in your organization, or one of the following [project roles](../../cloud/projects/project-roles.md) for the project that contains your cluster:

  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Database Data Reader/Writer](../../cloud/projects/project-roles.md#project-cluster-data-reader-writer) (Allows queries that read and write data)
  * [Database Data Reader](../../cloud/projects/project-roles.md#project-cluster-data-reader) (Allows read-only queries)

## [](#workbench-features)Workbench Features

Features of the workbench include:

* Controls for adding and managing databases, scopes, collections, and links. See [Access and Organize Data in Capella Analytics Services](../sources/database-objects.md).
* A single, integrated visual interface for query development and testing. The query editor offers multi-line formatting, copy-and-paste, syntax coloring, and easy cursor movement. See [Write and Run Queries](editor.md).
* Query-writing assistance from Capella iQ. See [Get Assistance from Capella iQ](iq.md).
* Immediate display of metrics for executed queries and access to the query plan. See [View Query Metrics or Plan](metrics-plan.md).
* A query history for quick revision and re-execution. See [Use the Query History](history.md).
* Define query-specific settings, including a maximum time limit and positional parameters. See [Set Query Options](options.md).
* Options for displaying query results in JSON or table format, for copying or downloading query results in JSON format, and for copying a flattened version of query results in TSV format. See [Work with Query Results](results.md).
* Data visualization options for query results. See [Visualize Results in Charts](charts.md).
* Options for saving results in views or tabular views. See [Save Views or Tabular Views](views-tavs.md).

## [](#accessing-the-workbench)Accessing the Workbench

1. Select the **Capella Analytics** tab.
2. Click the name of the cluster you want to work with. The workbench opens.

The workbench has the following working panes:

* An explorer where you select, create, and manage entities.
* The query editor.
* Options for reviewing query results.
* A query **History** tab that toggles with the **iQ** tab.

## [](#see-also)See Also

* [Access Data](../intro/examples.md)
* [SELECT Statements](../sqlpp/3%5Fquery.md)