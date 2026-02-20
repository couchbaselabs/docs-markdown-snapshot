---
title: Buckets, Scopes, and Collections
description: The data in a Couchbase Capella cluster is categorized and
  organized into different data containers.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/data-service/about-buckets-scopes-collections.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:clusters:data-service/about-buckets-scopes-collections.adoc[]
---

[View original HTML](/cloud/clusters/data-service/about-buckets-scopes-collections.html)

# Buckets, Scopes, and Collections

> The data in a Couchbase Capella cluster is categorized and organized into different data containers. These data containers hold documents, which hold JSON key-value pairs that define your data. 

Capella clusters have 3 types of data containers:

* [Buckets](#buckets)
* [Scopes](#scopes)
* [Collections](#collections)

![Diagram](../_images/diag-cb5d8600a1de6e8181323bf018c8c29f69ee3450.svg) 

Use the hierarchy of buckets, scopes, and collections to categorize and organize your data for quick and easy retrieval.

Store documents in collections and group similar collections with scopes. For example, you could use scopes and collections to group data in a travel application:

![Diagram](../_images/diag-000acf74d2f2b661d42bdf793571f72906383e34.svg) 

> [!TIP]
> You can create new buckets, scopes, and collections when you import data into your cluster. For more information, see [Import Data with the Capella UI](import-data-documents.md).

## [](#buckets)Buckets

Buckets are the top-level storage containers for data in a Capella cluster.

You must create a bucket before you can store any data in your cluster. A Capella cluster can have a maximum of 30 buckets.

![Diagram](../_images/diag-651804110f3bcc1ed3ab2ef8e49fe60e1641975a.svg) 

For more information about how to create a new bucket, see [Create a Bucket](manage-buckets.md#add-bucket).

## [](#scopes)Scopes

A scope is a data container that exists inside a Capella bucket. Use scopes to group related [collections](#collections).

Each scope must contain at least 1 collection. A cluster can hold up to 1000 collections, and you can spread this number across multiple scopes and buckets. Buckets are also limited to 1 collection per MB of memory quota.

![Diagram](../_images/diag-b049801fbd52303a31d064061e0437dc69e0dc77.svg) 

For more information about how to create a new scope, see [Create a Scope](scopes-collections.md#create-scope).

### [](#%5Fdefault-scope)\_default Scope

When you create a bucket in your Capella cluster, a `_default` scope and collection are automatically created within that bucket. Any document that you create without a specific scope and collection is assigned to the `_default` scope and collection.

You cannot delete the `_default` scope.

### [](#%5Fsystem-scope)\_system Scope

> [!IMPORTANT]
> The `_system` scope is part of all clusters using Couchbase Server 7.6 or later. When you upgrade a cluster to Couchbase Server 7.6, Capella adds the `_system` scope to your existing buckets.

All sample buckets and buckets that you create include a `_system` scope. The `_system` scope contains the `_mobile` and `_query` collections that store system documents for related Couchbases services.

The `_system` scope and its collections are read-only, and their structure is subject to change without notice. Do not use these collections for other purposes.

You cannot remove the `_system` scope or its collections.

## [](#collections)Collections

A collection is a data container that exists inside a Capella [scope](#scopes). It’s the smallest container that holds the documents inside a [bucket](#buckets).

Each cluster can have a maximum of 1000 collections. You can spread this number of collections across multiple scopes and buckets. Buckets are also limited to 1 collection per MB of memory quota.

![Diagram](../_images/diag-dada333daf64c5aaad187a9e4490270010e46f81.svg) 

For more information about how to create a new collection, see [Create a Collection](scopes-collections.md#create-collection).

### [](#default-collections)\_default Collection

When you create a bucket in your Capella cluster, a `_default` collection is automatically created within your `_default` scope. Any document that you create without a specific scope and collection is assigned to the `_default` scope and collection.

You can delete the `_default` collection from the `_default` scope using the Couchbase Capella UI, API, SDKs, or queries. While you can delete the `_default` collection, there is no actual advantage to this. The `_default` collection is there to help group and organize documents without a set scope. If you decide to delete it, you’ll not be able to recreate or recover it later.

### [](#linking-collections)Linking Collections

You must link collections to your App Endpoints to use data contained within them for your mobile and IoT applications. For more information about collection linking and unlinking, see [linking a collection](../../../app-services/app-endpoints/creating-an-app-endpoint.md#linking-a-collection).

## [](#see-also)See Also

* [Manage Buckets](manage-buckets.md)
* [Manage Scopes and Collections](scopes-collections.md)
* [Manage Documents with the Capella UI](manage-documents.md)
* [Storage Engines](storage-engines.md)
* [Manage Replications](../xdcr/manage-xdcr-replications.md)