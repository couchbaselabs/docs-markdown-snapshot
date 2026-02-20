---
title: CouchbaseBucket Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.7.x/docs/user/modules/ROOT/pages/resource/couchbasebucket.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.7@operator::resource/couchbasebucket.adoc[]
---

[View original HTML](/operator/2.7/resource/couchbasebucket.html)

# CouchbaseBucket Resource

The CouchbaseBucket resource defines a set of documents in Couchbase server. A Couchbase client connects to and operates on a bucket, which provides independent management of a set documents and a security boundary for role based access control. A CouchbaseBucket provides replication and persistence for documents contained by it.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseBucket
metadata:
  name: ""
spec:
  compressionMode: passive
  conflictResolution: seqno
  enableFlush: false
  enableIndexReplica: false
  evictionPolicy: valueOnly
  ioPriority: low
  maxTTL: ""
  memoryQuota: 100Mi
  minimumDurability: ""
  name: ""
  rank: 0
  replicas: 1
  scopes:
    managed: false
    resources:
    - kind: CouchbaseScope
      name: ""
    selector: {}
  storageBackend: ""
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

### [](#couchbasebuckets-spec-compressionmode)couchbasebuckets.spec.compressionMode

#### [](#constraints-9)Constraints

**Type**: `string`

**Default**: `passive`

**Enumerations**: `off, passive, active`

#### [](#description-9)Description

CompressionMode defines how Couchbase server handles document compression. When off, documents are stored in memory, and transferred to the client uncompressed. When passive, documents are stored compressed in memory, and transferred to the client compressed when requested. When active, documents are stored compresses in memory and when transferred to the client. This field must be "off", "passive" or "active", defaulting to "passive". Be aware "off" in YAML 1.2 is a boolean, so must be quoted as a string in configuration files.

### [](#couchbasebuckets-spec-conflictresolution)couchbasebuckets.spec.conflictResolution

#### [](#constraints-10)Constraints

**Type**: `string`

**Default**: `seqno`

**Enumerations**: `seqno, lww`

#### [](#description-10)Description

ConflictResolution defines how XDCR handles concurrent write conflicts. Sequence number based resolution selects the document with the highest sequence number as the most recent. Timestamp based resolution selects the document that was written to most recently as the most recent. This field must be "seqno" (sequence based), or "lww" (timestamp based), defaulting to "seqno".

### [](#couchbasebuckets-spec-enableflush)couchbasebuckets.spec.enableFlush

#### [](#constraints-11)Constraints

**Type**: `boolean`

#### [](#description-11)Description

EnableFlush defines whether a client can delete all documents in a bucket. This field defaults to false.

### [](#couchbasebuckets-spec-enableindexreplica)couchbasebuckets.spec.enableIndexReplica

#### [](#constraints-12)Constraints

**Type**: `boolean`

#### [](#description-12)Description

EnableIndexReplica defines whether indexes for this bucket are replicated. This field defaults to false.

### [](#couchbasebuckets-spec-evictionpolicy)couchbasebuckets.spec.evictionPolicy

#### [](#constraints-13)Constraints

**Type**: `string`

**Default**: `valueOnly`

**Enumerations**: `valueOnly, fullEviction`

#### [](#description-13)Description

EvictionPolicy controls how Couchbase handles memory exhaustion. Value only eviction flushes documents to disk but maintains document metadata in memory in order to improve query performance. Full eviction removes all data from memory after the document is flushed to disk. This field must be "valueOnly" or "fullEviction", defaulting to "valueOnly".

### [](#couchbasebuckets-spec-iopriority)couchbasebuckets.spec.ioPriority

#### [](#constraints-14)Constraints

**Type**: `string`

**Default**: `low`

**Enumerations**: `low, high`

#### [](#description-14)Description

IOPriority controls how many threads a bucket has, per pod, to process reads and writes. This field must be "low" or "high", defaulting to "low". Modification of this field will cause a temporary service disruption as threads are restarted.

### [](#couchbasebuckets-spec-maxttl)couchbasebuckets.spec.maxTTL

#### [](#constraints-15)Constraints

**Type**: `string`

#### [](#description-15)Description

MaxTTL defines how long a document is permitted to exist for, without modification, until it is automatically deleted. This is a default and maximum time-to-live and may be set to a lower value by the client. If the client specifies a higher value, then it is truncated to the maximum durability. Documents are removed by Couchbase, after they have expired, when either accessed, the expiry pager is run, or the bucket is compacted. When set to 0, then documents are not expired by default. This field must be a duration in the range 0-2147483648s, defaulting to 0\. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbasebuckets-spec-memoryquota)couchbasebuckets.spec.memoryQuota

#### [](#constraints-16)Constraints

**Type**: `string`

**Default**: `100Mi`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-16)Description

MemoryQuota is a memory limit to the size of a bucket. When this limit is exceeded, documents will be evicted from memory to disk as defined by the eviction policy. The memory quota is defined per Couchbase pod running the data service. This field defaults to, and must be greater than or equal to 100Mi. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbasebuckets-spec-minimumdurability)couchbasebuckets.spec.minimumDurability

#### [](#constraints-17)Constraints

**Type**: `string`

**Enumerations**: `none, majority, majorityAndPersistActive, persistToMajority`

#### [](#description-17)Description

