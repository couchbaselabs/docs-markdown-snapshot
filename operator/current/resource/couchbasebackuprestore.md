---
title: CouchbaseBackupRestore Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.9.x/docs/user/modules/ROOT/pages/resource/couchbasebackuprestore.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/operator/current/resource/couchbasebackuprestore.html)

# CouchbaseBackupRestore Resource

CouchbaseBackupRestore allows the restoration of all Couchbase cluster data from a CouchbaseBackup resource.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseBackupRestore
metadata:
  name: ""
spec:
  backoffLimit: 2
  backup: ""
  buckets:
  data:
    exclude:
    - ""
    filterKeys: ""
    filterValues: ""
    include:
    - ""
    map:
    - source: ""
      target: ""
  defaultRecoveryMethod: none
  end:
    int: 0
    str: ""
  env:
  - name: ""
    value: ""
    valueFrom:
      configMapKeyRef:
        key: ""
        name: ""
        optional: false
      fieldRef:
        apiVersion: ""
        fieldPath: ""
      resourceFieldRef:
        containerName: ""
        divisor: ""
        resource: ""
      secretKeyRef:
        key: ""
        name: ""
        optional: false
  forceUpdates: false
  logRetention: 168h
  objectStore:
    endpoint:
      secret: ""
      url: ""
      useVirtualPath: false
    secret: ""
    uri: ""
    useIAM: false
  overwriteUsers: false
  preserveRestoreRecord: false
  repo: ""
  s3bucket: ""
  services:
    analytics: True
    bucketConfig: false
    bucketQuery: True
    clusterAnalytics: True
    clusterQuery: True
    data: True
    eventing: True
    ftAlias: True
    ftIndex: True
    gsiIndex: True
    users: false
    views: True
  stagingVolume:
    size: 20Gi
    storageClassName: ""
  start:
    int: 0
    str: ""
  threads: 1
  ttlSecondsAfterFinished: 0
status:
  archive: ""
  backups:
  - full: ""
    incrementals:
    - ""
    name: ""
  completed: false
  duration: ""
  failed: false
  job: ""
  lastFailure: ""
  lastRun: ""
  lastSuccess: ""
  output: ""
  pod: ""
  repo: ""
  running: false
