---
title: Querying with SQL++
description: You can query for documents in Couchbase using the SQL++ query
  language, a language based on SQL, but designed for structured and flexible
  JSON documents.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/sqlpp-queries-with-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:rust-sdk:howtos:sqlpp-queries-with-sdk.adoc[]
---

[View original HTML](/rust-sdk/current/howtos/sqlpp-queries-with-sdk.html)

# Querying with SQL++

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. 

On this page we dive straight into using the Query Service API from the Rust SDK. For a deeper look at the concepts, to help you better understand the Query Service, the SQL++ language, and the Index Service, see the links in the [Further Information](#further-information) section at the end of this page.

> You can query for documents in Couchbase using the SQL++ query language (formerly N1QL), a language based on SQL, but designed for structured and flexible JSON documents. 

Our query service uses SQL++, which will be fairly familiar to anyone who’s used any dialect of SQL. [Additional Resources](#additional-resources) for learning about SQL++ are listed at the bottom of the page. Before you get started you may wish to checkout the [SQL++ intro page](../../../server/current/n1ql/n1ql-language-reference/index.md).

> [!TIP]
> SQL++ Compared to Key-Value
> 
> SQL++ is excellent for performing queries against multiple documents, but if you only need to access or mutate a single document and you know its unique ID, it will be much more efficient to use the Key-Value API. We strongly recommend using both APIs to create a flexible, performant application.

## [](#getting-started)Getting Started

Let’s get started by connecting to a Couchbase cluster, as usual (of course, change the address and credentials to match your own cluster’s):

```rust
let cluster = Cluster::connect(
    "couchbase://localhost",
    ClusterOptions::new(Authenticator::PasswordAuthenticator(
        PasswordAuthenticator::new("username".to_string(), "password".to_string()),
    )),
)
.await?;
```

The examples below will use the travel-sample example bucket. We will also be using the `airline` collection within the `inventory` scope in that bucket. This can be installed through the Couchbase Admin UI in Settings → Sample Buckets.

In order to be able to use query on a scope, it is best to at least have a primary index created. The easiest way to create this is through the Couchbase Admin UI. Simply visit the Query tab then write this in the Query Editor and hit Execute:

```n1ql
CREATE PRIMARY INDEX ON `travel-sample`.`inventory`.`airline`
```

Note that building indexes is covered in more detail on the [Query concept page](../concept-docs/n1ql-query.md#index-building) — and in the [API Reference](https://docs.rs/couchbase/latest/couchbase/management/query/query%5Findex%5Fmanager/struct.QueryIndexManager.html#implementations).

## [](#a-simple-query)A Simple Query

Here’s the basics of how to run a simple query to fetch 10 random rows from travel-sample and print the results:

```rust
let scope = cluster.bucket("travel-sample").scope("inventory");
let statement = "SELECT * from `airline` LIMIT 10;";
let mut result = scope.query(statement, None).await?;

let mut rows = result.rows();
while let Some(row) = rows.next().await {
    let row: serde_json::Value = row?;
    println!("Row: {}", row);
}
```

(Note that we won’t be covering the SQL++ language itself in any detail here, but if you’re familiar with SQL you’ll see it’s very similar.)

The returned `QueryResult` contains a `rows[T]` method, allowing the results to be converted into something useful. The above example demonstrates returning the results as `serde_json::Value`, a flexible way to handle JSON.

`rows` can be deserialized into any type that implements `serde::DeserializeOwned`.

## [](#placeholder-and-named-arguments)Placeholder and Named Arguments

Placeholders allow you to specify variable constraints for a query.

There are two variants of placeholders: positional and named parameters. Both are used as placeholders for values in the `WHERE`, `LIMIT`, or `OFFSET` clause of a query.

Positional parameters use an ordinal placeholder for substitution and can be used like this:

```rust
let statement = "SELECT * from `airline` WHERE country = $1;";
let mut result = scope
    .query(
        statement,
        QueryOptions::new().add_positional_parameter("United States")?,
    )
    .await?;
```

Whereas named parameters can be used like this:

```rust
let statement = "SELECT * from `airline` WHERE country = $country;";
let mut result = scope
    .query(
        statement,
        QueryOptions::new().add_named_parameter("country", "United States")?,
    )
    .await?;
```

## [](#scan-consistency)Scan Consistency

Queries take an optional `scanConsistency` parameter that enables a tradeoff between latency and (eventual) consistency.

* A SQL++ query using the default `NotBounded` scan consistency will not wait for any indexes to finish updating before running the query and returning results, meaning that results are returned quickly, but the query will not return any documents that are yet to be indexed.
* With scan consistency set to `RequestPlus`, all outstanding document changes and index updates are processed before the query is run. Select this when consistency is always more important than performance.
* For a middle ground, `AtPlus` is a "read your own write" (RYOW) option, which means it just waits for the documents that you specify to be indexed.

Here’s how to specify the `RequestPlus` scan consistency level:

```rust
    let result = cluster
        .bucket("travel-sample")
        .scope("inventory")
        .query(
            "SELECT count(*) from `airport`",
            QueryOptions::new().scan_consistency(ScanConsistency::RequestPlus),
        )
        .await?;
```

And the `AtPlus` level is represented with `ScanConsistency.AtPlus`, combined with `consistent_with`:

```rust
let mutation_state = {
    let result = cluster
        .bucket("travel-sample")
        .scope("inventory")
        .collection("airport")
        .upsert(
            "airport_1254",
            serde_json::json!({"name": "New Airport"}),
            None,
        )
        .await?;

    // MutationState can be created from a token directly.
    let state = MutationState::from(result.mutation_token().clone().unwrap());

    state
};

let result = cluster
    .bucket("travel-sample")
    .scope("inventory")
    .query(
        "SELECT count(*) from `airport`",
        QueryOptions::new().scan_consistency(ScanConsistency::AtPlus(mutation_state)),
    )
    .await?;
```

## [](#returning-results-as-your-own-type)Returning Results as Your Own Type

The Rust SDK supports returning SQL++ results directly as Rust struct types.

A very small amount of boilerplate is required to tell the SDK how to convert your case class to/from JSON. You can read more about `serde` [here](https://serde.rs/), including how to customize the deserialization process.

```rust
#[derive(Deserialize)]
pub struct Address {
    city: String,
}

#[derive(Deserialize)]
pub struct User {
    name: String,
    address: Vec<Address>,
    age: u8,
}
```

Now you’re free to pull out the results directly as your type:

```rust
let statement = "SELECT name, address, age from `users` LIMIT 10;";
let mut result = scope.query(statement, None).await?;

let mut rows = result.rows();
while let Some(row) = rows.next().await {
    let user: User = row?;
    println!("User: {} in city {}", user.name, user.address[0].city);
}
```

## [](#querying-at-cluster-level)Querying at Cluster Level

The code snippet below shows how to run a simple query to fetch 10 random rows from travel-sample and print the results. Querying at the `Cluster` level without specifying a scope or collection means that the query is implicitly executed against the `_default` collection in the `_default` scope.

```rust
let statement = "SELECT name from `travel-sample` LIMIT 10;";
let mut result = cluster.query(statement, None).await?;
```

## [](#additional-resources)Additional Resources

> [!NOTE]
> SQL++ is not the only query option in Couchbase. Be sure to check that [your use case fits your selection of query service](../concept-docs/querying-your-data.md).

The [SQL++ interactive tutorial](http://query.pub.couchbase.com/tutorial/#1) is a good introduction to the basics of SQL++ use.