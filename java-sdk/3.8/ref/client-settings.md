---
title: Client Settings
description: The <code>ClusterEnvironment</code> class enables you to configure
  Java SDK options for security, timeouts, reliability, and performance.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.8/modules/ref/pages/client-settings.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:3.8@java-sdk:ref:client-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.8/ref/client-settings.html)

# Client Settings

> The `ClusterEnvironment` class enables you to configure Java SDK options for security, timeouts, reliability, and performance. 

## [](#the-environment-builder)The Environment Builder

Most client settings are related to the `ClusterEnvironment`. Because `ClusterEnvironment` is an immutable class, you need to configure it by using its embedded `Builder` class. It is designed to apply the builder arguments in a fluent fashion and then create the `ClusterEnvironment` at the very end.

Creating a cluster with custom settings

```java
Cluster cluster = Cluster.connect(
    connectionString,
    ClusterOptions.clusterOptions(username, password)
        .environment(env -> {
          // "env" is a `ClusterEnvironment.Builder`. Customize
          // client settings by calling builder methods.

          // Don't call env.build()! The SDK takes care of that.
        })
```

## [](#config-builders)Nested Config Builders

Client settings are grouped into categories, with one builder class per category. These builders all work in the same way, which we'll illustrate by using timeout and I/O settings as an example.

Timeout settings are configured using an instance of `TimeoutConfig.Builder`. The usual way to get an instance is to call a configuration callback method on the `ClusterEnvironment.Builder` class.

There's a similar class for I/O settings, called `IoConfig.Builder`.

Each category of client settings has its own builder class.

Configuring client settings for timeouts and I/O

```java
Cluster cluster = Cluster.connect(
    connectionString,
    ClusterOptions.clusterOptions(username, password)
        .environment(env -> env // ClusterEnvironment.Builder
            .timeoutConfig(timeout -> timeout // TimeoutConfig.Builder
                .kvTimeout(Duration.ofSeconds(5))
                .queryTimeout(Duration.ofSeconds(10))
            )
            .ioConfig(io -> io // IoConfig.Builder
                .maxHttpConnections(64)
            )
        )
);
```

The name of the `ClusterEnvironment.Builder` method for configuring a nested builder matches the name of the nested config class. For example, the `TimeoutConfig.Builder` is configured using the environment builder's `timeoutConfig` method, the `IoConfig.Builder` is configured using the `ioConfig` method, and so on.

## [](#connection-string-params)Connection String Parameters

Many client settings may also be configured by specifying a parameter in the connection string.

