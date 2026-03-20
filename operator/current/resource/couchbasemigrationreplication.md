---
title: CouchbaseMigrationReplication Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.9.x/docs/user/modules/ROOT/pages/resource/couchbasemigrationreplication.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:operator::resource/couchbasemigrationreplication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/resource/couchbasemigrationreplication.html)

# CouchbaseMigrationReplication Resource

The CouchbaseScopeMigration resource represents the use of the special migration mapping within XDCR to take a filtered list from the default scope and collection of the source bucket, replicate it to named scopes and collections within the target bucket. The bucket-to-bucket replication cannot duplicate any used by the CouchbaseReplication resource, as these two types of replication are mutually exclusive between buckets. <https://docs.couchbase.com/server/current/learn/clusters-and-availability/xdcr-with-scopes-and-collections.html#migration>.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseMigrationReplication
metadata:
  name: ""
migrationMapping:
  mappings:
  - filter: _default._default
    targetKeyspace:
      collection: ""
      scope: ""
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

## [](#couchbasemigrationreplications-apiversion)couchbasemigrationreplications.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbasemigrationreplications-kind)couchbasemigrationreplications.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbasemigrationreplications-metadata)couchbasemigrationreplications.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbasemigrationreplications-metadata-name)couchbasemigrationreplications.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbasemigrationreplications-metadata-namespace)couchbasemigrationreplications.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbasemigrationreplications-metadata-labels)couchbasemigrationreplications.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbasemigrationreplications-metadata-annotations)couchbasemigrationreplications.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbasemigrationreplications-migrationmapping)couchbasemigrationreplications.migrationMapping

### [](#constraints-8)Constraints

**Required**

**Type**: `object`

### [](#description-8)Description

The migration mappings to use, should never be empty as that is just an implicit bucket-to-bucket replication then.

### [](#couchbasemigrationreplications-migrationmapping-mappings)couchbasemigrationreplications.migrationMapping.mappings

#### [](#constraints-9)Constraints

**Required**

**Type**: `[]object`

#### [](#description-9)Description

The migration mappings to use, should never be empty as that is just an implicit bucket-to-bucket replication then.

### [](#couchbasemigrationreplications-migrationmapping-mappings-filter)couchbasemigrationreplications.migrationMapping.mappings.filter

#### [](#constraints-10)Constraints

**Type**: `string`

**Default**: `_default._default`

#### [](#description-10)Description

A filter to select from the source default scope and collection. Defaults to select everything in the default scope and collection.

### [](#couchbasemigrationreplications-migrationmapping-mappings-targetkeyspace)couchbasemigrationreplications.migrationMapping.mappings.targetKeyspace

#### [](#constraints-11)Constraints

**Required**

**Type**: `object`

#### [](#description-11)Description

The destination of our migration, must be a scope and collection.

### [](#couchbasemigrationreplications-migrationmapping-mappings-targetkeyspace-collection)couchbasemigrationreplications.migrationMapping.mappings.targetKeyspace.collection

#### [](#constraints-12)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-12)Description

The optional collection within the scope. May be empty to just work at scope level.

### [](#couchbasemigrationreplications-migrationmapping-mappings-targetkeyspace-scope)couchbasemigrationreplications.migrationMapping.mappings.targetKeyspace.scope

#### [](#constraints-13)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-13)Description

The scope to use.

## [](#couchbasemigrationreplications-spec)couchbasemigrationreplications.spec

### [](#constraints-14)Constraints

**Required**

**Type**: `object`

### [](#description-14)Description

CouchbaseReplicationSpec allows configuration of an XDCR replication.

### [](#couchbasemigrationreplications-spec-bucket)couchbasemigrationreplications.spec.bucket

#### [](#constraints-15)Constraints

**Required**

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-15)Description

Bucket is the source bucket to replicate from. This refers to the Couchbase bucket name, not the resource name of the bucket. A bucket with this name must be defined on this cluster. Legal bucket names have a maximum length of 100 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "-\_%\\.".

