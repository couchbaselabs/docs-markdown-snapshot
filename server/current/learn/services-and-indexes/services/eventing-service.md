---
title: Eventing Service
description: The <em>Eventing Service</em> provides near real-time handling of
  changes to data; whereby code is executed either in response to mutations, or
  as scheduled by timers.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/learn/pages/services-and-indexes/services/eventing-service.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:learn:services-and-indexes/services/eventing-service.adoc[]
---

[View original HTML](/server/current/learn/services-and-indexes/services/eventing-service.html)

# Eventing Service

> The _Eventing Service_ provides near real-time handling of changes to data; whereby code is executed either in response to mutations, or as scheduled by timers. 

## [](#understanding-eventing)Understanding Eventing

The _Eventing Service_ allows functions to be written, saved, and triggered in response to events. Events include changes made to specified items, and the arrival of scheduled points-in-time.

The Eventing Service depends on the [Data Service](data-service.md), which must therefore be running on at least one cluster node.

For more information about using the Eventing Service, see [Eventing Service: Fundamentals](../../../eventing/eventing-overview.md).

For more information about adding or removing the Eventing Service on an existing node of a cluster, see [Modify Services and Rebalance](../../../manage/manage-nodes/modify-services-and-rebalance.md).