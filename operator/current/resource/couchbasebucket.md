---
title: CouchbaseBucket Resource
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/couchbase-operator/edit/2.9.x/docs/user/modules/ROOT/pages/resource/couchbasebucket.adoc
  xref: xref:operator::resource/couchbasebucket.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/resource/couchbasebucket.html)

# CouchbaseBucket Resource

The CouchbaseBucket resource defines a set of documents in Couchbase server. A Couchbase client connects to and operates on a bucket, which provides independent management of a set documents and a security boundary for role based access control. A CouchbaseBucket provides replication and persistence for documents contained by it.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseBucket
metadata:
  name: ""
spec:
  accessScannerEnabled: True
  autoCompaction:
    databaseFragmentationThreshold:
      percent: 0
      size: ""
    magmaFragmentationPercentage: 0
    timeWindow:
      abortCompactionOutsideWindow: false
      end: ""
      start: ""
    tombstonePurgeInterval: ""
    viewFragmentationThreshold:
      percent: 0
      size: ""
  compressionMode: passive
  conflictResolution: seqno
  durabilityImpossibleFallback: ""
  enableCrossClusterVersioning: false
  enableFlush: false
  enableIndexReplica: false
  encryptionAtRest:
    keyLifetime: 8760h
    keyName: ""
    rotationInterval: 720h
  evictionPolicy: valueOnly
  expiryPagerSleepTime: 10m
  historyRetention:
    bytes: 0
    collectionHistoryDefault: True
    seconds: 0
  ioPriority: low
  maxTTL: ""
  memoryHighWatermark: 85
  memoryLowWatermark: 75
  memoryQuota: 100Mi
  minimumDurability: ""
  name: ""
  numVBuckets: 0
  onlineEvictionPolicyChange: false
  rank: 0
  replicas: 1
  scopes:
    managed: false
    resources:
    - kind: CouchbaseScope
      name: ""
    selector: {}
  storageBackend: ""
  versionPruningWindowHrs: 0
  warmupBehavior: background
```

## [](#couchbasebuckets-apiversion)couchbasebuckets.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbasebuckets-kind)couchbasebuckets.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbasebuckets-metadata)couchbasebuckets.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbasebuckets-metadata-name)couchbasebuckets.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbasebuckets-metadata-namespace)couchbasebuckets.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbasebuckets-metadata-labels)couchbasebuckets.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbasebuckets-metadata-annotations)couchbasebuckets.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbasebuckets-spec)couchbasebuckets.spec

### [](#constraints-8)Constraints

**Type**: `object`

**Default**: `{}`

### [](#description-8)Description

CouchbaseBucketSpec is the specification for a Couchbase bucket resource, and allows the bucket to be customized.

### [](#couchbasebuckets-spec-accessscannerenabled)couchbasebuckets.spec.accessScannerEnabled

#### [](#constraints-9)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-9)Description

AccessScannerEnabled allows the bucket to be configured to allow enabling and disabling the access scanner. This feature is only supported for Couchbase Server 8.0.0+. It is set to true by default.

### [](#couchbasebuckets-spec-autocompaction)couchbasebuckets.spec.autoCompaction

#### [](#constraints-10)Constraints

**Type**: `object`

#### [](#description-10)Description

AutoCompaction allows the configuration of auto-compaction settings, including on what conditions disk space is reclaimed and when it is allowed to run, on a per-bucket basis. If any of these fields are configured, those that are not configured here will take the value set at the cluster level. Excluding this field (which is the default), will set the autoCompactionSettings to false and the bucket will use cluster defaults.

### [](#couchbasebuckets-spec-autocompaction-databasefragmentationthreshold)couchbasebuckets.spec.autoCompaction.databaseFragmentationThreshold

#### [](#constraints-11)Constraints

**Type**: `object`

#### [](#description-11)Description

DatabaseFragmentationThreshold defines triggers for when database compaction should start on buckets with a couchstore storage backend. This field will be ignored if the bucket has a magma storage backend.

### [](#couchbasebuckets-spec-autocompaction-databasefragmentationthreshold-percent)couchbasebuckets.spec.autoCompaction.databaseFragmentationThreshold.percent

#### [](#constraints-12)Constraints

**Type**: `integer`

**Minimum**: `2`

**Maximum**: `100`

#### [](#description-12)Description

Percent specifies the level of view fragmentation that must be reached for View compaction to be automatically triggered. This field must be in the range 2-100, defaulting to the cluster level value.

### [](#couchbasebuckets-spec-autocompaction-databasefragmentationthreshold-size)couchbasebuckets.spec.autoCompaction.databaseFragmentationThreshold.size

#### [](#constraints-13)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-13)Description

Size the level of database fragmentation that must be reached for data compaction to be automatically triggered on the bucket. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbasebuckets-spec-autocompaction-magmafragmentationpercentage)couchbasebuckets.spec.autoCompaction.magmaFragmentationPercentage

#### [](#constraints-14)Constraints

**Type**: `integer`

**Minimum**: `10`

**Maximum**: `100`

#### [](#description-14)Description

MagmaFragmentationThresholdPercentage defines the percentage of magma fragmentation level to determine the point when compaction is triggered for buckets with a magma storage backend. This field will be ignored if the bucket has a couchstore storage backend.

### [](#couchbasebuckets-spec-autocompaction-timewindow)couchbasebuckets.spec.autoCompaction.timeWindow

#### [](#constraints-15)Constraints

**Type**: `object`

#### [](#description-15)Description

TimeWindow allows restriction of when compaction can occur. This field will be ignored if the bucket has a magma storage backend.

### [](#couchbasebuckets-spec-autocompaction-timewindow-abortcompactionoutsidewindow)couchbasebuckets.spec.autoCompaction.timeWindow.abortCompactionOutsideWindow

#### [](#constraints-16)Constraints

**Type**: `boolean`

#### [](#description-16)Description

AbortCompactionOutsideWindow stops compaction processes when the process moves outside the window, defaulting to false.

### [](#couchbasebuckets-spec-autocompaction-timewindow-end)couchbasebuckets.spec.autoCompaction.timeWindow.end

#### [](#constraints-17)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$`

