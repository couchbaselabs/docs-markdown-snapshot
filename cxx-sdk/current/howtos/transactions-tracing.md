---
title: Tracing
description: Tracing Couchbase Distributed ACID transactions.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.4/modules/howtos/pages/transactions-tracing.adoc
  xref: xref:cxx-sdk:howtos:transactions-tracing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/current/howtos/transactions-tracing.html)

# Tracing

> Tracing Couchbase Distributed ACID transactions. 

If configured, detailed telemetry on each transaction can be output that is compatible with various external systems including OpenTelemetry and its predecessor OpenTracing. This telemetry is particularly useful for monitoring performance.

See the [SDK Request Tracing documentation](observability-tracing.md) for how to configure this.

Tracing should currently be regarded as 'developer preview' functionality, as the spans and attributes output may change over time.

## [](#parent-spans)Parent Spans

The application may wish to indicate that the transaction is part of a larger span — for instance, a user request. It can do this by passing that as a parent span.

This can be done using the SDK's `RequestTracer` abstraction as so:

```scala
Unresolved include directive in modules/howtos/pages/transactions-tracing.adoc - include::devguide:example$scala/TransactionsExample.scala[]
```

Or if you have an existing OpenTelemetry span you can easily convert it to a Couchbase `RequestSpan` and pass it to the SDK:

```scala
Unresolved include directive in modules/howtos/pages/transactions-tracing.adoc - include::devguide:example$scala/TransactionsExample.scala[]
```