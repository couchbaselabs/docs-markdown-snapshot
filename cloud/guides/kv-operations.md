---
title: Work with Documents
description: How to perform CRUD key-value operations in Couchbase.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/kv-operations.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:guides:kv-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/guides/kv-operations.html)

# Work with Documents

> How to perform CRUD key-value operations in Couchbase. 

## [](#introduction)Introduction

Every item in a database goes through the basic CRUD cycle, which is typical of an application’s use of data. CRUD stands for create, read, update, and delete:

* **C**reate: when data is first inserted into the cluster
* **R**ead: when an application retrieves the data
* **U**pdate: when data is modified to reflect a change in the state represented by the data
* **D**elete: when the data is no longer needed

The [Key-Value (KV) or Data Service](../clusters/data-service/data-service.md) offers Couchbase clients the fastest and simplest way to create, retrieve or mutate data where the key is known.

## [](#before-you-begin)Before You Begin

If you want to try out the examples in this section, follow the instructions given in [Create an Account and Deploy Your Free Tier Operational Cluster](../get-started/create-account.md) to create a free account, deploy a cluster, and load a sample dataset.

### [](#couchbase-clients)Couchbase Clients

Clients access data by connecting to a Couchbase cluster over the network. The most common type of client is a Couchbase SDK, which is a full programmatic API that enables applications to take the best advantage of Couchbase. This developer guide focuses on the most commonly-used SDKs, but full explanations and reference documentation for all SDKs is available.

The Couchbase Shell (cbsh) also provides a quick and streamlined interface for simple access, and is suitable if you just want to access an item without writing any code. Note that the Couchbase Shell is maintained by Couchbase, but it is not covered by support.

Read the following for further information about the clients available:

* [Couchbase Shell (cbsh)](https://couchbase.sh/docs/)
* [SDK Clients](#home::sdk.adoc)

It is also possible to access document data via the Couchbase Capella UI.

## [](#next-steps)Next Steps

Key-Value Operations guides:

* [Manage Documents with the Capella UI](../clusters/data-service/manage-documents.md)
* [Create Documents](creating-data.md)
* [Read Documents](reading-data.md)
* [Update Documents](updating-data.md)
* [Delete Documents](deleting-data.md)
* [Work with Documents in Bulk](bulk-operations.md)