### [](#couchbasemigrationreplications-spec-checkpointinterval)couchbasemigrationreplications.spec.checkpointInterval

#### [](#constraints-16)Constraints

**Type**: `integer`

**Minimum**: `60`

**Maximum**: `14400`

#### [](#description-16)Description

CheckpointInterval is the interval in seconds between checkpoints.

### [](#couchbasemigrationreplications-spec-collectionsosomode)couchbasemigrationreplications.spec.collectionsOSOMode

#### [](#constraints-17)Constraints

**Type**: `boolean`

#### [](#description-17)Description

CollectionsOSOMode optimizes for out-of-order mutations streaming (performance toggle). This field defaults to true.

### [](#couchbasemigrationreplications-spec-compressiontype)couchbasemigrationreplications.spec.compressionType

#### [](#constraints-18)Constraints

**Type**: `string`

**Enumerations**: `Auto, None`

#### [](#description-18)Description

CompressionType is the compression used for XDCR traffic.

### [](#couchbasemigrationreplications-spec-conflictlogging)couchbasemigrationreplications.spec.conflictLogging

#### [](#constraints-19)Constraints

**Type**: `object`

#### [](#description-19)Description

ConflictLogging is the configuration for conflict logging. This feature is available in Couchbase Server 8.0.0 and later.

### [](#couchbasemigrationreplications-spec-conflictlogging-enabled)couchbasemigrationreplications.spec.conflictLogging.enabled

#### [](#constraints-20)Constraints

**Type**: `boolean`

#### [](#description-20)Description

Enabled defines whether conflict logging is enabled.

### [](#couchbasemigrationreplications-spec-conflictlogging-logcollection)couchbasemigrationreplications.spec.conflictLogging.logCollection

#### [](#constraints-21)Constraints

**Type**: `object`

#### [](#description-21)Description

LogCollection defines the collection to log conflicts to.

### [](#couchbasemigrationreplications-spec-conflictlogging-logcollection-bucket)couchbasemigrationreplications.spec.conflictLogging.logCollection.bucket

#### [](#constraints-22)Constraints

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-22)Description

Bucket defines the bucket to log conflicts to.

### [](#couchbasemigrationreplications-spec-conflictlogging-logcollection-collection)couchbasemigrationreplications.spec.conflictLogging.logCollection.collection

#### [](#constraints-23)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-23)Description

Collection defines the collection to log conflicts to.

### [](#couchbasemigrationreplications-spec-conflictlogging-logcollection-scope)couchbasemigrationreplications.spec.conflictLogging.logCollection.scope

#### [](#constraints-24)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-24)Description

Scope defines the scope to log conflicts to.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules)couchbasemigrationreplications.spec.conflictLogging.loggingRules

#### [](#constraints-25)Constraints

**Type**: `object`

#### [](#description-25)Description

LoggingRules defines the list of logging rules for conflict logging. The rules can be scoped to a specific scope or a specific collection in a scope. The rules can disable logging, log to the default collection defined at `spec.conflictLogging.logCollection`, or log to a different collection.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-customcollectionrules)couchbasemigrationreplications.spec.conflictLogging.loggingRules.customCollectionRules

#### [](#constraints-26)Constraints

**Type**: `[]object`

#### [](#description-26)Description

CustomCollectionRules defines the rules for logging to a different collection.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-customcollectionrules-collection)couchbasemigrationreplications.spec.conflictLogging.loggingRules.customCollectionRules.collection

#### [](#constraints-27)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-27)Description

Collection defines the collection to apply the rule to.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-customcollectionrules-logcollection)couchbasemigrationreplications.spec.conflictLogging.loggingRules.customCollectionRules.logCollection

#### [](#constraints-28)Constraints

**Required**

**Type**: `object`

#### [](#description-28)Description

LogCollection defines the collection to log conflicts to.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-customcollectionrules-logcollection-bucket)couchbasemigrationreplications.spec.conflictLogging.loggingRules.customCollectionRules.logCollection.bucket

