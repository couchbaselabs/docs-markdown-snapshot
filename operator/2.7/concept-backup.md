---
title: Couchbase Backup and Restore
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.7/modules/ROOT/pages/concept-backup.adoc
  xref: xref:2.7@operator::concept-backup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.7/concept-backup.html)

# Couchbase Backup and Restore

> The Autonomous Operator provides facilities that allow data to be backed up, restored, and archived in order to aid in cluster disaster recovery. 

## [](#overview)Overview

The Autonomous Operator provides automated backup and restore capabilities through a native integration with the [cbbackupmgr tool](../../server/current/backup-restore/enterprise-backup-restore.md) in Couchbase Server. Automated backup is enabled in the [CouchbaseCluster](resource/couchbasecluster.md) resource (it is _disabled_ by default). When backup is enabled, the Autonomous Operator defaults to a Couchbase-supplied [operator-backup](https://hub.docker.com/r/couchbase/operator-backup) container image that contains [cbbackupmgr](../../server/current/backup-restore/cbbackupmgr.md).

Once automated backup is enabled, individual backup policies can be configured using [CouchbaseBackup](resource/couchbasebackup.md) resources, which define things like _schedule_ and _backup strategy_. Each [CouchbaseBackup](resource/couchbasebackup.md) resource creates one or two Kubernetes [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) resources that will spawn backup jobs according to the given Cron schedule(s). These backup jobs execute a helper script to perform logging and cleanup, as well as launch the [cbbackupmgr](../../server/current/backup-restore/cbbackupmgr.md) utility to perform backup and restore.

For information on configuring automated backup and restore, refer to [Configure Automated Backup and Restore](howto-backup.md).

> [!TIP]
> Because backup policies are configured with a separate resource, you can use [custom resource RBAC](concept-rbac.md) to allow individuals who may not have access to [CouchbaseCluster](resource/couchbasecluster.md) resources to still perform backup administration.

## [](#about-the-operator-backup-image)About the `operator-backup` Image

Each version of Couchbase Server is released with a compatible version of the [cbbackupmgr tool](../../server/current/backup-restore/enterprise-backup-restore.md). This tool is included in the [operator-backup](https://hub.docker.com/r/couchbase/operator-backup) container image that is used by the Autonomous Operator to provide automated backup and restore capabilities.

Whenever the Autonomous Operator gains support for a new version of Couchbase Server, a new and/or compatible version of the [operator-backup](https://hub.docker.com/r/couchbase/operator-backup) image will be made available at the same time that includes a fully compatible version of [cbbackupmgr](../../server/current/backup-restore/cbbackupmgr.md). For a list of compatible images for this release of the Autonomous Operator, refer to [Couchbase Backup and Restore Compatibility](prerequisite-and-setup.md#couchbase-backup-and-restore-compatibility).

> [!IMPORTANT]
> Only the official Couchbase-supplied [operator-backup](https://hub.docker.com/r/couchbase/operator-backup) container image is supported. This image is designed only for use with the Autonomous Operator, and is not meant for any other context.
> 
> In addition, you should ensure that your image source is trusted. The backup image requires access to the Couchbase cluster administrative credentials in order to login and perform collection. Granting these credentials to arbitrary code is potentially harmful.

## [](#important-considerations)Important Considerations

* The Autonomous Operator supports two of the backup strategies available in [cbbackupmgr](../../server/current/backup-restore/cbbackupmgr.md): _Full Only_ and _Full/Incremental_. Complete descriptions and explanations of these strategies can be found in the [cbbackupmgr strategies documentation](../../server/current/backup-restore/cbbackupmgr-strategies.md).
* The Autonomous Operator runs the backup utility in a separate Pod. Where this Pod is scheduled can have implications on backup performance, and can affect whether backup jobs are able to complete within the desired time window.  
You should schedule backup Pods onto Kubernetes nodes that have enough resources to successfully fulfill your backup schedule. It is also recommended that you do not schedule backup Pods onto Kubernetes nodes that host Couchbase cluster Pods, since your Couchbase cluster would be competing for resources with the backup utility. Refer to [Pod Scheduling](howto-backup.md#pod-scheduling) for more information.
* Backup Pods require access permissions that necessitate the creation of `ServiceAccount`, `Role`, and `RoleBinding` resources. Refer to [Grant Access Permissions](howto-backup.md#grant-backup-permissions) for more information.
* You can enable and disable automated backup at any time in the [CouchbaseCluster](resource/couchbasecluster.md) resource. Disabling automated backup does not delete [CouchbaseBackup](resource/couchbasebackup.md) resources. When you re-enabled automated backup, any applicable [CouchbaseBackup](resource/couchbasebackup.md) resources that still exist will continue to be used.
* When your Couchbase cluster is configured with TLS, backups and restores will also occur over TLS to provide end-to-end encryption of your data while in transit.  
> [!IMPORTANT]  
> The [cbbackupmgr](../../server/current/backup-restore/cbbackupmgr.md) tool _does not_ support mutual TLS authentication. If your Couchbase cluster is using mandatory client certificate authentication, the Autonomous Operator, in an effort to keep the backup from failing, will downgrade the connection between the backup Pod and the cluster to _plain text_. In both server-side TLS and optional client certificate authentication modes of operation, the backup will occur over TLS, using basic HTTP authentication.

## [](#additional-resources)Additional Resources

* [Configure Automated Backup and Restore](howto-backup.md)