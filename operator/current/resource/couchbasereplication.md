---
title: CouchbaseReplication Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.9.x/docs/user/modules/ROOT/pages/resource/couchbasereplication.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:operator::resource/couchbasereplication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/resource/couchbasereplication.html)

# CouchbaseReplication Resource

The CouchbaseReplication resource represents a Couchbase-to-Couchbase, XDCR replication stream from a source bucket to a destination bucket. This provides off-site backup, migration, and disaster recovery.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
explicitMapping:
  allowRules:
  - sourceKeyspace:
      collection: ""
      scope: ""
    targetKeyspace:
      collection: ""
      scope: ""
  denyRules:
  - sourceKeyspace:
      collection: ""
      scope: ""
kind: CouchbaseReplication
metadata:
  name: ""
spec:
  bucket: ""
  checkpointInterval: 0
  collectionsOSOMode: false
  compressionType: ""
  conflictLogging:
    enabled: false
    logCollection:
      bucket: ""
      collection: ""
      scope: ""
    loggingRules:
      customCollectionRules:
      - collection: ""
        logCollection:
          bucket: ""
          collection: ""
          scope: ""
        scope: ""
      defaultCollectionRules:
      - collection: ""
        scope: ""
      noLoggingRules:
      - collection: ""
        scope: ""
  desiredLatency: 0
  docBatchSizeKb: 0
  failureRestartInterval: 0
  filterBinary: false
  filterBypassExpiry: false
  filterBypassUncommittedTxn: false
  filterDeletion: false
  filterExpiration: false
  filterExpression: ""
  filterSkipRestream: false
  hlvPruningWindowSec: 0
  jsFunctionTimeoutMs: 0
  logLevel: ""
  mergeFunctionMapping:
  mobile: ""
  networkUsageLimit: 0
  optimisticReplicationThreshold: 0
  paused: false
  priority: ""
  remoteBucket: ""
  retryOnRemoteAuthErr: false
  retryOnRemoteAuthErrMaxWaitSec: 0
  sourceNozzlePerNode: 0
  statsInterval: 0
  targetNozzlePerNode: 0
  workerBatchSize: 0