```

## [](#couchbasebackuprestores-apiversion)couchbasebackuprestores.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbasebackuprestores-kind)couchbasebackuprestores.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbasebackuprestores-metadata)couchbasebackuprestores.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbasebackuprestores-metadata-name)couchbasebackuprestores.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbasebackuprestores-metadata-namespace)couchbasebackuprestores.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbasebackuprestores-metadata-labels)couchbasebackuprestores.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbasebackuprestores-metadata-annotations)couchbasebackuprestores.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbasebackuprestores-spec)couchbasebackuprestores.spec

### [](#constraints-8)Constraints

**Required**

**Type**: `object`

### [](#description-8)Description

CouchbaseBackupRestoreSpec allows the specification of data restoration to be configured. This includes the backup and repository to restore data from, and the time range of data to be restored.

### [](#couchbasebackuprestores-spec-backofflimit)couchbasebackuprestores.spec.backoffLimit

#### [](#constraints-9)Constraints

**Type**: `integer`

**Default**: `2`

#### [](#description-9)Description

Number of times the restore job should try to execute.

### [](#couchbasebackuprestores-spec-backup)couchbasebackuprestores.spec.backup

#### [](#constraints-10)Constraints

**Type**: `string`

#### [](#description-10)Description

The backup resource name associated with this restore, or the backup PVC name to restore from.

### [](#couchbasebackuprestores-spec-buckets)couchbasebackuprestores.spec.buckets

#### [](#constraints-11)Constraints

**Type**: `object`

#### [](#description-11)Description

**DEPRECATED** \- by spec.data.

Specific buckets can be explicitly included or excluded in the restore, as well as bucket mappings. This field is now ignored.

### [](#couchbasebackuprestores-spec-data)couchbasebackuprestores.spec.data

#### [](#constraints-12)Constraints

**Type**: `object`

#### [](#description-12)Description

Data allows control over what key-value/document data is included in the restore. By default, all data is included.

### [](#couchbasebackuprestores-spec-data-exclude)couchbasebackuprestores.spec.data.exclude

#### [](#constraints-13)Constraints

**Type**: `[]string`

**Minimum Items**: `1`

**Pattern (Regular Expression)**: `^(?:[a-zA-Z0-9\-_%]|\\.){1,100}(\.default(\.default)?|\.[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,29}(\.[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,29})?)?$`

#### [](#description-13)Description

Exclude defines the buckets, scopes or collections that are excluded from the backup. When this field is set, it implies that by default everything will be backed up, and data items can be explicitly excluded. You may define an exclusion as a bucket — `my-bucket`, a scope — `my-bucket.my-scope`, or a collection — `my-bucket.my-scope.my-collection`. Buckets may contain periods, and therefore must be escaped — `my\.bucket.my-scope`, as period is the separator used to delimit scopes and collections. Excluded data cannot overlap e.g. specifying `my-bucket` and `my-bucket.my-scope` is illegal. This field cannot be used at the same time as included items.

### [](#couchbasebackuprestores-spec-data-filterkeys)couchbasebackuprestores.spec.data.filterKeys

#### [](#constraints-14)Constraints

**Type**: `string`

#### [](#description-14)Description

FilterKeys only restores documents whose names match the provided regular expression.

### [](#couchbasebackuprestores-spec-data-filtervalues)couchbasebackuprestores.spec.data.filterValues

#### [](#constraints-15)Constraints

**Type**: `string`

#### [](#description-15)Description

FilterValues only restores documents whose values match the provided regular expression.

### [](#couchbasebackuprestores-spec-data-include)couchbasebackuprestores.spec.data.include

#### [](#constraints-16)Constraints

**Type**: `[]string`

**Minimum Items**: `1`

**Pattern (Regular Expression)**: `^(?:[a-zA-Z0-9\-_%]|\\.){1,100}(\.default(\.default)?|\.[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,29}(\.[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,29})?)?$`

#### [](#description-16)Description

Include defines the buckets, scopes or collections that are included in the restore. When this field is set, it implies that by default nothing will be restored, and data items must be explicitly included. You may define an inclusion as a bucket — `my-bucket`, a scope — `my-bucket.my-scope`, or a collection — `my-bucket.my-scope.my-collection`. Buckets may contain periods, and therefore must be escaped — `my\.bucket.my-scope`, as period is the separator used to delimit scopes and collections. Included data cannot overlap e.g. specifying `my-bucket` and `my-bucket.my-scope` is illegal. This field cannot be used at the same time as excluded items.

### [](#couchbasebackuprestores-spec-data-map)couchbasebackuprestores.spec.data.map

#### [](#constraints-17)Constraints

**Type**: `[]object`

#### [](#description-17)Description

Map allows data items in the restore to be remapped to a different named container. Buckets can be remapped to other buckets e.g. "source=target", scopes and collections can be remapped to other scopes and collections within the same bucket only e.g. "bucket.scope=bucket.other" or "bucket.scope.collection=bucket.scope.other". Map sources may only be specified once, and may not overlap.

### [](#couchbasebackuprestores-spec-data-map-source)couchbasebackuprestores.spec.data.map.source

#### [](#constraints-18)Constraints

**Required**

**Type**: `string`

**Pattern (Regular Expression)**: `^(?:[a-zA-Z0-9\-_%]|\\.){1,100}(\.default(\.default)?|\.[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,29}(\.[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,29})?)?$`

#### [](#description-18)Description

Source defines the data source of the mapping, this may be either a bucket, scope or collection.

### [](#couchbasebackuprestores-spec-data-map-target)couchbasebackuprestores.spec.data.map.target

#### [](#constraints-19)Constraints

**Required**

**Type**: `string`

**Pattern (Regular Expression)**: `^(?:[a-zA-Z0-9\-_%]|\\.){1,100}(\.default(\.default)?|\.[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,29}(\.[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,29})?)?$`

#### [](#description-19)Description

Target defines the data target of the mapping, this may be either a bucket, scope or collection, and must refer to the same type as the restore source.

### [](#couchbasebackuprestores-spec-defaultrecoverymethod)couchbasebackuprestores.spec.defaultRecoveryMethod

#### [](#constraints-20)Constraints

**Type**: `string`

**Default**: `none`

**Enumerations**: `none, resume, purge`

#### [](#description-20)Description

DefaultRecoveryMethod specifies how cbbackupmgr should recover from broken backup/restore attempts.

### [](#couchbasebackuprestores-spec-end)couchbasebackuprestores.spec.end

#### [](#constraints-21)Constraints

**Type**: `object`

#### [](#description-21)Description

End denotes the last backup to restore from. Omitting this field will only restore the backup referenced by start. This may be specified as an integer index (starting from 1), a string specifying a short date DD-MM-YYYY, the backup name, or one of either `end` or `latest` keywords.

### [](#couchbasebackuprestores-spec-end-int)couchbasebackuprestores.spec.end.int

#### [](#constraints-22)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-22)Description

Int references a relative backup by index.

### [](#couchbasebackuprestores-spec-end-str)couchbasebackuprestores.spec.end.str

#### [](#constraints-23)Constraints

**Type**: `string`

#### [](#description-23)Description

Str references an absolute backup by name.

### [](#couchbasebackuprestores-spec-env)couchbasebackuprestores.spec.env

#### [](#constraints-24)Constraints

**Type**: `[]object`

#### [](#description-24)Description

Env defines environment variables to be set on the restore container. These can be used to configure cbbackupmgr behavior via environment variables.

### [](#couchbasebackuprestores-spec-env-name)couchbasebackuprestores.spec.env.name

#### [](#constraints-25)Constraints

**Required**

**Type**: `string`

#### [](#description-25)Description

Name of the environment variable. Must be a C\_IDENTIFIER.

### [](#couchbasebackuprestores-spec-env-value)couchbasebackuprestores.spec.env.value

#### [](#constraints-26)Constraints

**Type**: `string`

#### [](#description-26)Description

Variable references $(VAR\_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR\_NAME) syntax: i.e. "(VAR\_NAME)" will produce the string literal "$(VAR\_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".

### [](#couchbasebackuprestores-spec-env-valuefrom)couchbasebackuprestores.spec.env.valueFrom

#### [](#constraints-27)Constraints

**Type**: `object`

#### [](#description-27)Description

Source for the environment variable’s value. Cannot be used if value is not empty.

### [](#couchbasebackuprestores-spec-env-valuefrom-configmapkeyref)couchbasebackuprestores.spec.env.valueFrom.configMapKeyRef

#### [](#constraints-28)Constraints

**Type**: `object`

#### [](#description-28)Description

Selects a key of a ConfigMap.

### [](#couchbasebackuprestores-spec-env-valuefrom-configmapkeyref-key)couchbasebackuprestores.spec.env.valueFrom.configMapKeyRef.key

#### [](#constraints-29)Constraints

**Required**

**Type**: `string`

#### [](#description-29)Description

The key to select.

### [](#couchbasebackuprestores-spec-env-valuefrom-configmapkeyref-name)couchbasebackuprestores.spec.env.valueFrom.configMapKeyRef.name

#### [](#constraints-30)Constraints

**Type**: `string`

#### [](#description-30)Description

Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>.

### [](#couchbasebackuprestores-spec-env-valuefrom-configmapkeyref-optional)couchbasebackuprestores.spec.env.valueFrom.configMapKeyRef.optional

#### [](#constraints-31)Constraints

**Type**: `boolean`

#### [](#description-31)Description

Specify whether the ConfigMap or its key must be defined.

### [](#couchbasebackuprestores-spec-env-valuefrom-fieldref)couchbasebackuprestores.spec.env.valueFrom.fieldRef

#### [](#constraints-32)Constraints

**Type**: `object`

#### [](#description-32)Description

Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.

### [](#couchbasebackuprestores-spec-env-valuefrom-fieldref-apiversion)couchbasebackuprestores.spec.env.valueFrom.fieldRef.apiVersion

#### [](#constraints-33)Constraints

**Type**: `string`

#### [](#description-33)Description

Version of the schema the FieldPath is written in terms of, defaults to "v1".

### [](#couchbasebackuprestores-spec-env-valuefrom-fieldref-fieldpath)couchbasebackuprestores.spec.env.valueFrom.fieldRef.fieldPath

#### [](#constraints-34)Constraints

**Required**

**Type**: `string`

#### [](#description-34)Description

Path of the field to select in the specified API version.

### [](#couchbasebackuprestores-spec-env-valuefrom-resourcefieldref)couchbasebackuprestores.spec.env.valueFrom.resourceFieldRef

#### [](#constraints-35)Constraints

**Type**: `object`

#### [](#description-35)Description

Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.

### [](#couchbasebackuprestores-spec-env-valuefrom-resourcefieldref-containername)couchbasebackuprestores.spec.env.valueFrom.resourceFieldRef.containerName

#### [](#constraints-36)Constraints

**Type**: `string`

#### [](#description-36)Description

Container name: required for volumes, optional for env vars.

### [](#couchbasebackuprestores-spec-env-valuefrom-resourcefieldref-divisor)couchbasebackuprestores.spec.env.valueFrom.resourceFieldRef.divisor

#### [](#constraints-37)Constraints

**Type**: `integer or string`

#### [](#description-37)Description

Specifies the output format of the exposed resources, defaults to "1".

### [](#couchbasebackuprestores-spec-env-valuefrom-resourcefieldref-resource)couchbasebackuprestores.spec.env.valueFrom.resourceFieldRef.resource

#### [](#constraints-38)Constraints

**Required**

**Type**: `string`

#### [](#description-38)Description

Required: resource to select.

### [](#couchbasebackuprestores-spec-env-valuefrom-secretkeyref)couchbasebackuprestores.spec.env.valueFrom.secretKeyRef

#### [](#constraints-39)Constraints

**Type**: `object`

#### [](#description-39)Description

Selects a key of a secret in the pod’s namespace.

### [](#couchbasebackuprestores-spec-env-valuefrom-secretkeyref-key)couchbasebackuprestores.spec.env.valueFrom.secretKeyRef.key

#### [](#constraints-40)Constraints

**Required**

**Type**: `string`

#### [](#description-40)Description

The key of the secret to select from. Must be a valid secret key.

### [](#couchbasebackuprestores-spec-env-valuefrom-secretkeyref-name)couchbasebackuprestores.spec.env.valueFrom.secretKeyRef.name

#### [](#constraints-41)Constraints

**Type**: `string`

#### [](#description-41)Description

Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>.

### [](#couchbasebackuprestores-spec-env-valuefrom-secretkeyref-optional)couchbasebackuprestores.spec.env.valueFrom.secretKeyRef.optional

#### [](#constraints-42)Constraints

**Type**: `boolean`

#### [](#description-42)Description

Specify whether the Secret or its key must be defined.

### [](#couchbasebackuprestores-spec-forceupdates)couchbasebackuprestores.spec.forceUpdates

#### [](#constraints-43)Constraints

**Type**: `boolean`

#### [](#description-43)Description

Forces data in the Couchbase cluster to be overwritten even if the data in the cluster is newer. By default, the system does not force updates, and all updates use Couchbase’s conflict resolution mechanism to ensure that if newer data exists on the cluster, older restored data does not overwrite it. However, if `couchbasebackuprestores.spec.forceUpdates` is true, then the backup record will _always_ overwrite the cluster record, regardless of Couchbase’s conflict resolution.

### [](#couchbasebackuprestores-spec-logretention)couchbasebackuprestores.spec.logRetention

#### [](#constraints-44)Constraints

**Type**: `string`

**Default**: `168h`

#### [](#description-44)Description

Number of hours to hold restore script logs for, everything older will be deleted. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbasebackuprestores-spec-objectstore)couchbasebackuprestores.spec.objectStore

#### [](#constraints-45)Constraints

**Type**: `object`

#### [](#description-45)Description

The remote destination for backup.

### [](#couchbasebackuprestores-spec-objectstore-endpoint)couchbasebackuprestores.spec.objectStore.endpoint

#### [](#constraints-46)Constraints

**Type**: `object`

#### [](#description-46)Description

Endpoint contains the configuration for connecting to a custom Azure/S3/GCP compliant object store. If set will override `CouchbaseCluster.spec.backup.objectEndpoint`See <https://docs.couchbase.com/server/current/backup-restore/cbbackupmgr-cloud.html#compatible-object-stores>.

### [](#couchbasebackuprestores-spec-objectstore-endpoint-secret)couchbasebackuprestores.spec.objectStore.endpoint.secret

#### [](#constraints-47)Constraints

**Type**: `string`

#### [](#description-47)Description

The name of the secret, in this namespace, that contains the CA certificate for verification of a TLS endpoint The secret must have the key with the name "tls.crt".

### [](#couchbasebackuprestores-spec-objectstore-endpoint-url)couchbasebackuprestores.spec.objectStore.endpoint.url

#### [](#constraints-48)Constraints

**Type**: `string`

#### [](#description-48)Description

The host/address of the custom object endpoint.

### [](#couchbasebackuprestores-spec-objectstore-endpoint-usevirtualpath)couchbasebackuprestores.spec.objectStore.endpoint.useVirtualPath

#### [](#constraints-49)Constraints

**Type**: `boolean`

#### [](#description-49)Description

UseVirtualPath will force the AWS SDK to use the new virtual style paths which are often required by S3 compatible object stores.

### [](#couchbasebackuprestores-spec-objectstore-secret)couchbasebackuprestores.spec.objectStore.secret

#### [](#constraints-50)Constraints

**Type**: `string`

#### [](#description-50)Description

ObjStoreSecret must contain two fields, access-key-id, secret-access-key and optionally either region or refresh-token. These correspond to the fields used by cbbackupmgr <https://docs.couchbase.com/server/current/backup-restore/cbbackupmgr-backup.html#optional-2>.

### [](#couchbasebackuprestores-spec-objectstore-uri)couchbasebackuprestores.spec.objectStore.uri

#### [](#constraints-51)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(az|s3|gs)://.{3,}$`

