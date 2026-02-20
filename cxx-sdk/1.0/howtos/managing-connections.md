---
title: Managing Connections
description: This section describes how to connect the C++ SDK to a Couchbase cluster.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.0/modules/howtos/pages/managing-connections.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:1.0@cxx-sdk:howtos:managing-connections.adoc[]
---

[View original HTML](/cxx-sdk/1.0/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the C++ SDK to a Couchbase cluster. It contains best practices as well as information on TLS/SSL and advanced connection options, and a sub-page on troubleshooting Cloud connections. 

Our [Getting Started pages](#hello-world:start-using-sdk) cover the basics of making a connection to a Capella or self-managed Couchbase cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to a Couchbase cluster — on Capella, or self-managed — is represented by a cluster object. A cluster provides access to buckets, scopes, and collections, as well as various Couchbase services and management interfaces. The simplest way to create a `cluster` object is to call `couchbase::cluster::connect()` with a connection string, username, and password:

```c++
auto [err, cluster] = couchbase::cluster::connect(connection_string, options).get();
```

And here it is in the context of a full connection lifecycle:

```c++
#include <couchbase/cluster.hxx>
#include <couchbase/fmt/error.hxx>

#include <iostream>

int
main(int argc, const char* argv[])
{
    if (argc != 4) {
        fmt::println("USAGE: ./start_using couchbase://127.0.0.1 Administrator password");
        return 1;
    }

    std::string connection_string{ argv[1] }; // "couchbase://127.0.0.1"
    std::string username{ argv[2] };          // "Administrator"
    std::string password{ argv[3] };          // "password"
    std::string bucket_name{ "travel-sample" };

    auto options = couchbase::cluster_options(username, password);
    // customize through the 'options'.
    // For example, optimize timeouts for WAN
    options.apply_profile("wan_development");

    // [1] connect to cluster using the given connection string and the options
    auto [err, cluster] = couchbase::cluster::connect(connection_string, options).get();
    if (err) {
        fmt::println("Unable to connect to the cluster: {}", err);
        return 1;
    }

    // get a bucket reference
    auto bucket = cluster.bucket(bucket_name);

    // get a user-defined collection reference
    auto scope = bucket.scope("tenant_agent_00");
    auto collection = scope.collection("users");

    { // your database interactions here
    }

    // close cluster connection
    cluster.close().get();
    return 0;
}
```

If this were compiled as `start_using`, then the connection string and authentication credentials would be passed as arguments to the command like so:

```console
$ ./start_using couchbase://127.0.0.1 Administrator password
```

Here we’re talking to a local development cluster. For Capella, this will need `couchbases://` for TLS, followed by your Capella cluster name — see [Connect To Your Cluster](../../../cloud/get-started/connect.md). The client certificate for connecting to Capella is included in the C++ SDK installation.

## [](#connection-strings)Connection Strings

A Couchbase connection string is a comma-delimited list of IP addresses and/or hostnames, optionally followed by a list of parameters.

The parameter list is just like the query component of a URI; name-value pairs have an equals sign (`=`) separating the name and value, with an ampersand (`&`) between each pair. Just as in a URI, the first parameter is prefixed by a question mark (`?`).

Simple connection string with one seed node

127.0.0.1

Connection string with two seed nodes

nodeA.example.com,nodeB.example.com

Connection string with two parameters

127.0.0.1?network=external&key_value_timeout=10s

For the C++ SDK and its wrapper SDKs, this is the main method of passing client options, such as timeout options or I/O options. For more details see [Client Settings](../ref/client-settings.md), or the latest, complete listing in the \[API Reference\].

## [](#secure-connections)Secure Connections

Couchbase Server Enterprise Edition and Couchbase Capella support full encryption of client-side traffic using Transport Layer Security (TLS).

## [](#dealing-with-network-latency)Dealing With Network Latency

### [](#working-in-the-cloud)Working in the Cloud

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region). As this may not always be possible during development, read the guidance on working with [constrained network environments](../ref/client-settings.md#commonly-used-options). More details on connecting your client code to Couchbase Capella can be found [in the Cloud docs](../../../cloud/get-started/connect.md#connecting-your-sdk-to-capella).

> [!IMPORTANT]
> If you are connecting from _IPv6-only_ environment, you cannot connect to Couchbase Capella as you are unable to use the IPv4 records published for Capella clusters.

#### [](#troubleshooting-connections-to-cloud)Troubleshooting Connections to Cloud

Some DNS caching providers (notably, home routers) can’t handle an SRV record that’s large — if you have DNS-SRV issues with such a set-up, reduce your DNS-SRV to only include three records. \[_For development only, not production._\]. Our [Troubleshooting Cloud Connections](troubleshooting-cloud-connections.md) page will help you to diagnose this and other problems — as well as introducing the SDK doctor tool.

## [](#complex-environments)Complex Environments

### [](#alternate-addresses-and-custom-ports)Alternate Addresses and Custom Ports

If your Couchbase Server cluster is running in a containerized, port mapped, or otherwise NAT’d environment like Docker or Kubernetes, a client running outside that environment may need additional information in order to connect the cluster. Both the client and server require special configuration in this case.

## [](#using-dns-srv-records)Using DNS SRV records

As an alternative to specifying multiple hosts in your program, you can get the actual bootstrap node list from a DNS SRV record. For Capella, where you only have one endpoint provided, it’s good practice to always enable DNS-SRV on the client.

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

DNS SRV bootstrapping is enabled by default in the C++ SDK. In order to make the SDK use the SRV records, you need to pass in the hostname or host address from your records (here `1.1.1.1`), and can also pass in a timeout value:

```cpp
options.dns().timeout(std::chrono::seconds{1});
options.dns().nameserver("1.1.1.1");
```