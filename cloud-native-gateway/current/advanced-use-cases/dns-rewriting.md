---
title: Deploying Cloud Native Gateway in a DNS Rewriting Environment
description: How to deploy Cloud Native Gateway when DNS is rewritten between
  clients, the gateway, and Couchbase cluster nodes.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/advanced-use-cases/pages/dns-rewriting.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:advanced-use-cases:dns-rewriting.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/advanced-use-cases/dns-rewriting.html)

# Deploying Cloud Native Gateway in a DNS Rewriting Environment

> How to deploy Cloud Native Gateway when DNS is rewritten between clients, the gateway, and Couchbase cluster nodes. 

## [](#background)Background

Cloud Native Gateway resolves the Couchbase cluster topology dynamically. When it bootstraps via `--cb-host`, it fetches the cluster configuration that contains hostnames for every node. The gateway then opens connections to those hostnames for KV and Query traffic, as well as Search and Analytics.

DNS rewriting between the gateway and the Couchbase nodes can cause hostnames in the cluster configuration to fail to resolve.

## [](#recommended-deployment-gateway-behind-the-nat-boundary)Recommended Deployment: Gateway Behind the NAT Boundary

Deploy the gateway on the same network as the Couchbase cluster — behind the NAT boundary. This is the simplest way to avoid DNS rewriting issues. When the gateway shares a network with the cluster nodes, all hostnames in the cluster configuration resolve naturally without any rewriting.

                 NAT / Firewall
                      │
Clients  ─── DNS ───▶ │ ──▶  Cloud Native Gateway ──▶  Couchbase Cluster
(external)            │      (internal)                (internal)
                      │

This reduces the DNS problem to a single hop. Clients need to reach the gateway through one external address. This can be a load balancer VIP, a DNS record, or a Kubernetes Service. The gateway handles all backend connectivity to the cluster nodes internally, where hostnames resolve without intervention.

If you cannot co-locate the gateway with the cluster, the following sections cover how to handle DNS rewriting.

## [](#problem-scenarios)Problem Scenarios

The following scenarios describe common DNS rewriting issues and their symptoms:

### [](#gateway-cannot-resolve-couchbase-node-hostnames)Gateway Cannot Resolve Couchbase Node Hostnames

The Couchbase cluster configuration advertises node hostnames as seen by the cluster itself, for example `node1.cb-internal.local`. If the gateway runs in a different DNS zone, these hostnames may not resolve.

Symptoms:

* Gateway logs: `failed to connect to couchbase cluster`
* Connection timeouts to KV or query services after successful bootstrap
* Bootstrap succeeds because `--cb-host` is reachable, but subsequent data operations fail
* Intermittent timeouts after node changes due to high DNS TTL caching stale entries — reduce the DNS TTL or use an IP-based connection string

Although not recommended, you can deploy Cloud Native Gateway outside of the NAT boundary using alternate addresses. Couchbase Server supports configuring alternate addresses on each node. An alternate address is a second hostname that the node advertises alongside its default address in the cluster configuration. You can also include a set of alternate ports. When Cloud Native Gateway bootstraps with an external network context, the cluster can return the alternate addresses instead of the internal ones. This allows Cloud Native Gateway to reach all nodes without any external DNS rewriting.

See the [Couchbase Server alternate addresses documentation](https://docs.couchbase.com/server/current/learn/clusters-and-availability/connectivity.html#alternate-addresses) for details on how to configure this.

### [](#clients-cannot-resolve-the-gateway-address)Clients Cannot Resolve the Gateway Address

Protostellar SDK clients connect to the gateway's gRPC port. If DNS is rewritten between the client and the gateway, the client may not be able to reach the gateway. Load balancers and DNS records handle this externally. The gateway itself does not advertise its own address to clients.

Symptoms:

* SDK connection timeouts
* TLS SNI mismatch errors if the rewritten name does not match the certificate

## [](#configuration)Configuration

The following configuration options help manage DNS rewriting in your deployment.

### [](#cb-hostconnecting-to-couchbase)`--cb-host` — Connecting to Couchbase

Use a hostname or IP that resolves from the gateway's network context:

```bash
# If Couchbase nodes advertise internal names, use the bootstrap node's
# resolvable address
./cloud-native-gateway --cb-host couchbase://cb-node1.rewritten.example.com

# With TLS
./cloud-native-gateway --cb-host couchbases://cb-node1.rewritten.example.com
```

The `$HOST` variable in the Couchbase configuration replaces the hostname derived from the bootstrap connection string. This helps when nodes advertise `$HOST` as a placeholder.

### [](#client-facing-address)Client-Facing Address

The gateway does not have a command-line tool flag to advertise its own address to clients. You can manage client connectivity to the gateway externally through:

* A load balancer or reverse proxy pointed at the gateway's data port
* A Kubernetes Service — ClusterIP, NodePort, or LoadBalancer
* DNS records that resolve to the gateway hosts

Verify that the external DNS name or IP used by clients resolves or routes to the gateway's bound address and data port, which defaults to 18098.

### [](#coredns-rewrite-rules-in-kubernetes)CoreDNS Rewrite Rules in Kubernetes

If Cloud Native Gateway runs in Kubernetes, the Couchbase cluster may advertise hostnames that do not resolve inside the cluster. Add rewrite rules to CoreDNS to map them to reachable addresses:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns-custom
  namespace: kube-system
data:
  custom.server: |
    cb-node1.internal.corp:53 {
      rewrite name cb-node1.internal.corp cb-node1.reachable.example.com
      forward . /etc/resolv.conf
    }
```

Add a rewrite entry for every Couchbase node hostname returned in the cluster configuration, not just the bootstrap node.

### [](#tls-certificate-considerations)TLS Certificate Considerations

When DNS is rewritten, the TLS certificate presented by the gateway must match the hostname that clients use to connect. Verify that the certificate's Subject Alternative Names, or SANs, include:

* The external/rewritten DNS name clients use
* Any load balancer or service mesh DNS names

When connecting to a Couchbase cluster over TLS with `couchbases://`, the `--cluster-ca-cert` CA must validate the certificates presented by the Couchbase nodes. The CA validates against their rewritten DNS names, or the names the nodes present in their certificates.