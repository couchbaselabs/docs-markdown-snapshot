---
title: maxConcurrentPartitionMovesPerNode
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-advance-settings-maxConcurrentPartitionMovesPerNode.adoc
  xref: xref:7.2@server:fts:fts-advance-settings-maxConcurrentPartitionMovesPerNode.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-advance-settings-maxConcurrentPartitionMovesPerNode.html)

# maxConcurrentPartitionMovesPerNode

The `maxConcurrentPartitionMovesPerNode` setting offers a way to speed up the rebalance operation to move partitions concurrently.

During the rebalance operations, FTS moves or builds partitions one at a time per node. It offers a way to speed up the rebalance operation to move partitions concurrently.

So, the way to speed up the rebalance operation is to enable the movement of partitions parallelly.

Setting the `maxConcurrentPartitionMovesPerNode` to **N** as a runtime cluster option can concurrently build the N number of partitions in parallel per node at a time and help in completing the rebalancing faster.

Setting `maxFeedsPerDCPAgent` to 1 with a sufficient FTS memory quota can help to maximize the rebalancing throughput.

## [](#example)Example

**Speed Up the Rebalance operation**:

* Set `maxConcurrentPartitionMovesPerNode` to any number, for example 10, to bring additional concurrency:  
curl -XPUT -H "Content-type:application/json" http://<username>:<password>@<ip>:8094/api/managerOptions \-d '{"maxConcurrentPartitionMovesPerNode": "10"}
* Set `maxConcurrentPartitionMovesPerNode` to N as runtime cluster option:  
curl -XPUT -H "Content-type:application/json" http://<username>:<password>@<ip>:8094/api/managerOptions \-d '{"maxConcurrentPartitionMovesPerNode": "N"}'
* Set `maxConcurrentPartitionMovesPerNode` to 1 for maximum concurrency:  
curl -XPUT -H "Content-type:application/json" http://<username>:<password>@<ip>:8094/api/managerOptions \-d '{"maxFeedsPerDCPAgent": "1"}'  
> [!NOTE]  
> Ensure that you have enough memory quota.