---
title: Querying with SQL++
description: You can query for documents in Couchbase using the SQL++ query
  language, a language based on SQL, but designed for structured and flexible
  JSON documents.
editUrl: https://github.com/couchbase/docs-analytics-sdk-nodejs/edit/release/1.0/modules/howtos/pages/sqlpp-queries-with-sdk.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/nodejs-analytics-sdk/current/howtos/sqlpp-queries-with-sdk.html)

# Querying with SQL++

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. 

On this page we dive straight into using the Query Service API from the Node.js Analytics SDK. For a deeper look at the concepts, to help you better understand the Query Service, and the SQL++ language, see the links in the [Further Information](#further-information) section at the end of this page.

Here we show queries against the Travel Sample collection, at cluster and scope level, and give links to information on adding other collections to your data.

## [](#before-you-start)Before You Start

This page assumes that you have [installed the Node.js Analytics SDK](../hello-world/start-using-sdk.md), and created an [Enterprise Analytics cluster](../../../enterprise-analytics/current/install/introduction-linux-installation.md).

Create a collection to work upon by [importing the travel-sample dataset](../../../enterprise-analytics/current/intro/connecting-to-data-sources.md#import-the-travel-sample-collections) into your cluster.

## [](#querying-your-dataset)Querying Your Dataset

Most queries return more than one result, and you want to iterate over the results:

Scope Level

```javascript
const scope = cluster.database('travel-sample').scope('inventory')

let qs =
    `
    SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
    FROM route
    GROUP BY airline
    ORDER BY route_count DESC
    `

let res = await scope.executeQuery(qs)

for await (let row of res.rows()) {
    console.log(row)
}

console.log('Metadata: ', res.metadata())
```

Cluster Level

```javascript
let qs =
    `
    SELECT r.airline, COUNT(*) AS route_count, AVG(r.distance) AS avg_route_distance
    FROM \`travel-sample\`.\`inventory\`.\`route\` AS r
    GROUP BY r.airline
    ORDER BY route_count DESC
    `

let res = await cluster.executeQuery(qs)
```

### [](#positional-and-named-parameters)Positional and Named Parameters

Supplying parameters as individual arguments to the query allows the query engine to optimize the parsing and planning of the query. You can either supply these parameters by name or by position.

Execute an async query with positional arguments:

Positional Parameters

```javascript
const scope = cluster.database('travel-sample').scope('inventory')

let qs =
    `
    SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
    FROM route
    WHERE sourceairport = $1 AND distance >= $2
    GROUP BY airline
    ORDER BY route_count DESC
    `

let res = await scope.executeQuery(qs, {
    positionalParameters: ['SFO', 1000],
})
```

Execute an async query with named arguments:

Named Parameters

```javascript
const scope = cluster.database('travel-sample').scope('inventory')

let qs =
    `
    SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
    FROM route
    WHERE sourceairport = $sourceAirport AND distance >= $distance
    GROUP BY airline
    ORDER BY route_count DESC
    `

let res = await scope.executeQuery(qs, {
    namedParameters: {sourceAirport: 'SFO', distance: 1000}
})
```

## [](#query-options)Query Options

The Query Service provides an array of options to customize your query. The following table lists them all:

__Table 1\. Available Query Options__
| Name                                            | Description                                                                                                                                                 |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| abortSignal?: AbortSignal                       | Sets an abort signal for the query allowing the operation to be cancelled.                                                                                  |
| clientContextId?: string                        | The returned client context id for this query.                                                                                                              |
| deserializer?: Deserializer                     | Sets the deserializer used by QueryResult.rows to convert query result rows into objects. If not specified, defaults to the cluster’s default deserializer. |
| namedParameters?: {     \[key: string\]: any; } | Named values to be used for the placeholders within the query.                                                                                              |
| positionalParameters?: any\[\]                  | Positional values to be used for the placeholders within the query.                                                                                         |
| raw?: {     \[key: string\]: any; }             | Specifies any additional parameters which should be passed to the query engine when executing the query.                                                    |
| readOnly?: boolean                              | Indicates whether this query should be executed in read-only mode.                                                                                          |
| scanConsistency?: QueryScanConsistency          | Specifies the consistency requirements when executing the query.                                                                                            |
| timeout?: number                                | The timeout for this operation, represented in milliseconds.                                                                                                |

## [](#further-information)Further Information

The [SQL++ for Analytics Reference](../../../server/current/analytics/1%5Fintro.md)offers a complete guide to the SQL++ language for both of our analytics services, including all of the latest additions.