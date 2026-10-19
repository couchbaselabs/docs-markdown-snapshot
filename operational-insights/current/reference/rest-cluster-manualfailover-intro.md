---
title: Manual Failover
description: Manual failover can be managed by means of the REST API.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-cluster-manualfailover-intro.adoc
  xref: xref:enterprise-analytics:reference:rest-cluster-manualfailover-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-cluster-manualfailover-intro.html)

# Manual Failover

> Manual failover can be managed by means of the REST API. 

## [](#apis-in-this-section)APIs in this Section

The APIs described in this section support _Manual Failover_. An overview is provided in [Failover](../manage/manage-nodes/fail-nodes-over.md); for recovering a failed-over node, see [Recover a Node and Rebalance](../manage/manage-nodes/recover-nodes.md).

The APIs described in this section are listed in the following table.

| HTTP Method | URI                         | Documented at                                     |
| ----------- | --------------------------- | ------------------------------------------------- |
| POST        | /controller/failOver        | [Performing Hard Failover](rest-node-failover.md) |
| POST        | /controller/setRecoveryType | [Setting Recovery Type](rest-node-recovery.md)    |
| POST        | /controller/hardResetNode   | [Reinitializing Nodes](rest-reinitialize-node.md) |