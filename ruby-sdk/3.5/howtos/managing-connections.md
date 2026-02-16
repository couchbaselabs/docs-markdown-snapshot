[View original HTML](/ruby-sdk/3.5/howtos/managing-connections.html)

> This section describes how to connect the Ruby SDK to a Couchbase cluster. It contains best practices as well as information on TLS/SSL and other advanced connection options. 

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to a Couchbase Server cluster is represented by a `Cluster` object. A `Cluster` provides access to Buckets, Scopes, and Collections, as well as various Couchbase services and management interfaces. The simplest way to create a `Cluster` object is to call `Cluster.connect()` with a [connection string](#connection-strings), username, and password:

```ruby
require "couchbase"
include Couchbase # to avoid repeating module name
options = Cluster::ClusterOptions.new
options.authenticate("Administrator", "password")
cluster = Cluster.connect("couchbase://localhost", options)
```

|  | If you are connecting to a version of Couchbase Server older than 6.5, it will be more efficient if the addresses are those of data (KV) nodes. You will in any case, with 6.0 and earlier, need to open a Bucket instance before connecting to any other HTTP services (such as _Query_ or _Search_). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

In a production environment, your connection string should include the addresses of multiple server nodes in case some are currently unavailable. Multiple addresses may be specified in a connection string by delimiting them with commas:

```ruby
options = Couchbase::ClusterOptions.new
options.authenticator = Couchbase::PasswordAuthenticator.new("Administrator", "password")
cluster = Cluster.connect("couchbase://192.168.56.101,192.168.56.102", options)
```

|  | You don’t need to include the address of every node in the cluster. The client fetches the full address list from the first node it is able to contact. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#connection-strings)Connection Strings

A Couchbase connection string is a comma-delimited list of IP addresses and/or hostnames, optionally followed by a list of parameters.

The parameter list is just like the query component of a URI; name-value pairs have an equals sign (`=`) separating the name and value, with an ampersand (`&`) between each pair. Just as in a URI, the first parameter is prefixed by a question mark (`?`).

Simple connection string with one seed node

couchbase://127.0.0.1

Connection string with two seed nodes

couchbase://nodeA.example.com,nodeB.example.com

Connection string with two parameters

couchbases://127.0.0.1?enable_dns_srv=false&query_timeout=10000

The full list of recognized parameters is in the table below.

A connection string must be prefixed by either `couchbase://` or `couchbases://`.

## [](#connection-lifecycle)Connection Lifecycle

Most of the high-level classes in the Ruby SDK are designed to be safe for concurrent use by multiple threads.

We recommend creating a single `Cluster` instance when your application starts up, and sharing this instance throughout your application. If you know at startup time which buckets, scopes, and collections your application will use, we recommend obtaining them from the `Cluster` at startup time and sharing those instances throughout your application as well.

## [](#alternate-addresses)Alternate Addresses and Custom Ports

If your Couchbase Server cluster is running in a containerized, port mapped, or otherwise NATed environment like Docker or Kubernetes, a client running outside that environment may need additional information in order to connect the cluster. Both the client and server require special configuration in this case.

On the server side, each server node must be configured to advertise its external address as well as any custom port mapping. This is done with the `setting-alternate-address` [CLI command](../../../server/7.6/cli/cbcli/couchbase-cli-setting-alternate-address.md) introduced in Couchbase Server 6.5\. A node configured in this way will advertise two addresses: one for connecting from the same network, and another for connecting from an external network. This can also be set and retrieved [through the REST API](../../../server/7.6/rest-api/rest-set-up-alternate-address.md#assign-alternate-address-and-port-numbers).

On the client side, the externally visible ports must be used when connecting. If the external ports are not the default, you can specify custom ports explicitly in the connection string.

```ruby
options = Couchbase::ClusterOptions.new
options.authenticator = Couchbase::PasswordAuthenticator.new("Administrator", "password")
cluster = Cluster.connect("couchbase://192.168.42.101:12000,192.168.42.102:12002", options)
```

|  | In a deployment that uses multi-dimensional scaling, a custom KV port is only applicable for nodes running the KV service. A custom manager port may be specified regardless of which services are running on the node. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

In many cases the client is able to automatically select the correct set of addresses to use when connecting to a cluster that advertises multiple addresses. If the detection heuristic fails in your environment, you can override it by setting the `network` client setting to `default` if the client and server are on the same network, or\`external\` if they’re on different networks.

|  | Any TLS certificates must be set up at the point where the connections are being made. |
|  | -------------------------------------------------------------------------------------- |

## [](#ssl)Secure Connections

Couchbase Server Enterprise Edition and Couchbase Capella support full encryption of client-side traffic using Transport Layer Security (TLS). This includes key-value type operations, queries, and configuration communication. Make sure you have the Enterprise Edition of Couchbase Server, or a Couchbase Capella account, before proceeding with configuring encryption on the client side.

For TLS certificate verification the SDK uses the following CA certificates:

* The certificates in the Mozilla Root CA bundle (bundled with the SDK as of 3.4.3 and obtained from [curl](https://curl.se/docs/caextract.html)).
* The certificates in OpenSSL’s default CA certificate store (as of SDK 3.4.0).
* The self-signed root certificate that is used to sign the Couchbase Capella certificates (bundled with the SDK as of 3.3.0).

The OpenSSL defaults can be overridden using the `SSL_CERT_DIR` and `SSL_CERT_FILE` environment variables. The `SSL_CERT_DIR` variable is used to set a specific directory in which the client should look for individual certificate files, whereas the `SSL_CERT_FILE` environment variable is used to point to a single file containing one or more certificates. More information can be found in the relevant [OpenSSL documentation](https://www.openssl.org/docs/man1.1.1/man3/SSL%5FCTX%5Fload%5Fverify%5Flocations.html).

Loading the Mozilla certificates can be disabled by setting the `disable_mozilla_ca_certificates` parameter in the connection string.

The Couchbase++ core’s metadata provide information about where OpenSSL’s default certificate store is located, which version of the Mozilla CA certificate store was bundled, and other useful details. You can get the relevant metadata using the following command:

```console
$ ruby -r couchbase -e 'pp Couchbase::BUILD_INFO[:cxx_client].select{|k, _| k =~ /^(mozilla|openssl_default)/}'
```

```ruby
{:mozilla_ca_bundle_date=>"Tue Jan 10 04:12:06 2023 GMT",
 :mozilla_ca_bundle_embedded=>true,
 :mozilla_ca_bundle_sha256=>"fb1ecd641d0a02c01bc9036d513cb658bbda62a75e246bedbc01764560a639f0",
 :mozilla_ca_bundle_size=>137,
 :openssl_default_cert_dir=>"/etc/pki/tls/certs",
 :openssl_default_cert_dir_env=>"SSL_CERT_DIR",
 :openssl_default_cert_file=>"/etc/pki/tls/cert.pem",
 :openssl_default_cert_file_env=>"SSL_CERT_FILE"}
```

With debug-level logging enabled, if the Mozilla certificates have been loaded, a message with the information about the version of the Mozilla CA certificate store will be outputted. For example:

```console
loading 137 CA certificates from Mozilla bundle. Update date: "Tue Jan 10 04:12:06 2023 GMT", SHA256: "fb1ecd641d0a02c01bc9036d513cb658bbda62a75e246bedbc01764560a639f0"
```

* Couchbase Capella
* Couchbase Server

The Ruby SDK bundles Capella’s standard root certificate by default. This means you don’t need any additional configuration to enable TLS — simply use `couchbases://` in your connection string.

|  | Capella’s root certificate is **not** signed by a well known CA (Certificate Authority). However, as the certificate is bundled with the SDK, it is trusted by default. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Certificates from the Mozilla Root CA store are now bundled with the SDK (as of version 3.4.3). If the server’s certificate is signed by a well-known CA (e.g., GoDaddy, Verisign, etc.), you don’t need to configure the `trust_certificate` path in your connection string — simply use `couchbases://`.

You can still provide a certificate explicitly if necessary:

1. Get the CA certificate from the cluster and save it in a text file.
2. Enable encryption on the client side and point it to the file containing the certificate.

It is important to make sure you are transferring the certificate in an encrypted manner from the server to the client side, so either copy it through SSH or through a similar secure mechanism.

If you are running on `localhost` and just want to enable TLS for a development machine, just copying and pasting it suffices — _so long as you use `127.0.0.1` rather than `localhost` in the connection string_. This is because the certificate will not match the name _localhost_. Setting `tls_verify` to `none` is a workaround if you need to use `couchbases://localhost`.

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

The next step is to enable encryption by connecting to a cluster with the 'couchbases://' protocol in the connection string and pass it the path to the certificate file via '?trust\_certificate=…​' in the connection string itself.

```ruby
options = Couchbase::ClusterOptions.new
options.authenticator = Couchbase::PasswordAuthenticator.new("Administrator", "password")
cluster = Cluster("couchbases://127.0.0.1?trust_certificate=/path/to/certificate.pem", options)
```

Then use this custom `Cluster` when opening the connection to the cluster.

If you want to verify it’s actually working, you can use a tool like `tcpdump`. For example, an unencrypted upsert request looks like this (using `sudo tcpdump -i lo0 -A -s 0 port 11210`):

E..e..@.@.............+......q{...#..Y.....
.E...Ey........9........................id{"key":"value"}

After enabling encryption, you cannot inspect the traffic in cleartext (same upsert request, but watched on port 11207 which is the default encrypted port):

E.....@.@.............+....Z.'yZ..#........
..... ...xuG.O=.#.........?.Q)8..D...S.W.4.-#....@7...^.Gk.4.t..C+......6..)}......N..m..o.3...d.,.	...W.....U..
.%v.....4....m*...A.2I.1.&.*,6+..#..#.5

Unresolved include directive in modules/howtos/pages/managing-connections.adoc - include::7.5@sdk:shared:partial$dnssrv-pars.adoc\[\]

DNS SRV bootstrapping is enabled by default in the Ruby SDK. In order to make the SDK use the SRV records, you need to pass in the hostname from your records (here `example.com`):

```ruby
options = Couchbase::ClusterOptions.new
options.authenticator = Couchbase::PasswordAuthenticator.new("Administrator", "password")
cluster = Cluster.connect("couchbases://couchbase.example.com?enable_dns_srv=true", options)
```

If the DNS SRV records could not be loaded properly you’ll get the message logged and the given host name will be used as an A record lookup.

[2020-09-07 14:30:26.358] [186383,186390] [warning] 47ms, DNS SRV query returned 0 records for "localhost", assuming that cluster is listening this address

Unresolved include directive in modules/howtos/pages/managing-connections.adoc - include::7.5@sdk:shared:partial$managing-connections.adoc\[\]

## [](#further-reading)Further Reading

For more on RBAC, refer to the [Server docs](../../../server/7.6/learn/security/authorization-overview.md).