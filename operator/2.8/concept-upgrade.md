[View original HTML](/operator/2.8/concept-upgrade.html)

> The Operator allows a managed Couchbase cluster to be upgraded. This includes upgrading the Couchbase Server version and also related Kubernetes resources. 

## [](#upgrading-couchbase-server)Upgrading Couchbase Server

The Couchbase Server version can be [upgraded](howto-couchbase-upgrade.md) by the Operator.

Upgrades may be performed using one of a number of different strategies as specified by [couchbaseclusters.spec.upgradeStrategy](resource/couchbasecluster.md#couchbaseclusters-spec-upgradestrategy) in the `CouchbaseCluster` resource:

* InPlaceUpgrade performs an in-place upgrade on one, or more, pods at a time
* Rolling upgrades upgrade one, or more, pods at a time
* Immediate upgrades upgrade all pods at the same time

For rolling and immediate upgrades, the process is as follows:

* One or more candidate pods are selected
* New pods are created for each of the candidates with the same Couchbase configuration as the existing ones
* Data is rebalanced from the old pods to the new ones
* The candidate pods are deleted

For in place upgrades, the process is as follows:

* One or more candidate pods are selected
* Each candidate is failed over and updated with the new version
* Each PVC associated with the candidate is updated with the new version
* Operator performs an in place upgrade on the candidate

When using rolling upgrades, performing the operation one pod at a time, risk is limited in the event of an issue, and can be rolled back. A rolling upgrade requires the least network and compute overhead, so will affect client operation less.

When using immediate upgrades, there is a greater risk, and requires greater resource during the upgrade, however the operation itself is significantly faster. Immediate upgrades may have an undesired effect on client performance as all pods in the cluster are undergoing upgrade at the same time.

When using in-place upgrade, the pods and PVCs are updated to use the new version. This is quicker than a rolling upgrade and will retain the same PVCs (data retained). In-place upgrade cannot be used in conjunction with immediate upgrades. The validator will fail the request if immediate upgrade strategy and in-place upgrade process are both specified. The same pod names and networking settings will be retained when the pod is restarted by the operator.

You can balance time against risk by tailoring rolling updates with the [couchbaseclusters.spec.rollingUpgrade](resource/couchbasecluster.md#couchbaseclusters-spec-rollingupgrade) configuration parameter. This allows rolling upgrades to upgrade 2 pods at a time, or 20% of the cluster at a time, for example.

|  | In-place upgrades are a volatile process that can lead to interruptions in service. It should not be used when there are less than 2 data nodes defined or data loss may occur. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#how-to-upgrade-a-cluster)How to Upgrade a cluster

To upgrade a cluster, you need to modify the CouchbaseCluster resource to specify the new version of Couchbase Server that you want to upgrade to. This can be done by updating the `spec.image` field in the CouchbaseCluster manifest to the new version.

For example, if you were upgrading from version 7.2.4 to 7.6.0 then the CouchbaseCluster resource needs to be updated as follows:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: my-couchbase-cluster
spec:
  image: couchbase/server:7.6.0
```

### [](#couchbase-server-upgrade-constraints)Couchbase Server Upgrade Constraints

Not all upgrade paths are supported by Couchbase Server. The Operator enforces the following constraints on Couchbase Server version upgrades.

* Upgrades must be an upgrade, downgrades are not supported due to potential protocol incompatibility, for example:

  * 5.5.0 to 5.5.3 is allowed
  * 5.5.3 to 5.5.0 is not allowed
* Upgrades must not cross multiple major version boundaries, for example:

  * 5.x.x to 6.x.x is allowed
  * 5.x.x to 7.x.x is not allowed
* Couchbase Server versions cannot be changed during an upgrade

Refer to the Couchbase Server [upgrade documentation](../../server/current/install/upgrade.md) for more information about direct upgrade paths.

|  | Modifying the Couchbase Server version during an upgrade is permitted only if the end result is a roll-back to the previous version. |
|  | ------------------------------------------------------------------------------------------------------------------------------------ |

### [](#rollback)Rollback

The Couchbase Operator provides the capability to roll back while it is in progress. A rollback can only be performed if the upgrade is in progress and has not yet completed. Once a cluster has fully upgraded to the new version the cluster can no longer be downgraded to a previous version. A rollback will simply replace the nodes on the new version and replace them with nodes with the version they had before an upgrade was started.

#### [](#how-to-roll-back-an-upgrade)How to Roll Back an Upgrade

To initiate a rollback, you need to modify the CouchbaseCluster resource to specify the previous version of Couchbase Server that was running before the upgrade started. This can be done by updating the `spec.image` field in the CouchbaseCluster manifest to the previous version.

For example, if you were upgrading from version 7.2.4 to 7.6.0 and encountered issues, you can roll back to version 7.2.4 by updating the manifest as follows:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: my-couchbase-cluster
spec:
  image: couchbase/server:7.2.4
```

After applying this change, the operator will begin the rollback process.

### [](#controlled-upgrades)Controlled Upgrades

The Operator provides the capability to control the upgrade process by upgrading specific server classes at a time, this gives the ability to control the upgrade process and ensure that the upgrade process is controlled. For example, it is possible to upgrade the data nodes first, then the query nodes, and finally the index nodes.

Whilst performing a controlled upgrade the cluster will be in a mixed state with different versions of Couchbase Server running at the same time. This time should be kept to a minimum to avoid potential issues with the cluster.

#### [](#how-to-perform-a-controlled-upgrade)How to Perform a Controlled Upgrade

To perform a controlled upgrade you need to first modify the CouchbaseCluster Image to specify the image that you want to upgrade to. This can be done by updating the `spec.image` field in the CouchbaseCluster manifest. You can then specify the server classes that you want to upgrade first by updating the `spec.servers.image` to the older image for the server classes you do not want to be upgraded first. You can explicitly update `spec.servers.image` for the server classes that you want to upgrade first, alternatively if the image is not specified for a server class then the image specified in `spec.image` will be used.

Example `CouchbaseCluster` Resource with three Server Classes

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  image: couchbase/server:7.2.4
  ...
  servers:
    - size: 3
      name: data
      services:
        - data
    - size: 3
      name: index
      services:
        - index
    - size: 3
      name: query
      services:
        - query
```

For the example above if you want to upgrade the data nodes first, then the query nodes, and finally the index nodes you can update the `CouchbaseCluster` resource as follows:

Example `CouchbaseCluster` Resource with Controlled Upgrade data nodes first

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  image: couchbase/server:7.6.0 (1)
  ...
  servers:
    - size: 3
      name: data
      services:
        - data
    - size: 3
      name: index
      image: couchbase/server:7.2.4 (2)
      services:
        - index
    - size: 3
      image: couchbase/server:7.2.4 (3)
      name: query
      services:
        - query
```

| **1** | The cluster image needs to be the latest version that you want to upgrade to.                                         |
| ----- | --------------------------------------------------------------------------------------------------------------------- |
| **2** | The image for the index server class is set to the older version to ensure that the index nodes are not upgraded yet. |
| **3** | The image for the query server class is set to the older version to ensure that the query nodes are not upgraded yet. |

Example `CouchbaseCluster` Resource with Controlled Upgrade Upgrading query nodes second

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  image: couchbase/server:7.6.0
  ...
  servers:
    - size: 3
      name: data
      services:
        - data
    - size: 3
      name: index
      image: couchbase/server:7.2.4 (1)
      services:
        - index
    - size: 3
      name: query
      services:
        - query
```

| **1** | The image for the index server class is set to the older version to ensure that the index nodes are not upgraded yet. |
| ----- | --------------------------------------------------------------------------------------------------------------------- |

Example `CouchbaseCluster` Resource with Controlled Upgrade Upgrading index nodes last

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  image: couchbase/server:7.6.0
  ...
  servers:
    - size: 3
      name: data
      services:
        - data
    - size: 3
      name: index
      services:
        - index
    - size: 3
      name: query
      services:
        - query
```

#### [](#how-to-perform-a-controlled-rollback)How to Perform a Controlled Rollback

The Operator also allows you to perform a controlled rollback. To perform a controlled rollback you would performed the controlled rollback steps in reverse. The following examples shows how to perform a controlled rollback on a example cluster where all the server classes but one have upgraded to the new version. Note that once a cluster is fully upgraded to the new version a rollback is no longer possible.

Example Starting `CouchbaseCluster` Resource for Controlled Rollback

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  image: couchbase/server:7.6.0 (1)
  ...
  servers:
    - size: 3
      name: data
      services:
        - data
    - size: 3
      name: index
      image: couchbase/server:7.2.4 (2)
      services:
        - index
    - size: 3
      name: query
      services:
        - query
```

| **1** | The cluster image is the latest version that is being upgraded to.                                                     |
| ----- | ---------------------------------------------------------------------------------------------------------------------- |
| **2** | The image for the index server class is set to the older version indicating that the index nodes are not upgraded yet. |

Example `CouchbaseCluster` Resource Controlled Rollback Query Nodes

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  image: couchbase/server:7.6.0 (1)
  ...
  servers:
    - size: 3
      name: data
      services:
        - data
    - size: 3
      name: index
      image: couchbase/server:7.2.4
      services:
        - index
    - size: 3
      name: query
      image: couchbase/server:7.2.4 (2)
      services:
        - query
```

| **1** | During a controlled rollback the cluster image should stay as the version that was being upgraded to. If this is changed to the older version then the cluster will all be rolled back to the older version without control over the server class order. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The image for the query server class is set to the older version indicating that the query nodes should be rolled back next.                                                                                                                             |

Example `CouchbaseCluster` Resource Controlled Rollback Remaining Data Nodes

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  image: couchbase/server:7.2.4 (1)
  ...
  servers:
    - size: 3
      name: data
      services:
        - data
    - size: 3
      name: index
      services:
        - index
    - size: 3
      name: query
      services:
        - query
```

| **1** | As there is only one server class left to rollback the cluster image can be set to the older version and the remaining server nodes in the data class will be rolled back. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#upgrading-pods)Upgrading Pods

In Kubernetes pods are immutable — they cannot be modified once they are created. If a `CouchbaseCluster` configuration value is modified that would also modify the underlying pod, then the Operator must create a new pod to replace the old one that does not match the required specification. Pod upgrades work in exactly the same way as an upgrade to the Couchbase Server version; in fact upgrading the Couchbase Server image is just a subset of modifying any other pod specification parameter.

The Operator compares the required pod specification with the one used to create the original pod, a candidate is selected if the specifications differ. The Operator therefore can perform the following tasks:

* Modification of environment variables
* [Modification of scheduling constraints](concept-scheduling.md)
* [Modification of memory constraints](concept-memory-allocation.md)
* [Enabling and disabling of TLS](concept-tls.md)
* [Enabling and disabling of persistent storage](concept-persistent-volumes.md)

This mechanism allows a cluster to be used from evaluation right up to production, with features enabled as they are required, without service disruption.

## [](#upgrading-persistent-volumes)Upgrading Persistent Volumes

Online persistent volume resizing support is not yet available in all supported versions of Kubernetes. As a result the Operator supports [persistent volume resizing](howto-persistent-volumes.md) using a similar mechanism to [Upgrading Pods](#upgrading-pods). The Operator will detect a modification to the specification of a persistent volume template and schedule a pod upgrade in order to satisfy the request.

During an in-place upgrade, the PVC will be updated to include the updated image and couchbase server versions. The size of the PVC and data within it will not be edited.