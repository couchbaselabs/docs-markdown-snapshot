---
title: Configure XDCR
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.8/modules/ROOT/pages/howto-xdcr.adoc
  xref: xref:2.8@operator::howto-xdcr.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.8/howto-xdcr.html)

# Configure XDCR

> How to set up unidirectional replication to another Couchbase cluster in a different Kubernetes cluster. 

Couchbase Server allows the use of cross data center replication (XDCR). XDCR allows data to be physically migrated to a new cluster, or replicated to a standby system for disaster recovery or physical locality.

This page documents how to setup XDCR to replicate data to a different Kubernetes cluster.

## [](#dns-based-addressing)DNS Based Addressing

In this scenario the remote cluster is accessible with Kubernetes based DNS. This applies to both [intra-Kubernetes networking](concept-couchbase-networking.md#intra-kubernetes-networking) and [inter-Kubernetes networking with forwarded DNS](concept-couchbase-networking.md#inter-kubernetes-networking-with-forwarded-dns).

When using inter-Kubernetes networking, the local XDCR client must forward DNS requests to the remote cluster in order to resolve DNS names of the target Couchbase instances. Refer to the [Inter-Kubernetes Networking with Forwarded DNS](tutorial-remote-dns.md) tutorial to understand how to configure forwarding DNS servers.

TLS is optional with this configuration, but shown for completeness. To configure without TLS, omit any TLS related attributes.

### [](#remote-cluster)Remote Cluster

The remote cluster needs to set some networking options:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: my-remote-cluster
spec:
  networking:
    tls: (1)
      secretSource:
        serverSecretName: my-server-tls-secret
```

| **1** | **TLS only:** TLS configuration is configured as per the [TLS configuration guide](tutorial-tls.md). |
| ----- | ---------------------------------------------------------------------------------------------------- |

### [](#local-cluster)Local Cluster

A resource is created to replicate the bucket `source` on the local cluster to `destination` on the remote:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseReplication
metadata:
  name: replicate-source-to-destination-in-remote-cluster
  labels:
    replication: from-my-cluster-to-remote-cluster (1)
spec:
  bucket: source
  remoteBucket: destination
```

| **1** | The resource is labeled with replication:from-my-cluster-to-remote-cluster to avoid any ambiguity because by default the Operator will select all CouchbaseReplication resources in the namespace and apply them to all remote clusters. Thus the label is specific to the source cluster and target cluster. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

We define a remote cluster on our local resource:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: my-cluster
spec:
  xdcr:
    managed: true
    remoteClusters:
    - name: remote-cluster (1)
      uuid: 611e50b21e333a56e3d6d3570309d7e3 (2)
      hostname: couchbases://my-remote-cluster.my-remote-namespace?network=default (3)
      authenticationSecret: my-xdcr-secret (4)
      tls:
        secret: my-xdcr-tls-secret (5)
      replications: (6)
        selector:
          matchLabels:
             replication: from-my-cluster-to-remote-cluster
  servers:
  - pod:
      spec:
        dnsPolicy: None (7)
        dnsConfig: (8)
          nameservers:
            - "172.20.92.77"
          searches:
            - default.svc.cluster.local
            - svc.cluster.local
            - cluster.local
```

| **1** | The name remote-cluster is unique among remote clusters on this local cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | The uuid has been collected by interrogating the [couchbaseclusters.status.clusterId](resource/couchbasecluster.md#couchbaseclusters-status-clusterid) field on the remote cluster.                                                                                                                                                                                                                                                                                                                                                                                            |
| **3** | The correct hostname to use is the remote cluster's console service to provide stable naming and service discovery. The hostname is calculated as per the [SDK configuration how-to](howto-client-sdks.md#dns-based-addressing).                                                                                                                                                                                                                                                                                                                                               |
| **4** | As we are not using client certificate authentication we specify a secret containing a username and password on the remote system.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **5** | **TLS only:** For TLS connections you need to specify the remote cluster CA certificate in order to verify the remote cluster is trusted. [couchbaseclusters.spec.xdcr.remoteClusters.tls.secret](resource/couchbasecluster.md#couchbaseclusters-spec-xdcr-remoteclusters-tls-secret) documents the secret format.                                                                                                                                                                                                                                                             |
| **6** | Replications are selected that match the labels we specify, in this instance the ones that go from this cluster to the remote one.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **7** | **Inter-Kubernetes networking with forwarded DNS only:** the [couchbaseclusters.spec.servers.pod.spec.dnsPolicy](resource/couchbasecluster.md#couchbaseclusters-spec-servers-pod) field tells Kubernetes to provide no default DNS configuration.                                                                                                                                                                                                                                                                                                                              |
| **8** | **Inter-Kubernetes networking with forwarded DNS only:** the [couchbaseclusters.spec.servers.pod.spec.dnsConfig](resource/couchbasecluster.md#couchbaseclusters-spec-servers-pod) field explicitly defines the local DNS name server to use. This name server is capable of forwarding DNS requests for the remote cluster to the remote Kubernetes DNS server. Other DNS requests are forwarded to the local Kubernetes DNS server. DNS search domains should remain as shown, however default should be modified to be the same as the namespace the cluster is deployed in. |

## [](#dns-based-addressing-with-external-dns)DNS Based Addressing with External DNS

In this scenario the remote cluster is configured to use [public networking with external-DNS](concept-couchbase-networking.md#public-networking-with-external-dns). By using this feature the configuration is forced to use TLS which both secures the XDCR replication end-to-end and simplifies configuration.

### [](#remote-cluster-2)Remote Cluster

The remote cluster needs to set some networking options:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: my-remote-cluster
spec:
  networking:
    tls: (1)
      secretSource:
        serverSecretName: my-server-tls-secret
    dns: (2)
      domain: my-remote-cluster.example.com
    exposeAdminConsole: true (3)
    adminConsoleServiceTemplate:
      spec:
        type: LoadBalancer (4)
    exposedFeatures: (5)
    - xdcr
    exposedFeatureServiceTemplate:
      spec:
        type: LoadBalancer (6)
```

| **1** | TLS configuration is required and spec.networking.tls is configured as per the [TLS configuration guide](tutorial-tls.md). The TLS server certificate needs an additional subject alternative name (SAN) valid for the public host names that will be generated for the pods. In this instance DNS:\*.my-remote-cluster.example.com. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | The domain is also specified in spec.networking.dns.domain so that per-pod and console services are annotated correctly. A 3rd party solution is required to synchronize these DNS name annotations with a DDNS server in the cloud.                                                                                                 |
| **3** | By specifying spec.networking.exposeAdminConsole as true this creates a service for console.my-remote-cluster.example.com. This admin console service is a stable DNS name and can be used to perform service discovery — it does not change as the cluster topology does.                                                           |
| **4** | spec.networking.adminConsoleServiceTemplate type is set to LoadBalancer which creates a stable public IP for clients to connect to.                                                                                                                                                                                                  |
| **5** | spec.networking.exposedFeatures selects the feature set of ports to expose external to the Kubernetes cluster. In this instance the xdcr feature set exposes the admin, data and index ports required for XDCR replication.                                                                                                          |
| **6** | spec.networking.exposedFeatureServiceTemplate type is set to LoadBalancer and causes the Operator to create a load balancer per-pod. Each load-balancer has a unique IP address — unlike a NodePort — so that standard port number can be used.                                                                                      |

### [](#local-cluster-2)Local Cluster

A resource is created to replicate the bucket `source` on the local cluster to `destination` on the remote:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseReplication
metadata:
  name: replicate-source-to-destination-in-remote-cluster
  labels:
    replication: from-my-cluster-to-remote-cluster (1)
spec:
  bucket: source
  remoteBucket: destination
```

| **1** | The resource is labeled with replication:from-my-cluster-to-remote-cluster to avoid any ambiguity because by default the Operator will select all CouchbaseReplication resources in the namespace and apply them to all remote clusters. Thus the label is specific to the source cluster and target cluster. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

We define a remote cluster on our local resource:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: my-cluster
spec:
  xdcr:
    managed: true
    remoteClusters:
    - name: remote-cluster (1)
      uuid: 611e50b21e333a56e3d6d3570309d7e3 (2)
      hostname: couchbases://console.my-remote-cluster.example.com?network=external (3)
      authenticationSecret: my-xdcr-secret (4)
      tls:
        secret: my-xdcr-tls-secret (5)
      replications: (6)
        selector:
          matchLabels:
             replication: from-my-cluster-to-remote-cluster
```

| **1** | The name remote-cluster is unique among remote clusters on this local cluster.                                                                                                                                                                                                                       |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The uuid has been collected by interrogating the [couchbaseclusters.status.clusterId](resource/couchbasecluster.md#couchbaseclusters-status-clusterid) field on the remote cluster.                                                                                                                  |
| **3** | The correct hostname to use is the remote cluster's console service to provide stable naming and service discovery. The hostname is calculated as per the [SDK configuration how-to](howto-client-sdks.md#dns-based-addressing-with-external-dns).                                                   |
| **4** | As we are not using client certificate authentication we specify a secret containing a username and password on the remote system.                                                                                                                                                                   |
| **5** | For TLS connections you need to specify the remote cluster CA certificate in order to verify the remote cluster is trusted. [couchbaseclusters.spec.xdcr.remoteClusters.tls.secret](resource/couchbasecluster.md#couchbaseclusters-spec-xdcr-remoteclusters-tls-secret) documents the secret format. |
| **6** | Replications are selected that match the labels we specify, in this instance the ones that go from this cluster to the remote one.                                                                                                                                                                   |

## [](#ip-based-addressing)IP Based Addressing

In this discouraged scenario, there is no shared DNS between two Kubernetes clusters - we must use IP based addressing. Pods are exposed by using Kubernetes `NodePort` type services. As there is no DNS, TLS is not supported, so security must be maintained between the two clusters using a VPN.

When you use NodePorts on a remote Couchbase cluster for XDCR connections, you risk interruptions if Kubernetes deletes and recreates the Service. Kubernetes does not guarantee that a new Service reuses the same NodePort. If the port number changes, XDCR connections that rely on the old IP:NodePort become invalid.

The exact outcome depends on the Kubernetes CNI (Container Networking Interface) implementation. In some cases, Kubernetes removes the old port before it creates the new one, which causes a brief loss of connectivity. In other cases, Kubernetes creates the new NodePort first, which reduces or avoids downtime.

* Single-node Couchbase cluster: When the node's NodePort changes, XDCR cannot reconnect automatically. In this case, you must manually update the replication configuration at couchbaseclusters.spec.xdcr.remoteClusters.hostname with the new IP:NodePort of the Couchbase node.
* Multi-node Couchbase cluster: When a node's NodePort changes, XDCR reconnects to another node that still exposes a valid NodePort. However, if XDCR tries to reconnect through the updated node, you may still need to update couchbaseclusters.spec.xdcr.remoteClusters.hostname with the new port.

> [!IMPORTANT]
> When using Istio or another service mesh, remember that strict mode mTLS cannot be used with Kubernetes node ports. This means XDCR will be unable to replicate when using IP based addressing with strict mode mTLS.

### [](#remote-cluster-3)Remote Cluster

The remote cluster needs to set some networking options:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: my-remote-cluster
spec:
  networking:
    exposeAdminConsole: true (1)
    adminConsoleServiceTemplate:
      spec:
        type: NodePort (2)
    exposedFeatures: (3)
    - xdcr
    exposedFeatureServiceTemplate:
      spec:
        type: NodePort (4)
```

| **1** | spec.networking.exposeAdminConsole creates a load balanced service used to connect to the remote cluster.                                                                                                                                                       |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | spec.networking.adminConsoleServiceTemplate type is set to NodePort surfacing the administrative console service on the Kubernetes node network.                                                                                                                |
| **3** | spec.networking.exposedFeatures selects the feature set of ports to expose external to the Kubernetes cluster. In this instance the xdcr feature set exposes the admin, data and index ports required for XDCR replication.                                     |
| **4** | spec.networking.exposedFeatureServiceTemplate type is set to NodePort which surfaces the exposed feature sets, per-pod, on the Kubernetes node network. This allows the cluster to escape the confines of any overlay network and be seen by the local cluster. |

### [](#local-cluster-3)Local Cluster

A resource is created to replicate the bucket `source` on the local cluster to `destination` on the remote:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseReplication
metadata:
  name: replicate-source-to-destination-in-remote-cluster
  labels:
    replication: from-my-cluster-to-remote-cluster (1)
spec:
  bucket: source
  remoteBucket: destination
```

| **1** | The resource is labeled with replication:from-my-cluster-to-remote-cluster to avoid any ambiguity because by default the Operator will select all CouchbaseReplication resources in the namespace and apply them to all remote clusters. Thus the label is specific to the source cluster and target cluster. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

We define a remote cluster on our local resource:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: my-cluster
spec:
  xdcr:
    managed: true
    remoteClusters:
    - name: remote-cluster (1)
      uuid: 611e50b21e333a56e3d6d3570309d7e3 (2)
      hostname: http://10.16.5.87:30584?network=external (3)
      authenticationSecret: my-xdcr-secret (4)
      replications: (5)
        selector:
          matchLabels:
             replication: from-my-cluster-to-remote-cluster
```

| **1** | The name remote-cluster is unique among remote clusters on this local cluster.                                                                                                      |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The uuid has been collected by interrogating the [couchbaseclusters.status.clusterId](resource/couchbasecluster.md#couchbaseclusters-status-clusterid) field on the remote cluster. |
| **3** | The correct hostname to use. The hostname is calculated as per the [SDK configuration how-to](howto-client-sdks.md#ip-based-addressing).                                            |
| **4** | As we are not using client certificate authentication we specify a secret containing a username and password on the remote system.                                                  |
| **5** | Finally we select replications that match the labels we specify, in this instance the ones that go from this cluster to the remote one.                                             |

## [](#scopes-and-collections-support)Scopes and collections support

With Couchbase Server version 7 and greater, scope and collections support is now present for XDCR. The Couchbase Kubernetes Operator fully supports the various options available to the Couchbase Server version it is running with, full details can be found in the [official documentation](#server:manage:manage-xdcr/replicate-using-scopes-and-collections.html).

> [!NOTE]
> If scopes and collections are not used then XDCR maintains the previous approach of replicating the full bucket by default.

> [!IMPORTANT]
> These options are all only valid if the version of Couchbase Server deployed in the Couchbase Cluster is 7+. The target bucket must be set up with the correct scopes and collections to support XDCR.

### [](#replication)Replication

XDCR differs slightly from RBAC and other usage of scopes and collections in that it has the concept of mappings and keyspaces as defined in the [official documentation](#server:learn:clusters-and-availability/xdcr-with-scopes-and-collections.html). These follow a set of allow and deny rules as indicated which are reflected as a list within the CRD.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseReplication
metadata:
  name: replicationscopesandcollections
spec:
  bucket: bucket0 (1)
  remoteBucket: anotherbucket
explicitMapping: (2)
  allowRules: (3)
    - sourceKeyspace: (4)
        scope: "scope0"
      targetKeyspace: (5)
        scope: "scope0"
    - sourceKeyspace:
        scope: scope1
        collection: collection1 (6)
      targetKeyspace:
        scope: targetscope1
        collection: targetcollection1 (7)
    - sourceKeyspace:
        scope: scope1
        collection: collection2
      targetKeyspace:
        scope: targetscope1
        collection: targetcollection2
    - sourceKeyspace:
        scope: scope2
        collection: collection2
      targetKeyspace:
        scope: targetscope2
        collection: targetcollection2
  denyRules: (8)
    # More specific denial rule of the scope0 implicit mappings
    - sourceKeyspace:
        scope: scope0
        collection: bugs
```

| **1** | The source bucket, this must be defined as a CRD at least in the source cluster. Eventual consistency rules apply so if the bucket is still being created then we will keep retrying until it reconciles.                                                                                                                                                                                  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | The explicitMapping is the new Couchbase Server 7 set of explicit mapping rules.                                                                                                                                                                                                                                                                                                           |
| **3** | A set of allow rules, i.e. request to replicate these.                                                                                                                                                                                                                                                                                                                                     |
| **4** | The source keyspace to replicate from, in this case it will replicate the entire scope0 scope including all its collections subject to any deny rules.                                                                                                                                                                                                                                     |
| **5** | The target keyspace to replicate to, this must be a matching size to the source so if you specify a collection in the source you must specify a collection in the target.                                                                                                                                                                                                                  |
| **6** | This is an example of replicating only a specific collection collection1 in scope scope1.                                                                                                                                                                                                                                                                                                  |
| **7** | The target keyspace must be of identical size so as we are replicating from a collection we must also specify a target collection.                                                                                                                                                                                                                                                         |
| **8** | Deny rules can be used to prevent replication of specific keyspaces. This is useful if for example you have a scope with a large number of collections and you want to replicate all but a small number. You can indicate an allow rule for the scope and then filter out the collections you do not want via deny rules rather than have to specify every collection you want explicitly. |

As you can see this is an extension of the previously defined CRD to cater for scopes and collections. If the `explicitMapping` structure is not set then it will behave as it did previously with full bucket replication including any scopes and collections.

### [](#migration)Migration

One particular area of note is the ability to [migrate](#server:learn:clusters-and-availability/xdcr-with-scopes-and-collections.html#migration) data from the default scope and collection of the source bucket into named scopes and collections of the target bucket. As this is intended as a one-off task and mutually exclusive from standard replication a new separate CRD is provided to configure it.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseMigrationReplication
metadata:
  name: migrationscopesandcollections
spec:
  bucket: explicit-name (1)
  remoteBucket: explicit-name
migrationMapping: (2)
  mappings:
    - targetKeyspace: (3)
        scope: donald
        collection: antique
      filter: "type=duck && age=old" (4)
    - filter: "Iamnotaduck"
      targetKeyspace:
        scope: migrationscope
        collection: migrationcollection
```

| **1** | The source bucket to use, this must exist at least as a CRD definition.                                                                                                                                                                                                                                                                                                                       |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The set of mappings to use for migration. This can either be the entire default scope and collection into a single named target scope and collection or you can filter it via a regex into separate target scopes and collections. The options are mutually exclusive so you either replicate the entirety into a single scope and collection or you filter it into different ones, not both. |
| **3** | An example of replicating to a named scope and collection.                                                                                                                                                                                                                                                                                                                                    |
| **4** | An example of a regex to apply to the data. This is obviously data dependent and not something that can be validated by the operator.                                                                                                                                                                                                                                                         |

## [](#further-reading)Further Reading

* [CouchbaseReplication resource reference](resource/couchbasereplication.md)
* [CouchbaseMigrationReplication resource reference](resource/couchbasemigrationreplication.md)