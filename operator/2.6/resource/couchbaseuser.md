---
title: CouchbaseUser Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.6.x/docs/user/modules/ROOT/pages/resource/couchbaseuser.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.6@operator::resource/couchbaseuser.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/resource/couchbaseuser.html)

# CouchbaseUser Resource

CouchbaseUser allows the automation of Couchbase user management.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseUser
metadata:
  name: ""
spec:
  authDomain: ""
  authSecret: ""
  fullName: ""
```

## [](#couchbaseusers-apiversion)couchbaseusers.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbaseusers-kind)couchbaseusers.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbaseusers-metadata)couchbaseusers.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbaseusers-metadata-name)couchbaseusers.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbaseusers-metadata-namespace)couchbaseusers.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbaseusers-metadata-labels)couchbaseusers.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbaseusers-metadata-annotations)couchbaseusers.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbaseusers-spec)couchbaseusers.spec

### [](#constraints-8)Constraints

**Required**

**Type**: `object`

### [](#description-8)Description

CouchbaseUserSpec allows the specification of Couchbase user configuration.

### [](#couchbaseusers-spec-authdomain)couchbaseusers.spec.authDomain

#### [](#constraints-9)Constraints

**Required**

**Type**: `string`

**Enumerations**: `local, external`

#### [](#description-9)Description

The domain which provides user authentication.

### [](#couchbaseusers-spec-authsecret)couchbaseusers.spec.authSecret

#### [](#constraints-10)Constraints

**Type**: `string`

#### [](#description-10)Description

Name of Kubernetes secret with password for Couchbase domain.

### [](#couchbaseusers-spec-fullname)couchbaseusers.spec.fullName

#### [](#constraints-11)Constraints

**Type**: `string`

#### [](#description-11)Description

Full Name of Couchbase user.