#### [](#description-17)Description

End is a wallclock time, in the form HH:MM, when a compaction should stop.

### [](#couchbasebuckets-spec-autocompaction-timewindow-start)couchbasebuckets.spec.autoCompaction.timeWindow.start

#### [](#constraints-18)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$`

#### [](#description-18)Description

Start is a wallclock time, in the form HH:MM, when a compaction is permitted to start.

### [](#couchbasebuckets-spec-autocompaction-tombstonepurgeinterval)couchbasebuckets.spec.autoCompaction.tombstonePurgeInterval

#### [](#constraints-19)Constraints

**Type**: `string`

#### [](#description-19)Description

TombstonePurgeInterval controls how long to wait before purging tombstones. This field must be in the range 1h-1440h, defaulting to the cluster level value. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbasebuckets-spec-autocompaction-viewfragmentationthreshold)couchbasebuckets.spec.autoCompaction.viewFragmentationThreshold

#### [](#constraints-20)Constraints

**Type**: `object`

#### [](#description-20)Description

ViewFragmentationThreshold defines triggers for when view compaction should start. This field will be ignored if the bucket has a magma storage backend.

### [](#couchbasebuckets-spec-autocompaction-viewfragmentationthreshold-percent)couchbasebuckets.spec.autoCompaction.viewFragmentationThreshold.percent

#### [](#constraints-21)Constraints

**Type**: `integer`

**Minimum**: `2`

**Maximum**: `100`

#### [](#description-21)Description

Percent specifies the percentage level of View fragmentation that must be reached for View compaction to be automatically triggered on the bucket This field must be in the range 2-100, defaulting to the cluster level value.

### [](#couchbasebuckets-spec-autocompaction-viewfragmentationthreshold-size)couchbasebuckets.spec.autoCompaction.viewFragmentationThreshold.size

#### [](#constraints-22)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-22)Description

Size is the level of View fragmentation that must be reached for view compaction to be automatically triggered on the bucket. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbasebuckets-spec-compressionmode)couchbasebuckets.spec.compressionMode

#### [](#constraints-23)Constraints

**Type**: `string`

**Default**: `passive`

