---
title: Managing Connections
description: This section describes how to connect the Kotlin SDK to a Couchbase cluster.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/release/3.9/modules/howtos/pages/managing-connections.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/kotlin-sdk/current/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the Kotlin SDK to a Couchbase cluster. It contains best practices as well as information on TLS/SSL and other advanced connection options. 

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to a Couchbase Server cluster is represented by a `Cluster` object. A `Cluster` provides access to Buckets, Scopes, and Collections, as well as various Couchbase services and management interfaces. The simplest way to create a `Cluster` object is to use the [Cluster.connect](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client/kotlin-client/com.couchbase.client.kotlin/-cluster/-companion/) companion factory method to create a [Cluster](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client/kotlin-client/com.couchbase.client.kotlin/-cluster/) object.

It’s best to create a single Cluster when your application starts up, and share it across your application. When your application shuts down, disconnect the Cluster. Disconnecting gives any in-flight requests a chance to complete, then releases the resources managed by the Cluster.

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

| **1** | If you’re connecting to Capella, enable TLS by using couchbases:// (note the final 's') instead of couchbase://. For more information about TLS, see [Secure Connections](secure-connections.md).                                                                                                                                                                                                                                                                                                                                              |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The Kotlin SDK uses [coroutines](https://kotlinlang.org/docs/coroutines-overview.html) for asynchronous execution. Many of the methods in the SDK are suspending functions, and can only be called from a coroutine context. The [runBlocking](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/run-blocking.html) method is a convenient way to create a coroutine context in a main method, in test code, or in some other blocking context, but should never be called from within another coroutine. |
| **3** | Cluster.connect returns immediately. The SDK continues working in the background to finish connecting. Waiting for the connection to complete is optional, but can be good because it lets you know right away if there is a problem with the connection. Waiting here also makes it less likely a following request times out, since none of the time allotted to the next request is spent waiting for the connection to complete.                                                                                                           |

In a production environment, your connection string should include the addresses of multiple server nodes in case some are currently unavailable. Multiple addresses may be specified in a connection string by delimiting them with commas:

```java
val connectionString = "foo.example.com,bar.example.com"
```

> [!TIP]
> You don’t need to include the address of every node in the cluster. The client fetches the full address list from the first node it is able to contact.

## [](#connection-strings)Connection Strings

A Couchbase connection string is a comma-delimited list of IP addresses and/or hostnames, optionally followed by a list of parameters.

The parameter list is just like the query component of a URI; name-value pairs have an equals sign (`=`) separating the name and value, with an ampersand (`&`) between each pair. Just as in a URI, the first parameter is prefixed by a question mark (`?`).

Simple connection string with one seed node

127.0.0.1

Connection string with two seed nodes

nodeA.example.com,nodeB.example.com

Connection string with two parameters

127.0.0.1?io.networkResolution=external&timeout.kvTimeout=10s

The full list of recognized parameters is documented in the client settings reference. Any client setting with a system property name may also be specified as a connection string parameter (without the `com.couchbase.env.` prefix).

## [](#alternate-addresses-and-custom-ports)Alternate Addresses and Custom Ports

If your Couchbase Server cluster is running in a containerized, port mapped, or otherwise NAT’d environment like Docker or Kubernetes, a client running outside that environment may need additional information in order to connect the cluster. Both the client and server require special configuration in this case.

On the server side, each server node must be configured to advertise its external address as well as any custom port mapping. This is done with the `setting-alternate-address` CLI command introduced in Couchbase Server 6.5\. A node configured in this way will advertise two addresses: one for connecting from the same network, and another for connecting from an external network.

On the client side, the externally visible ports must be used when connecting. If the external ports are not the default, you can specify custom ports in the connection string when calling `Cluster.connect()`.

By default, the Couchbase Key Value (KV) service listens on port 11210 (or 11207 for TLS), and the Manager service listens on port 8091 (or 18091 for TLS). The SDK can bootstrap against either service, but the KV service is preferable because it’s faster.

If the server is listening on a non-default port, or there is some kind of port mapping going on, include the port in the connection string:

Connection string with non-standard KV port

```kotlin
val connectionString = "foo.example.com:1234"
```

For nodes that do not have the KV service, you can connect using a custom manager port instead. Notice how `=manager` appears after the port number, identifying it as a manager port:

Connection string with non-standard Manager port

```kotlin
val connectionString = "foo.example.com:4567=manager"
```

> [!TIP]
> In a deployment that uses multi-dimensional scaling, a custom KV port is only applicable for nodes running the KV service. A custom manager port may be specified regardless of which services are running on the node.

In many cases the client is able to automatically select the correct set of addresses to use when connecting to a cluster that advertises multiple addresses. If the detection heuristic fails in your environment, you can override it by setting the `io.networkResolution` client setting to `default` if the client and server are on the same network, or `external` if they’re on different networks.

## [](#ssl)Secure Connections

Couchbase Server Enterprise Edition and Couchbase Capella support full encryption of client-side traffic using Transport Layer Security (TLS). That includes key-value type operations, queries, and configuration communication. Make sure you have the Enterprise Edition of Couchbase Server, or a Couchbase Capella account, before proceeding with configuring encryption on the client side.

* Couchbase Capella
* Couchbase Server

The Kotlin SDK bundles Capella’s standard root certificate by default. This means you don’t need any additional configuration to enable TLS — simply use `couchbases://` in your connection string.

> [!NOTE]
> Capella’s root certificate is **not** signed by a well known CA (Certificate Authority). However, as the certificate is bundled with the SDK, it is trusted by default.

As of SDK 1.1, if you connect to a Couchbase Server cluster with a root certificate issued by a trusted CA (Certificate Authority), you no longer need to configure this in the `securityConfig` settings.

