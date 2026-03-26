---
title: Import Filter
description: Introducing <em>import filters</em> and how to use them to speed-up
  the initial import process.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/import-filter.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@sync-gateway::import-filter.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/import-filter.html)

# Import Filter

> Introducing _import filters_ and how to use them to speed-up the initial import process.  

## [](#introduction)Introduction

The purpose of the import filter is to identify the subset of documents eligible to be replicated by Sync Gateway. This subset is based on application requirements, and is applied to all future mutations.

Without a filter (the default), Sync Gateway imports all documents and so we recommend use of this import filter unless there is a compelling use-case against it.

## [](#function-provision)Function Provision

Use the [Database Configuration](rest-api-admin.md#/Database%5FConfiguration/) Admin Rest API endpoint [/{db}/\_config/import\_filter](rest-api-admin.md#/Database%5FConfiguration/update%5Fimport%5Ffilter) to provision an import filter for a database using the `application/javascript` mime type.

If you are using legacy configuration then, you need to include it in your configuration file, see: [import-filter](configuration-properties-legacy.md#databases-this%5Fdb-import%5Ffilter).

## [](#configuration)Configuration

Example 1\. Using an Import Filter

* API
* Legacy

```bash
//
curl -X PUT "http://localhost:4985/froglist/_config/import_filter" \
-H "accept: application/json" \
-H "Content-Type: application/javascript" \
-H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" \ (1)
-d "\"function(doc) {\ if (doc.type != 'mobile') {\ return false\ }\ return true\}\\\""
//
```

| **1** | You will need to provide authentication in the call; unless it is disabled (not recommended in production environment). |
| ----- | ----------------------------------------------------------------------------------------------------------------------- |

```json
//
//  ... Preceding configuration data as required by the user ...
  {
  "databases": {
    "getting-started-db": {
      "bucket": "getting-started-bucket",
      "import_docs": true,
      "num_index_replicas": 0, (1)
      // ... other config as required
      "import_filter": `
      function(doc) { (2)
        if (doc.type != "mobile") {
          return false
        }
        return true
        }`,
      // ... other config as required
  }
  //  ... Further configuration data as required by the user ...

//
```

Configuration properties:

| **1** | The user's username that you created on the Couchbase Server Admin Console.                                                                                                                                                                                            |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The user's password that you created on the Couchbase Server Admin Console.                                                                                                                                                                                            |
| **3** | The [Sync with Couchbase Server](sync-with-couchbase-server.md) feature allows Couchbase Server SDKs to also perform operations on this bucket.                                                                                                                        |
| **4** | num\_index\_replicas is the number of index replicas stored in Couchbase Server, introduced with GSI/N1QL indexing — see [Indexing](indexing.md). If you're running a single Couchbase Server node for development purposes the num\_index\_replicas must be set to 0. |
| **5** | Only import documents which have a type property equal to mobile.                                                                                                                                                                                                      |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function-overview.md)
* [Import filter](#)
* [Access Control](configuration-schema-access-control.md)
* [Add/Update Sync Function](#rest-api-admin.html#/Access%5FControl/update%5Fsync%5Ffunction)
* [Sync Function Overview](sync-function-overview.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)