**Enumerations**: `off, passive, active`

#### [](#description-23)Description

CompressionMode defines how Couchbase server handles document compression. When off, documents are stored in memory, and transferred to the client uncompressed. When passive, documents are stored compressed in memory, and transferred to the client compressed when requested. When active, documents are stored compresses in memory and when transferred to the client. This field must be "off", "passive" or "active", defaulting to "passive". Be aware "off" in YAML 1.2 is a boolean, so must be quoted as a string in configuration files.

### [](#couchbasebuckets-spec-conflictresolution)couchbasebuckets.spec.conflictResolution

#### [](#constraints-24)Constraints

**Type**: `string`

**Default**: `seqno`

**Enumerations**: `seqno, lww`

#### [](#description-24)Description

ConflictResolution defines how XDCR handles concurrent write conflicts. Sequence number based resolution selects the document with the highest sequence number as the most recent. Timestamp based resolution selects the document that was written to most recently as the most recent. This field must be "seqno" (sequence based), or "lww" (timestamp based), defaulting to "seqno".

### [](#couchbasebuckets-spec-durabilityimpossiblefallback)couchbasebuckets.spec.durabilityImpossibleFallback

#### [](#constraints-25)Constraints

**Type**: `string`

**Enumerations**: `disabled, fallbackToActiveAck`

#### [](#description-25)Description

DurabilityImpossibleFallback defines whether to report writes as durable even if not enough replicas are written to. This feature is only supported for Couchbase Server 8.0.0+. Defaults to disabled.

### [](#couchbasebuckets-spec-enablecrossclusterversioning)couchbasebuckets.spec.enableCrossClusterVersioning

#### [](#constraints-26)Constraints

**Type**: `boolean`

#### [](#description-26)Description

EnableCrossClusterVersioning allows the bucket to be configured to allow cross-cluster versioning. This feature is only supported for Couchbase Server 7.6.0+. Once it has been set to true, it cannot be toggled to false.

### [](#couchbasebuckets-spec-enableflush)couchbasebuckets.spec.enableFlush

#### [](#constraints-27)Constraints

**Type**: `boolean`

#### [](#description-27)Description

EnableFlush defines whether a client can delete all documents in a bucket. This field defaults to false.

### [](#couchbasebuckets-spec-enableindexreplica)couchbasebuckets.spec.enableIndexReplica

#### [](#constraints-28)Constraints

**Type**: `boolean`

#### [](#description-28)Description

EnableIndexReplica defines whether indexes for this bucket are replicated. This field defaults to false.

### [](#couchbasebuckets-spec-encryptionatrest)couchbasebuckets.spec.encryptionAtRest

#### [](#constraints-29)Constraints

**Type**: `object`

#### [](#description-29)Description

EncryptionAtRest defines the encryption at rest settings for the bucket. This field is only supported for Couchbase Server 8.0.0+.

### [](#couchbasebuckets-spec-encryptionatrest-keylifetime)couchbasebuckets.spec.encryptionAtRest.keyLifetime

#### [](#constraints-30)Constraints

**Type**: `string`

**Default**: `8760h`

#### [](#description-30)Description

KeyLifetime is the lifetime of the encryption key. Must be greater or equal to 30 days. Default is 365 days.

### [](#couchbasebuckets-spec-encryptionatrest-keyname)couchbasebuckets.spec.encryptionAtRest.keyName

#### [](#constraints-31)Constraints

**Required**

**Type**: `string`

#### [](#description-31)Description

Key is the name of the encryption key to use for encryption at rest.

### [](#couchbasebuckets-spec-encryptionatrest-rotationinterval)couchbasebuckets.spec.encryptionAtRest.rotationInterval

#### [](#constraints-32)Constraints

**Type**: `string`

**Default**: `720h`

#### [](#description-32)Description

RotationInterval is the interval at which the encryption key will be rotated. Must be greater or equal to 7 days. Default is 30 days.

### [](#couchbasebuckets-spec-evictionpolicy)couchbasebuckets.spec.evictionPolicy

#### [](#constraints-33)Constraints

**Type**: `string`

**Default**: `valueOnly`

