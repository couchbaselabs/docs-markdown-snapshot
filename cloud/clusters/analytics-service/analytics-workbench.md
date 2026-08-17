---
title: Analytics Workbench
description: The Analytics Workbench provides a rich graphical user interface to
  perform Analytics query development.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/analytics-service/analytics-workbench.adoc
  xref: xref:cloud:clusters:analytics-service/analytics-workbench.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/analytics-service/analytics-workbench.html)

# Analytics Workbench

> The Analytics Workbench provides a rich graphical user interface to perform Analytics query development. 

Using the **Analytics Workbench**, you can conveniently explore data, create, edit, run, and save SQL++ for Analytics queries, view and save query results, explore Analytics scopes and Analytics collections, and view the Couchbase buckets which are being shadowed — all in a single window.

Features of the Analytics Workbench include:

* A single, integrated visual interface to perform Analytics query development and testing.
* Easy viewing and editing of complex queries by providing features such as multi-line formatting, copy-and-paste, syntax coloring, and easy cursor movement.
* View the Analytics scopes and Analytics collections available to the Analytics Service and the Couchbase buckets that are being shadowed.
* Display query results in JSON or table formats. You can also save the query history to a file on disk.

For more information on Couchbase Analytics, see the [Analytics section](../../../server/current/learn/services-and-indexes/services/analytics-service.md) in our Couchbase Server documentation.

> [!NOTE]
> The Analytics Workbench is only available on clusters that are running the [Analytics Service](analytics-service.md).

## [](#accessing-the-analytics-workbench)Accessing the Analytics Workbench

If a cluster is running the [Analytics Service](analytics-service.md), the Analytics Workbench can be accessed under the cluster's **Data Tools** **Analytics** tab.

The **Analytics Workbench** consists of the following working areas:

