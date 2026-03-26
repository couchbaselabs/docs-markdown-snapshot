---
title: Managing Connections
description: This section describes how to connect the Rust SDK to a Couchbase cluster.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/managing-connections.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:rust-sdk:howtos:managing-connections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the Rust SDK to a Couchbase cluster. It contains best practices as well as information on TLS/SSL and advanced connection options, and a sub-page on troubleshooting Cloud connections. 

Our [Getting Started pages](../hello-world/start-using-sdk.md) cover the basics of making a connection to a Capella or self-managed Couchbase cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to a Couchbase Server cluster is represented by a `Cluster` object. A `Cluster` provides access to buckets, scopes, and collections, as well as various Couchbase services and management interfaces. The simplest way to create a `Cluster` object is to call `Cluster.connect()` with a [connection string](#connection-strings) (or Capella endpoint), username, and password:

* Couchbase Capella
* Self-Managed Couchbase Server

```rust
// Update this to your cluster
let endpoint = "cb.<your-endpoint>.cloud.couchbase.com";
let username = "<your-username>";
let password = "<your-password>";
let bucket_name = "travel-sample";

let cluster_options = ClusterOptions::new(Authenticator::PasswordAuthenticator(
    PasswordAuthenticator::new(username.to_string(), password.to_string()),
));

let cluster = timeout(
    Duration::from_secs(30),
    Cluster::connect(format!("couchbases://{endpoint}"), cluster_options),
)
.await
.unwrap();
```

Note, the client certificate for connecting to a Capella operational cluster is included in the SDK installation.

```rust
// Update this to your cluster
let username = "<your-username>";
let password = "<your-password>";
let bucket_name = "travel-sample";

let cluster = timeout(
    Duration::from_secs(60),
    Cluster::connect(
        // For a secure cluster connection, use `couchbases://<your-cluster-ip>` instead.
        "couchbase://localhost",
        ClusterOptions::new(Authenticator::PasswordAuthenticator(
            PasswordAuthenticator::new(username, password),
        )),
    ),
)
.await
.unwrap();
```

In a production environment, your connection string should include the addresses of multiple server nodes in case some are currently unavailable. Multiple addresses may be specified in a connection string by delimiting them with commas:

```rust
let connection_string = "couchbase://node1.example.com,node2.example.com,node3.example.com";
let cluster = Cluster::connect(
    connection_string,
    ClusterOptions::new(Authenticator::PasswordAuthenticator(
        PasswordAuthenticator::new(username, password),
    )),
)
.await?;
```

> [!TIP]
> You don't need to include the address of every node in the cluster. The client fetches the full address list from the first node it is able to contact.

### [](#waiting-for-bootstrap-completion)Waiting for Bootstrap Completion

When `Cluster.connect` is called, the client begins bootstrapping the cluster connection, which includes fetching the cluster configuration and opening connections to all of the KV (Data Service) nodes. Opening resources after initial `Cluster.connect` is asynchronous. That is, the call to `cluster.bucket` will complete instantly, and opening that resource will continue in the background — for each bucket that you open the SDK will open a new set of KV connections and manage a different bucket configuration from the cluster.

You can force waiting for the resource to be opened with a call to `wait_until_ready`, which is available on both the `Cluster` and `Bucket`. Here is an example of using it on the bucket:

```rust
let bucket = cluster.bucket("travel-sample");
timeout(Duration::from_secs(30), bucket.wait_until_ready(None)).await?;
```

If not present, then the first Key Value (KV) operation on the bucket will wait for it to be ready. Any issues opening that bucket (for instance, if it does not exist), will result in an error being returned from that data operation.

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

The full list of recognized parameters is documented in the [client settings](../ref/client-settings.md) reference.

### [](#connection-lifecycle)Connection Lifecycle

Most of the high-level classes in the Rust SDK are designed to be safe for concurrent use by multiple threads. You will get the best performance if you share and reuse instances of `Cluster`, `Bucket`, `Scope`, and `Collection`, all of which are thread-safe.

We recommend creating a single `Cluster` instance when your application starts up, and sharing this instance throughout your application. If you know at startup time which buckets, scopes, and collections your application will use, we recommend obtaining them from the `Cluster` at startup time and sharing those instances throughout your application as well.

When the `Cluster` is dropped all active connections to the Couchbase Server cluster will be closed and all resources will be released. Any attempt to use any derived resources (buckets, scopes, collections, etc.) after the `Cluster` has been dropped will result in an error.

## [](#ssl)Secure Connections

Both Couchbase Capella, and the [Enterprise Edition](../../../server/current/introduction/editions.md#enterprise-edition) of self-managed Couchbase Server, support full encryption of client-side traffic using Transport Layer Security (TLS). That includes data (key-value type) operations, queries, and configuration communication. Make sure you have the Enterprise Edition of Couchbase Server, or a Couchbase Capella account, before proceeding with configuring encryption on the client side.

* Couchbase Capella
* Self-Managed Couchbase Server

The Rust SDK bundles Capella's standard root certificate by default. This means you don't need any additional configuration to enable TLS — simply use `couchbases://` in your connection string.

