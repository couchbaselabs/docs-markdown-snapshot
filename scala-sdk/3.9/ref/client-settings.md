---
title: Client Settings
description: The <code>ClusterEnvironment</code> class enables you to configure
  Scala SDK options for bootstrapping, timeouts, reliability, and performance.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.9/modules/ref/pages/client-settings.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/scala-sdk/3.9/ref/client-settings.html)

# Client Settings

> The `ClusterEnvironment` class enables you to configure Scala SDK options for bootstrapping, timeouts, reliability, and performance. 

## [](#the-environment-builder)The Environment Builder

Most client settings are related to the `ClusterEnvironment`. Because `ClusterEnvironment` is an immutable class, you need to configure it by using its embedded `Builder` class. It is designed to apply the builder arguments in a fluent fashion and then create the `ClusterEnvironment` at the very end.

Creating a cluster with custom settings

```scala
val clusterTry: Try[Cluster] = ClusterEnvironment.builder
// Customize settings here
.build
  .flatMap(
    env =>
      Cluster.connect(
        "localhost",
        ClusterOptions
          .create("username", "password")
          .environment(env)
    )
  )

clusterTry match {
  case Success(cluster) =>
    // Work with cluster

    // Shutdown gracefully
    cluster.disconnect()
    cluster.env.shutdown()

  case Failure(err) => println(s"Failure: $err")
}
```

## [](#config-builders)Config Builders

Environment settings are grouped into categories, with one builder class per category. These builders all work in the same way, which we’ll illustrate by using timeout settings as an example.

Timeout settings are configured using an instance of `TimeoutConfig`. As with most options blocks in the SDK, this is a Scala case class - e.g. an immutable data class - with fluent-style methods that return new immutable copies with a new setting applied.

Creating a new timeout config builder

```scala
ClusterEnvironment.builder
  .timeoutConfig(
    TimeoutConfig()
      .kvTimeout(5.seconds)
      .queryTimeout(10.seconds)
  )
  .build
```

The name of the cluster environment builder method for getting and setting each config builder always matches the name of the config class. For example, `TimeoutConfig` is set via the environment builder’s `timeoutConfig` method, `IoConfig` is set via the `ioConfig` method, and so on.

> [!NOTE]
> There are `com.couchbase.client.scala.env` and `com.couchbase.client.core.env` versions of all environment parameters: be sure to import the `.scala` versions.

## [](#system-properties)System Properties

Many client settings may also be configured by setting a Scala system property. If a system property is set, it always takes precedence over the builder setting.

Configuration via system property

```scala
System.setProperty("com.couchbase.env.timeout.kvTimeout", "10s") (1)
System.setProperty("com.couchbase.env.timeout.queryTimeout", "15s")

ClusterEnvironment.builder
  .timeoutConfig(
    TimeoutConfig()
      .kvTimeout(5.seconds) (2)
  )
  .build
```

| **1** | When specifying durations, s stands for seconds. Other valid qualifiers are ns for nanoseconds, us for microseconds, ms for milliseconds, and m for minutes.                          |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The kvTimeout value specified via TimeoutConfig.Builder is overridden by the system property. In this example the actual kvTimeout is 10 seconds, and the queryTimeout is 15 seconds. |

> [!TIP]
> System property names starting with `com.couchbase.env` are paths in an object graph rooted at the environment builder. Setting the property `com.couchbase.env.timeout.kvTimeout` maps to `TimeoutConfig.kvTimeout` (the 'Config' is implicit and should not be included in the property).

## [](#configuration-options)Configuration Options

The following tables cover all possible configuration options and explain their usage and default values. The tables categorize the options into groups for bootstrapping, timeout, reliability, performance, and advanced options.

## [](#security-options)Security Options

By default the client will connect to Couchbase Server using an unencrypted connection. If you are using the Enterprise Edition, it’s possible to secure the connection using TLS.

Template for configuring security settings

```scala
ClusterEnvironment.builder
  .securityConfig(SecurityConfig().enableTls(true))
  .build
```

> [!NOTE]
> Unless you set `enableTls` to `true`, none of the other security settings in this section have any effect.

Name: **Enabling Secure Connections**

Builder Method: `SecurityConfig.enableTls(Boolean)`

