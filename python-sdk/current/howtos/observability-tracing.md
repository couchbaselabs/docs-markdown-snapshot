---
title: Request Tracing
description: Collecting information about an individual request and its response
  is an essential feature of every observability stack.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/release/4.6/modules/howtos/pages/observability-tracing.adoc
  xref: xref:python-sdk:howtos:observability-tracing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/howtos/observability-tracing.html)

# Request Tracing

> Collecting information about an individual request and its response is an essential feature of every observability stack. 

To give insight into a request/response flow, the SDK provides a `RequestTracer` interface and ships with both a default implementation as well as modules that can be plugged into feed the traces to external systems (including OpenTelemetry).

## [](#the-default-thresholdloggingtracer)The Default ThresholdLoggingTracer

> [!NOTE]
> As of v4.6.0 the Threshold Logger is native to the Python SDK. In previous versions the underlying C++ core was responsible for all tracing related behaviour.

By default, the SDK will emit information about requests that are over a configurable threshold every 10 seconds. Note that if no requests are over the threshold no event / log will be emitted.

It is possible to customize this behavior by modifying the configuration:

```python
tracing_opts = ClusterTracingOptions(
    tracing_threshold_queue_flush_interval=timedelta(seconds=5),
    tracing_threshold_queue_size=10,
    tracing_threshold_kv=timedelta(milliseconds=500))

auth = PasswordAuthenticator("Administrator", "password")
cluster_opts = ClusterOptions(authenticator=auth, tracing_options=tracing_opts)

cluster = Cluster.connect("couchbase://your-ip", cluster_opts)
```

In this case the emit interval is 5 seconds and Key/Value requests will only be considered if their latency is greater or equal than 500 milliseconds.

The JSON blob emitted looks similar to the following (prettified here for readability):

```json
[
   {
      "top":[
         {
            "operation_name":"get",
            "server_us":2,
            "last_local_id":"E64FED2600000001/00000000EA6B514E",
            "last_local_address":"127.0.0.1:51807",
            "last_remote_address":"127.0.0.1:11210",
            "last_dispatch_us":2748,
            "last_operation_id":"0x9",
            "total_us":324653
         },
         {
            "operation_name":"get",
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

For each service (e.g. Key/Value or Query) an entry exists in the outer JSON array. The top N (10 by default) slowest operations are collected and displayed, sorted by the total duration. This promotes quick visibility of the "worst offenders" and more efficient troubleshooting.

Please note that in future releases this format is planned to change for easier readability, so we do not provide any stability guarantees on the logging output format and it might change between minor versions.

## [](#opentelemetry-integration)OpenTelemetry Integration

The built-in tracer is great if you do not have a centralized monitoring system, but if you already plug into the OpenTelemetry ecosystem we want to make sure to provide first-class support.

### [](#exporting-to-opentelemetry)Exporting to OpenTelemetry

This method exports tracing telemetry in OpenTelemetry's standard format (OTLP), which can be sent to any OTLP-compatible receiver such as Jaeger, Zipkin, or `opentelemetry-collector`.

To do this, install the required Python libraries for OpenTelemetry:

> [!NOTE]
> The Python SDK allows for the OpenTelemetry API and SDK packages to be installed along with the SDK via `python3 -m pip install couchbase[otel]`.

```console
$ python3 -m pip install opentelemetry-api~=1.22, opentelemetry-sdk~=1.22
```

And now:

```python
# create service resource
resource = Resource.create(attributes={
    "service.name": SERVICE_NAME,
    "service.version": "1.0.0",
})

# Create the Provider
tracer_provider = TracerProvider(resource=resource, sampler=ALWAYS_ON)  # Sample all traces for demo purposes

# setup an exporter
# This exporter exports traces on the OTLP protocol over GRPC to localhost:4317.
exporter = OTLPSpanExporter(
    endpoint='localhost:4317',
    insecure=True
)

# Attach the exporter to a Batch Processor
span_processor = BatchSpanProcessor(exporter)
tracer_provider.add_span_processor(span_processor)

# Set the global provider
trace.set_tracer_provider(tracer_provider)

# create the SDK's tracer
# required import: from couchbase.observability.otel_tracing import get_otel_tracer
couchbase_tracer = get_otel_tracer(tracer_provider)

# pass the tracer to the Couchbase SDK via ClusterOptions
opts = ClusterOptions(
    PasswordAuthenticator(USERNAME, PASSWORD),
    tracer=couchbase_tracer,
)

cluster = Cluster.connect('couchbase://localhost', opts)
```

At this point the SDK will automatically be exporting spans, and you should see them in your receiver of choice.

Create file `docker-compose.yml`:

```yaml
services:
  jaeger:
    image: jaegertracing/all-in-one:latest
    environment:
      - COLLECTOR_OTLP_ENABLED=true
    ports:
      - "4317:4317"   # OTLP gRPC receiver
      - "16686:16686" # Jaeger UI
```

Now start up Jaeger with OTLP support:

```console
$ docker-compose up -d
```

Now run the application. All being well, spans should display in Jaeger (the UI is available on <http://localhost:16686>) under the service that matches what was used for the `service.name` attribute in the application.

### [](#opentelemetry-troubleshooting)OpenTelemetry Troubleshooting

* There are many ways to export spans. The example is exporting OpenTelemetry Protocol (OTLP) spans over GRPC to port 4317, which we believe is the _de facto_ standard for OpenTelemetry. Make sure that your receiver is compatible with this, e.g. has these ports open and is ready to receive OTLP traffic over GRPC. With [Jaeger in Docker](https://www.jaegertracing.io/docs/1.41/getting-started/) this is achieved with the options `-e COLLECTOR_OTLP_ENABLED=true` and `-p 4317:4317`.
* The exporter used in this example is `BatchSpanProcessor`, which may not have a chance to export spans if the application exits very quickly (e.g. a test application). `SimpleSpanProcessor` can be used instead, though is not likely suitable for production.
* The example above uses `sampler=ALWAYS_ON`, which exports every span. This may need to be reduced to avoid overwhelming the receiver, with e.g. `sampler=TraceIdRatioBased(0.01)` to sample 1% of all traces.
* It can be worth sending traces into [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/), and forwarding them on from there to your receiver of choice. Among other capabilities the collector can log traces it receives, making for easier debugging.

### [](#parent-spans)Parent spans

If you want to set a parent for a SDK request, you can do it in the respective `*Options`:

```python
with app_tracer.start_as_current_span("operations") as parent_span:
    result = collection.get("my-doc", GetOptions(parent_span=parent_span))
```