#### [](#constraints-29)Constraints

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-29)Description

Bucket defines the bucket to log conflicts to.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-customcollectionrules-logcollection-collection)couchbasemigrationreplications.spec.conflictLogging.loggingRules.customCollectionRules.logCollection.collection

#### [](#constraints-30)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-30)Description

Collection defines the collection to log conflicts to.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-customcollectionrules-logcollection-scope)couchbasemigrationreplications.spec.conflictLogging.loggingRules.customCollectionRules.logCollection.scope

#### [](#constraints-31)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-31)Description

Scope defines the scope to log conflicts to.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-customcollectionrules-scope)couchbasemigrationreplications.spec.conflictLogging.loggingRules.customCollectionRules.scope

#### [](#constraints-32)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-32)Description

Scope defines the scope to apply the rule to.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-defaultcollectionrules)couchbasemigrationreplications.spec.conflictLogging.loggingRules.defaultCollectionRules

#### [](#constraints-33)Constraints

**Type**: `[]object`

#### [](#description-33)Description

DefaultCollectionRules defines the rules for logging to the default collection.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-defaultcollectionrules-collection)couchbasemigrationreplications.spec.conflictLogging.loggingRules.defaultCollectionRules.collection

#### [](#constraints-34)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-34)Description

Collection defines the collection to apply the rule to.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-defaultcollectionrules-scope)couchbasemigrationreplications.spec.conflictLogging.loggingRules.defaultCollectionRules.scope

#### [](#constraints-35)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-35)Description

Scope defines the scope to apply the rule to.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-nologgingrules)couchbasemigrationreplications.spec.conflictLogging.loggingRules.noLoggingRules

#### [](#constraints-36)Constraints

**Type**: `[]object`

#### [](#description-36)Description

NoLoggingRules defines the rules for disabling logging to for conflicts in a specific scope or collection.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-nologgingrules-collection)couchbasemigrationreplications.spec.conflictLogging.loggingRules.noLoggingRules.collection

#### [](#constraints-37)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-37)Description

Collection defines the collection to apply the rule to.

### [](#couchbasemigrationreplications-spec-conflictlogging-loggingrules-nologgingrules-scope)couchbasemigrationreplications.spec.conflictLogging.loggingRules.noLoggingRules.scope

#### [](#constraints-38)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-38)Description

Scope defines the scope to apply the rule to.

### [](#couchbasemigrationreplications-spec-desiredlatency)couchbasemigrationreplications.spec.desiredLatency

#### [](#constraints-39)Constraints

**Type**: `integer`

#### [](#description-39)Description

DesiredLatency is the target latency (ms) for high-priority replications. This field defaults to 50.

### [](#couchbasemigrationreplications-spec-docbatchsizekb)couchbasemigrationreplications.spec.docBatchSizeKb

#### [](#constraints-40)Constraints

**Type**: `integer`

**Minimum**: `10`

**Maximum**: `10000`

#### [](#description-40)Description

DocBatchSizeKb is the size (KB) of document batches sent.

### [](#couchbasemigrationreplications-spec-failurerestartinterval)couchbasemigrationreplications.spec.failureRestartInterval

#### [](#constraints-41)Constraints

**Type**: `integer`

**Minimum**: `1`

**Maximum**: `300`

#### [](#description-41)Description

FailureRestartInterval is the seconds to wait before restarting after a failure.

### [](#couchbasemigrationreplications-spec-filterbinary)couchbasemigrationreplications.spec.filterBinary

#### [](#constraints-42)Constraints

**Type**: `boolean`

#### [](#description-42)Description

