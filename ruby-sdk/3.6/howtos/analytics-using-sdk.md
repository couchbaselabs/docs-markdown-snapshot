---
title: Analytics
description: Parallel data management for complex queries over many records,
  using a familiar SQL-like syntax.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.6/modules/howtos/pages/analytics-using-sdk.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/ruby-sdk/3.6/howtos/analytics-using-sdk.html)

# Analytics

> Parallel data management for complex queries over many records, using a familiar SQL-like syntax. 

This page covers using our operational Ruby SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase’s analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](#home::analytics-sdk.adoc) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](#home::columnar-sdk.adoc) for more information.

For complex and long-running queries, involving large ad hoc join, set, aggregation, and grouping operations, Couchbase Data Platform offers the [Couchbase Analytics Service (CBAS)](#7.1@server:analytics:introduction.adoc). This is the analytic counterpart to our [operational data focussed Query Service](n1ql-queries-with-sdk.md). The analytics service is available in Couchbase Data Platform 6.0 and later (developer preview in 5.5).

## [](#getting-started)Getting Started

After familiarizing yourself with our [introductory primer](#7.1@server:analytics:primer-beer.adoc), in particular creating a dataset and linking it to a bucket to shadow the operational data, try Couchbase Analytics using the Ruby SDK. Intentionally, the API for analytics is very similar to that of the query service. In these examples we will be using an `airports` dataset created on the `travel-sample` bucket.

```ruby
result = cluster.analytics_query('SELECT "hello" AS greeting')
result.rows.each do |row|
  puts row
  #=> {"greeting"=>"hello"}
end
puts "Reported execution time: #{result.meta_data.metrics.execution_time}"
#=> Reported execution time: 14.392402ms
```

## [](#queries)Queries

A query can either be `simple` or be `parameterized`. If parameters are used, they can either be `positional` or `named`:

Positional parameters

```ruby
options = Cluster::AnalyticsOptions.new
options.positional_parameters(["France"])
result = cluster.analytics_query(
  'SELECT COUNT(*) FROM airports WHERE country = ?',
  options)
```

Named parameters

```ruby
options = Cluster::AnalyticsOptions.new
options.named_parameters("country" => "France")
result = cluster.analytics_query(
  'SELECT COUNT(*) FROM airports WHERE country = $country',
  options)
```

> [!NOTE]
> As timeouts are propagated to the server by the client, a timeout set on the client side may be used to stop the processing of a request, in order to save system resources.

## [](#options)Options

Additional parameters may be sent as part of the query.

__Table 1\. AnalyticsOptions__
| Name                        | Description                                                                                              |
| --------------------------- | -------------------------------------------------------------------------------------------------------- |
| String #client\_context\_id | Provides a custom client context ID for this query; default is a random UUID.                            |
| Boolean #priority           | Allows certain requests to have higher priority than others.                                             |
| Boolean #readonly           | Allows explicitly marking a query as being read-only, and not mutating any documents on the server side. |
| Symbol #scan\_consistency   | Specifies level of consistency for the query — :not\_bounded, :request\_plus.                            |
| Integer #scan\_wait         | The maximum duration (in milliseconds) the query engine is willing to wait before failing.               |
| Integer #timeout            | Timeout in milliseconds.                                                                                 |
| JsonTranscoder #transcoder  | Transcoder to use on rows.                                                                               |

Here, we set a `client_context_id`:

```ruby
options = Cluster::AnalyticsOptions.new
options.client_context_id = "user-44-#{rand}"
result = cluster.analytics_query(
  'SELECT * FROM airports WHERE country = "France" LIMIT 10',
  options)
puts result.meta_data.client_context_id
#=> user-44-0.9295598007016517
```

And here we set high priority for the query:

```ruby
options = Cluster::AnalyticsOptions.new
options.priority = true
result = cluster.analytics_query(
  'SELECT * FROM airports WHERE country = "France" LIMIT 10',
  options)
```

Here we pass `readonly` to explicitly mark a query as being read only, and not mutating any documents on the server side.

```ruby
options = Cluster::AnalyticsOptions.new
options.readonly = true
result = cluster.analytics_query(
  'SELECT * FROM airports WHERE country = "France" LIMIT 10',
  options)
```

## [](#handling-the-response)Handling the Response

The analytics query result may contain various sorts of data and metadata, depending upon the nature of the query, as you will have seen when working through our [introductory primer](#7.1@server:analytics:primer-beer.adoc).

Errors caused by resource unavailability (such as timeouts and _Operation cannot be performed during rebalance_ messages) leading to an [automatic retry](error-handling.md#retry) by the SDK.

### [](#metadata)MetaData

The `metadata` object contains useful metadata, such as `Metrics` and `ClientContextID`.

```ruby
result = cluster.analytics_query("SELECT 1=1")
puts "Execution time: #{result.meta_data.metrics.execution_time}"
```

## [](#scan-consistency)Scan Consistency

Like the [Couchbase Query Service](n1ql-queries-with-sdk.md#scan-consistency), and [Search](#full-text-searching-with-sdk.html#consistency), Analytics allows `:request_plus` queries — ensuring results contain information from updated indexes:

```ruby
#options = Cluster::AnalyticsOptions.new
#options.scan_consistency = :request_plus
#result = cluster.analytics_query(
  #'SELECT * FROM airports WHERE country = "France" LIMIT 10',
  #options)
```

## [](#scoped-queries-on-named-collections)Scoped Queries on Named Collections

Given a dataset created against a collection, for example:

```n1ql
CREATE DATASET `airports-collection` ON `travel-sample`.inventory.airport;
```

You can run a query as follows:

```ruby
result = cluster.analytics_query('SELECT airportname, country FROM `travel-sample`.inventory.airport WHERE country="France" LIMIT 3')
```

In addition to running a query via the `Cluster` object, you can run one via the `Scope` object.

```ruby
bucket = cluster.bucket("travel-sample")
scope = bucket.scope("inventory")
result = scope.analytics_query('SELECT airportname, country FROM airport WHERE country="France" LIMIT 3')
```