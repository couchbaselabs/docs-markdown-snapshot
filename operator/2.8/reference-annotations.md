[View original HTML](/operator/2.8/reference-annotations.html)

> Couchbase Operator uses special annotations to configure specific resources. 

## [](#bucket-backend-configuration)Bucket Backend Configuration

### [](#managed-buckets)Managed Buckets

#### [](#cao-couchbase-combuckets-defaultstoragebackend)`cao.couchbase.com/buckets.defaultStorageBackend`

Used to configure the default storage backend for managed CouchbaseBucket. Changing the storage backend of a pre-existing bucket is only supported on Couchbase Server version 7.6.0 Defaults to `couchstore`, accepts either `couchstore` or `magma`.

### [](#unmanaged-buckets)Unmanaged Buckets

#### [](#cao-couchbase-combuckets-targetunmanagedbucketstoragebackend)`cao.couchbase.com/buckets.targetUnmanagedBucketStorageBackend`

Used to force a storage backend on all buckets in a Couchbase Cluster. This configuration only takes action if bucket management is disabled When configured the Couchbase Operator will attempt to force all buckets in a cluster to a particular storage backend. This config is only used with Couchbase Server 7.6.0\. Accepts either `couchstore` or `magma`.

### [](#bucket-migrations)Bucket Migrations

#### [](#cao-couchbase-combuckets-enablebucketmigrationroutines)`cao.couchbase.com/buckets.enableBucketMigrationRoutines`

By default, bucket storage backend migrations are not enabled as they will result in a swap-rebalance of every effected couchbase node. This means changing the bucket storage backend will be prevented unless this annotation is set to "true". Accepts either `true` or `false`.

#### [](#cao-couchbase-combuckets-maxconcurrentpodswaps)`cao.couchbase.com/buckets.maxConcurrentPodSwaps`

Used to change the number of pods affected by a bucket storage backend migration. By default, only one pod will be migrated at a time. This field must be a number greater than 0.

## [](#sample-buckets)Sample buckets

#### [](#cao-couchbase-comsamplebucket)`cao.couchbase.com/sampleBucket`

SampleBucket indicates whether the bucket should be treated as a sample bucket. If set to "true", the bucket name will define the sample bucket used and the bucket will be created with the sample bucket configuration, not the CRD specification. SampleBuckets have a memory quota of 200Mi and a couchstore storage backend. If this annotation is changed to false or removed, the bucket will then be updated with the CRD specification. This annotation cannot be added to an existing bucket and should not be used for production clusters.

## [](#cluster-scheduling)Cluster Scheduling

### [](#rescheduling-to-different-server-groups-on-failed-scheduling)Rescheduling To Different Server Groups On Failed Scheduling

#### [](#cao-couchbase-comrescheduledifferentservergroup)`cao.couchbase.com/rescheduleDifferentServerGroup`

Used to allow Couchbase Operator to attempt to reschedule a pod to a different server group if the pod fails to schedule on the original server group. By default Couchbase Operator will continue to try to schedule the pod on the original server group if it fails to schedule. With this annotation applied to a cluster the operator will try to schedule the pod to a different server group that has the same number of Couchbase Pods in it as the original server group. This is to ensure that the cluster remains balanced across the server groups. This is a best effort attempt and may not always succeed. If there are no server groups with the same number of pods as the original server group the pod will be scheduled on the original server group. Accepts either `true` or `false`.

### [](#server-group-shuffling)Server Group Shuffling

#### [](#cao-couchbase-comshuffleservergroups)`cao.couchbase.com/shuffleServerGroups`

Used to allow Couchbase Operator to shuffle the order that pods are scheduled to defined server groups. By default Couchbase Operator will schedule pods to server groups in lexical order. The shuffling is pseudo-random and is based on the cluster name and namespace, so the same cluster/namespace combination will always shuffle the server groups in the same order. Accepts either `true` or `false`.

## [](#pod-rescheduling)Pod Rescheduling

### [](#individual-pod-rescheduling)Individual Pod Rescheduling

#### [](#cao-couchbase-comreschedule)`cao.couchbase.com/reschedule`

Used to force a pod to be rescheduled. When this annotation is applied to a Couchbase pod, the operator will detect it and reschedule the pod. The pods will either be Swap Rebalanced or go through a InPlaceUpgrade depending on [couchbaseclusters.spec.upgradeProcess](resource/couchbasecluster.md#couchbaseclusters-spec-upgradeprocess). Accepts either `true` or `false`.

## [](#host-network)Host Network

### [](#improved-host-network-support)Improved Host Network Support

#### [](#cao-couchbase-comnetworking-improvedhostnetwork)`cao.couchbase.com/networking.improvedHostNetwork`

Used to enable improved host network support. This annotation is used to enable improved host network support for Couchbase Server pods. When enabled on a cluster the operator will skip SAN validation and will add the underlying Kubernetes hostname a pod is running on to the alternate addresses list.

#### [](#cao-couchbase-comnetworking-initpodswithnodehostname)`cao.couchbase.com/networking.initPodsWithNodeHostname`

Used to set the hostname of the pod to the name of the node it is running on. The annotation `cao.couchbase.com/networking.improvedHostNetwork` must also be set to `true` in order for the annotation to take effect. When set to true, the pods will be initialised with the node name as the hostname of the pod without an alternate address.

## [](#cloud-native-gateway)Cloud Native Gateway

### [](#otlp-endpoint)OTLP Endpoint

#### [](#cao-couchbase-comnetworking-cloudnativegateway-otlp-endpoint)`cao.couchbase.com/networking.cloudNativeGateway.otlp.endpoint`

Used to set a custom OTLP endpoint for on Cloud Native Gateway. This annotation is applied to the cluster, and takes a string value (e.g. "https://otel:1234"). The value is passed directly to the Cloud Native Gateway container.