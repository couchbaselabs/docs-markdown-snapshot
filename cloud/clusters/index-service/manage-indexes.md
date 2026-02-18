---
title: Manage Indexes
description: You can perform some index management tasks using the Couchbase Capella UI.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/index-service/manage-indexes.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/clusters/index-service/manage-indexes.html)

# Manage Indexes

> You can perform some index management tasks using the Couchbase Capella UI. 

## [](#accessing-indexes-in-the-capella-ui)Accessing Indexes in the Capella UI

> [!IMPORTANT]
> Permissions Required
> 
> To access indexes in the Couchbase Capella UI, you need the following permissions:
> 
> You need the [Project Owner](../../projects/project-roles.md#project-owner-role) or [Data Writer](../../projects/project-roles.md#project-cluster-data-reader-writer) role for the project containing the cluster.

To view the Indexes page for a cluster that’s running the [Index Service](../../indexes/indexing-overview.md):

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with indexes.
3. Go to **Data Tools** **Indexes**.

### [](#index-summary)Index Summary

The Indexes page summarizes all indexes on the cluster in a tabular format. It includes sortable columns and a row for each index.

Each index has the following information:

| Statistic | Description                                                                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name      | The name of the index or replica.                                                                                                                 |
| Reqs/sec  | The number of requests per second.                                                                                                                |
| Resident  | The percentage of the data held in memory.                                                                                                        |
| Items     | The number of items indexed.                                                                                                                      |
| Size      | The size of indexable data that’s maintained for the index or replica.                                                                            |
| Status    | The current state of the Index Service on the node where this index is stored. The possible statuses include **ready**, **pause**, or **warmup**. |
| Last Scan | The latest scan time.                                                                                                                             |
| Keyspace  | The keyspace for which the index or replica was created.                                                                                          |

## [](#create-an-index)Create an Index

Indexes are created using the SQL++ query language. The [Query tab](../query-service/query-workbench.md) can [create](../../n1ql/n1ql-language-reference/createindex.md), [modify](../../n1ql/n1ql-language-reference/alterindex.md), and [drop](../../n1ql/n1ql-language-reference/dropindex.md) indexes using SQL++ statements.

## [](#inspect-an-index)Inspect an Index

The **Index Definition** section displays the SQL++ statement used to define the index. Directly below it is a snippet of the information from the [index list](#index-summary).

To view the details of an index: Select its name on the Indexes page.

### [](#open-the-index-definition)Open the Index Definition

Use the SQL++ query language to define and edit indexes. Using the query editor, you can modify the index definition as required to create a new index. You can’t change the definition of the existing index. You can create a new index with the modified definition and then drop the old index.

To open the index definition in the [Query tab](../query-service/query-workbench.md): Click **Open definition in Query Editor**.

The index definition is added to the query editor.

### [](#view-index-performance)View Index Performance

The **Bucket’s Index Performance** section displays statistics for the Index Service or the selected bucket that the current index is defined for.

The following statistics are available:

| Statistic                  | Description                                                                                                                                                                                 | Applies To       |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Index Service RAM Quota    | The buffer cache size for the Index Service across all nodes.                                                                                                                               | Index Service.   |
| Index Service RAM Percent  | The amount of memory used by the Index Service, as a percentage of the amount of memory available to the Index Service.                                                                     | Index Service.   |
| Total Scan Rate            | The number of index items scanned by the Index Service per second for the selected bucket.                                                                                                  | Selected bucket. |
| RAM Used/Remaining         | The amount of memory used by the Index Service, and the remaining amount of memory available to the Index Service.                                                                          | Index Service.   |
| Index Fragmentation        | The percentage fragmentation of all indexes for the selected bucket. This indicates the percentage of disk space consumed by the indexes, but not utilized for items stored in the indexes. | Selected bucket. |
| Scan Rate (over 5 minutes) | The number of rows or index entries returned by a scan on this index over the last five minutes.                                                                                            | Index Service.   |
| Index Disk Size            | The total disk file size consumed by all indexes for the selected bucket.                                                                                                                   | Selected bucket. |
| Index Data Size            | The actual data size consumed by all indexes for the selected bucket.                                                                                                                       | Selected bucket. |

## [](#drop-an-index)Drop an Index

> [!TIP]
> You can also drop an index using the SQL++ [DROP INDEX](../../n1ql/n1ql-language-reference/dropindex.md) or [DROP PRIMARY INDEX](../../n1ql/n1ql-language-reference/dropprimaryindex.md) commands.

To drop an index:

1. On the Indexes page, find the index.
2. Click the Trash icon  at the end of its row.
3. When prompted to confirm the deletion, type "delete" and click **Delete Index** to drop the index.