**Enumerations**: `valueOnly, fullEviction`

#### [](#description-33)Description

EvictionPolicy controls how Couchbase handles memory exhaustion. Value only eviction flushes documents to disk but maintains document metadata in memory in order to improve query performance. Full eviction removes all data from memory after the document is flushed to disk. This field must be "valueOnly" or "fullEviction", defaulting to "valueOnly".

### [](#couchbasebuckets-spec-expirypagersleeptime)couchbasebuckets.spec.expiryPagerSleepTime

#### [](#constraints-34)Constraints

**Type**: `string`

**Default**: `10m`

#### [](#description-34)Description

ExpiryPagerSleepTime defines the time between Expiry Pager runs. It defaults to 10 minutes. This field is only supported for Couchbase Server 8.0.0+.

### [](#couchbasebuckets-spec-historyretention)couchbasebuckets.spec.historyRetention

#### [](#constraints-35)Constraints

**Type**: `object`

#### [](#description-35)Description

HistoryRetention configures settings for bucket history retention and default values for associated collections.

### [](#couchbasebuckets-spec-historyretention-bytes)couchbasebuckets.spec.historyRetention.bytes

#### [](#constraints-36)Constraints

**Type**: `integer`

#### [](#description-36)Description

Bytes defines how much history an individual vbucket should aim to retain on disk in bytes. This field defaults to 0 and has a minimum working value of 2147483648\. This is only supported on buckets with storageBackend=magma.

### [](#couchbasebuckets-spec-historyretention-collectionhistorydefault)couchbasebuckets.spec.historyRetention.collectionHistoryDefault

#### [](#constraints-37)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-37)Description

CollectionHistoryDefault determines whether history retention is enabled for newly created collections by default. This field defaults to true. This is only supported on buckets with storageBackend=magma.

### [](#couchbasebuckets-spec-historyretention-seconds)couchbasebuckets.spec.historyRetention.seconds

#### [](#constraints-38)Constraints

**Type**: `integer`

#### [](#description-38)Description

Seconds defines how many seconds of history an individual vbucket should aim to retain on disk. This field defaults to 0\. This is only supported on buckets with storageBackend=magma.

### [](#couchbasebuckets-spec-iopriority)couchbasebuckets.spec.ioPriority

#### [](#constraints-39)Constraints

**Type**: `string`

**Default**: `low`

**Enumerations**: `low, high`

#### [](#description-39)Description

IOPriority controls how many threads a bucket has, per pod, to process reads and writes. This field must be "low" or "high", defaulting to "low". Modification of this field will cause a temporary service disruption as threads are restarted.

### [](#couchbasebuckets-spec-maxttl)couchbasebuckets.spec.maxTTL

#### [](#constraints-40)Constraints

**Type**: `string`

#### [](#description-40)Description

MaxTTL defines how long a document is permitted to exist for, without modification, until it is automatically deleted. This is a default and maximum time-to-live and may be set to a lower value by the client. If the client specifies a higher value, then it is truncated to the maximum durability. Documents are removed by Couchbase, after they have expired, when either accessed, the expiry pager is run, or the bucket is compacted. When set to 0, then documents are not expired by default. This field must be a duration in the range 0-2147483648s, defaulting to 0\. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbasebuckets-spec-memoryhighwatermark)couchbasebuckets.spec.memoryHighWatermark

#### [](#constraints-41)Constraints

**Type**: `integer`

**Default**: `85`

**Minimum**: `51`

**Maximum**: `90`

#### [](#description-41)Description

MemoryHighWatermark defines the memory high watermark for the bucket. It must be between 51 and 90\. It must also be greater than spec.memoryLowWatermark. It defaults to 85\. This field is only supported for Couchbase Server 8.0.0+.

### [](#couchbasebuckets-spec-memorylowwatermark)couchbasebuckets.spec.memoryLowWatermark

#### [](#constraints-42)Constraints

**Type**: `integer`

**Default**: `75`

**Minimum**: `50`

**Maximum**: `89`

#### [](#description-42)Description

MemoryLowWatermark defines the memory low watermark for the bucket. It must be between 50 and 89\. It must also be less than spec.memoryHighWatermark. It defaults to 75\. This field is only supported for Couchbase Server 8.0.0+.

