---
title: CouchbaseScope Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.6.x/docs/user/modules/ROOT/pages/resource/couchbasescope.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.6@operator::resource/couchbasescope.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/resource/couchbasescope.html)

# CouchbaseScope Resource

CouchbaseScope represents a logical unit of data storage that sits between buckets and collections e.g. a bucket may contain multiple scopes, and a scope may contain multiple collections. At present, scopes are not nested, so provide only a single level of abstraction. Scopes provide a coarser grained basis for role-based access control (RBAC) and cross-datacenter replication (XDCR) than collections, but finer that buckets. In order to be considered by the Operator, a scope must be referenced by either a `CouchbaseBucket` or `CouchbaseEphemeralBucket` resource.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseScope
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
  defaultScope: false
  name: ""
```

## [](#couchbasescopes-apiversion)couchbasescopes.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbasescopes-kind)couchbasescopes.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbasescopes-metadata)couchbasescopes.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbasescopes-metadata-name)couchbasescopes.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbasescopes-metadata-namespace)couchbasescopes.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbasescopes-metadata-labels)couchbasescopes.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbasescopes-metadata-annotations)couchbasescopes.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbasescopes-spec)couchbasescopes.spec

### [](#constraints-8)Constraints

**Type**: `object`

**Default**: `{}`

### [](#description-8)Description

Spec defines the desired state of the resource.

### [](#couchbasescopes-spec-collections)couchbasescopes.spec.collections

#### [](#constraints-9)Constraints

**Type**: `object`

#### [](#description-9)Description

Collections defines how to collate collections included in this scope or scope group. Any of the provided methods may be used to collate a set of collections to manage. Collated collections must have unique names, otherwise it is considered ambiguous, and an error condition.

### [](#couchbasescopes-spec-collections-managed)couchbasescopes.spec.collections.managed

#### [](#constraints-10)Constraints

**Type**: `boolean`

#### [](#description-10)Description

Managed indicates whether collections within this scope are managed. If not then you can dynamically create and delete collections with the Couchbase UI or SDKs.

### [](#couchbasescopes-spec-collections-preservedefaultcollection)couchbasescopes.spec.collections.preserveDefaultCollection

#### [](#constraints-11)Constraints

**Type**: `boolean`

#### [](#description-11)Description

PreserveDefaultCollection indicates whether the Operator should manage the default collection within the default scope. The default collection can be deleted, but can not be recreated by Couchbase Server. By setting this field to `true`, the Operator will implicitly manage the default collection within the default scope. The default collection cannot be modified and will have no document time-to-live (TTL). When set to `false`, the operator will not manage the default collection, which will be deleted and cannot be used or recreated.

### [](#couchbasescopes-spec-collections-resources)couchbasescopes.spec.collections.resources

#### [](#constraints-12)Constraints

**Type**: `[]object`

#### [](#description-12)Description

Resources is an explicit list of named resources that will be considered for inclusion in this scope or scopes. If a resource reference doesn't match a resource, then no error conditions are raised due to undefined resource creation ordering and eventual consistency.

### [](#couchbasescopes-spec-collections-resources-kind)couchbasescopes.spec.collections.resources.kind

#### [](#constraints-13)Constraints

**Type**: `string`

**Default**: `CouchbaseCollection`

**Enumerations**: `CouchbaseCollection, CouchbaseCollectionGroup`

#### [](#description-13)Description

Kind indicates the kind of resource that is being referenced. A scope can only reference `CouchbaseCollection` and `CouchbaseCollectionGroup` resource kinds. This field defaults to `CouchbaseCollection` if not specified.

### [](#couchbasescopes-spec-collections-resources-name)couchbasescopes.spec.collections.resources.name

#### [](#constraints-14)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250}$`

#### [](#description-14)Description

Name is the name of the Kubernetes resource name that is being referenced. Legal collection names have a maximum length of 251 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "\_-%".

### [](#couchbasescopes-spec-collections-selector)couchbasescopes.spec.collections.selector

#### [](#constraints-15)Constraints

**Type**: `object`

#### [](#description-15)Description

Selector allows resources to be implicitly considered for inclusion in this scope or scopes. More info: <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#labelselector-v1-meta>.

### [](#couchbasescopes-spec-defaultscope)couchbasescopes.spec.defaultScope

#### [](#constraints-16)Constraints

**Type**: `boolean`

#### [](#description-16)Description

DefaultScope indicates whether this resource represents the default scope for a bucket. When set to `true`, this allows the user to refer to and manage collections within the default scope. When not defined, the Operator will implicitly manage the default scope as the default scope can not be deleted from Couchbase Server. The Operator defined default scope will also have the `persistDefaultCollection` flag set to `true`. Only one default scope is permitted to be contained in a bucket.

### [](#couchbasescopes-spec-name)couchbasescopes.spec.name

#### [](#constraints-17)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250}$`

#### [](#description-17)Description

Name specifies the name of the scope. By default, the metadata.name is used to define the scope name, however, due to the limited character set, this field can be used to override the default and provide the full functionality. Additionally the `metadata.name` field is a DNS label, and thus limited to 63 characters, this field must be used if the name is longer than this limit. Scope names must be 1-251 characters in length, contain only \[a-zA-Z0-9\_-%\] and not start with either \_ or %.