---
title: Manage Indexes
description: Indexes provided by the Index Service can be managed with Couchbase
  Web Console, with the CLI, and with the REST API.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/manage/pages/manage-indexes/manage-indexes.adoc
  xref: xref:7.2@server:manage:manage-indexes/manage-indexes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/manage/manage-indexes/manage-indexes.html)

# Manage Indexes

> Indexes provided by the Index Service can be managed with Couchbase Web Console, with the CLI, and with the REST API. 

## [](#defining-editing-and-managing-indexes)Defining, Editing, and Managing Indexes

Indexes provided by the _Index Service_ facilitate and enhance use of the _Query Service_; which reads information from and writes information to _documents_, provided by the _Data Service_. These indexes are administered by means of two facilities:

* The _SQL++_ language, which is provided by the Query Service as a means of querying data within documents; and of defining and editing indexes. See the [SQL++ Language Reference](../../n1ql/n1ql-language-reference/index.md) for information.
* _Couchbase Web Console_, which provides a user interface for the management of indexes.

This page describes how to use Couchbase Web Console to manage indexes. It also shows how to use the console's **Query Editor**, provided on the **Query** screen, to define and edit indexes by means of SQL++.

## [](#access-indexes)Access the Indexes Screen

The user interface for index management is provided on the **Indexes** screen. Access this by left-clicking on the tab in the left-hand navigation bar:

![indexesTab](../_images/manage-ui/indexesTab.png) 

An index list, showing a summary of all currently-defined indexes, is displayed in table format.

![indexesScreenFullyPrepared](../_images/manage-ui/indexesScreenFullyPrepared.png) 

The **Bucket & Scope** fields allow selection of a bucket from those defined on the cluster; and of a scope from those defined within the bucket. Left-click on the left-hand field, to display a pull-down menu of available buckets:

![buckets pulldown menu](../_images/manage-indexes/buckets-pulldown-menu.png) 

Likewise, left-click on the right-hand field, to display a pull-down menu of scopes within the selected bucket:

![scopes pulldown menu](../_images/manage-indexes/scopes-pulldown-menu.png) 

Each time a selection is made, the list of indexes in the lower panel is redisplayed; so as to show the indexes that are defined on data within the selected scope and bucket.

Note that towards the right, an additional control provides a pull-down menu whereby indexes can be viewed either for all Index-Service nodes on the cluster, or by node. Additionally, an interactive field is provided, to allow the displayed content to be filtered; by entering either all or part of an index-name.

## [](#index-summary)Index Summary

The index list displays the following information about each index:

* **index name**. The name of the index. There may also be one or more indicators after the index name, giving further information:  
![index indicators](../_images/manage-indexes/index-indicators.png)  

  * `partitioned` indicates that the index is _partitioned_. An overview of partitioning is provided in [Index Partitioning](../../learn/services-and-indexes/indexes/index-replication.md#index-partitioning). Examples of creating partitioned indexes are provided in [Partition Keys](../../n1ql/n1ql-language-reference/index-partitioning.md#partition-keys).
  * `replica _n_` indicates that this is an _index replica_, where `_n_` is the replica ID. An overview of index replication, and examples of creating index replicas, are provided in [Index Replication](../../learn/services-and-indexes/indexes/index-replication.md#index-replication).
  * `stale` indicates that the node on which the index or partition is stored is not available.
* **requests/sec**. The number of requests per second.
* **resident ratio**. The percentage of the data held in memory.
* **items**. The number of items currently indexed.
* **data size**. The size of indexable data that is maintained for the index or replica.
* **keyspace**. The keyspace for which the index or replica was created.
* **status**. The current state of the Index Service on the node on which this index is stored. The state can be expressed as **ready**, **pause**, **warmup**, or **n mutations remaining** (where **n** is an integer).  
The color of the left margin of the index row also reflects the current state of the index. For example, the color is green when the index is **ready**; and orange when the index is in **warmup**.  
![index margins](../_images/manage-indexes/index-margins.png)

## [](#expand-index)Index Administration

To administer an index, left-click on a specific index row in the indexes list, to expand the row. (Subsequently, whenever appropriate, left-click on the row again, to collapse it.) When the row is expanded, it appears as follows:

![index row expanded](../_images/manage-indexes/index-row-expanded.png) 

The following information is thus provided:

* **Definition**. The SQL++ statement used to define the index.
* **Storage Mode**. The [storage mode](../../learn/services-and-indexes/indexes/storage-modes.md) used by the Index Service on the node on which this index is stored.
* **Nodes**. (Only displayed for partitioned indexes.) The nodes on which the index partitions are stored, and the number of partitions stored on each node.

In addition, when the index row is expanded, the **Index Stats** control is displayed, along with the **Open in Workbench** and **Drop** buttons. These controls are described below.

### [](#index-stats)Show the Index Statistics

To see statistics for the index, left-click on the **Index Stats** control in the expanded index row. The panel expands vertically, and provides the following display of interactive charts:

![index stats display](../_images/manage-indexes/index-stats-display.png) 

For more information on these charts, see [Index Statistics](../monitor/monitoring-indexes.md#index-stats).

### [](#edit-index)Open the Index in the Query Workbench

If an index is opened in the _Query Workbench_, its definition can be inspected and modified.

Proceed as follows:

1. From the **Indexes** screen, left-click the **Open in Workbench** button, in the expanded index row. The index definition is displayed in the Query Workbench:  
![indexInQueryWorkbench](../_images/manage-indexes/indexInQueryWorkbench.png)
2. Modify the SQL++ index-definition, as required. (Note that you cannot change the definition of the existing index, but you can create a new index with the modified definition.)

Immediately beneath the **Query Editor**, four buttons are displayed. These can be used to test queries, and to determine how to design corresponding indexes; so as to maximize query-performance. The buttons are as follows.

#### [](#execute)Execute

When left-clicked on, this executes the query that has been typed into the **Query Editor**. For example, type the following query into the **Query Editor**: `` SELECT icao FROM `travel-sample` WHERE name = "SeaPort Airlines"; ``. This selects every `icao` key-value pair from the bucket `travel-sample`, where the host document also contains a `name` value that is `SeaPort Airlines`:

![queryEditorWithSelectQuery](../_images/manage-ui/queryEditorWithSelectQuery.png) 

Left-click on the **Execute** button.

![leftClickOnExecuteButton](../_images/manage-ui/leftClickOnExecuteButton.png) 

Couchbase Web Console now provides feedback on the ongoing execution of the query, to the right of the buttons. When query-execution has concluded, the results are duly displayed:

![resultsOfqueryExecution](../_images/manage-indexes/resultsOfqueryExecution.png) 

Note also that the default appearance of the **Query** screen includes, at the upper right, a button labeled **query context**:

![queryContextButton](../_images/manage-indexes/queryContextButton.png) 

Left-click on the control at the right-hand side of the button, to reveal its pulldown menu. This menu contains an entry for each bucket defined on the cluster:

![bucketsButton](../_images/manage-indexes/bucketsButton.png) 

Once a bucket has been selected, a further button (with pulldown-menu control) appears to the right, allowing selection of a scope within the selected bucket:

![scopesButton](../_images/manage-indexes/scopesButton.png) 

Once a scope — for example, `inventory` — has been selected, queries can be entered into the **Query Editor** panel without explicit specification of bucket or scope being required: the bucket and scope for the query will be inferred from the pulldown-menu selections that have been made. For example, the following expression performs a query on the documents in the `airline` collection; which itself resides within `inventory`, within `travel-sample`:

![queryEditorWithShorterSelectQuery](../_images/manage-indexes/queryEditorWithShorterSelectQuery.png) 

Note that buckets and scopes other than those currently selected by means of the pulldown menus can still be explicitly specified within the **Query Editor**, if required.

#### [](#explain)Explain

When left-clicked on, this provides an explanation of how query-execution proceeded:

![leftClickOnExplainButton](../_images/manage-ui/leftClickOnExplainButton.png) 

The explanation is now displayed in the **Query Results** panel:

![queryExplanation](../_images/manage-ui/queryExplanation.png) 

This indicates the bucket and primary index scan that have been used in the query; as well as the filter applied, and the number of terms returned.

#### [](#index-advisor)Index Advisor

When left-clicked on, this displays advice as to what index or indexes might be created, in order to improve the future performance of the query:

![leftClickOnAdviseButton](../_images/manage-indexes/leftClickOnAdviseButton.png) 

Advice is duly displayed in the **Query Results** panel:

![queryAdviceDisplay2](../_images/manage-indexes/queryAdviceDisplay2.png) 

In this instance, the advice consists of two options; which are, respectively, the creation of a _covering_ index, and the creation of a regular index. To create a covering index, left-click on the **Create and Build Covering Index** button:

The following notification is now displayed:

![indexCreateWarning](../_images/manage-ui/indexCreateWarning.png) 

Left-click on **Continue**. When index-creation is completed, the following success-message appears on the **Query** screen:

![createIndexSuccessMessage](../_images/manage-ui/createIndexSuccessMessage.png) 

#### [](#run-as-tx)Run as TX

The **Run as TX** button allows the specified query to be run transactionally, across multiple indexes. For information on transactions, see [Transactions](../../learn/data/transactions.md).

Left-click on the **Run as TX** button, and the query is run as a transaction. When the transaction is complete, status is displayed as follows:

![transactionSuccessDisplay](../_images/manage-indexes/transactionSuccessDisplay.png) 

### [](#index-definition-support-in-community-edition)Index-Definition Support in Community Edition

Note that in Couchbase Server _Community_ Edition, index-definition support is provided in a slightly different way. The area immediately below the **Query Editor** appears as follows:

![ceIndexAdvisorLink](../_images/manage-ui/ceIndexAdvisorLink.png) 

The [External Query Advisor](https://index-advisor.couchbase.com/indexadvisor/#1) link takes the user to an external web-site, where the **Query Advisor** can be accessed and used.

### [](#drop-index)Drop the Index

To drop the index from the bucket:

1. Left-click the **Drop** button in the expanded index row.  
A pop-up message appears, asking if you are sure you want to drop the index.  
![drop index](../_images/manage-indexes/drop-index.png)
2. Left-click on the **Drop Index** button, to drop the index. Alternatively, left-click on the **Cancel** button, to cancel.

Note that you can also drop an index by means of the SQL++ [DROP INDEX](../../n1ql/n1ql-language-reference/dropindex.md) and [DROP PRIMARY INDEX](../../n1ql/n1ql-language-reference/dropprimaryindex.md) commands.

## [](#index-summary-stats)Index Summary Statistics

Summary statistics for the Index Service are displayed in the footer of the Indexes screen.

![service stats](../_images/manage-indexes/service-stats.png) 

For details of the index summary statistics, refer to [Index Service Statistics](../monitor/monitoring-indexes.md#service-stats).

## [](#cli)Manage Indexes with the CLI

You can manage some Index-Service settings using the CLI. Refer to [Index Storage Settings via CLI](../manage-settings/general-settings.md#index-storage-settings-via-cli).

Note that there is no CLI support for the administration of specific indexes. However, you can get index information from the system catalog. Refer to [Querying Indexes](../../n1ql/n1ql-intro/sysinfo.md#querying-indexes).

You can also edit or remove indexes using SQL++. Refer to [SQL++ Language Reference](../../n1ql/n1ql-language-reference/index.md) for more details.

## [](#rest-api)Manage Indexes with the REST API

You can manage some Index-Service settings using the REST API. Refer to [Index Settings via REST](../manage-settings/general-settings.md#index-settings-via-rest).

Note that there is no REST API support for the administration of specific indexes.

## [](#related-links)See Also

Information on index statistics is provided in [Monitor Indexes](../monitor/monitoring-indexes.md).