* The [Analytics Editor](#query-editor), at the top of the Analytics Workbench.
* The [Analytics Query Results and Plans](#results), at the bottom of the Analytics Workbench.
* The [Analytics Scopes](#insights-sidebar), to the right of the Analytics Workbench.

## [](#query-editor)Using the Analytics Editor

The Analytics Editor is where you build and run queries. Enter a query into the Analytics Editor using the [SQL++ for Analytics](../../../server/current/analytics/1%5Fintro.md) language. Since large result sets can take a long time to display, it's recommended that you use the [LIMIT](../../../server/current/analytics/3%5Fquery.md#Limit%5Fclauses) clause as part of your query when appropriate.

The Analytics Editor provides syntax highlighting: for easy viewing, SQL++ keywords, numbers, and string literals are differently colored.

After entering a query, you can execute the query to view the results or view the query plan.

## [](#add-a-collection)Add a Collection

The Analytics Workbench allows you to add collections to make them available in Analytics. To create an Analytics collection on a local link:

1. Inside the Analytics Scopes area, click the **Add Collection** () button next to the link where you want to create the collection.  
This opens the **Add Collection** flyout.
2. In the **Name** box, enter a name for the Analytics collection.
3. Use the **Bucket**, **Scope**, and **Collection** drop-down lists to specify the data source for this Analytics collection.
4. (Optional) If needed, in the **Where** field, enter an expression to filter the documents in the collection. You must not include the WHERE keyword, and the expression must be deterministic. For example, `activity = "eat"`.
5. Click **Create** add the collection.  
The new collection will appear just below the local link.

## [](#run-an-analytics-query)Run an Analytics Query

To run the query, click **Execute**.

> [!TIP]
> You can also execute queries by typing a semi-colon (`;`) at the end of the query and hitting Enter.

When the query is running, the **Execute** button changes to **Cancel**, which allows you to cancel the running query. When you cancel a running query, it stops the activity on the cluster side as well.

When you execute a query, the results are displayed in the [Query Results](#results) area. You can view the query results in JSON format or Table format. By default, when you execute a query, the **JSON** tab is selected in the Query Results area, showing the results in JSON format.

## [](#explain-an-analytics-query)Explain an Analytics Query

Each time a query is executed, an EXPLAIN command is automatically run in the background to retrieve the query plan for that query. You may also generate the query plan without running the query by clicking **Explain**.

You can view the query plan in the [Query Results](#results) area.

## [](#results)Viewing the Query Results

The Query Results area enables you to view the query results and the query execution plan.

The examples in this section display the result of the following query:

```sqlpp
SELECT meta(bw) AS meta, bw AS data
FROM breweries bw
WHERE meta(bw).id = 'kona_brewing';
```

### [](#query-metrics)Query Metrics

When a query finishes, the query metrics for that query are displayed between the Analytics Editor and the Query Results areas.

* **Status icon** — Shows the status of the query. Possible icons include  (success) and  (failure).
* **Last Run** — The time at which the query was last executed.
* **RTT** (Round-trip time) — the total time it took to send the request and receive the response from the server.
* **Elapsed** — Shows the overall query time.
* **Execution** — Shows the query execution time.

### [](#json-format)JSON Format

The **JSON** tab formats the results to make the data easy to read. You can also expand and collapse objects and array values using the small arrow icons next to the line numbers.

```json
[
  {
    "meta": {
      "id": "kona_brewing",
      "vbid": 862,
      "seq": 6,
      "cas": 1777477851619917800,
      "flags": 0
    },
    "data": {
      "name": "Kona Brewing",
      "city": "Kailua-Kona",
      "state": "Hawaii",
      "code": "96740",
      "country": "United States",
      "phone": "1-808-334-1133",
      "website": "http://www.konabrewingco.com",
      "type": "brewery",
      "updated": "2010-07-22 20:00:20",
      "description": "",
```

### [](#table-format)Table Format

The **Table** tab presents the results in a tabular format. The tool converts the JSON documents to HTML tables and presents sub-objects or sub-arrays as sub-tables. This format works well for queries that return an array of objects.

### [](#results-plan-text)Plan Text

The **Plan Text** tab shows the query execution plan in JSON format.

If you have run the query, a detailed query execution plan is shown, which includes information about how long each step in the plan took to execute. If you clicked **Explain** without running the query, the intended query execution plan is shown, without the details that would be included if you actually executed the query.

```json
{
  "logicalPlan": {
    "operator": "distribute-result",
    "expressions": [
      "$$18"
    ],
    "operatorId": "1.1",
    "execution-mode": "UNPARTITIONED",
    "optimizer-estimates": {
      "cardinality": 0,
      "op-cost": 0,
      "total-cost": 0
    },
    "inputs": [
      {
        "operator": "project",
        "variables": [
          "$$18"
        ],
        "operatorId": "1.2",
```

## [](#view-query-history)View Query History

The Analytics Workbench maintains a history of all the queries executed. If you edit a previous query and execute it, the new query is stored at the end of the history. The history is persistent across browser sessions. The query history only saves queries; due to limited browser storage, it does not save query results. When you restart the browser or reload the page, you can see your old queries, but you must re-execute the queries if you want to see their results.

> [!NOTE]
> Clearing the browser history clears the history maintained by the Analytics Editor as well.

To open the **Query History** flyout menu, click **History** above the Analytics Editor.

You can scroll through the entire query history, and click on an individual query to be taken to that particular point in the history.

* **Search history** — You can search the query history by entering text in the **Filter Queries** search box. All matching queries are displayed.
* **Delete a specific entry** — Click the Trash icon next to a particular query to delete it from the history.  
> [!TIP]  
> This can be useful if you want a more manicured history for when you're [exporting it](#export-query) for future use.
* **Delete all entries** — Click **Clear** to delete the entire query history.

### [](#import-query)Import Query

To load queries from a file into the Query History:

1. In the Query History, click **Import** to open the **Import Query History** flyout menu.
2. Click **Import Queries** and then select a local `.json` file that you wish to import. After clicking **Save**, the content of the file is added to the query history.

### [](#export-query)Export Query History

To export the query history in JSON format:

1. In the Query History, click **Export** to open the **Export History** flyout menu.
2. Enter a name for the exported file and click **Export**.

## [](#query-settings)Modify Query Settings

To specify various settings for the Analytics Workbench and the Analytics Service:

1. Click **Settings**. This opens the **Query Settings** flyout menu.
2. Configure the following settings and click **Submit** to save the configuration.

| Option                    | Description                                                                                                                                                                                                                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Timeout**               | The timeout parameter can be used to limit the running time of a query.                                                                                                                                                                                                                                                                           |
| **Scan Consistency**      | The consistency guarantee constraint for index scanning. Select one of the following options: **Not Bounded** **Request Plus** For more information, see [Analytics Query Parameters](../../../server/current/analytics/query-params.md#common-parameters) in the Couchbase Server documentation.                                                 |
| **Transaction Timeout**   | The timeout parameter that limits the running time of a transaction.                                                                                                                                                                                                                                                                              |
| **Named Parameters**      | For the prepared queries, this option allows you to specify any number of named parameters. Click **+** to add new named parameters, and **\-** to remove the parameters. Named parameters must start with the dollar sign ($) for use in prepared queries. Otherwise, they're interpreted as request-level parameters for the Analytics Service. |
| **Positional Parameters** | For the prepared queries, this option allows you to specify values for $1, $2, and so on up to as many positional parameters as you have. Click **+** to add new positional parameters, and **\-** to remove the parameters. The parameters are automatically labeled as **$1**, **$2**, and so on.                                               |

## [](#insights-sidebar)Data Insights / Analytics Scopes

The **Analytics Scopes** area shows scopes, any links with the link type and connection status, and collections that are being shadowed.

The **Analytics Scopes** working area shows all Analytics scopes. By default, only the **Default** Analytics scope exists.

Below each Analytics scope, the Analytics Scopes area shows any links that exist within that scope. By default, each Analytics scope contains only the **Local** link, which enables Analytics to shadow data from the Data service. You can use the [Links](#analytics-links) flyout to create additional external links within any Analytics scope.

Below each link, the Analytics Scopes area shows any Analytics collections that have been created on that link.

This area also provides buttons to:

* Add a link. Create external links to analyze data on Amazon S3, Google Cloud Storage, or Microsoft Azure Blob.
* Add collection. Specify an Analytics collection that you would like to use with the Analytics Workbench.
* Drop a link (). Remove a link from the Analytics Workbench.
* Drop a collection (). Remove an Analytics collection from the Analytics Workbench.

## [](#analytics-links)Analytics Links

The Links flyout in the Analytics Workbench enables you to create, manage, and delete external links. For more information, see [Analytics Links](analytics-links.md).

## [](#analytics-monitor)Analytics Monitor

The Monitor flyout in the Analytics Workbench enables you to monitor Analytics queries and metrics. For more information, see [Analytics Monitor](analytics-monitor.md).