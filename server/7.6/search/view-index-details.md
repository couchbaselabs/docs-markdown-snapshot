---
title: View Index Details with the Web Console
description: Use the Index Details page in the Couchbase Server Web Console to
  view partition layouts and query execution times.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/view-index-details.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:search:view-index-details.adoc[]
---

[View original HTML](/server/7.6/search/view-index-details.html)

# View Index Details with the Web Console

> Use the Index Details page in the Couchbase Server Web Console to view partition layouts and query execution times. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* You have created a Search index.  
For more information about how to create a Search index, see [Create a Search Index](create-search-indexes.md).
* Your user account has the **Search Admin** role for the bucket where you created your Search index.
* You have logged in to the Couchbase Server Web Console.

## [](#view-the-index-details-page)View the Index Details Page

To view the Index Details page for a Search index from the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the name of the index you want to view.
3. Click **Index details** (![The Index Details button, which is a hamburger menu with 3 bars.](_images/index-details-button.png)).

### [](#partition-layout-tab)Partition Layout Tab

Use the **Partition Layout** tab to view the location of your Search index partitions inside your Couchbase cluster:

| Property        | Description                                                                                                                                                                                                                                                                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Index Partition | The name of the specific Search index partition.                                                                                                                                                                                                                                                                                                                |
| vBuckets        | For each Search index partition, the specific [vBucket](../../current/learn/buckets-memory-and-storage/vbuckets.md) or vBuckets that contain the partition.                                                                                                                                                                                                     |
| Group           | The specific server group, IP address, and port for the Search index partition. The Partition Layout tab marks the active or primary partition for the Search index with a P. Any replications of the Search index are marked with an R. If the user has read and write permissions for the partition, the Partition Layout tab marks the partition with an rw. |

### [](#query-monitor-tab)Query Monitor Tab

Use the **Query Monitor** tab to view active queries that meet or exceed a specified execution time, and pause those queries:

* To pause all active queries, click **Pause**.
* In the **Longer than** box, select or enter a time value to filter your active queries.  
You can enter a value in milliseconds (`ms`), seconds (`s`), or minutes (`m`).

## [](#next-steps)Next Steps

To edit your Search index configuration, see [Customize a Search Index with the Web Console](customize-index.md).

To run a search with your Search index, see [Run a Search With a Search Index](run-searches.md).