#### [](#description-51)Description

URI is a reference to a remote object store. This is the prefix of the object store and the bucket name. i.e s3://bucket, az://bucket or gs://bucket.

### [](#couchbasebackuprestores-spec-objectstore-useiam)couchbasebackuprestores.spec.objectStore.useIAM

#### [](#constraints-52)Constraints

**Type**: `boolean`

#### [](#description-52)Description

Whether to allow the backup SDK to attempt to authenticate using the instance metadata api. If set, will override `CouchbaseCluster.spec.backup.useIAM`.

### [](#couchbasebackuprestores-spec-overwriteusers)couchbasebackuprestores.spec.overwriteUsers

#### [](#constraints-53)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-53)Description

Overwrites the already existing users in the cluster when user restoration is enabled (spec.services.users). The default behavior of backup/restore of users is to skip already existing users. This is only available for Couchbase Server 7.6 and later. This field defaults to `false`.

### [](#couchbasebackuprestores-spec-preserverestorerecord)couchbasebackuprestores.spec.preserveRestoreRecord

#### [](#constraints-54)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-54)Description

PreserveRestoreRecord indicates whether the restore record should be preserved after the restore job has completed.

### [](#couchbasebackuprestores-spec-repo)couchbasebackuprestores.spec.repo

#### [](#constraints-55)Constraints

