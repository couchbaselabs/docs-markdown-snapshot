---
title: Connecting
description: Connecting to a Couchbase Server cluster and configuring client settings.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/3.9/modules/howtos/pages/connecting.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:3.9@kotlin-sdk:howtos:connecting.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/3.9/howtos/connecting.html)

# Connecting

> Connecting to a Couchbase Server cluster and configuring client settings. 

## [](#connecting-to-a-cluster)Connecting to a cluster

Use the [Cluster.connect](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client/kotlin-client/com.couchbase.client.kotlin/-cluster/-companion/) companion factory method to create a [Cluster](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client/kotlin-client/com.couchbase.client.kotlin/-cluster/) object. This object represents a connection to a Couchbase Server cluster.

It's best to create a single Cluster when your application starts up, and share it across your application. When your application shuts down, disconnect the Cluster. Disconnecting gives any in-flight requests a chance to complete, then releases the resources managed by the Cluster.

```kotlin
import com.couchbase.client.kotlin.Cluster
import kotlinx.coroutines.runBlocking
import kotlin.time.Duration.Companion.seconds

fun main() {
    val cluster = Cluster.connect(
        connectionString = "couchbase://127.0.0.1", (1)
        username = "username",
        password = "password",
    )

    runBlocking { (2)
        try {
            cluster.waitUntilReady(10.seconds) (3)
            // ...
        } finally {
            cluster.disconnect()
        }
    }
}
```

| **1** | If you're connecting to Capella, enable TLS by using couchbases:// (note the final 's') instead of couchbase://. For more information about TLS, see [Secure Connections](secure-connections.md).                                                                                                                                                                                                                                                                                                                                              |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The Kotlin SDK uses [coroutines](https://kotlinlang.org/docs/coroutines-overview.html) for asynchronous execution. Many of the methods in the SDK are suspending functions, and can only be called from a coroutine context. The [runBlocking](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/run-blocking.html) method is a convenient way to create a coroutine context in a main method, in test code, or in some other blocking context, but should never be called from within another coroutine. |
| **3** | Cluster.connect returns immediately. The SDK continues working in the background to finish connecting. Waiting for the connection to complete is optional, but can be good because it lets you know right away if there is a problem with the connection. Waiting here also makes it less likely a following request times out, since none of the time allotted to the next request is spent waiting for the connection to complete.                                                                                                           |

## [](#connection-string)Connection String

The SDK needs to know the address of at least one node in the Couchbase Server cluster. After it connects to one node, it discovers the others.

The simplest connection string is a single hostname or literal IP address, like `"foo.example.com"` or `"127.0.0.1"`.

With DNS SRV, one address is enough. The SDK uses the address to look up the DNS SRV record, then inspects the record to discover the addresses of all the nodes.

> [!NOTE]
> Couchbase Capella always uses DNS SRV.

If you're not using DNS SRV, it's good to include the addresses of multiple nodes in the connection string. The more addresses you provide, the more likely the SDK is able to connect when some nodes are unavailable. To specify multiple addresses, join them with commas:

Connection string with two addresses

```kotlin
val connectionString = "foo.example.com,bar.example.com"
```

### [](#connection-string-ports)Non-standard ports

By default, the Couchbase Key Value (KV) service listens on port 11210 (or 11207 for TLS), and the Manager service listens on port 8091 (or 18091 for TLS). The SDK can bootstrap against either service, but the KV service is preferable because it's faster.

If the server is listening on a non-default port, or there is some kind of port mapping going on, include the port in the connection string:

Connection string with non-standard KV port

```kotlin
val connectionString = "foo.example.com:1234"
```

