---
title: Use the Query History
description: The workbench for Enterprise Analytics maintains a history of all
  the queries you've executed.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/query/pages/history.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:query:history.adoc[]
---

[View original HTML](/enterprise-analytics/current/query/history.html)

# Use the Query History

> The workbench for Enterprise Analytics maintains a history of all the queries you’ve executed. 

## [](#prerequisites)Prerequisites

To use the Enterprise Analytics UI, you need the `**Enterprise Analytics Access**` role along with specific privileges.

## [](#view-query-history)View Query History

In the UI, select the **Workbench** tab and click the **history** tab. You can scroll through the entire query history, and click an individual query to view that particular point in the history.

If you edit a previous query and execute it, the new version of the query appears at the end of the history. Your query history is persistent across browser sessions.

The query history only saves queries. Due to limited browser storage, it does not save query results. As a result, when you restart the browser or reload the page you can see your old queries, but you must rerun a query to see its results.

> [!NOTE]
> Clearing the browser history clears the history maintained by the query editor as well.

## [](#import-query)Import Queries

You can load a new query into the query editor from a JSON file. The query can be the [exported query](#export-query) from a different cluster.

> [!CAUTION]
> Importing a query overwrites your current query.

1. Click **Import**.
2. From the **Open** file window choose a local `.json` file that you want to import.
3. Click **Open**.  
The preexisting query is overwritten with the query of the imported file.

## [](#export-query)Export Query Statement or Results

You can export the current query statement or result to a `.txt` file, which you [import](#import-query) into other clusters.

1. Click **Export**.
2. Select **Query Results** or **Query Statement**.
3. Use the **File Name** field to specify a name for the exported file.
4. Click **Submit**.

## [](#query-history-options)Query History Options

You can use the following options to work with the list of queries in the history:

* **search history** — Search the query history by entering text in the **filter queries** search box. Enterprise Analytics lists all matching queries.
* **delete a specific entry** — Choose a specific entry and click **Delete Selected** to delete it from the history.  
> [!TIP]  
> This can be useful if you want a more manicured history for when you’re exporting it for future use.
* **Delete all entries** — Click **Delete all** to delete the entire query history.
* **Close & Run** — Click **Close&Run** to run the selected query.
* **Close** — Click **Close&Run** to close the **Query History** window.

## [](#see-also)See Also

* [Query and Explore with the Workbench](workbench.md)
* [SELECT Statements](../sqlpp/3%5Fquery.md)