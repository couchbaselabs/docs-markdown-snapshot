---
title: Request Tracing
description: Collecting information about an individual request and its response
  is an essential feature of every observability stack.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.2/modules/howtos/pages/observability-tracing.adoc
  xref: xref:1.2@cxx-sdk:howtos:observability-tracing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/1.2/howtos/observability-tracing.html)

# Request Tracing

> Collecting information about an individual request and its response is an essential feature of every observability stack. 

To give insight into a request/response flow, the SDK provides a `RequestTracer` interface and ships with both a default implementation as well as modules that can feed the traces to external systems (including OpenTelemetry).

## [](#the-default-thresholdrequesttracer)The Default ThresholdRequestTracer

By default, the SDK will emit information about requests that are over a configurable threshold every 10 seconds. Note that if no requests are over the threshold then no event / log will be emitted.

It is possible to customize this behavior by modifying the configuration:

```scala
val config: Try[ClusterEnvironment] = ClusterEnvironment.builder
  .thresholdRequestTracerConfig(ThresholdRequestTracerConfig()
    .emitInterval(1.minutes)
    .kvThreshold(2.seconds))
  .build

val cluster: Try[Cluster] = config.flatMap(c =>
  Cluster.connect("localhost", ClusterOptions
    .create("username", "password")
    .environment(c)))
```

In this case the emit interval is one minute and Key/Value requests will only be considered if their latency is greater or equal than two seconds.

The JSON blob emitted looks similar to the following (prettified here for readability):

```json
[
   {
      "top":[
         {
            "operation_name":"GetRequest",
            "server_us":2,
            "last_local_id":"E64FED2600000001/00000000EA6B514E",
            "last_local_address":"127.0.0.1:51807",
            "last_remote_address":"127.0.0.1:11210",
            "last_dispatch_us":2748,
            "last_operation_id":"0x9",
            "total_us":324653
         },
         {
            "operation_name":"GetRequest",
            "server_us":0,
            "last_local_id":"E64FED2600000001/00000000EA6B514E",
            "last_local_address":"127.0.0.1:51807",
            "last_remote_address":"127.0.0.1:11210",
            "last_dispatch_us":1916,
            "last_operation_id":"0x1b692",
            "total_us":2007
         }
      ],
      "service":"kv",
      "count":2
   }
]
```

For each service (e.g. Key-Value or Query), an entry exists in the outer JSON array. The top N (10 by default) slowest operations are collected and displayed, sorted by the total duration. This promotes quick visibility of the "worst offenders", and more efficient troubleshooting.

Please note that in future releases this format is planned to change for easier readability, so we do not provide any stability guarantees on the logging output format and it might change between minor versions.

A new, yet to be stabilized, format can be enabled by setting the `com.couchbase.thresholdRequestTracerNewOutputFormat` system property to `true`. More information will be provided as we get closer to stabilization.

## [](#opentelemetry-integration)OpenTelemetry Integration

The built-in tracer is great if you do not have a centralized monitoring system, but if you already plug into the OpenTelemetry ecosystem we want to make sure to provide first-class support.

### [](#opentelemetry-setup)OpenTelemetry Setup

