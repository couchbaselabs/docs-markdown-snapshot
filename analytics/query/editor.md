[View original HTML](/analytics/query/editor.html)

> To query data in Capella Analytics collections you use SQL++, a SQL-for-JSON language specification that is similar to SQL. 

To support the full feature set of Capella Analytics services, SQL++ for Capella Analytics, a customized and extended version of the SQL++ for Capella Analytics query language, is available. See [SQL++ for Capella Analytics](../sqlpp/1%5Fintro.md).

Capella Analytics uses rule-based optimization to query your collections until you run an `ANALYZE COLLECTION` statement on each collection involved in a query. As the data in a collection changes, you can run `ANALYZE COLLECTION` periodically to update the information used for CBO. See [Cost-Based Optimizer for Capella Analytics Services](../sqlpp/5b%5Fcbo.md).

## [](#prerequisites)Prerequisites

To use the workbench for Capella Analytics:

* You must have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role in your organization, or one of the following [project roles](../../cloud/projects/project-roles.md) for the project that contains your cluster:

  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Database Data Reader/Writer](../../cloud/projects/project-roles.md#project-cluster-data-reader-writer) (Allows queries that read and write data)
  * [Database Data Reader](../../cloud/projects/project-roles.md#project-cluster-data-reader) (Allows read-only queries)

## [](#query-editor)Using the Query Editor

The query editor is where you build and run queries. You can use the query editor’s **Query Context** lists to set the database and scope you want a query to use.

You use SQL++ for Capella Analytics to write queries. For information about the SQL++ statements and syntax you use in Capella Analytics, see [DDL Statements](../sqlpp/5%5Fddl.md) and [DML Statements](../sqlpp/5%5Fdml.md).

|  | Since large result sets can take a long time to display, it’s recommended that you use the LIMIT clause as part of your query when appropriate. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------- |

The query editor provides syntax highlighting. For easy viewing, SQL++ for Capella Analytics keywords, numbers, and string literals are differently colored.

You can use the **query options** to define request-level parameters, change the query timeout period, and so on. See [Set Query Options](options.md).

After entering a query, you can run the query to view the results. You can also view [metrics and the query plan](metrics-plan.md).

### [](#run)Run a Query

After you enter a query, click **Run Query**.

|  | You can also execute a query by typing a semicolon ; at the end of the query and then using the Enter key. |
|  | ---------------------------------------------------------------------------------------------------------- |

While the query is running, the **Run Query** button changes to **Cancel**, which allows you to cancel the running query. You can also cancel DDL and DML statements. When you cancel a running query or statement, it stops the activity on the data source side as well.

When a query runs to completion, its results appear below the query editor in the [query results pane](results.md).

## [](#see-also)See Also

* [SQL++ for Capella Analytics](../sqlpp/1%5Fintro.md)
* [Query and Explore with the Workbench](workbench.md)
* [Work with Query Results](results.md)