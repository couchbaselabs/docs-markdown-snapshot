---
title: Query Workbench
description: The Query Workbench provides a rich graphical user interface to
  perform query development.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/tools/pages/query-workbench.adoc
  xref: xref:7.6@server:tools:query-workbench.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/tools/query-workbench.html)

# Query Workbench

> The Query Workbench provides a rich graphical user interface to perform query development. 

Using the **Query Workbench**, you can conveniently explore data, create, edit, run, and save SQL++ queries, view and save query results, and explore the document structures in a keyspace — all in a single window.

Features of the Query Workbench include:

* A single, integrated visual interface to perform query development and testing.
* Easy viewing and editing of complex queries by providing features such as multi-line formatting, copy-and-paste, syntax coloring, auto completion of SQL++ keywords and keyspace and field names, and easy cursor movement.
* View the structure of the documents in a keyspace by using the SQL++ [INFER](../n1ql/n1ql-language-reference/infer.md) command. You no longer have to select the documents at random and guess the structure of the document.
* Display query results in multiple formats: JSON, table, and so on. You can also save the query results to a file on disk.

From the **Couchbase Web Console** select the **Query** menu. By default, the **Query Workbench** tab is displayed.

> [!NOTE]
> The Query Workbench only runs on nodes which are running the Query service. If the Query service is _not_ running on the current node, it provides a link to the nodes in the cluster which _are_ running the Query service.

The **Query Workbench** consists of three working areas as shown in the following figure:

* [Query Editor](#n1ql-editor)
* [Results](#results) — for query results and plans
* [Explore Your Data](#bucket-analyzer) — for data insights

![The Query Workbench with the Query Editor, Query Results, and Data Insights highlighted](_images/query-workbench-areas.png) 

Figure 1\. Query Workbench Areas

## [](#n1ql-editor)Use the Query Editor

The Query Editor is where you enter and edit queries.

The Query Editor provides the following additional features:

* **Syntax coloring** — For easy viewing, SQL++ keywords, numbers and string literals are differently colored.
* **Auto-completion** — When entering a keyword in the Query editor, if you press the Tab key or Ctrl+Space, the tool offers a list of matching SQL++ keywords and keyspace names that are close to what you have typed so far. For names that have a space or a hyphen (-), the auto-complete option includes back quotes around the name.
* **Auto-formatting** — Click the format icon  to reflow and indent the query to enhance readability.

Click the double-headed arrow icon  to enlarge the **Query Editor** and **Results** areas — the **Explore Your Data** area is resized accordingly.

## [](#run-a-query)Run a Query

After entering a query, you can execute the query either by typing a semicolon (`;`) and pressing Enter, or by clicking the **Execute** button. When the query is running, the **Execute** button changes to **Cancel**, which allows you to cancel the running query. When you cancel a running query, it stops the activity on the server side as well. After running the query, you can view the [query results](#results), view the [query execution plan](#query-plans), or get [index advice](#index-advisor) for the query.

> [!NOTE]
> The **Cancel** button does not cancel index creation statements. The index creation continues on the server side even though it appears to have been canceled from the Query Workbench.

You can also run a sequence of statements in the Query Editor. Each statement must be terminated with a semicolon. After each statement, you must press Shift+Enter to start a new line _without_ executing the query. When you enter the last statement, you can run the sequence of statements either by typing a semicolon (`;`) and pressing Enter, or by clicking the **Execute** button.

## [](#run-a-transaction)Run a Transaction

You can use the Query Editor to execute a Couchbase transaction. To execute a transaction containing multiple statements, compose the sequence of statements in the Query Editor. Each statement must be terminated with a semicolon. After each statement, you must press Shift+Enter to start a new line _without_ executing the query. You can then click **Execute** to execute the transaction.

You can also use the Query Editor to execute a single statement as a transaction. Simply enter the statement in the Query Editor and click **Run as TX**.

In either case, you do not need to specify the `txid` parameter or the `tximplicit` parameter. If you need to specify any other parameters for the Couchbase transaction, you can use the [query run-time preferences](#query-preferences) window.

## [](#query-context)Set Query Context

You can set the query context using the query context drop-down menu at the top right of the Query Editor. This specifies the bucket and scope used to resolve partial keyspace references within the request. When the query context is set, you can write queries using just the collection names, without having to enter the keyspace path.

![The query context menu with `travel-sample`.`inventory` selected](_images/query-workbench-context.png) 

The query context drop-down menu does not enable you to specify a namespace for the query context. Currently, only the `default` namespace is available. The default namespace is used for the query context.

To set the query context:

1. Using the context controls at the top right of the Query Editor, open the bucket drop-down menu and select the required bucket. When a bucket is selected, a scope drop-down menu is displayed to the right.
2. Open the scope drop-down menu and select the required scope.

To unset the query context, using the context controls at the top right of the Query Editor, open the bucket drop-down menu and select `unset`. The scope drop-down menu disappears.

To set the query context from the cbq shell or the REST API, use the [query\_context](../n1ql/n1ql-manage/query-settings.md#query%5Fcontext) request-level parameter.

For more information on scopes and collections, refer to [Scopes and Collections](../learn/data/scopes-and-collections.md).

## [](#view-query-history)View Query History

The tool maintains a history of all the queries executed. If you edit a previous query and execute it, the new query is stored at the end of the history. The history is persistent across browser sessions. The query history only saves queries; due to limited browser storage it does not save query results. Thus, when you restart the browser or reload the page, you can see your old queries, but you must re-execute the queries if you want to see their results.

> [!NOTE]
> Clearing the browser history clears the history maintained by the Query Editor as well.

Click the **history** link, at the top of the editor, to open the **Query History** window. When the window opens, the current query is selected.

![The Query History window with several queries displayed](_images/query-workbench-history.png) 

* You can scroll through the entire query history, and click to select an individual query.
* You can search the query history by entering a text in the search box located on the top. All matching queries are displayed. If no matching query is found, then the entire history is displayed.
* To delete a specific entry, select a query, then click **Delete Selected**. The query is deleted from the history.
* To delete all entries, click **Delete All**. The entire query history is deleted.
* To re-run a specific query, select a query, then click **Close & Run**. The query history is closed and the query is re-run.
* To close the query history, click **Close**. The query history is closed without making any further changes.

## [](#history-status)History Status

The currently shown position in the history is indicated by the numbers next to the history link. For example, **(151/152)** indicates that query #151 is currently shown, out of a total history length of 152 queries. Use the forward or back arrowhead icons  to move to the next or previous query in the history. The forward arrowhead icon  can also create a new blank query when you are already at the end of the query history.

## [](#results)View Query Results

When you execute a query, the results are displayed in the **Results** area. Since large result sets can take a long time to display, we recommend using the [LIMIT](../n1ql/n1ql-language-reference/limit.md) clause as part of your query when appropriate.

When a query finishes, the query metrics for that query are displayed to the right of the **Execute** button.

Status

Shows the status of the query. The values can be: success, failed, or HTTP codes.

Elapsed

Shows the overall query time.

Execution

Shows the query execution time.

Result Count

Shows the number of returned documents.

Mutation Count

Shows the number of documents deleted or changed by the query. This appears only for [UPDATE](../n1ql/n1ql-language-reference/update.md) and [DELETE](../n1ql/n1ql-language-reference/delete.md) queries instead of Result Count.

Result Size

Shows the size in bytes of the query result.

You can choose to view the results in several different formats. The sections below display the result of the following query in each of the available formats.

```sqlpp
SELECT r.airline, COUNT(1) num_routes, SUM(ARRAY_COUNT(r.schedule)) schedules
FROM `travel-sample`.inventory.route r
WHERE r.sourceairport = 'SFO'
GROUP BY r.airline, r.schedule;
```

### [](#json-format)JSON Format

Click **JSON** to display the results in JSON format. The results are highlighted to make the data easy to read. You can also expand and collapse objects and array values using the small arrow icons next to the line numbers.

![Query results in JSON format](_images/query-workbench-result-json.png) 

Click the copy icon  to copy the query results to the clipboard in tab-separated format.

Click the search icon  to search the results for the text you specify.

### [](#table-format)Table Format

Click **Table** to present the results in a tabular format. The tool converts the JSON documents to HTML tables, and presents sub-objects or sub-arrays as sub-tables. This format works well for queries that return an array of objects. You can hover the mouse pointer over a data value to see the path to that value in a tool tip. You can sort a column by clicking the column header.

![Query results in table format](_images/query-workbench-result-table.png) 

Click the copy icon  to copy the query results to the clipboard in tab-separated format.

### [](#chart-format)Chart Format

You can click **Chart** to present the results as a chart, as long as your query returns a suitable data series.

![Query results in chart format](_images/query-workbench-chart.png) 

You can select the type of chart and the data options from the drop-down controls at the top left of the chart.

To select the type of chart, open the **Chart Type** drop-down list ① and select a format for the chart: **X-Y**, **Connected Points**, **Line**, **Area**, **Bar**, **Grouped Bar**, **Pie**, or **Donut**.

For **X-Y**, **Connected Points**, **Line**, and **Area** charts:

* Open the **X-Axis** drop-down list and select the field for the x-axis of the chart.
* Open the **Y-Axis** drop-down list and select the field for the y-axis of the chart.

For **X-Y** charts only: open the **Color** drop-down list and select a color for the data points.

For **Bar**, **Grouped Bar**, **Pie**, and **Donut** charts:

* Open the **Label** drop-down list ② and select the field by which to categorize the data.
* Use the **Value(s)** list ③ to specify the data series to be rendered on the chart.

Click the download icon  to download the chart in SVG format.

## [](#query-plans)Query Plans

Each time a query is executed, an [EXPLAIN](../n1ql/n1ql-language-reference/explain.md) command is automatically run in the background to retrieve the query plan for that query.

To display the query plan, click the **Plan** link or the **Plan Text** link in the **Results** area. You may also generate the query plan and display the plan in graphical format by clicking **Explain**.

The sections below display the plan for the following query in each of the available formats.

```sqlpp
SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
```

### [](#plan)Plan

This is where the results are presented in a graphical format.

![Query plan in graphical format](_images/query-workbench-result-plan.png) 

① At the top, there is a summary which also shows lists of the keyspaces, indexes, and fields used by the query.

② At the bottom is a data-flow diagram of query operators, with the initial scans at the right, and the final output on the left. Potentially expensive operators are highlighted.

Once the query is complete, if you have selected the **Collect query timings** option in the preferences dialog, the query plan will be updated with timing information (where available) for each operation.

The data flow generally follows these steps:

1. Scan
2. Fetch
3. Filter
4. Projection (part 1)
5. Order
6. Projection (part 2)

> [!NOTE]
> Projection is split into two parts (one before Order and one after Order), but Query Workbench shows only the first part.

Clicking on any unit of the plan shows more details of it.

![Query plan in graphical format with Initial Project pop-up shown](_images/query-workbench_Plan.png) 

In general, the preference of scan is:

1. Covering Index
2. Index Scan
3. Intersect Scan
4. Union Scan, and finally
5. Fetch

### [](#plan-text)Plan Text

This simply shows the text output of the [EXPLAIN](../n1ql/n1ql-language-reference/explain.md) command.

![Query plan in JSON format](_images/query-workbench-result-plantext.png) 

## [](#index-advisor)Index Advisor

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

When you execute a [SELECT](../n1ql/n1ql-language-reference/selectintro.md) query, a [MERGE](../n1ql/n1ql-language-reference/merge.md) query, an [UPDATE](../n1ql/n1ql-language-reference/update.md) query, or a [DELETE](../n1ql/n1ql-language-reference/delete.md) query, an [ADVISE](../n1ql/n1ql-language-reference/advise.md) command is automatically run in the background to generate index advice for that query.

To display the index advice in graphical format, click the **Advice** link in the **Results** area. You may also generate the index advice and display the advice in graphical format by clicking **Index Advisor**.

When you run an ADVISE statement in the Query Workbench, you can use the **Table**, **JSON**, or **Tree** link to see the result, just like any other query. You can also use the **Advice** link in the Query Workbench to see the result of the ADVISE statement in graphical format.

### [](#advice)Advice

If there is any index advice for this query, the results of the Index Advisor are displayed under one or more of the following possible headings.

![Index advice for the query](_images/query-workbench-result-advice.png) 

Indexes Currently Used

The index or indexes currently used by this query are listed under this heading. (The exact name of this heading reflects the number of indexes that the query uses.)

Index Recommendations

If the Index Advisor can recommend any secondary indexes, array indexes, functional indexes, or partial indexes for this query, they are listed under this heading.

You can click **Create & Build Indexes** to create and build these recommended indexes. (The exact name of this button reflects the number of indexes that the Index Advisor recommends.) This process may take a while.

Covered Index Recommendations

If the Index Advisor can also recommend any [covering indexes](../n1ql/n1ql-language-reference/covering-indexes.md) for this query, in addition to the secondary indexes, array indexes, functional indexes, or partial indexes, they are listed under this heading.

You can click **Create & Build Covered Indexes** to create and build these recommended indexes. (The exact name of this button reflects the number of covering indexes that the Index Advisor recommends.) This process may take a while.

If there is no index advice for this query, the results area may display the one of the following messages:

* `Existing Indexes are Sufficient` — the existing indexes are sufficient for this query.
* `No index recommendation at this time` — the Index Advisor cannot recommend a query.
* `Advise supports SELECT, MERGE, UPDATE and DELETE statements only` — this query is not suitable for the Index Advisor.
* `Click 'Advise' to generate query index advice` — the Index Advisor has not yet been run.

Refer to [Recommendation Rules](../n1ql/n1ql-language-reference/advise.md#recommendation-rules) for details of the rules that the index advisor uses to recommend an index.

### [](#index-advice-in-community-edition)Index Advice in Community Edition

[COMMUNITY EDITION](https://www.couchbase.com/products/editions)

Note that in Couchbase Server Community Edition, index advice is provided in a different way. The area immediately below the **Query Editor** appears as follows:

![Execute button, Explain button, and External Query Advisor link](../manage/_images/manage-ui/ceIndexAdvisorLink.png) 

To get index advice, click the [External Query Advisor](https://index-advisor.couchbase.com/indexadvisor/#1) link to access the Couchbase **Index Advisor** web site.

## [](#bucket-analyzer)View Data Insights

The **Explore Your Data** area displays all installed keyspaces in the cluster. By default, when the Query Workbench is first loaded, it retrieves a list of available keyspaces from the cluster. The **Explore Your Data** area is automatically refreshed when keyspaces or indexes are added or removed.

Click the double-headed arrow icon  to enlarge the **Explore Your Data** area — the **Query Editor** and **Results** areas are resized accordingly.

Within the **Explore Your Data** area, buckets, scopes, and collections are displayed in a hierarchy, which you can expand or collapse.

* To expand a heading within the hierarchy, click the heading, or click the rightward-pointing arrowhead  before the heading.
* To collapse a heading within the hierarchy, click the heading again, or click the downward-pointing arrowhead  before the heading.

Buckets are displayed at the top level of the hierarchy. When you expand a bucket, the scopes within that bucket are displayed below it. Similarly, when you expand a scope, the collections within that scope are displayed below it.

The number of collections within the bucket is displayed to the right of the bucket heading. Similarly, the number of documents within a collection is displayed to the right of the collection heading. You may need to refresh the **Explore Your Data** area to see these figures. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

![Hierarchy of bucket, scopes, and collections in the Data Insights area](_images/query-workbench-insights-keyspaces.png) 

When you expand a collection, one or more headings are displayed showing the flavors (types) of document stored within that collection. The percentage of documents of each flavor is shown to the right. If there are any indexes within that collection, an **Indexes** heading is also displayed, showing the indexes within the collection.

You can expand any document flavor to view the schema for those documents: field names, types, and if you hover the mouse pointer over a field name, you can see example values for that field. Keyspace analysis is based on the SQL++ [INFER](../n1ql/n1ql-language-reference/infer.md) statement, which you can run manually to get more detailed results.

You can expand the **Indexes** heading to view the names and definitions of the indexes within the collection.

![Schema and indexes for a collection in the Data Insights area](_images/query-workbench-insights-infer.png) 

The information in the **Explore Your Data** area is updated regularly, but it may take a short time to reflect recent changes. To force the **Explore Your Data** area to update, click **Refresh**.

## [](#import-query)Import Data

You can load a query from a file into the Query Editor, or load a set of queries from a file into the query history.

1. Click **Import** to display the **Import Query / History** window.  
![The Import Query / History window](_images/query-workbench-import.png)
2. Specify the data that you want to import:  
Query  
Loads the imported query into the Query Editor.  
Query History  
Adds the imported queries to the end of the current query history.
3. Choose **Next** to continue, or **Cancel** to cancel.

> [!NOTE]
> The browser's Open File dialog is displayed. Locate and open a text file or JSON file containing the data you want to import.

Alternatively, you can drag and drop the file from the Desktop into the **Query Editor** to a load a file. The content of the file is added in the **Query Editor** as a new query at the end of the history.

## [](#export-query-or-results)Export Data

You can export the query statement, query results, or query history.

1. Click **Export** to display the **Export Query / Data / History** window.  
![The Export Query / Data / History window](_images/query-workbench-export.png)
2. Specify the data that you want to export:  
Current query results (JSON)  
Exports the results in the JSON file format.  
Current results as tab-separated (text)  
Exports the results as tab-separated text.  
Query history (JSON)  
Exports just the query history in the JSON file format.  
Query history including results (JSON)  
Exports the query history and results in the JSON format.  
Current Query Statement  
Exports the current query statement in the .txt format.
3. In the **Filename** box, specify the name of the file where data is to be saved. The file extension is added automatically. By default, the query is saved in the Downloads directory when using Firefox and Chrome browsers.
4. Choose **Save** to export the data, or **Cancel** to cancel.

> [!NOTE]
> When using Safari, clicking **Save** loads the data into a new window. You have to save the file manually using the **File** **Save As** menu.

## [](#query-preferences)Query Preferences

To specify the query settings:

1. Click the cog icon  near the top right of the Query Workbench. The **Run-Time Preferences** window is displayed.  
![The Run-Time Preferences window](_images/query-workbench-preferences.png)
2. Define the following options:  
Collect query timings  
The server records the timing for most operations in the query plan, showing the updated query plan with the query result. Both graphical and textual query plans are updated with the timing information when the query is complete.  
Automatically infer bucket schemas  
The query workbench automatically infers keyspace schemas to make field names available for autocompletion. In some cases this may impact server performance.  
Automatically format queries before executing  
The query workbench automatically formats queries with line breaks and indentation before executing.  
Use Cost-Based Optimizer  
Specifies whether the [cost-based optimizer](../n1ql/n1ql-language-reference/cost-based-optimizer.md) is enabled.  
Don't save query history  
Disables auto-saving query history to local storage in your browser. This is a consideration for shared machines. When selected, any query history will be lost when you leave or refresh the query workbench.  
Max Parallelism  
Specifies the maximum parallelism for the query. If you do not specify, the cbq-engine uses its default value. For more information, refer to the [max\_parallelism](../n1ql/n1ql-manage/query-settings.md#max%5Fparallelism%5Freq) parameter.  
Scan Consistency  
Specifies the consistency guarantee for index scanning. Select one of the following options:

  * not\_bounded
  * request\_plus
  * statement\_plus  
For more information, refer to the [scan\_consistency](../n1ql/n1ql-manage/query-settings.md#scan%5Fconsistency) parameter.  
Positional Parameters  
For prepared queries, this option allows you to specify values for any number of positional parameters. Click the **+** button to add new positional parameters, and the **\-** button to remove the parameters. The parameters are automatically labelled as **$1**, **$2**, and so on.  
Named Parameters  
For prepared queries, this option allows you to specify any number of named parameters. Named parameters must start with the dollar sign ($) for use in prepared queries. Otherwise, they are interpreted as parameters to the Query REST API.  
Query Timeout  
Specifies the maximum time to spend on a query before timing out. For more information, refer to the [timeout](../n1ql/n1ql-manage/query-settings.md#timeout%5Freq) parameter.  
Transaction Timeout  
Specifies the maximum time to spend on a transaction before timing out. Only applies to [BEGIN TRANSACTION](../n1ql/n1ql-language-reference/begin-transaction.md) statements, or statements executed with the **Run as TX** button. For more information, refer to the [txtimeout](../n1ql/n1ql-manage/query-settings.md#txtimeout%5Freq) parameter.
3. Choose **Save Preferences** to save the preferences, or **Cancel** to cancel.

---

[1](#%5Ffootnoteref%5F1). If there is no primary index on a collection, the count of documents within the collection includes any [transaction records](../learn/data/transactions.md#additional-storage-use) that may be stored in that collection. However, if there is a primary index on the collection, the count of documents does not include transaction records.