---
title: Tracing
description: Tracing Couchbase Distributed ACID transactions.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.0/modules/howtos/pages/transactions-tracing.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cxx-sdk/1.0/howtos/transactions-tracing.html)

# Tracing

> Tracing Couchbase Distributed ACID transactions. 

If configured, detailed telemetry on each transaction can be output that is compatible with various external systems including OpenTelemetry and its predecessor OpenTracing. This telemetry is particularly useful for monitoring performance.

See the [SDK Request Tracing documentation](observability-tracing.md) for how to configure this.

Tracing should currently be regarded as 'developer preview' functionality, as the spans and attributes output may change over time.

## [](#parent-spans)Parent Spans

The application may wish to indicate that the transaction is part of a larger span — for instance, a user request. It can do this by passing that as a parent span.

This can be done using the SDK’s `RequestTracer` abstraction as so:

```scala
val span = cluster.env.core.requestTracer.requestSpan("your-span-name", null)
cluster.transactions.run((ctx: TransactionAttemptContext) => {
  Success()
}, Some(TransactionOptions().parentSpan(span)))
```

Or if you have an existing OpenTelemetry span you can easily convert it to a Couchbase `RequestSpan` and pass it to the SDK:

```scala
val span = Span.current // this is a span created by your code earlier

val wrapped = OpenTelemetryRequestSpan.wrap(span)
cluster.transactions.run((ctx: TransactionAttemptContext) => {
  Success()
}, Some(TransactionOptions().parentSpan(wrapped)))
```