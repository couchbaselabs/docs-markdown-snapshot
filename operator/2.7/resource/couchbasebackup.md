---
title: CouchbaseBackup Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.7.x/docs/user/modules/ROOT/pages/resource/couchbasebackup.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.7@operator::resource/couchbasebackup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.7/resource/couchbasebackup.html)

# CouchbaseBackup Resource

CouchbaseBackup allows automatic backup of all data from a Couchbase cluster into persistent storage.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseBackup
metadata:
  name: ""
spec:
  autoScaling:
    incrementPercent: 20
    limit: ""
    thresholdPercent: 20
  backoffLimit: 2
  backupRetention: 720h
  data:
    exclude:
    - ""
    include:
    - ""
  defaultRecoveryMethod: none
  ephemeralVolume: false
  failedJobsHistoryLimit: 3
  full:
    schedule: ""
  incremental:
    schedule: ""
  logRetention: 168h
  objectStore:
    endpoint:
      secret: ""
      url: ""
      useVirtualPath: false
    secret: ""
    uri: ""
    useIAM: false
  s3bucket: ""
  services:
    analytics: True
    bucketConfig: True
    bucketQuery: True
    clusterAnalytics: True
    clusterQuery: True
    data: True
    eventing: True
    ftsAliases: True
    ftsIndexes: True
    gsIndexes: True
    users: false
    views: True
  size: 20Gi
  storageClassName: ""
  strategy: full_incremental
  successfulJobsHistoryLimit: 3
  threads: 1
  ttlSecondsAfterFinished: 0
status:
  archive: ""
  backups:
  - full: ""
    incrementals:
    - ""
    name: ""
  capacityUsed: ""
  cronjob: ""
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

## [](#couchbasebackups-apiversion)couchbasebackups.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbasebackups-kind)couchbasebackups.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbasebackups-metadata)couchbasebackups.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbasebackups-metadata-name)couchbasebackups.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbasebackups-metadata-namespace)couchbasebackups.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbasebackups-metadata-labels)couchbasebackups.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbasebackups-metadata-annotations)couchbasebackups.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbasebackups-spec)couchbasebackups.spec

### [](#constraints-8)Constraints

**Required**

**Type**: `object`

### [](#description-8)Description

CouchbaseBackupSpec is allows the specification of how a Couchbase backup is configured, including when backups are performed, how long they are retained for, and where they are backed up to.

### [](#couchbasebackups-spec-autoscaling)couchbasebackups.spec.autoScaling

#### [](#constraints-9)Constraints

**Type**: `object`

#### [](#description-9)Description

AutoScaling allows the volume size to be dynamically increased. When specified, the backup volume will start with an initial size as defined by `spec.size`, and increase as required.

### [](#couchbasebackups-spec-autoscaling-incrementpercent)couchbasebackups.spec.autoScaling.incrementPercent

#### [](#constraints-10)Constraints

**Type**: `integer`

**Default**: `20`

**Minimum**: `0`

#### [](#description-10)Description

IncrementPercent controls how much the volume is increased each time the threshold is exceeded, upto a maximum as defined by the limit. This field defaults to 20 if not specified.

### [](#couchbasebackups-spec-autoscaling-limit)couchbasebackups.spec.autoScaling.limit

#### [](#constraints-11)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-11)Description

Limit imposes a hard limit on the size we can autoscale to. When not specified no bounds are imposed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbasebackups-spec-autoscaling-thresholdpercent)couchbasebackups.spec.autoScaling.thresholdPercent

#### [](#constraints-12)Constraints

**Type**: `integer`

**Default**: `20`

**Minimum**: `0`

**Maximum**: `99`

#### [](#description-12)Description

ThresholdPercent determines the point at which a volume is autoscaled. This represents the percentage of free space remaining on the volume, when less than this threshold, it will trigger a volume expansion. For example, if the volume is 100Gi, and the threshold 20%, then a resize will be triggered when the used capacity exceeds 80Gi, and free space is less than 20Gi. This field defaults to 20 if not specified.

### [](#couchbasebackups-spec-backofflimit)couchbasebackups.spec.backoffLimit

#### [](#constraints-13)Constraints

**Type**: `integer`

**Default**: `2`

#### [](#description-13)Description

Number of times a backup job should try to execute. Once it hits the BackoffLimit it will not run until the next scheduled job.

### [](#couchbasebackups-spec-backupretention)couchbasebackups.spec.backupRetention

#### [](#constraints-14)Constraints