```

## [](#couchbasereplications-apiversion)couchbasereplications.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbasereplications-explicitmapping)couchbasereplications.explicitMapping

### [](#constraints-2)Constraints

**Type**: `object`

### [](#description-2)Description

The explicit mappings to use for replication which are optional. For Scopes and Collection replication support we can specify a set of implicit and explicit mappings to use. If none is specified then it is assumed to be existing bucket level replication. <https://docs.couchbase.com/server/current/learn/clusters-and-availability/xdcr-with-scopes-and-collections.html#explicit-mapping>.

### [](#couchbasereplications-explicitmapping-allowrules)couchbasereplications.explicitMapping.allowRules

#### [](#constraints-3)Constraints

**Type**: `[]object`

#### [](#description-3)Description

The list of explicit replications to carry out including any nested implicit replications: specifying a scope implicitly replicates all collections within it. There should be no duplicates, including more-specific duplicates, e.g. if you specify replication of a scope then you can only deny replication of collections within it.

### [](#couchbasereplications-explicitmapping-allowrules-sourcekeyspace)couchbasereplications.explicitMapping.allowRules.sourceKeyspace

#### [](#constraints-4)Constraints

**Required**

**Type**: `object`

#### [](#description-4)Description

The source keyspace: where to replicate from. Source and target must match whether they have a collection or not, i.e. you cannot replicate from a scope to a collection.

### [](#couchbasereplications-explicitmapping-allowrules-sourcekeyspace-collection)couchbasereplications.explicitMapping.allowRules.sourceKeyspace.collection

#### [](#constraints-5)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-5)Description

The optional collection within the scope. May be empty to just work at scope level.

### [](#couchbasereplications-explicitmapping-allowrules-sourcekeyspace-scope)couchbasereplications.explicitMapping.allowRules.sourceKeyspace.scope

#### [](#constraints-6)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-6)Description

The scope to use.

### [](#couchbasereplications-explicitmapping-allowrules-targetkeyspace)couchbasereplications.explicitMapping.allowRules.targetKeyspace

#### [](#constraints-7)Constraints

**Required**

**Type**: `object`

#### [](#description-7)Description

The target keyspace: where to replicate to. Source and target must match whether they have a collection or not, i.e. you cannot replicate from a scope to a collection.

### [](#couchbasereplications-explicitmapping-allowrules-targetkeyspace-collection)couchbasereplications.explicitMapping.allowRules.targetKeyspace.collection

#### [](#constraints-8)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-8)Description

The optional collection within the scope. May be empty to just work at scope level.

### [](#couchbasereplications-explicitmapping-allowrules-targetkeyspace-scope)couchbasereplications.explicitMapping.allowRules.targetKeyspace.scope

#### [](#constraints-9)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-9)Description

The scope to use.

### [](#couchbasereplications-explicitmapping-denyrules)couchbasereplications.explicitMapping.denyRules

#### [](#constraints-10)Constraints

**Type**: `[]object`

#### [](#description-10)Description

The list of explicit replications to prevent including any nested implicit denials: specifying a scope implicitly denies all collections within it. There should be no duplicates, including more-specific duplicates, e.g. if you specify denial of replication of a scope then you can only specify replication of collections within it.

### [](#couchbasereplications-explicitmapping-denyrules-sourcekeyspace)couchbasereplications.explicitMapping.denyRules.sourceKeyspace

#### [](#constraints-11)Constraints

**Required**

**Type**: `object`

#### [](#description-11)Description

The source keyspace: where to block replication from.

### [](#couchbasereplications-explicitmapping-denyrules-sourcekeyspace-collection)couchbasereplications.explicitMapping.denyRules.sourceKeyspace.collection

#### [](#constraints-12)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-12)Description

The optional collection within the scope. May be empty to just work at scope level.

### [](#couchbasereplications-explicitmapping-denyrules-sourcekeyspace-scope)couchbasereplications.explicitMapping.denyRules.sourceKeyspace.scope

#### [](#constraints-13)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-13)Description

The scope to use.

## [](#couchbasereplications-kind)couchbasereplications.kind

### [](#constraints-14)Constraints

**Type**: `string`

### [](#description-14)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbasereplications-metadata)couchbasereplications.metadata

### [](#constraints-15)Constraints

**Required**

**Type**: `object`

### [](#description-15)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbasereplications-metadata-name)couchbasereplications.metadata.name

#### [](#constraints-16)Constraints

**Type**: `string`

#### [](#description-16)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbasereplications-metadata-namespace)couchbasereplications.metadata.namespace

#### [](#constraints-17)Constraints

**Type**: `string`

#### [](#description-17)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbasereplications-metadata-labels)couchbasereplications.metadata.labels

#### [](#constraints-18)Constraints

**Type**: `map[string]string`

#### [](#description-18)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbasereplications-metadata-annotations)couchbasereplications.metadata.annotations

#### [](#constraints-19)Constraints

**Type**: `map[string]string`

#### [](#description-19)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbasereplications-spec)couchbasereplications.spec

### [](#constraints-20)Constraints

**Required**

**Type**: `object`

### [](#description-20)Description

CouchbaseReplicationSpec allows configuration of an XDCR replication.

### [](#couchbasereplications-spec-bucket)couchbasereplications.spec.bucket

#### [](#constraints-21)Constraints

**Required**

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-21)Description

Bucket is the source bucket to replicate from. This refers to the Couchbase bucket name, not the resource name of the bucket. A bucket with this name must be defined on this cluster. Legal bucket names have a maximum length of 100 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "-\_%\\.".

### [](#couchbasereplications-spec-checkpointinterval)couchbasereplications.spec.checkpointInterval

#### [](#constraints-22)Constraints

**Type**: `integer`

**Minimum**: `60`

**Maximum**: `14400`

#### [](#description-22)Description

CheckpointInterval is the interval in seconds between checkpoints.

### [](#couchbasereplications-spec-collectionsosomode)couchbasereplications.spec.collectionsOSOMode

#### [](#constraints-23)Constraints

**Type**: `boolean`

#### [](#description-23)Description

CollectionsOSOMode optimizes for out-of-order mutations streaming (performance toggle). This field defaults to true.

### [](#couchbasereplications-spec-compressiontype)couchbasereplications.spec.compressionType

#### [](#constraints-24)Constraints

**Type**: `string`

**Enumerations**: `Auto, None`

#### [](#description-24)Description

CompressionType is the compression used for XDCR traffic.

### [](#couchbasereplications-spec-conflictlogging)couchbasereplications.spec.conflictLogging

#### [](#constraints-25)Constraints

**Type**: `object`

#### [](#description-25)Description

ConflictLogging is the configuration for conflict logging. This feature is available in Couchbase Server 8.0.0 and later.

### [](#couchbasereplications-spec-conflictlogging-enabled)couchbasereplications.spec.conflictLogging.enabled

#### [](#constraints-26)Constraints

**Type**: `boolean`

#### [](#description-26)Description

Enabled defines whether conflict logging is enabled.

### [](#couchbasereplications-spec-conflictlogging-logcollection)couchbasereplications.spec.conflictLogging.logCollection

#### [](#constraints-27)Constraints

**Type**: `object`

#### [](#description-27)Description

LogCollection defines the collection to log conflicts to.

### [](#couchbasereplications-spec-conflictlogging-logcollection-bucket)couchbasereplications.spec.conflictLogging.logCollection.bucket

#### [](#constraints-28)Constraints

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-28)Description

Bucket defines the bucket to log conflicts to.

### [](#couchbasereplications-spec-conflictlogging-logcollection-collection)couchbasereplications.spec.conflictLogging.logCollection.collection

#### [](#constraints-29)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-29)Description

Collection defines the collection to log conflicts to.

### [](#couchbasereplications-spec-conflictlogging-logcollection-scope)couchbasereplications.spec.conflictLogging.logCollection.scope

#### [](#constraints-30)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-30)Description

Scope defines the scope to log conflicts to.

### [](#couchbasereplications-spec-conflictlogging-loggingrules)couchbasereplications.spec.conflictLogging.loggingRules

#### [](#constraints-31)Constraints

**Type**: `object`

#### [](#description-31)Description

LoggingRules defines the list of logging rules for conflict logging. The rules can be scoped to a specific scope or a specific collection in a scope. The rules can disable logging, log to the default collection defined at `spec.conflictLogging.logCollection`, or log to a different collection.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-customcollectionrules)couchbasereplications.spec.conflictLogging.loggingRules.customCollectionRules

#### [](#constraints-32)Constraints

**Type**: `[]object`

#### [](#description-32)Description

CustomCollectionRules defines the rules for logging to a different collection.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-customcollectionrules-collection)couchbasereplications.spec.conflictLogging.loggingRules.customCollectionRules.collection

#### [](#constraints-33)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-33)Description

Collection defines the collection to apply the rule to.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-customcollectionrules-logcollection)couchbasereplications.spec.conflictLogging.loggingRules.customCollectionRules.logCollection

#### [](#constraints-34)Constraints

**Required**

**Type**: `object`

#### [](#description-34)Description

LogCollection defines the collection to log conflicts to.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-customcollectionrules-logcollection-bucket)couchbasereplications.spec.conflictLogging.loggingRules.customCollectionRules.logCollection.bucket

#### [](#constraints-35)Constraints

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-35)Description

Bucket defines the bucket to log conflicts to.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-customcollectionrules-logcollection-collection)couchbasereplications.spec.conflictLogging.loggingRules.customCollectionRules.logCollection.collection

#### [](#constraints-36)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-36)Description

Collection defines the collection to log conflicts to.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-customcollectionrules-logcollection-scope)couchbasereplications.spec.conflictLogging.loggingRules.customCollectionRules.logCollection.scope

#### [](#constraints-37)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-37)Description

Scope defines the scope to log conflicts to.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-customcollectionrules-scope)couchbasereplications.spec.conflictLogging.loggingRules.customCollectionRules.scope

#### [](#constraints-38)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-38)Description

Scope defines the scope to apply the rule to.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-defaultcollectionrules)couchbasereplications.spec.conflictLogging.loggingRules.defaultCollectionRules

#### [](#constraints-39)Constraints

**Type**: `[]object`

#### [](#description-39)Description

DefaultCollectionRules defines the rules for logging to the default collection.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-defaultcollectionrules-collection)couchbasereplications.spec.conflictLogging.loggingRules.defaultCollectionRules.collection

#### [](#constraints-40)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-40)Description

Collection defines the collection to apply the rule to.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-defaultcollectionrules-scope)couchbasereplications.spec.conflictLogging.loggingRules.defaultCollectionRules.scope

#### [](#constraints-41)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-41)Description

Scope defines the scope to apply the rule to.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-nologgingrules)couchbasereplications.spec.conflictLogging.loggingRules.noLoggingRules

#### [](#constraints-42)Constraints

**Type**: `[]object`

#### [](#description-42)Description

NoLoggingRules defines the rules for disabling logging to for conflicts in a specific scope or collection.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-nologgingrules-collection)couchbasereplications.spec.conflictLogging.loggingRules.noLoggingRules.collection

#### [](#constraints-43)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-43)Description

Collection defines the collection to apply the rule to.

### [](#couchbasereplications-spec-conflictlogging-loggingrules-nologgingrules-scope)couchbasereplications.spec.conflictLogging.loggingRules.noLoggingRules.scope

#### [](#constraints-44)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-44)Description

Scope defines the scope to apply the rule to.

### [](#couchbasereplications-spec-desiredlatency)couchbasereplications.spec.desiredLatency

#### [](#constraints-45)Constraints

**Type**: `integer`

#### [](#description-45)Description

DesiredLatency is the target latency (ms) for high-priority replications. This field defaults to 50.

### [](#couchbasereplications-spec-docbatchsizekb)couchbasereplications.spec.docBatchSizeKb

#### [](#constraints-46)Constraints

**Type**: `integer`

**Minimum**: `10`

**Maximum**: `10000`

#### [](#description-46)Description

DocBatchSizeKb is the size (KB) of document batches sent.

### [](#couchbasereplications-spec-failurerestartinterval)couchbasereplications.spec.failureRestartInterval

#### [](#constraints-47)Constraints

**Type**: `integer`

**Minimum**: `1`

**Maximum**: `300`

#### [](#description-47)Description

FailureRestartInterval is the seconds to wait before restarting after a failure.

### [](#couchbasereplications-spec-filterbinary)couchbasereplications.spec.filterBinary

#### [](#constraints-48)Constraints

**Type**: `boolean`

#### [](#description-48)Description

FilterBinary specifies whether binary documents should be replicated. The value can be true or false (the default). If the value is true, binary documents are not replicated, regardless of whether a filterExpression is applied. If the value is false: The behavior is identical to that of all Couchbase-Server versions prior to 7.2.1 (with the exception of 7.1.5), where the filterBinary flag did not exist. If a filter expression is not provided, binary documents are replicated. If a filter expression is provided, and the expression refers only to either the document's key, or its xattr, or to both, the expression is applied, and the document is replicated if the expression permits. If a filter expression is provided, and the expression refers only to the document's body, the document is replicated. If a filter expression is provided, and the expression refers to the document's key, or its xattr, or to both; and also refers to the document's body; the document is not replicated (regardless of whether the key or xattr might appear to permit replication).

### [](#couchbasereplications-spec-filterbypassexpiry)couchbasereplications.spec.filterBypassExpiry

#### [](#constraints-49)Constraints

**Type**: `boolean`

#### [](#description-49)Description

FilterBypassExpiry when true, TTL is removed before replication.

### [](#couchbasereplications-spec-filterbypassuncommittedtxn)couchbasereplications.spec.filterBypassUncommittedTxn

#### [](#constraints-50)Constraints

**Type**: `boolean`

#### [](#description-50)Description

FilterBypassUncommittedTxn when true, documents with uncommitted txn xattrs are not replicated.

### [](#couchbasereplications-spec-filterdeletion)couchbasereplications.spec.filterDeletion

#### [](#constraints-51)Constraints

**Type**: `boolean`

#### [](#description-51)Description

FilterDeletion when true, delete mutations are filtered out (not replicated).

### [](#couchbasereplications-spec-filterexpiration)couchbasereplications.spec.filterExpiration

#### [](#constraints-52)Constraints

**Type**: `boolean`

#### [](#description-52)Description

FilterExpiration when true, expiry mutations are filtered out.

### [](#couchbasereplications-spec-filterexpression)couchbasereplications.spec.filterExpression

#### [](#constraints-53)Constraints

**Type**: `string`

#### [](#description-53)Description

FilterExpression is a filter expression to match against documents in the source bucket. Each document that produces a successful match is replicated.

### [](#couchbasereplications-spec-filterskiprestream)couchbasereplications.spec.filterSkipRestream

#### [](#constraints-54)Constraints

**Type**: `boolean`

#### [](#description-54)Description

FilterSkipRestream controls whether replication restarts after filterExpression changes. When false (default), replication restarts after filter changes. When true, continues without restart. Note: Server requires this field when filterExpression is set. If not specified, operator defaults to false.

### [](#couchbasereplications-spec-hlvpruningwindowsec)couchbasereplications.spec.hlvPruningWindowSec

#### [](#constraints-55)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-55)Description

HlvPruningWindowSec is the HLV pruning window (sec) for hybrid logical vector conflict resolution.

### [](#couchbasereplications-spec-jsfunctiontimeoutms)couchbasereplications.spec.jsFunctionTimeoutMs

#### [](#constraints-56)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-56)Description

JSFunctionTimeoutMs is the timeout for JS custom conflict-resolution functions (ms).

### [](#couchbasereplications-spec-loglevel)couchbasereplications.spec.logLevel

#### [](#constraints-57)Constraints

**Type**: `string`

**Enumerations**: `Error, Info, Debug, Trace`

#### [](#description-57)Description

LogLevel is the logging verbosity for XDCR.

### [](#couchbasereplications-spec-mergefunctionmapping)couchbasereplications.spec.mergeFunctionMapping

#### [](#constraints-58)Constraints

**Type**: `map[string]string`

#### [](#description-58)Description

MergeFunctionMapping maps collection specifiers (scope.collection) to merge function names for custom conflict resolution. Nil values can be used to explicitly unset merge functions for specific collections.

### [](#couchbasereplications-spec-mobile)couchbasereplications.spec.mobile

#### [](#constraints-59)Constraints

**Type**: `string`

**Enumerations**: `Off, Active`

#### [](#description-59)Description

Mobile enables mobile (Sync Gateway) active-active mode. This feature is available in Couchbase Server 7.6.4 and later.

### [](#couchbasereplications-spec-networkusagelimit)couchbasereplications.spec.networkUsageLimit

#### [](#constraints-60)Constraints

**Type**: `integer`

**Minimum**: `0`

#### [](#description-60)Description

NetworkUsageLimit is the upper limit for replication network usage (MB/s).

### [](#couchbasereplications-spec-optimisticreplicationthreshold)couchbasereplications.spec.optimisticReplicationThreshold

#### [](#constraints-61)Constraints

**Type**: `integer`

**Minimum**: `0`

**Maximum**: `20971520`

#### [](#description-61)Description

OptimisticReplicationThreshold is the size threshold below which documents replicate optimistically.

### [](#couchbasereplications-spec-paused)couchbasereplications.spec.paused

#### [](#constraints-62)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-62)Description

PauseRequested indicates whether the replication has been issued a pause request.

### [](#couchbasereplications-spec-priority)couchbasereplications.spec.priority

#### [](#constraints-63)Constraints

**Type**: `string`

**Enumerations**: `High, Medium, Low`

#### [](#description-63)Description

Priority is the resource priority for replication streams.

### [](#couchbasereplications-spec-remotebucket)couchbasereplications.spec.remoteBucket

#### [](#constraints-64)Constraints

**Required**

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-64)Description

RemoteBucket is the remote bucket name to synchronize to. This refers to the Couchbase bucket name, not the resource name of the bucket. Legal bucket names have a maximum length of 100 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "-\_%\\.".

### [](#couchbasereplications-spec-retryonremoteautherr)couchbasereplications.spec.retryOnRemoteAuthErr

#### [](#constraints-65)Constraints

**Type**: `boolean`

#### [](#description-65)Description

RetryOnRemoteAuthErr defines whether to retry connections when remote auth fails.

### [](#couchbasereplications-spec-retryonremoteautherrmaxwaitsec)couchbasereplications.spec.retryOnRemoteAuthErrMaxWaitSec

#### [](#constraints-66)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-66)Description

RetryOnRemoteAuthErrMaxWaitSec is the max wait seconds for retrying remote auth failures. Only effective if retryOnRemoteAuthErr is true.

### [](#couchbasereplications-spec-sourcenozzlepernode)couchbasereplications.spec.sourceNozzlePerNode

#### [](#constraints-67)Constraints

**Type**: `integer`

**Minimum**: `1`

**Maximum**: `100`

#### [](#description-67)Description

SourceNozzlePerNode is the number of source nozzles (parallelism) per source node.

### [](#couchbasereplications-spec-statsinterval)couchbasereplications.spec.statsInterval

#### [](#constraints-68)Constraints

**Type**: `integer`

**Minimum**: `200`

**Maximum**: `600000`

#### [](#description-68)Description

StatsInterval is the interval for statistics updates (ms).

### [](#couchbasereplications-spec-targetnozzlepernode)couchbasereplications.spec.targetNozzlePerNode

#### [](#constraints-69)Constraints

**Type**: `integer`

**Minimum**: `1`

**Maximum**: `100`

#### [](#description-69)Description

TargetNozzlePerNode is the number of target nozzles per target node (parallelism).

### [](#couchbasereplications-spec-workerbatchsize)couchbasereplications.spec.workerBatchSize

#### [](#constraints-70)Constraints

**Type**: `integer`

**Minimum**: `500`

**Maximum**: `10000`

#### [](#description-70)Description

WorkerBatchSize is the number of mutations per worker batch.