---
title: Request Tracing
description: Collecting information about an individual request and its response
  is an essential feature of every observability stack.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/observability-tracing.adoc
  xref: xref:rust-sdk:howtos:observability-tracing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/howtos/observability-tracing.html)

# Request Tracing

> Collecting information about an individual request and its response is an essential feature of every observability stack. 

The SDK instruments all operations with [tracing](https://docs.rs/tracing/latest/tracing/struct.Span.html) spans. These can be consumed by any compatible [tracing-subscriber Layer](https://docs.rs/tracing-subscriber/latest/tracing%5Fsubscriber/layer/index.html), including the shipped `ThresholdLoggingTracer`which logs the slowest operations exceeding configurable per-service latency thresholds, or an OpenTelemetry backend via the [tracing-opentelemetry](https://docs.rs/tracing-opentelemetry/latest/tracing%5Fopentelemetry/) bridge.

All SDK spans are emitted at `trace` level under the `couchbase::tracing` target.

## [](#the-thresholdloggingtracer)The ThresholdLoggingTracer

The `ThresholdLoggingTracer` is a tracing\_subscriber Layer that collects completed operations and periodically emits a JSON report of the slowest ones that exceeded configurable per-service thresholds.

By default, the SDK emits information about requests that are over a configurable threshold every 10 seconds. Note that if no requests are over the threshold, no logs will be emitted.

Set up your `Cargo.toml` dependencies:

```toml
[dependencies]
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["fmt"] }
```

The simplest setup registers `ThresholdLoggingTracer` together with a `fmt` layer for general log output. This must be called within a Tokio runtime:

```rust
#[tokio::main]
async fn main() {
    use std::time::Duration;
    use couchbase::threshold_logging_tracer::{ThresholdLoggingTracer, ThresholdLoggingOptions};
    use tracing_subscriber::layer::SubscriberExt;

    let tracer = ThresholdLoggingTracer::new(Some(
        ThresholdLoggingOptions::new()
            .kv_threshold(Duration::from_millis(1000))
            .emit_interval(Duration::from_secs(60))
            .sample_size(5),
    ));
    let subscriber = tracing_subscriber::registry()
        .with(tracing_subscriber::fmt::layer())
        .with(tracer);

    tracing::subscriber::set_global_default(subscriber)
        .expect("Failed to set global tracing subscriber");
    // ...
}
```

The JSON blob emitted looks similar to the following (prettified here for readability):

```json
{
   "kv": {
      "total_count": 2,
      "top_requests": [
         {
            "total_duration_us": 13333,
            "last_dispatch_duration_us": 13112,
            "total_dispatch_duration_us": 13112,
            "operation_name": "get",
            "last_local_id": "80d81672-0a71-4ab6-8667-80c0f16d3710",
            "last_remote_socket": "192.168.106.129:11210"
         },
         {
            "total_duration_us": 6252,
            "encode_duration_us": 10,
            "last_dispatch_duration_us": 6159,
            "total_dispatch_duration_us": 6159,
            "operation_name": "upsert",
            "last_local_id": "4e459355-9550-45fb-b5f4-ea71f5d4d613",
            "last_remote_socket": "192.168.106.130:11210"
         }
      ]
   }
}
```

For each service (e.g. Key/Value or Query) an entry exists in the outer JSON array. The top N (10 by default) slowest operations are collected and displayed, sorted by the total duration. This promotes quick visibility of the "worst offenders" and more efficient troubleshooting.

**Note:** The stability of this output format is `Uncommitted` and may change between minor versions.

__Table 1\. ThresholdLoggingOptions Properties__
| Property              | Default    | Description                                                       |
| --------------------- | ---------- | ----------------------------------------------------------------- |
| emit\_interval        | 10 seconds | How often the tracer emits the threshold report.                  |
| kv\_threshold         | 500 ms     | Minimum duration for a KV operation to be included.               |
| query\_threshold      | 1 second   | Minimum duration for a Query operation to be included.            |
| search\_threshold     | 1 second   | Minimum duration for a FTS operation to be included.              |
| management\_threshold | 1 second   | Minimum duration for a Management operation to be included.       |
| sample\_size          | 10         | Maximum number of operations to include per service per interval. |

## [](#otel)OpenTelemetry Integration

The Rust tracing ecosystem integrates with OpenTelemetry via the [tracing-opentelemetry](https://crates.io/crates/tracing-opentelemetry) crate. This bridges `tracing` spans to any OpenTelemetry-compatible receiver such as Jaeger, Zipkin, or `opentelemetry-collector`.

### [](#exporting-to-opentelemetry)Exporting to OpenTelemetry

Add the relevant dependencies to your `Cargo.toml`:

```toml
[dependencies]
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["fmt"] }
tracing-opentelemetry = "0.32"
opentelemetry = "0.31"
opentelemetry_sdk = "0.31"
opentelemetry-otlp = { version = "0.31", features = ["grpc-tonic"] }
```

Configure the OpenTelemetry pipeline and set up your OpenTelemetryLayer:

```rust
use std::time::Duration;
use couchbase::authenticator::PasswordAuthenticator;
use couchbase::cluster::Cluster;
use couchbase::options::cluster_options::ClusterOptions;
use opentelemetry::KeyValue;
use opentelemetry::trace::TracerProvider;
use opentelemetry_sdk::{
    trace::{BatchSpanProcessor, Sampler, SdkTracerProvider},
    Resource,
};
use opentelemetry_otlp::{Protocol, SpanExporter, WithExportConfig};
use tracing::instrument::WithSubscriber;
use tracing_subscriber::{layer::SubscriberExt, Registry};
use tracing_opentelemetry::OpenTelemetryLayer;

#[tokio::main]
async fn main() {
    let tracer_provider = setup_otel_tracer_provider();
    let tracer = tracer_provider.tracer("my-app");

    let subscriber = Registry::default()
        .with(OpenTelemetryLayer::new(tracer))
        .with(tracing_subscriber::fmt::layer()); // Add any other layers you want

    // Scope the subscriber to your SDK calls.
    // Alternatively, register it globally with:
    //   tracing::subscriber::set_global_default(subscriber)
    // Note: with a global subscriber, all spans in the process will share the same
    // instrumentation scope name.
    your_couchbase_sdk_calls()
        .with_subscriber(subscriber)
        .await;
}

fn setup_otel_tracer_provider() -> SdkTracerProvider {
    // This exporter exports traces on the OTLP protocol over GRPC to localhost:4317.
    let exporter = SpanExporter::builder()
        .with_tonic()
        .with_protocol(Protocol::Grpc)
        .with_endpoint("http://localhost:4317")
        .build()
        .expect("failed to build OTLP exporter");

    let resource = Resource::builder()
        // An OpenTelemetry service name generally reflects the name of your microservice,
        // e.g. "shopping-cart-service".
        .with_attributes([
            KeyValue::new("service.name", "YOUR_SERVICE_NAME_HERE"),
        ])
        .build();

    let tracer_provider = SdkTracerProvider::builder()
        .with_resource(resource)
        // Export every trace: this may be too heavy for production.
        // An alternative is `.with_sampler(Sampler::TraceIdRatioBased(0.01))`
        .with_sampler(Sampler::AlwaysOn)
        // The BatchSpanProcessor will efficiently batch traces and periodically export them.
        .with_span_processor(
            BatchSpanProcessor::builder(exporter)
                .with_batch_config(
                    opentelemetry_sdk::trace::BatchConfigBuilder::default()
                        .with_scheduled_delay(Duration::from_millis(5000))
                        .build(),
                )
                .build(),
        )
        .build();

    tracer_provider
}

async fn your_couchbase_sdk_calls() {
    // Your Couchbase SDK calls here, e.g.:
    let opts = ClusterOptions::new(PasswordAuthenticator::new("username", "password").into());
    let cluster = Cluster::connect("couchbase://localhost", opts).await.unwrap();
    let bucket = cluster.bucket("my_bucket");
    let collection = bucket.default_collection();
    collection.insert("my_key", "my_value", None).await.unwrap();
}
```

> [!NOTE]
> You can also register the subscriber with `tracing::subscriber::set_global_default(subscriber)`. However, `tracing-opentelemetry` attaches a single `SdkTracer`, so all tracing spans in the process will share this tracer.

### [](#opentelemetry-troubleshooting)OpenTelemetry Troubleshooting

* There are many ways to export spans. The example is exporting OpenTelemetry Protocol (OTLP) spans over GRPC to port 4317, which we believe is the _de facto_ standard for OpenTelemetry. Make sure that your receiver is compatible with this, e.g. has these ports open and is ready to receive OTLP traffic over GRPC. With [Jaeger in Docker](https://www.jaegertracing.io/docs/1.41/getting-started/) this is achieved with the options `-e COLLECTOR_OTLP_ENABLED=true` and `-p 4317:4317`.
* The exporter used in this example is `BatchSpanProcessor`, which may not have a chance to export spans if the application exits very quickly (e.g. a test application). `SimpleSpanProcessor` can be used instead, though is not suitable for most production use cases.
* The example above uses `Sampler.alwaysOn()`, which exports every span. This may need to be reduced to avoid overwhelming the receiver, with e.g. `Sampler.traceIdRatioBased(0.01)` to sample 1% of all traces.
* It can be worth sending traces into [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/), and forwarding them on from there to your receiver of choice. Among other capabilities the collector can log traces it receives, making for easier debugging.

## [](#parent-spans)Parent spans

Because the SDK uses the `tracing` crate for instrumentation, parent span context is inherited automatically. Any SDK call made while a `tracing` span is entered will nest its spans beneath it.

In synchronous code this happens naturally when the span is entered in the same thread. In async code, however, futures can be polled across different tasks, so you need to attach the span explicitly using the [Instrument](https://docs.rs/tracing/latest/tracing/trait.Instrument.html) trait:

```rust
use tracing::Instrument;

let parent_span = tracing::info_span!("my-parent-span");

let result = collection
    .get("my-doc-id", GetOptions::default())
    .instrument(parent_span)
    .await?;
```

`.instrument()` moves the span into the future, entering and exiting it each time the future is polled. This ensures SDK spans emitted during the `get` call appear as children of `parent_span` in whatever backend is configured.