**Type**: `string`

**Default**: `720h`

#### [](#description-14)Description

Number of hours to hold backups for, everything older will be deleted. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbasebackups-spec-data)couchbasebackups.spec.data

#### [](#constraints-15)Constraints

**Type**: `object`

#### [](#description-15)Description

Data allows control over what key-value/document data is included in the backup. By default, all data is included. Modifications to this field will only take effect on the next full backup.

### [](#couchbasebackups-spec-data-exclude)couchbasebackups.spec.data.exclude

#### [](#constraints-16)Constraints

**Type**: `[]string`

**Minimum Items**: `1`

**Pattern (Regular Expression)**: `^(?:[a-zA-Z0-9\-_%]|\\.){1,100}(\.default(\.default)?|\.[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,29}(\.[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,29})?)?$`

#### [](#description-16)Description

Exclude defines the buckets, scopes or collections that are excluded from the backup. When this field is set, it implies that by default everything will be backed up, and data items can be explicitly excluded. You may define an exclusion as a bucket — `my-bucket`, a scope — `my-bucket.my-scope`, or a collection — `my-bucket.my-scope.my-collection`. Buckets may contain periods, and therefore must be escaped — `my\.bucket.my-scope`, as period is the separator used to delimit scopes and collections. Excluded data cannot overlap e.g. specifying `my-bucket` and `my-bucket.my-scope` is illegal. This field cannot be used at the same time as included items.

### [](#couchbasebackups-spec-data-include)couchbasebackups.spec.data.include

#### [](#constraints-17)Constraints

**Type**: `[]string`

**Minimum Items**: `1`

**Pattern (Regular Expression)**: `^(?:[a-zA-Z0-9\-_%]|\\.){1,100}(\.default(\.default)?|\.[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,29}(\.[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,29})?)?$`

#### [](#description-17)Description

Include defines the buckets, scopes or collections that are included in the backup. When this field is set, it implies that by default nothing will be backed up, and data items must be explicitly included. You may define an inclusion as a bucket — `my-bucket`, a scope — `my-bucket.my-scope`, or a collection — `my-bucket.my-scope.my-collection`. Buckets may contain periods, and therefore must be escaped — `my\.bucket.my-scope`, as period is the separator used to delimit scopes and collections. Included data cannot overlap e.g. specifying `my-bucket` and `my-bucket.my-scope` is illegal. This field cannot be used at the same time as excluded items.

### [](#couchbasebackups-spec-defaultrecoverymethod)couchbasebackups.spec.defaultRecoveryMethod

#### [](#constraints-18)Constraints

**Type**: `string`

**Default**: `none`

**Enumerations**: `none, resume, purge`

#### [](#description-18)Description

DefaultRecoveryMethod specifies how cbbackupmgr should recover from broken backup/restore attempts. NOTE: To use the `resume` or `purge` parameters, you will need to install `couchbasebackup` version `1.3.5` or greater. For `couchbasebackup` versions earlier than `1.3.5` only the `none` parameter is supported.

### [](#couchbasebackups-spec-ephemeralvolume)couchbasebackups.spec.ephemeralVolume

#### [](#constraints-19)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-19)Description

EphemeralVolume sets backup to use an ephemeral volume instead of a persistent volume. This is used when backing up to a remote cloud provider, where a persistent volume is not needed.

### [](#couchbasebackups-spec-failedjobshistorylimit)couchbasebackups.spec.failedJobsHistoryLimit

#### [](#constraints-20)Constraints

**Type**: `integer`

**Default**: `3`

**Minimum**: `0`

#### [](#description-20)Description

Amount of failed jobs to keep.

### [](#couchbasebackups-spec-full)couchbasebackups.spec.full

#### [](#constraints-21)Constraints

**Type**: `object`

#### [](#description-21)Description

Full is the schedule on when to take full backups. Used in Full/Incremental and FullOnly backup strategies.

### [](#couchbasebackups-spec-full-schedule)couchbasebackups.spec.full.schedule

#### [](#constraints-22)Constraints

**Required**

**Type**: `string`

#### [](#description-22)Description

Schedule takes a cron schedule in string format.

### [](#couchbasebackups-spec-incremental)couchbasebackups.spec.incremental

#### [](#constraints-23)Constraints

**Type**: `object`

#### [](#description-23)Description

Incremental is the schedule on when to take incremental backups. Used in Full/Incremental backup strategies.

### [](#couchbasebackups-spec-incremental-schedule)couchbasebackups.spec.incremental.schedule

