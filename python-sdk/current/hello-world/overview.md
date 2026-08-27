---
title: Couchbase Python SDK 4.6
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/release/4.6/modules/hello-world/pages/overview.adoc
  xref: xref:python-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/hello-world/overview.html)

# Couchbase Python SDK 4.6

# Couchbase Python SDK 4.6

The Couchbase Python SDK allows Python applications to access a Couchbase cluster — Capella or self-managed.

[Quickstart Guide](start-using-sdk.md) | [SDK Release Notes](../project-docs/sdk-release-notes.md) | [Python SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/) | [Python SDK source code](https://github.com/couchbase/couchbase-python-client)

A fast and scalable database is even better when it's easy to develop for. Couchbase gives you the Python APIs to work with Capella, our managed solution, or self-managed options in your private Cloud or datacenter.

* Data Ops (CRUD)
* SQL++ Query (OLTP)
* Vector Search

```python
# Upsert with Durability level Majority
document = dict(foo="bar", bar="foo")
opts = UpsertOptions(durability=ServerDurability(Durability.MAJORITY))
result = collection.upsert("document-key", document, opts)
```

```python
result = cluster.query(
    "SELECT ts.* FROM `travel-sample`.inventory.airport WHERE city=$city",
    QueryOptions(named_parameters={"city": "San Jose"}))
```

```python
  result = cluster.query(
         "SELECT d.id, d.question, d.wanted_similar_color_from_search, " +
         "  ARRAY_CONCAT( " +
           "d.couchbase_search_query.knn[0].vector[0:4], " +
           "['...'] " +
         ") AS vector " +
      "FROM `vector-sample`.`color`.`rgb-questions` AS d " +
  	"WHERE d.id = $id;",
  QueryOptions(named_parameters={'id': '#87CEEB'})

    for row in result.rows():
        print(f"Found match: {row}")
```

Couchbase is a large platform — covering many services — and Couchbase SDKs are not thin wrappers generated around a REST API, but well thought out interfaces to the platform that make it easier to design and maintain your client code, and work with Couchbase in more natural ways for your platform. Install the SDK, and explore in the way that works best for you.

Installing the SDK via pip

```console
$ python3 -m pip install couchbase
```

The Couchbase Python SDK integrates into the Python ecosystem through a number of extensions and connectors, including:

* [Python with Flask tutorial](https://developer.couchbase.com/tutorial-quickstart-flask-python/)
* [Apache Spark Connector](../../../spark-connector/3.5/pyspark.md)
* [Couchbase Jupyter Labs](https://github.com/couchbase-examples/couchbase-jupyter-labs/)

## Exploring the Python SDK

The links in the sections below will take you where you want to go — as will the navigation on the left-hand side of this page. But if you don't know exactly where you need to go, try one of the following:

* Our [Quickstart Guide](start-using-sdk.md) introduces the SDK with a quick install, and CRUD examples against the Data Service.
* Couchbase's familiar SQL-family query language and fuzzy search options (including vector search) are introduced on the [Querying Your Data](../concept-docs/querying-your-data.md) page.
* The Python SDK docs are, necessarily, just a sub-set [Python SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/) — and a complete listing of all APIs can be found in the reference.
* For a fuller orientation, there is a [guide to the Python SDK docs](../project-docs/metadoc-about-these-sdk-docs.md)

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the Python SDK.

Easy to Connect & Get Started

* [Getting Started](start-using-sdk.md)
* [Sample Application](sample-application.md)
* [Managing Connections](../howtos/managing-connections.md)

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../howtos/full-text-searching-with-sdk.md)
* For real-time analytics, see our [Enterprise Analytics Python SDK](../../../python-analytics-sdk/current/hello-world/overview.md)

Lightning Fast Data Service

* [Data Operations](../howtos/kv-operations.md)
* [Sub-Document Operations](../howtos/subdocument-operations.md)
* [Encrypting Your Data](../howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Error Handling](../howtos/error-handling.md)
* [Logging](../howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../howtos/slow-operations-logging.md)
* [Health Check](../howtos/health-check.md)

  
##  Resources

Useful resources to help support your development experience with Couchbase and the Python SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [SDK source code](https://github.com/couchbase/couchbase-python-client)

Deployment

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Integrations & Ecosystem](../project-docs/third-party-integrations.md)
* [Full Installation](../project-docs/sdk-full-installation.md)
  
  
##  Couchbase Operational Cluster Feature Compatibility

All of the SDKs have API compatibility with most of the features in Couchbase Operational Clusters — whether self-managed, or Capella. The following table covers possible exceptions, and gives the version of the Python SDK and Couchbase Server with which some features were introduced.

__Couchbase Server and SDK Supported Version Matrix__
|                                                                                              | Server 7.2  | Server 7.6.x     | Server 8.0 |
| -------------------------------------------------------------------------------------------- | ----------- | ---------------- | ---------- |
| KV Range Scan                                                                                | N/A         | From 4.2.0       |            |
| Zone aware replica reads                                                                     | N/A         | From 4.4.0       |            |
| Vector Search with Search Vector Index                                                       | N/A         | From 4.2.0       |            |
| Vector Query using Hyperscale Vector Index                                                   | N/A         | From SDK 4.5.0 ① |            |
| Vector Query using Composite (GSI & vector) index                                            | N/A         | From SDK 4.5.0 ① |            |
| Distributed ACID Transactions                                                                | From 4.0.0  |                  |            |
| DNS SRV refresh for serverless environments (AWS Lambda, Azure Functions, and GCP Functions) | From 4.1.5  |                  |            |
| Circuit Breakers                                                                             | Unsupported |                  |            |
| Response Time Observability with OTel                                                        | From 4.6.0  |                  |            |
| Field Level Encryption                                                                       | From 3.2.0  |                  |            |
| Cloud Native Gateway                                                                         | Unsupported |                  |            |

| **1** | As part of the standard SDK SQL++ API, it should be compatible with all earlier versions of the SDK — but it has not been tested. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------- |

  
> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.