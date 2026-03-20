---
title: Key-Value Operations
description: How to perform CRUD key-value operations in Couchbase.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/kv-operations.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:guides:kv-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/guides/kv-operations.html)

# Key-Value Operations

> How to perform CRUD key-value operations in Couchbase.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

Every item in a database goes through the basic _CRUD_ cycle, which is typical of an application’s use of data. CRUD stands for create, read, update, and delete:

* **C**reate: when data is first inserted into the cluster
* **R**ead: when an application retrieves the data
* **U**pdate: when data is modified to reflect a change in the state represented by the data
* **D**elete: when the data is no longer needed

The [Key-Value (KV) or Data Service](../learn/services-and-indexes/services/data-service.md) offers Couchbase clients the fastest and simplest way to create, retrieve or mutate data where the key is known.

## [](#before-you-begin)Before You Begin

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset.

### [](#couchbase-clients)Couchbase Clients

Clients access data by connecting to a Couchbase cluster over the network. The most common type of client is a Couchbase SDK, which is a full programmatic API that enables applications to take the best advantage of Couchbase. This developer guide focuses on the most commonly-used SDKs, but full explanations and reference documentation for all SDKs is available.

The command line clients also provide a quick and streamlined interface for simple access and are suitable if you just want to access an item without writing any code.

> [!NOTE]
> With some editions, the command line clients are provided as part of the installation of Couchbase Server. Assuming a default installation, you can find them in the following location, depending on your operating system:
> 
> | Linux   | /opt/couchbase/bin                                                       |
> | ------- | ------------------------------------------------------------------------ |
> | Windows | C:\\Program Files\\Couchbase\\Server\\bin                                |
> | macOS   | /Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin |
> 
> If the command line client is not provided with your installation of Couchbase Server, you must install the C SDK in order to use the command line clients.

Read the following for further information about the clients available:

* [Command Line Clients](../../../c-sdk/current/hello-world/cbc.md)
* [SDK Clients](#home::sdk.adoc)

It is also possible to access document data via the Couchbase Server UI.

![The Documents UI can be used to perform crud operations](_images/documents-kv-operations.png) 

Figure 1\. Document Data Access

For further details, refer to [Examine Your Bucket and Its Documents](../getting-started/look-at-the-results.md#examine-your-bucket-and-its-documents).

## [](#next-steps)Next Steps

Key-Value Operations guides:

* [Creating Data](creating-data.md)
* [Reading Data](reading-data.md)
* [Updating Data](updating-data.md)
* [Deleting Data](deleting-data.md)
* [Bulk Operations](bulk-operations.md)