**Type**: `string`

#### [](#description-55)Description

Repo is the backup folder to restore from. If no repository is specified, the backup container will choose the latest.

### [](#couchbasebackuprestores-spec-s3bucket)couchbasebackuprestores.spec.s3bucket

#### [](#constraints-56)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^s3://[a-z0-9-\.\/]{3,63}$`

#### [](#description-56)Description

**DEPRECATED** \- by spec.objectStore.uri Name of S3 bucket to restore from.

If non-empty this overrides local backup.

### [](#couchbasebackuprestores-spec-services)couchbasebackuprestores.spec.services

#### [](#constraints-57)Constraints

**Type**: `object`

**Default**: `{}`

#### [](#description-57)Description

This list accepts a certain set of parameters that will disable that data and prevent it being restored.

### [](#couchbasebackuprestores-spec-services-analytics)couchbasebackuprestores.spec.services.analytics

#### [](#constraints-58)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-58)Description

Analytics restores analytics datasets from the backup. This field defaults to true.

### [](#couchbasebackuprestores-spec-services-bucketconfig)couchbasebackuprestores.spec.services.bucketConfig

#### [](#constraints-59)Constraints

**Type**: `boolean`

#### [](#description-59)Description

BucketConfig restores all bucket configuration settings. If you are restoring to cluster with managed buckets, then this option may conflict with existing bucket settings, and the results are undefined, so avoid use. This option is intended for use with unmanaged buckets. Note that bucket durability settings are not restored in versions less than and equal to 1.1.0, and will need to be manually applied. This field defaults to false.

