---
title: CouchbaseMemcachedBucket Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.6.x/docs/user/modules/ROOT/pages/resource/couchbasememcachedbucket.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.6@operator::resource/couchbasememcachedbucket.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/resource/couchbasememcachedbucket.html)

# CouchbaseMemcachedBucket Resource

The CouchbaseMemcachedBucket resource defines a set of documents in Couchbase server. A Couchbase client connects to and operates on a bucket, which provides independent management of a set documents and a security boundary for role based access control. A CouchbaseEphemeralBucket provides in-memory only storage for documents contained by it.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseMemcachedBucket
metadata:
  name: ""
spec:
  enableFlush: false
  memoryQuota: 100Mi
  name: ""
```

## [](#couchbasememcachedbuckets-apiversion)couchbasememcachedbuckets.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbasememcachedbuckets-kind)couchbasememcachedbuckets.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbasememcachedbuckets-metadata)couchbasememcachedbuckets.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbasememcachedbuckets-metadata-name)couchbasememcachedbuckets.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbasememcachedbuckets-metadata-namespace)couchbasememcachedbuckets.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbasememcachedbuckets-metadata-labels)couchbasememcachedbuckets.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbasememcachedbuckets-metadata-annotations)couchbasememcachedbuckets.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbasememcachedbuckets-spec)couchbasememcachedbuckets.spec

### [](#constraints-8)Constraints

**Type**: `object`

**Default**: `{}`

### [](#description-8)Description

CouchbaseMemcachedBucketSpec is the specification for a Memcached bucket resource, and allows the bucket to be customized.

### [](#couchbasememcachedbuckets-spec-enableflush)couchbasememcachedbuckets.spec.enableFlush

#### [](#constraints-9)Constraints

**Type**: `boolean`

#### [](#description-9)Description

EnableFlush defines whether a client can delete all documents in a bucket. This field defaults to false.

### [](#couchbasememcachedbuckets-spec-memoryquota)couchbasememcachedbuckets.spec.memoryQuota

#### [](#constraints-10)Constraints

**Type**: `string`

**Default**: `100Mi`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-10)Description

MemoryQuota is a memory limit to the size of a bucket. The memory quota is defined per Couchbase pod running the data service. This field defaults to, and must be greater than or equal to 100Mi. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbasememcachedbuckets-spec-name)couchbasememcachedbuckets.spec.name

#### [](#constraints-11)Constraints

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-11)Description

Name is the name of the bucket within Couchbase server. By default the Operator will use the `metadata.name` field to define the bucket name. The `metadata.name` field only supports a subset of the supported character set. When specified, this field overrides `metadata.name`. Legal bucket names have a maximum length of 100 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "-\_%\\.".