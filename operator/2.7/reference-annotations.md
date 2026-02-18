---
title: Annotation Documentation
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.7/modules/ROOT/pages/reference-annotations.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/operator/2.7/reference-annotations.html)

# Annotation Documentation

> Couchbase Operator uses special annotations to configure specific resources. 

## [](#history-retention)History Retention

### [](#bucket)Bucket

```yaml
apiVersion: v2
kind: CouchbaseBucket
metadata:
  name: "my-bucket"
  annotations:
    cao.couchbase.com/historyRetention.seconds: "1000"
    cao.couchbase.com/historyRetention.bytes: "2147483648"
    cao.couchbase.com/historyRetention.collectionHistoryDefault: "true"
spec:
  storageBackend: magma
  memoryQuota: 1024Mi
  evictionPolicy: valueOnly
```

#### [](#cao-couchbase-comhistoryretention-seconds)`cao.couchbase.com/historyRetention.seconds`

Used for configuring history retention time for a bucket. This parameter is parsed into an integer and defines how many seconds of history an individual vbucket should aim to retain on disk. Defaults to `0`, and can be altered after bucket creation. This annotation is only supported on buckets with `couchbasebuckets.spec.storageBackend=magma`.

#### [](#cao-couchbase-comhistoryretention-bytes)`cao.couchbase.com/historyRetention.bytes`

Used for configuring history retention size for a bucket. This parameter is parsed into an integer and defines how many bytes of history an individual vbucket should aim to retain on disk. Defaults to `0` and has a minimum working value of `2147483648`. Can be altered after bucket creation. Only supported on buckets with `couchbasebuckets.spec.storageBackend=magma`. This annotation is only supported on buckets with `couchbasebuckets.spec.storageBackend=magma`.

#### [](#cao-couchbase-comhistoryretention-collectionhistorydefault)`cao.couchbase.com/historyRetention.collectionHistoryDefault`

Used for configuring whether history retention is enabled for a collection by default. This parameter sets whether history retention is enabled by default on newly created collections. Defaults to `true`, and accepts `true` or `false`. This field can be altered after bucket creation. This annotation is only supported on buckets with `couchbasebuckets.spec.storageBackend=magma`.

### [](#collection)Collection

```yaml
apiVersion: v2
kind: CouchbaseCollection
metadata:
  name: "my-collection"
  annotations:
    cao.couchbase.com/history: "true"
```

#### [](#cao-couchbase-comhistory)`cao.couchbase.com/history`

Used for enabling/disabling history retention at collection creation time. This parameter is used to enable/disable history retention when a new collection is being created. Any changes to this field once the collection has been created will be ignored. Accepts a either `true` or `false` and defaults to the bucket level `collectionHistoryDefault`.

## [](#bucket-backend-configuration)Bucket Backend Configuration

### [](#managed-buckets)Managed Buckets

#### [](#cao-couchbase-combuckets-defaultstoragebackend)`cao.couchbase.com/buckets.defaultStorageBackend`

Used to configure the default storage backend for managed CouchbaseBucket. Changing the storage backend of a pre-existing bucket is only supported on CouchbaseServer version 7.6.0 Defaults to `couchstore`, accepts either `couchstore` or `magma`.

### [](#unmanaged-buckets)Unmanaged Buckets

#### [](#cao-couchbase-combuckets-targetunmanagedbucketstoragebackend)`cao.couchbase.com/buckets.targetUnmanagedBucketStorageBackend`

Used to force a storage backend on all buckets in a Couchbase Cluster. This configuration only takes action if bucket management is disabled When configured the Couchbase Operator will attempt to force all buckets in a cluster to a particular storage backend. This config is only used with Couchbase Server 7.6.0\. Accepts either `couchstore` or `magma`.

## [](#cluster-scheduling)Cluster Scheduling

### [](#rescheduling-to-different-server-groups-on-failed-scheduling)Rescheduling To Different Server Groups On Failed Scheduling

#### [](#cao-couchbase-comrescheduledifferentservergroup)`cao.couchbase.com/rescheduleDifferentServerGroup`

Used to allow Couchbase Operator to attempt to reschedule a pod to a different server group if the pod fails to schedule on the original server group. By default Couchbase Operator will continue to try to schedule the pod on the original server group if it fails to schedule. With this annotation applied to a cluster the operator will try to schedule the pod to a different server group that has the same number of Couchbase Pods in it as the original server group. This is to ensure that the cluster remains balanced across the server groups. This is a best effort attempt and may not always succeed. If there are no server groups with the same number of pods as the original server group the pod will be scheduled on the original server group. Accepts either `true` or `false`.

### [](#server-group-shuffling)Server Group Shuffling

#### [](#cao-couchbase-comshuffleservergroups)`cao.couchbase.com/shuffleServerGroups`

Used to allow Couchbase Operator to shuffle the order that pods are scheduled to defined server groups. By default Couchbase Operator will schedule pods to server groups in lexical order. The shuffling is pseudo-random and is based on the cluster name and namespce, so the same cluster/namespace combination will always shuffle the server groups in the same order. Accepts either `true` or `false`.

## [](#pod-rescheduling)Pod Rescheduling

### [](#individual-pod-rescheduling)Individual Pod Rescheduling

#### [](#cao-couchbase-comreschedule)`cao.couchbase.com/reschedule`

Used to force a pod to be rescheduled. When this annotation is applied to a Couchbase pod, the operator will detect it and reschedule the pod. The pods will either be Swap Rebalanced or go through a InPlaceUpgrade depending on [couchbaseclusters.spec.upgradeProcess](resource/couchbasecluster.md#couchbaseclusters-spec-upgradeprocess). Accepts either `true` or `false`.

## [](#host-network)Host Network

### [](#improved-host-network-support)Improved Host Network Support

#### [](#cao-couchbase-comnetworking-improvedhostnetwork)`cao.couchbase.com/networking.improvedHostNetwork`

Used to enable improved host network support. This annotation is used to enable improved host network support for Couchbase Server pods. When enabled on a cluster the operator will skip SAN validation and will add the underlying Kubernetes hostname a pod is running on to the alternate addresses list.

## [](#cloud-native-gateway)Cloud Native Gateway

### [](#otlp-endpoint)OTLP Endpoint

#### [](#cao-couchbase-comnetworking-cloudnativegateway-otlp-endpoint)`cao.couchbase.com/networking.cloudNativeGateway.otlp.endpoint`

Used to set a custom OTLP endpoint for on Cloud Native Gateway. This annotation is applied to the cluster, and takes a string value (e.g. "https://otel:1234"). The value is passed directly to the Cloud Native Gateway container.