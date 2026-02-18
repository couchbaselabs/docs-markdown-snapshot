---
title: CouchbaseRoleBinding Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.8.x/docs/user/modules/ROOT/pages/resource/couchbaserolebinding.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/operator/2.8/resource/couchbaserolebinding.html)

# CouchbaseRoleBinding Resource

CouchbaseRoleBinding allows association of Couchbase users with groups.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseRoleBinding
metadata:
  name: ""
spec:
  roleRef:
    kind: ""
    name: ""
  subjects:
  - kind: ""
    name: ""
```

## [](#couchbaserolebindings-apiversion)couchbaserolebindings.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbaserolebindings-kind)couchbaserolebindings.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbaserolebindings-metadata)couchbaserolebindings.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbaserolebindings-metadata-name)couchbaserolebindings.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbaserolebindings-metadata-namespace)couchbaserolebindings.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbaserolebindings-metadata-labels)couchbaserolebindings.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbaserolebindings-metadata-annotations)couchbaserolebindings.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbaserolebindings-spec)couchbaserolebindings.spec

### [](#constraints-8)Constraints

**Required**

**Type**: `object`

### [](#description-8)Description

CouchbaseRoleBindingSpec defines the group of subjects i.e. users, and the role i.e. group they are a member of.

### [](#couchbaserolebindings-spec-roleref)couchbaserolebindings.spec.roleRef

#### [](#constraints-9)Constraints

**Required**

**Type**: `object`

#### [](#description-9)Description

CouchbaseGroup being bound to subjects.

### [](#couchbaserolebindings-spec-roleref-kind)couchbaserolebindings.spec.roleRef.kind

#### [](#constraints-10)Constraints

**Required**

**Type**: `string`

**Enumerations**: `CouchbaseGroup`

#### [](#description-10)Description

Kind of role to use for binding.

### [](#couchbaserolebindings-spec-roleref-name)couchbaserolebindings.spec.roleRef.name

#### [](#constraints-11)Constraints

**Required**

**Type**: `string`

#### [](#description-11)Description

Name of role resource to use for binding.

### [](#couchbaserolebindings-spec-subjects)couchbaserolebindings.spec.subjects

#### [](#constraints-12)Constraints

**Required**

**Type**: `[]object`

#### [](#description-12)Description

List of users to bind a role to.

### [](#couchbaserolebindings-spec-subjects-kind)couchbaserolebindings.spec.subjects.kind

#### [](#constraints-13)Constraints

**Required**

**Type**: `string`

**Enumerations**: `CouchbaseUser`

#### [](#description-13)Description

Couchbase user/group kind.

### [](#couchbaserolebindings-spec-subjects-name)couchbaserolebindings.spec.subjects.name

#### [](#constraints-14)Constraints

**Required**

**Type**: `string`

#### [](#description-14)Description

Name of Couchbase user resource.