---
title: Couchbase Rust SDK 1.0
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/hello-world/pages/overview.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:rust-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/hello-world/overview.html)

# Couchbase Rust SDK 1.0

# Couchbase Rust SDK 1.0

The Couchbase Rust SDK allows Rust applications to access a Couchbase cluster — Capella or self-managed.

[Quickstart Guide](start-using-sdk.md) | [SDK Release Notes](../project-docs/sdk-release-notes.md) | [Rust SDK API Reference](https://docs.rs/couchbase/latest/couchbase/) | [Rust SDK source code](https://github.com/couchbase/couchbase-rs/)

What’s the point of a fast and scalable database if it’s not easy to develop for? Couchbase gives you the Rust APIs to work with Capella, our managed solution, or self-managed options in your private Cloud or datacenter.

* Data Ops (CRUD)
* SQL++ Query (OLTP)
* Vector Search

```rust
let doc = json!({
        "foo": "bar",
        "baz": "qux",
});

match collection.upsert("document-key", doc, None).await {
    Ok(_result) => {
        println!("Document upsert successful");
    }
    Err(e) => {
        println!("Error: {e}");
    }
}
```

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

```rust
let request = SearchRequest::with_vector_search(VectorSearch::new(
    vec![VectorQuery::with_vector("vector_field", vector_query)],
    None,
));

let result = scope.search("vector-index", request, None).await?;
```

Couchbase is a large platform — covering many services — and Couchbase SDKs are not thin wrappers generated around a REST API, but well thought out interfaces to the platform that make it easier to design and maintain your client code, and work with Couchbase in more natural ways for your platform. Install the SDK, and explore in the way that works best for you.

Installing the SDK via Rust Cargo

```none
cargo add couchbase
```

The links below will take you where you want to go — as will the navigation on the left-hand side of this page. But if you don’t know exactly where you need to go, try one of the following:

* Our [Quickstart Guide](start-using-sdk.md) introduces the SDK with a quick install, and CRUD examples against the Data Service.
* Couchbase’s familiar SQL-family query language and fuzzy search options (including vector search) are introduced on the [Querying Your Data](../concept-docs/querying-your-data.md) page.
* The Rust SDK docs are, necessarily, just a sub-set [Rust SDK API Reference](https://docs.rs/couchbase/latest/couchbase/) — and a complete reference of all APIs can be found there.
* For a fuller orientation, there is a [guide to the Rust SDK docs](../project-docs/metadoc-about-these-sdk-docs.md)

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the Rust SDK.

Easy to Connect & Get Started

* [Quickstart Guide](start-using-sdk.md)
* [Managing Connections](../howtos/managing-connections.md)

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../howtos/full-text-searching-with-sdk.md)

Lightning Fast Data Service

* [Data Operations](../howtos/kv-operations.md)
* [Sub-Document Operations](../howtos/subdocument-operations.md)

Observability & Error Handling

* [Handling Errors](../howtos/error-handling.md)
* [Logging](../howtos/collecting-information-and-logging.md)
* [Health Check](../howtos/health-check.md)

  
##  Resources

Useful resources to help support your development experience with Couchbase and the Rust SDK.

Reference

* [API Reference](https://docs.rs/couchbase/latest/couchbase/)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [SDK source code](https://github.com/couchbase/couchbase-rs/)

Deployment

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Integrations & Ecosystem](../project-docs/third-party-integrations.md)
* [Couchbase Rust SDK Installation](../project-docs/sdk-full-installation.md)
  
  
##  Couchbase Operational Cluster Feature Compatibility

All of the SDKs have API compatibility with most of the features in Couchbase Operational clusters — whether self-managed, or Capella. The following table covers possible exceptions, and gives the version of the Rust SDK and Couchbase Server with which some features were introduced.

__Couchbase Server and SDK Supported Version Matrix__
|                                  | Server 7.6.x               | Server 8.0       |
| -------------------------------- | -------------------------- | ---------------- |
| KV Range Scan                    | All SDK versions           |                  |
| Vector Search                    | All SDK versions           |                  |
| Zone aware replica reads         | All SDK versions           |                  |
| KV preferred server groups reads | All SDK versions           |                  |
| Vector Query using GSI           | N/A                        | All SDK versions |
| Distributed ACID Transactions    | N/A                        |                  |
| Response Time Observability      | All supported SDK versions |                  |
| Field Level Encryption           | N/A                        |                  |
| Cloud Native Gateway             | N/A                        |                  |

  
> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase’s analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.