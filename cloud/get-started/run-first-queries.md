---
title: Explore Sample Data with Data Tools
description: Use Couchbase Capella's Data Tools to explore and work with your data.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/get-started/pages/run-first-queries.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:get-started:run-first-queries.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/get-started/run-first-queries.html)

# Explore Sample Data with Data Tools

> Use Couchbase Capella’s Data Tools to explore and work with your data. 

Your free tier operational cluster includes a `travel-sample` bucket, which you can use to try out Capella operational’s Data Tools. The sample bucket contains documents used for booking travel.

To start exploring your sample data, you can:

* View and edit documents through the [Documents viewer](#documents-viewer)
* Run a SQL++ query through the [Query tab](#first-query)
* Speed up your queries with an [index](#index)
* Load earlier queries into the query editor with the [query history](#query-history)

## [](#documents-viewer)View and Edit Documents with the Documents Viewer

Capella groups documents in buckets. You can add scopes and collections to a bucket to group related documents together. For more information about buckets, scopes, and collections, see [Buckets, Scopes, and Collections](../clusters/data-service/about-buckets-scopes-collections.md).

To view and edit a document in your cluster:

1. Go to **Data Tools** **Documents**.
2. In the **Get documents from** section, select:

  * **travel-sample** in the **Bucket** list
  * **inventory** in the **Scope** list
  * **airport** in the **Collection** list
3. In the **Paginate and Filter documents** section, change the **Limit** field to `8` to specify the maximum number of documents to return.
4. Click **Get Documents** to update the returned document list.
5. In the documents table, click **airport\_1261**.
6. In the **Edit Document** dialog, change the `city` from `"Amiens"` to `"Rouen"` and click **Save Document**.

You have now updated the `city` of the document **airport\_1261** to `"Rouen"`.

## [](#first-query)Run Your First Query with the Query Tab

You can use the **Query** tab to run SQL++ queries.

To run your first query:

1. Go to **Data Tools** **Query**.
2. In the query editor, replace the existing text with the following query:  
```sqlpp  
SELECT route.airlineid, airline.name, route.sourceairport, route.destinationairport  
FROM `travel-sample` route  
INNER JOIN `travel-sample` airline  
ON route.airlineid = META(airline).id  
WHERE route.type = "route"  
AND route.destinationairport = "SFO"  
ORDER BY route.sourceairport;  
```
3. Press Enter or click **Run**. The query results are automatically displayed in JSON format.

> [!TIP]
> Capella can also display the query results as a table, chart, plan, and plan text.
> 
> To display the results in the format of a data-flow diagram with query operators, select the **Plan** tab. The initial scans are on the right of the diagram and the final query output is on the left.
> 
> The query results highlight the operators that might use a lot of resources. For example, Capella spends almost 90% of the time on the **Fetch** operator when running your query.

For more information about the tools on the Query tab, see [Query Tab](../clusters/query-service/query-workbench.md).

## [](#index)Speed Up Your Query with an Index

You can use indexes to improve the performance of your queries.

After you run your query in the query editor, click **Build Suggested** under **Suggested Covered Indexes** on the **Index Advice** right pane. Capella generates an index for you called `adv_destinationairport_sourceairport_airlineid_type`. If you run your query again, the query execution time changes from around 172ms to 24ms.

For more information about indexes in Capella, see [Primary and Secondary Index Reference](../indexes/indexing-overview.md).

## [](#iq-insights)Explore Results with iQ Insights

You can use iQ Insights to generate a variety of relevant insights with the help of AI. These generated insights are in the form of relevant questions, descriptions, and visualizations of your query results, helping you gain a better understanding of your data.

To gain insights on your query results, select the **iQ Insights** tab in the query results pane and click the **Generate Now** button.

To learn more about iQ Insights, see [Explore iQ Insights](capella-iq/explore-iq-insights.md).

## [](#query-history)Access Your Query History

You can use your query history to load earlier queries into your query editor.

To acess your query history:

1. Click **Recent Queries**.
2. Select a query from your query history on the right pane.
3. Click **Run** to run the query again.

## [](#next-steps)Next Steps

After you run your first query, you can:

* [Try out Couchbase SDKs](sdk-playground.md)
* [Import your own data](../clusters/data-service/import-data-documents.md)
* [Configure App Services for your free tier operational cluster](../../app-services/get-started/configuring-app-services.md)

If you want to connect to your cluster:

1. [Generate your cluster credentials](../clusters/manage-database-users.md) to connect and control access to you cluster.
2. [Add your current IP address as an allowed IP for you cluster](../clusters/allow-ip-address.md).
3. [Generate a code snippet](connect.md) to connect your cluster to your application.
4. Choose and install a [Couchbase SDK](#home:ROOT:sdk.adoc).
5. (Optional) Download the security certificate for your cluster and add it to your application’s server machine or IDE:

  1. In the **Operational** tab, select a cluster.
  2. Go to **Settings** **Security Certificate**.
  3. Click **Download**.