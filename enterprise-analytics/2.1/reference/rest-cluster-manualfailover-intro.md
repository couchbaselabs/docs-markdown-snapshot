---
title: Manual Failover
description: Manual failover can be managed by means of the REST API.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/reference/pages/rest-cluster-manualfailover-intro.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:reference:rest-cluster-manualfailover-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/reference/rest-cluster-manualfailover-intro.html)

# Manual Failover

> Manual failover can be managed by means of the REST API. 

## [](#apis-in-this-section)APIs in this Section

The APIs described in this section support _Manual Failover_. A complete overview is provided in [Failover](#learn:clusters-and-availability/failover.adoc).

The APIs described in this section are listed in the following table.

| HTTP Method | URI                               | Documented at                                                           |
| ----------- | --------------------------------- | ----------------------------------------------------------------------- |
| POST        | /controller/failOver              | [Performing Hard Failover](rest-node-failover.md)                       |
| POST        | /controller/startGracefulFailover | [Performing Graceful Failover](#reference:rest-failover-graceful.adoc)  |
| POST        | /controller/setRecoveryType       | [Setting Recovery Type](#reference:rest-node-recovery-incremental.adoc) |