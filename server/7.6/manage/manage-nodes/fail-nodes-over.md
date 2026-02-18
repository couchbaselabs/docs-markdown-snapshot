---
title: Fail a Node Over and Rebalance
description: Nodes can be <em>failed over</em>, and thereby removed safely from
  a cluster in the event of unavoidable downtime, without any break in the
  serving of data to applications.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/manage/pages/manage-nodes/fail-nodes-over.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/manage/manage-nodes/fail-nodes-over.html)

# Fail a Node Over and Rebalance

> Nodes can be _failed over_, and thereby removed safely from a cluster in the event of unavoidable downtime, without any break in the serving of data to applications. 

## [](#understanding-failover)Understanding Failover

A complete conceptual description of failover is provided in [Failover](../../learn/clusters-and-availability/failover.md). There are two basic types: _graceful_ and _hard_.

* _Graceful_ allows a Data Service node to be removed from the cluster _proactively_, in an orderly and controlled fashion (say, for the purposes of system-maintenance). It is manually initiated when the entire cluster is in a healthy state, and all active and replica vBuckets on all nodes are available.
* _Hard_: The ability to drop a node from the cluster _reactively_, because the node has become unavailable or unstable. It is manually or automatically initiated, and should be applied after the point at which active vBuckets have been lost. If applied to an available node running the Data Service, ongoing writes and replications may be interrupted.

The automatic initiation of hard failover is known as _automatic_ failover, and is configured by means of the [General](../manage-settings/general-settings.md) settings screen, in the **Settings** area of Couchbase Web Console; or by means of equivalent CLI and REST API commands.

Note that when a node is flagged for _failover_ (as opposed to _removal_), replica vBuckets are lost when rebalance occurs, following node-removal. By contrast, _removal_ creates new copies of replica vBuckets that would otherwise be lost (thereby creating greater competition for the memory resources of the remaining nodes).

This section shows how graceful and hard failover can be initiated.