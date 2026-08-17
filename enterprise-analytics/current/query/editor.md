---
title: Write and Run Queries
description: To query data in Enterprise Analytics collections you use SQL++, a
  SQL-for-JSON language specification that is similar to SQL.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/query/pages/editor.adoc
  xref: xref:enterprise-analytics:query:editor.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/query/editor.html)

# Write and Run Queries

> To query data in Enterprise Analytics collections you use SQL++, a SQL-for-JSON language specification that is similar to SQL. 

To support the full feature set of Enterprise Analytics, SQL++ for Enterprise Analytics, a customized and extended version of the SQL++ for Enterprise Analytics query language, is available. See [SQL++ for Enterprise Analytics](../sqlpp/1%5Fintro.md).

Enterprise Analytics uses rule-based optimization to query your collections until you run an `ANALYZE COLLECTION` statement on each collection involved in a query. As the data in a collection changes, you can run `ANALYZE COLLECTION` periodically to update the information used for CBO. See [Cost-Based Optimizer for Enterprise Analytics Services](../sqlpp/5b%5Fcbo.md).

## [](#prerequisites)Prerequisites

To use the Enterprise Analytics UI, you need the `**Enterprise Analytics Access**` role along with specific privileges.

## [](#query-editor)Using the Query Editor

The query editor is where you build and run queries. You can use the query editor's **Query Context** lists to set the database and scope you want a query to use.

You use SQL++ for Enterprise Analytics to write queries. For information about the SQL++ statements and syntax you use in Enterprise Analytics, see [DDL Statements](../sqlpp/5%5Fddl.md) and [DML Statements](../sqlpp/5%5Fdml.md).

> [!TIP]
> Since large result sets can take a long time to display, it's recommended that you use the `LIMIT` clause as part of your query when appropriate.

The query editor provides syntax highlighting. For easy viewing, SQL++ for Enterprise Analytics keywords, numbers, and string literals are differently colored.

You can use the **query options** to define request-level parameters, change the query timeout period, and so on. See [Set Query Options](options.md).

After entering a query, you can run the query to view the results. You can also view [metrics and the query plan](metrics-plan.md).

### [](#run)Run a Query

After you enter a query, click **Execute**.

> [!TIP]
> You can also execute a query by typing a semicolon `;` at the end of the query and then using the Enter key.

While the query is running, the **Execute** button changes to **Cancel**, which allows you to cancel the running query. You can also cancel DDL and DML statements. When you cancel a running query or statement, it stops the activity on the data source side as well.

When a query runs to completion, its results appear in the [query results pane](results.md) of the query editor.

## [](#see-also)See Also

* [SQL++ for Enterprise Analytics](../sqlpp/1%5Fintro.md)
* [Query and Explore with the Workbench](workbench.md)
* [Work with Query Results](results.md)