---
title: Analytics
description: Parallel data management for complex queries over many records,
  using a familiar SQL++ syntax.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.4/modules/howtos/pages/analytics-using-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:4.4@nodejs-sdk:howtos:analytics-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.4/howtos/analytics-using-sdk.html)

# Analytics

> Parallel data management for complex queries over many records, using a familiar SQL++ syntax. 

This page covers using our operational Node.js SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.

For complex and long-running queries, involving large ad hoc join, set, aggregation, and grouping operations, Couchbase Data Platform offers the [Couchbase Analytics Service (CBAS)](../../../server/7.6/analytics/introduction.md). This is the analytic counterpart to our [operational data focussed Query Service](n1ql-queries-with-sdk.md).

The analytics service is available in [Capella operational](../../../cloud/clusters/analytics-service/analytics-service.md)or the Enterprise Edition of self-managed Couchbase Server.

## [](#getting-started)Getting Started

After familiarizing yourself with our [introductory primer](../../../server/7.6/analytics/primer-beer.md), in particular creating a dataset and linking it to a bucket to shadow the operational data, try Couchbase Analytics using the Node.js SDK. Intentionally, the API for analytics is very similar to that of the query service.

```javascript
var result = await cluster.analyticsQuery('SELECT "hello" AS greeting')
result.rows.forEach((row) => {
  console.log(row)
})
```

## [](#queries)Queries

A query can either be `simple` or be `parameterized`. If parameters are used, they can either be `positional` or `named`. Here is one example of each:

```javascript
var result = await cluster.analyticsQuery(
  'SELECT airportname, country FROM airports WHERE country="France" LIMIT 3'
)
```

The query may be performed with positional parameters:

```javascript
var result = await cluster.analyticsQuery(
  'SELECT airportname, country FROM airports WHERE country = ? LIMIT 3',
  { parameters: ['France'] }
)
```

Alternatively, the query may be performed with named parameters:

```javascript
var result = await cluster.analyticsQuery(
  'SELECT airportname, country FROM airports WHERE country = $country LIMIT 3',
  { parameters: { country: 'France' } }
)
```

> [!NOTE]
> As timeouts are propagated to the server by the client, a timeout set on the client side may be used to stop the processing of a request, in order to save system resources. See example in the next section.

## [](#fluent-api)Fluent API

Additional parameters may be sent as part of the query, using the options block in the API. There are currently three parameters:

* **Client Context ID**, sets a context ID that is returned back as part of the result. Uses the `clientContextId` option; default is a random UUID
* **Server Side Timeout**, customizes the timeout sent to the server. Does not usually have to be set, as the client sets it based on the timeout on the operation. Uses the `timeout` option, and defaults to the Analytics timeout set on the client (75s). This can be adjusted at the [cluster global config level](../ref/client-settings.md#timeout-options).
* **Priority**, set if the request should have priority over others. The `priority` option, defaults to `false`.

Here, we give the request priority over others, and set a custom, server-side timeout value:

```javascript
var result = await cluster.analyticsQuery(
  'SELECT airportname, country FROM airports WHERE country="France" LIMIT 3',
  {
    priority: true,
    timeout: 100, // seconds
  }
)
```

## [](#handling-the-response)Handling the Response

Assuming that no errors are thrown during the exceution of your query, the return value will be a `AnalyticsQueryResult` object. You can access the individual rows which were returned through the rows property. These rows may contain various sorts of data and metadata, depending upon the nature of the query, as you will have seen when working through our [introductory primer](../../../server/7.6/analytics/primer-beer.md).

```javascript
  var result = await cluster.analyticsQuery('SELECT "hello" AS greeting')

  result.rows.forEach((row) => {
    console.log('Greeting: %s', row.greeting)
  })
```

### [](#metadata)MetaData

The `meta` property of `AnalyticsQueryResult` contains useful metadata, such as metrics, which contains properties such as `elapsedTime`, and `resultCount`. Here is a snippet printing out some metrics from a query:

```javascript
  var result = await cluster.analyticsQuery('SELECT "hello" AS greeting')

  console.log('Elapsed time: %d', result.meta.metrics.elapsedTime)
  console.log('Execution time: %d', result.meta.metrics.executionTime)
  console.log('Result count: %d', result.meta.metrics.resultCount)
  console.log('Error count: %d', result.meta.metrics.errorCount)
```

For a listing of available `metrics` in the meta-data, see the [Understanding Analytics](../concept-docs/analytics-for-sdk-users.md) SDK doc.

## [](#scoped-queries-on-named-collections)Scoped Queries on Named Collections

Given a dataset created against a collection, for example:

```n1ql
ALTER COLLECTION `travel-sample`.inventory.airport ENABLE ANALYTICS;

-- NB: this is more or less equivalent to:
CREATE DATAVERSE `travel-sample`.inventory;
CREATE DATASET `travel-sample`.inventory.airport ON `travel-sample`.inventory.airport;
```

You can run a query as follows:

```javascript
  var result = await cluster.analyticsQuery(
    'SELECT airportname, country FROM `travel-sample`.inventory.airport WHERE country="France" LIMIT 3'
  )
```

## [](#advanced-analytics-topics)Advanced Analytics Topics

From Couchbase Data Platform 6.5, _KV Ingestion_ is added to CBAS.