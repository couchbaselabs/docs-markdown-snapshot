[View original HTML](/operator/2.8/resource/couchbasegroup.html)

CouchbaseGroup allows the automation of Couchbase group management.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseGroup
metadata:
  name: ""
spec:
  ldapGroupRef: ""
  roles:
  - bucket: ""
    buckets:
      resources:
      - kind: CouchbaseBucket
        name: ""
      selector:
        matchExpressions:
        - key: ""
          operator: ""
          values:
          - ""
        matchLabels:
    collections:
      resources:
      - kind: CouchbaseCollection
        name: ""
      selector:
        matchExpressions:
        - key: ""
          operator: ""
          values:
          - ""
        matchLabels:
    name: ""
    scopes:
      resources:
      - kind: CouchbaseScope
        name: ""
      selector:
        matchExpressions:
        - key: ""
          operator: ""
          values:
          - ""
        matchLabels:
```

## [](#couchbasegroups-apiversion)couchbasegroups.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbasegroups-kind)couchbasegroups.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbasegroups-metadata)couchbasegroups.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbasegroups-metadata-name)couchbasegroups.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbasegroups-metadata-namespace)couchbasegroups.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbasegroups-metadata-labels)couchbasegroups.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbasegroups-metadata-annotations)couchbasegroups.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbasegroups-spec)couchbasegroups.spec

### [](#constraints-8)Constraints

**Required**

**Type**: `object`

### [](#description-8)Description

CouchbaseGroupSpec allows the specification of Couchbase group configuration.

### [](#couchbasegroups-spec-ldapgroupref)couchbasegroups.spec.ldapGroupRef

#### [](#constraints-9)Constraints

**Type**: `string`

#### [](#description-9)Description

LDAPGroupRef is a reference to an LDAP group.

### [](#couchbasegroups-spec-roles)couchbasegroups.spec.roles

#### [](#constraints-10)Constraints

**Required**

**Type**: `[]object`

#### [](#description-10)Description

Roles is a list of roles that this group is granted.

### [](#couchbasegroups-spec-roles-bucket)couchbasegroups.spec.roles.bucket

#### [](#constraints-11)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `\\*$|[a-zA-Z0-9-_%\.]+$`

#### [](#description-11)Description

Bucket name for bucket admin roles. When not specified for a role that can be scoped to a specific bucket, the role will apply to all buckets in the cluster. Deprecated: Couchbase Autonomous Operator 2.3.

### [](#couchbasegroups-spec-roles-buckets)couchbasegroups.spec.roles.buckets

#### [](#constraints-12)Constraints

**Type**: `object`

#### [](#description-12)Description

Bucket level access to apply to specified role. The bucket must exist. When not specified, the bucket field will be checked. If both are empty and the role can be scoped to a specific bucket, the role will apply to all buckets in the cluster.

### [](#couchbasegroups-spec-roles-buckets-resources)couchbasegroups.spec.roles.buckets.resources

#### [](#constraints-13)Constraints

**Type**: `[]object`

#### [](#description-13)Description

Resources is an explicit list of named bucket resources that will be considered for inclusion in this role. If a resource reference doesn’t match a resource, then no error conditions are raised due to undefined resource creation ordering and eventual consistency.

### [](#couchbasegroups-spec-roles-buckets-resources-kind)couchbasegroups.spec.roles.buckets.resources.kind

#### [](#constraints-14)Constraints

**Type**: `string`

**Default**: `CouchbaseBucket`

**Enumerations**: `CouchbaseBucket`

#### [](#description-14)Description

Kind indicates the kind of resource that is being referenced. A Role can only reference `CouchbaseBucket` kind. This field defaults to `CouchbaseBucket` if not specified.

### [](#couchbasegroups-spec-roles-buckets-resources-name)couchbasegroups.spec.roles.buckets.resources.name

#### [](#constraints-15)Constraints

**Required**

**Type**: `string`

#### [](#description-15)Description

Name is the name of the Kubernetes resource name that is being referenced.

### [](#couchbasegroups-spec-roles-buckets-selector)couchbasegroups.spec.roles.buckets.selector

#### [](#constraints-16)Constraints

**Type**: `object`

#### [](#description-16)Description

Selector allows resources to be implicitly considered for inclusion in this role. More info: <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#labelselector-v1-meta>.

### [](#couchbasegroups-spec-roles-buckets-selector-matchexpressions)couchbasegroups.spec.roles.buckets.selector.matchExpressions

#### [](#constraints-17)Constraints

**Type**: `[]object`

#### [](#description-17)Description

matchExpressions is a list of label selector requirements. The requirements are ANDed.

### [](#couchbasegroups-spec-roles-buckets-selector-matchexpressions-key)couchbasegroups.spec.roles.buckets.selector.matchExpressions.key

#### [](#constraints-18)Constraints

**Required**

**Type**: `string`

#### [](#description-18)Description

key is the label key that the selector applies to.

### [](#couchbasegroups-spec-roles-buckets-selector-matchexpressions-operator)couchbasegroups.spec.roles.buckets.selector.matchExpressions.operator

#### [](#constraints-19)Constraints

**Required**

**Type**: `string`

#### [](#description-19)Description

operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.

### [](#couchbasegroups-spec-roles-buckets-selector-matchexpressions-values)couchbasegroups.spec.roles.buckets.selector.matchExpressions.values

#### [](#constraints-20)Constraints

**Type**: `[]string`

#### [](#description-20)Description

values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

### [](#couchbasegroups-spec-roles-buckets-selector-matchlabels)couchbasegroups.spec.roles.buckets.selector.matchLabels

#### [](#constraints-21)Constraints

**Type**: `map[string]string`

#### [](#description-21)Description

matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

### [](#couchbasegroups-spec-roles-collections)couchbasegroups.spec.roles.collections

#### [](#constraints-22)Constraints

**Type**: `object`

#### [](#description-22)Description

Collection level access to apply to the specified role. The collection must exist. When not specified, the role is subject to scope or bucket level access.

### [](#couchbasegroups-spec-roles-collections-resources)couchbasegroups.spec.roles.collections.resources

#### [](#constraints-23)Constraints

**Type**: `[]object`

#### [](#description-23)Description

Resources is an explicit list of named resources that will be considered for inclusion in this collection or collections. If a resource reference doesn’t match a resource, then no error conditions are raised due to undefined resource creation ordering and eventual consistency.

### [](#couchbasegroups-spec-roles-collections-resources-kind)couchbasegroups.spec.roles.collections.resources.kind

#### [](#constraints-24)Constraints

**Type**: `string`

**Default**: `CouchbaseCollection`

**Enumerations**: `CouchbaseCollection, CouchbaseCollectionGroup`

#### [](#description-24)Description

Kind indicates the kind of resource that is being referenced. A scope can only reference `CouchbaseCollection` and `CouchbaseCollectionGroup`resource kinds. This field defaults to `CouchbaseCollection` if not specified.

### [](#couchbasegroups-spec-roles-collections-resources-name)couchbasegroups.spec.roles.collections.resources.name

#### [](#constraints-25)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250}$`