FilterBinary specifies whether binary documents should be replicated. The value can be true or false (the default). If the value is true, binary documents are not replicated, regardless of whether a filterExpression is applied. If the value is false: The behavior is identical to that of all Couchbase-Server versions prior to 7.2.1 (with the exception of 7.1.5), where the filterBinary flag did not exist. If a filter expression is not provided, binary documents are replicated. If a filter expression is provided, and the expression refers only to either the document’s key, or its xattr, or to both, the expression is applied, and the document is replicated if the expression permits. If a filter expression is provided, and the expression refers only to the document’s body, the document is replicated. If a filter expression is provided, and the expression refers to the document’s key, or its xattr, or to both; and also refers to the document’s body; the document is not replicated (regardless of whether the key or xattr might appear to permit replication).

### [](#couchbasemigrationreplications-spec-filterbypassexpiry)couchbasemigrationreplications.spec.filterBypassExpiry

#### [](#constraints-43)Constraints

**Type**: `boolean`

#### [](#description-43)Description

FilterBypassExpiry when true, TTL is removed before replication.

### [](#couchbasemigrationreplications-spec-filterbypassuncommittedtxn)couchbasemigrationreplications.spec.filterBypassUncommittedTxn

#### [](#constraints-44)Constraints

**Type**: `boolean`

#### [](#description-44)Description

FilterBypassUncommittedTxn when true, documents with uncommitted txn xattrs are not replicated.

### [](#couchbasemigrationreplications-spec-filterdeletion)couchbasemigrationreplications.spec.filterDeletion

#### [](#constraints-45)Constraints

**Type**: `boolean`

#### [](#description-45)Description

FilterDeletion when true, delete mutations are filtered out (not replicated).

### [](#couchbasemigrationreplications-spec-filterexpiration)couchbasemigrationreplications.spec.filterExpiration

#### [](#constraints-46)Constraints

**Type**: `boolean`

#### [](#description-46)Description

FilterExpiration when true, expiry mutations are filtered out.

### [](#couchbasemigrationreplications-spec-filterexpression)couchbasemigrationreplications.spec.filterExpression

#### [](#constraints-47)Constraints

**Type**: `string`

#### [](#description-47)Description

FilterExpression is a filter expression to match against documents in the source bucket. Each document that produces a successful match is replicated.

### [](#couchbasemigrationreplications-spec-filterskiprestream)couchbasemigrationreplications.spec.filterSkipRestream

#### [](#constraints-48)Constraints

**Type**: `boolean`

#### [](#description-48)Description

FilterSkipRestream controls whether replication restarts after filterExpression changes. When false (default), replication restarts after filter changes. When true, continues without restart. Note: Server requires this field when filterExpression is set. If not specified, operator defaults to false.

### [](#couchbasemigrationreplications-spec-hlvpruningwindowsec)couchbasemigrationreplications.spec.hlvPruningWindowSec

#### [](#constraints-49)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-49)Description

HlvPruningWindowSec is the HLV pruning window (sec) for hybrid logical vector conflict resolution.

### [](#couchbasemigrationreplications-spec-jsfunctiontimeoutms)couchbasemigrationreplications.spec.jsFunctionTimeoutMs

#### [](#constraints-50)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-50)Description

JSFunctionTimeoutMs is the timeout for JS custom conflict-resolution functions (ms).

### [](#couchbasemigrationreplications-spec-loglevel)couchbasemigrationreplications.spec.logLevel

#### [](#constraints-51)Constraints

**Type**: `string`

**Enumerations**: `Error, Info, Debug, Trace`

#### [](#description-51)Description

LogLevel is the logging verbosity for XDCR.

### [](#couchbasemigrationreplications-spec-mergefunctionmapping)couchbasemigrationreplications.spec.mergeFunctionMapping

#### [](#constraints-52)Constraints

**Type**: `map[string]string`

#### [](#description-52)Description

MergeFunctionMapping maps collection specifiers (scope.collection) to merge function names for custom conflict resolution. Nil values can be used to explicitly unset merge functions for specific collections.

### [](#couchbasemigrationreplications-spec-mobile)couchbasemigrationreplications.spec.mobile

#### [](#constraints-53)Constraints