MiniumumDurability defines how durable a document write is by default, and can be made more durable by the client. This feature enables ACID transactions. When none, Couchbase server will respond when the document is in memory, it will become eventually consistent across the cluster. When majority, Couchbase server will respond when the document is replicated to at least half of the pods running the data service in the cluster. When majorityAndPersistActive, Couchbase server will respond when the document is replicated to at least half of the pods running the data service in the cluster and the document has been persisted to disk on the document master pod. When persistToMajority, Couchbase server will respond when the document is replicated and persisted to disk on at least half of the pods running the data service in the cluster. This field must be either "none", "majority", "majorityAndPersistActive" or "persistToMajority", defaulting to "none".

### [](#couchbasebuckets-spec-name)couchbasebuckets.spec.name

#### [](#constraints-18)Constraints

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-18)Description

Name is the name of the bucket within Couchbase server. By default the Operator will use the `metadata.name` field to define the bucket name. The `metadata.name`field only supports a subset of the supported character set. When specified, this field overrides `metadata.name`. Legal bucket names have a maximum length of 100 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "-\_%\\.".

### [](#couchbasebuckets-spec-rank)couchbasebuckets.spec.rank

#### [](#constraints-19)Constraints

**Type**: `integer`

**Default**: `0`

**Minimum**: `0`

**Maximum**: `1000`

#### [](#description-19)Description

Rank determines the bucket’s place in the order in which the rebalance process handles the buckets on the cluster. The higher a bucket’s assigned integer (in relation to the integers assigned other buckets), the sooner in the rebalance process the bucket is handled. This assignment of rank allows a cluster’s most mission-critical data to be rebalanced with top priority. This option is only supported for Couchbase Server 7.6.0+.

### [](#couchbasebuckets-spec-replicas)couchbasebuckets.spec.replicas

#### [](#constraints-20)Constraints

**Type**: `integer`

**Default**: `1`

**Minimum**: `0`

**Maximum**: `3`

#### [](#description-20)Description

Replicas defines how many copies of documents Couchbase server maintains. This directly affects how fault tolerant a Couchbase cluster is. With a single replica, the cluster can tolerate one data pod going down and still service requests without data loss. The number of replicas also affect memory use. With a single replica, the effective memory quota for documents is halved, with two replicas it is one third. The number of replicas must be between 0 and 3, defaulting to 1.

### [](#couchbasebuckets-spec-scopes)couchbasebuckets.spec.scopes

#### [](#constraints-21)Constraints

**Type**: `object`

#### [](#description-21)Description

Scopes defines whether the Operator manages scopes for the bucket or not, and the set of scopes defined for the bucket.

### [](#couchbasebuckets-spec-scopes-managed)couchbasebuckets.spec.scopes.managed

#### [](#constraints-22)Constraints

**Type**: `boolean`

#### [](#description-22)Description

Managed defines whether scopes are managed for this bucket. This field is `false` by default, and the Operator will take no actions that will affect scopes and collections in this bucket. The default scope and collection will be present. When set to `true`, the Operator will manage user defined scopes, and optionally, their collections as defined by the `CouchbaseScope`, `CouchbaseScopeGroup`, `CouchbaseCollection` and `CouchbaseCollectionGroup` resource documentation. If this field is set to `false` while the already managed, then the Operator will leave whatever configuration is already present.

### [](#couchbasebuckets-spec-scopes-resources)couchbasebuckets.spec.scopes.resources

#### [](#constraints-23)Constraints

**Type**: `[]object`

#### [](#description-23)Description

Resources is an explicit list of named resources that will be considered for inclusion in this bucket. If a resource reference doesn’t match a resource, then no error conditions are raised due to undefined resource creation ordering and eventual consistency.

### [](#couchbasebuckets-spec-scopes-resources-kind)couchbasebuckets.spec.scopes.resources.kind

#### [](#constraints-24)Constraints

**Type**: `string`

**Default**: `CouchbaseScope`

**Enumerations**: `CouchbaseScope, CouchbaseScopeGroup`

#### [](#description-24)Description

Kind indicates the kind of resource that is being referenced. A scope can only reference `CouchbaseScope` and `CouchbaseScopeGroup`resource kinds. This field defaults to `CouchbaseScope` if not specified.

### [](#couchbasebuckets-spec-scopes-resources-name)couchbasebuckets.spec.scopes.resources.name

#### [](#constraints-25)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250}$`

#### [](#description-25)Description

Name is the name of the Kubernetes resource name that is being referenced. Legal scope names have a maximum length of 251 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "\_-%".

### [](#couchbasebuckets-spec-scopes-selector)couchbasebuckets.spec.scopes.selector

#### [](#constraints-26)Constraints

**Type**: `object`

#### [](#description-26)Description

Selector allows resources to be implicitly considered for inclusion in this bucket. More info: <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#labelselector-v1-meta>.

### [](#couchbasebuckets-spec-storagebackend)couchbasebuckets.spec.storageBackend

#### [](#constraints-27)Constraints

**Type**: `string`

**Enumerations**: `couchstore, magma`

#### [](#description-27)Description

StorageBackend to be assigned to and used by the bucket. Only valid for Couchbase Server 7.0.0 onward. Two different backend storage mechanisms can be used - "couchstore" or "magma", defaulting to "couchstore". Note: "magma" is only valid for Couchbase Server 7.1.0 onward.