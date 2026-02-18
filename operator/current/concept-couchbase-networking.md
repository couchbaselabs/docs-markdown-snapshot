---
title: Couchbase Networking
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.9/modules/ROOT/pages/concept-couchbase-networking.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/operator/current/concept-couchbase-networking.html)

# Couchbase Networking

> Connecting to a Couchbase cluster in Kubernetes is challenging. This section outlines supported strategies and key concepts. 

Couchbase Server is a high performance database, where data is distributed across all pods in a cluster. Clients are aware of which pod a data item should reside on and perform client-side load balancing. By performing the load balancing in the client, this avoids unnecessary network hops and improves performance. For this reason Couchbase Server cannot be accessed using normal Kubernetes `Service` or `Ingress` resources, unless accessed via [Cloud Native Gateway](concept-cloud-native-gateway.md) (CNG).

The following options depict the possible networking topologies for connecting clients to a Couchbase cluster. Clients includes all Couchbase Client SDKs, Couchbase Mobile and Couchbase XDCR connections unless otherwise stated.

## [](#intra-kubernetes-networking)Intra-Kubernetes Networking

Intra-Kubernetes networking is the simplest and allow clients running in the same Kubernetes cluster as the Couchbase server instance. This method of communication can be used by any client.

![networking basic intra](_images/networking-basic-intra.png) 

Figure 1\. Basic Intra-Kubernetes Networking

The client can use endpoint DNS entries to connect to individual Couchbase nodes. Stable service discovery is provided by SRV records. TLS can be used to secure communications.

Learn More

