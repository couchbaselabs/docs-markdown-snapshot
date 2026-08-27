---
title: durability-monitor
description: Provides durability statistics in relation to vBuckets.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cli/pages/cbstats/cbstats-durability-monitor.adoc
  xref: xref:7.2@server:cli:cbstats/cbstats-durability-monitor.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/cli/cbstats/cbstats-durability-monitor.html)

# durability-monitor

> Provides durability statistics in relation to vBuckets. 

## [](#syntax)Syntax

Request syntax:

cbstats host:11210 [common options] durability-monitor vbid

## [](#description)Description

This command provides durability statistics for the specified vBucket. Note that the vBucket ID _must_ be specified.

In the displayed output, the identifier for each durability statistic begins with the string `vb_`, followed by the vBucket ID and a colon. For example, for vBucket 1023, the identifier for the `high_prepared_seqno` statistic is `vb_1023:high_prepared_seqno`.

For an overview of durability in Couchbase Server, see [Durability](../../learn/data/durability.md).

__Table 1\. Durability Monitor Statistics__
| Name                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| high\_prepared\_seqno                                                 | The highest sequence number among the prepared durable writes for the vBucket. _Prepared_ durable writes are those in progress, and therefore not yet committed or aborted. The _highest_ sequence number is that of the durable write that has most recently met its durability requirements on the node for the vBucket. The durability requirements depend on the durability level specified for the write. Provided for both active and replica vBuckets. |
| last\_aborted\_seqno                                                  | The sequence number of the last aborted durable write for the vBucket. Provided for active vBuckets only.                                                                                                                                                                                                                                                                                                                                                     |
| last\_committed\_seqno                                                | The sequence number of the last committed durable write for the vBucket. Provided for active vBuckets only.                                                                                                                                                                                                                                                                                                                                                   |
| high\_completed\_seqno                                                | The highest sequence number among the completed durable writes for the vBucket. _Completed_ includes both _aborted_ and _committed_. Provided for replica vBuckets only.                                                                                                                                                                                                                                                                                      |
| last\_tracked\_seqno                                                  | The sequence number of the last durable write to be tracked for the vBucket. Provided for active vBuckets only.                                                                                                                                                                                                                                                                                                                                               |
| num\_tracked                                                          | The number of durable writes currently being tracked for the vBucket. Provided for active vBuckets only.                                                                                                                                                                                                                                                                                                                                                      |
| replication\_chain\_First:ns\_1@<node-ip-address>:last\_ack\_seqno    | The sequence number of the last prepared durable write that the stated node has acknowledged to the active node. The replication\_chain\_Second statistic may also appear, during a topology change, such as rebalance. Provided for active vBuckets only.                                                                                                                                                                                                    |
| replication\_chain\_First:ns\_1@<node-ip-address>:last\_write\_seqno: | The sequence number of the last-written durable write that the stated node has acknowledged to the active node. The replication\_chain\_Second statistic may also appear, during a topology change, such as rebalance. Provided for active vBuckets only.                                                                                                                                                                                                     |
| state                                                                 | The state of the vBucket, which can be either active or replica. Provided for both active and replica vBuckets.                                                                                                                                                                                                                                                                                                                                               |

For common options, see [cbstats](../cbstats-intro.md).

## [](#examples)Examples

The two commands shown below provide output for an _active_ and a _replica_ vBucket, respectively.

/opt/couchbase/bin/cbstats localhost:11210 -u Administrator -p password \
durability-monitor -b travel-sample 112
vb_112:high_prepared_seqno:                                          0
vb_112:last_aborted_seqno:                                           0
vb_112:last_committed_seqno:                                         0
vb_112:last_tracked_seqno:                                           0
vb_112:num_tracked:                                                  0
vb_112:replication_chain_First:ns_1@10.143.192.101:last_ack_seqno:   0
vb_112:replication_chain_First:ns_1@10.143.192.101:last_write_seqno: 0
vb_112:replication_chain_First:ns_1@10.143.192.102:last_ack_seqno:   28
vb_112:replication_chain_First:ns_1@10.143.192.102:last_write_seqno: 0
vb_112:replication_chain_First:size:                                 2
vb_112:state:                                                        active

/opt/couchbase/bin/cbstats localhost:11210 -u Administrator -p password \
durability-monitor -b travel-sample 17
vb_17:high_completed_seqno: 0
vb_17:high_prepared_seqno:  0
vb_17:state:                replica

## [](#see-also)See Also

An overview of durability is provided in [Durability](../../learn/data/durability.md).