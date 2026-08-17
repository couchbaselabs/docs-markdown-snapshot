---
title: Managing Enterprise Analytics Collections
description: This page describes how to manage collections with the Analytics Workbench.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sources/pages/manage-collections.adoc
  xref: xref:2.0@enterprise-analytics:sources:manage-collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/sources/manage-collections.html)

# Managing Enterprise Analytics Collections

The Analytics Workbench enables you to create, edit, drop collections, and connect or disconnect local links and remote links.

Collections are displayed in the insights sidebar of the Analytics Workbench. Each collection is associated with a specific database and scope chosen at the time of its creation.

* To create a remote link and associated collection, see [Stream Data from Remote Sources](manage-remote.md)
* To create an external link and associated collection, see [Set Up an External Data Source](manage-external.md).

## [](#viewing-collection-summaries)Viewing Collection Summaries

You can view a summary of a collection in the insights sidebar.

To display a summary of a collection, click the collection name in the insights sidebar, or click the arrow before the collection name.

The collection summary appears under the collection name, showing the name of the keyspace which is the data source for this collection, and, if applicable, the expression which filters the documents in the keyspace.

If you have created any indexes on this collection, the index names and definitions are shown under the collection summary.

To hide the summary of a collection, click the collection name in the insights sidebar again, or click the arrow before the collection name.

When data is being ingested, an indicator below each collection shows the percentage of mutations that need to be synchronized to that collection. If the indicator is not displayed, then the collection is up-to-date.

## [](#deleting-a-collection)Deleting a Collection

1. In the UI, select the **Workbench** tab and browse to the collection you want to delete.
2. Click the name of the collection, and click **drop collection**.  
The **Warning** dialog is displayed.
3. Choose **OK** to delete the link.

You can also delete a collection using the DROP ANALYTICS COLLECTION statement. For more information about deleting a collection, see [Drop Statements](#5%5Fddl.adoc#Drop%5Fstatements).

## [](#view-metadata-for-a-collection)View Metadata for a Collection

Each time you add a collection, Enterprise Analytics records its metadata in the `System.Metadata.Dataset` collection. To view metadata for a collection, you query this system collection. See [Querying Metadata](#5%5Fddl%5Fmetadata.adoc).

Important: Enterprise Analytics supports both column and row storage formats. By default, the column format is used, with a maximum of 4000 unique columns per collection. When ingesting JSON documents, each unique leaf node is treated as a column. For example: For example: { "a": { "b": \[1, 2\], "c": "value", "d": \[ { "x": 1, "y": 2 }, { "x": 3, "y": 4 } \] } } This document contributes 4 columns: - a.b: \[1, 2\] → 1 column - a.c: "value" → 1 column - a.d: \[{ "x": 1, "y": 2 }, { "x": 3, "y": 4 }\] → 2 columns (a.d.x and a.d.y)

Additional documents or array elements with the same structure do not increase the column count. Exceeding 4000 columns can impact performance and resource usage. Avoid naming fields dynamically (such as using timestamps as field names), as this can increase the column count.

Enterprise Analytics supports both column and row storage formats. By default, the column format is used, with a maximum of 4000 unique columns per collection.

When ingesting JSON documents, each unique leaf node is treated as a column. For example: