---
title: Manual Failover
description: Manual failover can be managed by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-cluster-manualfailover-intro.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:rest-api:rest-cluster-manualfailover-intro.adoc[]
---

[View original HTML](/server/7.6/rest-api/rest-cluster-manualfailover-intro.html)

# Manual Failover

> Manual failover can be managed by means of the REST API. 

## [](#apis-in-this-section)APIs in this Section

The APIs described in this section support _Manual Failover_. A complete overview is provided in [Failover](../learn/clusters-and-availability/failover.md).

The APIs described in this section are listed in the following table.

| HTTP Method | URI                               | Documented at                                              |
| ----------- | --------------------------------- | ---------------------------------------------------------- |
| POST        | /controller/failOver              | [Performing Hard Failover](rest-node-failover.md)          |
| POST        | /controller/startGracefulFailover | [Performing Graceful Failover](rest-failover-graceful.md)  |
| POST        | /controller/setRecoveryType       | [Setting Recovery Type](rest-node-recovery-incremental.md) |