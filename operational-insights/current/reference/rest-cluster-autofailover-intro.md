---
title: Auto-Failover
description: Auto-failover can be managed by means of the REST API.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-cluster-autofailover-intro.adoc
  xref: xref:enterprise-analytics:reference:rest-cluster-autofailover-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-cluster-autofailover-intro.html)

# Auto-Failover

> Auto-failover can be managed by means of the REST API. 

## [](#apis-in-this-section)APIs in this Section

The APIs described in this section support _Automatic Failover_ — or _auto-failover_; which can be configured to fail over one or more nodes automatically. No immediate administrator-intervention is required. Specifically, the Cluster Manager autonomously detects and verifies that the nodes are unresponsive, and then initiates the hard failover process. Auto-failover does not fix or identify problems that may have occurred. Once appropriate fixes have been applied to the cluster by the administrator, a rebalance is required. Auto-failover is always _hard_ failover.

An overview of failover, including how auto-failover is configured, is provided in [Failover](../manage/manage-nodes/fail-nodes-over.md).

The APIs for auto-failover are listed in the following table.

| HTTP Method | URI                               | Documented at                                                               |
| ----------- | --------------------------------- | --------------------------------------------------------------------------- |
| GET         | /settings/autoFailover            | [Retrieving Auto-Failover Settings](rest-cluster-autofailover-settings.md)  |
| POST        | /settings/autoFailover            | [Enabling and Disabling Auto-Failover](rest-cluster-autofailover-enable.md) |
| POST        | /settings/autoFailover/resetCount | [Resetting Auto-Failover](rest-cluster-autofailover-reset.md)               |
| POST        | /controller/setRecoveryType       | [Setting Recovery Type](rest-node-recovery.md)                              |