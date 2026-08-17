---
title: dcp
description: Shows statistics for Database Change Protocol (DCP).
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-dcp.adoc
  xref: xref:7.6@server:cli:cbstats/cbstats-dcp.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbstats/cbstats-dcp.html)

# dcp

> Shows statistics for Database Change Protocol (DCP). 

## [](#syntax)Syntax

Request syntax:

cbstats HOST:11210 dcp

## [](#description)Description

This command retrieves connections specific to statistics.

DCP statistics by connection type

DCP provides statistics for consumer, producer, and notifier connection types. The following tables describe the available consumer, producer, and notifier connection statistics. Each connection type has a group of statistics that apply to the connection overall and a group of statistics that apply to the individual streams in the connections.

The identifier for each DCP statistic begins with the string `ep_dcpq:` followed by a unique `client_id` and another colon. For example, if your client is named `slave1`, the identifier for the DCP statistic named `created` is `ep_dcpq:slave1:created`.

__Table 1\. Consumer connection statistics__
| Name                | Description                                            |
| ------------------- | ------------------------------------------------------ |
| connected           | True if this client is connected                       |
| created             | Creation time of the DCP connection                    |
| pending\_disconnect | True if we're hanging up on this client                |
| reserved            | True if the DCP stream is reserved                     |
| supports\_ack       | True if the connection uses flow control               |
| total\_acked\_bytes | The number of bytes that the consumer has acknowledged |
| type                | The connection type (producer, consumer, or notifier)  |

Consumer connection per-stream statistics

| Name               | Description                                             |
| ------------------ | ------------------------------------------------------- |
| buffer\_bytes      | The number of unprocessed bytes                         |
| buffer\_items      | The number of unprocessed items                         |
| end\_seqno         | The sequence number where this stream should end        |
| flags              | The flags used to create this stream                    |
| items\_ready       | Whether the stream has messages ready to send           |
| opaque             | The unique stream identifier                            |
| snap\_end\_seqno   | The end sequence number of the last snapshot received   |
| snap\_start\_seqno | The start sequence number of the last snapshot received |
| start\_seqno       | The start sequence number used to create this stream    |
| state              | The stream state (pending, reading, or dead)            |
| vb\_uuid           | The vBucket UUID used to create this stream             |

Producer and notifier connection statistics (stream-level statistics)

| Name                 | Description                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------- |
| backfilled           | The number of items sent from disk                                                        |
| cur\_snapshot\_end   | The end sequence number of the current snapshot being received                            |
| cur\_snapshot\_start | The start sequence number of the current snapshot being received                          |
| cur\_snapshot\_type  | The type of the current snapshot being received                                           |
| end\_seqno           | The sequence number of the last mutation to send                                          |
| flags                | The flags supplied in the stream request                                                  |
| items\_ready         | Whether the stream has items ready to send                                                |
| last\_sent\_seqno    | The last sequence number sent by this stream                                              |
| memory               | The number of items sent from memory                                                      |
| opaque               | The unique stream identifier                                                              |
| snap\_end\_seqno     | The last snapshot end sequence number (used if a consumer is resuming a stream)           |
| snap\_start\_seqno   | The last snapshot start sequence number (used if a consumer is resuming a stream)         |
| start\_seqno         | The sequence number to start sending mutations from                                       |
| state                | The stream state (pending, backfilling, in-memory, takeover-send, takeover-wait, or dead) |
| vb\_uuid             | The vBucket UUID used in the stream request                                               |

Producer and notifier connection statistics (producer-level statistics)

| Name                | Description                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------- |
| bytes\_sent         | The number of unacknowledged bytes sent to the consumer.                                      |
| connected           | True if this client is connected.                                                             |
| created             | Creation time for the DCP connection.                                                         |
| flow\_control       | True if the connection uses flow control.                                                     |
| items\_remaining    | The number of items remaining to be sent.                                                     |
| items\_sent         | The number of items already sent to the consumer.                                             |
| last\_sent\_time    | The last time items have been sent.                                                           |
| noop\_enabled       | Indicates whether this connection sends noops.                                                |
| noop\_wait          | Indicates whether this connection is waiting for a noop response from the consumer.           |
| pending\_disconnect | True if we're hanging up on this client.                                                      |
| reserved            | True if the DCP stream is reserved.                                                           |
| supports\_ack       | True if the connection uses flow control.                                                     |
| total\_acked\_bytes | The number of bytes that have been acknowledged by the consumer when flow control is enabled. |
| total\_bytes\_sent  | The number of bytes already sent to the consumer.                                             |
| type                | The connection type (producer, consumer, or notifier).                                        |
| unacked\_bytes      | The number of bytes the consumer has not acknowledged.                                        |

## [](#options)Options

None

## [](#example)Example

This example shows a request for all DCP-related statistics.

# ./cbstats 10.5.2.54:11210 dcp

Here's some output from the command. The output is quite lengthy, so this sample is truncated.

ep_dcp_count:                                                                               6
 ep_dcp_items_remaining:                                                                     0
 ep_dcp_items_sent:                                                                          0
 ep_dcp_producer_count:                                                                      3
 ep_dcp_queue_backfillremaining:                                                             0
 ep_dcp_queue_fill:                                                                          0
 ep_dcp_total_bytes:                                                                         6630
 ep_dcp_total_queue:                                                                         0
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:connected:                      true
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:created:                        1168
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:pending_disconnect:             false
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:reserved:                       true
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_buffer_bytes:        0
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_buffer_items:        0
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_cur_snapshot_type:   none
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_end_seqno:           18446744073709551615
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_flags:               0
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_items_ready:         false
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_last_received_seqno: 0
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_opaque:              73
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_snap_end_seqno:      0
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_snap_start_seqno:    0
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_start_seqno:         0
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_state:               reading
 eq_dcpq:replication:ns_1@10.5.2.117->ns_1@10.5.2.54:default:stream_100_vb_uuid:             122364695596024
 ...