---
title: Diagnosing and preventing Network Problems with Health Check
description: In today's distributed and virtual environments, users will often
  not have full administrative control over their whole network.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.3/modules/howtos/pages/health-check.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/php-sdk/4.3/howtos/health-check.html)

# Diagnosing and preventing Network Problems with Health Check

> In today’s distributed and virtual environments, users will often not have full administrative control over their whole network. Health Check introduces _Ping_ to check nodes are still healthy, and to force idle connections to be kept alive in environments with eager shutdowns of unused resources. _Diagnostics_ requests a report from a node, giving instant health check information. 

Diagnosing problems in distributed environments is far from easy, so Couchbase provides a _Health Check API_ with `Ping()` for active monitoring. ans `Diagnostics()` for a look at what the client believes is the current state of the cluster. More extensive discussion of the uses of Health Check can be found in the [Health Check Concept Guide](../concept-docs/health-check.md).

Usage can be found in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Bucket.html#method%5Fping).