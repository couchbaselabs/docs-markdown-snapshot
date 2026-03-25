---
title: CouchbaseScopeGroup Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.5.x/docs/user/modules/ROOT/pages/resource/couchbasescopegroup.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.5@operator::resource/couchbasescopegroup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/resource/couchbasescopegroup.html)

# CouchbaseScopeGroup Resource

CouchbaseScopeGroup represents a logical unit of data storage that sits between buckets and collections e.g. a bucket may contain multiple scopes, and a scope may contain multiple collections. At present, scopes are not nested, so provide only a single level of abstraction. Scopes provide a coarser grained basis for role-based access control (RBAC) and cross-datacenter replication (XDCR) than collections, but finer that buckets. In order to be considered by the Operator, a scope must be referenced by either a `CouchbaseBucket` or `CouchbaseEphemeralBucket` resource. Unlike `CouchbaseScope` resources, scope groups represents multiple scopes, with the same common set of collections, to be expressed as a single resource, minimizing required configuration and Kubernetes API traffic. It also forms the basis of Couchbase RBAC security boundaries.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseScopeGroup
metadata:
  name: ""
spec:
  collections:
    managed: false
    preserveDefaultCollection: false
    resources:
    - kind: CouchbaseCollection
      name: ""
    selector: {}
  names:
  - ""
```

## [](#couchbasescopegroups-apiversion)couchbasescopegroups.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbasescopegroups-kind)couchbasescopegroups.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbasescopegroups-metadata)couchbasescopegroups.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbasescopegroups-metadata-name)couchbasescopegroups.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbasescopegroups-metadata-namespace)couchbasescopegroups.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbasescopegroups-metadata-labels)couchbasescopegroups.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbasescopegroups-metadata-annotations)couchbasescopegroups.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbasescopegroups-spec)couchbasescopegroups.spec

### [](#constraints-8)Constraints

**Required**

**Type**: `object`

### [](#description-8)Description

Spec defines the desired state of the resource.

### [](#couchbasescopegroups-spec-collections)couchbasescopegroups.spec.collections

#### [](#constraints-9)Constraints

**Type**: `object`

#### [](#description-9)Description

Collections defines how to collate collections included in this scope or scope group. Any of the provided methods may be used to collate a set of collections to manage. Collated collections must have unique names, otherwise it is considered ambiguous, and an error condition.

### [](#couchbasescopegroups-spec-collections-managed)couchbasescopegroups.spec.collections.managed

#### [](#constraints-10)Constraints

**Type**: `boolean`

#### [](#description-10)Description

Managed indicates whether collections within this scope are managed. If not then you can dynamically create and delete collections with the Couchbase UI or SDKs.

### [](#couchbasescopegroups-spec-collections-preservedefaultcollection)couchbasescopegroups.spec.collections.preserveDefaultCollection

#### [](#constraints-11)Constraints

**Type**: `boolean`

#### [](#description-11)Description

PreserveDefaultCollection indicates whether the Operator should manage the default collection within the default scope. The default collection can be deleted, but can not be recreated by Couchbase Server. By setting this field to `true`, the Operator will implicitly manage the default collection within the default scope. The default collection cannot be modified and will have no document time-to-live (TTL). When set to `false`, the operator will not manage the default collection, which will be deleted and cannot be used or recreated.

### [](#couchbasescopegroups-spec-collections-resources)couchbasescopegroups.spec.collections.resources

#### [](#constraints-12)Constraints

**Type**: `[]object`

#### [](#description-12)Description

Resources is an explicit list of named resources that will be considered for inclusion in this scope or scopes. If a resource reference doesn’t match a resource, then no error conditions are raised due to undefined resource creation ordering and eventual consistency.

### [](#couchbasescopegroups-spec-collections-resources-kind)couchbasescopegroups.spec.collections.resources.kind

#### [](#constraints-13)Constraints

**Type**: `string`

**Default**: `CouchbaseCollection`

**Enumerations**: `CouchbaseCollection, CouchbaseCollectionGroup`

#### [](#description-13)Description

Kind indicates the kind of resource that is being referenced. A scope can only reference `CouchbaseCollection` and `CouchbaseCollectionGroup` resource kinds. This field defaults to `CouchbaseCollection` if not specified.

### [](#couchbasescopegroups-spec-collections-resources-name)couchbasescopegroups.spec.collections.resources.name

#### [](#constraints-14)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250}$`

#### [](#description-14)Description

Name is the name of the Kubernetes resource name that is being referenced. Legal collection names have a maximum length of 251 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "\_-%".

### [](#couchbasescopegroups-spec-collections-selector)couchbasescopegroups.spec.collections.selector

#### [](#constraints-15)Constraints

**Type**: `object`

#### [](#description-15)Description

Selector allows resources to be implicitly considered for inclusion in this scope or scopes. More info: <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#labelselector-v1-meta>.

### [](#couchbasescopegroups-spec-names)couchbasescopegroups.spec.names

#### [](#constraints-16)Constraints

**Required**

**Type**: `[]string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250}$`

#### [](#description-16)Description

Names specifies the names of the scopes. Unlike CouchbaseScope, which specifies a single scope, a scope group specifies multiple, and the scope group must specify at least one scope name. Any scope names specified must be unique. Scope names must be 1-251 characters in length, contain only \[a-zA-Z0-9\_-%\] and not start with either \_ or %.