### [](#couchbasebackuprestores-spec-services-bucketquery)couchbasebackuprestores.spec.services.bucketQuery

#### [](#constraints-60)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-60)Description

BucketQuery enables the backup of query metadata for all buckets. This field defaults to `true`.

### [](#couchbasebackuprestores-spec-services-clusteranalytics)couchbasebackuprestores.spec.services.clusterAnalytics

#### [](#constraints-61)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-61)Description

ClusterAnalytics enables the backup of cluster-wide analytics data, for example synonyms. This field defaults to `true`.

### [](#couchbasebackuprestores-spec-services-clusterquery)couchbasebackuprestores.spec.services.clusterQuery

#### [](#constraints-62)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-62)Description

ClusterQuery enables the backup of cluster level query metadata. This field defaults to `true`.

### [](#couchbasebackuprestores-spec-services-data)couchbasebackuprestores.spec.services.data

#### [](#constraints-63)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-63)Description

Data restores document data from the backup. This field defaults to true.

### [](#couchbasebackuprestores-spec-services-eventing)couchbasebackuprestores.spec.services.eventing

#### [](#constraints-64)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-64)Description

Eventing restores eventing functions from the backup. This field defaults to true.

### [](#couchbasebackuprestores-spec-services-ftalias)couchbasebackuprestores.spec.services.ftAlias

