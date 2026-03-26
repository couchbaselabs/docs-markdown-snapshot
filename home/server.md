---
title: Couchbase Server
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/ROOT/pages/server.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:home::server.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/server.html)

# Couchbase Server

# Couchbase Server

## 

Couchbase is the modern database for enterprise applications.

Couchbase Server is an open source, distributed, JSON document database. It exposes a scale-out, key-value store with managed cache for sub-millisecond data operations, purpose-built indexers for efficient queries, and a powerful query engine for executing SQL-like queries. For mobile and Internet of Things environments Couchbase also runs natively on-device and manages synchronization to the server.

try {
  final QueryResult result = cluster.query("SELECT * FROM `travel-sample`.inventory.airline LIMIT 100",
      queryOptions().metrics(true));

  for (JsonObject row : result.rowsAsObject()) {
    System.out.println("Found row: " + row);
  }

  System.out.println("Reported execution time: " + result.metaData().metrics().get().executionTime());
} catch (CouchbaseException ex) {
  ex.printStackTrace();
}

## Get Started

###### 

New to Couchbase

Read the Getting Started guide for step-by-step instructions to create and connect to the database and run your first query.

[Get Started](../server/current/getting-started/start-here.md)

###### 

Upgrading to v8.x

If you are an existing Couchbase user looking for information to upgrade to Couchbase Server 8.x and use collections and scopes, see [Upgrade and migrate your data to v8.x](../server/current/install/migrating-application-data.md).

###### 

Migrating to Couchbase

