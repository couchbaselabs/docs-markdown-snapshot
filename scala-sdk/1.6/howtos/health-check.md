---
title: Health Check
description: In today's distributed and virtual environments, users will often
  not have full administrative control over their whole network.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/temp/1.6/modules/howtos/pages/health-check.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:1.6@scala-sdk:howtos:health-check.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.6/howtos/health-check.html)

# Health Check

> In today's distributed and virtual environments, users will often not have full administrative control over their whole network. Health Check introduces _Ping_ to check nodes are still healthy, and to force idle connections to be kept alive in environments with eager shutdowns of unused resources. _Diagnostics_ requests a report from a node, giving instant health check information. 

Diagnosing problems in distributed environments is far from easy, so Couchbase provides a _Health Check API_ with `Ping()` for active monitoring. ans `Diagnostics()` for a look at what the client believes is the current state of the cluster. More extensive discussion of the uses of Health Check can be found in the [Health Check Concept Guide](../concept-docs/health-check.md).

## [](#ping)Ping

For use of `ping()`, refer to [the API docs](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Cluster.html#ping%28options:com.couchbase.client.scala.diagnostics.PingOptions%29:scala.util.Try%5Bcom.couchbase.client.core.diagnostics.PingResult%5D). See also the [PingOptions](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/diagnostics/PingOptions.html).

## [](#diagnostics)Diagnostics

`Diagnostics` returns a list of the nodes that the SDK currently has (or had) a connection to, and the current status of the connection. However this call _does not_ actively poll the nodes, reporting instead the state the last time it tried to access each node. If you want the _current_ status, then use [Ping](#ping).

For specifics, refer to the [API docs](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Cluster.html#diagnostics%28options:com.couchbase.client.scala.diagnostics.DiagnosticsOptions%29:scala.util.Try%5Bcom.couchbase.client.core.diagnostics.DiagnosticsResult%5D) — including [DiagnosticsOptions](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/diagnostics/DiagnosticsOptions.html).