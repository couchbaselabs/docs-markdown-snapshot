---
title: View and Analyze Data in Tableau
description: View and analyze data from Couchbase data sources using Tableau.
editUrl: https://github.com/couchbase/docs-tableau/edit/release/2.0/modules/ROOT/pages/using-couchbase-tableau-connector.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:tableau-connector::using-couchbase-tableau-connector.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/current/using-couchbase-tableau-connector.html)

# View and Analyze Data in Tableau

> View and analyze data from Couchbase data sources using Tableau. 

## [](#prerequisites)Prerequisites

Before you can view and analyze Couchbase data in Tableau, you must:

* Create Tabular Analytics Views from your Couchbase datasets for use with Tableau. For more information, see [Couchbase Analytics Tabular Views](tabular-views.md).
* Configure the connection between Tableau and your Couchbase data source. For more information, see [Configure the Connection](configure-connection.md).

## [](#view-data-from-analytic-views)View Data from Analytic Views

After Tableau connects to your Couchbase data source, the connection appears in the **Connections** section. The scopes defined when you [set up the connection](configure-connection.md#set-up-the-connection) appear under **Scopes**. The **Collections** section lists collections based on your [tabular analytics views](tabular-views.md).

To view the data for a specific view, drag and drop the view onto the data pane. This displays the data in a tabular format.

## [](#use-analytics-views-to-build-tableau-worksheets)Use Analytics Views to Build Tableau Worksheets

After setting up your Couchbase Analytics Tabular views, use them as a data source to build a Tableau worksheet.

1. From the Data Source pane, drag and drop the **airline\_view** onto the data pane.  
This brings up two views. The first view shows details about the view, including the mapping from the view column names to their corresponding document fields.
2. Select **Sheet1**. This sheet opens and displays individual columns from the view, along with a subset of columns called **Measure Values**.
3. Drag the **City** column on to the Rows section to add cities to the sheet.
4. Drag **Airport Name** to the columns section.
5. Select the drop-down on **Airport Name** and select **Measure** **Count**. This creates a simple bar graph that shows the number of airports for each city.

You can also filter your results by using the **Filters** section.

1. Drag and drop the **Country** field into the **Filters** section.
2. Select the country you want to filter by. For example, selecting France filters out cities from other countries.

Depending on the view you're using and the type of report you want to build, you can also select how the data is plotted by choosing one of the options in the **Marks** drop-down.

## [](#use-analytics-queries-to-build-tableau-worksheets)Use Analytics Queries to Build Tableau Worksheets

In addition to using predefined views or custom views, you can use Analytics queries as a data source.

To use Analytics queries, go to the **Data Source** tab and select **New Custom SQL**. Here you can submit queries through the Tableau Connector/JDBC driver that run in a special SQL-compatible mode where certain language constructs operate differently from the regular SQL++ execution.

> [!NOTE]
> The default scope is set based on the scope specified in the connection dialog. If no scope is explicitly mentioned, it's set to `Default`. However, users can provide any other scope when setting up the connection. To run Analytics queries, you may specify the Analytics scope along with the collection in your queries. If no scope is specified in a query, the scope set in the connection dialog will be used. For example, to use the airline Analytics collection, use `` `travel-sample`.inventory.airline ``.

### [](#run-analytics-queries-on-tableau)Run Analytics Queries on Tableau

A simple Analytics query you can execute is to get the counts of the hotels per city. In the Edit Custom SQL window, add the following query and select Preview Results.

```sqlpp
select
 country,
 city,
 count(id) as count
from `travel-sample`.inventory.hotel
group by country, city
order by count(id) desc
```

![Query 1](_images/analytics-query-1.png) 

You can also use queries that join multiple Analytics collections. For example, to get the airlines with the most routes you can run the following query.

```sqlpp
select a.id,
 a.callsign,
 a.name,
 a.country,
 count(r.id) as route_count
from `travel-sample`.inventory.airline a
join `travel-sample`.inventory.route r on META(a).id = r.airlineid
group by a.id, a.callsign, a.name, a.country
order by route_count desc
```

![Query 2](_images/analytics-query-2.png) 

The previous query can be expanded upon further by getting the percentile rank of airlines with the most routes with the following query.

```sqlpp
select
 a.id,
 a.callsign,
 a.name,
 a.country,
 count(r.id) as route_count,
 PERCENT_RANK() OVER (
  ORDER BY count(r.id)
  ) AS `rank`
from `travel-sample`.inventory.airline a
join `travel-sample`.inventory.route r on META(a).id = r.airlineid
group by a.id, a.callsign, a.name, a.country
order by route_count desc
limit 100
```

![Query 2](_images/analytics-query-3.png) 

### [](#use-analytics-queries-as-the-data-source-to-build-tableau-reports)Use Analytics Queries as the Data Source to Build Tableau Reports

After you execute your query, you can see the data from the query in a tabular form.

1. Go to the **Sheet** tab.
2. Add the **name** field to **Rows** and the **rank** field to **Columns**.
3. Click the **rank** label on the graph and choose descending to order the chart from highest to lowest.

## [](#publish-workbook-to-tableau-server)Publish Workbook to Tableau Server

Follow these steps to publish a workbook from Tableau Desktop to Tableau Server:

1. From the menu, choose **Server** **Publish Workbook**.
2. Select the project and enter a name for the workbook.
3. Configure any publish options, then click **Publish**.
4. After publishing, your web browser opens and prompts you to sign in to Tableau Server.
5. Sign in with your Tableau Server account.

After signing in, open the workbook on Tableau Server to:

* View the report in detail.
* Refresh the workbook data to load any updates from the source.

## [](#publish-data-sources-to-tableau-server)Publish Data Sources to Tableau Server

Publish a data source from Tableau Desktop so other users can build workbooks from it on Tableau Server.

To publish a data source:

1. In Tableau Desktop, choose **Server** **Publish Data Source**.
2. Select the project, enter a name for the data source, and configure any publish options.
3. Click **Publish**.

After publishing, your browser opens and prompts you to sign in to Tableau Server. Sign in with your Tableau Server account. After you sign in, the published data source appears in the selected project on Tableau Server. Users with access to that project can then open the data source to create workbooks and reports as needed.