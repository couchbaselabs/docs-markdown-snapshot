---
title: Managing Connections
description: This section describes how to connect the Python SDK to a Couchbase cluster.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.2/modules/howtos/pages/managing-connections.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:4.2@python-sdk:howtos:managing-connections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.2/howtos/managing-connections.html)

# Managing Connections

Please also refer to the [Server docs](../../../server/7.6/learn/security/authorization-overview.md).

> This section describes how to connect the Python SDK to a Couchbase cluster. It contains best practices as well as information on TLS/SSL and other advanced connection options. 

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to a Couchbase Server cluster is represented by a `Cluster` object. A `Cluster` provides access to Buckets, Scopes, and Collections, as well as various Couchbase services and management interfaces. The simplest way to create a `Cluster` object is to call `Cluster.connect()` with a [connection string](#connection-strings), username, and password:

```python
cluster = Cluster.connect("couchbase://your-ip", ClusterOptions(PasswordAuthenticator("Administrator", "password")))
bucket = cluster.bucket("travel-sample")
collection = bucket.default_collection()

# You can access multiple buckets using the same Cluster object.
another_bucket = cluster.bucket("beer-sample")

# You can access collections other than the default
# if your version of Couchbase Server supports this feature.
customer_a = bucket.scope("customer-a")
widgets = customer_a.collection("widgets")
```

> [!NOTE]
> If you are connecting to a version of Couchbase Server older than 6.5, it will be more efficient if the addresses are those of data (KV) nodes. You will in any case, with 6.0 and earlier, need to open a `` `Bucket `` instance before connecting to any other HTTP services (such as _Query_ or _Search_).

In a production environment, your connection string should include the addresses of multiple server nodes in case some are currently unavailable. Multiple addresses may be specified in a connection string by delimiting them with commas:

```python
cluster = Cluster.connect("couchbase://node1.example.com,node2.example.com", ClusterOptions(PasswordAuthenticator("Administrator", "password")))
```

> [!TIP]
> You don't need to include the address of every node in the cluster. The client fetches the full address list from the first node it is able to contact.

## [](#connection-strings)Connection Strings

A Couchbase connection string is a comma-delimited list of IP addresses and/or hostnames, optionally followed by a list of parameters.

The parameter list is just like the query component of a URI; name-value pairs have an equals sign (`=`) separating the name and value, with an ampersand (`&`) between each pair. Just as in a URI, the first parameter is prefixed by a question mark (`?`).

Simple connection string with one seed node

couchbase://127.0.0.1

Connection string with two seed nodes

couchbase://nodeA.example.com,nodeB.example.com

Connection string with two parameters

couchbases://127.0.0.1?compression=on&redaction=on

The full list of recognized parameters is documented in the client settings reference. Any client setting with a system property name may also be specified as a connection string parameter.

A connection string may optionally be prefixed by either `"couchbase://"` or `"couchbases://"`.

### [](#connection-options)Connection Options

The backend implementation of connection strings parameters changed substantially in 4.0\. See [more details on migrating to 4.0](../project-docs/migrating-sdk-code-to-3.n.md#sdk4-specifics).

[Configuring client settings with ClusterOptions()](../ref/client-settings.md#cluster-options) is the preferred option. More details can be found in the [API reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/couchbase%5Fapi/options.html#cluster).

## [](#connection-lifecycle)Connection Lifecycle

Most of the high-level classes in the Python SDK are designed to be safe for concurrent use by multiple threads. For asynchronous modes, you will get the best performance if you share and reuse instances of `Cluster`, `Bucket`, `Scope`, and `Collection`, all of which are thread-safe. For synchronous mode, it is better to use separate instances in different threads.

We recommend creating a single `Cluster` instance when your application starts up, and sharing this instance throughout your application. If you know at startup time which buckets, scopes, and collections your application will use, we recommend obtaining them from the `Cluster` at startup time and sharing those instances throughout your application as well.

## [](#alternate-addresses)Alternate Addresses and Custom Ports

If your Couchbase Server cluster is running in a containerized, port mapped, or otherwise NAT'd environment like Docker or Kubernetes, a client running outside that environment may need additional information in order to connect the cluster. Both the client and server require special configuration in this case.

On the server side, each server node must be configured to advertise its external address as well as any custom port mapping. This is done with the `setting-alternate-address` CLI command introduced in Couchbase Server 6.5\. A node configured in this way will advertise two addresses: one for connecting from the same network, and another for connecting from an external network.

> [!NOTE]
> Any TLS certificates must be set up at the point where the connections are being made.

## [](#ssl)Secure Connections

> [!WARNING]
> If the client cannot load or was not built with OpenSSL, attempting a TLS connection will result in a 'FEATURE\_UNAVAILABLE'.

Couchbase Server Enterprise Edition and Couchbase Capella support full encryption of client-side traffic using Transport Layer Security (TLS). This includes key-value type operations, queries, and configuration communication. Make sure you have the Enterprise Edition of Couchbase Server, or a Couchbase Capella account, before proceeding with configuring encryption on the client side.

For TLS certificate verification the SDK uses the following CA certificates:

* The certificates in the Mozilla Root CA bundle (bundled with the SDK as of 4.1.5 and obtained from [curl](https://curl.se/docs/caextract.html)).
* The certificates in OpenSSL's default CA certificate store (as of SDK 4.1.0).
* The self-signed root certificate that is used to sign the Couchbase Capella certificates (bundled with the SDK as of 4.0.0).

The OpenSSL defaults can be overridden using the `SSL_CERT_DIR` and `SSL_CERT_FILE` environment variables. The `SSL_CERT_DIR` variable is used to set a specific directory in which the client should look for individual certificate files, whereas the `SSL_CERT_FILE` environment variable is used to point to a single file containing one or more certificates. More information can be found in the relevant [OpenSSL documentation](https://www.openssl.org/docs/man1.1.1/man3/SSL%5FCTX%5Fload%5Fverify%5Flocations.html).

Loading the Mozilla certificates can be disabled by setting the `disable_mozilla_ca_certificates` property of `ClusterOptions`.

The Couchbase++ core's metadata provide information about where OpenSSL's default certificate store is located, which version of the Mozilla CA certificate store was bundled, and other useful details. You can get the metadata using the following command:

```console
$ python -c "from couchbase import get_metadata; print(get_metadata(detailed=True))"
```

```console
{
 ...
 'mozilla_ca_bundle_date': 'Tue Jan 10 04:12:06 2023 GMT',
 'mozilla_ca_bundle_embedded': True,
 'mozilla_ca_bundle_sha256': 'fb1ecd641d0a02c01bc9036d513cb658bbda62a75e246bedbc01764560a639f0',
 'mozilla_ca_bundle_size': 137,
 ...
 'openssl_default_cert_dir': '/opt/homebrew/etc/openssl@1.1/certs',
 'openssl_default_cert_dir_env': 'SSL_CERT_DIR',
 'openssl_default_cert_file': '/opt/homebrew/etc/openssl@1.1/cert.pem',
 'openssl_default_cert_file_env': 'SSL_CERT_FILE',
 ...
}
```

With debug-level logging enabled, if the Mozilla certificates have been loaded, a message with the information about the version of the Mozilla CA certificate store will be outputted. For example:

```console
loading 137 CA certificates from Mozilla bundle. Update date: "Tue Jan 10 04:12:06 2023 GMT", SHA256: "fb1ecd641d0a02c01bc9036d513cb658bbda62a75e246bedbc01764560a639f0"
```

* Couchbase Capella
* Couchbase Server

The Python SDK bundles Capella's standard root certificate by default. This means you don't need any additional configuration to enable TLS — simply use `couchbases://` in your connection string.

> [!NOTE]
> Capella's root certificate is **not** signed by a well known CA (Certificate Authority). However, as the certificate is bundled with the SDK, it is trusted by default.

Certificates from the Mozilla Root CA store are now bundled with the SDK (as of version 4.1.5). If the server's certificate is signed by a well-known CA (e.g., GoDaddy, Verisign, etc.), you don't need to configure the `cert_path` property in the `PasswordAuthenticator` — simply use `couchbases://` in your connection string.

You can still provide a certificate explicitly if necessary:

1. Get the CA certificate from the cluster and save it in a text file.
2. Enable encryption on the client side and point it to the file containing the certificate.

It is important to make sure you are transferring the certificate in an encrypted manner from the server to the client side, so either copy it through SSH or through a similar secure mechanism.

If you are running on `localhost` and just want to enable TLS for a development machine, just copying and pasting it suffices — _so long as you use `127.0.0.1` rather than `localhost` in the connection string_. This is because the certificate will not match the name _localhost_.

Navigate in the admin UI to **Settings** **Cluster** and copy the input box of the TLS certificate into a file on your machine (which we will refer to as `cluster.crt`). It looks similar to this:

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

The next step is to enable encryption by connecting to a cluster with the 'couchbases://' protocol in the connection string and pass it the path to the certificate file via an Authenticator, or via '?cert\_path=…​' in the connection string itself.

```python
cluster = Cluster("couchbases://your-ip",ClusterOptions(PasswordAuthenticator("Administrator","password",cert_path="/path/to/cluster.crt")))
```

Then use this custom `Cluster` when opening the connection to the cluster.

If you want to verify it's actually working, you can use a tool like `tcpdump`. For example, an unencrypted upsert request looks like this (using `sudo tcpdump -i lo0 -A -s 0 port 11210`):

E..e..@.@.............+......q{...#..Y.....
.E...Ey........9........................id{"key":"value"}

After enabling encryption, you cannot inspect the traffic in cleartext (same upsert request, but watched on port 11207 which is the default encrypted port):

E.....@.@.............+....Z.'yZ..#........
..... ...xuG.O=.#.........?.Q)8..D...S.W.4.-#....@7...^.Gk.4.t..C+......6..)}......N..m..o.3...d.,.	...W.....U..
.%v.....4....m*...A.2I.1.&.*,6+..#..#.5

## [](#working-in-the-cloud)Working in the Cloud

For most use cases, connecting client software using a Couchbase SDK to the [Couchbase Capella service](../../../home/cloud.md) is similar to connecting to an on-premises Couchbase Cluster. The use of DNS-SRV, Alternate Address, and TLS is covered above.

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region). As this may not always be possible during development, read the guidance on working with [constrained network environments](../ref/client-settings.md#commonly-used-options). More details on connecting your client code to Couchbase Capella can be found [in the Cloud docs](../../../cloud/get-started/connect.md#connecting-your-sdk-to-capella).

### [](#troubleshooting-connections-to-cloud)Troubleshooting Connections to Cloud

Some DNS caching providers (notably, home routers) can't handle an SRV record that's large — if you have DNS-SRV issues with such a set-up, reduce your DNS-SRV to only include three records. \[_For development only, not production._\]. Our [Troubleshooting Cloud Connections](troubleshooting-cloud-connections.md) page will help you to diagnose this and other problems — as well as introducing the SDK doctor tool.

## [](#async-apis)Async APIs

The Couchbase Python SDK provides first-class support for asynchronous programming. The supported asynchronous APIs offer a similar API to the synchronous API.

Methods in the asynchronous API return instances of the relevant Async API:

1. `Future` for asyncio (`acouchbase.cluster.Cluster` supplies the relevant Cluster object)
2. `Deferred` for Twisted

Reference our [asynchronous programming](concurrent-async-apis.md) page for more details.