#### [](#constraints-24)Constraints

**Required**

**Type**: `string`

#### [](#description-24)Description

Schedule takes a cron schedule in string format.

### [](#couchbasebackups-spec-logretention)couchbasebackups.spec.logRetention

#### [](#constraints-25)Constraints

**Type**: `string`

**Default**: `168h`

#### [](#description-25)Description

Number of hours to hold script logs for, everything older will be deleted. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbasebackups-spec-objectstore)couchbasebackups.spec.objectStore

#### [](#constraints-26)Constraints

**Type**: `object`

#### [](#description-26)Description

ObjectStore allows for backing up to a remote cloud storage.

### [](#couchbasebackups-spec-objectstore-endpoint)couchbasebackups.spec.objectStore.endpoint

#### [](#constraints-27)Constraints

**Type**: `object`

#### [](#description-27)Description

Endpoint contains the configuration for connecting to a custom Azure/S3/GCP compliant object store. If set will override `CouchbaseCluster.spec.backup.objectEndpoint`See <https://docs.couchbase.com/server/current/backup-restore/cbbackupmgr-cloud.html#compatible-object-stores>.

### [](#couchbasebackups-spec-objectstore-endpoint-secret)couchbasebackups.spec.objectStore.endpoint.secret

#### [](#constraints-28)Constraints

**Type**: `string`

#### [](#description-28)Description

The name of the secret, in this namespace, that contains the CA certificate for verification of a TLS endpoint The secret must have the key with the name "tls.crt".

### [](#couchbasebackups-spec-objectstore-endpoint-url)couchbasebackups.spec.objectStore.endpoint.url

#### [](#constraints-29)Constraints

**Type**: `string`

#### [](#description-29)Description

The host/address of the custom object endpoint.

### [](#couchbasebackups-spec-objectstore-endpoint-usevirtualpath)couchbasebackups.spec.objectStore.endpoint.useVirtualPath

#### [](#constraints-30)Constraints

**Type**: `boolean`

#### [](#description-30)Description

UseVirtualPath will force the AWS SDK to use the new virtual style paths which are often required by S3 compatible object stores.

### [](#couchbasebackups-spec-objectstore-secret)couchbasebackups.spec.objectStore.secret

#### [](#constraints-31)Constraints

**Type**: `string`

#### [](#description-31)Description

ObjStoreSecret must contain two fields, access-key-id, secret-access-key and optionally either region or refresh-token. These correspond to the fields used by cbbackupmgr <https://docs.couchbase.com/server/current/backup-restore/cbbackupmgr-backup.html#optional-2>.

### [](#couchbasebackups-spec-objectstore-uri)couchbasebackups.spec.objectStore.uri

#### [](#constraints-32)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(az|s3|gs)://.{3,}$`

#### [](#description-32)Description

URI is a reference to a remote object store. This is the prefix of the object store and the bucket name. i.e s3://bucket, az://bucket or gs://bucket.

### [](#couchbasebackups-spec-objectstore-useiam)couchbasebackups.spec.objectStore.useIAM

#### [](#constraints-33)Constraints

**Type**: `boolean`

#### [](#description-33)Description

Whether to allow the backup SDK to attempt to authenticate using the instance metadata api. If set, will override `CouchbaseCluster.spec.backup.useIAM`.

### [](#couchbasebackups-spec-s3bucket)couchbasebackups.spec.s3bucket

#### [](#constraints-34)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^s3://[a-z0-9-\.\/]{3,63}$`

#### [](#description-34)Description

**DEPRECATED** \- by spec.objectStore.uri Name of S3 bucket to backup to.

If non-empty this overrides local backup.

### [](#couchbasebackups-spec-services)couchbasebackups.spec.services

#### [](#constraints-35)Constraints

**Type**: `object`

**Default**: `{}`

#### [](#description-35)Description

Services allows control over what services are included in the backup. By default, all service data and metadata are included apart from users. Modifications to this field will only take effect on the next full backup.

### [](#couchbasebackups-spec-services-analytics)couchbasebackups.spec.services.analytics

#### [](#constraints-36)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-36)Description

Analytics enables the backup of analytics data. This field defaults to `true`.

### [](#couchbasebackups-spec-services-bucketconfig)couchbasebackups.spec.services.bucketConfig

#### [](#constraints-37)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-37)Description

BucketConfig enables the backup of bucket configuration. This field defaults to `true`.

