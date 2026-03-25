---
title: Import Filter
description: Introducing <em>import filters</em> and how to use them to speed-up
  the initial import process.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/import-filter.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::import-filter.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/import-filter.html)

# Import Filter

> Introducing _import filters_ and how to use them to speed-up the initial import process.  
> This topic provides an example configuration of Import filters

## [](#introduction)Introduction

Sync Gateway’s initial import process can take a considerable time to complete for clusters with a large amount of data. The process can be made more efficient by using an _Import filter_. Without a filter (the default), Sync Gateway imports all documents.

## [](#configuration)Configuration

To get started with a clusters which contains a large number of pre-existing documents, we recommend you use an `import_filter` to filter out unwanted data and reduce the initial import processing time — see: [Example 1](#ex-config).

Example 1\. Using an Import Filter

```json
//
{
  //  ... may be preceded by additional configuration data as required by the user ...
  "databases": {
    "getting-started-db": {
      "server": "http://localhost:8091",
      "bucket": "getting-started-bucket",
      "username": "sync_gateway", (1)
      "password": "password", (2)
      "enable_shared_bucket_access": true, (3)
      "import_docs": true,
      "num_index_replicas": 0, (4)
      "import_filter": `
        function(doc) { (5)
          if (doc.type != "mobile") {
            return false
          }
          return true
        }`,
      "users": {
        "GUEST": { "disabled": false, "admin_channels": ["*"] }
      },
      "sync": `function (doc, oldDoc) {
        if (doc.sdk) {
          channel(doc.sdk);
        }
      }`
    }
  }
  //  ... may be followed by additional configuration data as required by the user ...
}
//
```

Configuration properties:

| **1** | The user’s username that you created on the Couchbase Server Admin Console.                                                                                                                                                                                                                           |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The user’s password that you created on the Couchbase Server Admin Console.                                                                                                                                                                                                                           |
| **3** | The [Sync with Couchbase Server](../current/sync/sync-with-couchbase-server.md) feature allows Couchbase Server SDKs to also perform operations on this bucket.                                                                                                                                       |
| **4** | num\_index\_replicas is the number of index replicas stored in Couchbase Server, introduced with GSI/N1QL indexing — see [Indexing versus Views](../current/deploy/indexing.md). If you’re running a single Couchbase Server node for development purposes the num\_index\_replicas must be set to 0. |
| **5** | Only import documents which have a type property equal to mobile.                                                                                                                                                                                                                                     |

## [](#related-content)Related Content

###### [](#)

Learn more …​

* [Sync Function](../current/access-control/sync-function/sync-function.md)
* [Import filter](../current/sync/import-processing.md)
* [Inter-Sync Gateway Replication](../current/sync/sync-inter-syncgateway-overview.md)
* [Sync with Couchbase Server](../current/sync/sync-with-couchbase-server.md)

###### [](#-2)

Reference material …​

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)