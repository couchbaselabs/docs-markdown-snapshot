---
title: Auto-Failover
description: Auto-failover can be managed by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-cluster-autofailover-intro.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:rest-api:rest-cluster-autofailover-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/rest-api/rest-cluster-autofailover-intro.html)

# Auto-Failover

> Auto-failover can be managed by means of the REST API. 

## [](#apis-in-this-section)APIs in this Section

The APIs described in this section support _Automatic Failover_ —- or _auto-failover_; which can be configured to fail over one or more nodes automatically. No immediate administrator-intervention is required. Specifically, the Cluster Manager autonomously detects and verifies that the nodes are unresponsive, and then initiates the hard failover process. Auto-failover does not fix or identify problems that may have occurred. Once appropriate fixes have been applied to the cluster by the administrator, a rebalance is required. Auto-failover is always _hard_ failover.

A complete overview of auto-failover is provided in [Automatic Failover](../learn/clusters-and-availability/automatic-failover.md).

The APIs for auto-failover are listed in the following table.

| HTTP Method | URI                               | Documented at                                                               |
| ----------- | --------------------------------- | --------------------------------------------------------------------------- |
| GET         | /settings/autoFailover            | [Retrieving Auto-Failover Settings](rest-cluster-autofailover-settings.md)  |
| POST        | /settings/autoFailover            | [Enabling and Disabling Auto-Failover](rest-cluster-autofailover-enable.md) |
| POST        | /settings/autoFailover/resetCount | [Resetting Auto-Failover](rest-cluster-autofailover-reset.md)               |
| POST        | /controller/setRecoveryType       | [Setting Recovery Type](rest-node-recovery-incremental.md)                  |

## [](#auto-failover-and-durability)Auto-Failover and Durability

Couchbase Server provides _durability_, which ensures the greatest likelihood of data-writes surviving unexpected anomalies, such as node-outages. The auto-failover maximum should be established to support guarantees of durability. See [Durability](../learn/data/durability.md), for information.