There are many ways to configure OpenTelemetry. The first thing to consider is where your application should send the OpenTelemetry spans. They can be sent directly to a tracing tool like Zipkin or Jaegar. But a popular choice is to instead send to the [OpenTelemetry collector](https://opentelemetry.io/docs/collector/getting-started/), which can perform some span processing (such as batching) before sending on to your tracing tool.

This minimal OpenTelemetry Collector configuration file will simply log all spans to console, to sanity check that your application is outputting spans to the collector:

```yaml
receivers:
  otlp:
    protocols:
      grpc:

exporters:
  logging:
    logLevel: debug

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: []
      exporters: [logging]
    metrics:
      receivers: [otlp]
      processors: []
      exporters: [logging]
```

Save this to a file `config.yaml` and run the collector with:

```console
`otelcol --config config.yaml
```

### [](#application-setup)Application Setup

Include an additional dependency which provides the interoperability code:

```sbt
libraryDependencies += "com.couchbase.client" % "tracing-opentelemetry" % "0.3.4"

libraryDependencies += "io.opentelemetry" % "opentelemetry-sdk" % "1.1.0"
libraryDependencies += "io.opentelemetry" % "opentelemetry-exporter-zipkin" % "1.1.0"
libraryDependencies += "io.opentelemetry" % "opentelemetry-exporter-otlp" % "1.1.0"
libraryDependencies += "io.grpc" % "grpc-netty" % "1.35.0"
```

Before starting, here are all imports used in the following examples:

```scala

import com.couchbase.client.core.cnc.RequestSpan.StatusCode
import com.couchbase.client.core.cnc.RequestTracer
import com.couchbase.client.scala.durability.Durability
import com.couchbase.client.scala.env.{ClusterEnvironment, ThresholdRequestTracerConfig}
import com.couchbase.client.scala.json.JsonObject
import com.couchbase.client.scala.kv.{GetOptions, UpsertOptions}
import com.couchbase.client.scala.{Cluster, ClusterOptions, Collection}
import com.couchbase.client.tracing.opentelemetry.{OpenTelemetryRequestSpan, OpenTelemetryRequestTracer}
import io.opentelemetry.exporter.otlp.trace.OtlpGrpcSpanExporter
import io.opentelemetry.sdk.trace.SdkTracerProvider
import io.opentelemetry.sdk.trace.`export`.{BatchSpanProcessor, SimpleSpanProcessor}
import io.opentelemetry.sdk.trace.samplers.Sampler

import scala.concurrent.duration._
import scala.util.Try
```

Now, you can configure an OpenTelemetry `TracerProvider`. We are using the OTLP GRPC exporter, which the OpenTelemetry Collector is configured to listen for:

```scala

// Configure OpenTelemetry
val spanExporter = OtlpGrpcSpanExporter.getDefault
val spanProcessor = BatchSpanProcessor.builder(spanExporter)
  .setScheduleDelay(java.time.Duration.ofMillis(100))
  .build

val tracerProvider = SdkTracerProvider.builder
  .setSampler(Sampler.alwaysOn)
  .addSpanProcessor(spanProcessor)
  .build
```

Once the OpenTelemetry `TracerProvider` is set up, it can be wrapped into a Couchbase `RequestTracer` and passed into the environment:

```scala
// Get a Couchbase RequestTracer from the OpenTelemetry TracerProvider
val tracer: RequestTracer = OpenTelemetryRequestTracer.wrap(tracerProvider)

// Use the RequestTracer
val config: Try[ClusterEnvironment] = ClusterEnvironment.builder
  .requestTracer(tracer)
  .build

val cluster: Try[Cluster] = config.flatMap(c =>
  Cluster.connect("localhost", ClusterOptions
    .create("Administrator", "password")
    .environment(c)))
```

At this point, all spans will be sent into the OpenTelemetry collector. Once you are performing operations, you should see the collector (if it's using the configuration above) outputting spans to console:

```none
Span #510
    Trace ID       : 3a2e0be43ba961d0fa5220aa4e198a6c
    Parent ID      :
    ID             : 137a0adf88b8e798
    Name           : upsert
    Kind           : SPAN_KIND_INTERNAL
    Start time     : 2021-04-29 10:57:50.3517228 +0100 BST
    End time       : 2021-04-29 10:57:50.3531412 +0100 BST
    Status code    : STATUS_CODE_UNSET
    Status message :
Attributes:
     -> db.name: STRING(default)
     -> db.couchbase.service: STRING(kv)
     -> db.operation: STRING(upsert)
     -> db.system: STRING(couchbase)
     -> db.couchbase.collection: STRING(_default)
     -> db.couchbase.scope: STRING(_default)
```

### [](#parent-spans)Parent Spans

If you want to set a parent for an SDK request, you can do it in the respective `*Options` for any operation. Just call `OpenTelemetryRequestSpan.wrap` to wrap your OpenTelemetry span into a Couchbase span:

```scala
def getWithSpan(collection: Collection, span: io.opentelemetry.api.trace.Span) {
  collection.get("id", GetOptions()
    .parentSpan(OpenTelemetryRequestSpan.wrap(span)))
}
```

## [](#opentracing-integration)OpenTracing Integration

In addition to OpenTelemetry, we also provide support for OpenTracing for legacy systems which have not yet migrated to OpenTelemetry. Note that we still recommend migrating eventually since OpenTracing has been sunsetted.

You need to include the `tracing-opentracing` module:

```sbt
libraryDependencies += "com.couchbase.client" % "tracing-opentracing" % "0.3.4"
```

And then wrap the OpenTracing `Tracer`:

```scala
val tracer: RequestTracer = OpenTracingRequestTracer.wrap(tracer)

// Use the RequestTracer
val config: Try[ClusterEnvironment] = ClusterEnvironment.builder
  .requestTracer(tracer)
  .build
```

OpenTracing spans can be wrapped with `OpenTracingRequestSpan.wrap` and passed as parent spans to all SDK operations, in the same way as with OpenTelemetry.