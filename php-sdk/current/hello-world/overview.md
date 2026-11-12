---
title: Couchbase PHP SDK 4.6
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: PHP SDK
    version: "4.6"
antora:
  editUrl: https://github.com/couchbase/docs-sdk-php/edit/release/4.6/modules/hello-world/pages/overview.adoc
  xref: xref:php-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/current/hello-world/overview.html)

# Couchbase PHP SDK 4.6

# Couchbase PHP SDK 4.6

The Couchbase PHP SDK allows PHP applications to access a Couchbase cluster — Capella or self-managed. The Couchbase PHP SDK is a native PHP extension and uses a high-performance C++ library to handle communicating to the cluster over Couchbase binary protocols.

[Quickstart Guide](start-using-sdk.md) | [SDK Release Notes](../project-docs/sdk-release-notes.md) | [PHP SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-php-client/namespaces/couchbase.html) | [PHP SDK source code](https://github.com/couchbase/couchbase-php-client)

A fast and scalable database is even better when it's easy to develop for. Couchbase gives you the PHP APIs to work with Capella, our managed solution, or self-managed options in your private Cloud or datacenter.

* Data Ops (CRUD)
* SQL++ Query (OLTP)
* Vector Search

```php
// Upsert with Durability
$opts = new UpsertOptions();
$opts->timeout(3000 /* milliseconds */);
$opts->durabilityLevel(DurabilityLevel::MAJORITY);
$res = $collection->upsert("document-key2", $opts);
printf("document \"document-key2\" has been created with CAS \"%s\"\n", $res->cas());
```

```php
$options = new QueryOptions();
$options->positionalParameters(["France"]);
$result = $cluster->query('SELECT x.* FROM `travel-sample`.inventory.hotel x WHERE x.`country`=$1 LIMIT 10;', $options);

foreach ($result->rows() as $row) {
    printf("Name: %s, Address: %s, Description: %s\n", $row["name"], $row["address"], $row["description"]);
}
```

```php
$res = $cluster->query(
    "SELECT d.id, d.question, d.wanted_similar_color_from_search, 
      ARRAY_CONCAT(
        d.couchbase_search_query.knn[0].vector[0:4], 
        ['...']
      ) AS vector 
     FROM `vector-sample`.`color`.`rgb-questions` AS d 
     WHERE d.id = '#87CEEB';",
    QueryOptions::build()->metrics(true)
);
foreach ($res->rows() as $row) {
    print("\nFound match:\n");
    print_r($row);
}
```

Couchbase is a large platform — covering many services — and Couchbase SDKs are not thin wrappers generated around a REST API, but well thought out interfaces to the platform that make it easier to design and maintain your client code, and work with Couchbase in more natural ways for your platform. Install the SDK, and explore in the way that works best for you.

Installing the SDK via pecl

```console
$ pecl install couchbase
```

The Couchbase PHP SDK integrates into the PHP ecosystem through a number of extensions and connectors, including:

* [Laravel-Couchbase](https://github.com/friendsofcat/laravel-couchbase/tree/2.x)
  
  
## Exploring the PHP SDK

The links in the sections below will take you where you want to go — as will the navigation on the left-hand side of this page. But if you don't know exactly where you need to go, try one of the following:

* Our [Quickstart Guide](start-using-sdk.md) introduces the SDK with a quick install, and CRUD examples against the Data Service.
* Couchbase's familiar SQL-family query language and fuzzy search options (including vector search) are introduced on the [Querying Your Data](../concept-docs/querying-your-data.md) page.
* The PHP SDK docs are, necessarily, just a sub-set [PHP SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-php-client/namespaces/couchbase.html) — and a complete listing of all APIs can be found in the reference.
* For a fuller orientation, there is a [guide to the PHP SDK docs](../project-docs/metadoc-about-these-sdk-docs.md)

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the PHP SDK.

Easy to Connect & Get Started

* [Getting Started](start-using-sdk.md)
* [Sample Application](sample-application.md)
* [Managing Connections](../howtos/managing-connections.md)

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../howtos/full-text-searching-with-sdk.md)

Lightning Fast Data Service

* [Data Operations](../howtos/kv-operations.md)
* [Sub-Document Operations](../howtos/subdocument-operations.md)
* [Field Level Encryption from the SDK](../howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../howtos/error-handling.md)
* [Logging](../howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../howtos/slow-operations-logging.md)
* [Diagnosing and preventing Network Problems with Health Check](../howtos/health-check.md)

  
##  Resources

Useful resources to help support your development experience with Couchbase and the PHP SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-php-client/namespaces/couchbase.html)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [SDK source code](https://github.com/couchbase/couchbase-php-client)
* [Glossary](../ref/glossary.md)

Deployment

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [3.x to 4.x Migration Guide](../project-docs/migrating-sdk-code-3.x-to-4.x.md)
* [3rd Party Integrations](../project-docs/third-party-integrations.md)
* [Full Installation](../project-docs/sdk-full-installation.md)
  
  
##  Couchbase Operational Cluster Feature Compatibility

All of the SDKs have API compatibility with most of the features in Couchbase Operational Clusters — whether self-managed, or Capella. The following table covers possible exceptions, and gives the version of the PHP SDK and Couchbase Server with which some features were introduced.

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
| Field Level Encryption                                                                       | N/A         |                  |            |
| Cloud Native Gateway                                                                         | Unsupported |                  |            |

| **1** | As part of the standard SDK SQL++ API, it should be compatible with all earlier versions of the SDK — but it has not been tested. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------- |

  
> [!TIP]
> Operational Insights SDKs
> 
> SDKs for [Operational Insights Enterprise](../../../operational-insights/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Operational Insights Enterprise SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Operational Insights Capella](../../../operational-insights-cloud/intro/intro.md) — as this service does not have Operational Insights Enterprise's load balancer, and uses a different connection protocol. Operational Insights Capella SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Operational Insights Capella (Columnar) SDK pages](../../../home/columnar-sdk.md) for more information.