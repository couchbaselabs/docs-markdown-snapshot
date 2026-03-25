---
title: CouchbaseMigrationReplication Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.6.x/docs/user/modules/ROOT/pages/resource/couchbasemigrationreplication.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.6@operator::resource/couchbasemigrationreplication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/resource/couchbasemigrationreplication.html)

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
  compressionType: Auto
  filterExpression: ""
  paused: false
  remoteBucket: ""
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

### [](#couchbasemigrationreplications-spec-compressiontype)couchbasemigrationreplications.spec.compressionType

#### [](#constraints-16)Constraints

**Type**: `string`

**Default**: `Auto`

**Enumerations**: `None, Auto`

#### [](#description-16)Description

CompressionType is the type of compression to apply to the replication. When None, no compression will be applied to documents as they are transferred between clusters. When Auto, Couchbase server will automatically compress documents as they are transferred to reduce bandwidth requirements. This field must be one of "None" or "Auto", defaulting to "Auto".

### [](#couchbasemigrationreplications-spec-filterexpression)couchbasemigrationreplications.spec.filterExpression

#### [](#constraints-17)Constraints

**Type**: `string`

#### [](#description-17)Description

FilterExpression allows certain documents to be filtered out of the replication.

### [](#couchbasemigrationreplications-spec-paused)couchbasemigrationreplications.spec.paused

#### [](#constraints-18)Constraints

**Type**: `boolean`

#### [](#description-18)Description

Paused allows a replication to be stopped and restarted without having to restart the replication from the beginning.

### [](#couchbasemigrationreplications-spec-remotebucket)couchbasemigrationreplications.spec.remoteBucket

#### [](#constraints-19)Constraints

**Required**

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-19)Description

RemoteBucket is the remote bucket name to synchronize to. This refers to the Couchbase bucket name, not the resource name of the bucket. Legal bucket names have a maximum length of 100 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "-\_%\\.".