> [!NOTE]
> Capella's root certificate is **not** signed by a well known CA (Certificate Authority). However, as the certificate is bundled with the SDK, it is trusted by default.

You can provide a certificate:

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

```rust
// Unwrap used for brevity; handle errors as appropriate in production code.
let ca_cert = CertificateDer::from_pem_file("/path/to/cluster-root-certificate.pem").unwrap();

let cluster = Cluster::connect(
    "couchbases://node1.example.com",
    ClusterOptions::new(Authenticator::PasswordAuthenticator(
        PasswordAuthenticator::new(username, password),
    ))
    .tls_options(TlsOptions::new().add_ca_certificate(ca_cert)),
)
.await?;
```

If you want to verify it's actually working, you can use a tool like `tcpdump`. For example, an unencrypted upsert request looks like this (using `sudo tcpdump -i lo0 -A -s 0 port 11210`):

E..e..@.@.............+......q{...#..Y.....
.E...Ey........9........................id{"key":"value"}

After enabling encryption, you cannot inspect the traffic in cleartext (same upsert request, but watched on port 11207 which is the default encrypted port):

E.....@.@.............+....Z.'yZ..#........
..... ...xuG.O=.#.........?.Q)8..D...S.W.4.-#....@7...^.Gk.4.t..C+......6..)}......N..m..o.3...d.,.	...W.....U..
.%v.....4....m*...A.2I.1.&.*,6+..#..#.5

## [](#alternate-addresses-and-custom-ports)Alternate Addresses and Custom Ports

If your Couchbase Server cluster is running in a containerized, port mapped, or otherwise NAT'd environment like Docker or Kubernetes, a client running outside that environment may need additional information in order to connect the cluster. Both the client and server require special configuration in this case.

On the server side, each server node must be configured to advertise its external address as well as any custom port mapping. This is done with the [setting-alternate-address CLI command](https://docs.couchbase.com/server/6.5/cli/cbcli/couchbase-cli-setting-alternate-address.html) introduced in Couchbase Server 6.5\. A node configured in this way will advertise two addresses: one for connecting from the same network, and another for connecting from an external network.

On the client side, the externally visible ports must be used when connecting. If the external ports are not the default, you can specify custom ports in the connection string. The port where the data service is running must be specified

```none
127.0.0.1:11299
```

In many cases the client is able to automatically select the correct set of addresses to use when connecting to a cluster that advertises multiple addresses.

> [!NOTE]
> Any TLS certificates must be set up at the point where the connections are being made.

## [](#using-dns-srv-records)Using DNS SRV records

As an alternative to specifying multiple hosts in your program, you can get the actual bootstrap node list from a DNS SRV record. For Capella, where you only have one endpoint provided, it's good practice to always enable DNS-SRV on the client.

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

DNS SRV bootstrapping is enabled by default in the Rust SDK. In order to make the SDK use the SRV records, you need to pass in the hostname or host address from your records (here `1.1.1.1`), and can also pass in a timeout value:

```rust
let socket = "1.1.1.1:53".parse().unwrap();
opts = opts.dns_options(DnsOptions::new(socket).timeout(Duration::from_secs(1)));
```

> [!CAUTION]
> In the developer preview of the SDK, this feature is not part of the stable [Committed](../project-docs/compatibility.md#interface-stability) API. To enable it requires use of the `unstable-dns-options` — see the API reference for further information.

If the DNS SRV records could not be loaded properly you'll get an error logged and the given host name will be used as a A record lookup. Also, if you pass in more than one node, DNS SRV bootstrap will not be initiated:

## [](#working-in-the-cloud)Working in the Cloud

For most use cases, connecting client software using a Couchbase SDK to the [Couchbase Capella service](../../../home/cloud.md) is similar to connecting to an on-premises Couchbase Cluster. The use of DNS-SRV, Alternate Address, and TLS is covered above.

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region). As this may not always be possible during development, read the guidance on working with [constrained network environments](../ref/client-settings.md#commonly-used-options). More details on connecting your client code to Couchbase Capella can be found [in the Cloud docs](#cloud:clouds:connect.adoc#connecting-from-sdk-cli-or-cbsh).

### [](#troubleshooting-connections-to-cloud)Troubleshooting Connections to Cloud

Some DNS caching providers (notably, home routers) can't handle an SRV record that's large — if you have DNS-SRV issues with such a set-up, reduce your DNS-SRV to only include three records. \[_For development only, not production._\]. Our [Troubleshooting Cloud Connections](troubleshooting-cloud-connections.md) page will help you to diagnose this and other problems — as well as introducing the SDK doctor tool.

## [](#next-steps)Next Steps

* [Certificate Authentication](sdk-authentication.md#certificate-authentication)