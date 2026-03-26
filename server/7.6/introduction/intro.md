---
title: Couchbase Server
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/introduction/pages/intro.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.6@server:introduction:intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/introduction/intro.html)

# Couchbase Server

# Couchbase Server

###### 

Couchbase Server is an open source, distributed, JSON document database. It exposes a scale-out, key-value store with managed cache for sub-millisecond data operations, purpose-built indexers for efficient queries and a powerful query engine for executing SQL-like queries. For mobile and Internet of Things environments Couchbase also runs natively on-device and manages synchronization to the server.

###### 

![n1ql ansi join example](_images/n1ql-ansi-join-example.png) 

## Get Started

Concepts

* [Why Couchbase?](why-couchbase.md)
* [SQL++ versus SQL](../learn/data/n1ql-versus-sql.md)
* [Overview of Couchbase Server](../learn/architecture-overview.md)
* [Data & Transactions](../learn/data/data.md)
* [Database Clustering: Buckets, Memory, and Storage](../learn/buckets-memory-and-storage/buckets-memory-and-storage.md)
* [Clusters and Availability](../learn/clusters-and-availability/clusters-and-availability.md)
* [Services](../learn/services-and-indexes/services/services.md)

Installation

* [Deployment Options](../install/get-started.md)
* [Deployment Guidelines](../install/install-production-deployment.md)
* [Installation](../install/install-intro.md)
* [Upgrading Couchbase Server](../install/upgrade.md)
* [Uninstall](../install/install-uninstalling.md)

Tutorials

* [Get Started](../getting-started/start-here.md)
* [Developer Bootstrap Exercises](#tutorials:quick-start:quickstart-docker-image-manual-cb65.adoc)
* [Starter Kits](../getting-started/starter-kits.md)
* [Hello World Using SDKs](../../../java-sdk/current/hello-world/start-using-sdk.md)

## Develop

CRUD Operations

* [Developer's Intro](../develop/intro.md)
* [SDKs](../../../home/sdk.md)
* [CRUD Using SDKs](../../../java-sdk/current/howtos/kv-operations.md)

Transactions & Durability

* [Transactions](../learn/data/transactions.md)
* [Durability](../learn/data/durability.md)

Data Modeling

* [Data Model](../learn/data/document-data-model.md)

### Services

Data Service

* [Data Service](../learn/services-and-indexes/services/data-service.md)
* [Database Sharding Using vBuckets](../learn/buckets-memory-and-storage/vbuckets.md)
* [Bucket Time to Live and Document Expiry](../learn/data/expiration.md)
* [Compression](../learn/buckets-memory-and-storage/compression.md)

Index Service

* [Index Service](../learn/services-and-indexes/services/index-service.md)
* [Global Secondary Indexes](../learn/services-and-indexes/indexes/global-secondary-indexes.md)
* [Availability and Performance](../learn/services-and-indexes/indexes/index-replication.md)
* [Index Scans](../learn/services-and-indexes/indexes/index-scans.md)
* [Index Pushdowns](../learn/services-and-indexes/indexes/index%5Fpushdowns.md)
* [Index Storage Settings](../learn/services-and-indexes/indexes/storage-modes.md)

Query Service

* [Query Service](../n1ql/query.md)
* [Using Indexes for Query Performance](../learn/services-and-indexes/indexes/indexes.md)
* [SQL++ for Query Reference](../n1ql/n1ql-language-reference/index.md)
* [Query](../../../java-sdk/current/howtos/sqlpp-queries-with-sdk.md)

Search Service

* [Search Service](../search/search.md)
* [Troubleshooting and FAQs](../fts/fts-troubleshooting.md)
* [Full Text Search Using SDKs](../../../java-sdk/current/howtos/full-text-searching-with-sdk.md)

Analytics Service

* [Analytics Service](../learn/services-and-indexes/services/analytics-service.md)
* [SQL++ for Analytics Reference](../analytics/1%5Fintro.md)
* [Tutorial](../analytics/primer-beer.md)
* [Analytics Using SDKs](../../../java-sdk/current/howtos/analytics-using-sdk.md)

Eventing Service

* [Eventing Service](../eventing/eventing-overview.md)
* [Language Constructs](../eventing/eventing-language-constructs.md)
* [Examples: Using the Eventing Service](../eventing/eventing-examples.md)

### SDKs

Java SDK

* [Start Using the SDK](../../../java-sdk/current/hello-world/start-using-sdk.md)
* [Managing Connections](../../../java-sdk/current/howtos/managing-connections.md)
* [CRUD Using SDKs](../../../java-sdk/current/howtos/kv-operations.md)
* [Concurrent Document Mutations](../../../java-sdk/current/howtos/concurrent-document-mutations.md)
* [Logging](../../../java-sdk/current/howtos/collecting-information-and-logging.md)
* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client/)

Scala SDK

* [Start Using the SDK](../../../scala-sdk/current/hello-world/start-using-sdk.md)
* [Managing Connections](../../../scala-sdk/current/howtos/managing-connections.md)
* [CRUD Using SDKs](../../../scala-sdk/current/howtos/kv-operations.md)
* [Concurrent Document Mutations](../../../scala-sdk/current/howtos/concurrent-document-mutations.md)
* [Logging](../../../scala-sdk/current/howtos/collecting-information-and-logging.md)
* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/index.html)

