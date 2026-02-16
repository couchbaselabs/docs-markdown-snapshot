[View original HTML](/server/7.6/cli/cbstats/cbstats-dcpagg.html)

> Retrieves statistics that are logically grouped and aggregated together by prefixes. 

## [](#syntax)Syntax

cbstats HOST:11210 dcpagg

## [](#description)Description

This command retrieves statistics that are logically grouped and aggregated together by prefixes.

For example, if all your DCP connections started with the string `xdcr:` or `replication:`, you could use the command `cbstats dcpagg` to request statistics grouped by everything before the first colon character, giving you a set for `xdcr:` statistics and a set for `replication:` statistics.

The following table describes the aggregated DCP statistics.

__Table 1\. Aggregated DCP statistics__
| Name                            | Description                                                |
| ------------------------------- | ---------------------------------------------------------- |
| \[prefix\]:count                | Number of connections matching this prefix                 |
| \[prefix\]:producer\_count      | Total producer connections with this prefix                |
| \[prefix\]:items\_sent          | Total items sent with this prefix                          |
| \[prefix\]:items\_remaining     | Total items remaining to be sent with this prefix          |
| \[prefix\]:total\_bytes         | Total number of bytes sent with this prefix                |
| \[prefix\]:total\_backlog\_size | Total backfill items remaining to be sent with this prefix |

## [](#options)Options

None

## [](#example)Example

The following example shows a request for a set of aggregated DCP statistics:

# ./cbstats 10.5.2.54:11210 dcpagg

Here’s the output from the command:

 :total:backoff:                 0
 :total:count:                   6
 :total:items_remaining:         0
 :total:items_sent:              0
 :total:producer_count:          3
 :total:total_backlog_size:      0
 :total:total_bytes:             6630
 replication:backoff:            0
 replication:count:              6
 replication:items_remaining:    0
 replication:items_sent:         0
 replication:producer_count:     3
 replication:total_backlog_size: 0
 replication:total_bytes:        6630