#### [](#constraints-65)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-65)Description

FTAlias restores full-text search aliases from the backup. This field defaults to true.

### [](#couchbasebackuprestores-spec-services-ftindex)couchbasebackuprestores.spec.services.ftIndex

#### [](#constraints-66)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-66)Description

FTIndex restores full-text search indexes from the backup. This field defaults to true.

### [](#couchbasebackuprestores-spec-services-gsiindex)couchbasebackuprestores.spec.services.gsiIndex

#### [](#constraints-67)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-67)Description

GSIIndex restores document indexes from the backup. This field defaults to true.

### [](#couchbasebackuprestores-spec-services-users)couchbasebackuprestores.spec.services.users

#### [](#constraints-68)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-68)Description

Users restores cluster level users, including their roles and permissions. This is only available for Couchbase Server 7.6 and later. This field defaults to `false`.

### [](#couchbasebackuprestores-spec-services-views)couchbasebackuprestores.spec.services.views

#### [](#constraints-69)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-69)Description

Views restores views from the backup. This field defaults to true.

### [](#couchbasebackuprestores-spec-stagingvolume)couchbasebackuprestores.spec.stagingVolume

#### [](#constraints-70)Constraints

**Type**: `object`

**Default**: `{'size': '20Gi'}`

#### [](#description-70)Description

StagingVolume contains configuration related to the ephemeral volume used as staging when restoring from a cloud backup.

### [](#couchbasebackuprestores-spec-stagingvolume-size)couchbasebackuprestores.spec.stagingVolume.size

#### [](#constraints-71)Constraints

**Type**: `string`

**Default**: `20Gi`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-71)Description

Size allows the specification of a staging volume. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>The ephemeral volume will only be used when restoring from a cloud provider, if the backup job was created using ephemeral storage. Otherwise the restore job will share a staging volume with the backup job.

### [](#couchbasebackuprestores-spec-stagingvolume-storageclassname)couchbasebackuprestores.spec.stagingVolume.storageClassName

#### [](#constraints-72)Constraints

**Type**: `string`

#### [](#description-72)Description

Name of StorageClass to use.

### [](#couchbasebackuprestores-spec-start)couchbasebackuprestores.spec.start

#### [](#constraints-73)Constraints

**Type**: `object`

#### [](#description-73)Description

Start denotes the first backup to restore from. This may be specified as an integer index (starting from 1), a string specifying a short date DD-MM-YYYY, the backup name, or one of either `start` or `oldest` keywords.

### [](#couchbasebackuprestores-spec-start-int)couchbasebackuprestores.spec.start.int

#### [](#constraints-74)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-74)Description

Int references a relative backup by index.

### [](#couchbasebackuprestores-spec-start-str)couchbasebackuprestores.spec.start.str

#### [](#constraints-75)Constraints

**Type**: `string`

#### [](#description-75)Description

Str references an absolute backup by name.

### [](#couchbasebackuprestores-spec-threads)couchbasebackuprestores.spec.threads

#### [](#constraints-76)Constraints

**Type**: `integer`

**Default**: `1`

**Minimum**: `1`

#### [](#description-76)Description

How many threads to use during the restore.

### [](#couchbasebackuprestores-spec-ttlsecondsafterfinished)couchbasebackuprestores.spec.ttlSecondsAfterFinished

#### [](#constraints-77)Constraints