C SDK

* [Start Using the SDK](../../../c-sdk/current/hello-world/start-using-sdk.md)
* [Managing Connections](../../../c-sdk/current/howtos/managing-connections.md)
* [CRUD Using SDKs](../../../c-sdk/current/howtos/kv-operations.md)
* [Concurrent Document Mutations](../../../c-sdk/current/howtos/concurrent-document-mutations.md)
* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client/)

Node.js SDK

* [Start Using the SDK](../../../nodejs-sdk/current/hello-world/start-using-sdk.md)
* [CRUD Using SDKs](../../../nodejs-sdk/current/howtos/kv-operations.md)
* [Concurrent Document Mutations](../../../nodejs-sdk/current/howtos/concurrent-document-mutations.md)
* [Logging](../../../nodejs-sdk/current/howtos/collecting-information-and-logging.md)
* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-node-client/)

NET SDK

* [Start Using the SDK](../../../dotnet-sdk/current/hello-world/start-using-sdk.md)
* [CRUD Using SDKs](../../../dotnet-sdk/current/howtos/kv-operations.md)
* [Concurrent Document Mutations](../../../dotnet-sdk/current/howtos/concurrent-document-mutations.md)
* [Logging](../../../dotnet-sdk/current/howtos/collecting-information-and-logging.md)
* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client/)

PHP SDK

* [Start Using the SDK](../../../php-sdk/current/hello-world/start-using-sdk.md)
* [CRUD Using SDKs](../../../php-sdk/current/howtos/kv-operations.md)
* [Concurrent Document Mutations](../../../php-sdk/current/howtos/concurrent-document-mutations.md)
* [Logging](../../../php-sdk/current/howtos/collecting-information-and-logging.md)
* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-php-client/namespaces/couchbase.html)

Python SDK

* [Start Using the SDK](../../../python-sdk/current/hello-world/start-using-sdk.md)
* [Managing Connections](../../../python-sdk/current/howtos/managing-connections.md)
* [CRUD Using SDKs](../../../python-sdk/current/howtos/kv-operations.md)
* [Concurrent Document Mutations](../../../python-sdk/current/howtos/concurrent-document-mutations.md)
* [Logging](../../../python-sdk/current/howtos/collecting-information-and-logging.md)
* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/)

Go SDK

* [Start Using the SDK](../../../go-sdk/current/hello-world/start-using-sdk.md)
* [Managing Connections](../../../go-sdk/current/howtos/managing-connections.md)
* [CRUD Using SDKs](../../../go-sdk/current/howtos/kv-operations.md)
* [Concurrent Document Mutations](../../../go-sdk/current/howtos/concurrent-document-mutations.md)
* [Logging](../../../go-sdk/current/howtos/collecting-information-and-logging.md)
* [API Reference](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc)

## Administration and Tools

Cluster Management

* [Overview](../manage/management-overview.md)
* [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md)
* [Manage Buckets](../manage/manage-buckets/bucket-management-overview.md)

Monitoring and Logging

* [Monitoring](../manage/monitor/monitor-intro.md)
* [Logging](../manage/manage-logging/manage-logging.md)
* [Settings](../manage/manage-settings/manage-settings.md)
* [Troubleshoot](../manage/troubleshoot/troubleshoot.md)

REST API and Tools

* [cbimport](../tools/cbimport.md)
* [cbexport](../tools/cbexport.md)
* [Couchbase CLI](../cli/cli-intro.md)
* [REST API Reference](../rest-api/rest-intro.md)

## 

Security

* [Security Overview](../learn/security/security-overview.md)
* [Authentication](../learn/security/authentication.md)
* [Manage Certificates](../manage/manage-security/manage-certificates.md)
* [Authorization](../learn/security/authorization-overview.md)
* [Manage Users, Groups, and Roles](../manage/manage-security/manage-users-and-roles.md)

Replication

* [Cross Data Center Replication(XDCR) Architecture](../learn/clusters-and-availability/replication-architecture.md)
* [XDCR Advanced Filtering](../learn/clusters-and-availability/xdcr-filtering.md)
* [XDCR Cloud Deployment](../learn/clusters-and-availability/xdcr-overview.md)
* [Manage XDCR](../manage/manage-xdcr/xdcr-management-overview.md)

Backup and Restore

* [Manage Backup and Restore](../manage/manage-backup-and-restore/manage-backup-and-restore.md)
* [cbbackupmgr Tutorial](../backup-restore/cbbackupmgr-tutorial.md)

## Quick Links

Project Docs

* [Release Notes](../release-notes/relnotes.md)
* [Couchbase Server Editions](editions.md)

Feedback

* [Contact Couchbase](contact-couchbase.md)
* [Contribute to the Documentation](../../../home/contribute/index.md)