---
title: Metrics Reporting
description: Individual request tracing presents a very specific (though
  isolated) view of the system.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.9/modules/howtos/pages/observability-metrics.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/java-sdk/3.9/howtos/observability-metrics.html)

# Metrics Reporting

> Individual request tracing presents a very specific (though isolated) view of the system. In addition, it also makes sense to capture information that aggregates request data (i.e. requests per second), but also data which is not tied to a specific request at all (i.e. resource utilization). 

The SDK exposes metrics for operation durations, broken down into p50, p90, p99, p99.9, and p100 percentiles.

These metrics can either be logged periodically into the application logs, using the `LoggingMeter` (this is the default behaviour).

Or, sent into the OpenTelemetry or Micrometer libraries, where they can be sent on to the user’s metrics infrastructure — such as Prometheus.

## [](#the-default-loggingmeter)The Default LoggingMeter

The default implementation aggregates and logs request and response metrics.

By default the metrics will be emitted every 10 minutes, but you can customize the emit interval as well:

```java
ClusterEnvironment environment = ClusterEnvironment.builder()
        .loggingMeterConfig(config -> config.enabled(true).emitInterval(Duration.ofSeconds(30)))
        .build();
```

Once enabled, there is no further configuration needed. The `LoggingMeter` will emit the collected request statistics every interval. A possible report looks like this (prettified for better readability):

```json
{
   "meta":{
      "emit_interval_s":10
   },
   "query":{
      "127.0.0.1":{
         "total_count":9411,
         "percentiles_us":{
            "50.0":544.767,
            "90.0":905.215,
            "99.0":1589.247,
            "99.9":4095.999,
            "100.0":100663.295
         }
      }
   },
   "kv":{
      "127.0.0.1":{
         "total_count":9414,
         "percentiles_us":{
            "50.0":155.647,
            "90.0":274.431,
            "99.0":544.767,
            "99.9":1867.775,
            "100.0":574619.647
         }
      }
   }
}
```

Each report contains one object for each service that got used and is further separated on a per-node basis so they can be analyzed in isolation.

For each service / host combination, a total amount of recorded requests is reported, as well as percentiles from a histogram in microseconds. The meta section on top contains information such as the emit interval in seconds so tooling can later calculate numbers like requests per second.

The `LoggingMeter` can be configured on the environment as shown above. The following table shows the currently available properties:

__Table 1\. LoggingMeterConfig Properties__
| Property     | Default     | Description                                   |
| ------------ | ----------- | --------------------------------------------- |
| enabled      | false       | If the LoggingMeter should be enabled.        |
| emitInterval | 600 seconds | The interval where found orphans are emitted. |

## [](#opentelemetry-integration)OpenTelemetry Integration

The SDK supports plugging in any `OpenTelemetry` metrics consumer instead of using the default `LoggingMeter`.

To do this, first add this to your Maven, or the equivalent to your build tool of choice:

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-bom</artifactId>
            <version>1.17.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>metrics-opentelemetry</artifactId>
        <version>0.4.4</version>
    </dependency>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-api</artifactId>
    </dependency>
    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-sdk</artifactId>
    </dependency>
</dependencies>
```

In addition, you’ll need to get the metrics data into your metrics backend. This is often done by having the metrics backend (such as Prometheus) regularly gather, or 'scrape', the metrics data.

There are multiple approaches here. The `opentelemetry-exporter-prometheus` library makes it possible to open an HTTP server in the application that Prometheus can then scape.

As that library is in alpha, here we will instead show how to send OpenTelemetry metrics into `opentelemetry-collector`, where it can be scraped by Prometheus or another metrics backend.

This aligns well with tracing, where a recommended approach is also to send OpenTelemetry spans into `opentelemetry-collector`, where they can be processed and forwarded elsewhere. See [the Request Tracing documentation](observability-tracing.md) for more information.

For metrics, add this logic to the application:

```java
// Setup an exporter.
// This exporter exports traces on the OTLP protocol over GRPC to localhost:4317.
MetricExporter exporter = OtlpGrpcMetricExporter.builder()
        .setCompression("gzip")
        .setEndpoint("http://localhost:4317")
        .build();

// Create the OpenTelemetry SDK's SdkMeterProvider.
SdkMeterProvider sdkMeterProvider = SdkMeterProvider.builder()
        .setResource(Resource.getDefault()
                .merge(Resource.builder()
                        // An OpenTelemetry service name generally reflects the name of your microservice,
                        // e.g. "shopping-cart-service".
                        .put("service.name", "YOUR_SERVICE_NAME_HERE")
                        .build()))
        // Operation durations are in nanoseconds, which are too large for the default OpenTelemetry histogram buckets.
        .registerView(InstrumentSelector.builder().setType(InstrumentType.HISTOGRAM).build(),
                View.builder().setAggregation(Aggregation.explicitBucketHistogram(List.of(
                        100000.0,
                        250000.0,
                        500000.0,
                        1000000.0,
                        10000000.0,
                        100000000.0,
                        1000000000.0,
                        10000000000.0))).build())
        .registerMetricReader(PeriodicMetricReader.builder(exporter).setInterval(Duration.ofSeconds(1)).build())
        .build();

