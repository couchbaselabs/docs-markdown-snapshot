---
title: Manual Failover
description: Manual failover can be managed by means of the REST API.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-cluster-manualfailover-intro.adoc
  xref: xref:7.6@server:rest-api:rest-cluster-manualfailover-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/rest-api/rest-cluster-manualfailover-intro.html)

# Manual Failover

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> Manual failover can be managed by means of the REST API. 

## [](#apis-in-this-section)APIs in this Section

The APIs described in this section support _Manual Failover_. A complete overview is provided in [Failover](../learn/clusters-and-availability/failover.md).

The APIs described in this section are listed in the following table.

| HTTP Method | URI                               | Documented at                                              |
| ----------- | --------------------------------- | ---------------------------------------------------------- |
| POST        | /controller/failOver              | [Performing Hard Failover](rest-node-failover.md)          |
| POST        | /controller/startGracefulFailover | [Performing Graceful Failover](rest-failover-graceful.md)  |
| POST        | /controller/setRecoveryType       | [Setting Recovery Type](rest-node-recovery-incremental.md) |