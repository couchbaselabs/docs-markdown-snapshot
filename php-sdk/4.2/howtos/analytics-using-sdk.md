---
title: Analytics
description: Parallel data management for complex queries over many records,
  using a familiar SQL++ syntax.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/howtos/pages/analytics-using-sdk.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:4.2@php-sdk:howtos:analytics-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/4.2/howtos/analytics-using-sdk.html)

# Analytics

> Parallel data management for complex queries over many records, using a familiar SQL++ syntax. 

> [!TIP]
> Capella Columnar SDKs
> 
> SDKs for [Capella Columnar](../../../analytics/intro/intro.md) — Couchbase’s analytical database (RT-OLAP) for real time apps and operational intelligence — are in development, and will be arriving first for the Java, Node.js, and Python platforms.

For complex and long-running queries, involving large ad hoc join, set, aggregation, and grouping operations, Couchbase Data Platform offers the [Couchbase Analytics Service (CBAS)](#7.1@server:analytics:introduction.adoc). This is the analytic counterpart to our [operational data focussed Query Service](n1ql-queries-with-sdk.md). The analytics service is available in Couchbase Data Platform 6.0 and later (developer preview in 5.5).

## [](#getting-started)Getting Started

After familiarizing yourself with our [introductory primer](#7.1@server:analytics:primer-beer.adoc), in particular creating a dataset and linking it to a bucket to shadow the operational data, try Couchbase Analytics using the PHP SDK. Intentionally, the API for analytics is very similar to that of the query service. In these examples we will be using an `airports` dataset created on the `travel-sample` bucket.

In PHP SDK 2.x, Analytics was only available on the `Bucket` object; in PHP SDK 3.x, Analytics queries are submitted using the Cluster reference, not a Bucket or Collection:

```php
$options = new \Couchbase\AnalyticsOptions();
$result = $cluster->analyticsQuery('SELECT "hello" as greeting;', $options);

foreach ($result->rows() as $row) {
    printf("result: %s\n", $row["greeting"]);
}
```

## [](#queries)Queries

A query can either be `simple` or be `parameterized`. If parameters are used, they can either be `positional` or `named`. Here is one example of each:

```php
$options = new \Couchbase\AnalyticsOptions();
$result = $cluster->analyticsQuery('SELECT airportname, country FROM airports WHERE country = "France";', $options);
```

The query may be performed with positional parameters:

```php
$options = new \Couchbase\AnalyticsOptions();
$options->positionalParameters(["France"]);
$result = $cluster->analyticsQuery('SELECT airportname, country FROM airports WHERE country = $1;', $options);
```

Alternatively, the query may be performed with named parameters:

```php
$options = new \Couchbase\AnalyticsOptions();
$options->namedParameters(['$country' => "France"]);
$result = $cluster->analyticsQuery('SELECT airportname, country FROM airports WHERE country = $country;', $options);
```

> [!NOTE]
> As timeouts are propagated to the server by the client, a timeout set on the client side may be used to stop the processing of a request, in order to save system resources. See example in the next section.

## [](#options)Options

Additional parameters may be sent as part of the query.

* **Server Side Timeout**, customizes the timeout sent to the server. Does not usually have to be set, as the client sets it based on the timeout on the operation. Uses `timeout(long)`, and defaults to the Analytics timeout set on the client (75s). This can be adjusted at the [cluster global config level](../ref/client-settings.md#timeout-options).

Here, we set a custom, server-side timeout value:

```php
$options = new \Couchbase\AnalyticsOptions();
$options->timeout(100);
$result = $cluster->analyticsQuery('SELECT airportname, country FROM airports WHERE country = "France";', $options);
```

## [](#handling-the-response)Handling the Response

The analytics query result may contain various sorts of data and metadata, depending upon the nature of the query, as you will have seen when working through our [introductory primer](#7.1@server:analytics:primer-beer.adoc).

```php
$options = new \Couchbase\AnalyticsOptions();
$result = $cluster->analyticsQuery('SELECT airportname, country FROM airports WHERE country = "France";', $options);

foreach ($result->rows() as $row) {
    printf("Name: %s, Country: %s\n", $row["airportname"], $row["country"]);
}
```

Common errors are listed in our [Errors Reference doc](../ref/error-codes.md#analytics-errors), with errors caused by resource unavailability (such as timeouts and _Operation cannot be performed during rebalance_ messages) leading to an [automatic retry](error-handling.md#retry) by the SDK.

### [](#metadata)MetaData

The `metadata` object contains useful metadata, such as `Metrics` and `ClientContextID`. Here is a snippet using several items of metadata

```php
$options = new \Couchbase\AnalyticsOptions();
$result = $cluster->analyticsQuery('SELECT airportname, country FROM airports WHERE country = "France";', $options);

$metadata = $result->metadata();
$metrics = $metadata->metrics();
printf("Elapsed time: %d\n", $metrics["elapsedTime"]);
printf("Execution time: %d\n", $metrics["executionTime"]);
printf("Result count: %d\n", $metrics["resultCount"]);

$options = new \Couchbase\AnalyticsOptions();
$result = $cluster->analyticsQuery(
    'SELECT airportname, country FROM `travel-sample`.inventory.airport WHERE country = "France" LIMIT 3;',
    $options
);

foreach ($result->rows() as $row) {
    printf("Name: %s, Country: %s\n", $row["airportname"], $row["country"]);
}

$scope = $bucket->scope("inventory");
$options = new \Couchbase\AnalyticsOptions();
$result = $cluster->analyticsQuery('SELECT airportname, country FROM `airports` WHERE country = "France" LIMIT 2;', $options);

foreach ($result->rows() as $row) {
    printf("Name: %s, Country: %s\n", $row["airportname"], $row["country"]);
}
```

For a listing of available `Metrics` in `MetaData`, see the [Understanding Analytics](../concept-docs/analytics-for-sdk-users.md) SDK doc.

## [](#scoped-queries-on-named-collections)Scoped Queries on Named Collections

In addition to creating a dataset with a WHERE clause to filter the results to documents with certain characteristics, you can also create a dataset against a named collection, for example:

```n1ql
ALTER COLLECTION `travel-sample`.inventory.airport ENABLE ANALYTICS;

-- NB: this is more or less equivalent to:
CREATE DATAVERSE `travel-sample`.inventory;
CREATE DATASET `travel-sample`.inventory.airport ON `travel-sample`.inventory.airport;
```

We can then query the Dataset as normal, using the fully qualified keyspace:

```php
$options = new \Couchbase\AnalyticsOptions();
$result = $cluster->analyticsQuery(
    'SELECT airportname, country FROM `travel-sample`.inventory.airport WHERE country = "France" LIMIT 3;',
    $options
);

foreach ($result->rows() as $row) {
    printf("Name: %s, Country: %s\n", $row["airportname"], $row["country"]);
}
```

Note that using the `CREATE DATASET` syntax we could choose any Dataset name in any Dataverse, including the default. However the SDK supports this standard convention, allowing us to query from the Scope object:

```php
$scope = $bucket->scope("inventory");
$options = new \Couchbase\AnalyticsOptions();
$result = $cluster->analyticsQuery('SELECT airportname, country FROM `airports` WHERE country = "France" LIMIT 2;', $options);

foreach ($result->rows() as $row) {
    printf("Name: %s, Country: %s\n", $row["airportname"], $row["country"]);
}
```