#### [](#description-25)Description

Name is the name of the Kubernetes resource name that is being referenced. Legal collection names have a maximum length of 251 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "\_-%".

### [](#couchbasegroups-spec-roles-collections-selector)couchbasegroups.spec.roles.collections.selector

#### [](#constraints-26)Constraints

**Type**: `object`

#### [](#description-26)Description

Selector allows resources to be implicitly considered for inclusion in this collection or collections. More info: <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#labelselector-v1-meta>.

### [](#couchbasegroups-spec-roles-collections-selector-matchexpressions)couchbasegroups.spec.roles.collections.selector.matchExpressions

#### [](#constraints-27)Constraints

**Type**: `[]object`

#### [](#description-27)Description

matchExpressions is a list of label selector requirements. The requirements are ANDed.

### [](#couchbasegroups-spec-roles-collections-selector-matchexpressions-key)couchbasegroups.spec.roles.collections.selector.matchExpressions.key

#### [](#constraints-28)Constraints

**Required**

**Type**: `string`

#### [](#description-28)Description

key is the label key that the selector applies to.

### [](#couchbasegroups-spec-roles-collections-selector-matchexpressions-operator)couchbasegroups.spec.roles.collections.selector.matchExpressions.operator

#### [](#constraints-29)Constraints

**Required**

**Type**: `string`

#### [](#description-29)Description

operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.

### [](#couchbasegroups-spec-roles-collections-selector-matchexpressions-values)couchbasegroups.spec.roles.collections.selector.matchExpressions.values

#### [](#constraints-30)Constraints

**Type**: `[]string`

#### [](#description-30)Description

values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

### [](#couchbasegroups-spec-roles-collections-selector-matchlabels)couchbasegroups.spec.roles.collections.selector.matchLabels

#### [](#constraints-31)Constraints

**Type**: `map[string]string`

#### [](#description-31)Description

matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

### [](#couchbasegroups-spec-roles-name)couchbasegroups.spec.roles.name