### [](#couchbasebuckets-spec-memoryquota)couchbasebuckets.spec.memoryQuota

#### [](#constraints-43)Constraints

**Type**: `string`

**Default**: `100Mi`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-43)Description

MemoryQuota is a memory limit to the size of a bucket. When this limit is exceeded, documents will be evicted from memory to disk as defined by the eviction policy. The memory quota is defined per Couchbase pod running the data service. This field defaults to, and must be greater than or equal to 100Mi. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbasebuckets-spec-minimumdurability)couchbasebuckets.spec.minimumDurability

#### [](#constraints-44)Constraints

**Type**: `string`

**Enumerations**: `none, majority, majorityAndPersistActive, persistToMajority`

#### [](#description-44)Description

MiniumumDurability defines how durable a document write is by default, and can be made more durable by the client. This feature enables ACID transactions. When none, Couchbase server will respond when the document is in memory, it will become eventually consistent across the cluster. When majority, Couchbase server will respond when the document is replicated to at least half of the pods running the data service in the cluster. When majorityAndPersistActive, Couchbase server will respond when the document is replicated to at least half of the pods running the data service in the cluster and the document has been persisted to disk on the document master pod. When persistToMajority, Couchbase server will respond when the document is replicated and persisted to disk on at least half of the pods running the data service in the cluster. This field must be either "none", "majority", "majorityAndPersistActive" or "persistToMajority", defaulting to "none".

### [](#couchbasebuckets-spec-name)couchbasebuckets.spec.name

#### [](#constraints-45)Constraints

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-45)Description

Name is the name of the bucket within Couchbase server. By default the Operator will use the `metadata.name` field to define the bucket name. The `metadata.name`field only supports a subset of the supported character set. When specified, this field overrides `metadata.name`. Legal bucket names have a maximum length of 100 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "-\_%\\.".

### [](#couchbasebuckets-spec-numvbuckets)couchbasebuckets.spec.numVBuckets

#### [](#constraints-46)Constraints

**Type**: `integer`

#### [](#description-46)Description

NumVBuckets defines the number of virtual buckets (vBuckets) to be used by the bucket. Can be either 128 or 1024 and is only configurable for magma buckets on server versions 8.0.0 and onward. If migrating from a couchstore to magma bucket, this must be set to 1024.

### [](#couchbasebuckets-spec-onlineevictionpolicychange)couchbasebuckets.spec.onlineEvictionPolicyChange

#### [](#constraints-47)Constraints

**Type**: `boolean`

#### [](#description-47)Description

OnlineEvictionPolicyChange controls whether eviction policy changes can be made online without requiring a bucket restart. If set the eviction policy change will only take effect on the bucket nodes after a swap rebalance, delta recovery, or full recovery. If EnableBucketMigrationRoutines is set to true, on the cluster the operator will perform the swap rebalances. This field defaults to false. This field is only supported for Couchbase Server 8.0.0+. **DEVELOPER PREVIEW**: This feature is in developer preview and should not be used in production clusters.

### [](#couchbasebuckets-spec-rank)couchbasebuckets.spec.rank

#### [](#constraints-48)Constraints

**Type**: `integer`

**Default**: `0`

**Minimum**: `0`

**Maximum**: `1000`

#### [](#description-48)Description

Rank determines the bucket's place in the order in which the rebalance process handles the buckets on the cluster. The higher a bucket's assigned integer (in relation to the integers assigned other buckets), the sooner in the rebalance process the bucket is handled. This assignment of rank allows a cluster's most mission-critical data to be rebalanced with top priority. This option is only supported for Couchbase Server 7.6.0+.

### [](#couchbasebuckets-spec-replicas)couchbasebuckets.spec.replicas

#### [](#constraints-49)Constraints

**Type**: `integer`

**Default**: `1`

**Minimum**: `0`

**Maximum**: `3`

#### [](#description-49)Description

Replicas defines how many copies of documents Couchbase server maintains. This directly affects how fault tolerant a Couchbase cluster is. With a single replica, the cluster can tolerate one data pod going down and still service requests without data loss. The number of replicas also affect memory use. With a single replica, the effective memory quota for documents is halved, with two replicas it is one third. The number of replicas must be between 0 and 3, defaulting to 1.

