---
title: CouchbaseAutoscaler Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.9.x/docs/user/modules/ROOT/pages/resource/couchbaseautoscaler.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:operator::resource/couchbaseautoscaler.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/resource/couchbaseautoscaler.html)

# CouchbaseAutoscaler Resource

CouchbaseAutoscaler provides an interface for the Kubernetes Horizontal Pod Autoscaler to interact with the Couchbase cluster and provide autoscaling. This resource is not defined by the end user, and is managed by the Operator.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseAutoscaler
metadata:
  name: ""
spec:
  servers: ""
  size: 0
status:
  labelSelector: ""
  size: 0
```

## [](#couchbaseautoscalers-apiversion)couchbaseautoscalers.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbaseautoscalers-kind)couchbaseautoscalers.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbaseautoscalers-metadata)couchbaseautoscalers.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbaseautoscalers-metadata-name)couchbaseautoscalers.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbaseautoscalers-metadata-namespace)couchbaseautoscalers.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbaseautoscalers-metadata-labels)couchbaseautoscalers.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbaseautoscalers-metadata-annotations)couchbaseautoscalers.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbaseautoscalers-spec)couchbaseautoscalers.spec

### [](#constraints-8)Constraints

**Required**

**Type**: `object`

### [](#description-8)Description

CouchbaseAutoscalerSpec allows control over an autoscaling group.

### [](#couchbaseautoscalers-spec-servers)couchbaseautoscalers.spec.servers

#### [](#constraints-9)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

#### [](#description-9)Description

Servers specifies the server group that this autoscaler belongs to.

### [](#couchbaseautoscalers-spec-size)couchbaseautoscalers.spec.size

#### [](#constraints-10)Constraints

**Required**

**Type**: `integer`

**Minimum**: `0`

#### [](#description-10)Description

Size allows the server group to be dynamically scaled.

## [](#couchbaseautoscalers-status)couchbaseautoscalers.status

### [](#constraints-11)Constraints

**Type**: `object`

### [](#description-11)Description

CouchbaseAutoscalerStatus provides information to the HPA to assist with scaling server groups.

### [](#couchbaseautoscalers-status-labelselector)couchbaseautoscalers.status.labelSelector

#### [](#constraints-12)Constraints

**Required**

**Type**: `string`

#### [](#description-12)Description

LabelSelector allows the HPA to select resources to monitor for resource utilization in order to trigger scaling.

### [](#couchbaseautoscalers-status-size)couchbaseautoscalers.status.size

#### [](#constraints-13)Constraints

**Required**

**Type**: `integer`

**Minimum**: `1`

#### [](#description-13)Description

Size is the current size of the server group.