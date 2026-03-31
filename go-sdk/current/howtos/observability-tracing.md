---
title: Request Tracing
description: Collecting information about an individual request and its response
  is an essential feature of every observability stack.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/release/2.12/modules/howtos/pages/observability-tracing.adoc
pubDate: 2026-03-31T05:15:32.656Z
link: xref:go-sdk:howtos:observability-tracing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/current/howtos/observability-tracing.html)

# Request Tracing

> Collecting information about an individual request and its response is an essential feature of every observability stack. 

To give insight into a request/response flow, the SDK provides a `RequestTracer` interface and ships with both a default implementation as well as a module that can be plugged in to feed the traces to external systems (including OpenTelemetry).

## [](#the-default-thresholdloggingtracer)The Default ThresholdLoggingTracer

By default, the SDK will emit information about requests that are over a configurable threshold every 10 seconds. Note that if no requests are over the threshold no event / log will be emitted.

It is possible to customize this behavior by modifying the configuration:

```go
	tracer := gocb.NewThresholdLoggingTracer(&gocb.ThresholdLoggingOptions{
		Interval:    1 * time.Minute,
		SampleSize:  10,
		KVThreshold: 2 * time.Second,
	})
```

In this case the emit interval is one minute and Key/Value requests will only be considered if their latency is greater or equal to two seconds.

The JSON blob emitted looks similar to the following (prettified here for readability):

```json
[
   {
      "top":[
         {
            "operation_name":"Get",
            "server_us":2,
            "last_local_id":"E64FED2600000001/00000000EA6B514E",
            "last_local_address":"127.0.0.1:51807",
            "last_remote_address":"127.0.0.1:11210",
            "last_dispatch_us":2748,
            "last_operation_id":"0x9",
            "total_us":324653
         }
      ],
      "service":"kv",
      "count":1
   }
]
```

For each service (e.g. Key/Value or Query) an entry exists in the outer JSON array. The top N (10 by default) slowest operations are collected and displayed, sorted by the total duration. This promotes quick visibility of the "worst offenders" and more efficient troubleshooting.

Please note that we do not provide any stability guarantees on the logging output format and it might change between minor versions.

The `ThresholdLoggingTracer` can be configured using `ThresholdLoggingOptions`. The following table shows the currently available properties:

__Table 1\. ThresholdLoggingOptions Properties__
| Property            | Default          | Description                                           |
| ------------------- | ---------------- | ----------------------------------------------------- |
| Interval            | 10 seconds       | The interval where found slow operations are emitted. |
| SampleSize          | 10               | The number of samples to store per service.           |
| KVThreshold         | 500 milliseconds | The threshold for the KV service.                     |
| ViewsThreshold      | 1 second         | The threshold for the views service.                  |
| QueryThreshold      | 1 second         | The threshold for the query service.                  |
| SearchThreshold     | 1 second         | The threshold for the search service.                 |
| AnalyticsThreshold  | 1 second         | The threshold for the analytics service.              |
| ManagementThreshold | 1 second         | The threshold for the management service.             |

## [](#opentelemetry-integration)OpenTelemetry Integration

The built-in tracer is great if you do not have a centralized monitoring system, but if you already plug into the OpenTelemetry ecosystem we want to make sure to provide first-class support.

### [](#exporting-to-opentelemetry)Exporting to OpenTelemetry

This method exports tracing telemetry in OpenTelemetry's standard format (OTLP), which can be sent to any OTLP-compatible receiver such as Jaeger, Zipkin or `opentelemetry-collector`.

First, add the Couchbase OpenTelemetry module and the OTLP trace exporter as dependencies:

```console
go get github.com/couchbase/gocb-opentelemetry
go get go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc
go get go.opentelemetry.io/otel/sdk/trace
```

Then configure the tracer:

```go
	ctx := context.Background()

	// Setup an exporter.
	// This exporter exports traces on the OTLP protocol over GRPC to localhost:4317.
	exporter, err := otlptracegrpc.New(ctx,
		otlptracegrpc.WithEndpointURL("http://localhost:4317"),
	)
	if err != nil {
		log.Fatal(err)
	}

	// Create the OpenTelemetry SDK's TracerProvider.
	tracerProvider := sdktrace.NewTracerProvider(
		sdktrace.WithResource(resource.NewWithAttributes(
			semconv.SchemaURL,
			// An OpenTelemetry service name generally reflects the name of your microservice,
			// e.g. "shopping-cart-service".
			semconv.ServiceNameKey.String("YOUR_SERVICE_NAME_HERE"),
		)),
		// The BatchSpanProcessor will efficiently batch traces and periodically export them.
		sdktrace.WithBatcher(exporter),
		// Export every trace: this may be too heavy for production.
		// An alternative is `sdktrace.WithSampler(sdktrace.TraceIDRatioBased(0.01))`
		sdktrace.WithSampler(sdktrace.AlwaysSample()),
	)
	defer tracerProvider.Shutdown(ctx)

	// Provide the TracerProvider to the Couchbase OpenTelemetry tracer wrapper.
	tracer := gocbopentelemetry.NewOpenTelemetryRequestTracer(tracerProvider)

	// Provide the OpenTelemetry tracer as part of the Cluster configuration.
	cluster, err := gocb.Connect("localhost", gocb.ClusterOptions{
		Authenticator: gocb.PasswordAuthenticator{
			Username: "Administrator",
			Password: "password",
		},
		Tracer: tracer,
	})
	if err != nil {
		log.Fatal(err)
	}
```

At this point the SDK will automatically be exporting spans, and you should see them in your receiver of choice.

### [](#opentelemetry-troubleshooting)OpenTelemetry Troubleshooting

* There are many ways to export spans. The example is exporting OpenTelemetry Protocol (OTLP) spans over GRPC to port 4317, which is the _de facto_ standard for OpenTelemetry. Make sure that your receiver is compatible with this, e.g. has these ports open and is ready to receive OTLP traffic over GRPC. With [Jaeger in Docker](https://www.jaegertracing.io/docs/1.41/getting-started/) this is achieved with the options `-e COLLECTOR_OTLP_ENABLED=true` and `-p 4317:4317`.
* The exporter used in this example is `BatchSpanProcessor` (via `sdktrace.WithBatcher`), which may not have a chance to export spans if the application exits very quickly (e.g. a test application). `sdktrace.WithSyncer` can be used instead for synchronous export, though it is not likely suitable for production.
* The example above uses `sdktrace.AlwaysSample()`, which exports every span. This may need to be reduced to avoid overwhelming the receiver, with e.g. `sdktrace.TraceIDRatioBased(0.01)` to sample 1% of all traces.
* It can be worth sending traces into [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/), and forwarding them on from there to your receiver of choice. Among other capabilities the collector can log traces it receives, making for easier debugging.

### [](#parent-spans)Parent Spans

If you want to set a parent for an SDK request, you can do it in the respective `*Options` struct. Wrap an existing OpenTelemetry span with `gocbopentelemetry.NewOpenTelemetryRequestSpan` and pass it as the `ParentSpan`:

```go
	// Create an OpenTelemetry span to use as a parent.
	otelCtx, parentOtelSpan := tracerProvider.Tracer("my-app").Start(ctx, "my-operation")
	defer parentOtelSpan.End()

	// Wrap it in a Couchbase RequestSpan and pass it as a parent to the SDK operation.
	parentSpan := gocbopentelemetry.NewOpenTelemetryRequestSpan(otelCtx, parentOtelSpan)

	result, err := col.Get("my-doc", &gocb.GetOptions{
		ParentSpan: parentSpan,
	})
```