* [How-to connect to the UI](howto-ui.md#port-forwarding)
* [How-to connect a client SDK](howto-client-sdks.md#dns-based-addressing)
* [How-to configure XDCR](howto-xdcr.md#dns-based-addressing)

## [](#inter-kubernetes-networking-with-forwarded-dns)Inter-Kubernetes Networking with Forwarded DNS

Inter-Kubernetes networking allows clients to connect to Couchbase server instances in a remote Kubernetes cluster. It uses the DNS service offered by the remote Kubernetes cluster to provide addressing.

A local DNS server is used by Couchbase Server and clients to forward DNS requests for a remote namespace to a remote Kubernetes cluster. Requests that do not fall into this DNS zone are forwarded to the local DNS service. Any DNS server that supports forwarding of zones to remote DNS servers can be used, but we recommend [CoreDNS](https://coredns.io) as the de facto cloud native standard.

This method of communication can only be used if clients in one cluster can communicate with pods in another — it uses [routed networking](concept-kubernetes-networking.md#routed-networking). For example:

* Google GKE allows multiple Kubernetes clusters in the same virtual private cloud, and has routed networking by default.
* Amazon AWS can use the [VPC CNI plugin](https://github.com/aws/amazon-vpc-cni-k8s) to create routed networks that can be peered together.

![networking basic forwarded dns](_images/networking-basic-forwarded-dns.png) 

Figure 2\. Basic Inter-Kubernetes Networking

The client can use endpoint DNS entries to connect to individual Couchbase nodes. Stable service discovery is provided by SRV records. TLS can be used to secure communications.

Learn More

* [How-to connect to the UI](howto-ui.md#port-forwarding)
* [How-to connect a client SDK](howto-client-sdks.md#dns-based-addressing)
* [How-to configure XDCR](howto-xdcr.md#dns-based-addressing)
* [Inter-Kubernetes networking with forwarded DNS tutorial](tutorial-remote-dns.md)

## [](#public-networking-with-external-dns)Public Networking with External DNS

Public networking allows clients to connect to Couchbase server instances from anywhere with an Internet connection.

[External DNS](https://github.com/kubernetes-sigs/external-dns) is a service that can be run in a Kubernetes namespace. It allows services to advertise load-balancer service public IP addresses with public DDNS services. This networking type requires [Exposed Features](#exposed-features), which has its own [client requirements and limitations](#exposed-features-client-requirements).

![networking basic external dns](_images/networking-basic-external-dns.png) 

Figure 3\. Basic Public Networking

The client can use DNS names for load-balancer service public IP addresses to connect to individual Couchbase nodes. Stable service discovery is provided by a load-balanced HTTP connection to the cluster admin service. TLS must be used to secure communications.

Learn More

* [How-to configure public networking](howto-public-networking.md)
* [How-to connect to the UI](howto-ui.md#dns-based-addressing)
* [How-to connect a client SDK](howto-client-sdks.md#dns-based-addressing-with-external-dns)
* [How-to configure XDCR](howto-xdcr.md#dns-based-addressing-with-external-dns)
* [Public networking tutorial](tutorial-public-addressability.md)

## [](#generic-networking)Generic Networking

Generic networking use is discouraged for production deployments. It should be avoided in preference for one of the prior methods of communication. This networking type requires [Exposed Features](#exposed-features), which has its own [client requirements and limitations](#exposed-features-client-requirements).

![networking basic nodeport](_images/networking-basic-nodeport.png) 

Figure 4\. Generic Networking

The client uses Kubernetes node ports to connect to individual Couchbase nodes. Stable service discovery is not possible. TLS cannot be used to secure communications.

> [!IMPORTANT]
> When using Istio or another service mesh, remember that strict mode mTLS cannot be used with Kubernetes node ports.

Learn More

* [How-to configure node port networking](howto-nodeport-networking.md)
* [How-to connect to the UI](howto-ui.md#port-forwarding)
* [How-to connect a client SDK](howto-client-sdks.md#ip-based-addressing)
* [How-to configure XDCR](howto-xdcr.md#ip-based-addressing)

## [](#exposed-features)Exposed Features

Both [Public Networking with External DNS](#public-networking-with-external-dns) and [Generic Networking](#generic-networking) require client traffic to cross as DNAT boundary. In both cases clients connect to different IP addresses than those of the underlying Couchbase pods. As a result when clients initially contact Couchbase Server to get a map of nodes and their hostnames then Operator must override the internal Kubernetes DNS names.

Setting [couchbaseclusters.spec.networking.exposedFeatures](resource/couchbasecluster.md#couchbaseclusters-spec-networking-exposedfeatures) when creating a Couchbase cluster will instruct the Operator to override node mappings so that clients can connect to the correct IP address that a client can connect to. It will also cause the Operator to create separate services that are visible external to the Kubernetes cluster.

Additionally [couchbaseclusters.spec.networking.dns.domain](resource/couchbasecluster.md#couchbaseclusters-spec-networking-dns-domain) is specified when using [Public Networking with External DNS](#public-networking-with-external-dns), populating the cluster node maps with DNS names and annotating the services so [External DNS](https://github.com/kubernetes-sigs/external-dns) can replicate this to a cloud DDNS service provider.

### [](#exposed-features-client-requirements)Supported Client Versions for use with Exposed Features

As [Public Networking with External DNS](#public-networking-with-external-dns) and [Generic Networking](#generic-networking) require exposed features, clients need to be able to support this feature. The minimum versions are specified below.

__Table 1\. Couchbase Clients That Support Exposed Features__
| Client                            | Version                                                                                                                                                                                                                    |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Couchbase Server (XDCR)           | 6.0.1+ 5.5.3+                                                                                                                                                                                                              |
| Node.js SDK                       | 2.5.0+ When not using the embedded libcouchbase and choosing to build with an external installation, libcouchbase 2.9.2+ is required.                                                                                      |
| PHP SDK                           | Any supported version using libcouchbase 2.9.2+                                                                                                                                                                            |
| Python SDK                        | Any supported version using libcouchbase 2.9.2+                                                                                                                                                                            |
| C SDK (a.k.a. libcouchbase)       | 2.9.2+                                                                                                                                                                                                                     |
| Java SDK                          | 2.7.7+                                                                                                                                                                                                                     |
| .NET SDK                          | 2.7.9+                                                                                                                                                                                                                     |
| Go SDK                            | 1.6.1+                                                                                                                                                                                                                     |
| Couchbase Sync Gateway            | 2.7.0+ \* \*Earlier versions of Sync Gateway have limited support for exposed features. For more information, refer to [Sync Gateway Limitations When Using Exposed Features](#sync-gateway-exposed-features-limitations). |
| Couchbase Elasticsearch Connector | 4.1.0+                                                                                                                                                                                                                     |
| Couchbase Kafka Connector         | 3.4.5+                                                                                                                                                                                                                     |

> [!NOTE]
> A known issue exists ([K8S-1585](https://issues.couchbase.com/browse/K8S-1585)) where lookup may fail when using DNS SRV over TLS to connect to a Couchbase Cluster in the same Kubernetes cluster. In such cases, the workaround is to add wildcard matches to the Subject Alternate Names (SANs) as discussed in the [Creating TLS Certificates](tutorial-tls.md#creating-a-couchbase-cluster-server-certificate) tutorial.

#### [](#sync-gateway-exposed-features-limitations)Sync Gateway Limitations When Using Exposed Features

Earlier versions of Sync Gateway can experience certain network limitations when connecting to a Couchbase cluster that is configured with [exposed features](#exposed-features). [Table 2](#table-sgw-exposed-features-limitations) describes the different network limitations that can occur based on the version of Sync Gateway that is being used.

> [!IMPORTANT]
> Sync Gateway, like other Couchbase clients, does not require exposed features to be configured in order to establish a network connection with an instance of Couchbase Server that is running on the same local Kubernetes cluster. The rows labeled **Local** in [Table 2](#table-sgw-exposed-features-limitations) assume that you already have exposed features configured for a different purpose, e.g. exposing the admin port for remote administration, connecting to a remote cluster for XDCR, etc. However, if you are running Sync Gateway on the same Kubernetes cluster as Couchbase Server, and there is nothing else requiring you to configure [couchbaseclusters.spec.networking.exposedFeatures](resource/couchbasecluster.md#couchbaseclusters-spec-networking-exposedfeatures) for a different purpose, then you can ignore the rest of this section as this issue will not affect you.

__Table 2\. Supported Connection Methods for Sync Gateway When Using Exposed Features__
| Sync Gateway Version | Relationship to Cluster | Method                                                   | Connection String                                                               | High Availability |
| -------------------- | ----------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------------- |
| 2.8.2+               | **Local**               | DNS SRV                                                  | couchbase://my-cluster-srv.my-namespace?network=default                         | ✅ Yes             |
| **Remote**           | DNS SRV                 | couchbase://my-cluster-srv.my-namespace?network=external | ✅ Yes                                                                           |                   |
| 2.8.0,2.7.3          | **Local**               | DNS address                                              | couchbase://pod-0.my-cluster.my-namespace.svc,pod-1.my-cluster.my-namespace.svc | 🚫 No             |
| **Remote**           | DNS SRV                 | couchbase://my-cluster-srv.my-namespace                  | ✅ Yes                                                                           |                   |
| ⇐ 2.7.2              | **Local**               | DNS address                                              | couchbase://pod-0.my-cluster.my-namespace.svc,pod-1.my-cluster.my-namespace.svc | 🚫 No             |
| **Remote**           | Round-robin DNS         | couchbase://my-cluster.my-namespace                      | ⚠️ Yes                                                                          |                   |

In [Table 2](#table-sgw-exposed-features-limitations) above, the **Relationship to Cluster** column indicates the location of the Sync Gateway cluster in relation to the Couchbase cluster that is being managed by the Kubernetes Operator. **_Local_** refers to instances where Sync Gateway is deployed in the same Kubernetes cluster where Couchbase Server is running (see [Intra-Kubernetes Networking](#intra-kubernetes-networking) and [Inter-Kubernetes Networking with Forwarded DNS](#inter-kubernetes-networking-with-forwarded-dns)). **_Remote_** refers to instances where Sync Gateway is deployed outside of the Kubernetes cluster where Couchbase Server is running (see [Public Networking with External DNS](#public-networking-with-external-dns)).

* Sync Gateway 2.8.2 and higher do not experience any connection issues related to exposed features as these versions have full support for DNS SRV lookup _and_ support explicit network selection. Both **Local** and **Remote** connections can be configured in accordance with the standard client connection [documentation](howto-client-sdks.md).
* Sync Gateway 2.7.3 and 2.8.0 introduced DNS SRV lookup for service discovery, however the automatic network selection behavior of Sync Gateway incorrectly directs traffic to "external" interfaces when running within the same Kubernetes cluster as the target Couchbase cluster.

  * **Remote** connections still work as expected and can be configured in accordance with the standard client connection [documentation](howto-client-sdks.md).
  * **Local** connections _do not_ work as expected, and Sync Gateway ends up selecting the "external" network interface. This causes network traffic to be sent through a load balancer, which can lead to significant financial costs with a cloud provider.  
  If you intend to use a **Local** connection, you can choose to mitigate the issue by connecting using only DNS addresses. This method requires that the connection string contain a list of the hostnames of all the Couchbase Server pods in the Couchbase cluster. This method of connectivity is highly discouraged, as it is not tolerant to Couchbase cluster pod topology changes. (Sync Gateway will be informed of any topology changes so long as it stays running. However, once it restarts, it will fail to reconnect because the connection string has the old topology.)
* Sync Gateway 2.7.2 and lower don’t feature DNS SRV support at all, instead falling back to a DNS address record lookup. **Local** connections have the same limitations as they do in versions 2.7.3 and 2.8.0 above. **Remote** connections support high availability through round-robin DNS. (Note, however, that since this connection method runs over HTTP on port 8091, there is a potential risk of a denial of service should port 8091 ever experience too many connections at once.)