[View original HTML](/cloud/clusters/query-service/query-workbench.html)

> Use the Query tab to develop and run SQL++ queries from your browser. 

With the **Data Tools** **Query** tab, you can also:

* Explore data
* Create, edit, and run queries
* Save SQL++ queries
* View and save query results
* Explore the document structures in a bucket

## [](#prerequisites)Prerequisites

* Your cluster must have the Query Service running.
* To view the Query tab and run queries that _read_ documents, you need the [Data Reader](../../projects/project-roles.md#project-cluster-data-reader) project role.
* To run queries that read and modify documents, you need the [Project Owner](../../projects/project-roles.md#project-owner-role) or [Data Writer](../../projects/project-roles.md#project-cluster-data-reader-writer) role.

## [](#access-the-query-tab)Access the Query Tab

To open the Query tab in a cluster running the Query Service:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Data Tools** **Query**.

The Query tab consists of three working areas:

* [Cluster Schema Browser](#insights-sidebar)
* [Query Editor](#query-editor)
* [Query Results and Plans](#results)

|  | You can expand and collapse the Cluster Schema Browser. You can vertically resize or expand the Query Editor and Results areas accordingly when you write queries or view query results. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#insights-sidebar)Cluster Schema Browser

The cluster schema browser (left pane) displays the buckets, scopes, and collections in the current cluster so you can browse your cluster schema. These keyspaces are in a hierarchy that you can expand or collapse.

* To expand or collapse a heading within the hierarchy, click the heading, or click the arrow before the heading.

Buckets appear at the top level of the hierarchy. When you expand a bucket, the scopes within that bucket appear below it. Similarly, when you expand a scope, the collections within that scope appear below it. The number of collections within the bucket is displayed to the right of the bucket heading.

### [](#add-a-bucket-scope-or-collection)Add a Bucket, Scope, or Collection

1. To add a new bucket, scope, or collection for your data in the cluster schema browser, click **+Create**.
2. Choose **New** and enter a name for your bucket, scope, or collection.
3. Click **Create**.  
For more information about how to create a bucket with custom settings, see [Create a Bucket](../data-service/manage-buckets.md#add-bucket).

## [](#query-editor)Query Editor

The query editor is where you build and run queries, and view query execution plans.

The query editor provides the following additional features:

* **Syntax coloring**: For easy viewing, SQL++ keywords, numbers, and string literals are differently colored.
* **Auto-completion**: Enter all or part of a keyword in the query editor and press Ctrl+Space to view a list of potential matching SQL++ keywords or bucket, scope, and collection names. For names that have a space or a hyphen (-), the auto-complete option includes back quotes around the name.
* **Support for SQL++ INFER statements**: Support the SQL++ [INFER](../../n1ql/n1ql-language-reference/infer.md) statement.

## [](#specify-bucket-and-scope-context)Specify a Bucket and Scope Context

You can specify the bucket and scope query context. When you set the query context to a bucket and scope, you can write queries using just the collection name without specifying the keyspace path.

For example, here’s how a query would look without specifying a bucket and scope in the query editor:

```sqlpp
SELECT * FROM `travel-sample`.`inventory`.`airline`;
```

If you specify the bucket as `travel-sample` and the scope as `inventory`, the query can be simplified to:

```sqlpp
SELECT * FROM `airline`;
```

To set the query context, from **Query Context**, choose a Bucket and Scope from the lists.

To remove the query context, choose **select a bucket** from the **Bucket** list.

For more information about scopes and collections, see [Buckets, Scopes, and Collections](../data-service/about-buckets-scopes-collections.md).

## [](#run-a-query)Run a Query

In the query editor, write a SQL++ query or use [Capella iQ](../../get-started/capella-iq/work-with-capellaiq.md) for assistance.

Use the **Format** button to improve the formatting and readability of your query before running it.

Once you have a statement ready, click **Run**.

|  | You can also execute queries by typing a semi-colon (;) at the end of the query and pressing Enter. |
|  | --------------------------------------------------------------------------------------------------- |

When the query is running, the **Run** button changes to **Cancel**, which allows you to cancel the running query. When you cancel a running query, it stops the activity on the cluster side as well.

|  | The **Cancel** button doesn’t cancel index creation statements. The index creation continues on the server side even though it appears to have been canceled from the query editor. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#query-settings)Modify Query Settings

You can specify various settings for the query editor by clicking **Query Options**.

Configure the following settings and click **Save Settings** to save the configuration.

| Option                   | Description                                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Collect query timings    | Collects per-operator query timings during query executions and displays them in a query plan. This option is selected by default.                                                                                                                                                                                                                     |
| Use Cost-Based Optimizer | Turns the cost-based optimizer on or off. For more information, see [Understand the Cost-Based Optimizer for Queries](../../n1ql/n1ql-language-reference/cost-based-optimizer.md).                                                                                                                                                                     |
| Don’t save query history | Disables auto-saving query history to local storage in your browser. This is a consideration for shared machines. When selected, any query history will be lost when you leave or refresh the query editor.                                                                                                                                            |
| Max Parallelism          | Specifies the maximum parallelism for the query. If you do not specify, the cbq-engine uses its default value. For more information about maximum parallelism, see the [max\_parallelism](../../n1ql/n1ql-manage/query-settings.md#max%5Fparallelism%5Freq) request-level parameter.                                                                   |
| Query Timeout            | The timeout parameter in seconds limiting the running time of a query. You can set this to a maximum of 1800 seconds                                                                                                                                                                                                                                   |
| Transaction Timeout      | Specifies the maximum time in seconds spent on a transaction before timing out.                                                                                                                                                                                                                                                                        |
| Scan Consistency         | This is a cbq-engine option. Select one of the following options: **Not Bounded** **Request Plus** **Statement Plus** For more information, see [Index Consistency](../../indexes/index-replication.md#index-consistency).                                                                                                                             |
| Positional Parameters    | For the prepared queries, this option allows you to specify values for $1, $2, and so on up to as many positional parameters as you have. Click the **+** button to add new positional parameters, and the **\-** button to remove the parameters. The parameters are automatically labeled as "$1", "$2", and so on.                                  |
| Named Parameters         | For the prepared queries, this option allows you to specify any number of named parameters. Click the **+** button to add new named parameters, and the **\-** button to remove the parameters. Named parameters must start with the dollar sign ($) for use in prepared queries. Otherwise, they are interpreted as parameters to the Query REST API. |

## [](#index-advice)Index Advice

The [ADVISE](../../n1ql/n1ql-language-reference/advise.md) command generates index advice to recommend indexes that optimize the response time for a query. You can use this command with [SELECT](../../n1ql/n1ql-language-reference/selectintro.md), [MERGE](../../n1ql/n1ql-language-reference/merge.md), [UPDATE](../../n1ql/n1ql-language-reference/update.md), or [DELETE](../../n1ql/n1ql-language-reference/delete.md) queries.

* To view index advice for a query entered into the query editor, click **Index Advice**. The query editor shows any suggested indexes by name and keyspace.
* To view updated advice after you change a query, or filter available indexes by bucket, scope, or collection, click **Update Advice**.

## [](#results)Query Results

When you execute a query, the results display in the query results area. Since large result sets can take a long time to display, it’s recommended that you use the [LIMIT](../../n1ql/n1ql-language-reference/limit.md) clause as part of your query when appropriate.

When a query finishes, metrics for that query appear between the query editor and the query results areas.

| Query Metric              | Description                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------ |
| The status of the query   | The values can be success, failed, or HTTP codes.                                    |
| **Last Run**              | The time at which the query was last executed.                                       |
| **Round-trip time (RTT)** | The total time it took to send the request and receive the response from the server. |
| **Docs**                  | The number of documents returned.                                                    |
| **Size**                  | The total size, in bytes, of the documents returned.                                 |
| **Elapsed**               | The time taken by the server to process the request.                                 |
| **Execution**             | The time taken by the server to execute the query.                                   |

### [](#table-format)Table Format

The **Table** tab presents the results in a tabular format. The tool converts the JSON documents to HTML tables and presents sub-objects or sub-arrays as sub-tables. This format works well for queries that return an array of objects, like `` select `beer-sample`.* from `beer-sample`; ``. Point to a data value to see the path to that value in a tooltip. You can sort the data based on a column by clicking the column header.

### [](#json-format)JSON Format

The **JSON** tab formats the results to make the data easy to read. You can also expand and collapse objects and array values using the small arrow icons next to the line numbers.

### [](#query-chart)Chart Format

You can click Chart to present the results as a chart, as long as your query returns a suitable data series.

You can select the type of chart and the data options from the drop-down controls at the top left of the chart. You can select the type of chart and the data options from the lists at the top left of the chart. To select the type of chart, in the Chart Type list, select a format for the chart: X-Y, Connected Points, Line, Area, Bar, Grouped Bar, Pie, or Donut.

### [](#iq-insights)iQ Insights Format

The **iQ Insights** tab lets you leverage the power of AI to generate relevant questions, descriptions, and visualizations of your query results. You can choose from any of these different responses and visualizations, and select those that best represent your data.

For more information about iQ Insights, see [Explore iQ Insights](../../get-started/capella-iq/explore-iq-insights.md).

#### [](#x-y-connected-points-line-and-area-charts)X-Y, Connected Points, Line, and Area Charts

1. In the **X-axis column** list, select the field for the x-axis of the chart.
2. In the **Y-axis column** list, select the field for the y-axis of the chart.

For X-Y charts only: in the **Color** list, select a color for the data points.

#### [](#bar-grouped-bar-pie-and-donut-charts)Bar, Grouped Bar, Pie, and Donut Charts

1. In the **Label** list, select the field to use to categorize the data.
2. In the **Value** list, specify the data series to be rendered on the chart.

### [](#plan)Plan

Each time you execute a query, an [EXPLAIN](../../n1ql/n1ql-language-reference/explain.md) command is automatically run in the background to retrieve the query plan for that query.

#### [](#results-plan)Plan

The **Plan** tab presents the query in a graphical format.

At the top, the tab shows a summary which also shows lists of the buckets, indexes, and fields used by the query.

At the bottom of the tab is a data-flow diagram of query operators, with the initial scans at the right, and the final output on the left.

Potentially expensive operators are highlighted.

The data flow generally follows these steps:

1. Scan
2. Fetch
3. Filter
4. Projection (part 1)
5. Order
6. Projection (part 2)

|  | Projection is split into two parts (one before Order and one after Order), but the query editor shows only the first part. |
|  | -------------------------------------------------------------------------------------------------------------------------- |

Click a unit of the plan to see more details about it.

An example query:

| Unit name          | Information shown when clicked                                                                                                                                                                                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Order              | {'#operator':'Order':'sort\_terms': \[{'expr':'(\`travel-sample\`.\`name\`)'}\]}                                                                                                                                                                                                                        |
| Project            | {'#operator':'InitialProject':'result\_terms': \[{'expr':'self','star':true}\]}                                                                                                                                                                                                                         |
| Filter             | {'#operator':'Filter','condition':'(((\`travel-sample\`.\`type\`) = \\'landmark\\') and ((\`travel-sample\`.\`city\`) = \\'San Francisco\\'))'}                                                                                                                                                         |
| Fetch              | {'#operator':'Fetch','keyspace':'travel-sample','namespace':'default'}                                                                                                                                                                                                                                  |
| IntersectScan      | (none)                                                                                                                                                                                                                                                                                                  |
| IndexScan2 (above) | {'#operator':'IndexScan2','index':'def\_city','index\_id':'d51323973a9c8458','index\_projection': {'primary\_key':true},'keyspace':'travel-sample','namespace':'default','spans': \[{'exact':true,'range':\[{'high':'\\San Francisco\\'','inclusion':3,'low':'\\'San Francisco\\''}\]}\],'using':'gsi'} |
| IndexScan2 (below) | {'#operator':'IndexScan2','index':'def\_city','index\_id':'a11b1af8651888cf','index\_projection': {'primary\_key':true},'keyspace':'travel-sample','namespace':'default','spans': \[{'exact':true,'range':\[{'high':'\\'landmark'\\'','inclusion':3,'low':'\\'landmark\\''}\]}\],'using':'gsi'}         |

In general, the preference of scan is

1. Covering Index
2. Index Scan
3. Intersect Scan
4. Union Scan
5. Fetch

### [](#results-plan-text)Plan Text

The **Plan Text** tab shows the [EXPLAIN](../../n1ql/n1ql-language-reference/explain.md) query execution plan in JSON format.

## [](#view-query-history)View Query History

The query editor maintains a history of all the queries executed.

If you edit a previous query and execute it, the new query is stored at the end of the history. The history is persistent across browser sessions. The query history saves queries; due to limited browser storage, it doesn’t save query results. When you restart the browser or reload the page, you can see your old queries, but you must re-execute the queries if you want to see their results.

|  | Clearing the browser history clears the history maintained by the query editor as well. |
|  | --------------------------------------------------------------------------------------- |

To open the **Query History** menu, click **History** .

You can scroll through the entire query history, and click an individual query to view that particular point in the history.

* **Search history**: You can search the query history by entering text in the **Filter saved queries** search box. All matching queries are displayed.
* **Delete a specific entry**: Click the Trash icon next to a query to delete it from the history.

|  | Deleting entries can be useful if you want a more manicured history when you [export the history](#export-query) for future use. |
|  | -------------------------------------------------------------------------------------------------------------------------------- |
* **Delete all entries**: Click the Trash icon next to the Export query history icon to delete the entire query history.

## [](#import-query)Import Queries

You can load a new query history into the query editor from a JSON file. The query history can be the [exported query history](#export-query) from a different cluster.

|  | Importing a query history overwrites your current query history. |
|  | ---------------------------------------------------------------- |

1. From the cluster’s **Data Tools** **Query** page, click **History**.  
This opens the **Query History** menu.
2. Click the Import query history icon next to the search box.
3. From the **Open** file window choose a local `.json` file that you want to import.
4. Click **Open**.  
The preexisting query history is overwritten with the query history of the imported file.

## [](#export-query)Export Query History

You can export the current query history to a JSON file, which you [import](#import-query) into other clusters.

1. From the cluster’s **Data Tools** **Query** page, click **History**.  
This opens the **Query History** menu.
2. Click the Export query history icon next to the search box.  
This opens the **Export Query History** window.
3. Use the **File Name** field to specify a name for the exported JSON file.
4. Click **Submit**.  
The window closes and the file downloads to your computer.