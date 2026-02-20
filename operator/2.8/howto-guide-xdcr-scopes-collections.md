---
title: "How-to Guide: XDCR with Scopes and Collections"
description: A how-to guide on configuring cross data center replication (XDCR)
  using the Kubernetes Operator.
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.8/modules/ROOT/pages/howto-guide-xdcr-scopes-collections.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.8@operator::howto-guide-xdcr-scopes-collections.adoc[]
---

[View original HTML](/operator/2.8/howto-guide-xdcr-scopes-collections.html)

# How-to Guide: XDCR with Scopes and Collections

> A how-to guide on configuring cross data center replication (XDCR) using the Kubernetes Operator. 

## [](#overview)Overview

Couchbase Server allows the use of cross data center replication (XDCR). XDCR allows data to be physically migrated to a new cluster, or replicated to a standby system for disaster recovery or physical locality.

This guide will take you through a few examples on how to configure XDCR.

## [](#prerequisites)Prerequisites

* If you are new to role-based access control in Couchbase, refer to the [Roles Page](../../server/current/learn/security/roles.md)
* If you are new to Couchbase Kubernetes Operator (CAO), refer to the [Kubernetes Operator Introduction](overview.md)
* Couchbase Scopes and Collections was added in Version 7.0\. Refer to the [Couchbase Scopes and Collections](concept-scopes-and-collections.md) page to learn more about these
* To install the Couchbase Kubernetes Operator please refer to [Install Operator on Kubernetes](install-kubernetes.md) or [Install Operator on OpenShift](install-openshift.md)

## [](#configure-xdcr)Configure XDCR

> [!NOTE]
> This guide uses IP based Addressing to configure XDCR. To configure it using a different approach please refer to [Configure XDCR](howto-xdcr.md).

XDCR can be configured to do `Unidirectional` and `Bidirectional` replication.

### [](#unidirectional-replication)Unidirectional Replication

Unidirectional Replication is a replication configuration that has the following characteristics: Transactions that occur at a source bucket are replicated to the destination bucket.

#### [](#remote-cluster)Remote Cluster

The remote cluster needs to set some networking options:

```console
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: my-remote-cluster
spec:
  networking:
    exposeAdminConsole: true (1)
    adminConsoleServiceTemplate: (2)
      spec:
        type: NodePort
    exposedFeatures: (3)
    - xdcr
    exposedFeatureServiceTemplate: (4)
      spec:
        type: NodePort
```

| **1** | spec.networking.exposeAdminConsole creates a load balanced service used to connect to the remote cluster.                                                                                                                                                       |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | spec.networking.adminConsoleServiceTemplate type is set to NodePort surfacing the administrative console service on the Kubernetes node network.                                                                                                                |
| **3** | spec.networking.exposedFeatures selects the feature set of ports to expose external to the Kubernetes cluster. In this instance the XDCR feature set exposes the admin, data and index ports required for XDCR replication.                                     |
| **4** | spec.networking.exposedFeatureServiceTemplate type is set to NodePort which surfaces the exposed feature sets, per-pod, on the Kubernetes node network. This allows the cluster to escape the confines of any overlay network and be seen by the local cluster. |

#### [](#local-cluster)Local Cluster

A resource is created to replicate the bucket `source` on the local cluster to `destination` on the remote:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseReplication
metadata:
  name: replicate-source-to-destination-in-remote-cluster
  labels:
    replication: from-my-cluster-to-remote-cluster
explicitMapping:
  allowRules:
  - sourceKeyspace:
      scope: "scope0"
      collection: "collection0"
    targetKeyspace:
      scope: "scope0"
      collection: "collection1"
spec:
  bucket: source
  remoteBucket: destination
```

The resource is labeled with `replication:from-my-cluster-to-remote-cluster` to avoid any ambiguity. This is because the Operator will select all `CouchbaseReplication` resources in the namespace and apply them to all remote clusters by default. Thus, the label is specific to the source cluster and target cluster.

Create a secret for authentication of remote Couchbase cluster:

```yaml
apiVersion: v1
data:
  password: cGFzc3dvcmQ=         (1)
  username: QWRtaW5pc3RyYXRvcg==  (2)
kind: Secret
metadata:
  name: my-xdcr-secret