Find guidance and considerations when migrating from a different database to Couchbase through this [blog series](https://blog.couchbase.com/moving-from-sql-server-to-couchbase-part-1-data-modeling/).

###### 

Explore Tutorials

Explore Couchbase [Tutorials](https://developer.couchbase.com/tutorials/) to learn how to build and operate apps using Couchbase.

###### 

## Develop Using Couchbase

Build your first sample app

* [Developer's Intro](../server/current/guides/kv-operations.md)
* [Data Model](../server/current/learn/data/document-data-model.md)
* [Hello World Using SDKs](../java-sdk/current/hello-world/start-using-sdk.md)
* [CRUD Using SDKs](../java-sdk/current/howtos/kv-operations.md)

Data Service

* [Data Service](../server/current/learn/services-and-indexes/services/data-service.md)
* [Scopes and Collections](../server/current/learn/data/scopes-and-collections.md)
* [Extended Attributes (XATTRs)](../server/current/learn/data/extended-attributes-fundamentals.md)
* [CRUD using Java SDK](../java-sdk/current/howtos/kv-operations.md)

Querying Data

* [Query Service](../server/current/n1ql/query.md)
* [Indexes and Query Performance](../server/current/indexes/indexing-and-query-perf.md)
* [N1QL Language Reference](../server/current/n1ql/n1ql-language-reference/index.md)
* [Query Using Java SDK](../java-sdk/current/howtos/sqlpp-queries-with-sdk.md)

Full-text Search

* [Search Service](../server/current/search/search.md)
* [Understanding Analyzers](#server:fts:fts-analyzers.adoc)
* [Creating Full Text Indexes](#server:fts:fts.adoc)
* [Search Using Java SDK](../java-sdk/current/howtos/full-text-searching-with-sdk.md)

Choosing the right index

* [Index Service](../server/current/learn/services-and-indexes/services/index-service.md)
* [Index Lifecyle](../server/current/indexes/index-lifecycle.md)
* [Using Indexes](../server/current/indexes/indexing-overview.md)
* [Index Service REST API](../server/current/rest-api/rest-index-service.md)

Analytics

* [Analytics Service](../server/current/learn/services-and-indexes/services/analytics-service.md)
* [N1QL for Analytics](../server/current/analytics/1%5Fintro.md)
* [Tutorial](../server/current/analytics/primer-beer.md)
* [Analytics Using Java SDK](../java-sdk/current/howtos/analytics-using-sdk.md)

Eventing

* [Eventing Service](../server/current/eventing/eventing-overview.md)
* [Language Constructs](../server/current/eventing/eventing-language-constructs.md)
* [Examples: Using the Eventing Service](../server/current/eventing/eventing-examples.md)
* [Eventing REST API](../server/current/eventing-rest-api/index.md)

Transactions

* [Transactions](../server/current/learn/data/transactions.md)
* [Durability](../server/current/learn/data/durability.md)
* [Java Transaction Library](../java-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)
* [N1QL Support for Transactions](../server/current/n1ql/n1ql-language-reference/transactions.md)

Replication

* [Cross Data Center Replication(XDCR) Architecture](../server/current/learn/clusters-and-availability/replication-architecture.md)
* [XDCR Cloud Deployment](../server/current/learn/clusters-and-availability/xdcr-overview.md)
* [Manage XDCR](../server/current/manage/manage-xdcr/xdcr-management-overview.md)

Backup and Restore

* [Backup Service](../server/current/learn/services-and-indexes/services/backup-service.md)
* [Manage Backup and Restore](../server/current/manage/manage-backup-and-restore/manage-backup-and-restore.md)
* [Backup Service REST API](../server/current/rest-api/backup-rest-api.md)

###### 

## Administration

Buckets, Memory, and Storage

* [Database Sharding using vBuckets](../server/current/learn/buckets-memory-and-storage/vbuckets.md)
* [Memory and Storage](../server/current/learn/buckets-memory-and-storage/memory-and-storage.md)
* [Compression](../server/current/learn/buckets-memory-and-storage/compression.md)

Cluster Management

* [Overview](../server/current/manage/management-overview.md)
* [Manage Nodes and Clusters](../server/current/manage/manage-nodes/node-management-overview.md)
* [Manage Buckets](../server/current/manage/manage-buckets/bucket-management-overview.md)

Security

* [Security Overview](../server/current/learn/security/security-overview.md)
* [Authentication](../server/current/learn/security/authentication.md)
* [Manage Certificates](../server/current/manage/manage-security/manage-certificates.md)
* [Authorization](../server/current/learn/security/authorization-overview.md)
* [Manage Users, Groups, and Roles](../server/current/manage/manage-security/manage-users-and-roles.md)

Monitoring and Logging

* [Monitoring](../server/current/manage/monitor/monitor-intro.md)
* [Logging](../server/current/manage/manage-logging/manage-logging.md)
* [Settings](../server/current/manage/manage-settings/manage-settings.md)
* [Troubleshoot](../server/current/manage/troubleshoot/troubleshoot.md)

Installation

* [Deployment Options](../server/current/install/get-started.md)
* [Deployment Guidelines](../server/current/install/install-production-deployment.md)
* [Installation](../server/current/install/install-intro.md)
* [Upgrading Couchbase Server](../server/current/install/upgrade.md)
* [Uninstall](../server/current/install/install-uninstalling.md)

Migrating to v8.x

* [Migrating to a collection-based data model](../server/current/install/migrating-application-data.md)
* [Migrating to Couchbase](https://blog.couchbase.com/moving-from-sql-server-to-couchbase-part-1-data-modeling/)

Couchbase Server Tools

* [Couchbase CLI](../server/current/cli/cli-intro.md)
* [Query Workbench](../server/current/tools/query-workbench.md)
* [cbq - the command line shell for N1QL](../server/current/n1ql/n1ql-intro/cbq.md)
* [Backups using cbbackupmgr](../server/current/backup-restore/enterprise-backup-restore.md)
* [Data Import using cbimport](../server/current/tools/cbimport.md)
* [Couchbase Shell (Beta)](https://couchbase.sh)

References

* [REST API Reference](../server/current/rest-api/rest-intro.md)
* [Metrics Reference](../server/current/metrics-reference/metrics-reference.md)
* [XDCR Reference](#xdcr-reference:xdcr-reference-intro.adoc)
* [Audit Events Reference](#audit-event-reference:audit-event-reference.adoc)
* [Rebalance Reference](#rebalance-reference:rebalance-reference.adoc)

###### 

## Product Docs

###### 

Release Notes

Find information about platform support changes, deprecation notifications, notable improvements, and fixed and known issues in a release.

[Release Notes](../server/current/release-notes/relnotes.md)

###### 

What's New

Find information about new features and enhancements in a release.

[What's new](../server/current/introduction/whats-new.md)

###### 

Editions

Couchbase Server comes in two editions: Enterprise Edition and Community Edition. Find information on the differences between the two editions here.

[Couchbase Server Editions](../server/current/introduction/editions.md)