> [!NOTE]
> A connection string parameter takes precedence over the corresponding [builder method](#config-builders).

Configuration via connection string parameters

```java
Cluster cluster = Cluster.connect(
    "couchbase://127.0.0.1?timeout.kvTimeout=10s&timeout.queryTimeout=15s", (1)
    ClusterOptions.clusterOptions(username, password)
        .environment(env -> env
            .timeoutConfig(timeout -> timeout
                .kvTimeout(Duration.ofSeconds(5)) (2)
            )
        )
);
```

| **1** | When specifying durations, s stands for seconds. Other valid qualifiers are ns for nanoseconds, us for microseconds, ms for milliseconds, and m for minutes.                                                         |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The kvTimeout value specified via TimeoutConfig.Builder is overridden by the timeout.kvTimeout connection string parameter. In this example, the actual kvTimeout is 10 seconds, and the queryTimeout is 15 seconds. |

## [](#system-properties)System Properties

Any client setting that can be specified as a connection string parameter may also be specified as a Java system property.

> [!NOTE]
> A system property takes precedence over the corresponding [connection string parameter](#connection-string-params) or [builder method](#config-builders).

Configuration via system property

```java
System.setProperty("com.couchbase.env.timeout.kvTimeout", "10s"); (1)
System.setProperty("com.couchbase.env.timeout.queryTimeout", "15s");

Cluster cluster = Cluster.connect(
    "couchbase://127.0.0.1?timeout.queryTimeout=30s", (2)
    ClusterOptions.clusterOptions(username, password)
        .environment(env -> env
            .timeoutConfig(timeout -> timeout
                .kvTimeout(Duration.ofSeconds(5)) (2)
            )
        )
);
```

| **1** | When specifying durations, s stands for seconds. Other valid qualifiers are ns for nanoseconds, us for microseconds, ms for milliseconds, and m for minutes.    |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The client setting specified here is overridden by the system property. In this example the actual kvTimeout is 10 seconds, and the queryTimeout is 15 seconds. |

> [!TIP]
> The system property name for a client setting is always `com.couchbase.env.` plus the connection string parameter name.

## [](#configuration-options)Configuration Options

The following sections cover all possible configuration options and explain their usage and default values. They are categorized into groups for [security](#security-options), [I/O](#io-options), [circuit breakers](#circuit-breaker-options), [timeout](#timeout-options), [compression](#compression-options), and [general](#general-options) options.

### [](#security-options)Security Options

By default the client will connect to Couchbase Server using an unencrypted connection. If you are using the Enterprise Edition, it's possible to secure the connection using TLS.

Template for configuring security settings

```java
Cluster cluster = Cluster.connect(
    connectionString,
    ClusterOptions.clusterOptions(username, password)
        .environment(env -> env
            .securityConfig(security -> security
                .enableTls(true)
            )
        )
);
```

#### [](#security.enableTls)Enabling Secure Connections

| Connection String | security.enableTls                              |
| ----------------- | ----------------------------------------------- |
| System Property   | com.couchbase.env.security.enableTls            |
| Builder           | env.securityConfig(it -> it.enableTls(boolean)) |
| Default Value     | false                                           |

Set this to `true` to encrypt all communication between the client and server using TLS. This feature requires the Enterprise Edition of Couchbase Server.

> [!TIP]
> The recommended way to enable TLS is to specify a connection string that starts with the `couchbases://` (note the final "s") scheme. This forces a secure connection, regardless of whether `security.enableTls` is true or false.
> 
> Specifying `security.enableTls` is only required when building a [shared cluster environment](../howtos/managing-connections.md#multiple-clusters) for use with secure connections.

When TLS is enabled, you might also need to specify the trusted certificates by calling exactly one of `trustCertificate`, `trustCertificates`, or `trustManagerFactory`. Please see the [Managing Connections](../howtos/managing-connections.md) section for more details on how to set it up properly.

#### [](#security.enableNativeTls)Disabling Native TLS Provider

| Connection String | security.enableNativeTls                              |
| ----------------- | ----------------------------------------------------- |
| System Property   | com.couchbase.env.security.enableNativeTls            |
| Builder           | env.securityConfig(it -> it.enableNativeTls(boolean)) |
| Default Value     | true                                                  |

When TLS is enabled, the client will by default use an optimized native TLS provider if one is available. If for some reason you need to disable the native provider and use the JDK's portable provider instead, set this to `false`. If TLS is not enabled, then `security.enableNativeTls` has no effect.

#### [](#security.trustCertificate)TLS Certificate Location

| Connection String | security.trustCertificate (or certpath)             |
| ----------------- | --------------------------------------------------- |
| System Property   | com.couchbase.env.security.trustCertificate         |
| Builder           | env.securityConfig(it -> it.trustCertificate(Path)) |
| Default Value     | N/A                                                 |

Path to a file containing a single X.509 certificate to trust as a Certificate Authority when establishing secure connections. See the [Connection Management](../howtos/managing-connections.md#ssl) section for more details on how to set it up properly.

#### [](#security.trustCertificates)TLS Certificates

| Connection String | N/A                                                                   |
| ----------------- | --------------------------------------------------------------------- |
| System Property   | N/A                                                                   |
| Builder           | env.securityConfig(it -> it.trustCertificates(List<X509Certificate>)) |
| Default Value     | N/A                                                                   |

If you wish to trust more than one certificate, or prefer to load the certificate yourself, then call this method to specify the certificates to trust as Certificate Authorities when establishing secure connections. See the [Connection Management](../howtos/managing-connections.md#ssl) section for more details on how to set it up properly.

#### [](#security.trustManagerFactory)Custom TLS Trust Manager Factory

| Connection String | N/A                                                                   |
| ----------------- | --------------------------------------------------------------------- |
| System Property   | N/A                                                                   |
| Builder           | env.securityConfig(it -> it.trustManagerFactory(TrustManagerFactory)) |
| Default Value     | N/A                                                                   |

As an alternative to specifying the certificates to trust, you can specify a custom `TrustManagerFactory` to use when establishing secure connections. See the [Connection Management](../howtos/managing-connections.md#ssl) section for more details on how to set it up properly.

### [](#io-options)I/O Options

I/O settings are represented by the Java class `IoConfig`. The associated `ClusterEnvironment.Builder` method is called `ioConfig`.

Template for configuring I/O settings

```java
Cluster cluster = Cluster.connect(
    connectionString,
    ClusterOptions.clusterOptions(username, password)
        .environment(env -> env
            .ioConfig(io -> io
                .networkResolution(NetworkResolution.AUTO)
            )
        )
);
```

#### [](#io.enableDnsSrv)DNS SRV Enabled

| Connection String | io.enableDnsSrv                              |
| ----------------- | -------------------------------------------- |
| System Property   | com.couchbase.env.io.enableDnsSrv            |
| Builder           | env.ioConfig(it -> it.enableDnsSrv(boolean)) |
| Default Value     | true                                         |

Gets the bootstrap node list from a DNS SRV record. See the [Connection Management](../howtos/managing-connections.md#using-dns-srv-records) section for more information on how to use it properly.

#### [](#io.mutationTokensEnabled)Mutation Tokens Enabled

| Connection String | io.mutationTokensEnabled                              |
| ----------------- | ----------------------------------------------------- |
| System Property   | com.couchbase.env.io.mutationTokensEnabled            |
| Builder           | env.ioConfig(it -> it.mutationTokensEnabled(boolean)) |
| Default Value     | true                                                  |

Mutation tokens allow enhanced durability requirements as well as advanced [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) querying capabilities. Set this to `false` if you do not require these features and wish to avoid the associated overhead.

#### [](#io.networkResolution)Network Resolution

| Connection String | io.networkResolution (or network)                 |
| ----------------- | ------------------------------------------------- |
| System Property   | com.couchbase.env.io.networkResolution            |
| Builder           | env.ioConfig(it -> it.networkResolution(boolean)) |
| Default Value     | auto                                              |

> [!NOTE]
> The value for the connection string parameter or system property should be one of `auto`, `default`, or `external` (lower case).

Each node in the Couchbase Server cluster might have multiple addresses associated with it. For example, a node might have one address that should be used when connecting from inside the same virtual network environment where the server is running, and a second address for connecting from outside the server's network environment.

By default the client will use a simple matching heuristic to determine which set of addresses to use (it will select the set of addresses that contains a seed node's host and port).

If you wish to override the heuristic, you can set this value to `default` if the client is running in the same network as the server, or `external` if the client is running in a different network.

#### [](#io.captureTraffic)Capture Traffic

| Connection String | io.captureTraffic                                    |
| ----------------- | ---------------------------------------------------- |
| System Property   | com.couchbase.env.io.captureTraffic                  |
| Builder           | env.ioConfig(it -> it.captureTraffic(ServiceType…​)) |
| Default Value     | traffic capture is disabled                          |

> [!TIP]
> Multiple services may be specified in the connection string parameter or system property value using a comma-delimited list such as `KV,QUERY`. To enable capture for all services, set the value to an empty string.

Call this method to log all traffic to the specified services. If no services are specified, traffic to all services is captured.

Captured traffic is logged to the `com.couchbase.io` category at `TRACE` level. To see the traffic, you may need to configure your logging framework to include these messages.

#### [](#io.enableTcpKeepAlives)Socket Keepalive

| Connection String | io.enableTcpKeepAlives                              |
| ----------------- | --------------------------------------------------- |
| System Property   | com.couchbase.env.io.enableTcpKeepAlives            |
| Builder           | env.ioConfig(it -> it.enableTcpKeepAlives(boolean)) |
| Default Value     | true                                                |

If enabled, the client periodically sends a TCP keepalive to the server to prevent firewalls and other network equipment from dropping idle TCP connections.

#### [](#io.tcpKeepAliveTime)Socket Keepalive Interval

| Connection String | io.tcpKeepAliveTime                               |
| ----------------- | ------------------------------------------------- |
| System Property   | com.couchbase.env.io.tcpKeepAliveTime             |
| Builder           | env.ioConfig(it -> it.tcpKeepAliveTime(Duration)) |
| Default Value     | 60s                                               |

The idle time after which a TCP keepalive gets fired. (This setting has no effect if `io.enableTcpKeepAlives` is `false`.)

> [!NOTE]
> This setting only propagates to the OS on Linux when the epoll transport is used. On all other platforms, the OS-configured time is used (and you need to tune it there if you want to override the default interval).

#### [](#io.numKvConnections)Key/Value Endpoints per Node

| Connection String | io.numKvConnections                          |
| ----------------- | -------------------------------------------- |
| System Property   | com.couchbase.env.io.numKvConnections        |
| Builder           | env.ioConfig(it -> it.numKvConnections(int)) |
| Default Value     | 1                                            |

The number of actual endpoints (sockets) to open per node in the cluster against the Key/Value service. By default, for every node in the cluster one socket is opened where all traffic is pushed through. That way the SDK implicitly benefits from network batching characteristics when the workload increases. If you suspect based on profiling and benchmarking that the socket is saturated you can think about slightly increasing it to have more "parallel pipelines". This might be especially helpful if you need to push large documents through it. The recommendation is keeping it at 1 unless there is other evidence.

> [!NOTE]
> [Durable Write](../concept-docs/durability-replication-failure-considerations.md#synchronous-writes) operations with Couchbase Server 6.5 and above require up to 16 kvEndpoints per node, for most efficient operation, unless the environment dictates something a little lower.

#### [](#io.maxHttpConnections)Max HTTP Endpoints per Service per Node

| Connection String | io.maxHttpConnections                          |
| ----------------- | ---------------------------------------------- |
| System Property   | com.couchbase.env.io.maxHttpConnections        |
| Builder           | env.ioConfig(it -> it.maxHttpConnections(int)) |
| Default Value     | 12                                             |

Each service (except the Key/Value service) has a separate dynamically sized pool of HTTP connections for issuing requests. This setting puts an upper bound on the number of HTTP connections in each pool.

#### [](#io.idleHttpConnectionTimeout)Idle HTTP Connection Timeout

| Connection String | io.idleHttpConnectionTimeout                               |
| ----------------- | ---------------------------------------------------------- |
| System Property   | com.couchbase.env.io.idleHttpConnectionTimeout             |
| Builder           | env.ioConfig(it -> it.idleHttpConnectionTimeout(Duration)) |
| Default Value     | 1s                                                         |

The length of time an HTTP connection may remain idle before it is closed and removed from the pool. Durations longer than 1 second are not recommended, since Couchbase Server aggressively drops idle connections.

#### [](#io.configPollInterval)Config Poll Interval

| Connection String | io.configPollInterval                               |
| ----------------- | --------------------------------------------------- |
| System Property   | com.couchbase.env.io.configPollInterval             |
| Builder           | env.ioConfig(it -> it.configPollInterval(Duration)) |
| Default Value     | 2.5s                                                |

The interval at which the client fetches cluster topology information in order to proactively detect changes.

### [](#circuit-breaker-options)Circuit Breaker Options

Circuit breakers are a tool for preventing cascading failures.

When a circuit is closed, requests are sent to the server as normal. If too many requests fail within a certain time window, the breaker opens the circuit, preventing requests from going through.

When a circuit is open, any requests to the service immediately fail without the client even talking to the server. After a "sleep delay" elapses, the next request is allowed to go through the to the server. This trial request is called a "canary."

Each service has an associated circuit breaker which may be configured independently of the others. The `IoConfig` builder has methods for configuring the circuit breakers of each service.

Template for configuring circuit breaker settings

```java
Cluster cluster = Cluster.connect(
    connectionString,
    ClusterOptions.clusterOptions(username, password)
        .environment(env -> env
            .ioConfig(io -> io.
                kvCircuitBreakerConfig(kvBreaker -> kvBreaker
                    .enabled(true)
                    .volumeThreshold(45)
                    .errorThresholdPercentage(25)
                    .sleepWindow(Duration.ofSeconds(1))
                    .rollingWindow(Duration.ofMinutes(2))
                )
            )
        )
);
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

Default: `false`

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

### [](#timeout-options)Timeout Options

The default timeout values are suitable for most environments, and should be adjusted only after profiling the expected latencies in your deployment environment. If you get a timeout exception, it may be a symptom of another issue; increasing the timeout duration is sometimes not the best long-term solution.

Most timeouts can be overridden on a per-operation basis (for example, by passing a custom options block to a "get" or "query" method). The values set here are used as the defaults when no per-operation timeout is specified. See [setting duration values](#duration-values) under [System Properties](#system-properties).

Template for configuring timeouts

```java
Cluster cluster = Cluster.connect(
    connectionString,
    ClusterOptions.clusterOptions(username, password)
        .environment(env -> env
            .timeoutConfig(timeout -> timeout
                .kvTimeout(Duration.ofMillis(2500))
            )
        )
);
```

#### [](#timeout.kvTimeout)Key-Value Timeout

| Connection String | timeout.kvTimeout                               |
| ----------------- | ----------------------------------------------- |
| System Property   | com.couchbase.env.timeout.kvTimeout             |
| Builder           | env.timeoutConfig(it -> it.kvTimeout(Duration)) |
| Default Value     | 2.5s — _but see TIP, below_                     |

The Key/Value default timeout is used on operations which are performed on a specific key if not overridden by a custom timeout. This includes all commands like get(), getFromReplica() and all mutation commands, but does not include operations that are performed with enhanced durability requirements.

> [!TIP]
> [Durable Write operations](../concept-docs/durability-replication-failure-considerations.md#synchronous-writes) have their own timeout setting, `kvDurableTimeout`, see below.

#### [](#timeout.kvDurableTimeout)Key-Value Durable Operation Timeout

| Connection String | timeout.kvDurableTimeout                               |
| ----------------- | ------------------------------------------------------ |
| System Property   | com.couchbase.env.timeout.kvDurableTimeout             |
| Builder           | env.timeoutConfig(it -> it.kvDurableTimeout(Duration)) |
| Default Value     | 10s                                                    |

Key/Value operations with enhanced durability requirements may take longer to complete, so they have a separate default timeout.

**Do not** set this above 65s, which is the maximum possible `SyncWrite` timeout on the Server side.

> [!WARNING]
> The `kvDurableTimeout` property is not part of the stable API and may change or be removed at any time.

#### [](#timeout.viewTimeout)View Timeout

| Connection String | timeout.viewTimeout                               |
| ----------------- | ------------------------------------------------- |
| System Property   | com.couchbase.env.timeout.viewTimeout             |
| Builder           | env.timeoutConfig(it -> it.viewTimeout(Duration)) |
| Default Value     | 75s                                               |

The View timeout is used on view operations if not overridden by a custom timeout. Note that it is set to such a high timeout compared to key/value since it can affect hundreds or thousands of rows. Also, if there is a node failure during the request the internal cluster timeout is set to 60 seconds.

#### [](#timeout.queryTimeout)Query Timeout

| Connection String | timeout.queryTimeout                               |
| ----------------- | -------------------------------------------------- |
| System Property   | com.couchbase.env.timeout.queryTimeout             |
| Builder           | env.timeoutConfig(it -> it.queryTimeout(Duration)) |
| Default Value     | 75s                                                |

The Query timeout is used on all SQL++ query operations if not overridden by a custom timeout. Note that it is set to such a high timeout compared to key/value since it can affect hundreds or thousands of rows.

#### [](#timeout.searchTimeout)Search Timeout

| Connection String | timeout.searchTimeout                               |
| ----------------- | --------------------------------------------------- |
| System Property   | com.couchbase.env.timeout.searchTimeout             |
| Builder           | env.timeoutConfig(it -> it.searchTimeout(Duration)) |
| Default Value     | 75s                                                 |

The Search timeout is used on all FTS operations if not overridden by a custom timeout. Note that it is set to such a high timeout compared to key/value since it can affect hundreds or thousands of rows.

#### [](#timeout.analyticsTimeout)Analytics Timeout

| Connection String | timeout.analyticsTimeout                               |
| ----------------- | ------------------------------------------------------ |
| System Property   | com.couchbase.env.timeout.analyticsTimeout             |
| Builder           | env.timeoutConfig(it -> it.analyticsTimeout(Duration)) |
| Default Value     | 75s                                                    |

The Analytics timeout is used on all Analytics query operations if not overridden by a custom timeout. Note that it is set to such a high timeout compared to key/value since it can affect hundreds or thousands of rows.

#### [](#timeout.connectTimeout)Connect Timeout

| Connection String | timeout.connectTimeout                               |
| ----------------- | ---------------------------------------------------- |
| System Property   | com.couchbase.env.timeout.connectTimeout             |
| Builder           | env.timeoutConfig(it -> it.connectTimeout(Duration)) |
| Default Value     | 10s                                                  |

The connect timeout is used when a Bucket is opened and if not overridden by a custom timeout. If you feel the urge to change this value to something higher, there is a good chance that your network is not properly set up. Connecting to the server should in practice not take longer than a second on a reasonably fast network.

#### [](#timeout.disconnectTimeout)Disconnect Timeout

| Connection String | timeout.disconnectTimeout                               |
| ----------------- | ------------------------------------------------------- |
| System Property   | com.couchbase.env.timeout.disconnectTimeout             |
| Builder           | env.timeoutConfig(it -> it.disconnectTimeout(Duration)) |
| Default Value     | 10s                                                     |

The disconnect timeout is used when a Cluster is disconnected and if not overridden by a custom timeout. A timeout is applied here always to make sure that your code does not get stuck at shutdown. The default should provide enough time to drain all outstanding operations properly, but make sure to adapt this timeout to fit your application requirements.

#### [](#timeout.managementTimeout)Management Timeout

| Connection String | timeout.managementTimeout                               |
| ----------------- | ------------------------------------------------------- |
| System Property   | com.couchbase.env.timeout.managementTimeout             |
| Builder           | env.timeoutConfig(it -> it.managementTimeout(Duration)) |
| Default Value     | 75s                                                     |

The management timeout is used on all cluster management APIs (BucketManager, UserManager, CollectionManager, QueryIndexManager, etc.) if not overridden by a custom timeout. The default is quite high because some operations (such as flushing a bucket, for example) might take a long time.

### [](#compression-options)Compression Options

The client can optionally compress documents before sending them to Couchbase Server.

Template for configuring CompressionExample settings

```java
Cluster cluster = Cluster.connect(
    connectionString,
    ClusterOptions.clusterOptions(username, password)
        .environment(env -> env
            .compressionConfig(compression -> compression
                .minSize(32)
            )
        )
);
```

#### [](#compression.enable)Enabling Compression

| Connection String | compression.enable                              |
| ----------------- | ----------------------------------------------- |
| System Property   | com.couchbase.env.compression.enable            |
| Builder           | env.compressionConfig(it -> it.enable(boolean)) |
| Default Value     | true                                            |

If enabled, the client will compress documents before they are sent to Couchbase Server. If this is set to `false`, the other compression settings have no effect.

#### [](#compression.minSize)Document Minimum Size

| Connection String | compression.minSize                          |
| ----------------- | -------------------------------------------- |
| System Property   | com.couchbase.env.compression.minSize        |
| Builder           | env.compressionConfig(it -> it.minSize(int)) |
| Default Value     | 32                                           |

Size in bytes. Documents smaller than this size are never compressed.

#### [](#compression.minRatio)Document Minimum Compressibility

| Connection String | compression.minRatio                          |
| ----------------- | --------------------------------------------- |
| System Property   | com.couchbase.env.compression.minRatio        |
| Builder           | env.compressionConfig(it -> it.minRatio(int)) |
| Default Value     | 0.83                                          |

A floating point value between 0 and 1\. Specifies how "compressible" a document must be in order for the compressed form to be sent to the server.

> [!TIP]
> Increasing the value allows CompressionExample to be used with less-compressible documents.

If the compressed document size divided by the uncompressed document size is greater than this value, then the uncompressed version of the document will be sent to Couchbase Server instead of the compressed version.

For example, with a `minRatio` of `0.83`, CompressionExample will only be used if the size of the compressed document is less than 83% of the uncompressed document size.

### [](#general-options)General Options

The settings in this category apply to the client in general. They are configured directly on the `ClusterEnvironment.Builder`.

Template for configuring general settings

```java
Cluster cluster = Cluster.connect(
    connectionString,
    ClusterOptions.clusterOptions(username, password)
        .environment(env -> env
            .retryStrategy(BestEffortRetryStrategy.INSTANCE)
        )
);
```

#### [](#retryStrategy)Retry Strategy

| Connection String | N/A                              |
| ----------------- | -------------------------------- |
| System Property   | N/A                              |
| Builder           | env.retryStrategy(RetryStrategy) |
| Default Value     | BestEffortRetryStrategy.INSTANCE |

The client's default retry strategy.

A retry strategy decides whether a failed operation should be retried. Implementing a custom strategy is fairly advanced, so the SDK ships with two out of the box: `BestEffortRetryStrategy` and `FailFastRetryStrategy`.

The "best effort" strategy will retry the operation until it either succeeds or the timeout expires. The "fail fast" strategy will immediately report the failure to your application, giving you more control over how and when to retry.

> [!TIP]
> Most client operations that accept an options block allow for overriding the default strategy as one of the options.

See the advanced section in the documentation on more specific information on retry strategies and failure management.

#### [](#unordered-executions)Unordered Execution

| Connection String | N/A                                     |
| ----------------- | --------------------------------------- |
| System Property   | com.couchbase.unorderedExecutionEnabled |
| Builder           | N/A                                     |
| Default Value     | true                                    |

From Couchbase 7.0, Out-of-Order execution allows the server to concurrently handle multiple requests on the same connection, potentially improving performance for durable writes and multi-document ACID transactions. This means that tuning the number of connections (KV endpoints) is no longer necessary as a workaround where data not available in the cache is causing timeouts.

This is set to `true` by default. Note, changing the setting will only affect Server versions 7.0 onwards.

#### [](#jsonSerializer)JSON Serializer

| Connection String | N/A                                |
| ----------------- | ---------------------------------- |
| System Property   | N/A                                |
| Builder           | env.jsonSerializer(JsonSerializer) |
| Default Value     | _see description below_            |

The JSON serializer handles the conversion between JSON and Java objects.

If Jackson is present in the class path, the default serializer will be an instance of `JacksonJsonSerializer` using a default `ObjectMapper`.

> [!TIP]
> To create a serializer backed by a custom `ObjectMapper`, call `JacksonJsonSerializer.create` and pass in your custom mapper.

If Jackson is not present, the client will fall back to using an unspecified default serializer. (Actually, it will use a repackaged version of Jackson, but this is an implementation detail you should not depend on.)

#### [](#transcoder)Transcoder

| Connection String | N/A                        |
| ----------------- | -------------------------- |
| System Property   | N/A                        |
| Builder           | env.transcoder(Transcoder) |
| Default Value     | JsonTranscoder             |

The transcoder is responsible for converting KV binary packages to and from Java objects.

The default transcoder assumes you are working with JSON documents. It uses the configured `jsonSerializer` to convert between JSON and Java objects. When writing documents it sets the appropriate flags to indicate the document content is JSON.

The transcoder configured here is just the default; it can be overridden on a per-operation basis.

#### [](#requestTracer)Request Tracer

| Connection String | N/A                              |
| ----------------- | -------------------------------- |
| System Property   | N/A                              |
| Builder           | env.requestTracer(RequestTracer) |
| Default Value     | ThresholdRequestTracer           |

The default tracer logs the slowest requests per service.

Various `RequestTracer` implementations exist, both as part of the core library and as external modules that can be attached (i.e. for OpenTracing and OpenTelemetry). It is recommended to use those modules and not write your own tracer unless absolutely needed.

> [!NOTE]
> When using a non-default tracer, you are responsible for starting and stopping it.

#### [](#scheduler)Computation Scheduler

| Connection String | N/A                      |
| ----------------- | ------------------------ |
| System Property   | N/A                      |
| Builder           | env.scheduler(Scheduler) |
| Default Value     | _see below_              |

This is an advanced setting that should not be modified without good reason.

The scheduler used for all CPU-intensive, non-blocking computations in the core, client, and user space. The default is a scheduler created from Reactor's `Schedulers.newParallel` method, with one daemon thread per CPU core. Extra care should be used when changing the scheduler, since many internal components depend on it.

> [!NOTE]
> Shutting down the cluster environment will not dispose of a custom scheduler. You are responsible for disposing of it after it is no longer needed.

#### [](#eventBus)Event Bus

| Connection String | N/A                |
| ----------------- | ------------------ |
| System Property   | N/A                |
| Builder           | eventBus(EventBus) |
| Default Value     | DefaultEventBus    |

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

| Connection String | applyProfile                   |
| ----------------- | ------------------------------ |
| System Property   | com.couchbase.env.applyProfile |
| Builder           | applyProfile(String)           |
| Default Value     | no profile                     |

Configuration Profiles provide predefined client settings that allow you to quickly configure an environment for common use-cases. When using a configuration profile, the current client settings are overridden with the values provided in the profile. Any property that is not specified in the profile is left unchanged.

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../../current/project-docs/compatibility.md#interface-stability) and may be subject to change.

### [](#wan-development)WAN Development

**Builder Method:** `env.applyProfile("wan-development")`

The `wan-development` configuration profile can be used to modify client settings for development or high-latency environments. This profile changes the default timeouts.

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

Using the [Cloud Native Gateway](../howtos/managing-connections.md#cloud-native-gateway) protocol (to connect to Couchbase Server running on [Couchbase Autonomous Operator](#operator::concept-cloud-native-gateway.adoc) 2.6.1 or newer) should not need any changes to config.

Some settings will be ignored when using the `couchbase2://` protocol. Currently, these include:

* Compression
* `numKvConnections`