// Create the OpenTelemetry SDK's OpenTelemetry object.
OpenTelemetry openTelemetry = OpenTelemetrySdk.builder()
        .setMeterProvider(sdkMeterProvider)
        .buildAndRegisterGlobal();

// Provide the OpenTelemetry object as part of the Cluster configuration.
Cluster cluster = Cluster.connect(hostname, ClusterOptions.clusterOptions(username, password)
        .environment(env -> env.meter(OpenTelemetryMeter.wrap(openTelemetry))));
```

At this point the SDK is hooked up with the OpenTelemetry metrics and will emit them to the exporter.

A `db.couchbase.operations` histogram is exported, which will appear in Prometheus as `db_couchbase_operations`.

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
  logging:
    loglevel: debug
  prometheus:
    endpoint: '0.0.0.0:10000'

service:
  pipelines:
    metrics:
      receivers: [otlp]
      processors: []
      exporters: [prometheus, logging]
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

Now run the application. All being well, `opentelemetry-collector` should regularly log that it’s receiving the `db.couchbase.operations` metric, as it has been configured with a `logging` exporter.

And Prometheus (the UI is available on <http://localhost:9090>) should allow querying for `db_couchbase_operations`. (Though a real deployment will generally use another tool, such as Grafana, for visualisation.)

If this fails, check <http://localhost:9090/api/v1/targets> to see if Prometheus is unable to contact `opentelemetry-collector`.

## [](#micrometer-integration)Micrometer Integration

In addition to OpenTelemetry, we also provide a module allowing SDK metrics to be integrated into Micrometer.

To do this, first add this to your Maven, or the equivalent to your build tool of choice:

```xml
<dependency>
    <groupId>com.couchbase.client</groupId>
    <artifactId>metrics-micrometer</artifactId>
    <version>0.4.4</version>
</dependency>
<dependency>
    <groupId>io.prometheus</groupId>
    <artifactId>simpleclient</artifactId>
    <version>0.16.0</version>
</dependency>
<dependency>
    <groupId>io.prometheus</groupId>
    <artifactId>simpleclient_httpserver</artifactId>
    <version>0.16.0</version>
</dependency>
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-registry-prometheus</artifactId>
    <version>1.10.5</version>
</dependency>
<!-- Gives improved histograms for Micrometer when on classpath -->
<dependency>
    <groupId>org.hdrhistogram</groupId>
    <artifactId>HdrHistogram</artifactId>
    <version>2.1.12</version>
</dependency>
```

You can now create a Micrometer registry and pass it into the SDK. Here we’re using a Prometheus Micrometer registry, and setting up an HTTP server inside the application that will run on port 10000 and which Prometheus can scrape.

But Micrometer of course, like OpenTelemetry, can support many more metrics backends than Prometheus. See the Micrometer documentation for details.

```java
PrometheusMeterRegistry prometheusRegistry = new PrometheusMeterRegistry(PrometheusConfig.DEFAULT);

// Micrometer won't create a histogram by default, configure that.
prometheusRegistry.config().meterFilter(
        new MeterFilter() {
            @Override
            public DistributionStatisticConfig configure(Meter.Id id, DistributionStatisticConfig config) {
                if (id.getType() == Meter.Type.DISTRIBUTION_SUMMARY) {
                    return DistributionStatisticConfig.builder()
                            .percentilesHistogram(true)
                            .build()
                            .merge(config);
                }
                return config;
            }
        });

// Setup an HTTP server running on port 10000 that Prometheus can scrape for Micrometer metrics.
new HTTPServer(new InetSocketAddress(10000), prometheusRegistry.getPrometheusRegistry(), true);

// Provide the Micrometer registry as part of the Cluster configuration.
Cluster cluster = Cluster.connect(hostname, ClusterOptions.clusterOptions(username, password)
        .environment(env -> env.meter(MicrometerMeter.wrap(prometheusRegistry))));
```

At this point the metrics are hooked up to Micrometer, and ready to be scraped by Prometheus. See the OpenTelemetry documentation above for what metrics to expect.

### [](#testing-2)Testing

For convenience, here is a simple Docker-based Prometheus configuration for localhost testing of a Micrometer metrics setup.

Create file `prometheus.yaml`:

```none
scrape_configs:
  - job_name: 'otel-collector'

    scrape_interval: 1s

    static_configs:
      - targets: ['host.docker.internal:10000']
        labels:
          group: 'production'
```

Now run Prometheus:

```none
docker run --rm --name prometheus -p 9090:9090  --mount type=bind,source="${PWD}/prometheus.yaml,destination=/etc/prometheus/prometheus.yml" prom/prometheus
```

Note the Prometheus config uses `host.docker.internal` to connect from a Docker container to the application running on localhost. This will not work on all Docker deployments — see the Docker documentation for more information on connecting to localhost.

Now run the application.

All being well, Prometheus (the UI is available on <http://localhost:9090>) should allow querying for `db_couchbase_operations_buckets`. (Though a real deployment will generally use another tool, such as Grafana, for visualization.)

If this fails, check <http://localhost:9090/api/v1/targets> to see if Prometheus is unable to contact the application.