**Type**: `string`

**Enumerations**: `Off, Active`

#### [](#description-53)Description

Mobile enables mobile (Sync Gateway) active-active mode. This feature is available in Couchbase Server 7.6.4 and later.

### [](#couchbasemigrationreplications-spec-networkusagelimit)couchbasemigrationreplications.spec.networkUsageLimit

#### [](#constraints-54)Constraints

**Type**: `integer`

**Minimum**: `0`

#### [](#description-54)Description

NetworkUsageLimit is the upper limit for replication network usage (MB/s).

### [](#couchbasemigrationreplications-spec-optimisticreplicationthreshold)couchbasemigrationreplications.spec.optimisticReplicationThreshold

#### [](#constraints-55)Constraints

**Type**: `integer`

**Minimum**: `0`

**Maximum**: `20971520`

#### [](#description-55)Description

OptimisticReplicationThreshold is the size threshold below which documents replicate optimistically.

### [](#couchbasemigrationreplications-spec-paused)couchbasemigrationreplications.spec.paused

#### [](#constraints-56)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-56)Description

PauseRequested indicates whether the replication has been issued a pause request.

### [](#couchbasemigrationreplications-spec-priority)couchbasemigrationreplications.spec.priority

#### [](#constraints-57)Constraints

**Type**: `string`

**Enumerations**: `High, Medium, Low`

#### [](#description-57)Description

Priority is the resource priority for replication streams.

### [](#couchbasemigrationreplications-spec-remotebucket)couchbasemigrationreplications.spec.remoteBucket

#### [](#constraints-58)Constraints

**Required**

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-58)Description

RemoteBucket is the remote bucket name to synchronize to. This refers to the Couchbase bucket name, not the resource name of the bucket. Legal bucket names have a maximum length of 100 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "-\_%\\.".

### [](#couchbasemigrationreplications-spec-retryonremoteautherr)couchbasemigrationreplications.spec.retryOnRemoteAuthErr

#### [](#constraints-59)Constraints

**Type**: `boolean`

#### [](#description-59)Description

RetryOnRemoteAuthErr defines whether to retry connections when remote auth fails.

### [](#couchbasemigrationreplications-spec-retryonremoteautherrmaxwaitsec)couchbasemigrationreplications.spec.retryOnRemoteAuthErrMaxWaitSec

#### [](#constraints-60)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-60)Description

RetryOnRemoteAuthErrMaxWaitSec is the max wait seconds for retrying remote auth failures. Only effective if retryOnRemoteAuthErr is true.

### [](#couchbasemigrationreplications-spec-sourcenozzlepernode)couchbasemigrationreplications.spec.sourceNozzlePerNode

#### [](#constraints-61)Constraints

**Type**: `integer`

**Minimum**: `1`

**Maximum**: `100`

#### [](#description-61)Description

SourceNozzlePerNode is the number of source nozzles (parallelism) per source node.

### [](#couchbasemigrationreplications-spec-statsinterval)couchbasemigrationreplications.spec.statsInterval

#### [](#constraints-62)Constraints

**Type**: `integer`

**Minimum**: `200`

**Maximum**: `600000`

#### [](#description-62)Description

StatsInterval is the interval for statistics updates (ms).

### [](#couchbasemigrationreplications-spec-targetnozzlepernode)couchbasemigrationreplications.spec.targetNozzlePerNode

#### [](#constraints-63)Constraints

**Type**: `integer`

**Minimum**: `1`

**Maximum**: `100`

#### [](#description-63)Description

TargetNozzlePerNode is the number of target nozzles per target node (parallelism).

### [](#couchbasemigrationreplications-spec-workerbatchsize)couchbasemigrationreplications.spec.workerBatchSize

#### [](#constraints-64)Constraints

**Type**: `integer`

**Minimum**: `500`

**Maximum**: `10000`

#### [](#description-64)Description

WorkerBatchSize is the number of mutations per worker batch.