### [](#couchbasebuckets-spec-scopes)couchbasebuckets.spec.scopes

#### [](#constraints-50)Constraints

**Type**: `object`

#### [](#description-50)Description

Scopes defines whether the Operator manages scopes for the bucket or not, and the set of scopes defined for the bucket.

### [](#couchbasebuckets-spec-scopes-managed)couchbasebuckets.spec.scopes.managed

#### [](#constraints-51)Constraints

**Type**: `boolean`

#### [](#description-51)Description

Managed defines whether scopes are managed for this bucket. This field is `false` by default, and the Operator will take no actions that will affect scopes and collections in this bucket. The default scope and collection will be present. When set to `true`, the Operator will manage user defined scopes, and optionally, their collections as defined by the `CouchbaseScope`, `CouchbaseScopeGroup`, `CouchbaseCollection` and `CouchbaseCollectionGroup` resource documentation. If this field is set to `false` while the already managed, then the Operator will leave whatever configuration is already present.

### [](#couchbasebuckets-spec-scopes-resources)couchbasebuckets.spec.scopes.resources

#### [](#constraints-52)Constraints

**Type**: `[]object`

#### [](#description-52)Description

Resources is an explicit list of named resources that will be considered for inclusion in this bucket. If a resource reference doesn't match a resource, then no error conditions are raised due to undefined resource creation ordering and eventual consistency.

### [](#couchbasebuckets-spec-scopes-resources-kind)couchbasebuckets.spec.scopes.resources.kind

#### [](#constraints-53)Constraints

**Type**: `string`

**Default**: `CouchbaseScope`

**Enumerations**: `CouchbaseScope, CouchbaseScopeGroup`

#### [](#description-53)Description

Kind indicates the kind of resource that is being referenced. A scope can only reference `CouchbaseScope` and `CouchbaseScopeGroup`resource kinds. This field defaults to `CouchbaseScope` if not specified.

### [](#couchbasebuckets-spec-scopes-resources-name)couchbasebuckets.spec.scopes.resources.name

#### [](#constraints-54)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250}$`

#### [](#description-54)Description

Name is the name of the Kubernetes resource name that is being referenced. Legal scope names have a maximum length of 251 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "\_-%".

### [](#couchbasebuckets-spec-scopes-selector)couchbasebuckets.spec.scopes.selector

#### [](#constraints-55)Constraints

**Type**: `object`

#### [](#description-55)Description

Selector allows resources to be implicitly considered for inclusion in this bucket. More info: <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#labelselector-v1-meta>.

### [](#couchbasebuckets-spec-storagebackend)couchbasebuckets.spec.storageBackend

#### [](#constraints-56)Constraints

**Type**: `string`

**Enumerations**: `couchstore, magma`

#### [](#description-56)Description

StorageBackend to be assigned to and used by the bucket. Only valid for Couchbase Server 7.0.0 onward. Two different backend storage mechanisms can be used - "couchstore" or "magma", defaulting to "couchstore" for server versions earlier than 8.0.0\. Defaults to "magma" for server versions 8.0.0 and onward. Note: "magma" is only valid for Couchbase Server 7.1.0 onward.

### [](#couchbasebuckets-spec-versionpruningwindowhrs)couchbasebuckets.spec.versionPruningWindowHrs

#### [](#constraints-57)Constraints

**Type**: `integer`

#### [](#description-57)Description

VersionPruningWindowHrs defines the number of hours to retain version history for a bucket. This field must be an integer larger than 23, defaulting to 720 (30 days). This feature is only supported for Couchbase Server 7.6.0+.

### [](#couchbasebuckets-spec-warmupbehavior)couchbasebuckets.spec.warmupBehavior

#### [](#constraints-58)Constraints

**Type**: `string`

**Default**: `background`

**Enumerations**: `none, background, blocking`

#### [](#description-58)Description

WarmupBehavior defines the behavior of the bucket when it is being warmed up. It defaults to "background". This field is only supported for Couchbase Server 8.0.0+.