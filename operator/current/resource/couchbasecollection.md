---
title: CouchbaseCollection Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.9.x/docs/user/modules/ROOT/pages/resource/couchbasecollection.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:operator::resource/couchbasecollection.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/resource/couchbasecollection.html)

# CouchbaseCollection Resource

CouchbaseCollection represent the finest grained size of data storage in Couchbase. Collections contain all documents and indexes in the system. Collections also form the finest grain basis for role-based access control (RBAC) and cross-datacenter replication (XDCR). In order to be considered by the Operator, every collection must be referenced by a `CouchbaseScope` or `CouchbaseScopeGroup` resource.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseCollection
metadata:
  name: ""
spec:
  history: false
  maxTTL: ""
  name: ""
```

## [](#couchbasecollections-apiversion)couchbasecollections.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbasecollections-kind)couchbasecollections.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbasecollections-metadata)couchbasecollections.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbasecollections-metadata-name)couchbasecollections.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbasecollections-metadata-namespace)couchbasecollections.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbasecollections-metadata-labels)couchbasecollections.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbasecollections-metadata-annotations)couchbasecollections.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbasecollections-spec)couchbasecollections.spec

### [](#constraints-8)Constraints

**Type**: `object`

**Default**: `{}`

### [](#description-8)Description

Spec defines the desired state of the resource.

### [](#couchbasecollections-spec-history)couchbasecollections.spec.history

#### [](#constraints-9)Constraints

**Type**: `boolean`

#### [](#description-9)Description

History defines whether change history is retained for the collection. If this field is set, it will override the historyRetention.collectionDefault bucket level value. This is only supported with storageBackend=magma at the bucket level.

### [](#couchbasecollections-spec-maxttl)couchbasecollections.spec.maxTTL

#### [](#constraints-10)Constraints

**Type**: `string`

#### [](#description-10)Description

MaxTTL defines how long a document is permitted to exist for, without modification, until it is automatically deleted. This field takes precedence over any TTL defined at the bucket level. This is a default, and maximum time-to-live and may be set to a lower value by the client. If the client specifies a higher value, then it is truncated to the maximum durability. Documents are removed by Couchbase, after they have expired, when either accessed, the expiry pager is run, or the bucket is compacted. When set to 0, then documents are not expired by default. This field must either be a duration in the range 0-2147483648s or "-1", defaulting to 0\. If set to "-1", the collection's bucket will be prevented from setting a default expiration on the collection's documents. While this field can be changed on the CRD, it will not be updated on the collection if the Couchbase Server version is pre 7.6.0\. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbasecollections-spec-name)couchbasecollections.spec.name

#### [](#constraints-11)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250}$`

#### [](#description-11)Description

Name specifies the name of the collection. By default, the metadata.name is used to define the collection name, however, due to the limited character set, this field can be used to override the default and provide the full functionality. Additionally the `metadata.name` field is a DNS label, and thus limited to 63 characters, this field must be used if the name is longer than this limit. Collection names must be 1-251 characters in length, contain only \[a-zA-Z0-9\_-%\] and not start with either \_ or %.