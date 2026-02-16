[View original HTML](/operator/2.7/howto-persistent-volumes.html)

> Configure and manage persistent volumes for a Couchbase cluster. 

## [](#configuring-persistent-volumes)Configuring Persistent Volumes

Ensure you have read the [storage classes](concept-persistent-volumes.md#supported-storage-classes) documentation, created any necessary storage classes for your platform, and setup file system groups for your platform.

Once storage classes are provisioned correctly, you can start provisioning persistent volume claims by modifying the [CouchbaseCluster](resource/couchbasecluster.md) configuration:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  servers:
  - size: 1
    name: data_services
    services:
      - data
    volumeMounts:
      default: couchbase (1)
  volumeClaimTemplates: (2)
  - metadata:
      name: couchbase (3)
    spec:
      storageClassName: standard (4)
      resources: (5)
        requests:
          storage: 1Gi
```

| **1** | [couchbaseclusters.spec.servers.volumeMounts.default](resource/couchbasecluster.md#couchbaseclusters-spec-servers-volumemounts-default) tells the Operator to provision a default persistent volume claim and attach it to a pod of that server class.                                                                                                                             |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [couchbaseclusters.spec.volumeClaimTemplates](resource/couchbasecluster.md#couchbaseclusters-spec-volumeclaimtemplates) defines a list of templates related to storage. These will be used to create Kubernetes persistent volume claims and therefore have the same data structure. However the Operator is only concerned with the following parameters, any others are ignored. |
| **3** | [couchbaseclusters.spec.volumeClaimTemplates.metadata.name](resource/couchbasecluster.md#couchbaseclusters-spec-volumeclaimtemplates) is a unique identifier for a persistent volume template. It is referred to by attributes in the [couchbaseclusters.spec.servers.volumeMounts](resource/couchbasecluster.md#couchbaseclusters-spec-servers-volumemounts) object.              |
| **4** | [couchbaseclusters.spec.volumeClaimTemplates.spec.storageClassName](resource/couchbasecluster.md#couchbaseclusters-spec-volumeclaimtemplates) refers to a dynamically allocated storage class defined on the platform.                                                                                                                                                             |
| **5** | [couchbaseclusters.spec.volumeClaimTemplates.spec.resources](resource/couchbasecluster.md#couchbaseclusters-spec-volumeclaimtemplates) defines the size of the volume that will be allocated.                                                                                                                                                                                      |

## [](#resizing-persistent-volumes)Resizing Persistent Volumes

You can expand or contract persistent storage by modifying the [CouchbaseCluster](resource/couchbasecluster.md) configuration.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  volumeClaimTemplates:
  - metadata:
      name: couchbase
    spec:
      storageClassName: standard
      resources:
        requests:
          storage: 1Gi (1)
```

| **1** | You can resize the persistent storage of any pods that reference the modified persistent volume claim template. For example, to allocate more space per-pod, [update the specification](howto-couchbase-update.md) from 1Gi to 2Gi: |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  volumeClaimTemplates:
  - metadata:
      name: couchbase
    spec:
      storageClassName: standard
      resources:
        requests:
          storage: 2Gi (1)
```

| **1** | The modification will trigger the Operator to detect that existing persistent volume claims do not match the intended size. The Operator triggers a rolling upgrade of the affected pods. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | You can also modify the storage class and the Operator will detect and upgrade the cluster to use it. |
|  | ----------------------------------------------------------------------------------------------------- |

### [](#online-volume-expansion)Online Volume Expansion

Normally, the Couchbase cluster must undergo a rolling upgrade whenever the volume size is modified. However, persistent volumes that are already in use by Couchbase clusters can optionally be _expanded in-place_ without needing to perform an upgrade on the underlying storage subsystem. The Autonomous Operator achieves this by working in conjunction with [Kubernetes Persistent Volume Expansion](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims) to claim additional storage for running pods without any downtime.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  enableOnlineVolumeExpansion: true (1)
  onlineVolumeExpansionTimeoutInMins: 10 (2)
  volumeClaimTemplates:
  - metadata:
      name: couchbase
    spec:
      storageClassName: standard
      resources:
        requests:
          storage: 2Gi (3)
```

| **1** | [couchbaseclusters.spec.enableOnlineVolumeExpansion](resource/couchbasecluster.md#couchbaseclusters-spec-enableonlinevolumeexpansion): This field must be set to true for the Autonomous Operator to allow online volume expansion.                                                                                                  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | [couchbaseclusters.spec.onlineVolumeExpansionTimeoutInMins](resource/couchbasecluster.md#couchbaseclusters-spec-onlinevolumeexpansiontimeoutinmins): This field must be provided as a retry mechanism with a timeout in minutes. It could be in between 0 to 30 minutes, defaulting to 10 minutes. No unit is needed to be provided. |
| **3** | Modifying the storage size will trigger the Autonomous Operator to detect that existing persistent volume claims do not match the intended size (as it normally would). However, if the new value is larger than the previous value, the Autonomous Operator will attempt an online expansion of the volume.                         |

You can verify the status of the volume expansion task by checking events on the `CouchbaseCluster` resource:

```console
$ kubectl describe couchbasecluster expand-couchbase-cluster
```

If the volume expansion was successful, you should expect output similar to the following:

Normal  ExpandVolumeStarted    46s          Expanding Volume cb-example-0003-data-01 from 1Gi to 2Gi **(1)**
Normal  ExpandVolumeSucceeded  41s          Successfully expanded volume cb-example-0002-default-01
Normal  ExpandVolumeStarted    18s          Expanding Volume cb-example-0004-data-01 from 1Gi to 2Gi **(1)**
Normal  ExpandVolumeSucceeded  6s           Successfully expanded volume cb-example-0002-default-01

| **1** | In this example, the persistent volume on each of the Couchbase data pods has been expanded in place from 1Gi to 2Gi. |
| ----- | --------------------------------------------------------------------------------------------------------------------- |

It may take some time for online volume expansion to complete, especially since some cloud vendors impose rate limits on storage creation.

|  | Once the provided timeout in [couchbaseclusters.spec.onlineVolumeExpansionTimeoutInMins](resource/couchbasecluster.md#couchbaseclusters-spec-onlinevolumeexpansiontimeoutinmins) is reached for retries and the volume resize is not successful, as the underlying infrastructure could not provide larger volumes, it would report a failure. Unfortunately, the request cannot be rolled back since the request can only be increased. Therefore, the only way to abort a suspended expansion task is to set [couchbaseclusters.spec.enableOnlineVolumeExpansion](resource/couchbasecluster.md#couchbaseclusters-spec-enableonlinevolumeexpansion) back to false so that a rolling upgrade may occur. Refer to [Volume Expansion Lifecycle](reference-couchbasecluster-events.md#volume-expansion-lifecycle) for a description of volume expansion events. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

It’s important to note that setting [couchbaseclusters.spec.enableOnlineVolumeExpansion](resource/couchbasecluster.md#couchbaseclusters-spec-enableonlinevolumeexpansion) to `true` _does not guarantee that volumes will be expanded online_. Please review the following notes before attempting online volume expansion:

* The underlying `StorageClass` must be capable of performing [volume expansions](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims) (`allowVolumeExpansion=true`).

  * The Autonomous Operator has no way of detecting if the underlying storage class supports volume expansion. Therefore, it is important that you confirm that your volume type supports volume expansion before enabling online volume expansion in the [CouchbaseCluster](resource/couchbasecluster.md) resource.  
  In general, block storage volume types such as `GCE-PD`, `AWS-EBS`, A\`zure Disk\`, `Cinder`, and `Ceph RBD` typically require a full file system expansion, whereas network attached file systems like `Glusterfs` and `Azure File` can always be expanded online.
* Volume size can only be _increased_.

  * Kubernetes does not currently support online reductions in volume size.
  * New storage sizes can only be specified in [volumeClaimTemplates.spec.resources.requests.storage](resource/couchbasecluster.md#couchbaseclusters-spec-volumeclaimtemplates), and must be a larger value than the current size (values smaller than the current size will be blocked by the dynamic admission controller). Note that persistent volumes are fully managed by the Autonomous Operator, therefore any manual changes to the PersistentVolumeClaim size made outside of the [CouchbaseCluster](resource/couchbasecluster.md) spec will be reverted.
  * To reduce volume size, set [couchbaseclusters.spec.enableOnlineVolumeExpansion](resource/couchbasecluster.md#couchbaseclusters-spec-enableonlinevolumeexpansion) back to `false` and proceed with [traditional resizing](#resizing-persistent-volumes) (which requires rolling upgrade).
* If online volume expansion fails for some reason, the Autonomous Operator will fall back to a traditional rolling upgrade as a means to expand volumes.
* The Autonomous Operator cannot detect if [resizing in-use PersistentVolumeClaims (ExpandInUsePersistentVolumes)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#resizing-an-in-use-persistentvolumeclaim) is enabled on the current Kubernetes cluster.