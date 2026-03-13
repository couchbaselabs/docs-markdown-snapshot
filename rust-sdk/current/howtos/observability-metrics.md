---
title: Metrics Reporting
description: Individual request tracing presents a very specific (though
  isolated) view of the system.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/observability-metrics.adoc
pubDate: 2026-03-13T03:41:17.220Z
link: xref:rust-sdk:howtos:observability-metrics.adoc[]
---

[View original HTML](/rust-sdk/current/howtos/observability-metrics.html)

# Metrics Reporting

> Individual request tracing presents a very specific (though isolated) view of the system. In addition, it also makes sense to capture information that aggregates request data (i.e. requests per second), but also data which is not tied to a specific request at all (i.e. resource utilization). 

The SDK exposes metrics for operation durations, broken down into p50, p90, p99, p99.9, and p100 percentiles, reported per service and per operation type.

SDK metrics are reported via a tracing event on the `couchbase::metrics` target, which can be consumed by any compatible [tracing\_subscriber::Layer](https://docs.rs/tracing-subscriber/latest/tracing%5Fsubscriber/layer/trait.Layer.html). The SDK ships the `LoggingMeter` layer which periodically logs them as JSON into the application’s `tracing` output.

Both `LoggingMeter` and `ThresholdLoggingTracer` (see [Request Tracing](observability-tracing.md)) are layers that can be composed on a single tracing [Subscriber](https://docs.rs/tracing-core/0.1.35/tracing%5Fcore/subscriber/trait.Subscriber.html), alongside any other layers such as `tracing_subscriber::fmt::layer()`.

## [](#the-loggingmeter)The LoggingMeter

`LoggingMeter` is a `tracing_subscriber::Layer` that collects per-operation latency histograms and emits a JSON report on a configurable interval. If no other meters are enabled then it is **strongly** advised that you enable this by default to aid with debugging, along with the `ThresholdLoggingTracer`

Set up your `Cargo.toml` dependencies:

```toml
[dependencies]
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["fmt"] }
```

The simplest setup registers `LoggingMeter` together with an `fmt` layer for general log output. This must be called within a Tokio runtime:

```rust
#[tokio::main]
async fn main() {
    use std::time::Duration;
    use couchbase::logging_meter::{LoggingMeter, LoggingMeterOptions};
    use tracing_subscriber::layer::SubscriberExt;

    let meter = LoggingMeter::new(Some(
        LoggingMeterOptions::new().emit_interval(Duration::from_secs(300)),
    ));
    let subscriber = tracing_subscriber::registry()
        .with(meter)
        .with(tracing_subscriber::fmt::layer()); // Add any other layers you want, e.g. fmt for logging, ThresholdLoggingTracer, etc.

    tracing::subscriber::set_global_default(subscriber)
        .expect("Failed to set global tracing subscriber");
    // ...
}
```

Once registered, the `LoggingMeter` will emit the collected request statistics every interval.

A possible report looks like this (prettified for readability):

```json
{
   "meta": {
      "emit_interval_s": 600
   },
   "operations": {
      "query": {
         "query": {
            "total_count": 9411,
            "percentiles_us": {
               "50.0": 544,
               "90.0": 905,
               "99.0": 1589,
               "99.9": 4095,
               "100.0": 100663
            }
         }
      },
      "kv": {
         "get": {
            "total_count": 9414,
            "percentiles_us": {
               "50.0": 155,
               "90.0": 274,
               "99.0": 544,
               "99.9": 1867,
               "100.0": 574619
            }
         },
         "upsert": {
            "total_count": 2100,
            "percentiles_us": {
               "50.0": 120,
               "90.0": 210,
               "99.0": 480,
               "99.9": 1200,
               "100.0": 48000
            }
         }
      }
   }
}
```

Each report contains one object for each service that got used.

For each operation, a total amount of recorded requests is reported, as well as percentiles from a histogram in microseconds. The meta section on top contains information such as the emit interval in seconds so tooling can later calculate numbers like requests per second.

The `LoggingMeter` can be configured on the environment as shown above. The following table shows the currently available properties:

__Table 1\. LoggingMeterOptions Properties__
| Property       | Default     | Description                                                 |
| -------------- | ----------- | ----------------------------------------------------------- |
| emit\_interval | 600 seconds | How often the meter will emit the collected metrics report. |

## [](#otel)OpenTelemetry Integration

The Rust tracing ecosystem integrates with OpenTelemetry via the [tracing-opentelemetry](https://crates.io/crates/tracing-opentelemetry) crate, OpenTelemetry metrics are supported with the SDK via the [MetricsLayer](https://docs.rs/tracing-opentelemetry/latest/tracing%5Fopentelemetry/struct.MetricsLayer.html)which bridges SDK metrics to any OpenTelemetry-compatible backend (Prometheus, Grafana, Datadog, etc.).

Add the relevant dependencies to your `Cargo.toml`:

```toml
[dependencies]
tracing-subscriber = { version = "0.3", features = ["fmt"] }
tracing-opentelemetry = "0.32"
opentelemetry = "0.31"
opentelemetry_sdk = "0.31"
opentelemetry-otlp = { version = "0.31", features = ["grpc-tonic", "gzip-tonic"] }
```

Then configure the OpenTelemetry pipeline and add its layer to your subscriber stack alongside any other layers:

```rust
use std::time::Duration;
use opentelemetry::KeyValue;
use opentelemetry_sdk::{
    metrics::{SdkMeterProvider, PeriodicReader, Instrument, Stream},
    Resource,
};
use opentelemetry_otlp::{MetricExporter, Protocol, WithExportConfig};
use opentelemetry_otlp::WithTonicConfig;
use tracing_subscriber::layer::SubscriberExt;
use tracing_opentelemetry::MetricsLayer;
use tracing::instrument::WithSubscriber;
use couchbase::cluster::Cluster;
use couchbase::options::cluster_options::ClusterOptions;
use couchbase::authenticator::PasswordAuthenticator;

#[tokio::main]
async fn main() {
    let meter_provider = setup_otel_meter_provider();

    let subscriber = tracing_subscriber::registry()
        .with(MetricsLayer::new(meter_provider))
        .with(tracing_subscriber::fmt::layer()); // Add any other layers you want

    // Scope the subscriber to your SDK calls.
    // Alternatively, register it globally with:
    // tracing::subscriber::set_global_default(subscriber)
    your_couchbase_sdk_calls()
        .with_subscriber(subscriber)
        .await;
}

fn setup_otel_meter_provider() -> SdkMeterProvider {
    // Set up an exporter.
    // This exporter exports traces on the OTLP protocol over GRPC to localhost:4317.
    let exporter = MetricExporter::builder()
        .with_tonic()
        .with_protocol(Protocol::Grpc)
        .with_endpoint("http://localhost:4317")
        .with_compression(opentelemetry_otlp::Compression::Gzip)
        .build()
        .expect("failed to build OTLP metric exporter");

    // Export metrics every second
    let reader = PeriodicReader::builder(exporter)
        .with_interval(Duration::from_secs(1))
        .build();

    let resource = Resource::builder()
        // An OpenTelemetry service name generally reflects the name of your microservice,
        // e.g. "shopping-cart-service".
        .with_attributes([
            KeyValue::new("service.name", "YOUR_SERVICE_NAME_HERE"),
        ])
        .build();

    // Optional workaround for https://github.com/tokio-rs/tracing-opentelemetry/issues/254
    // This ensures the units of the metrics the SDK emits are set correctly to seconds.
    let unit_view = |inst: &Instrument| -> Option<Stream> {
        match inst.name() {
            "db.client.operation.duration" => {
                Stream::builder()
                    .with_unit("s")
                    .build()
                    .ok()
            }
            _ => None,
        }
    };

    let meter_provider = SdkMeterProvider::builder()
        .with_resource(resource)
        .with_reader(reader)
        .with_view(unit_view)
        .build();

    meter_provider
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

At this point the SDK is hooked up with the OpenTelemetry metrics and will emit them to the exporter.

A `db.client.operation.duration` histogram is exported, which will appear in Prometheus as `db_client_operation_duration`.

It has these tags: `db.couchbase.service` ("kv", "query", etc.) and `db.operation` ("upsert", "query", etc.)

### [](#testing)Testing

For convenience, here is a simple Docker-based configuration of `opentelemetry-collector` and Prometheus for localhost testing of an OpenTelemetry setup.

Create file `otel.yaml`:

```none
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: '0.0.0.0:4317'
      http:
        endpoint: '0.0.0.0:4318'

exporters:
  debug:
    verbosity: detailed
  prometheus:
    endpoint: '0.0.0.0:10000'

service:
  pipelines:
    metrics:
      receivers: [ otlp ]
      processors: [ ]
      exporters: [ prometheus, debug ]
```

And file `prometheus.yaml`:

```none
scrape_configs:
  - job_name: 'otel-collector'

    scrape_interval: 1s

    static_configs:
      - targets: ['otel:10000']
        labels:
          group: 'production'
```

Now run `opentelemetry-collector` and Prometheus:

```none
docker network create shared
docker run --rm --name otel -v "${PWD}/otel.yaml:/etc/otel-local-config.yaml" -p 4317:4317 -p 10000:10000 --network shared otel/opentelemetry-collector --config /etc/otel-local-config.yaml
docker run --rm --name prometheus -p 9090:9090  --mount type=bind,source="${PWD}/prometheus.yaml,destination=/etc/prometheus/prometheus.yml" --network shared prom/prometheus
```

Some things to note:

* The containers are put on the same network so they can refer to each other by container name.
* The app has been told to export metrics over OLTP GRPC to localhost:4317\. `opentelemetry-collector` is listening to this.
* `opentelemetry-collector` will store the metrics, and exposes port 10000 for Prometheus to periodically scrape.

Now run the application. All being well, `opentelemetry-collector` should regularly log that it’s receiving the `db.client.operation.duration` metric, as it has been configured with a `debug` exporter.

And Prometheus (the UI is available on <http://localhost:9090>) should allow querying for `db_client_operation_duration`. (Though a real deployment will generally use another tool, such as Grafana, for visualisation.)

If this fails, check <http://localhost:9090/api/v1/targets> to see if Prometheus is unable to contact `opentelemetry-collector`.