---
title: Analytics
description: Parallel data management for complex queries over many records,
  using a familiar SQL++ syntax.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.1/modules/howtos/pages/analytics-using-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:1.1@cxx-sdk:howtos:analytics-using-sdk.adoc[]
---

[View original HTML](/cxx-sdk/1.1/howtos/analytics-using-sdk.html)

# Analytics

> Parallel data management for complex queries over many records, using a familiar SQL++ syntax. 

This page covers using our operational C++ SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase’s analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](#home::analytics-sdk.adoc) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](#home::columnar-sdk.adoc) for more information.

For complex and long-running queries, involving large ad hoc join, set, aggregation, and grouping operations, Couchbase Data Platform offers the [Couchbase Analytics Service (CBAS)](../../../server/7.6/analytics/introduction.md). This is the analytic counterpart to our [operational data focussed Query Service](sqlpp-queries-with-sdk.md).

The analytics service is available in [Capella operational](../../../cloud/clusters/analytics-service/analytics-service.md)or the Enterprise Edition of self-managed Couchbase Server.

## [](#getting-started)Getting Started

After familiarizing yourself with our [introductory primer](../../../server/7.6/analytics/primer-beer.md), in particular creating a dataset and linking it to a bucket to shadow the operational data, try Couchbase Analytics using the C++ SDK. Intentionally, the API for analytics is very similar to that of the query service.

Before starting, here’s all imports used in the following examples:

```c++
#include <couchbase/cluster.hxx>
#include <couchbase/fmt/error.hxx>

#include <tao/json/to_string.hpp>
```

Here’s a complete example of doing an analytics query and handling the results:

```c++
std::string query{ R"(SELECT "hello" AS greeting)" };
auto [err, res] = cluster.analytics_query(query).get();
if (err) {
    fmt::println("Got an error doing analytics query: {}", err);
} else {
    auto rows = res.rows_as<couchbase::codec::tao_json_serializer>();
    for (const auto& row : rows) {
        fmt::println("row: {}", tao::json::to_string(row));
    }
}
```

Let’s break this down. First, we get the results in the form of a `std::pair<couchbase::error, couchbase::analytics_result>`.

An `analytics_result` contains various things of interest, such as metrics, but the main thing we’re interested in are the rows (results). They’re fetched with a `rows_as_json` call.

We check explicitly for an `error` which indicates something went wrong during the analytics query call. Please see [Error Handling](error-handling.md) for details.

Here we’re fetching rows converted into JSON, but as with SQL++ (formerly N1QL) there’s many more options available. Rows can be returned as JSON representations from multiple third party C++ libraries, directly as a user defined class, and more. Please see [JSON Libraries](json.md) for full details.

Finally, we iterate through the `rows`.

## [](#queries)Queries

A query can either be `simple` or be `parameterized`. If parameters are used, they can either be `positional` or `named`. Here is one example of each:

```c++
std::string query{ R"(SELECT airportname, country FROM airports WHERE country = ?)" };
auto options = couchbase::analytics_options().positional_parameters("France");
auto [err, res] = cluster.analytics_query(query, options).get();
```

```c++
std::string query{ R"(SELECT airportname, country FROM airports WHERE country = $country)" };
auto options = couchbase::analytics_options().named_parameters(std::pair{ "country", "France" });
auto [err, res] = cluster.analytics_query(query, options).get();
```

## [](#additional-parameters)Additional Parameters

The handful of additional parameters are illustrated here:

```c++
std::string query{ R"(SELECT airportname, country FROM airports WHERE country = "France")" };
auto options = couchbase::analytics_options()
         // Ask the analytics service to give this request higher priority
         .priority(true)
         // The client context id is returned in the results, so can be used by the
         // application to correlate requests and responses
         .client_context_id("my-id")
         // Override how long the analytics query is allowed to take before timing out
         .timeout(std::chrono::milliseconds(90000));

auto [err, res] = cluster.analytics_query(query, options).get();
```

### [](#metadata)Metadata

`analytics_result::meta_data()` contains useful metadata, such as `elapsedTime`, and `resultCount`:

```c++
std::string query{ R"(SELECT airportname, country FROM airports WHERE country = "France")" };
auto [err, res] = cluster.analytics_query(query).get();

if (err) {
    fmt::println("Got an error doing analytics query: {}", err);
} else {
    auto rows = res.rows_as<couchbase::codec::tao_json_serializer>();
    for (const auto& row : rows) {
        fmt::println("row: {}", tao::json::to_string(row));
    }

    auto elapsed_time = res.meta_data().metrics().elapsed_time();
    auto result_count = res.meta_data().metrics().result_count();
    auto error_count = res.meta_data().metrics().error_count();
}
```