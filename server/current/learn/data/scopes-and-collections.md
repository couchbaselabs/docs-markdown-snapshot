---
title: Scopes and Collections
description: Couchbase Server provides <em>scopes</em> and <em>collections</em>;
  allowing documents to be categorized and organized, within a bucket.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/learn/pages/data/scopes-and-collections.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:learn:data/scopes-and-collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/learn/data/scopes-and-collections.html)

# Scopes and Collections

> Couchbase Server provides _scopes_ and _collections_; allowing documents to be categorized and organized, within a bucket. 

This page contains an in-depth look at scopes and collections in Couchbase. If you are looking for an introduction to logically partitioning your data with scopes and collections, you may like to start with the [introduction to the topic](../../tutorials/buckets-scopes-and-collections.md#scopes-and-collections) in our developer tutorial.

## [](#understanding-scopes-and-collections)Understanding Scopes and Collections

A _collection_ is a data container, defined on Couchbase Server, within a bucket whose type is either _Couchbase_ or _Ephemeral_. Up to 1000 collections can be created per cluster. Item-names must be unique within their collection. Items can optionally be assigned to different collections according to content-type. For example, within a bucket that contains travel information, documents that relate specifically to _airports_ might be assigned to an _airports_ collection, while documents that relate to _hotels_ might be assigned to a _hotels_ collection, and so on. Applications can be assigned per-collection access-rights; allowing each application to access only those collections it requires.

A collection can be created and managed by means of the Couchbase Web Console UI, the Couchbase CLI, the Couchbase REST API, and SQL++. It can also be created and managed by means of the SDK: see [Collection Management](#3.3@java-sdk:howtos:provisioning-cluster-resources.adoc#collection-management). A collection can be indexed; and it can be dropped. The data in a collection can be replicated, by means of _Cross Data Center Replication_ (XDCR), to another collection in the same or in a different bucket. A collection is named by the administrator when created: it cannot subsequently be renamed.

A _scope_ is a mechanism for the grouping of multiple collections. Up to 1000 scopes can be created per cluster. Collection-names must be unique within their scope. Collections might be assigned to different scopes according to content-type, or to deployment-phase (ie, test versus production). Applications can be assigned per-scope access-rights; allowing each application to access only those scopes it requires.

A scope can be created and managed by means of the Couchbase Web Console UI, the Couchbase CLI, the Couchbase REST API, and SQL++. It can also be created and managed by means of the SDK: see [Collection Management](#3.3@java-sdk:howtos:provisioning-cluster-resources.adoc#collection-management). A scope can be dropped. A scope cannot be indexed. The contents of a scope can be replicated, by means of _Cross Data Center Replication_ (XDCR), to another scope in the same or in a different bucket. A scope is named by the administrator when created: it cannot subsequently be renamed.

### [](#benefits-of-scopes-and-collections)Benefits of Scopes and Collections

The benefits of scopes and collections include:

* The logical grouping of similar documents; potentially simplifying operations such as query, XDCR, and backup and restore.
* The increased efficiency of indexing, due to the Data Service being able to provide documents from specific collections to the Index Service.
* Simplified querying, since query statements are able to easily specify particular subsets of documents.
* Easier migration from relational databases to Couchbase Server, since collections can be designed to correspond to pre-existing relational tables.
* Secure isolation of different document-types, within a bucket; allowing applications to be specifically authorized to use only their appropriate subsets of data (see [Access to Scopes and Collections](#access-to-scopes-and-collections), below).

## [](#naming-for-scopes-and-collections)Naming for Scopes and Collections

User-defined scopes and collections must be assigned user-defined names. Such names:

* Must be between 1 and 251 characters in length.
* Can only contain the characters `A-Z`, `a-z`, `0-9`, and the symbols `_`, `-`, and `%`. Note that scope and collection names are _case sensitive_.
* Cannot start with `_` or `%`.

The namespace within a scope is independent of any other namespace within any other scope: consequently, the same collection-name can exist in multiple scopes, within a single bucket. Similarly, the namespace within a collection is independent of any other namespace within any other collection: consequently, the same document-key can exist in multiple collections, within a single scope.

## [](#default-scope-and-collection)Default Scope and Collection

Every created bucket is automatically given a _default scope_, and within it, a _default collection_. Each is named `_default`. All documents created within the bucket without reference to specific scopes or collections are saved in the default collection, within the default scope. On upgrade from a version of Couchbase Server prior to 7.0, all existing data is automatically placed in the default scope and default collection.

The default scope cannot be dropped. The default collection _can_ be dropped, by means of either the Couchbase CLI, or the REST API. Once dropped, the default collection cannot be recreated.

## [](#the-%5Fsystem-scope-and-its-collections)The `_system` Scope, and its Collections

In Couchbase Server 7.6 and later versions, in each user-created or sample bucket, a `_system` scope is created and maintained by default. This scope contains collections used by Couchbase services, for service-specific data. The scope and its collections _cannot_ be dropped.

> [!WARNING]
> Users should NOT rely on the content of those collections. Their structure is subject to change without warning.

For reference, the collections are as follows:

`_mobile`

Sync-Gateway owned metadata.

`_query`

This collection stores:

* Cost-Based Optimizer statistics, gathered through `UPDATE STATISTICS`/`ANALYZE`
* Metadata about Query side User Defined Functions.

## [](#access-to-scopes-and-collections)Access to Scopes and Collections

Access to scopes and collections is protected by _Role-Based Access Control_ (RBAC): therefore, appropriate roles must be assigned.

For information on RBAC, see [Authorization](../security/authorization-overview.md). For a list of roles, see [Roles](../security/roles.md). For examples of how to assign roles to scopes and collections, see [Manage Users, Groups, and Roles](../../manage/manage-security/manage-users-and-roles.md).

## [](#tenant-separation)Tenant Separation

A query may refer to a collection using an absolute _keyspace path_; or a relative _partial keyspace reference_, which must be resolved by means of the _query context_. The use of partial keyspace references and query context supports the separation of tenant data in a multi-tenancy environment. For details, refer to [Query Context](../../n1ql/n1ql-intro/queriesandresults.md#query-context).

## [](#expiration-and-collections)Expiration and Collections

An _expiration_ value can be established on a collection: this determines the maximum expiration time of individual items within the collection. For information, see [Expiration](expiration.md).

## [](#change-history)Change History

When _Magma_ storage is used for a bucket, the changes made to documents within the bucket’s collections can be recorded, in a _change history_. The change history resides on disk. Its capacity is administrator-specified. When the change history is full, old records are automatically removed (by means of compaction), to allow space for new records.

For detailed information, see [Change History](change-history.md).

## [](#managing-scopes-and-collections)Managing Scopes and Collections

See [Manage Scopes and Collections](../../manage/manage-scopes-and-collections/manage-scopes-and-collections.md), for information on how to use the CLI and REST API to create, maintain, and delete scopes and collections.

For information on using the Backup Service to _inspect_ scopes and collections within backed-up data, and to _restore_ data to specific scopes and collections, see [Manage Backup and Restore](../../manage/manage-backup-and-restore/manage-backup-and-restore.md).

For information on using scopes and collections with _Cross Data Center Replication_ (XDCR), see [Replicate Using Scopes and Collections](../../manage/manage-xdcr/replicate-using-scopes-and-collections.md).

For a complete reference to the CLI command for managing scopes and collections, see [collection-manage](../../cli/cbcli/couchbase-cli-collection-manage.md).

For reference pages for the REST API commands that manage scopes and collections, see [Scopes and Collections REST API](../../rest-api/scopes-and-collections-api.md).

For the `cbstats` reference pages for scopes and collections, see [scopes](../../cli/cbstats/cbstats-scopes.md), [scopes-details](../../cli/cbstats/cbstats-scopes-details.md), [collections](../../cli/cbstats/cbstats-collections.md), and [collections-details](../../cli/cbstats/cbstats-collections-details.md).

As indicated above, it is possible to create, maintain, and delete scopes and collections using {sql++}. See the [SQL++ Language Reference](../../n1ql/n1ql-language-reference/index.md) for further details.

## [](#working-with-collections-from-couchbase-sdks)Working with Scopes and Collections from Couchbase SDKs

The 3.x API versions of Couchbase SDKs work with scopes and collections. For information, see the [Java Howto doc](#3.3@java-sdk:howtos:working-with-collections.adoc).