type: Opaque
```

| **1** | password: password of remote Couchbase cluster |
| ----- | ---------------------------------------------- |
| **2** | username: username of remote Couchbase cluster |

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

Upon completion of the above steps, XDCR will be configured on the source cluster to replicate the data of the `source` bucket to the `destination` bucket in the remote cluster.

To verify that, login to the Web UI, and go to the XDCR section, you’ll see it configured as shown in the image below.

![xdcr replications](_images/xdcr-replications.png) 

### [](#bidirectional-replication)Bidirectional Replication

Bidirectional Replication is a replication configuration that has the following characteristics: Transactions that occur at a source bucket are replicated to the destination bucket and transactions that occur at a destination bucket are copied to the source bucket.

In the [Unidirectional Replication](#unidirectional-replication) section, we configured the replication from source to destination cluster. In this case, we will configure the destination cluster with minor changes in the steps mentioned for Unidirectional Replication.

#### [](#remote-cluster-2)Remote Cluster

This time the remote cluster is the source cluster which we already configured in Unidirectional Replication.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: my-remote-cluster
spec:
  networking:
    exposeAdminConsole: true (1)
    adminConsoleServiceTemplate: (2)
      spec:
        type: NodePort
    exposedFeatures: (3)
    - xdcr
    exposedFeatureServiceTemplate: (4)
      spec:
        type: NodePort
```

| **1** | spec.networking.exposeAdminConsole creates a load balanced service used to connect to the remote cluster.                                                                                                                                                       |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | spec.networking.adminConsoleServiceTemplate type is set to NodePort surfacing the administrative console service on the Kubernetes node network.                                                                                                                |
| **3** | spec.networking.exposedFeatures selects the feature set of ports to expose external to the Kubernetes cluster. In this instance the XDCR feature set exposes the admin, data and index ports required for XDCR replication.                                     |
| **4** | spec.networking.exposedFeatureServiceTemplate type is set to NodePort which surfaces the exposed feature sets, per-pod, on the Kubernetes node network. This allows the cluster to escape the confines of any overlay network and be seen by the local cluster. |

#### [](#local-cluster-2)Local Cluster

A resource is created to replicate the bucket `destination` on the local cluster to `source` on the remote:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseReplication
metadata:
  name: replicate-destination-to-source-in-remote-cluster
  labels:
    replication: from-my-cluster-to-remote-cluster
explicitMapping:
  allowRules:
  - sourceKeyspace:
      scope: "scope0"
      collection: "collection1"
    targetKeyspace:
      scope: "scope0"
      collection: "collection0"
spec:
  bucket: destination
  remoteBucket: source
```

The resource is labeled with `replication:from-my-cluster-to-remote-cluster` to avoid any ambiguity because by default the Operator will select all `CouchbaseReplication` resources in the namespace and apply them to all remote clusters. Thus the label is specific to the source cluster and target cluster.

Create a secret for authentication of remote Couchbase cluster:

```yaml
apiVersion: v1
data:
  password: cGFzc3dvcmQ=          # password
  username: QWRtaW5pc3RyYXRvcg==  # Administrator
kind: Secret
metadata:
  name: my-xdcr-secret
type: Opaque
```

We define a remote cluster on our local resource:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: destination-cluster
spec:
  xdcr:
    managed: true
    remoteClusters:
    - name: remote-cluster (1)
      uuid: 9c2e50b21e333a56e3d6d357030cd83e (2)
      hostname: http://10.17.2.35:31294?network=external (3)
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

Upon completion of the above steps, XDCR will be configured on the destination cluster to replicate the data of the destination bucket to the source bucket in the remote cluster.

![xdcr replications](_images/xdcr-replications.png) 

By combining unidirectional and bidirectional topologies, you have the flexibility to create several complex topologies such as the chain and propagation topology.

#### [](#chain-replication)Chain Replication

Chain Replication is a configuration in which transactions occurring at source bucket can be replicated to destination bucket, and the transactions occurring at destination bucket can be replicated to another destination bucket.

Chain replication topology is useful for minimizing data center network bandwidth because the cluster at the head of the chain only replicates to the next cluster along the chain rather than all the clusters.

![xdcr chain replication](_images/xdcr-chain-replication.png) 

#### [](#propagation-replication)Propagation Replication

Propagation replication can be useful in a scenario when you want to set up a replication scheme between two regional offices and several other local offices. Data between the regional offices is replicated bidirectionally between Datacenter 1 and Datacenter 2\. Data changes in the local offices (Datacenters 3 and 4) are pushed to the regional office using unidirectional replication.

![xdcr propagation replication](_images/xdcr-propagation-replication.png) 

## [](#further-reading)Further Reading

* [Cross Data Center Replication](../../server/current/learn/clusters-and-availability/xdcr-overview.md)