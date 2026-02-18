---
title: Search Service Quick Start Guide
description: Following appropriate preparations, full text searches can be
  performed in a number of ways.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-quickstart-guide.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-quickstart-guide.html)

# Search Service Quick Start Guide

> Following appropriate preparations, full text searches can be performed in a number of ways. 

## [](#preparing-for-full-text-searches)Prerequisites

The user interface for Full Text Search is provided by the Couchbase Web Console.

* Ensure that Couchbase Server has the Search service appropriately enabled. The service must be enabled for a given node as part of that node’s initial configuration. Refer to Create a Cluster for information.
* You must have permission to log into the console, load sample data, create indexes, create search indexes, and perform searches. For information on Role-Based Access Control, see [Authorization](../learn/security/authorization-overview.md).
* The example(s) provided assume that you have can load or have loaded the `travel-sample` dataset. You will perform your Search operations on the data under this bucket. For instructions on how to load this sample dataset, see [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).
* The Couchbase Web Console by accessing `http://localhost:8091` or if remote `http://${CB_HOSTNAME}:8091` where **CB\_HOSTNAME** is an environment variable set to a FQDN or an IP address for a node on your Couchbase cluster.

## [](#quick-start-via-the-classic-editor)Quick Start via the Classic Editor

To quickly become familiarized with the Search service, try one of the step by step index creation (and query) examples against the `travel-sample` sample dataset:

* Collections

* Creating a **One Field Index** [via the UI](fts-creating-index-from-UI-classic-editor-onefield.md) (or [via the REST API](fts-creating-index-from-REST-onefield.md)), followed by a sample Search query.
* Creating a **Dynamic Index** [via the UI](fts-creating-index-from-UI-classic-editor-dynamic.md) (or [via the REST API](fts-creating-index-from-REST-dynamic.md)), followed by a sample Search query.
* Creating a **Geopoint Index** [via the UI](fts-creating-index-from-UI-classic-editor-geopoint.md) (or [via the REST API](fts-creating-index-from-REST-geopoint.md)), followed by a sample Search query.

Bucket Compatibility

Creating a **Legacy Index** [via the UI](fts-creating-index-from-UI-classic-editor-legacy.md) (or [via the REST API](fts-creating-index-from-REST-legacy.md)), followed by a sample Search query.

The above Legacy Index is used for compatibility after an upgrade from buckets to collections uses the old bucket style "**default \_mapping** which only works on the _default scope and \_default collection where buckets are upgraded into. The preferred method as of version 7.0 is shown in [Creating a Dynamic Index](fts-creating-index-from-UI-classic-editor-dynamic.md) above._ 

For a more detailed explanation of the available index creation, including index creation by means of the Couchbase REST API, refer to [Creating Search Indexes](fts-creating-indexes.md).

To install the `travel-sample` sample dataset, refer to [Install Sample Buckets with the UI ](../manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).

For a more detailed explanation of the available Query options, refer to [Searching from the UI](fts-searching-from-the-UI.md)

> [!NOTE]
> During index creation, in support of most query-types, you can select (or create) and use an _analyzer_. This is optional: if you do not specify an analyzer, a default analyzer is provided. Analyzers can be created by means of the Couchbase Web Console, during index creation, as described in [Creating Search Indexes](fts-creating-indexes.md). Their functionality and inner components are described in detail in [Understanding Analyzers](fts-index-analyzers.md).

## [](#performing-full-text-searches)Methods to Access the Search service

Search queries (Full Text, Geospatial, Numeric, and other) can be performed with:

* The Couchbase Web Console. This UI can also be used to create indexes and analyzers. Refer to [Searching from the UI](fts-searching-from-the-UI.md) for information.
* The Couchbase REST API. Refer to [Searching with the REST API](fts-searching-with-curl-http-requests.md#Searching-with-the-REST-API-%28cURL/HTTP%29) for information. Refer also to [Search API](../rest-api/rest-fts.md) for REST reference details.
* The Couchbase SDK. This supports several languages, and allows Search queries to be performed with each. Refer to the SDK’s [Java Search Overview](../../../java-sdk/current/concept-docs/full-text-search-overview.md) page for information. Note that the [Searching from the Java SDK](../../../java-sdk/current/howtos/full-text-searching-with-sdk.md) page for the _Java_ SDK provides an extensive code-example that demonstrates multiple options for performing searches.
* The SQL++ Search functions. These enable you to perform a full text search as part of a SQL++ query. Refer to [Search Functions](../n1ql/n1ql-language-reference/searchfun.md) for information.

## [](#establishing-demonstration-indexes)Accessing the Search service via the Java SDK

The Java SDK code-example provided in [Searching from the Java SDK](../../../java-sdk/current/howtos/full-text-searching-with-sdk.md) contains multiple demonstration calls — each featuring a different query-combination — and makes use of three different index-definitions, related to the `travel-sample` bucket: for the code example to run successfully, the three indexes must be appropriately pre-established. Instructions on how to use the Couchbase REST API to establish the definitions refer to [Index Creation with REST API](fts-creating-index-with-rest-api.md).