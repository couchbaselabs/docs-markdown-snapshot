---
title: Managing Connections
description: This section describes how to connect the Node.js SDK to a Couchbase cluster.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.5/modules/howtos/pages/managing-connections.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:4.5@nodejs-sdk:howtos:managing-connections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.5/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the Node.js SDK to a Couchbase cluster. It contains best practices as well as information on TLS/SSL and other advanced connection options. 

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to a Couchbase Server cluster is represented by a `Cluster` object. A `Cluster` provides access to Buckets, Scopes, and Collections, as well as various Couchbase services and management interfaces. The simplest way to create a `Cluster` object is to `const cluster = couchbase.connect` with a username, and password:

```javascript
var cluster = await couchbase.connect('couchbase://localhost', {
  username: 'Administrator',
  password: 'password',
})
```

If you're connecting to a Capella cluster, substitute the `localhost` line with the cluster's endpoint address.

Connecting to a Capella cluster

```javascript
const clusterConnStr = 'couchbases://cb.<your-endpoint>.cloud.couchbase.com'
```

`couchbases://` — note the final `s` — is needed for SSL. The Capella client certificate is included with the SDK.

For a self-managed cluster:

Connecting to a self-managed Couchbase cluster

```javascript
cluster = await couchbase.connect('couchbases://nodeA.example.com', {
  trustStorePath: '/path/to/ca/certificates.pem',
  username: 'Administrator',
  password: 'password',
})
```

> [!NOTE]
> If you are connecting to a version of Couchbase Server older than 6.5, it will be more efficient if the addresses are those of data (KV) nodes. You will in any case, with 6.0 and earlier, need to open a `` `Bucket `` instance before connecting to any other HTTP services (such as _Query_ or _Search_.

Connection String options are covered [in the API guide](https://docs.couchbase.com/sdk-api/couchbase-node-client/interfaces/ConnectOptions.html).

In a production environment, your connection string should include the addresses of multiple server nodes in case some are currently unavailable. Multiple addresses may be specified in a connection string by delimiting them with commas:

```javascript
cluster = await couchbase.connect(
  'couchbase://node1.example.com,node2.example.com',
  {
    username: 'Administrator',
    password: 'password',
  }
)
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

couchbase://127.0.0.1?network=external&operation_timeout=10.0