If you need to bootstrap against a non-standard Manager port (because the node isn't running the KV service), tell the SDK it's a Manager port by appending "=manager", like this:

Connection string with non-standard Manager port

```kotlin
val connectionString = "foo.example.com:4567=manager"
```

### [](#connection-string-params)Connection string parameters

Connection strings can also configure client settings.

We mentioned DNS SRV earlier. Let's suppose for some reason you need to tell the SDK not to use DNS SRV. There are few different ways to do that, but since we're talking about connections strings, let's put a `?` after the address list and add a parameter:

Connection string with a parameter

```kotlin
val connectionString = "foo.example.com?io.enableDnsSrv=false"
```

(It's usually not necessary to disable support for DNS SRV, even if you're not using it — we're just using `io.enableDnsSrv` as an example client setting.)

> [!WARNING]
> Connection string parameters don't like sharing
> 
> If you decide to share a `ClusterEnvironment` by calling `Cluster.connectUsingSharedEnvironment`, the connection string must not have parameters. Environment sharing is an advanced topic we'll cover later.

To include multiple parameters, join them with `&`, like:

Connection string with two parameters

```kotlin
val connectionString =
    "foo.example.com?io.enableDnsSrv=false&timeout.kvTimeout=5s"
```

Any ampersands (`&`) or percent signs (`%`) in a parameter value must be [percent-encoded](https://en.wikipedia.org/wiki/Percent-encoding). It's fine to percent-encode the whole value.

### [](#connection-string-scheme)Connection string scheme

A connection string may start with a URI scheme. The supported prefixes are `couchbase://` and `couchbases://` (note the final 's', which stands for "secure"). For example:

Connection string with a URI scheme specifying TLS is required

```none
couchbases://foo.example.com
```

The `couchbases://` prefix uses secure connections with TLS.

The `couchbase://` prefix uses insecure connections by default, but you can still enable TLS with the `security.enableTls` client setting.

> [!NOTE]
> The [Secure Connections](secure-connections.md) documentation describes additional client settings that might be required when TLS is enabled.

Omitting the scheme is equivalent to specifying the `couchbase://` prefix.

### [](#cloud-native-gateway)Cloud Native Gateway

Couchbase's next generation connection protocol, introduced in Kotlin SDK 1.2 and [Couchbase Autonomous Operator 2.6.1](../../../cloud-native-gateway/current/intro/about-cng.md), can be enabled simply by changing the connection string to `couchbase2://` but there are a few differences to be aware of, described [below](#limitations).

The protocol implements a gRPC-style interface between the SDK and Couchbase Server (in this case, only available in the Server running on Kubernetes or OpenShift, with a forthcoming release of [Couchbase Autonomous Operator](../../../operator/current/overview.md).

#### [](#limitations)Limitations

The underlying protocol will not work with certain legacy features: MapReduce Views (a deprecated Service — use [Query](n1ql-queries.md) instead) and Memcached buckets (superseded by the improved [Ephemeral Buckets](#8.0.0@server:learn:buckets-memory-and-storage/buckets.adoc#bucket-types)).

The following are not currently implemented over the `couchbase2://` protocol:

* Authentication by client certificate.
* Multi-document ACID transactions.
* Analytics service.
* Health Check.

There are some different behaviors seen with this protocol:

* Some config options are unsupported — see the [Settings page](../ref/client-settings.md#cloud-native-gateway).
* The SDK will poll the gRPC channels until they are in a good state, or return an error, or timeout while waiting — in our standard protocol there is an option of setting `waitUntilReady()` for just certain services to become available.
* Some error codes are more generic — in cases where the client would not be expected to need to take specific action — but should cause no problem, unless you have written code looking at individual strings within the error messages.
* Although documents continue to be stored compressed by Couchbase Server, they will not be transmitted in compressed form (to and from the client) over the wire, using `couchbase2://`.

## [](#client-settings)Client Settings

> A "client setting" controls an aspect of the SDK's behavior. 

You've already seen how a client setting like `io.enableDnsSrv` can be [included in the connection string](#connection-string-params). Here are some other ways to configure client settings.

> [!TIP]
> It's fine to mix the different ways of specifying client settings. Just keep in mind the [precedence rules](#client-settings-precedence).

### [](#client-settings-system-property)System properties

The SDK looks for Java system properties whose names start with `com.couchbase.env.`. For each property it finds, it strips the prefix and interprets the rest of the name as client setting name. Since we've been using the `io.enableDnsSrv` client setting as an example, here's what it would look like to configure it with a Java system property on the command line:

```bash
$ java -Dcom.couchbase.env.io.enableDnsSrv=false ...
```

Alternatively, you can set a system property in code:

```kotlin
System.setProperty("com.couchbase.env.io.enableDnsSrv", "false")
```

Just make sure to set the property _before_ calling `Cluster.connect`, otherwise it has no effect.

### [](#client-settings-programmatic)Programmatic configuration

Finally, you can specify client settings by passing another argument to `Cluster.connect`. The extra argument configures the cluster's `ClusterEnvironment`. We'll talk more about cluster environments later, but for now you can think of an environment as something that holds client settings.

> [!NOTE]
> Client settings whose values are Kotlin/Java objects can _only_ be set programmatically. This includes settings like the default JSON serializer, the default retry strategy, etc.

There is a Domain-Specific Language (DSL) for configuring the environment, with a traditional builder as an alternative.

#### [](#cluster-env-dsl)Cluster Environment DSL

Setting `io.enableDnsSrv` using the DSL

```kotlin
val cluster = Cluster.connect(connectionString, username, password) {
    io {
        enableDnsSrv = false
    }
}
```

Each `.` in the setting name corresponds to a nested lambda in the DSL. For example, if you also wanted to configure the `io.kvCircuitBreaker.enabled` setting, you could write:

Setting `io.enableDnsSrv` and `io.kvCircuitBreaker.enabled` using the DSL

```kotlin
val cluster = Cluster.connect(connectionString, username, password) {
    io {
        enableDnsSrv = false

        kvCircuitBreaker {
            enabled = true
        }
    }
}
```

> [!TIP]
> If you type `this.` inside one of the DSL blocks, IntelliJ IDEA's code completion popup displays the settings available in that block.

#### [](#cluster-env-builder)Cluster Environment builder

There is also a traditional builder to use if you don't like the DSL.

Setting `io.enableDnsSrv` using a builder

```kotlin
val envBuilder = ClusterEnvironment.builder()
    .ioConfig(IoConfig.enableDnsSrv(false))

val cluster = Cluster.connect(connectionString, username, password, envBuilder)
```

### [](#client-settings-precedence)Client settings precedence

When the same setting is specified in different ways, for example as both a system property and a connection string parameter, a simple precedence rule determines which value is used.

System properties have the highest precedence, followed by connection string parameters. Programmatic configuration has the lowest precedence.

### [](#cloud-native-gateway-settings)Cloud Native Gateway Settings

Using the [Cloud Native Gateway](#howtos:managing-connections.adoc#cloud-native-gateway) protocol (to connect to Couchbase Server running on [Couchbase Autonomous Operator](../../../cloud-native-gateway/current/intro/about-cng.md) 2.6.1 or newer) should not need any changes to config.

Some settings will be ignored when using the `couchbase2://` protocol. Currently, these include:

* Compression
* `numKvConnections`

## [](#summary)Summary

To connect to Couchbase, create a `Cluster` object by calling `Cluster.connect`. Optionally, call `waitUntilReady` to wait for the connection to complete. If possible, share a single `Cluster` object across your whole application. When the Cluster is no longer needed, call `disconnect` to release resources.

A connection string includes at least one address to use for bootstrapping the connection, and may specify custom ports and parameters.

There are three different ways to configure client settings: Java system properties, connection string parameters, and programmatic configuration.