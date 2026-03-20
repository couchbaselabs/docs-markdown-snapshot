---
title: Classic Editor Examples
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-creating-index-from-UI-classic-editor.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-creating-index-from-UI-classic-editor.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-creating-index-from-UI-classic-editor.html)

# Classic Editor Examples

> The classic editor is the most advanced interface where users can directly configure the index mapping with all of capabilities in Search. 

## [](#prerequisites)Prerequisites

The user interface for Full Text Search is provided by the Couchbase Web Console.

* Ensure that Couchbase Server has the Search service appropriately enabled. The service must be enabled for a given node as part of that node’s initial configuration. Refer to Create a Cluster for information.
* You must have permission to log into the console, load sample data, create indexes, create search indexes, and perform searches. For information on Role-Based Access Control, see [Authorization](../learn/security/authorization-overview.md).
* The example(s) provided assume that you have can load or have loaded the `travel-sample` dataset. You will perform your Search operations on the data under this bucket. For instructions on how to load this sample dataset, see [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).
* The Couchbase Web Console by accessing `http://localhost:8091` or if remote `http://${CB_HOSTNAME}:8091` where **CB\_HOSTNAME** is an environment variable set to a FQDN or an IP address for a node on your Couchbase cluster.

## [](#quickstart-via-the-classic-editor)Quickstart via the Classic Editor

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