The cluster’s root certificate just needs to be issued by a CA whose certificate is in the JVM’s trust store. This includes well known CAs (e.g., GoDaddy, Verisign, etc…​), plus any other CA certificates that you wish to add.

> [!TIP]
> The JVM’s trust store is represented by a file named `cacerts`, which can be found inside your installation folder.

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

```java
Unresolved include directive in modules/howtos/pages/managing-connections.adoc - include::devguide:example$java/ManagingConnections.java[]
```

If you want to verify it’s actually working, you can use a tool like `tcpdump`. For example, an unencrypted upsert request looks like this (using `sudo tcpdump -i lo0 -A -s 0 port 11210`):

E..e..@.@.............+......q{...#..Y.....
.E...Ey........9........................id{"key":"value"}

After enabling encryption, you cannot inspect the traffic in cleartext (same upsert request, but watched on port 11207 which is the default encrypted port):

E.....@.@.............+....Z.'yZ..#........
..... ...xuG.O=.#.........?.Q)8..D...S.W.4.-#....@7...^.Gk.4.t..C+......6..)}......N..m..o.3...d.,.	...W.....U..
.%v.....4....m*...A.2I.1.&.*,6+..#..#.5

## [](#cloud-native-gateway)Cloud Native Gateway

Couchbase’s next generation connection protocol, introduced in Kotlin SDK 1.2 and [Couchbase Autonomous Operator 2.6.1](../../../operator/current/concept-cloud-native-gateway.md), can be enabled simply by changing the connection string to `couchbase2://` but there are a few differences to be aware of, described [below](#limitations).

The protocol implements a gRPC-style interface between the SDK and Couchbase Server (in this case, only available in the Server running on Kubernetes or OpenShift, with a recent version of [Couchbase Autonomous Operator](../../../operator/current/overview.md)).

### [](#limitations)Limitations

The underlying protocol will not work with certain legacy features: MapReduce Views (a deprecated Service — use [Query](#howtos:n1ql-queries-with-sdk.adoc) instead) and Memcached buckets (superseded by the improved [Ephemeral Buckets](#8.0.0@server:learn:buckets-memory-and-storage/buckets.adoc#bucket-types)).

The following are not currently implemented over the `couchbase2://` protocol:

* Authentication by client certificate.
* Multi-document ACID transactions.
* Analytics service.
* Health Check.

And the output from these features should be seen as volatile and subject to change:

* Metrics and tracing, including the ThresholdLoggingTracer, LoggingMeter, and spans output.

There are some different behaviors seen with this protocol:

* Some config options are unsupported — see the [Settings page](../ref/client-settings.md#cloud-native-gateway).
* The SDK will poll the gRPC channels until they are in a good state, or return an error, or timeout while waiting — in our standard protocol there is an option of setting `waitUntilReady()` for just certain services to become available.
* Some error codes are more generic — in cases where the client would not be expected to need to take specific action — but should cause no problem, unless you have written code looking at individual strings within the error messages.
* Although documents continue to be stored compressed by Couchbase Server, they will not be transmitted in compressed form (to and from the client) over the wire, using `couchbase2://`.

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

DNS SRV bootstrapping is enabled by default in the Kotlin SDK. In order to make the SDK use the SRV records, you need to pass in the hostname from your records.

If the DNS SRV records could not be loaded properly you’ll get the exception logged and the given host name will be used as a A record lookup.

WARNING: DNS SRV lookup failed, proceeding with normal bootstrap.
javax.naming.NameNotFoundException: DNS name not found [response code 3];
   remaining name '_couchbase._tcp.example.com'
	at com.sun.jndi.dns.DnsClient.checkResponseCode(DnsClient.java:651)
	at com.sun.jndi.dns.DnsClient.isMatchResponse(DnsClient.java:569)

Also, if you pass in more than one node, DNS SRV bootstrap will not be initiated:

INFO: DNS SRV enabled, but less or more than one seed node given.
Proceeding with normal bootstrap.

## [](#waiting-for-bootstrap-completion)Waiting for Bootstrap Completion

Depending on the environment and network latency, bootstrapping the SDK fully might take a little longer than the default key-value timeout of 2.5 seconds, so you may see timeouts during bootstrap. To prevent those early timeouts from happening, you can use the `waitUntilReady` method.

You can also set timeouts through the connection string:

```kotlin
val connectionString =
    "foo.example.com?io.enableDnsSrv=false&timeout.kvTimeout=5s"
```

Other timeout issues may occur when using the SDK located geographically separately from the Couchbase Server cluster — this is [not recommended](../project-docs/compatibility.md#network-requirements). See the [Cloud section](#working-in-the-cloud) below for some suggestions of settings adjustments.

For most use cases, connecting client software using a Couchbase SDK to the [Couchbase Capella service](#cloud:ROOT:index.adoc) is similar to connecting to an on-premises Couchbase Cluster. The use of DNS-SRV, Alternate Address, and TLS is covered above.

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region). As this may not always be possible during development, read the guidance on working with [constrained network environments](../ref/client-settings.md#commonly-used-options). More details on connecting your client code to Couchbase Capella can be found [in the Cloud docs](#cloud:clouds:connect.adoc#connecting-from-sdk-cli-or-cbsh).

### [](#troubleshooting-connections-to-cloud)Troubleshooting Connections to Cloud

Some DNS caching providers (notably, home routers) can’t handle an SRV record that’s large — if you have DNS-SRV issues with such a set-up, reduce your DNS-SRV to only include three records. \[_For development only, not production._\]. Our [Troubleshooting Cloud Connections](troubleshooting-cloud-connections.md) page will help you to diagnose this and other problems — as well as introducing the SDK doctor tool.