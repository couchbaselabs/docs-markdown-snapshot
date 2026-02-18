---
title: Rebalance
description: When one or more nodes have been brought into or taken out of a
  cluster, <em>rebalance</em> redistributes data, indexes, event processing, and
  query processing among available nodes.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/reference/pages/rest-rebalance-overview.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/2.0/reference/rest-rebalance-overview.html)

# Rebalance

> When one or more nodes have been brought into or taken out of a cluster, _rebalance_ redistributes data, indexes, event processing, and query processing among available nodes. Rebalance can be performed and configured by means of the REST API. 

## [](#apis-in-this-section)APIs in this Section

_Rebalance_ must be performed whenever the number of nodes in a cluster have changed, and whenever buckets have been added or removed. A complete overview is provided in [Rebalance](#learn:clusters-and-availability/rebalance.adoc).

The REST API for rebalance is as follows:

| HTTP Method | URI                                             | Documented at                                                                                      |
| ----------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| POST        | /controller/rebalance                           | [Rebalancing the Cluster](rest-cluster-rebalance.md)                                               |
| GET         | /pools/default                                  | [Getting Rebalance Reason Codes](rest-retrieve-cluster-rebalance-reason-codes.md)                  |
| GET         | /pools/default/rebalanceProgress                | [Getting Rebalance Progress](rest-get-rebalance-progress.md)                                       |
| GET         | /pools/default/retryRebalance                   | [Configuring Rebalance Retries](rest-configure-rebalance-retry.md)                                 |
| POST        | /pools/default/retryRebalance                   | [Configuring Rebalance Retries](rest-configure-rebalance-retry.md)                                 |
| GET         | /pools/default/pendingRetryRebalance            | [Getting Rebalance-Retry Status](rest-get-rebalance-retry.md)                                      |
| POST        | /controller/cancelRebalanceRetry/<rebalance-id> | [Canceling Rebalance Retries](rest-cancel-rebalance-retry.md)                                      |
| GET         | /settings/rebalance                             | [Limiting Concurrent vBucket Moves](#reference:rest-limit-rebalance-moves.adoc)                    |
| POST        | /settings/rebalance                             | [Limiting Concurrent vBucket Moves](#reference:rest-limit-rebalance-moves.adoc)                    |
| POST        | /internalSettings                               | [Disabling Consistent View Query Results on Rebalance](#reference:rest-cluster-disable-query.adoc) |