### [](#couchbasebackups-spec-services-bucketquery)couchbasebackups.spec.services.bucketQuery

#### [](#constraints-38)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-38)Description

BucketQuery enables the backup of query metadata for all buckets. This field defaults to `true`.

### [](#couchbasebackups-spec-services-clusteranalytics)couchbasebackups.spec.services.clusterAnalytics

#### [](#constraints-39)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-39)Description

ClusterAnalytics enables the backup of cluster-wide analytics data, for example synonyms. This field defaults to `true`.

### [](#couchbasebackups-spec-services-clusterquery)couchbasebackups.spec.services.clusterQuery

#### [](#constraints-40)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-40)Description

ClusterQuery enables the backup of cluster level query metadata. This field defaults to `true`.

### [](#couchbasebackups-spec-services-data)couchbasebackups.spec.services.data

#### [](#constraints-41)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-41)Description

Data enables the backup of key-value data/documents for all buckets. This can be further refined with the couchbasebackups.spec.data configuration. This field defaults to `true`.

### [](#couchbasebackups-spec-services-eventing)couchbasebackups.spec.services.eventing

#### [](#constraints-42)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-42)Description

Eventing enables the backup of eventing service metadata. This field defaults to `true`.

### [](#couchbasebackups-spec-services-ftsaliases)couchbasebackups.spec.services.ftsAliases

#### [](#constraints-43)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-43)Description

FTSAliases enables the backup of full-text search alias definitions. This field defaults to `true`.

### [](#couchbasebackups-spec-services-ftsindexes)couchbasebackups.spec.services.ftsIndexes

#### [](#constraints-44)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-44)Description

FTSIndexes enables the backup of full-text search index definitions for all buckets. This field defaults to `true`.

### [](#couchbasebackups-spec-services-gsindexes)couchbasebackups.spec.services.gsIndexes

#### [](#constraints-45)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-45)Description

GSIndexes enables the backup of global secondary index definitions for all buckets. This field defaults to `true`.

### [](#couchbasebackups-spec-services-users)couchbasebackups.spec.services.users

#### [](#constraints-46)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-46)Description

Users enables the backup of users including their roles and permissions. This is only available for Couchbase Server 7.6 and later. This field defaults to `false`.

### [](#couchbasebackups-spec-services-views)couchbasebackups.spec.services.views

#### [](#constraints-47)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-47)Description

Views enables the backup of view definitions for all buckets. This field defaults to `true`.

### [](#couchbasebackups-spec-size)couchbasebackups.spec.size

#### [](#constraints-48)Constraints

**Type**: `string`

**Default**: `20Gi`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-48)Description

Size allows the specification of a backup persistent volume, when using volume based backup. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbasebackups-spec-storageclassname)couchbasebackups.spec.storageClassName

#### [](#constraints-49)Constraints

**Type**: `string`

#### [](#description-49)Description

Name of StorageClass to use.

### [](#couchbasebackups-spec-strategy)couchbasebackups.spec.strategy

#### [](#constraints-50)Constraints

**Type**: `string`

**Default**: `full_incremental`

**Enumerations**: `full_incremental, full_only, immediate_incremental, immediate_full`

#### [](#description-50)Description

Strategy defines how to perform backups. `full_only` will only perform full backups, and you must define a schedule in the `spec.full` field. `full_incremental`will perform periodic full backups, and incremental backups in between. You must define full and incremental schedules in the `spec.full` and `spec.incremental` fields respectively. Care should be taken to ensure full and incremental schedules do not overlap, taking into account the backup time, as this will cause failures as the jobs attempt to mount the same backup volume. To cause a backup to occur immediately use `immediate_incremental`or `immediate_full` for incremental or full backups respectively. This field default to `full_incremental`. Info: <https://docs.couchbase.com/server/current/backup-restore/cbbackupmgr-strategies.html>.

### [](#couchbasebackups-spec-successfuljobshistorylimit)couchbasebackups.spec.successfulJobsHistoryLimit

#### [](#constraints-51)Constraints

**Type**: `integer`

**Default**: `3`

**Minimum**: `0`

#### [](#description-51)Description

Amount of successful jobs to keep.

### [](#couchbasebackups-spec-threads)couchbasebackups.spec.threads

#### [](#constraints-52)Constraints

**Type**: `integer`

**Default**: `1`

**Minimum**: `0`

#### [](#description-52)Description

How many threads to use during the backup. This field defaults to 1.

