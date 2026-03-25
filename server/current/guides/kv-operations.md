---
title: Work with Documents
description: How to perform CRUD key-value operations in Couchbase.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/guides/pages/kv-operations.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:server:guides:kv-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/guides/kv-operations.html)

# Work with Documents

> How to perform CRUD key-value operations in Couchbase. 

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
* [SDK Clients](../../../home/sdk.md)

It is also possible to access document data via the Couchbase Server UI.

## [](#next-steps)Next Steps

Key-Value Operations guides:

* [Manage Documents in the Couchbase Web Console](../manage/manage-documents/manage-documents.md)
* [Create Documents](creating-data.md)
* [Read Documents](reading-data.md)
* [Update Documents](updating-data.md)
* [Delete Documents](deleting-data.md)
* [Work with Documents in Bulk](bulk-operations.md)