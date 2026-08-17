---
title: Quick Editor and Example
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-creating-index-from-UI-quick-editor.adoc
  xref: xref:7.2@server:fts:fts-creating-index-from-UI-quick-editor.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-creating-index-from-UI-quick-editor.html)

# Quick Editor and Example

> The Quick Editor allows a visual inerface select fields from collections to easily quickly build near optimal indexes. 

## [](#prerequisites)Prerequisites

The user interface for Full Text Search is provided by the Couchbase Web Console.

* Ensure that Couchbase Server has the Search service appropriately enabled. The service must be enabled for a given node as part of that node's initial configuration. Refer to Create a Cluster for information.
* You must have permission to log into the console, load sample data, create indexes, create search indexes, and perform searches. For information on Role-Based Access Control, see [Authorization](../learn/security/authorization-overview.md).
* The example(s) provided assume that you have can load or have loaded the `travel-sample` dataset. You will perform your Search operations on the data under this bucket. For instructions on how to load this sample dataset, see [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).
* The Couchbase Web Console by accessing `http://localhost:8091` or if remote `http://${CB_HOSTNAME}:8091` where **CB\_HOSTNAME** is an environment variable set to a FQDN or an IP address for a node on your Couchbase cluster.

## [](#creating-a-search-index-via-the-quick-editor)Creating a Search Index via the Quick editor

Quick Editor is a newer interface in Search where you can quickly select the bucket, scope, and collection and choose the index fields from the searched documents.

Due to this, the search query performance will be optimized as it has to handle fewer fields, increasing the query latency.

To access the Full Text Search screen, left-click on the **Search** tab in the navigation bar on the left-hand side:

![fts select search tab](_images/fts-select-search-tab.png) 

The Full Text Search screen now appears as follows:

![fts search page](_images/fts-search-page.png) 

To quick edit an index, left-click on the **Quick Edit** button towards the right-hand side on the Full Text Indexes panel.

The console contains areas for displaying indexes and aliases: but both are empty since none has yet been created.

The Quick Edit screen appears:

![fts quick edit screen](_images/fts-quick-edit-screen.png) 

Quick Edit allows you to modify and delete the configured mapped fields with the same index. To delete the mapped fields, select the field from the Mapped Fields grid and click Delete.

To map the new fields, select the field from the JSON format document, change the configuration and click Add.

![fts quick edit add index](_images/fts-quick-edit-add-index.png) 

To modify the mapped fields, select the field from the Mapped Fields, change the configuration and click Update.

![fts quick edit update index](_images/fts-quick-edit-update-index.png) 

To save your changes in the quick index, left-click on the **Update Index** button near the bottom of the screen.

## [](#quick-index)Quick Index

To create a quick index, left-click on the **QUICK INDEX** button, towards the right-hand side:

The QUICK INDEX screen appears:

![fts quick index screen](_images/fts-quick-index-screen.png) 

To define a basic index on which Full Text Search can be performed, begin by entering a unique name for the index into the Index Name field, on the upper-left: for example, travel-sample-index. (Note that only alphanumeric characters, hyphens, and underscores are allowed for index names. Note also that the first character of the name must be an alphabetic character.) Then, use the pull-down menu provided for the Keyspace field, at the upper-right, to specify as follows:

bucket: `travel-sample`

scope: `inventory`

collection: `hotel`

![fts quick index name and bucket](_images/fts-quick-index-name-and-bucket.png) 

The user can continue to randomly pick documents until they find a document of their intended type/schema. It is also possible to have multi-schema documents within a collection.

![fts quick index json](_images/fts-quick-index-json.png) 

Select the required field from the document, which is needed to be mapped to this index. Once the field is selected, the configuration panel is displayed on the right.

![fts quick index json configuration](_images/fts-quick-index-json-configuration.png) 

Select the related type of the field from the **Type** dropdown.

Select **Index this field as an identifier** to index the identifier values precisely without any transformation; for this case, language selection is disabled.

After that, select the required language for the chosen field.

Additionally, select from the following configuration options corresponding to the selected language:

* **Include in search results**: Select this option to include the field in the search result.
* **Support highlighting**: Select this option to highlight the matched field. For this option, you must select the **Include in search result** option.
* **Support phrase matching**: Select this option to match the phrases in the index.
* **Support sorting and faceting**: Select this option to allow sorting and faceting the index.

> [!NOTE]
> Selecting configuration options requires additional storage and makes the index size larger.

## [](#document-refreshreselection-option)Document Refresh/Reselection option

The 'Refresh' option will randomly select a document from the given Keyspace (bucket.scope.collection).

![fts quick index refresh](_images/fts-quick-index-refresh.png) 

Include In search results, Support phrase matching, and Support sorting and faceting. Searchable As field allows you to modify searchable input for the selected field.

![fts quick index searchable input](_images/fts-quick-index-searchable-input.png) 

Once the configuration is completed for the selected fields, click Add. Mapped fields will display the updated columns.

![fts quick index json mapping](_images/fts-quick-index-json-mapping.png) 

This is all you need to specify in order to create a basic index for test and development. No further configuration is required.

Note, however, that such default indexing is not recommended for production environments since it creates indexes that may be unnecessarily large, and therefore insufficiently performant. To review the wide range of available options for creating indexes appropriate for production environments, see Creating Indexes.

To save your index,

Left-click on the **Create Index** button near the bottom of the screen:

At this point, you are returned to the Full Text Search screen. A row now appears, in the Full Text Indexes panel, for the quick index you have created. When left-clicked on, the row opens as follows:

![fts new quick index progress](_images/fts-new-quick-index-progress.png) 

> [!NOTE]
> The percentage figure appears under the indexing progress column, and is incremented in correspondence with the build-progress of the index. When 100% is reached, the index build is said to be complete. Search queries will, however, be allowed as soon as the index is created, meaning partial results can be expected until the index build is complete.

Once the new index has been built, it supports Full Text Searches performed by all available means: the Console UI, the Couchbase REST API, and the Couchbase SDK.

> [!NOTE]
> If one or more of the nodes in the cluster running data service go down and/or are failed over, indexing progress may show a value > 100%.