**Type**: `integer`

**Minimum**: `0`

#### [](#description-77)Description

Number of seconds to elapse before a completed job is deleted.

## [](#couchbasebackuprestores-status)couchbasebackuprestores.status

### [](#constraints-78)Constraints

**Type**: `object`

### [](#description-78)Description

CouchbaseBackupRestoreStatus provides status indications of a restore from backup. This includes whether or not the restore is running, whether the restore succeed or not, and the duration the restore took.

### [](#couchbasebackuprestores-status-archive)couchbasebackuprestores.status.archive

#### [](#constraints-79)Constraints

**Type**: `string`

#### [](#description-79)Description

Location of Backup Archive.

### [](#couchbasebackuprestores-status-backups)couchbasebackuprestores.status.backups

#### [](#constraints-80)Constraints

**Type**: `[]object`

#### [](#description-80)Description

Backups gives us a full list of all backups and their respective repository locations.

### [](#couchbasebackuprestores-status-backups-full)couchbasebackuprestores.status.backups.full

#### [](#constraints-81)Constraints

**Type**: `string`

#### [](#description-81)Description

Full backup inside the repository.

### [](#couchbasebackuprestores-status-backups-incrementals)couchbasebackuprestores.status.backups.incrementals

#### [](#constraints-82)Constraints

**Type**: `[]string`

#### [](#description-82)Description

Incremental backups inside the repository.

### [](#couchbasebackuprestores-status-backups-name)couchbasebackuprestores.status.backups.name

#### [](#constraints-83)Constraints

**Required**

**Type**: `string`

#### [](#description-83)Description

Name of the repository.

### [](#couchbasebackuprestores-status-completed)couchbasebackuprestores.status.completed

#### [](#constraints-84)Constraints

**Required**

**Type**: `boolean`

#### [](#description-84)Description

Completed indicates whether the restore has been successfully completed.

### [](#couchbasebackuprestores-status-duration)couchbasebackuprestores.status.duration

#### [](#constraints-85)Constraints

**Type**: `string`

#### [](#description-85)Description

Duration tells us how long the last restore took. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbasebackuprestores-status-failed)couchbasebackuprestores.status.failed

#### [](#constraints-86)Constraints

**Required**

**Type**: `boolean`

#### [](#description-86)Description

Failed indicates whether the most recent restore has failed.

### [](#couchbasebackuprestores-status-job)couchbasebackuprestores.status.job

#### [](#constraints-87)Constraints

**Type**: `string`

#### [](#description-87)Description

**DEPRECATED** \- field may no longer be populated.

Job tells us which job is running/ran last.

### [](#couchbasebackuprestores-status-lastfailure)couchbasebackuprestores.status.lastFailure

#### [](#constraints-88)Constraints

**Type**: `string`

#### [](#description-88)Description

LastFailure tells us the time the last failed restore failed.

### [](#couchbasebackuprestores-status-lastrun)couchbasebackuprestores.status.lastRun

#### [](#constraints-89)Constraints

**Type**: `string`

#### [](#description-89)Description

LastRun tells us the time the last restore job started.

### [](#couchbasebackuprestores-status-lastsuccess)couchbasebackuprestores.status.lastSuccess

#### [](#constraints-90)Constraints

**Type**: `string`

#### [](#description-90)Description

LastSuccess gives us the time the last successful restore finished.

### [](#couchbasebackuprestores-status-output)couchbasebackuprestores.status.output

#### [](#constraints-91)Constraints

**Type**: `string`

#### [](#description-91)Description

**DEPRECATED** \- field may no longer be populated.

Output reports useful information from the backup process.

### [](#couchbasebackuprestores-status-pod)couchbasebackuprestores.status.pod

#### [](#constraints-92)Constraints

**Type**: `string`

#### [](#description-92)Description

**DEPRECATED** \- field may no longer be populated.

Pod tells us which pod is running/ran last.

### [](#couchbasebackuprestores-status-repo)couchbasebackuprestores.status.repo

#### [](#constraints-93)Constraints

**Type**: `string`

#### [](#description-93)Description

Repo is where we are currently performing operations.

### [](#couchbasebackuprestores-status-running)couchbasebackuprestores.status.running

#### [](#constraints-94)Constraints

**Required**

**Type**: `boolean`

#### [](#description-94)Description

Running indicates whether a restore is currently being performed.