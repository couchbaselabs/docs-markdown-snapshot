---
title: Logging
description: The Rust SDK logs events via the `tracing` crate.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/collecting-information-and-logging.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:rust-sdk:howtos:collecting-information-and-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/howtos/collecting-information-and-logging.html)

# Logging

> The Rust SDK logs events via the \`tracing\` crate. It has no hard dependency on a specific logger implementation, but setting up [tracing-subscriber](https://docs.rs/tracing-subscriber/latest/tracing%5Fsubscriber/) is recommended. 

## [](#configuring-logging)Configuring Logging

The Couchbase Rust SDK emits all log messages as [tracing](https://docs.rs/tracing/latest/tracing/) events. It also enables the [log compatibility feature](https://docs.rs/tracing/latest/tracing/#emitting-log-records), which means any logger configured via the [log](https://docs.rs/log/latest/log/) crate (such as `env_logger`) will also receive SDK log messages. However, setting up a [tracing-subscriber](https://docs.rs/tracing-subscriber/latest/tracing%5Fsubscriber/) directly is the recommended approach as it allows you to leverage the tracing spans and metrics the SDK emits.

### [](#recommended-setup-with-tracing-subscriber)Recommended setup with tracing-subscriber

Add the following to your `Cargo.toml`:

```toml
[dependencies]
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["env-filter", "fmt"] }
```

Then register a subscriber before connecting to Couchbase:

```rust
#[tokio::main]
async fn main() {
    use tracing_subscriber::{layer::SubscriberExt, EnvFilter};
    use couchbase::logging_meter::LoggingMeter;
    use couchbase::threshold_logging_tracer::ThresholdLoggingTracer;

    let filter = EnvFilter::try_from_default_env()
        .unwrap_or_else(|_| {
            EnvFilter::new("info")
        });

    let subscriber = tracing_subscriber::registry()
        .with(ThresholdLoggingTracer::new(None)) // Enables periodic slow operation logging
        .with(LoggingMeter::new(None)) // Enables periodic operation metrics logging
        .with(tracing_subscriber::fmt::layer().with_filter(filter));

    tracing::subscriber::set_global_default(subscriber)
        .expect("Failed to set global tracing subscriber");
}
```

> [!NOTE]
> The above setup also enables the [ThresholdLoggingTracer](observability-tracing.md) and [LoggingMeter](observability-metrics.md), these are optional, however it is highly recommended that these are enabled if you are not using any other tracers or meters to help aid with debugging.

With this setup you can control verbosity at runtime via the `RUST_LOG` environment variable:

```console
$ RUST_LOG='couchbase=debug' cargo run
```

### [](#alternative-log-compatible-loggers)Alternative: 'log' compatible loggers

If you prefer to stay with the [log](https://docs.rs/log/latest/log/) ecosystem, the SDK has the [log](https://docs.rs/tracing/latest/tracing/#crate-feature-flags) feature of the tracing crate enabled, meaning that any logger which consumes `log` records, such as the `env_logger` will work without any extra configuration:

```toml
[dependencies]
env_logger = "0.11"
```

```rust
env_logger::init();
```

Set `RUST_LOG` to control verbosity:

```console
$ RUST_LOG='couchbase=debug' cargo run
```

> [!TIP]
> In addition to the special targets mentioned below, when logging at 'trace' level with the `log` compatible loggers, you may wish to also filter out the `tracing::span` target, which logs each time spans are entered and exited, as this can add a lot of noise to the logs.

### [](#special-targets)Special log targets

The SDK emits events under two special targets that deserve attention:

`couchbase::tracing`

The SDK orchestrates `tracing` [spans](https://docs.rs/tracing/latest/tracing/span/index.html) to this target at trace level. Filter this target off on your logger if you don’t want span noise in your log output. Note that this target _is_ still needed if you have any layers consuming SDK spans, such as the [ThresholdLoggingTracer or OpenTelemetry layer](observability-tracing.md) in your subscriber stack — `EnvFilter` filtering can be done per-layer, so other layers can still receive them.

`couchbase::metrics`

Internal metrics events intended exclusively for metrics backends such as the [LoggingMeter or OpenTelemetry MetricsLayer](observability-metrics.md). These are emitted at `trace` level only and produce no useful output in plain log format, so it is recommended to configure your logger to turn this off.