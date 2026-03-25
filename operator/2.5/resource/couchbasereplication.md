---
title: CouchbaseReplication Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.5.x/docs/user/modules/ROOT/pages/resource/couchbasereplication.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.5@operator::resource/couchbasereplication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/resource/couchbasereplication.html)

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
  compressionType: Auto
  filterExpression: ""
  paused: false
  remoteBucket: ""
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

### [](#couchbasereplications-spec-compressiontype)couchbasereplications.spec.compressionType

#### [](#constraints-22)Constraints

**Type**: `string`

**Default**: `Auto`

**Enumerations**: `None, Auto`

#### [](#description-22)Description

CompressionType is the type of compression to apply to the replication. When None, no compression will be applied to documents as they are transferred between clusters. When Auto, Couchbase server will automatically compress documents as they are transferred to reduce bandwidth requirements. This field must be one of "None" or "Auto", defaulting to "Auto".

### [](#couchbasereplications-spec-filterexpression)couchbasereplications.spec.filterExpression

#### [](#constraints-23)Constraints

**Type**: `string`

#### [](#description-23)Description

FilterExpression allows certain documents to be filtered out of the replication.

### [](#couchbasereplications-spec-paused)couchbasereplications.spec.paused

#### [](#constraints-24)Constraints

**Type**: `boolean`

#### [](#description-24)Description

Paused allows a replication to be stopped and restarted without having to restart the replication from the beginning.

### [](#couchbasereplications-spec-remotebucket)couchbasereplications.spec.remoteBucket

#### [](#constraints-25)Constraints

**Required**

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-25)Description

RemoteBucket is the remote bucket name to synchronize to. This refers to the Couchbase bucket name, not the resource name of the bucket. Legal bucket names have a maximum length of 100 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "-\_%\\.".