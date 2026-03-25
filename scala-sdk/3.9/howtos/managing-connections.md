---
title: Managing Connections
description: This section describes how to connect the Scala SDK to a Couchbase cluster.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.9/modules/howtos/pages/managing-connections.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.9@scala-sdk:howtos:managing-connections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/3.9/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the Scala SDK to a Couchbase cluster. It contains best practices as well as information on TLS/SSL and advanced connection options, and a sub-page on troubleshooting Cloud connections. 

Our [Getting Started pages](#hello-world:start-using-sdk) cover the basics of making a connection to a Capella or self-managed Couchbase cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

The examples below use these imports:

```scala
import com.couchbase.client.scala._
import com.couchbase.client.scala.env._
import com.couchbase.client.scala.kv.GetResult
import reactor.core.scala.publisher.SMono

import java.nio.file.Path
import scala.concurrent.Future
import scala.concurrent.duration._
import scala.util.{Failure, Success, Try}
```

A connection to a Couchbase Server cluster is represented by a `Cluster` object. A `Cluster` provides access to buckets, scopes, and collections, as well as various Couchbase services and management interfaces. The simplest way to create a `Cluster` object is to call `Cluster.connect()` with a [connection string](#connection-strings) (or Capella endpoint), username, and password:

* Couchbase Capella
* Self-Managed Couchbase Server
* Cloud Native Gateway (CNG)

```scala
// Update this to your cluster
val endpoint = "cb.<your-endpoint>.cloud.couchbase.com"
val username = "username"
val password = "Password!123"
val bucketName = "travel-sample"

val env = ClusterEnvironment.builder
  .securityConfig(
    SecurityConfig()
      .enableTls(true)
  )
  // Sets a pre-configured profile called "wan-development" to help avoid latency issues
  // when accessing Capella from a different Wide Area Network
  // or Availability Zone (e.g. your laptop).
  .applyProfile(ClusterEnvironment.WanDevelopmentProfile)
  .build
  .get

val cluster = Cluster
  .connect(
    "couchbases://" + endpoint,
    ClusterOptions
      .create(username, password)
      .environment(env)
  )
  .get
```

Note, the client certificate for connecting to a Capella operational cluster is included in the SDK installation.

```scala
val clusterTry: Try[Cluster] =
  Cluster.connect("127.0.0.1", "username", "password")

clusterTry match {

  case Success(cluster) =>
    val bucket = cluster.bucket("beer-sample")
    val customerA = bucket.scope("customer-a")
    val widgets = customerA.collection("widgets")

    cluster.disconnect()

  case Failure(err) =>
    println(s"Failed to open cluster: $err")
}
```

Couchbase’s large number of ports across the URLs of many services can be proxied by using a `couchbase2://` endpoint as the connection string — currently only compatible with recent versions of [Couchbase Autonomous Operator](../../../operator/current/concept-cloud-native-gateway.md):

```scala
.connect(
  "couchbase2://10.12.14.16",
  ClusterOptions
    .create(username, password)
    .environment(env)
)
```

Read more on the [Connections](#cloud-native-gateway) page.

In a production environment, your connection string should include the addresses of multiple server nodes in case some are currently unavailable. Multiple addresses may be specified in a connection string by delimiting them with commas:

```scala
val connectionString = "192.168.56.101,192.168.56.102"
val cluster = Cluster.connect(connectionString, "username", "password")
```

> [!TIP]
> You don’t need to include the address of every node in the cluster. The client fetches the full address list from the first node it is able to contact.

### [](#waiting-for-bootstrap-completion)Waiting for Bootstrap Completion

Opening resources is asynchronous. That is, the call to `cluster.bucket` or `Cluster.connect` will complete instantly, and opening that resource will continue in the background.

You can force waiting for the resource to be opened with a call to `waitUntilReady`, which is available on both the `Cluster` and `Bucket`. Here is an example of using it on the bucket:

```scala
val clusterTry: Try[Cluster] =
  Cluster.connect("127.0.0.1", "username", "password")

clusterTry match {

  case Success(cluster) =>
    val bucket = cluster.bucket("beer-sample")

    bucket.waitUntilReady(30.seconds) match {
      case Success(_) =>
        val collection = bucket.defaultCollection
        // ... continue to use collection as normal ...

      case Failure(err) =>
        println(s"Failed to open bucket: $err")
    }

    cluster.disconnect()

  case Failure(err) =>
    println(s"Failed to open cluster: $err")
}
```

If not present, then the first Key Value (KV) operation on the bucket will wait for it to be ready. Any issues opening that bucket (for instance, if it does not exist), will result in an error being raised from that data operation.

Other timeout issues may occur when using the SDK located geographically separately from the Couchbase Server cluster — this is [not recommended in production deployments](../project-docs/compatibility.md#network-requirements), but often occurs during development. See the [Cloud section](#working-in-the-cloud) below for some suggestions of settings adjustments.

### [](#connection-strings)Connection Strings

A Couchbase connection string is a comma-delimited list of IP addresses and/or hostnames, optionally followed by a list of parameters.

The parameter list is just like the query component of a URI; name-value pairs have an equals sign (`=`) separating the name and value, with an ampersand (`&`) between each pair. Just as in a URI, the first parameter is prefixed by a question mark (`?`).

Simple connection string with one seed node

127.0.0.1

Connection string with two seed nodes

nodeA.example.com,nodeB.example.com

Connection string with two parameters

127.0.0.1?io.networkResolution=external&timeout.kvTimeout=10s

The full list of recognized parameters is documented in the client settings reference. Any client setting with a system property name may also be specified as a connection string parameter (without the `com.couchbase.env.` prefix).

> [!WARNING]
> When creating a `Cluster` using a custom `ClusterEnvironment`, **_connection string parameters are ignored_**, since client settings are frozen when the cluster environment is built.

### [](#cluster-environment)Cluster Environment

A `ClusterEnvironment` manages shared resources like thread pools, timers, and schedulers. It also holds the client settings. One way to customize the client’s behavior is to build your own `ClusterEnvironment` with custom settings:

```scala
val envTry: Try[ClusterEnvironment] = ClusterEnvironment.builder
  .timeoutConfig(TimeoutConfig().kvTimeout(10.seconds))
  .build

envTry match {

  case Success(env) =>
    val clusterTry = Cluster.connect(
      "127.0.0.1",
      ClusterOptions
        .create("username", "password")
        .environment(env)
    )

    clusterTry match {
      case Success(cluster) =>
        // ... use the Cluster

        // Shutdown gracefully by shutting down the environment after
        // any Clusters using it
        cluster.disconnect()
        env.shutdown()

      case Failure(err) => println(s"Failed to open cluster: $err")
    }

  case Failure(err) => println(s"Failed to create environment: $err")
}
```

This is a verbose example for simplicity, and the user may prefer to use `flatMap` or a for-comprehension to combine the multiple `Try`.

Note there are `com.couchbase.client.scala.env` and `com.couchbase.client.core.env` versions of all environment parameters: be sure to import the `.scala` versions.

> [!TIP]
> If you create a `Cluster` without specifying a custom environment, the client creates a default environment used exclusively by that `Cluster`. This default `ClusterEnvironment` is managed completely by the Scala SDK, and is automatically shut down when the associated `Cluster` is disconnected.

### [](#connection-lifecycle)Connection Lifecycle

Most of the high-level classes in the Scala SDK are designed to be safe for concurrent use by multiple threads. You will get the best performance if you share and reuse instances of `ClusterEnvironment`, `Cluster`, `Bucket`, `Scope`, and `Collection`, all of which are thread-safe.

We recommend creating a single `Cluster` instance when your application starts up, and sharing this instance throughout your application. If you know at startup time which buckets, scopes, and collections your application will use, we recommend obtaining them from the `Cluster` at startup time and sharing those instances throughout your application as well.

Before your application stops, gracefully shut down the client by calling the `disconnect()` method of each `Cluster` you created. If you created any `ClusterEnvironment` instances, call their `shutdown()` method after disconnecting the associated clusters.

### [](#multiple-clusters)Connecting to Multiple Clusters

If a single application needs to connect to multiple Couchbase Server clusters, we recommend creating a single `ClusterEnvironment` and sharing it between the `Clusters`. We will use a for-comprehension here to avoid excessive `Try` juggling.

```scala
val result = for {
  env <- ClusterEnvironment.builder
    .timeoutConfig(TimeoutConfig().kvTimeout(10.seconds))
    .build

  clusterA <- Cluster.connect(
    "clusterA.example.com",
    ClusterOptions
      .create("username", "password")
      .environment(env)
  )

  clusterB <- Cluster.connect(
    "clusterB.example.com",
    ClusterOptions
      .create("username", "password")
      .environment(env)
  )

  result <- doSomethingWithClusters(clusterA, clusterB)

  _ <- Success(clusterA.disconnect())
  _ <- Success(clusterB.disconnect())
  _ <- Success(env.shutdown())
} yield result

result match {
  case Failure(err) => println(s"Failure: $err")
  case _            =>
}
```

Remember, whenever you manually create a `ClusterEnvironment` like this, the SDK will not shut it down when you call `Cluster.disconnect()`. Instead you are responsible for shutting it down after disconnecting all clusters that share the environment.

## [](#ssl)Secure Connections

Both Couchbase Capella, and the [Enterprise Edition](../../../server/current/introduction/editions.md#enterprise-edition) of self-managed Couchbase Server, support full encryption of client-side traffic using Transport Layer Security (TLS). That includes data (key-value type) operations, queries, and configuration communication. Make sure you have the Enterprise Edition of Couchbase Server, or a Couchbase Capella account, before proceeding with configuring encryption on the client side.

* Couchbase Capella
* Self-Managed Couchbase Server

The Scala SDK bundles Capella’s standard root certificate by default. This means you don’t need any additional configuration to enable TLS — simply use `couchbases://` in your connection string.

> [!NOTE]
> Capella’s root certificate is **not** signed by a well known CA (Certificate Authority). However, as the certificate is bundled with the SDK, it is trusted by default.

As of SDK 1.4, if you connect to a Couchbase Server cluster with a root certificate issued by a trusted CA (Certificate Authority), you no longer need to configure this in the `securityConfig` settings.

The cluster’s root certificate just needs to be issued by a CA whose certificate is in the JVM’s trust store. This includes well known CAs (e.g., GoDaddy, Verisign, etc…​), plus any other CA certificates that you wish to add.

> [!TIP]
> The JVM’s trust store is represented by a file named `cacerts`, which can be found inside your Java installation folder.

You can still provide a certificate explicitly if necessary:

1. Get the CA certificate from the cluster and save it in a text file.
2. Enable encryption on the client side and point it to the file containing the certificate.

It is important to make sure you are transferring the certificate in an encrypted manner from the server to the client side, so either copy it through SSH or through a similar secure mechanism.

If you are running on `localhost` and just want to enable TLS for a development machine, just copying and pasting it suffices — _so long as you use `127.0.0.1` rather than `localhost` in the connection string_. This is because the certificate will not match the name _localhost_.

Navigate in the admin UI to **Settings** **Cluster** and copy the input box of the TLS certificate into a file on your machine (which we will refer to as `cluster.cert`). It looks similar to this:

-----BEGIN CERTIFICATE-----
MIICmDCCAYKgAwIBAgIIE4FSjsc3nyIwCwYJKoZIhvcNAQEFMAwxCjAIBgNVBAMT
ASowHhcNMTMwMTAxMDAwMDAwWhcNNDkxMjMxMjM1OTU5WjAMMQowCAYDVQQDEwEq
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzz2I3Gi1XcOCNRVYwY5R
................................................................
mgDnQI8nw2arBRoseLpF6WNw22CawxHVOlMceQaGOW9gqKNBN948EvJJ55Dhl7qG
BQp8sR0J6BsSc86jItQtK9eQWRg62+/XsgVCmDjrB5owHPz+vZPYhsMWixVhLjPJ
mkzeUUj/kschgQ0BWT+N+pyKAFFafjwFYtD0e5NwFUUBfsOyQtYV9xu3fw+T2N8S
itfGtmmlEfaplVGzGPaG0Eyr53g5g2BgQbi5l5Tt2awqhd22WOVbCalABd9t2IoI
F4+FjEqAEIr1mQepDaNM0gEfVcgd2SzGhC3yhYFBAH//8W4DUot5ciEhoBs=
-----END CERTIFICATE-----

The next step is to enable encryption and pass it the path to the certificate file.

```scala
val env = ClusterEnvironment.builder
   .securityConfig(
     SecurityConfig()
       .enableTls(true)
       .trustCertificate(Path.of("/path/to/cluster-root-certificate.pem"))
   )
  .build
  .get
```

Then use this custom `ClusterEnvironment` when opening the connection to the cluster. See [Cluster Environment](#cluster-environment) for an example of creating a `Cluster` with a custom environment.

If you want to verify it’s actually working, you can use a tool like `tcpdump`. For example, an unencrypted upsert request looks like this (using `sudo tcpdump -i lo0 -A -s 0 port 11210`):

E..e..@.@.............+......q{...#..Y.....
.E...Ey........9........................id{"key":"value"}

After enabling encryption, you cannot inspect the traffic in cleartext (same upsert request, but watched on port 11207 which is the default encrypted port):

E.....@.@.............+....Z.'yZ..#........
..... ...xuG.O=.#.........?.Q)8..D...S.W.4.-#....@7...^.Gk.4.t..C+......6..)}......N..m..o.3...d.,.	...W.....U..
.%v.....4....m*...A.2I.1.&.*,6+..#..#.5

The SDK includes the certificate for Capella. If you are working with a self-managed Couchbase cluster, add the certificate with:

```scala
ClusterEnvironment env = ClusterEnvironment.builder()
    .securityConfig(SecurityConfig.enableTls(true).trustCertificate(Paths.get("/path/to/cluster.cert"))).build();
```

## [](#alternate-addresses-and-custom-ports)Alternate Addresses and Custom Ports

If your Couchbase Server cluster is running in a containerized, port mapped, or otherwise NAT’d environment like Docker or Kubernetes, a client running outside that environment may need additional information in order to connect the cluster. Both the client and server require special configuration in this case.

On the server side, each server node must be configured to advertise its external address as well as any custom port mapping. This is done with the [setting-alternate-address CLI command](https://docs.couchbase.com/server/6.5/cli/cbcli/couchbase-cli-setting-alternate-address.html) introduced in Couchbase Server 6.5\. A node configured in this way will advertise two addresses: one for connecting from the same network, and another for connecting from an external network.

On the client side, the externally visible ports must be used when connecting. If the external ports are not the default, you can specify custom ports using the overloaded `Cluster.connect()` method that takes a set of `SeedNode` objects instead of a connection string.

```scala
val customKvPort = 1234
val customManagerPort = 2345
val seedNodes = Set(
  SeedNode("127.0.0.1", Some(customKvPort), Some(customManagerPort))
)

val cluster = Cluster.connect(seedNodes, ClusterOptions.create("username", "password"))
```

> [!TIP]
> In a deployment that uses multi-dimensional scaling, a custom KV port is only applicable for nodes running the KV service. A custom manager port may be specified regardless of which services are running on the node.

In many cases the client is able to automatically select the correct set of addresses to use when connecting to a cluster that advertises multiple addresses. If the detection heuristic fails in your environment, you can override it by setting the `io.networkResolution` client setting to `default` if the client and server are on the same network, or `external` if they’re on different networks.

> [!NOTE]
> Any TLS certificates must be set up at the point where the connections are being made.

## [](#using-dns-srv-records)Using DNS SRV records

As an alternative to specifying multiple hosts in your program, you can get the actual bootstrap node list from a DNS SRV record. For Capella, where you only have one endpoint provided, it’s good practice to always enable DNS-SRV on the client.

The following steps are necessary to make it work:

1. Set up your DNS server to respond properly from a DNS SRV request.
2. Enable it on the SDK and point it towards the DNS SRV entry.

### [](#setting-up-the-dns-server)Setting up the DNS Server

Capella gives you DNS-SRV by default — these instructions are for self-managed clusters, where you are responsible for your own DNS records.

Your DNS server zone file should be set up like this, with one row for each bootstrap (KV, a.k.a. Data Service) node:

; Service.Protocol.Domain	TTL	Class	Type	Priority	Weight	 Port	Target
_couchbases._tcp.example.com.	3600	IN	SRV	0		0	 11207	node1.example.com.
_couchbases._tcp.example.com.	3600	IN 	SRV	0		0	 11207	node2.example.com.
_couchbases._tcp.example.com.	3600	IN 	SRV	0		0	 11207	node3.example.com.

The first line comment is not needed in the record, we are showing the column headers here for illustration purposes. The myriad complexities of DNS are beyond the scope of this document, but note that SRV records must point to an A record, not a `CNAME`.

The order in which you list the nodes — and any value entered for `Priority` or `Weight` — will be ignored by the SDK. Nevertheless, best practice here is to set them to `0`, avoiding ambiguity.

Also note, the above is for connections using TLS. Should you be using an insecure connection (in testing or development, or totally within a firewalled environment), then your records would look like:

_couchbase._tcp.example.com.  3600  IN  SRV  0  0  11210  node1.example.com.
_couchbase._tcp.example.com.  3600  IN  SRV  0  0  11210  node2.example.com.
_couchbase._tcp.example.com.  3600  IN  SRV  0  0  11210  node3.example.com.

### [](#specifying-dns-srv-for-the-sdk)Specifying DNS-SRV for the SDK

* The connection string must be to a single hostname, with no explicit port specifier, pointing to the DNS SRV entry — `couchbases://example.com`.
* DNS-SRV must be enabled in the [client settings](../ref/client-settings.md).

DNS SRV bootstrapping is enabled by default in the Scala SDK. In order to make the SDK use the SRV records, you need to pass in the hostname from your records (here `example.com`):

```scala
ClusterEnvironment env = ClusterEnvironment.builder().ioConfig(IoConfig.enableDnsSrv(true)).build();
```

If the DNS SRV records could not be loaded properly you’ll get the exception logged and the given host name will be used as a A record lookup.

WARNING: DNS SRV lookup failed, proceeding with normal bootstrap.
javax.naming.NameNotFoundException: DNS name not found [response code 3];
   remaining name '_couchbase._tcp.example.com'
	at com.sun.jndi.dns.DnsClient.checkResponseCode(DnsClient.java:651)
	at com.sun.jndi.dns.DnsClient.isMatchResponse(DnsClient.java:569)

Also, if you pass in more than one node, DNS SRV bootstrap will not be initiated:

INFO: DNS SRV enabled, but less or more than one seed node given.
Proceeding with normal bootstrap.

## [](#cloud-native-gateway)Cloud Native Gateway

Couchbase’s next generation connection protocol, introduced in Scala SDK 1.5 and Couchbase Autonomous Operator 2.6.1, can be enabled simply by changing the connection string to `couchbase2://` but there are a few differences to be aware of, described [below](#limitations).

The protocol implements a gRPC-style interface between the SDK and Couchbase Server. (Only available with Couchbase Server running on Kubernetes or OpenShift, with a recent release of [Couchbase Autonomous Operator](../../../operator/current/overview.md): 2.6.1 onwards).

### [](#limitations)Limitations

The underlying protocol will not work with certain legacy features: MapReduce Views (a deprecated Service — use [Query](sqlpp-queries-with-sdk.md) instead) and Memcached buckets (superseded by the improved [Ephemeral Buckets](#8.0.0@server:learn:buckets-memory-and-storage/buckets.adoc#bucket-types)).

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

## [](#working-in-the-cloud)Working in the Cloud

For most use cases, connecting client software using a Couchbase SDK to the [Couchbase Capella service](../../../home/cloud.md) is similar to connecting to an on-premises Couchbase Cluster. The use of DNS-SRV, Alternate Address, and TLS is covered above.

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region). As this may not always be possible during development, read the guidance on working with [constrained network environments](../ref/client-settings.md#commonly-used-options). More details on connecting your client code to Couchbase Capella can be found [in the Cloud docs](#cloud:clouds:connect.adoc#connecting-from-sdk-cli-or-cbsh).

### [](#troubleshooting-connections-to-cloud)Troubleshooting Connections to Cloud

Some DNS caching providers (notably, home routers) can’t handle an SRV record that’s large — if you have DNS-SRV issues with such a set-up, reduce your DNS-SRV to only include three records. \[_For development only, not production._\]. Our [Troubleshooting Cloud Connections](troubleshooting-cloud-connections.md) page will help you to diagnose this and other problems — as well as introducing the SDK doctor tool.

## [](#async-and-reactive-apis)Async and Reactive APIs

The Couchbase Scala SDK provides first-class support for asynchronous and reactive programming. In fact, the synchronous API is just a thin wrapper around the asynchronous API.

Methods in the asynchronous API return instances of the standard Scala `Future`.

The Scala SDK’s reactive API is built on [Project Reactor](https://projectreactor.io) and the [Scala extensions](https://github.com/reactor/reactor-scala-extensions). Reactor implements the standard Reactive Streams API introduced in Scala 9, and extends it with a rich set of useful operators. Methods in the reactive API return instances of `SFlux` or `SMono`.

If you wish to embrace the async or reactive programming model, there are two ways to get started:

* Call `async` or `reactive` on the object to access its `Async*` or `Reactive*` counterpart. For example, if you have a `Collection` called `myCollection`, you can obtain a `ReactiveCollection` by calling `myCollection.reactive`.
* Instantiate an `AsyncCluster` or `ReactiveCluster` in the first place. The `bucket()` method of an `AsyncCluster` returns an `AsyncBucket`, while the `bucket()` method of a `ReactiveCluster` turns a `ReactiveBucket`.

So if you are connecting to the bucket synchronously but then want to switch over to asynchronous data operations, you can do it like this:

```scala
Cluster.connect("127.0.0.1", "username", "password") match {
  case Success(cluster: Cluster) =>
    val bucket: Bucket = cluster.bucket("travel-sample")
    val async: AsyncBucket = bucket.async
    val reactive: ReactiveBucket = bucket.reactive

    val r1: Try[GetResult] = bucket.defaultCollection.get("id")
    val r2: Future[GetResult] = async.defaultCollection.get("id")
    val r3: SMono[GetResult] = reactive.defaultCollection.get("id")

    cluster.disconnect()

  case Failure(err) => println(s"Failure: $err")
}
```

On the other hand, you can use the Async API right from the beginning:

```scala
AsyncCluster.connect("127.0.0.1", "username", "password") match {
  case Success(cluster: AsyncCluster) =>
    val async: AsyncBucket = cluster.bucket("travel-sample")

    cluster.disconnect()

  case Failure(err) => println(s"Failure: $err")
}
```

Here’s the same example, but using the Reactive API instead of the Async API:

```scala
ReactiveCluster.connect("127.0.0.1", "username", "password") match {
  case Success(cluster: ReactiveCluster) =>
    val async: ReactiveBucket = cluster.bucket("travel-sample")

    cluster.disconnect()

  case Failure(err) => println(s"Failure: $err")
}
```

## [](#next-steps)Next Steps

* [Certificate Authentication](#secure-connections.adoc)