### [](#couchbasebackups-spec-ttlsecondsafterfinished)couchbasebackups.spec.ttlSecondsAfterFinished

#### [](#constraints-53)Constraints

**Type**: `integer`

**Minimum**: `0`

#### [](#description-53)Description

Amount of time to elapse before a completed job is deleted.

## [](#couchbasebackups-status)couchbasebackups.status

### [](#constraints-54)Constraints

**Type**: `object`

### [](#description-54)Description

CouchbaseBackupStatus provides status notifications about the Couchbase backup including when the last backup occurred, whether is succeeded or not, the run time of the backup and the size of the backup.

### [](#couchbasebackups-status-archive)couchbasebackups.status.archive

#### [](#constraints-55)Constraints

**Type**: `string`

#### [](#description-55)Description

Location of Backup Archive.

### [](#couchbasebackups-status-backups)couchbasebackups.status.backups

#### [](#constraints-56)Constraints

**Type**: `[]object`

#### [](#description-56)Description

Backups gives us a full list of all backups and their respective repository locations.

### [](#couchbasebackups-status-backups-full)couchbasebackups.status.backups.full

#### [](#constraints-57)Constraints

**Type**: `string`

#### [](#description-57)Description

Full backup inside the repository.

### [](#couchbasebackups-status-backups-incrementals)couchbasebackups.status.backups.incrementals

#### [](#constraints-58)Constraints

**Type**: `[]string`

#### [](#description-58)Description

Incremental backups inside the repository.

### [](#couchbasebackups-status-backups-name)couchbasebackups.status.backups.name

#### [](#constraints-59)Constraints

**Required**

**Type**: `string`

#### [](#description-59)Description

Name of the repository.

### [](#couchbasebackups-status-capacityused)couchbasebackups.status.capacityUsed

#### [](#constraints-60)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-60)Description

CapacityUsed tells us how much of the PVC we are using. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbasebackups-status-cronjob)couchbasebackups.status.cronjob

#### [](#constraints-61)Constraints

**Type**: `string`

#### [](#description-61)Description

**DEPRECATED** \- field may no longer be populated.

Cronjob tells us which Cronjob the job belongs to.

### [](#couchbasebackups-status-duration)couchbasebackups.status.duration

#### [](#constraints-62)Constraints

**Type**: `string`

#### [](#description-62)Description

Duration tells us how long the last backup took. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbasebackups-status-failed)couchbasebackups.status.failed

#### [](#constraints-63)Constraints

**Required**

**Type**: `boolean`

#### [](#description-63)Description

Failed indicates whether the most recent backup has failed.

### [](#couchbasebackups-status-job)couchbasebackups.status.job

#### [](#constraints-64)Constraints

**Type**: `string`

#### [](#description-64)Description

**DEPRECATED** \- field may no longer be populated.

Job tells us which job is running/ran last.

### [](#couchbasebackups-status-lastfailure)couchbasebackups.status.lastFailure

#### [](#constraints-65)Constraints

**Type**: `string`

#### [](#description-65)Description

LastFailure tells us the time the last failed backup failed.

### [](#couchbasebackups-status-lastrun)couchbasebackups.status.lastRun

#### [](#constraints-66)Constraints

**Type**: `string`

#### [](#description-66)Description

LastRun tells us the time the last backup job started.

### [](#couchbasebackups-status-lastsuccess)couchbasebackups.status.lastSuccess

#### [](#constraints-67)Constraints

**Type**: `string`

#### [](#description-67)Description

LastSuccess gives us the time the last successful backup finished.

### [](#couchbasebackups-status-output)couchbasebackups.status.output

#### [](#constraints-68)Constraints

**Type**: `string`

#### [](#description-68)Description

**DEPRECATED** \- field may no longer be populated.

Output reports useful information from the backup\_script.

### [](#couchbasebackups-status-pod)couchbasebackups.status.pod

#### [](#constraints-69)Constraints

**Type**: `string`

#### [](#description-69)Description

**DEPRECATED** \- field may no longer be populated.

Pod tells us which pod is running/ran last.

### [](#couchbasebackups-status-repo)couchbasebackups.status.repo

#### [](#constraints-70)Constraints

**Type**: `string`

#### [](#description-70)Description

Repo is where we are currently performing operations.

### [](#couchbasebackups-status-running)couchbasebackups.status.running

#### [](#constraints-71)Constraints

**Required**

**Type**: `boolean`

#### [](#description-71)Description

Running indicates whether a backup is currently being performed.