Default: `false`

System Property: `com.couchbase.env.security.enableTls`

Set this to `true` to encrypt all communication between the client and server using TLS. This feature requires the Enterprise Edition of Couchbase Server 3.0 or later. If TLS is enabled you must also specify the trusted certificates by calling exactly one of `trustCertificate`, `trustCertificates`, or `trustManagerFactory`. Please see the [Managing Connections](../howtos/managing-connections.md) section for more details on how to set it up properly.

Name: **Disabling Native TLS Provider**

Builder Method: `SecurityConfig.enableNativeTls(Boolean)`

Default: `true`

System Property: `com.couchbase.env.security.enableNativeTls`

When TLS is enabled, the client will by default use an optimized native TLS provider if one is available. If for some reason you need to disable the native provider and use the JDK’s portable provider instead, set this to `false`. If `enableTls` is `false` then `enableNativeTls` has no effect.

Name: **TLS Certificates**

Builder Method: `SecurityConfig.trustCertificates(Seq<X509Certificate>)`

Default: N/A

System Property: N/A

If you wish to trust more than one certificate, or prefer to load the certificate yourself, then call this method to specify the certificates to trust as Certificate Authorities when establishing secure connections. See the [Connection Management](../howtos/managing-connections.md#ssl) section for more details on how to set it up properly.

Name: **Custom TLS Trust Manager Factory**

Builder Method: `SecurityConfig.trustManagerFactory(TrustManagerFactory)`

Default: N/A

System Property: N/A

As an alternative to specifying the certificates to trust, you can specify a custom `TrustManagerFactory` to use when establishing secure connections. See the [Connection Management](../howtos/managing-connections.md#ssl) section for more details on how to set it up properly.

## [](#io-options)I/O Options

I/O settings are represented by the Scala class `IoConfig`. The associated `ClusterEnvironment.Builder` method is called `ioConfig`.

Template for configuring I/O settings

```scala
ClusterEnvironment.builder
  .ioConfig(IoConfig().networkResolution(NetworkResolution.AUTO))
  .build
```

Name: **Mutation Tokens Enabled**

Builder Method: `IoConfig.mutationTokensEnabled(Boolean)`

Default: `true`

System Property: `com.couchbase.env.io.mutationTokensEnabled`

Mutation tokens allow enhanced durability requirements as well as advanced querying capabilities. Set this to `false` if you do not require these features and wish to avoid the very small associated overhead.

Name: **Network Resolution**

Builder Method: `IoConfig.networkResolution(NetworkResolution)`

Default: `auto`

System Property: `com.couchbase.env.io.networkResolution`

> [!NOTE]
> The system property value should be one of `auto`, `default`, or `external` (lower case).

Each node in the Couchbase Server cluster might have multiple addresses associated with it. For example, a node might have one address that should be used when connecting from inside the same virtual network environment where the server is running, and a second address for connecting from outside the server’s network environment.

By default the client will use a simple matching heuristic to determine which set of addresses to use (it will select the set of addresses that contains a seed node’s host and port).

If you wish to override the heuristic, you can set this value to `default` if the client is running in the same network as the server, or `external` if the client is running in a different network.

Name: **Capture Traffic**

Builder Method: `IoConfig.captureTraffic(Set[ServiceType])`

Default: capture is disabled

System Property: `com.couchbase.env.io.captureTraffic`

> [!TIP]
> Multiple services may be specified in the system property value using a comma-delimited list such as `KV,QUERY`. To enable capture for all services, set the value of the system property to an empty string.

Call this method to log all traffic to the specified services. If no services are specified, traffic to all services is captured.

Name: **Socket Keepalive**

Builder Method: `IoConfig.enableTcpKeepAlives(Boolean)`

Default: `true`

System Property: `com.couchbase.env.io.enableTcpKeepAlives`

If enabled, the client periodically sends a TCP keepalive to the server to prevent firewalls and other network equipment from dropping idle TCP connections.

Name: **Socket Keepalive Interval**

Builder Method: `IoConfig.tcpKeepAliveTime(Duration)`

Default: `60s`

System Property: `com.couchbase.env.io.tcpKeepAliveTime`

The idle time after which a TCP keepalive gets fired. (This setting has no effect if `enableTcpKeepAlives` is `false`.)

> [!NOTE]
> This setting only propagates to the OS on Linux when the epoll transport is used. On all other platforms, the OS-configured time is used (and you need to tune it there if you want to override the default interval).

Name: **Key/Value Endpoints per Node**

Builder Method: `IoConfig.numKvConnections(Int)`

Default: `1`

System Property: `com.couchbase.env.io.numKvConnections`

The number of actual endpoints (sockets) to open per node in the cluster against the Key/Value service. By default, for every node in the cluster one socket is opened where all traffic is pushed through. That way the SDK implicitly benefits from network batching characteristics when the workload increases. If you suspect based on profiling and benchmarking that the socket is saturated you can think about slightly increasing it to have more "parallel pipelines". This might be especially helpful if you need to push large documents through it. The recommendation is keeping it at 1 unless there is other evidence.

> [!NOTE]
> [Durable Write](../concept-docs/durability-replication-failure-considerations.md#synchronous-writes) operations with Couchbase Server 6.5 and above require up to 16 kvEndpoints per node, for most efficient operation, unless the environment dictates something a little lower.

Name: **Max HTTP Endpoints per Service per Node**

Builder Method: `IoConfig.maxHttpConnections(Int)`

Default: `12`

System Property: `com.couchbase.env.io.maxHttpConnections`

Each service (except the Key/Value service) has a separate dynamically sized pool of HTTP connections for issuing requests. This setting puts an upper bound on the number of HTTP connections in each pool.

Name: **Idle HTTP Connection Timeout**

Builder Method: `IoConfig.idleHttpConnectionTimeout(Duration)`

Default: `30s`

System Property: `com.couchbase.env.io.idleHttpConnectionTimeout`

The length of time an HTTP connection may remain idle before it is closed and removed from the pool. Durations longer than 50 seconds are not recommended, since some services have a 1 minute server side idle timeout.

Name: **Config Poll Interval**

Builder Method: `IoConfig.configPollInterval(Duration)`

Default: `2.5s`

System Property: `com.couchbase.env.io.configPollInterval`

The interval at which the client fetches cluster topology information in order to proactively detect changes.

### [](#circuit-breaker-options)Circuit Breaker Options

Circuit breakers are a tool for preventing cascading failures.

When a circuit is closed, requests are sent to the server as normal. If too many requests fail within a certain time window, the breaker opens the circuit, preventing requests from going through.

When a circuit is open, any requests to the service immediately fail without the client even talking to the server. After a "sleep delay" elapses, the next request is allowed to go through the to the server. This trial request is called a "canary."

Each service has an associated circuit breaker which may be configured independently of the others. The `IoConfig` builder has methods for configuring the circuit breakers of each service.

Template for configuring circuit breaker settings

```scala
ClusterEnvironment.builder
  .ioConfig(
    IoConfig()
      .kvCircuitBreakerConfig(
        CircuitBreakerConfig()
          .enabled(true)
          .volumeThreshold(45)
          .errorThresholdPercentage(25)
          .sleepWindow(1.seconds)
          .rollingWindow(2.minutes)
      )
  )
  .build
```

The corresponding system properties would be:

```properties
com.couchbase.env.io.kvCircuitBreaker.enabled=true
com.couchbase.env.io.kvCircuitBreaker.volumeThreshold=45
com.couchbase.env.io.kvCircuitBreaker.errorThresholdPercentage=25
com.couchbase.env.io.kvCircuitBreaker.sleepWindow=1s
com.couchbase.env.io.kvCircuitBreaker.rollingWindow=2m
```

For the other services, replace `kv` with `query`, `view`, `search`, `analytics`, or `manager`.

The properties of a circuit breaker are described below.

enabled

Default: `true`

Enables or disables this circuit breaker.

If this property is set to false, then the circuit breaker is not used and all other properties are ignored.

volumeThreshold

Default: `20`

The volume threshold defines how many operations must be in the window before the threshold percentage can be meaningfully calculated.

errorThresholdPercentage

Default: `50`

The percentage of operations in a window that may fail before the circuit is opened. The value is an integer in the range \[0,100\].

sleepWindow

Default: `5s`

The delay between when the circuit opens and when the canary is tried.

rollingWindow

Default: `1m`

How long the window is in which the number of failed ops are tracked in a rolling fashion.

> [!TIP]
> Cloud Native Gateway
> 
> If using the `couchbase2://` connection protocol with [Cloud Native Gateway](../howtos/managing-connections.md#cloud-native-gateway), note that circuit breaker options are not available when using this protocol. The connection protocol uses a separate queue per node, and thus avoids the main cause of possible cascading failure.

## [](#timeout-options)Timeout Options

The default timeout values are suitable for most environments, and should be adjusted only after profiling the expected latencies in your deployment environment. If you get a timeout exception, it may be a symptom of another issue; increasing the timeout duration is sometimes not the best long-term solution.

Most timeouts can be overridden on a per-operation basis (for example, by passing a custom options block to a "get" or "query" method). The values set here are used as the defaults when no per-operation timeout is specified. See [setting duration values](#duration-values) under [System Properties](#system-properties).

Timeout settings are represented by the Scala class `TimeoutConfig`. The associated `ClusterEnvironment.Builder` method is called `timeoutConfig`.

Template for configuring timeouts

```scala
ClusterEnvironment.builder
  .timeoutConfig(
    TimeoutConfig()
      .kvTimeout(5.seconds)
      .queryTimeout(10.seconds)
  )
  .build
```

### [](#timeout-options-reference)Timeout Options Reference

Name: **Key-Value Timeout**

Builder Method: `TimeoutConfig.kvTimeout(Duration)`

Default: `2.5s` — _but see tip, below_

System Property: `com.couchbase.env.timeout.kvTimeout`

The Key/Value default timeout is used on operations which are performed on a specific key if not overridden by a custom timeout. This includes all commands like get(), getFromReplica() and all mutation commands, but does not include operations that are performed with enhanced durability requirements.

> [!TIP]
> [Durable Write operations](../concept-docs/durability-replication-failure-considerations.md#synchronous-writes) have their own timeout setting, `kvDurableTimeout`, see below.

Name: **Key-Value Durable Operation Timeout**

Builder Method: `TimeoutConfig.kvDurableTimeout(Duration)`

Default: `10s`

System Property: `com.couchbase.env.timeout.kvDurableTimeout`

Key/Value operations with enhanced durability requirements may take longer to complete, so they have a separate default timeout.

**Do not** set this above 65s, which is the maximum possible `SyncWrite` timeout on the Server side.

> [!WARNING]
> The `kvDurableTimeout` property is not part of the stable API and may change or be removed at any time.

Name: **View Timeout**

Builder Method: `TimeoutConfig.viewTimeout(Duration)`

Default: `75s`

System Property: `com.couchbase.env.timeout.viewTimeout`

The View timeout is used on view operations if not overridden by a custom timeout. Note that it is set to such a high timeout compared to key/value since it can affect hundreds or thousands of rows. Also, if there is a node failure during the request the internal cluster timeout is set to 60 seconds.

Name: **Query Timeout**

Builder Method: `TimeoutConfig.queryTimeout(Duration)`

Default: `75s`

System Property: `com.couchbase.env.timeout.queryTimeout`

The Query timeout is used on all SQL++ (formerly N1QL) query operations if not overridden by a custom timeout. Note that it is set to such a high timeout compared to key/value since it can affect hundreds or thousands of rows.

Name: **Search Timeout**

Builder Method: `TimeoutConfig.searchTimeout(Duration)`

Default: `75s`

System Property: `com.couchbase.env.timeout.searchTimeout`

The Search timeout is used on all FTS operations if not overridden by a custom timeout. Note that it is set to such a high timeout compared to key/value since it can affect hundreds or thousands of rows.

Name: **Analytics Timeout**

Builder Method: `TimeoutConfig.analyticsTimeout(Duration)`

Default: `75s`

System Property: `com.couchbase.env.timeout.analyticsTimeout`

The Analytics timeout is used on all Analytics query operations if not overridden by a custom timeout. Note that it is set to such a high timeout compared to key/value since it can affect hundreds or thousands of rows.

Name: **Connect Timeout**

Builder Method: `TimeoutConfig.connectTimeout(Duration)`

Default: `10s`

System Property: `com.couchbase.env.timeout.connectTimeout`

The connect timeout is used when a Bucket is opened and if not overridden by a custom timeout. If you feel the urge to change this value to something higher, there is a good chance that your network is not properly set up. Connecting to the server should in practice not take longer than a second on a reasonably fast network.

Name: **Disconnect Timeout**

Builder Method: `TimeoutConfig.disconnectTimeout(Duration)`

Default: `10s`

System Property: `com.couchbase.env.timeout.disconnectTimeout`

The disconnect timeout is used when a Cluster is disconnected and if not overridden by a custom timeout. A timeout is applied here always to make sure that your code does not get stuck at shutdown. The default should provide enough time to drain all outstanding operations properly, but make sure to adapt this timeout to fit your application requirements.

Name: **Management Timeout**

Builder Method: `TimeoutConfig.managementTimeout(Duration)`

Default: `75s`

System Property: `com.couchbase.env.timeout.managementTimeout`

The management timeout is used on all cluster management APIs (BucketManager, UserManager, CollectionManager, QueryIndexManager, etc.) if not overridden by a custom timeout. The default is quite high because some operations (such as flushing a bucket, for example) might take a long time.

## [](#compression-options)Compression Options

The client can optionally compress documents before sending them to Couchbase Server.

Compression settings are represented by the Scala class `CompressionConfig`. The associated `ClusterEnvironment.Builder` method is called `compressionConfig`.

Template for configuring compression settings

```scala
ClusterEnvironment.builder
  .compressionConfig(CompressionConfig().enable(true))
  .build
```

Name: **Enabling Compression**

Builder Method: `CompressionConfig.enable`

Default: `true`

System Property: `com.couchbase.env.compression.enable(Boolean)`

If enabled, the client will compress documents before they are sent to Couchbase Server. If this is set to `false`, the other compression settings have no effect.

Name: **Document Minimum Size**

Builder Method: `CompressionConfig.minSize(Int)`

Default: `32`

System Property: `com.couchbase.env.compression.minSize`

Size in bytes. Documents smaller than this size are never compressed.

Name: **Document Minimum Compressibility**

Builder Method: `CompressionConfig.minRatio(Double)`

Default: `0.83`

System Property: `com.couchbase.env.compression.minRatio`

A floating point value between 0 and 1\. Specifies how "compressible" a document must be in order for the compressed form to be sent to the server.

> [!TIP]
> Increasing the value allows compression to be used with less-compressible documents.

If the compressed document size divided by the uncompressed document size is greater than this value, then the uncompressed version of the document will be sent to Couchbase Server instead of the compressed version.

For example, with a `minRatio` of `0.83`, compression will only be used if the size of the compressed document is less than 83% of the uncompressed document size.

## [](#general-options)General Options

The settings in this category apply to the client in general. They are configured directly on the `ClusterEnvironment.Builder`.

Template for configuring general settings

```scala
ClusterEnvironment.builder
  .retryStrategy(BestEffortRetryStrategy.INSTANCE)
  .build
```

Name: **Retry Strategy**

Builder Method: `retryStrategy(RetryStrategy)`

Default: `BestEffortRetryStrategy.INSTANCE`

System Property: N/A

The client’s default retry strategy.

A retry strategy decides whether a failed operation should be retried. Implementing a custom strategy is fairly advanced, so the SDK ships with two out of the box: `BestEffortRetryStrategy` and `FailFastRetryStrategy`.

The "best effort" strategy will retry the operation until it either succeeds or the timeout expires. The "fail fast" strategy will immediately report the failure to your application, giving you more control over how and when to retry.

> [!TIP]
> Most client operations that accept an options block allow for overriding the default strategy as one of the options.

See the advanced section in the documentation on more specific information on retry strategies and failure management.

Name: **Transcoder**

Builder Method: `transcoder(Transcoder)`

Default: `JsonTranscoder`

System Property: N/A

The transcoder is responsible for converting KV binary packages to and from Scala objects.

The default transcoder assumes you are working with JSON documents. When writing documents it sets the appropriate flags to indicate the document content is JSON.

The transcoder configured here is just the default; it can be overridden on a per-operation basis.

Name: **Request Tracer**

Builder Method: `requestTracer(RequestTracer)`

Default: `ThresholdRequestTracer`

System Property: N/A

The default tracer logs the slowest requests per service.

Various `RequestTracer` implementations exist, both as part of the core library and as external modules that can be attached (i.e. for OpenTracing and OpenTelemetry). It is recommended to use those modules and not write your own tracer unless absolutely needed.

> [!NOTE]
> When using a non-default tracer, you are responsible for starting and stopping it.

Name: **Computation Scheduler**

Builder Method: `scheduler(Scheduler)`

Default: _see below_

System Property: N/A

This is an advanced setting that should not be modified without good reason.

The scheduler used for all CPU-intensive, non-blocking computations in the core, client, and user space. The default is a scheduler created from Reactor’s `Schedulers.newParallel` method, with one daemon thread per CPU core. Extra care should be used when changing the scheduler, since many internal components depend on it.

> [!NOTE]
> Shutting down the cluster environment will not dispose of a custom scheduler. You are responsible for disposing of it after it is no longer needed.

Name: **Event Bus**

Builder Method: `eventBus(EventBus)`

Default: `DefaultEventBus`

System Property: N/A

This is an advanced setting that should not be modified without good reason.

The event bus implementation used to transport system, performance, and debug events from producers to subscribers. If you provide a custom implementation, double check that it fits with the contract of the event bus as documented.

> [!NOTE]
> Shutting down the cluster environment will not stop a custom event bus. You are responsible for stopping it after it is no longer needed.

## [](#commonly-used-options)Commonly Used Options

The defaults above have been carefully considered and in general it is not recommended to make changes without expert guidance or careful testing of the change. Some options may be commonly used together in certain envionments or to achieve certain effects.

### [](#constrained-network-environments)Constrained Network Environments

Though [wide area network](../project-docs/compatibility.md#network-requirements) (WAN) connections are not directly supported, some development and non-critical operations activities across a WAN are convenient. Most likely for connecting to Couchbase Capella, or Server running in your own cloud account, whilst developing from a laptop or other machine not located in the same data center. These settings are some you may want to consider adjusting:

* Connect Timeout to 30s
* Key-Value Timeout to 5s
* Config Poll Interval to 10s
* Circuit Breaker ErrorThresholdPercentage to 75

> [!NOTE]
> As of SDK API 3.4 you can also use a **Configuration Profile**, which allows you to quickly configure your environment for common use-cases. See the [Configuration Profiles](#configuration-profiles) section for more details.

A program using the SDK can also use the `waitUntilReady()` API call to handle all connection negotiations and related errors at one place. It may be useful to block in, for example, a basic console testing application for up to 30 seconds before proceeding in the program to perform data operations. See the API reference for further details.

## [](#configuration-profiles)Configuration Profiles

Configuration Profiles provide predefined client settings that allow you to quickly configure an environment for common use-cases. When using a configuration profile, the current client settings are overridden with the values provided in the profile. Any property that is not specified in the profile is left unchanged.

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../../../java-sdk/current/project-docs/compatibility.md#interface-stability) and may be subject to change.

### [](#wan-development)WAN Development

**Builder Method:** `applyProfile(ClusterEnvironment.WanDevelopmentProfile)`

A `ClusterEnvironment.WanDevelopmentProfile` configuration profile can be used to modify client settings for development or high-latency environments. This profile changes the default timeouts.

__Table 1\. Profile Settings__
| Setting             | Default Value | WAN Profile Value |
| ------------------- | ------------- | ----------------- |
| KvConnectTimeout    | 10s           | 20s               |
| kvTimeout           | 2.5s          | 20s               |
| kvDurabilityTimeout | 10s           | 20s               |
| ViewTimeout         | 75s           | 120s              |
| QueryTimeout        | 75s           | 120s              |
| AnalyticsTimeout    | 75s           | 120s              |
| SearchTimeout       | 75s           | 120s              |
| ManagementTimeout   | 75s           | 120s              |

**Do not** set `kvDurabilityTimeout` above 65s, which is the maximum possible `SyncWrite` timeout on the Server side.

## [](#cloud-native-gateway)Cloud Native Gateway

Some settings will be ignored when using the `couchbase2://` protocol. Currently, these include:

* Compression
* `numKvConnections`