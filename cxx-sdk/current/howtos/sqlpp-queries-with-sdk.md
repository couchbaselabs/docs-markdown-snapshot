[View original HTML](/cxx-sdk/current/howtos/sqlpp-queries-with-sdk.html)

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. 

On this page we dive straight into using the Query Service API from the C++ SDK. For a deeper look at the concepts, to help you better understand the Query Service, the SQL++ language, and the Index Service, see the links in the [Further Information](#further-information) section at the end of this page.

> You can query for documents in Couchbase using the SQL++ query language (formerly N1QL), a language based on SQL, but designed for structured and flexible JSON documents. 

Our query service uses SQL++, which will be fairly familiar to anyone who’s used any dialect of SQL. [Additional Resources](#additional-resources) for learning about SQL++ are listed at the bottom of the page. Before you get started you may wish to checkout the [SQL++ intro page](#6.5@server:n1ql:n1ql-language-reference/index.adoc).

|  | SQL++ Compared to Key-Value SQL++ is excellent for performing queries against multiple documents, but if you only need to access or mutate a single document and you know its unique ID, it will be much more efficient to use the Key-Value API. We strongly recommend using both APIs to create a flexible, performant application. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#getting-started)Getting Started

Let’s get started by pulling in all the imports needed in the examples below:

```c++
#include <couchbase/cluster.hxx>
#include <couchbase/codec/tao_json_serializer.hxx>

#include <fmt/format.h>
#include <tao/json/value.hpp>
#include <tao/json/to_string.hpp>

#include <couchbase/fmt/cas.hxx>
#include <couchbase/fmt/error.hxx>

#include <iostream>
```

Then we connect to a Couchbase cluster, as usual (of course, change the address and credentials to match your own cluster’s):

```c++
auto options = couchbase::cluster_options(username, password);
options.apply_profile("wan_development");
auto [connect_err, cluster] = couchbase::cluster::connect(connection_string, options).get();
if (connect_err) {
    fmt::println("Unable to connect to the cluster: {}", connect_err);
    return 1;
}
auto bucket = cluster.bucket(bucket_name);
auto scope = bucket.scope(scope_name);
auto collection = bucket.scope(scope_name).collection(collection_name);
```

The examples below will use the travel-sample example bucket. This can be installed through the Couchbase Admin UI in Settings → Sample Buckets.

In order to be able to use query on a bucket, it must have at least a primary index created. The easiest way to create this is through the Couchbase Admin UI. Simply visit the Query tab then write this in the Query Editor and hit Execute:

```n1ql
CREATE PRIMARY INDEX ON `travel-sample`
```

Note that building indexes is covered in more detail on the [Query concept page](../concept-docs/n1ql-query.md#index-building) — and in the [API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/manager/query/index.html).

## [](#a-simple-query)A Simple Query

Here’s the basics of how to run a simple query to fetch 10 random rows from travel-sample and print the results:

```c++
std::string statement = "SELECT * from `travel-sample` LIMIT 10;";
const auto [err, result] = cluster.query(statement, {}).get();
```

(Note that we won’t be covering the SQL++ language itself in any detail here, but if you’re familiar with SQL you’ll see it’s very similar.)

The C++ SDK returns a `couchbase::error` instance that wraps an `std::error_code` rather than throwing exceptions. You can check whether an error occurred like this:

```c++
if (err) {
    fmt::println("Error: {}", err);
} else {
    fmt::println("Got {} rows", result.rows_as<couchbase::codec::tao_json_serializer, tao::json::value>().size());
}
```

The returned `query_result` contains an `rows_as<S,T>` method, allowing the results to be converted into something useful. The above example demonstrates returning the results as a `tao::json::value` using the serializer `couchbase::codec::tao_json_serializer`, that uses the _taoJSON_ library.

In addition to `rows_as<S,T>` we provide accessors for common use cases like `rows_as_json` and `rows_as_binary`.

Please see [this guide](json.md) for more information on the supported ways of working with JSON.

The rows can be iterated as follows:

```c++
const auto [err, result] =
  cluster.query("SELECT * FROM `travel-sample` LIMIT 10;", {}).get();
if (err) {
    fmt::println("Error: {}", err);
} else {
    for (const auto& row : result.rows_as<couchbase::codec::tao_json_serializer>()) {
        fmt::println("{}", tao::json::to_string(row));
    }
}
```

|  | All of the examples here use the simplest of the two asynchronous APIs provided by the C++ SDK, which returns an std::future. There’s also a callback-based asynchronous API. See [Choosing an API](#concurrent-async-apis) for more details. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#placeholder-and-named-arguments)Placeholder and Named Arguments

Placeholders allow you to specify variable constraints for a query.

There are two variants of placeholders: positional and named parameters. Both are used as placeholders for values in the WHERE, LIMIT or OFFSET clause of a query.

Positional parameters use an ordinal placeholder for substitution and can be used like this:

```c++
std::string stmt = R""""(
                    SELECT COUNT(*)
                    FROM `travel-sample`.inventory.airport
                    WHERE country=$1;
                    )"""";
const auto [err, result] =
  cluster
    .query(
      stmt, couchbase::query_options().adhoc(false).positional_parameters("United States")
    )
    .get();
```

Whereas named parameters can be used like this:

```c++
std::string stmt = R""""(
                    SELECT COUNT(*)
                    FROM `travel-sample`.inventory.airport
                    WHERE country=$country;
                    )"""";
const auto [err, result] =
  cluster
    .query(
      stmt,
      couchbase::query_options().named_parameters(
        std::make_pair<std::string, std::string>("country", "United States")
      )
    )
    .get();
```

## [](#scan-consistency)Scan Consistency

Queries take an optional `scan_consistency` parameter that enables a tradeoff between latency and (eventual) consistency.

* A SQL++ query using the default `not_bounded` scan consistency will not wait for any indexes to finish updating before running the query and returning results, meaning that results are returned quickly, but the query will not return any documents that are yet to be indexed.
* With scan consistency set to `request_plus`, all outstanding document changes and index updates are processed before the query is run. Select this when consistency is always more important than performance.
* For a middle ground, `at_plus` is a "read your own write" (RYOW) option, which means it just waits for the documents that you specify to be indexed.

Here’s how to specify the `request_plus` scan consistency level:

```c++
const auto [err, result] = cluster
                             .query(
                               "SELECT * FROM `travel-sample` LIMIT 10;",
                               couchbase::query_options().scan_consistency(
                                 couchbase::query_scan_consistency::request_plus
                               )
                             )
                             .get();
```

And the `at_plus` level is represented with `query_options.consistent_with()`:

```c++
auto [upsert_err, upsert_result] = collection.upsert("id", content).get();
assert(!upsert_err); // Just for demo, a production app should check the result properly

couchbase::mutation_state state;
state.add(upsert_result);
const auto [err, result] = cluster
                             .query(
                               "SELECT * FROM `travel-sample` LIMIT 10;",
                               couchbase::query_options().consistent_with(state)
                             )
                             .get();
if (err) {
    fmt::println("Error: {}", err);
}
```

## [](#querying-at-scope-level)Querying at Scope Level

It is possible to query off the [scope level](../../../server/current/learn/data/scopes-and-collections.md) with _Couchbase Server version 7.0_ onwards, using the `scope.query()` method. It takes the statement as a required argument, and then allows additional options if needed.

The code snippet below shows how to run a simple query to fetch 10 rows from travel-sample and print the results, the assumption is that the `airline` collection exists within the scope.

```c++
const auto [err, result] = scope.query("SELECT * FROM airline LIMIT 10;", {}).get();
if (err) {
    fmt::println("Error: {}", err);
} else {
    for (const auto& row : result.rows_as<couchbase::codec::tao_json_serializer>()) {
        fmt::println("{}", tao::json::to_string(row));
    }
}
```

A complete list of `query_options` can be found in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/structcouchbase%5F1%5F1query%5F%5Foptions.html).

## [](#additional-resources)Additional Resources

|  | SQL++ is not the only query option in Couchbase. Be sure to check that [your use case fits your selection of query service](../concept-docs/querying-your-data.md). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The [SQL++ interactive tutorial](http://query.pub.couchbase.com/tutorial/#1) is a good introduction to the basics of SQL++ use.

## [](#further-information)Further Information