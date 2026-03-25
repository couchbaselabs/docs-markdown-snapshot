---
title: Configure Automated Backup and Restore
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/howto-backup.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.6@operator::howto-backup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/howto-backup.html)

# Configure Automated Backup and Restore

> You can configure the Autonomous Operator to take periodic, automated backups of your Couchbase cluster with the existing functionality provided by `cbbackupmgr`, as well as being able to trigger automated immediate backups. 

## [](#overview)Overview

This page details how to backup a Couchbase cluster and restore data in the face of disaster. A conceptual overview of using the Autonomous Operator to backup and restore Couchbase clusters can be found in [Couchbase Backup and Restore](concept-backup.md).

The Autonomous Operator supports two of the backup strategies available in `cbbackupmgr`: _Full Only_ and _Full/Incremental_. Complete descriptions and explanations of these strategies can be found in the [cbbackupmgr documentation](../../server/current/backup-restore/cbbackupmgr-strategies.md). The examples on this page assume a backup schedule based on the _Full/Incremental_ strategy for both creating backups and performing restores.

> [!IMPORTANT]
> Backup and restore jobs rely on a shared persistent volume claim (PVC) when in use. On Kubernetes platforms you must specify a value for [couchbaseclusters.spec.security.podSecurityContext.fsGroup](resource/couchbasecluster.md#couchbaseclusters-spec-security-podsecuritycontext-fsgroup) in order for volume permissions to be the same across all jobs. Red Hat OpenShift is not affected by this constraint.
> 
> For further information about setting file system groups see the [persistent volume concepts](concept-persistent-volumes.md#using-storage-classes) page.

## [](#enable-automated-backup)Enable Automated Backup

In order for the Autonomous Operator to manage the automated backup of a cluster, the feature must be enabled in the `CouchbaseCluster` resource.

```yaml
apiVersion: couchbase/v2
kind: CouchbaseCluster
spec:
  backup:
    managed: true (1)
    image: couchbase/operator-backup:1.3.2 (2)
    serviceAccountName: couchbase-backup (3)
```

| **1** | The only required field to enable automated backup is [couchbaseclusters.spec.backup.managed](resource/couchbasecluster.md#couchbaseclusters-spec-backup-managed).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | If the [couchbaseclusters.spec.backup.image](resource/couchbasecluster.md#couchbaseclusters-spec-backup-image) field is left unspecified, then it will be automatically populated with the most recent container image that was available when the installed version of the Autonomous Operator was released. The default image for open source Kubernetes comes from [Docker Hub](https://hub.docker.com/r/couchbase/operator-backup), and the default image for OpenShift comes from the [Red Hat Container Catalog](https://access.redhat.com/containers/#/vendor/couchbase). When running on Red Hat OpenShift, you will want to modify this to use the Red Hat Container Catalog image. The image will be something similar to registry.connect.redhat.com/couchbase/operator-backup:1.3.2 (you can refer to the catalog for the most recent images). If image pull secrets are required to access the image, they can be set explicitly with the [couchbaseclusters.spec.backup.imagePullSecrets](resource/couchbasecluster.md#couchbaseclusters-spec-backup-imagepullsecrets) field or implicitly with a service account specified with the [couchbaseclusters.spec.backup.serviceAccountName](resource/couchbasecluster.md#couchbaseclusters-spec-backup-serviceaccountname) field. |
| **3** | If left unspecified, [couchbaseclusters.spec.backup.serviceAccountName](resource/couchbasecluster.md#couchbaseclusters-spec-backup-serviceaccountname) will default to the value of couchbase-backup. These Kubernetes resources **must** exist, otherwise backup jobs will not have the required permissions to complete successfully. This will be covered in the next [section](#grant-backup-permissions).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### [](#grant-backup-permissions)Grant Backup Permissions

Backup Pods need read-only access to Kubernetes resources such as `Pods`, `CronJobs`, and `Jobs`. They also need write access to Events and the `CouchbaseBackup`/`CouchbaseBackupRestore` custom resources. Without these resources, backup jobs will still run as scheduled, but they will ultimately fail as the pods won’t have the required permissions.

You can use the [cao](tools/cao.md) tool to create the resources that grant the required permissions. The following command creates the necessary resources in the default namespace:

```console
$ bin/cao create backup
```

To create the resources in a custom namespace, use the `-n` flag:

```console
$ bin/cao create backup -n my-namespace
```

To make your own edits to these resources, you can use `cao generate backup` to generate the YAML output instead of creating the resources in Kubernetes immediately.

## [](#configure-backups)Configure Backups

After automated backup is enabled for the cluster, individual backup policies can be configured using `CouchbaseBackup` resources. The following is a very simple configuration with only the minimum required fields set.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseBackup
metadata:
  name: my-backup
spec:
  strategy: full_incremental (1)
  full:
    schedule: "0 3 * * 0" (2)
  incremental:
    schedule: "0 3 * * 1-6" (2)
  size: 20Gi (3)
```

| **1** | Periodic backups require spec.strategy to be either full\_only or full\_incremental                                                                                                                                                                                                                               |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | On detection of the CouchbaseBackup resource, the Autonomous Operator creates the correct cron jobs for the spec.full.schedule and the spec.incremental.schedule. In this example a full backup would be performed at 3:00AM on a Sunday and then an incremental backup on every other day of the week at 3:00AM. |
| **3** | The Autonomous Operator will also create a PersistentVolumeClaim (PVC) to store the backups and logs with the same name that is specified in metadata.name. So if a PVC called "my-backup" does not yet exist in this case, one will be created. This would also happen if for some reason the PVC was deleted.   |

An immediate backup can also be triggered immediately using `CouchbaseBackup` resources with the `immediate_full` or `immediate_incremental` strategies. When the Autonomous Operator detects `CouchbaseBackup` resource with either of these strategies it will attempt to trigger a backup Job immediately. The following is a simple configuration with the minimum required fields set to take an immediate backup.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseBackup
metadata:
  name: my-backup
spec:
  strategy: immediate_full (1)
  size: 20Gi
```

| **1** | Immediate backups require spec.strategy to be either immediate\_full or immediate\_incremental |
| ----- | ---------------------------------------------------------------------------------------------- |

Once you have created a `CouchbaseBackup`, we can check that for the expected behavior by viewing the Operator logs.

* Kubernetes
* OpenShift

```console
$ kubectl logs -f deployments/couchbase-operator
```

```console
$ oc logs deployments/couchbase-operator
```

You should observe that a Persistent Volume Claim and the correct number of cron jobs have been created along with the `CouchbaseBackup` itself. The output should be similar to:

```console
{"level":"info","ts":1587134718.3592374,"logger":"cluster","msg":"Backup Cronjob created","cbbackup":"my-backup","cronjob":"my-backup-incremental"}
{"level":"info","ts":1587134718.3727212,"logger":"cluster","msg":"Backup Cronjob created","cbbackup":"my-backup","cronjob":"my-backup-full"}
{"level":"info","ts":1587134718.3722592,"logger":"cluster","msg":"Backup PVC created","cbbackup":"my-backup"}
{"level":"info","ts":1587134718.3727608,"logger":"cluster","msg":"Backup created","cbbackup":"my-backup"}
```

You can then validate for yourself that these resources exist and check that their details match up with what was defined in the `CouchbaseBackup` configuration.

* Kubernetes
* OpenShift

```console
$ kubectl get cronjob
$ kubectl get job
$ kubectl get pvc
```

```console
$ oc get cronjob
$ oc get job
$ oc get pvc
```

For example, for periodic backups the output of the `cronjobs` should look like:

```console
NAME                        SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
my-backup-full              0 3 * * 0     False     0        <none>          18s
my-backup-incremental       0 3 * * 1-6   False     0        <none>          18s
```

And for immediate backups the jobs should like:

```console
NAME                        COMPLETIONS   DURATION   AGE
my-immediate-backup-full    1/1           20s        17h
```

Any backups that have been triggered should have PVCs with the backup data:

```console
NAME        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
my-backup   Bound    pvc-0c3c717f-e10b-423e-9279-a99edf81019b   5Gi        RWO            standard       14s
```

> [!CAUTION]
> Deleting Persistent Volume Claims or Persistent Volumes will delete the backup data and backup log data permanently.

Once the first Job has been spawned by a backup cron job, the status fields of a `CouchbaseBackup` resource will update, and you can start [monitoring backup progress](#monitor-and-manage-backups).

## [](#restoring-from-a-backup)Restoring From a Backup

Restoring from a backup requires that you create a `CouchbaseBackupRestore` resource.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseBackupRestore
metadata:
  name: my-restore
spec:
  backup: my-backup
  repo: cb-example-2020-02-12T19_00_03
  start:
    int: 1
```

A `CouchbaseBackupRestore` resource behaves differently from a `CouchbaseBackup` resource in that it spawns just a singular, one-time job which attempts to restore the requested backup or range of backups.

In the example above, the `CouchbaseBackupRestore` resource configuration is restoring the first backup in the repository `"cb-example-2020-02-12T19_00_03"`. The first backup in any repository will be a full backup since the Autonomous Operator performs a full backup of the cluster after the creation of each backup repository.

If you don’t know the name of the backup repository that you want to restore from, you can find the name without having to explore the contents of a Persistent Volume Claim by simply referring to the [couchbasebackups.status](resource/couchbasebackup.md#couchbasebackups-status) object of the existing `CouchbaseBackup` resource.

You also have the option to restore a range of backups from the latest backup repository.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseBackupRestore
metadata:
  name: my-restore
spec:
  backup: my-backup
  start:
    str: oldest
  end:
    str: latest
```

In this example above, the Autonomous Operator would restore a range of backups from the latest backup repository. The omission of the `spec.repo` field means that the Autonomous Operator will look for the most recent backup repository.

> [!IMPORTANT]
> Any `CouchbaseBackupRestore` edits performed with `kubectl edit` will not be reflected in the respective `Job` once the `Job` has been created. The `CouchbaseBackupRestore` resource will have to be deleted and created from scratch. When a `CouchbaseBackupRestore` resource is deleted, its associated `Job` and `Pod` resources are deleted immediately.

### [](#additional-backup-options)Additional Backup Options

Backups allow data to be filtered so that you only backup what you need, minimizing storage space and improving performance. Backup options can only be modified on creation of a new backup repository, so when using a full/incremental backup strategy, modifications will be deferred until the next full backup.

Consider the following specification:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseBackup
metadata:
  name: my-backup
spec:
  data:
    include: (1)
    - bucket1
    - bucket1.scope
    - bucket2.scope.collection
    exclude: (2)
    - bucket3
  services: (3)
    analytics: true
    bucketConfig: true
    bucketQuery: true
    clusterAnalytics: true
    clusterQuery: true
    data: true
    eventing: true
    ftsAliases: true
    ftsIndexes: true
    gsIndexes: true
    views: true
  threads: 16 (4)
```

| **1** | [couchbasebackups.spec.data.include](resource/couchbasebackup.md#couchbasebackups-spec-data-include) allows data sources to be explicitly selected. When this field is set, the backup will exclude all data by default, and you have to opt-in to data items being included. Data items cannot alias, e.g. bucket and bucket.scope alias, because latter is contained in the former. This field cannot be specified at the same time as [couchbasebackups.spec.data.exclude](resource/couchbasebackup.md#couchbasebackups-spec-data-exclude).    |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [couchbasebackups.spec.data.exclude](resource/couchbasebackup.md#couchbasebackups-spec-data-exclude) allows data sources to be explicitly excluded. When this field is set, the backup will include all data by default, and you have to opt-out from data items being included. Data items cannot alias, e.g. bucket and bucket.scope alias, because latter is contained in the former. This field cannot be specified at the same time as [couchbasebackups.spec.data.include](resource/couchbasebackup.md#couchbasebackups-spec-data-include). |
| **3** | [couchbasebackups.spec.services](resource/couchbasebackup.md#couchbasebackups-spec-services) allows the selection of what services are backed up. By default all available services are include in the backup, and you have to opt-out.                                                                                                                                                                                                                                                                                                           |
| **4** | [couchbasebackups.spec.threads](resource/couchbasebackup.md#couchbasebackups-spec-threads) allows the number of threads used by the backup to be tailored. Increasing this value improves performance. Ensure any value used here is less than that provided for backup pod CPU resource requests.                                                                                                                                                                                                                                                |

Further details can be found on the [CouchbaseBackup resource reference](resource/couchbasebackup.md).

### [](#additional-restore-options)Additional Restore Options

Additional options from [cbbackupmgr restore](../../server/current/backup-restore/cbbackupmgr-restore.md) may also be specified.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseBackupRestore
metadata:
  name: my-restore
spec:
  backup: my-backup
  repo: cb-example-2020-02-12T19_00_03
  start:
    int: 1
  data:
    include: (1)
    - default
    - peanutbutter
    - princess.caroline
    exclude:
    - horseman
    map: (2)
    - source: default
      target: new-default
    - source: peanutbutter
      target: pickles
    filterKeys: "^cat.*" (3)
  services: (4)
    analytics: true
    bucketConfig: false
    bucketQuery: true
    clusterAnalytics: true
    clusterQuery: true
    data: true
    eventing: true
    ftAlias: true
    ftIndex: true
    gsiIndex: true
    views: true
  threads: 1 (5)
```

| **1** | [couchbasebackuprestores.spec.data.include](resource/couchbasebackuprestore.md#couchbasebackuprestores-spec-data-include): Explicitly restore only the specified list of buckets, scopes and collections. [couchbasebackuprestores.spec.data.exclude](resource/couchbasebackuprestore.md#couchbasebackuprestores-spec-data-exclude): Restore all buckets _except_ the list of specified buckets, scopes and collections. Include and exclude are mutually exclusive and cannot be specified at the same time. Data items cannot alias, e.g. bucket contains bucket.scope, and therefore cannot be defined at the same time.                                                                                                                                                                                                                                                                                                         |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [couchbasebackuprestores.spec.data.map](resource/couchbasebackuprestore.md#couchbasebackuprestores-spec-data-map): Specified when you want to restore a backup to a destination bucket, scope or collection that has a different name than the bucket, scope or collection that was originally backed up. This field requires a pair of fields named source and target. source refers to the name of the bucket, scope or collection to restore from in the backup archive target refers to the name of the existing (renamed) bucket, scope or collection to restore to in the Couchbase cluster Multiple source/target pairs may be specified. Note that this option will only restore data to the Data Service and will not restore the metadata for any other service. Refer to the [cbbackupmgr restore --map-buckets](../../server/current/backup-restore/cbbackupmgr-restore.md#options) documentation for more information. |
| **3** | [couchbasebackuprestores.spec.data.filterKeys](resource/couchbasebackuprestore.md#couchbasebackuprestores-spec-data-filterkeys) allows only those documents whose name matches a regular expression to be restored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **4** | [couchbasebackuprestores.spec.services](resource/couchbasebackuprestore.md#couchbasebackuprestores-spec-services): By default, all data and configuration settings, for all services, are restored to the Couchbase cluster, _apart from bucket configuration settings_. In order to skip restoring a particular service, simply set the service to false (these options correspond to the [cbbackupmgr restore --disable-<service>](../../server/current/backup-restore/cbbackupmgr-restore.md#options) flags). In order to restore bucket configuration settings, set [couchbasebackuprestores.spec.services.bucketConfig](resource/couchbasebackuprestore.md#couchbasebackuprestores-spec-services-bucketconfig) to true (this option corresponds to the [cbbackupmgr restore --enable-bucket-config](../../server/current/backup-restore/cbbackupmgr-restore.md#options) flag).                                                 |
| **5** | [couchbasebackuprestores.spec.threads](resource/couchbasebackuprestore.md#couchbasebackuprestores-spec-threads): An integer that specifies the number of concurrent cbbackupmgr clients to use when restoring data. Refer to the [cbbackupmgr restore --threads](../../server/current/backup-restore/cbbackupmgr-restore.md#options) documentation for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## [](#monitor-and-manage-backups)Monitor and Manage Backups

It’s important to regularly monitor backup performance to ensure you’re backing up all the required data within your desired time window.

For the simplest overview, run `get` commands on the `CouchbaseBackup` resources.

* Kubernetes
* OpenShift

```console
$ kubectl get couchbasebackup my-backup -o yaml
```

```console
$ oc get couchbasebackup my-backup -o yaml
```

> [!TIP]
> The short names `cbbackup` and `cbrestore` are available for `CouchbaseBackup` and `CouchbaseBackupRestore` respectively. So instead of executing `kubectl get couchbasebackup` you can instead write `kubectl get cbbackup`. To find out if any other of your current Kubernetes resources support a short name, run `kubectl api-resources`.

The command output should show the given `CouchbaseBackup` specification and also a [couchbasebackups.status](resource/couchbasebackup.md#couchbasebackups-status) section containing useful information similar to the following output.

```console
status:
  archive: /data/backups
  backups:
  - full: 2020-02-12T15_25_10.712665995Z
    incrementals:
    - 2020-02-12T15_28_11.986341497Z
    - 2020-02-12T15_26_09.875255309Z
    name: cb-example-2020-02-12T15_25_09
  - full: 2020-02-12T15_15_08.443231128Z
    incrementals:
    - 2020-02-12T15_18_12.465643387Z
    - 2020-02-12T15_16_08.037612813Z
    - 2020-02-12T15_24_10.264088039Z
    - 2020-02-12T15_22_11.215924706Z
    name: cb-example-2020-02-12T15_15_07
  capacityUsed: 1.47Gi
  duration: 17s
  job: cbbackup-full-incr-incremental-1587137280
  lastRun: "2020-02-12T15:28:11Z"
  lastSuccess: "2020-02-12T15:28:28Z"
  repo: repo
  running: false
```

Furthermore you can check that the cron jobs have updated and their status fields look correct.

* Kubernetes
* OpenShift

```console
$ kubectl get cronjob
```

```console
$ oc get cronjob
```

```console
NAME                        SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
my-backup-full              0 3 * * 0     False     0        2d              2d
my-backup-incremental       0 3 * * 1-6   False     0        16h             2d
```

* Kubernetes
* OpenShift

```console
$ kubectl get cronjob my-backup-full -o yaml
```

```console
$ oc get cronjob my-backup-full -o yaml
```

And finally we can check that the backup Jobs and their respective pods are there, and there is no more than the set limit specified in [couchbasebackups.spec.failedJobsHistoryLimit](resource/couchbasebackup.md#couchbasebackups-spec-failedjobshistorylimit) and [couchbasebackups.spec.successfulJobsHistoryLimit](resource/couchbasebackup.md#couchbasebackups-spec-successfuljobshistorylimit). These default to 5 and 3 respectively.

* Kubernetes
* OpenShift

```console
$ kubectl get jobs
```

```console
$ oc get jobs
```

```console
NAME                                        COMPLETIONS   DURATION   AGE
cbbackup-full-incr-full-1587138300          1/1           33s        11m
cbbackup-full-incr-incremental-1587138600   1/1           43s        6m8s
```

* Kubernetes
* OpenShift

```console
$ kubectl get pods
```

```console
$ oc get pods
```

```console
NAME                                              READY   STATUS      RESTARTS   AGE
cb-example-0000                                   1/1     Running     0          72m
cb-example-0001                                   1/1     Running     0          72m
cb-example-0002                                   1/1     Running     0          72m
cbbackup-full-incr-full-1587138300-92rfp          0/1     Completed   0          11m
cbbackup-full-incr-incremental-1587138600-vzmd2   0/1     Completed   0          6m5s
couchbase-operator-admission-7ccbd85455-6g64p     1/1     Running     0          73m
couchbase-operator-b6496564f-qpqsb                1/1     Running     0          73m
```

### [](#editing-a-backup-configuration)Editing a Backup Configuration

Only the preexisting schedules and volume size of a [CouchbaseBackup](resource/couchbasebackup.md) resource can be edited. Attempts to edit things like the name or strategy will fail.

### [](#online-backup-volume-resizing)Online Backup Volume Resizing

A Backup PVC that is referenced by an existing [CouchbaseBackup](resource/couchbasebackup.md) resource can be resized _manually_ by the user, or _automatically_ by the Autonomous Operator.

> [!IMPORTANT]
> A Backup PVC can only be resized if its associated StorageClass is configured to allow volume expansion. This means the default StorageClass in your Kubernetes environment should have `allowVolumeExpansion` set to `true`.
> 
> Ensure that the StorageClass is configured to allow volume expansion _before_ creating the [CouchbaseBackup](resource/couchbasebackup.md) resource.

#### [](#manual-backup-volume-resizing)Manual Backup Volume Resizing

To perform a manual resize, simply edit [couchbasebackups.spec.size](resource/couchbasebackup.md#couchbasebackups-spec-size) and change it to a value that is _larger_ than the current size. The resize will then be performed with the next scheduled backup job.

> [!NOTE]
> The underlying StorageClass must be configured to allow volume expansion in order to modify the size of the Backup PVC (as stated [previously](#online-backup-volume-resizing)). Changes to the volume size may go through,but the Autonomous Operator will error until the change is reverted.

#### [](#automated-backup-volume-resizing)Automated Backup Volume Resizing

A [CouchbaseBackup](resource/couchbasebackup.md) resource can be modified to allow the Autonomous Operator to automatically resize the Backup PVC once a specific percentage of space is left.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseBackup
metadata:
  name: my-backup
spec:
  strategy: full_incremental
  full:
    schedule: "0 3 * * 0"
  incremental:
    schedule: "0 3 * * 1-6"
  size: 20Gi (1)
  autoscaling:
    thresholdPercent: 20 (2)
    incrementPercent: 20 (3)
    limit: 100Gi (4)
```

| **1** | [couchbasebackups.spec.size](resource/couchbasebackup.md#couchbasebackups-spec-size) is set to the initial size when the [CouchbaseBackup](resource/couchbasebackup.md) resource is created. Here, the size is set to 20Gi (the default).                                                                                                                                                                                                                                   |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [couchbasebackups.spec.autoScaling.thresholdPercent](resource/couchbasebackup.md#couchbasebackups-spec-autoscaling-thresholdpercent) represents the percentage of free space _remaining_ on the volume at which point a volume expansion will be triggered. Here, the threshold is set to 20 (the default). In this case, if the volume is currently 80 GiB, a volume expansion will be triggered once the used capacity reaches 64 GiB and free space is less than 16 GiB. |
| **3** | [couchbasebackups.spec.autoScaling.incrementPercent](resource/couchbasebackup.md#couchbasebackups-spec-autoscaling-incrementpercent) controls how much the volume is increased each time the threshold is exceeded. Here, the increment is set to 20 (the default). In this case, if the volume is currently 80 GiB when the threshold is reached, the volume will be expanded to 100 GiB.                                                                                  |
| **4** | [couchbasebackups.spec.autoScaling.limit](resource/couchbasebackup.md#couchbasebackups-spec-autoscaling-limit) imposes a hard limit on the size of the Backup PVC, at which point the volume size will no longer be incremented. When this field is not defined, no bounds are imposed.                                                                                                                                                                                     |

> [!NOTE]
> The underlying StorageClass must be configured to allow volume expansion in order to modify the size of the Backup PVC (as stated [previously](#online-backup-volume-resizing)). Changes to the volume size may go through, but the Autonomous Operator will error until the change is reverted.

### [](#deleting-a-backup-configuration)Deleting a Backup Configuration

When a `CouchbaseBackup` resource is deleted, any associated `Cronjob`(s) are deleted. `Jobs` and their respective `Pods` from those `Cronjobs` are orphaned; the number of these resources that are left over is determined by the limits `spec.successfulJobsHistoryLimit` and `spec.failedJobsHistoryLimit`.

If a backup job is running whilst the parent `CouchbaseBackup` is deleted then the job will continue until completion or eventual failure.

### [](#viewing-detailed-logs)Viewing Detailed Logs

If anything goes wrong during a backup job, and backup pods return the `Error` status, detailed logging is stored on the Persistent Volume Claim for the backup. You can access these logs by creating a Kubernetes job that creates a pod that mounts this PVC and then running `kubectl exec` to shell into this pod. From there you can access the logs and backup data directly.

The following is an example file that creates such a Kubernetes job. The job creates a pod and mounts the PVC on the path `/data` as the backup and restore pods themselves would.

```yaml
kind: Job
apiVersion: batch/v1
metadata:
  name: backup-exec
spec:
  template:
    spec:
      containers:
        - name: couchbase-cluster-backup-create
          image: couchbase/operator-backup:1.3.2
          command: ["sleep"]
          args: ["30000"] (1)
          volumeMounts:
            - name: "couchbase-cluster-backup-volume"
              mountPath: "/data" (2)
      volumes:
        - name: couchbase-cluster-backup-volume
          persistentVolumeClaim:
            claimName: my-backup (3)
      restartPolicy: Never
      serviceAccountName: couchbase-backup
```

| **1** | The time in seconds to keep the pod running — make sure you give this argument sufficient time so you are not interrupted by the pod completing and any exec connection shutting down. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The mountPath may be any valid path, but for purposes of consistency it should be set to /data.                                                                                        |
| **3** | The claimName refers to the name of the PVC to be accessed, and also the same name of the CouchbaseBackup resource.                                                                    |

Backups are available to view at `/data/backups` and their respective logs at `/data/scriptlogs`. Inside `/data/scriptlogs` will be three folders, `full_only`, `incremental`, and `restore`. The first two folders correspond to any logs run under the relevant `CouchbaseBackup` strategy and the last folder is for `CouchbaseBackupRestore` operations exclusively.

## [](#advanced-backup-management)Advanced Backup Management

### [](#backup-scheduling)Backup Scheduling

As backups are performed on separate pods you will need to consider careful node scheduling when it comes to these pods in order to avoid performance issues and noisy neighbor problems. The following YAML example builds upon the initial YAML in [Enable Automated Backup](#enable-automated-backup).

```yaml
apiVersion: couchbase/v2
kind: CouchbaseCluster
spec:
  backup:
    managed: true
    image: couchbase/operator-backup:1.3.2
    serviceAccountName: couchbase-backup
    nodeSelector:
      instanceType: large (1)
    resources:
      requests:
        cpu: 100m
        memory: 100Mi (2)
    selector:
      matchLabels:
        cluster: my-cluster (3)
    tolerations: (4)
     - key: app
       operator: Equal
       value: cbbackup
       effect: NoSchedule
```

| **1** | The nodeSelector field defines which Kubernetes nodes the pods running the automated backup process will be constrained to. In this case we have specified that backup pods will be constrained to running on nodes of instanceType large.                                                                                                                                                                                                                                                    |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | If your Kubernetes environment requires it, you can set requests and limits for the pods that run the backup and restore jobs.                                                                                                                                                                                                                                                                                                                                                                |
| **3** | If you have more than one CouchbaseCluster resource deployed in the same namespace, you’ll need to use [resource label selection](concept-label-selection.md) to ensure that CouchbaseBackup and CouchbaseBackupRestore resources get created on the correct cluster. Like with other Couchbase custom resources, this means specifying a label for RBAC resources which matches the corresponding label selector of the CouchbaseCluster resource that you want the resources aggregated to. |
| **4** | Tolerations are applied to pods, and allow (but do not require) the pods to be scheduled onto nodes with matching taints. With taints and tolerations, you can grant backup pods exclusive access to specific nodes. In this example, if we wish to run all backup pods on a dedicated node and isolate them from the rest of the Autonomous Operator pods, we can do this by tainting a node with the key-value of app:cbbackup and defining a matching toleration.                          |

Further reference on all of these fields can be found in the [couchbaseclusters.spec.backup](resource/couchbasecluster.md#couchbaseclusters-spec-backup) resource configuration. For more overall information please see [Couchbase Scheduling and Isolation](#concept-scheduling).

### [](#backup-time-scheduling)Backup Time Scheduling

When deciding on the Cron schedules for the Full/Incremental strategy, you should take care that the schedules are not defined in a way for a potential clash between Full and Incremental backups. For the example given in this documentation and the `cbbackupmgr` documentation, this is obviously very unlikely but in a scenario where a backup is not given enough of a time window to complete, this could cause problems. This particularly common in situations where backups have been scheduled too frequently.

### [](#pod-scheduling)Pod Scheduling

Scheduling of backup and restore jobs is exactly the same as the mechanism used for Couchbase Server pods. The affinity and anti-affinity mechanisms are described in [Couchbase Scheduling and Isolation](concept-scheduling.md).

Backup and restore job affinity can be set, per `CouchbaseCluster`, with the [couchbaseclusters.spec.backup.nodeSelector](resource/couchbasecluster.md#couchbaseclusters-spec-backup-nodeselector) attribute, and toleration of anti-affinity rules can be set with the [couchbaseclusters.spec.backup.tolerations](resource/couchbasecluster.md#couchbaseclusters-spec-backup-tolerations) attribute.

## [](#backup-and-restore-to-a-cloud-store)Backup and Restore to a Cloud Store

If you are running a Couchbase cluster version 6.6.x or higher and using the backup image `operator-backup:1.3.2` or higher, the ability to backup and restore to and from AWS, Azure, and GCP is available.

There are two ways to configure access to a cloud store.

1. Manually through providing credentials via a secret.
2. Automatically by using instance metadata API to grant role access.

### [](#configure-explicit-credentials)Configure Explicit Credentials

When manually providing credentials, a separate `Secret` must be created that holds the credentials required for the cloud store. More information on the individual fields can be found under [cbbackupmgr](../../server/current/backup-restore/cbbackupmgr-backup.md#optional-2).

For AWS S3 three fields are expected in the secret. Region name, access key ID, and secret access key under the keys `region`, `access-key-id` and `secret-access-key`.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: s3-secret
type: Opaque
data:
  region: <aws-region>
  access-key-id: <access key id>
  secret-access-key: <secret access key>
```

For Azure Blob Storage the account name and the account key are expected under the keys `access-key-id` and `secret-access-key`.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: gcp-secret
type: Opaque
data:
  access-key-id: <account name>
  secret-access-key: <account key>
```

For Google Cloud Cloud Storage a client id, client secret and refresh token are expected under the keys `access-key-id`, `secret-access-key` and `refresh-token`.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: s3-secret
type: Opaque
data:
  access-key-id: <client id>
  secret-access-key: <client secret>
  refresh-token: <refresh-token>
```

In your `CouchbaseBackup` and `CouchbaseBackupRestore` object, you will need to reference this secret so the Operator knows where to extract the credentials from.

```yaml
apiVersion: couchbase/v2
kind: CouchbaseBackup
spec:
  ...
  objectStore:
    secret: cloud-secret
    uri: [az|s3|gcp]://example
```

### [](#configure-instance-metadata-authentication)Configure Instance Metadata Authentication

To allow backup to automatically use the instance metadata API for authentication, enable the [couchbasebackups.spec.objectStore.useIAM](resource/couchbasebackup.md#couchbasebackups-spec-objectstore-useiam) parameter. By default this is disabled. When using Azure and GCP this is all that’s required, for AWS a secret with the region key set must be provided.

```yaml
apiVersion: couchbase/v2
kind: CouchbaseBackup
spec:
  ...
  objectStore:
    useIAM: true
    secret: s3-region-secret
    uri: s3://example-bucket
```

#### [](#aws)AWS

When using AWS, if you have attached the IAM Role to an EKS node directly then this is sufficient configuration. If you have [setup IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html), the role `ARN` annotation must be applied to the backup service account either manually or when running `cao` using `cao create backup --iam-role-arn arn:aws:iam::<ACCOUNT_ID>:role/<IAM_ROLE_NAME>`

### [](#gcp)GCP

Applications running on a GKE cluster will attempt to use the default Compute Engine service account. To provide more granular control use Workload Identity. For how to setup Workload Identity with GCP follow [Use Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)

By default the service account to annotate will be `couchbase-backup`.

### [](#azure)Azure

Workload Identity support is not yet available.

### [](#configure-cloud-store-backup)Configure Cloud Store Backup

The cloud store that we wish to hold backups needs to be specified in the desired `CouchbaseBackup` and `CouchbaseBackupRestore` CRDs. Note that the prefix must be either `s3://`, `gs://`, or `az://`, otherwise the Admission Controller will not allow the creation of the CRD.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseBackup
metadata:
  name: my-backup
spec:
  strategy: full_incremental
  full:
    schedule: "0 3 * * 0"
  incremental:
    schedule: "0 3 * * 1-6"
  size: 20Gi
  objectStore:
    uri: s3://my-backup-bucket
```

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseBackupRestore
metadata:
  name: my-restore
spec:
  backup: my-backup
  start:
    str: oldest
  end:
    str: latest
  objectStore:
    uri: s3://my-backup-bucket
```

Please note that operations involving remote cloud stores take more time to complete in comparison to regular backup to PVCs so please bear this in mind when configuring your automated backup schedules.

> [!IMPORTANT]
> Backing up to cloud store still requires a local PVC with enough space for [a staging folder](../../server/current/backup-restore/cbbackupmgr-cloud.md#the-staging-directory), where files will be stored locally first before being uploaded to the remote cloud store. Please note that cleanup schedules will also apply to the local PVC as well as the remote cloud store.
> 
> The `staging` folder does not need to be created manually by the user.

### [](#backup-and-restore-to-compatible-cloud-object-stores)Backup and Restore to Compatible Cloud Object Stores

If you are using Couchbase Operator version 2.4.0 or higher, and Couchbase Operator Backup 1.3.2 version or higher, the ability to backup/restore using a compatible cloud store is available. Please see [Compatible Object Stores](../../server/current/backup-restore/cbbackupmgr-cloud.md#compatible-object-stores) for limitations.

Users wishing to use a compatible store should set [couchbasebackups.spec.objectStore.endpoint.url](resource/couchbasebackup.md#couchbasebackups-spec-objectstore-endpoint-url) to the host/address of the object store.

Optionally, [couchbasebackups.spec.objectStore.endpoint.secret](resource/couchbasebackup.md#couchbasebackups-spec-objectstore-endpoint-secret) can be set to the name of the secret containing the CA certificate the compatible object endpoint is using.

For example: to use Minio, a S3 compatible API.

```yaml
apiVersion: couchbase/v2
kind: CouchbaseBackup
spec:
  strategy: full_incremental
  full:
    schedule: "0 3 * * 0"
  incremental:
    schedule: "0 3 * * 1-6"
  size: 20Gi
  objectStore:
    secret: s3-secret
    uri: s3://example-bucket
    endpoint:
      url: https://minio.minio (1)
      secret: my-tls-secret (2)
      useVirtualPath: false (3)
```

| **1** | The only required parameter for using a custom object endpoint.                                                                                                                                      |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Only required if the custom object store is using a custom CA certificate for communication                                                                                                          |
| **3** | Only required if the custom object store uses virtual-hosted style addressing instead of path-style addressing. e.g <https://bucket.s3.amazonaws.com/file> vs <https://s3.amazonaws.com/bucket/file> |

Where `my-tls-secret` contains the certificate of the endpoint, similarly to below.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-tls-secret
type: kubernetes.io/tls
data:
  tls.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1J...
```

### [](#backup-and-restore-with-ephemeral-staging)Backup and Restore with Ephemeral Staging

If you are using Couchbase Operator version 2.4.0 or higher, and Couchbase Operator Backup 1.3.2 version or higher, the ability to backup/restore using a [generic ephemeral volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes) volume is available. This can only be used when backing up or restoring from a remote cloud store and may be useful for high availability setups. To enable ephemeral staging volumes for backup set [couchbasebackups.spec.ephemeralVolume](resource/couchbasebackup.md#couchbasebackups-spec-ephemeralvolume) to true, defaults to false. Both [couchbasebackups.spec.storageClassName](resource/couchbasebackup.md#couchbasebackups-spec-storageclassname) and [couchbasebackups.spec.size](resource/couchbasebackup.md#couchbasebackups-spec-size) will apply to the ephemeral PVC.

> [!NOTE]
> When enabled, the backup PVC will share it’s lifecycle with the backup/restore pod, and will not be removed until the pod is removed. It may be useful to tweak [couchbasebackups.spec.failedJobsHistoryLimit](resource/couchbasebackup.md#couchbasebackups-spec-failedjobshistorylimit) and [couchbasebackups.spec.successfulJobsHistoryLimit](resource/couchbasebackup.md#couchbasebackups-spec-successfuljobshistorylimit) to reduce the number of extraneous ephemeral volumes.

```yaml
apiVersion: couchbase/v2
kind: CouchbaseBackup
spec:
  strategy: full_incremental
  full:
    schedule: "0 3 * * 0"
  incremental:
    schedule: "0 3 * * 1-6"
  size: 20Gi
  objectStore:
    secret: s3-secret
    uri: s3://example-bucket
  ephemeralVolume: true
```

When restoring, if a backup PVC is not found, an ephemeral volume will be used instead. To change either the size of this volume or the storage class use [couchbasebackuprestores.spec.stagingVolume.size](resource/couchbasebackuprestore.md#couchbasebackuprestores-spec-stagingvolume-size) and [couchbasebackuprestores.spec.stagingVolume.storageClassName](resource/couchbasebackuprestore.md#couchbasebackuprestores-spec-stagingvolume-storageclassname) respectively.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseBackupRestore
metadata:
  name: my-restore
spec:
  backup: my-backup
  start:
    str: oldest
  end:
    str: latest
  objectStore:
    uri: s3://my-backup-bucket
  stagingVolume:
    size: 20Gi
    storageClassName: "default"
```