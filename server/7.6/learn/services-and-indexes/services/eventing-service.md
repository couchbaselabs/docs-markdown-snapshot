---
title: Eventing Service
description: The <em>Eventing Service</em> provides near real-time handling of
  changes to data; whereby code is executed either in response to mutations, or
  as scheduled by timers.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/learn/pages/services-and-indexes/services/eventing-service.adoc
  xref: xref:7.6@server:learn:services-and-indexes/services/eventing-service.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/learn/services-and-indexes/services/eventing-service.html)

# Eventing Service

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> The _Eventing Service_ provides near real-time handling of changes to data; whereby code is executed either in response to mutations, or as scheduled by timers. 

## [](#understanding-eventing)Understanding Eventing

The _Eventing Service_ allows functions to be written, saved, and triggered in response to events. Events include changes made to specified items, and the arrival of scheduled points-in-time.

The Eventing Service depends on the [Data Service](data-service.md), which must therefore be running on at least one cluster node.

For information on using the Eventing Service, see [Eventing Service: Fundamentals](../../../eventing/eventing-overview.md).