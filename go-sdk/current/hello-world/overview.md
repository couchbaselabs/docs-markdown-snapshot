---
title: Couchbase Go SDK 2.12
editUrl: https://github.com/couchbase/docs-sdk-go/edit/release/2.12/modules/hello-world/pages/overview.adoc
pubDate: 2026-04-28T05:36:31.051Z
link: xref:go-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/current/hello-world/overview.html)

# Couchbase Go SDK 2.12

# Couchbase Go SDK 2.12

The Couchbase Go SDK allows Go applications to access a Couchbase cluster — Capella or self-managed.

[Quickstart Guide](start-using-sdk.md) | [SDK Release Notes](../project-docs/sdk-release-notes.md) | [Go SDK API Reference](https://pkg.go.dev/github.com/couchbase/gocb/v2) | [Go SDK source code](https://github.com/couchbase/gocb)

What's the point of a fast and scalable database if it's not easy to develop for? Couchbase gives you the Go APIs to work with Capella, our managed solution, or self-managed options in your private Cloud or datacenter.

* Data Ops (CRUD)
* SQL++ Query (OLTP)
* Vector Search

```golang
// Upsert with Durability level Majority
durableResult, err := collection.Upsert("document-key", &document, &gocb.UpsertOptions{
	DurabilityLevel: gocb.DurabilityLevelMajority,
})
```

```golang
query := "SELECT x.* FROM `travel-sample`.inventory.hotel x WHERE x.`city`= $1 LIMIT 10"
rows, err := cluster.Query(query, &gocb.QueryOptions{
	ScanConsistency:      gocb.QueryScanConsistencyRequestPlus,
	PositionalParameters: []interface{}{"San Francisco"},
	Adhoc:                true,
})
if err != nil {
	panic(err)
}
```

```golang
request := gocb.SearchRequest{
	VectorSearch: vector.NewSearch(
		[]*vector.Query{
			vector.NewQuery("vector_field", vectorQuery).NumCandidates(2).Boost(0.3),
			vector.NewQuery("vector_field", anotherVectorQuery).NumCandidates(5).Boost(0.7),
		}, nil,
	),
	SearchQuery: search.NewMatchAllQuery(),
}
vectorResult, err := scope.Search("vector-and-fts-index", request, nil)
if err != nil {
	panic(err)
}
```

Couchbase is a large platform — covering many services — and Couchbase SDKs are not thin wrappers generated around a REST API, but well thought out interfaces to the platform that make it easier to design and maintain your client code, and work with Couchbase in more natural ways for your platform. Install the SDK, and explore in the way that works best for you.

Installing the SDK

```console
$ go get github.com/couchbase/gocb/v2
```

In line with the [Golang project](https://golang.org/doc/devel/release.html#policy), we support both the current, and the previous, versions of Go. At time of writing (February 2026), this is 1.25 and 1.26\. Older versions may remain compatible, but are not supported.

The links below will take you where you want to go — as will the navigation on the left-hand side of this page. But if you don't know exactly where you need to go, try one of the following:

* Our [Quickstart Guide](start-using-sdk.md) introduces the SDK with a quick install, and CRUD examples against the Data Service.
* Couchbase's familiar SQL-family query language and fuzzy search options (including vector search) are introduced on the [Querying Your Data](../concept-docs/querying-your-data.md) page.
* The Go SDK docs are, necessarily, just a sub-set [Go SDK API Reference](https://pkg.go.dev/github.com/couchbase/gocb/v2) — and a complete reference of all APIs can be found there.
* For a fuller orientation, there is a [guide to the Go SDK docs](../project-docs/metadoc-about-these-sdk-docs.md)

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the Go SDK.

Easy to Connect & Get Started

* [Quickstart Guide](start-using-sdk.md)
* [Quickstart with Golang and the Gin Web Framework](sample-application.md)
* [Managing Connections](../howtos/managing-connections.md)

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../howtos/full-text-searching-with-sdk.md)
* [OLAP — long running analytical queries](../howtos/analytics-using-sdk.md)

Lightning Fast Data Service

* [Data Operations](../howtos/kv-operations.md)
* [Sub-Document Operations](../howtos/subdocument-operations.md)
* [Encrypting Your Data](../howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../howtos/error-handling.md)
* [Logging](../howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../howtos/slow-operations-logging.md)
* [Health Check](../howtos/health-check.md)

  
##  Resources

Useful resources to help support your development experience with Couchbase and the Go SDK.

Reference

* [API Reference](https://pkg.go.dev/github.com/couchbase/gocb/v2)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [SDK source code](https://github.com/couchbase/gocb)

Deployment

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Integrations & Ecosystem](../project-docs/third-party-integrations.md)
* [Couchbase Go SDK Installation](../project-docs/sdk-full-installation.md)
  
  
##  Couchbase Operational Cluster Feature Compatibility

All of the SDKs have API compatibility with most of the features in Couchbase Operational Clusters — whether self-managed, or Capella. The following table covers possible exceptions, and gives the version of the Go SDK and Couchbase Server with which some features were introduced.

__Table 1\. Couchbase Server and SDK Supported Version Matrix__
|                                                                                              | Server 7.2  | Server 7.6.x      | Server 8.0 |
| -------------------------------------------------------------------------------------------- | ----------- | ----------------- | ---------- |
| KV Range Scan                                                                                | N/A         | From 2.7.0        |            |
| Zone aware replica reads                                                                     | N/A         | From 2.9.2        |            |
| Vector Search with Search Vector Index                                                       | N/A         | From 2.8.0        |            |
| Vector Query using Hyperscale Vector Index                                                   | N/A         | From SDK 2.11.0 ① |            |
| Vector Query using Composite (GSI & vector) index                                            | N/A         | From SDK 2.11.0 ① |            |
| Distributed ACID Transactions                                                                | From 2.4.0  |                   |            |
| DNS SRV refresh for serverless environments (AWS Lambda, Azure Functions, and GCP Functions) | From 2.6.0  |                   |            |
| Circuit Breakers                                                                             | From 2.0.0  |                   |            |
| OTel                                                                                         | From 2.12.0 |                   |            |
| Field Level Encryption                                                                       | From 1.5.0  |                   |            |
| Cloud Native Gateway                                                                         | From 2.7.0  |                   |            |

| **1** | As part of the standard SDK SQL++ API, it should be compatible with all earlier versions of the SDK — but it has not been tested. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------- |

  
> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.