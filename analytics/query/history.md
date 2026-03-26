---
title: Use the Query History
description: The workbench for Capella Analytics maintains a history of all the
  queries you've executed.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/query/pages/history.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:analytics:query:history.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/query/history.html)

# Use the Query History

> The workbench for Capella Analytics maintains a history of all the queries you've executed. 

## [](#prerequisites)Prerequisites

To use the workbench for Capella Analytics:

* You must have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role in your organization, or one of the following [project roles](../../cloud/projects/project-roles.md) for the project that contains your cluster:

  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Database Data Reader/Writer](../../cloud/projects/project-roles.md#project-cluster-data-reader-writer) (Allows queries that read and write data)
  * [Database Data Reader](../../cloud/projects/project-roles.md#project-cluster-data-reader) (Allows read-only queries)

## [](#view-query-history)View Query History

The query history appears by default when you open the workbench. If you have been working with Capella iQ, click the **History** tab to re-open the query history.

You click an individual query to populate the query editor, where you can revise it if needed or run it.

If you edit a previous query and execute it, the new version of the query appears at the end of the history. Your query history is persistent across browser sessions.

The query history only saves queries. Due to limited browser storage, it does not save query results. As a result, when you restart the browser or reload the page you can see your old queries, but you must rerun a query to see its results.

> [!NOTE]
> Clearing the browser history clears the history maintained by the query editor as well.

## [](#query-history-options)Query History Options

You can use the following options to work with the list of queries in the history:

* **Search history** — You can search the query history by entering text in the **Filter Queries** search box. Capella Analytics lists all matching queries.
* **Delete a specific entry** — Click the Trash icon next to a particular query to delete it from the history.  
> [!TIP]  
> This can be useful if you want a more manicured history for when you're exporting it for future use.
* **Delete all entries** — Click **Clear** to delete the entire query history.
* **Import Query** — To load queries from a file into the Query History, click **Import** to open a file picker.
* **Export Query History** — To export the query history in JSON format, click **Export** to open the Export Query History dialog box. Enter a name for the file and click **Export**.

Click the **iQ** tab to replace the query history pane with the **iQ** coding assistant. See [Get Assistance from Capella iQ](iq.md).

## [](#see-also)See Also

* [Query and Explore with the Workbench](workbench.md)
* [SELECT Statements](../sqlpp/3%5Fquery.md)