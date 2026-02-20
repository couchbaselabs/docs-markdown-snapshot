---
title: CouchbaseCollectionGroup Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.7.x/docs/user/modules/ROOT/pages/resource/couchbasecollectiongroup.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.7@operator::resource/couchbasecollectiongroup.adoc[]
---

[View original HTML](/operator/2.7/resource/couchbasecollectiongroup.html)

# CouchbaseCollectionGroup Resource

CouchbaseCollectionGroup represent the finest grained size of data storage in Couchbase. Collections contain all documents and indexes in the system. Collections also form the finest grain basis for role-based access control (RBAC) and cross-datacenter replication (XDCR). In order to be considered by the Operator, every collection group must be referenced by a `CouchbaseScope` or `CouchbaseScopeGroup` resource. Unlike the CouchbaseCollection resource, a collection group represents multiple collections, with common configuration parameters, to be expressed as a single resource, minimizing required configuration and Kubernetes API traffic. It also forms the basis of Couchbase RBAC security boundaries.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseCollectionGroup
metadata:
  name: ""
spec:
  maxTTL: ""
  names:
  - ""
```

## [](#couchbasecollectiongroups-apiversion)couchbasecollectiongroups.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbasecollectiongroups-kind)couchbasecollectiongroups.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbasecollectiongroups-metadata)couchbasecollectiongroups.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbasecollectiongroups-metadata-name)couchbasecollectiongroups.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbasecollectiongroups-metadata-namespace)couchbasecollectiongroups.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbasecollectiongroups-metadata-labels)couchbasecollectiongroups.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbasecollectiongroups-metadata-annotations)couchbasecollectiongroups.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbasecollectiongroups-spec)couchbasecollectiongroups.spec

### [](#constraints-8)Constraints

**Required**

**Type**: `object`

### [](#description-8)Description

Spec defines the desired state of the resource.

### [](#couchbasecollectiongroups-spec-maxttl)couchbasecollectiongroups.spec.maxTTL

#### [](#constraints-9)Constraints

**Type**: `string`

#### [](#description-9)Description

MaxTTL defines how long a document is permitted to exist for, without modification, until it is automatically deleted. This field takes precedence over any TTL defined at the bucket level. This is a default, and maximum time-to-live and may be set to a lower value by the client. If the client specifies a higher value, then it is truncated to the maximum durability. Documents are removed by Couchbase, after they have expired, when either accessed, the expiry pager is run, or the bucket is compacted. When set to 0, then documents are not expired by default. This field must be a duration in the range 0-2147483648s, defaulting to 0\. While this field can be changed on the CRD, it will not be updated on the collection if the Couchbase Server version is pre 7.6.0\. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbasecollectiongroups-spec-names)couchbasecollectiongroups.spec.names

#### [](#constraints-10)Constraints

**Required**

**Type**: `[]string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250}$`

#### [](#description-10)Description

Names specifies the names of the collections. Unlike CouchbaseCollection, which specifies a single collection, a collection group specifies multiple, and the collection group must specify at least one collection name. Any collection names specified must be unique. Collection names must be 1-251 characters in length, contain only \[a-zA-Z0-9\_-%\] and not start with either \_ or %.