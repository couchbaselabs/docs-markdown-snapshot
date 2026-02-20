---
title: Using the Couchbase Tableau Connector
editUrl: https://github.com/couchbase/docs-tableau/edit/release/1.1/modules/ROOT/pages/using-couchbase-tableau-connector.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:tableau-connector::using-couchbase-tableau-connector.adoc[]
---

[View original HTML](/tableau-connector/current/using-couchbase-tableau-connector.html)

# Using the Couchbase Tableau Connector

> The Couchbase Analytics Connector for Tableau is compatible with Couchbase Server running version 7.1 or higher. 

## [](#configure-connection)Configure Connection

Configure the Tableau connector based on the type of Couchbase Server instances you are using.

### [](#configure-couchbase-analytics-connector-for-couchbase-server-instances)Configure Couchbase Analytics Connector for Couchbase Server Instances

To connect to your Couchbase instance:

1. Set the **Server** field to the address of the Couchbase instance — for example, `localhost`.
2. Enter your **Username** and **Password**, and click **Sign In**.
3. (Optional) To securely connect to Couchbase with certificates enabled, select the **Require SSL** option.

![Tableau Connection Without SSL](_images/tableau-connection-without-ssl.png) 

### [](#ssl)Set Up SSL Support for Tableau Connector

To set up SSL support for Tableau Connector, see the following sections:

* [Set Up SSL Support for Tableau Desktop](setup-tableau-desktop.md#ssl)
* [Set Up SSL Support for Tableau Server](setup-tableau-server.md#ssl)

### [](#configure-advanced-settings)Configure Advanced Settings

To set up the connection timeout and the scan consistency mode, go to the **Advanced** tab.

![Tableau Connection Advanced Scan Consistency](_images/tableau-connector-config-advanced-110.png) 

Setting the scan consistency to `Request plus` displays a dropdown to select the scan wait time.

### [](#configure-tableau-server-connection-on-tableau-desktop)Configure Tableau Server Connection on Tableau Desktop

Reports and dashboards created on Tableau Desktop can be published and viewed on Tableau Server. To configure your Tableau Server connection, go to **Server** **Tableau Online**.

![Connect to Tableau Server](_images/connect-to-tableau-server.png) 

You will then be prompted to sign in to your Tableau Server account. Once signed in, you should see the connection in the Server section.

![Verify Tableau Server Connection](_images/verify-connection-to-tableau-server.png) 

> [!NOTE]
> If you’re using an on-premise instance of Tableau Server, you will need to configure SSL. This can be done by logging into the Tableau Services Manager UI and going to **Configuration** **Security** **External SSL**.

![Tableau Server SSL Configuration](_images/tableau-server-ssl-config.png) 

For more information on configuring SSL on your Tableau Server, follow the guide on the [Configuring SSL on Tableau Server](https://help.tableau.com/current/server/en-us/ssl%5Fconfig.htm#use-the-tsm-web-interface) page.

## [](#view-data-from-analytic-views-on-tableau)View Data from Analytic Views on Tableau

Once Tableau has successfully established a connection with your Couchbase Server, you should see it in the Connections section. You should also see the Analytics scopes set up in the previous steps.

![Analytics Scopes in Tableau](_images/analytic-scopes-in-tableau.png) 

The collections are listed based on the tabular views created. Dragging and dropping a view onto the data pane will then display the data for the view in a table.

![Analytics Views in Tableau](_images/view-data-from-analytic-views.png) 

## [](#use-couchbase-analytics-views-to-build-tableau-worksheets)Use Couchbase Analytics Views to Build Tableau Worksheets

Now that you have your Couchbase Analytics Tabular views set up on Tableau, you can now use these views as the data source to build your Tableau worksheets.

From the Data Source pane, drag and drop the **airline\_view** onto the data pane. This will bring up two views. The first view shows you details about the view including the mapping from the view column names to their corresponding document fields.

![Analytics View](_images/view-data-from-analytic-views.png) 

Next select **Sheet1**, which should now show the individual columns from the view along with a subset of the columns called **Measure Values**.

![Analytic Views Columns](_images/analytics-view-columns.png) 

Drag the **City** column on to the Rows section to add cities to the sheet. Next, add **Airport Name** to the columns section. Select the drop-down and choose **Measure** **Count**.

![Airports Per City](_images/airport-view.png) 

This will create a simple bar graph that shows the number of airports for each city.

![Airports Per City Graph](_images/airports-per-city.png) 

You can also filter your results by using the Filters section. Drag and drop the **Country** field into the Filters section and select the country to filter by.

![Filter Graph by Country](_images/filter-by-country.png) 

Selecting France then filters out cities from the other countries.

![Filter Result](_images/filter-result.png) 

Depending on the view you are using and the type of report you want to build, you can also select how the data is plotted by choosing one of the options in the Marks drop-down.

![Change Graph Style](_images/change-graph-style.png) 

## [](#use-couchbase-analytics-queries-to-build-tableau-worksheets)Use Couchbase Analytics Queries to Build Tableau Worksheets

Apart from the predefined views or any other custom views you create, the Couchbase Tableau connector also supports the use of Analytics queries as the data source.

To use Analytics queries, go to the Data Source tab and select New Custom SQL. Here you can submit queries through the Tableau Connector/JDBC driver that run in a special SQL-compatible mode where certain language constructs operate differently from the regular SQL++ execution.

![New Custom Query](_images/new-custom-query.png) 

> [!NOTE]
> The default scope is set based on the scope if specified in the connection dialog. If no scope is explicitly mentioned, it is set to `Default`, however users can provide any other scope when setting up the connection. To run Analytics queries, you may specify the Analytics scope along with the collection in your queries. If no scope is specified in a query, the scope set in the connection dialog will be used. For example, to use the airline Analytics collection, use `` `travel-sample`.inventory.airline ``.

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

Once you have executed your query, you should be able to see the data from the query in a tabular form.

![Analytics Query In Table](_images/analytics-query-tabular-view.png) 

Go to the Sheet tab and add the **name** field to the Rows section and the **rank** field generated by the query to the Columns section. You can then click on the **rank** label on the graph to sort the chart in from highest to lowest rank.

![Graph Using Analytics Query As Data Source](_images/analytics-query-data-source.png) 

## [](#publish-workbook-to-tableau-server)Publish Workbook to Tableau Server

Once you have created your reports, you can then publish them onto Tableau Server. From the menu, select **Server** **Publish Workbook**.

![Publish Report to Tableau Server](_images/publish-report.png) 

Select the project to publish the workbook to and give it a name. Once you have selected the options you need, click on the **Publish** button.

![Publish Workbook Dialog](_images/publish-workbook-dialog.png) 

Once published your browser will launch, and you will be prompted to log in to Tableau Server. Log in using you Tableau Server user account credentials.

![Tableau Server Login](_images/tableau-server-login.png) 

Once you are successfully logged in, you should see the workbook you created using Tableau Desktop.

![Published Workbooks](_images/published-workbook.png) 

You can click on the workbook to view it in greater detail. From this page you can also refresh the data so that your report reflects any updates made to the source.

![Published Workbook View](_images/published-workbook-view.png) 

## [](#publish-data-sources-to-tableau-server)Publish Data Sources to Tableau Server

You can also publish you data source directly to Tableau Server from Tableau Desktop. This will allow users with access to your Tableau Server project to view and build their own workbooks and reports using the Couchbase Analytics data source you have set up on Tableau Desktop. From the menu, select **Server** **Publish Data Source**.

![Publish Data Source](_images/publish-data-source.png) 

Select the project to publish to and give the data source a name and hit **Publish**.

![Publish Data Source Dialog](_images/publish-data-source-dialog.png) 

Once successfully configured, you will receive a notification on Tableau Server. Here you will be prompted to log in to Tableau Server again.

![Published Data Source](_images/published-data-source.png) 

Once logged in you should be able to see your data source. Using the data source you can then create your own workbooks and reports that use the data source set up by Tableau Server.

![Using Published Data Source](_images/using-published-data-source.png)