The full list of recognized parameters is documented in the [API reference](https://docs.couchbase.com/sdk-api/couchbase-node-client/interfaces/ConnectOptions.html).

A connection string may optionally be prefixed by either "couchbase://" or "couchbases://". If you wish to use TLS, the connection string must be configured as described in [Secure Connections](#ssl).

## [](#connection-lifecycle)Connection Lifecycle

We recommend creating a single `Cluster` instance when your application starts up, and sharing this instance throughout your application. Each of the respective sub-instances (Bucket, Collection, etc…​) of the Cluster class can be stored and re-used, or created in an on-demand fashion whenever needed.

Before your application stops, gracefully shut down the client by calling the `close()` method of each `Cluster` you created.

## [](#alternate-addresses-and-custom-ports)Alternate Addresses and Custom Ports

If your Couchbase Server cluster is running in a containerized, port mapped, or otherwise NAT'd environment like Docker or Kubernetes, a client running outside that environment may need additional information in order to connect to the cluster. Both the client and server require special configuration in this case.

On the server side, each server node must be configured to advertize its external address as well as any custom port mapping. This is done with the `setting-alternate-address` CLI command introduced in Couchbase Server 6.5\. A node configured in this way will advertise two addresses: one for connecting from the same network, and another for connecting from an external network.

On the client side, the externally visible ports must be used when connecting. If the external ports are not the default, you can specify custom ports by explicitly specifying them in the connection string:

```javascript
cluster = await couchbase.connect(
  'couchbase://localhost:1234?network=external',
  {
    username: 'Administrator',
    password: 'password',
  }
)
```

To verify how the connection string is being deconstructed by the library, our C SDK's `cbc connstr` may also be used:

```console
$ cbc connstr 'couchbase://localhost:1234,localhost:2345=http?network=external&timeout=10.0'
```

```console
Bucket:
Implicit port: 11210
SSL: DISABLED
Boostrap Protocols: CCCP,HTTP
Hosts:
  [memcached]         localhost:1234
  [restapi]           localhost:2345
Options:
  network=external
  timeout=10.0
```

In many cases the client is able to automatically select the correct set of addresses to use when connecting to a cluster that advertises multiple addresses.

If the detection heuristic fails in your environment, you can override it by setting the `network` client setting to `default` if the client and server are on the same network, or `external` if they're on different networks.

> [!NOTE]
> Any TLS certificates must be set up at the point where the connections are being made.

## [](#ssl)Secure Connections

Couchbase Server Enterprise Edition and Couchbase Capella support full encryption of client-side traffic using Transport Layer Security (TLS). This includes key-value type operations, queries, and configuration communication. Make sure you have the Enterprise Edition of Couchbase Server, or a Couchbase Capella account, before proceeding with configuring encryption on the client side.

For TLS verification the SDK uses the following certificates:

* The certificates in the Mozilla Root CA bundle (bundled with the SDK as of 4.2.4 and obtained from [curl](https://curl.se/docs/caextract.html)).
* The certificates in OpenSSL's default certificate store (as of 4.2.0).
* The self-signed root certificate that is used to sign Capella Certificates (bundled with the SDK as of 4.1.0).

The OpenSSL defaults can be overridden using the `SSL_CERT_DIR` and `SSL_CERT_FILE` environment variables. The `SSL_CERT_DIR` variable is used to set a specific directory in which the client should look for individual certificate files, whereas the `SSL_CERT_FILE` environment variable is used to point to a single file containing one or more certificates. More information can be found in the relevant [OpenSSL documentation](https://www.openssl.org/docs/man1.1.1/man3/SSL%5FCTX%5Fload%5Fverify%5Flocations.html).

Loading the Mozilla certificates can be disabled using the `disable_mozilla_ca_certificates` connection string parameter.

The Couchbase++ core's metadata provide information about where OpenSSL's default certificate store is located, which version of the Mozilla Root CA store is bundled with the SDK, and other useful details. You can obtain the metadata using the following command:

```console
$ node -p "JSON.parse(require('couchbase').cbppMetadata)"
```

```console
{
  ...
  mozilla_ca_bundle_date: 'Tue Jan 10 04:12:06 2023 GMT',
  mozilla_ca_bundle_embedded: true,
  mozilla_ca_bundle_sha256: 'fb1ecd641d0a02c01bc9036d513cb658bbda62a75e246bedbc01764560a639f0',
  mozilla_ca_bundle_size: 137,
  ...
  openssl_default_cert_dir: '/opt/homebrew/etc/openssl@1.1/certs',
  openssl_default_cert_dir_env: 'SSL_CERT_DIR',
  openssl_default_cert_file: '/opt/homebrew/etc/openssl@1.1/cert.pem',
  openssl_default_cert_file_env: 'SSL_CERT_FILE',
  ...
}
```

With debug-level logging enabled, if the Mozilla certificates have been loaded, a message with the information about the version of the Mozilla CA certificate store will be outputted. For example:

```console
[2023-05-17 15:54:23.907] [28822,310461] [debug] 7ms, [6d92f0-c4ba-d843-9d86-3c6839a2bed362]: loading 137 CA certificates from Mozilla bundle. Update date: "Tue Jan 10 04:12:06 2023 GMT", SHA256: "fb1ecd641d0a02c01bc9036d513cb658bbda62a75e246bedbc01764560a639f0"
```

* Couchbase Capella
* Couchbase Server

The Node.js SDK bundles Capella's standard root certificate by default. This means you don't need any additional configuration to enable TLS — simply use `couchbases://` in your connection string.

> [!NOTE]
> Capella's root certificate is **not** signed by a well known CA (Certificate Authority). However, as the certificate is bundled with the SDK, it is trusted by default.

Certificates from the Mozilla Root CA store are now bundled with the SDK. If the server's certificate is signed by a well-known CA (e.g., GoDaddy, Verisign, etc.), you don't need to configure this in the `SecurityConfig` settings, instead use `couchbases://` in your connection string.

You can still provide a certificate explicitly if necessary:

1. Get the CA certificate from the cluster and save it in a text file.
2. Enable encryption on the client side and point it to the file containing the certificate.

It is important to make sure you are transferring the certificate in an encrypted manner from the server to the client side, so either copy it through SSH, or through a similar secure mechanism.

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

The next step is to enable encryption and pass it the path to the certificate file (note the connection string scheme is `couchbases://` rather than the non-TLS `couchbase://`). Additionally, you need to provide your `username` and `password`:

```javascript
cluster = await couchbase.connect('couchbases://localhost', {
  trustStorePath: '/path/to/ca/certificates.pem',
  username: 'Administrator',
  password: 'password',
})
```

If you want to verify it's actually working, you can use a tool like `tcpdump`. For example, an unencrypted upsert request looks like this (using `sudo tcpdump -i lo0 -A -s 0 port 11210`):

E..e..@.@.............+......q{...#..Y.....
.E...Ey........9........................id{"key":"value"}

After enabling encryption, you cannot inspect the traffic in cleartext (same upsert request, but watched on port 11207 which is the default encrypted port):

E.....@.@.............+....Z.'yZ..#........
..... ...xuG.O=.#.........?.Q)8..D...S.W.4.-#....@7...^.Gk.4.t..C+......6..)}......N..m..o.3...d.,.     ...W.....U..
.%v.....4....m*...A.2I.1.&.*,6+..#..#.5

## [](#using-dns-srv-records)Using DNS SRV records

As an alternative to specifying multiple hosts in your program, you can get the actual bootstrap node list from a DNS SRV record. For Capella, where you only have one endpoint provided, it's good practice to always enable DNS-SRV on the client.

The following steps are necessary to make it work:

1. Set up your DNS server to respond properly from a DNS SRV request.
2. Enable it on the SDK and point it towards the DNS SRV entry.

### [](#setting-up-the-dns-server)Setting up the DNS Server

Capella gives you DNS-SRV by default — these instructions are for self-managed clusters, where you are responsible for your own DNS records.

Your DNS server zone file should be set up like this (one row for each bootstrap node):

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

The Node.js SDK always tries to use the SRV records, if the connection string contains a single hostname and the feature is not disabled explicitly with connection string option `dnssrv=off`.

In case of successful resolution a message like this will be written at `INFO` level of debug logs:

44ms [I4ebdb48d23db23b6] {10474} [INFO] (instance - L:219) Found host node.example.com:11210 via DNS SRV

If the DNS SRV records could not be loaded properly you'll get an exception logged and the given hostname will be used as an A record lookup.

81ms [If1e0caf208c1ff41] {11763} [INFO] (instance - L:202) DNS SRV lookup failed: LCB_ERR_UNKNOWN_HOST (1049). Ignore this if not relying on DNS SRV records

For most use cases, connecting client software using a Couchbase SDK to the [Couchbase Capella service](../../../home/cloud.md) is similar to connecting to an on-premises Couchbase Cluster. The use of DNS-SRV, Alternate Address, and TLS is covered above.

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region). As this may not always be possible during development, read the guidance on working with [constrained network environments](../ref/client-settings.md#commonly-used-options). More details on connecting your client code to Couchbase Capella can be found [in the Cloud docs](#cloud:clouds:connect.adoc#connecting-from-sdk-cli-or-cbsh).

### [](#troubleshooting-connections-to-cloud)Troubleshooting Connections to Cloud

Some DNS caching providers (notably, home routers) can't handle an SRV record that's large — if you have DNS-SRV issues with such a set-up, reduce your DNS-SRV to only include three records. \[_For development only, not production._\]. Our [Troubleshooting Cloud Connections](troubleshooting-cloud-connections.md) page will help you to diagnose this and other problems — as well as introducing the SDK doctor tool.