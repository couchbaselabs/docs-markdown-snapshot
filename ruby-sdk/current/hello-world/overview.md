---
title: Couchbase Ruby SDK 3.9
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Ruby SDK
    version: "3.9"
antora:
  editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/release/3.9/modules/hello-world/pages/overview.adoc
  xref: xref:ruby-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/current/hello-world/overview.html)

# Couchbase Ruby SDK 3.9

# Couchbase Ruby SDK 3.9

The Couchbase Ruby SDK allows Ruby applications to access a Couchbase cluster — Capella or self-managed. The Ruby SDK includes high-performance native Ruby extensions to handle communicating to the cluster over Couchbase's binary protocols.

[Quickstart Guide](start-using-sdk.md) | [SDK Release Notes](../project-docs/sdk-release-notes.md) | [Ruby SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase.html) | [Ruby SDK source code](https://github.com/couchbase/couchbase-ruby-client)

A fast and scalable database is even better when it's easy to develop for. Couchbase gives you the Ruby APIs to work with Capella, our managed solution, or self-managed options in your private Cloud or datacenter.

* Data Ops (CRUD)
* SQL++ Query (OLTP)
* Vector Search

```ruby
agent_scope = bucket.scope("tenant_agent_00")
users_collection = agent_scope.collection("users")
document = {"name" => "John Doe", "preferred_email" => "johndoe111@test123.test"}

result = users_collection.upsert("user-key", document)
```

```ruby
options = Cluster::QueryOptions.new
options.named_parameters({"country" => "France"})
result = cluster.query(
    'SELECT COUNT(*) AS airport_count FROM `travel-sample` WHERE type = "airport" AND country = $country',
    options)
puts "Airports in France: #{result.rows.first["airport_count"]}"
#=> Airports in France: 221
```

```ruby
request = SearchRequest.new(
  VectorSearch.new(
    [
      VectorQuery.new('vector_field', vector_query) do |q|
        q.num_candidates = 2
        q.boost = 0.3
      end,
      VectorQuery.new('vector_field', another_vector_query) do |q|
        q.num_candidates = 5
        q.boost = 0.7
      end,
    ],
    Options::VectorSearch.new(vector_query_combination: :and)
  )
)
result = scope.search('vector-index', request)

result.rows.each do |row|
  puts "Document ID: #{row.id}, search score: #{row.score}"
end
```

Couchbase is a large platform — covering many services — and Couchbase SDKs are not thin wrappers generated around a REST API, but well thought out interfaces to the platform that make it easier to design and maintain your client code, and work with Couchbase in more natural ways for your platform. Install the SDK, and explore in the way that works best for you.

Installing the SDK via RubyGem

```console
$ gem install couchbase
```

The Couchbase Ruby SDK integrates into the Ruby ecosystem through a number of extensions and connectors, including:

* [Rails Cache Store](https://guides.rubyonrails.org/caching%5Fwith%5Frails.html#cache-stores)

  
## Exploring the Ruby SDK

The links in the sections below will take you where you want to go — as will the navigation on the left-hand side of this page. But if you don't know exactly where you need to go, try one of the following:

* Our [Quickstart Guide](start-using-sdk.md) introduces the SDK with a quick install, and CRUD examples against the Data Service.
* Couchbase's familiar SQL-family query language and fuzzy search options (including vector search) are introduced on the [Querying Your Data](../concept-docs/querying-your-data.md) page.
* The Ruby SDK docs are, necessarily, just a sub-set [Ruby SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase.html) — and a complete listing of all APIs can be found in the reference.
* For a fuller orientation, there is a [guide to the Ruby SDK docs](../project-docs/metadoc-about-these-sdk-docs.md)

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the Ruby SDK.

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

Observability & Error Handling

* [Handling Errors](../howtos/error-handling.md)
* [Logging](../howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../howtos/slow-operations-logging.md)

  
##  Resources

Useful resources to help support your development experience with Couchbase and the Ruby SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase.html)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [SDK source code](https://github.com/couchbase/couchbase-ruby-client)

Deployment

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [3rd Party Integrations](../project-docs/third-party-integrations.md)
* [Full Installation](../project-docs/sdk-full-installation.md)
  
  
##  Couchbase Operational Cluster Feature Compatibility

All of the SDKs have API compatibility with most of the features in Couchbase Operational Clusters — whether self-managed, or Capella. The following table covers possible exceptions, and gives the version of the Ruby SDK and Couchbase Server with which some features were introduced.

__Couchbase Server and SDK Supported Version Matrix__
|                                                                                              | Server 7.2  | Server 7.6.x     | Server 8.0 |
| -------------------------------------------------------------------------------------------- | ----------- | ---------------- | ---------- |
| KV Range Scan                                                                                | N/A         | From 3.4.4       |            |
| Zone aware replica reads                                                                     | N/A         | From 3.5.5       |            |
| Vector Search with Search Vector Index                                                       | N/A         | From 3.5.0       |            |
| Vector Query using Hyperscale Vector Index                                                   | N/A         | From SDK 3.7.0 ① |            |
| Vector Query using Composite (GSI & vector) index                                            | N/A         | From SDK 3.7.0 ① |            |
| Distributed ACID Transactions                                                                | N/A         |                  |            |
| DNS SRV refresh for serverless environments (AWS Lambda, Azure Functions, and GCP Functions) | From 3.4.0  |                  |            |
| Circuit Breakers                                                                             | Unsupported |                  |            |
| Response Time Observability with OTel                                                        | From 3.8.0  |                  |            |
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