#### [](#constraints-32)Constraints

**Required**

**Type**: `string`

**Enumerations**: `admin, analytics_admin, analytics_manager, analytics_reader, analytics_select, backup_admin, bucket_admin, bucket_full_access, cluster_admin, data_backup, data_dcp_reader, data_monitoring, data_reader, data_writer, eventing_admin, external_stats_reader, fts_admin, fts_searcher, mobile_sync_gateway, sync_gateway_app, sync_gateway_app_ro, sync_gateway_configurator, sync_gateway_dev_ops, sync_gateway_replicator, query_delete, query_execute_external_functions, query_execute_functions, query_execute_global_external_functions, query_execute_global_functions, query_external_access, query_insert, query_manage_external_functions, query_manage_functions, query_manage_global_external_functions, query_manage_global_functions, query_manage_index, query_select, query_system_catalog, query_update, replication_admin, replication_target, ro_admin, scope_admin, security_admin, security_admin_external, security_admin_local, views_admin, views_reader, eventing_manage_functions, query_use_sequential_scans, query_use_sequences, query_manage_sequences`

#### [](#description-32)Description

Name of role.

### [](#couchbasegroups-spec-roles-scopes)couchbasegroups.spec.roles.scopes

#### [](#constraints-33)Constraints

**Type**: `object`

#### [](#description-33)Description

Scope level access to apply to specified role. The scope must exist. When not specified, the role will apply to selected bucket or all buckets in the cluster.

### [](#couchbasegroups-spec-roles-scopes-resources)couchbasegroups.spec.roles.scopes.resources

#### [](#constraints-34)Constraints

**Type**: `[]object`

#### [](#description-34)Description

Resources is an explicit list of named resources that will be considered for inclusion in this scope or scopes. If a resource reference doesn’t match a resource, then no error conditions are raised due to undefined resource creation ordering and eventual consistency.

### [](#couchbasegroups-spec-roles-scopes-resources-kind)couchbasegroups.spec.roles.scopes.resources.kind

#### [](#constraints-35)Constraints

**Type**: `string`

**Default**: `CouchbaseScope`

**Enumerations**: `CouchbaseScope, CouchbaseScopeGroup`

#### [](#description-35)Description

Kind indicates the kind of resource that is being referenced. A scope can only reference `CouchbaseScope` and `CouchbaseScopeGroup`resource kinds. This field defaults to `CouchbaseScope` if not specified.

### [](#couchbasegroups-spec-roles-scopes-resources-name)couchbasegroups.spec.roles.scopes.resources.name

#### [](#constraints-36)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250}$`

#### [](#description-36)Description

Name is the name of the Kubernetes resource name that is being referenced. Legal scope names have a maximum length of 251 characters and may be composed of any character from "a-z", "A-Z", "0-9" and "\_-%".

### [](#couchbasegroups-spec-roles-scopes-selector)couchbasegroups.spec.roles.scopes.selector

#### [](#constraints-37)Constraints

**Type**: `object`

#### [](#description-37)Description

Selector allows resources to be implicitly considered for inclusion in this scope or scopes. More info: <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#labelselector-v1-meta>.

### [](#couchbasegroups-spec-roles-scopes-selector-matchexpressions)couchbasegroups.spec.roles.scopes.selector.matchExpressions

#### [](#constraints-38)Constraints

**Type**: `[]object`

#### [](#description-38)Description

matchExpressions is a list of label selector requirements. The requirements are ANDed.

### [](#couchbasegroups-spec-roles-scopes-selector-matchexpressions-key)couchbasegroups.spec.roles.scopes.selector.matchExpressions.key

#### [](#constraints-39)Constraints

**Required**

**Type**: `string`

#### [](#description-39)Description

key is the label key that the selector applies to.

### [](#couchbasegroups-spec-roles-scopes-selector-matchexpressions-operator)couchbasegroups.spec.roles.scopes.selector.matchExpressions.operator

#### [](#constraints-40)Constraints

**Required**

**Type**: `string`

#### [](#description-40)Description

operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.

### [](#couchbasegroups-spec-roles-scopes-selector-matchexpressions-values)couchbasegroups.spec.roles.scopes.selector.matchExpressions.values

#### [](#constraints-41)Constraints

**Type**: `[]string`

#### [](#description-41)Description

values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

### [](#couchbasegroups-spec-roles-scopes-selector-matchlabels)couchbasegroups.spec.roles.scopes.selector.matchLabels

#### [](#constraints-42)Constraints

**Type**: `map[string]string`

#### [](#description-42)Description

matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.