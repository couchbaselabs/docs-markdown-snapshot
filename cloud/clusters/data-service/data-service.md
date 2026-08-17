---
title: Manage Your Data
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/data-service/data-service.adoc
  xref: xref:cloud:clusters:data-service/data-service.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/data-service/data-service.html)

# Manage Your Data

> The Data Service provides access to data. It supports the storing, setting, and retrieving of data-items, specified by key. 

The _Data Service_ is the most fundamental of all Couchbase services, providing read/write access to data in memory and on disk. The Data Service stores data items in _Buckets_. Before an item can be saved, a bucket must exist for it. Buckets only exist on nodes that run the Data Service.

## [](#deploying-the-data-service)Deploying the Data Service

The Data Service must run on at least one node of every cluster. However, at least three nodes are required for production environments. (Clusters with less than three Data nodes have [several limitations](../../../server/current/install/deployment-considerations-lt-3nodes.md).)

The Data Service provides a fully integrated in-memory caching layer, which provides high-speed data access. Couchbase Capella supports the [_Couchbase_ bucket type](../../../server/current/learn/buckets-memory-and-storage/buckets.md#bucket-types), which means that all data items are written to memory and persisted to disk. The Data Service manages memory to ensure high performance and scalability: memory quotas are established, and data not recently used can be ejected, to make room for data more frequently requested. You can configure a memory quota that provides caching for all or a portion of stored data items.

Read more about [Memory and Storage](../../../server/current/learn/buckets-memory-and-storage/memory-and-storage.md).

## [](#buckets)Buckets

Couchbase Capella uses buckets to group collections of keys and values logically. Buckets must be created before you can store any data. A maximum of 30 buckets can be created per cluster.

Buckets are protected by role-based access control (RBAC). Buckets can only be administered (created, modified, and deleted) by users that have the [Project Owner](../../projects/project-roles.md#project-owner-role) or [Cluster Manager](../../projects/project-roles.md#project-cluster-manager-role) project roles.

## [](#scopes-collections)Scopes and Collections

Couchbase Capella uses scopes and collections to categorize and organize documents within a bucket. Collections are data containers within a bucket, while scopes are mechanisms to group multiple collections. Each cluster can have up to 1000 scopes and 1000 collections.

Every bucket automatically includes the `_default` scope that itself contains the `_default` collection. Any document that's created within a bucket that does not reference a scope or collection is saved in the `_default` collection within the `_default` scope.

You cannot delete a bucket's `_default` scope. While you can delete the `_default` collection, there is no actual advantage in deleting it. The `_default` collection is there to help group and organize documents without a set scope. If you delete it, you'll not be able to recreate or recover it later.

Role-based access control (RBAC) is used to protect scopes and collections. Only project members with the [Project Owner](../../projects/project-roles.md#project-owner-role) or [Cluster Manager](../../projects/project-roles.md#project-cluster-manager-role) project roles can administer them.

For more information, see [Scopes and Collections](../../../server/current/learn/data/scopes-and-collections.md).