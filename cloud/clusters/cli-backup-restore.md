---
title: Back Up and Restore with Command Line Tools
description: Use Couchbase command line tools to manage ad hoc backups.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/cli-backup-restore.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/clusters/cli-backup-restore.html)

# Back Up and Restore with Command Line Tools

> Use Couchbase command line tools to manage ad hoc backups. 

You can use the `cbbackupmgr` command line tool included with Couchbase Server with a Couchbase Capella cluster. The command line tools are available as a separate package.

Use `cbbackupmgr` to back up and restore data across multiple Capella clusters, either in development or production environments. For more information about `cbbackupmgr`, see [cbbackupmgr](../../server/current/backup-restore/cbbackupmgr.md) in the Couchbase Server documentation.

For data migration between Couchbase clusters, [Cross Data Center Replication (XDCR)](xdcr/xdcr.md) is generally recommended. When XDCR cannot be used, the recommended method is to use `cbbackupmgr backup` and `cbbackupmgr restore`. Using cbexport and cbimport to migrate data from a Couchbase bucket that holds Sync Gateway data can cause the data to be corrupted.

## [](#prerequisites)Prerequisites

* cbbackupmgr version 7.6 or later
* cbbackupmgr version 7.2

All procedures and examples on this page assume the following:

* You have [configured cluster access](#clusters:manage-cluster-users.adoc) by creating cluster access credentials. You’ll need the username and password for the cluster credentials to connect to the cluster.
* You have [added your IP address](allow-ip-address.md) to the cluster’s list of allowed IPs.
* You have [downloaded your security certificate](../get-started/create-account.md#next-steps) for your cluster.
* You have [downloaded and installed](../reference/command-line-tools.md) the command line tools package.

All procedures and examples on this page assume the following:

* You have [configured cluster access](manage-database-users.md) by creating cluster access credentials. You’ll need the username and password for the cluster credentials to connect to the cluster.
* You have [added your IP address](allow-ip-address.md) to the cluster’s list of allowed IPs.
* You have [downloaded your security certificate](../get-started/create-account.md#next-steps) for your cluster.
* You have [downloaded and installed](../reference/command-line-tools.md) the command line tools package.
* You have set the following `--disable` options when you created your repository:  
`--disable-analytics`  
`--disable-cluster-analytics`  
`--disable-bucket-query`  
`--disable-cluster-query`

## [](#backup-and-restore-examples)Backup and Restore Examples

> [!TIP]
> For full examples, see [cbbackupmgr](../../server/current/backup-restore/cbbackupmgr.md) in the Couchbase Server documentation.

For production environments, use the secure `--cacert <cert_file>` option shown in the examples. For development environments, replace `--cacert <cert_file>` with `--no-ssl-verify`.

Use the `cbbackupmgr backup` and `cbbackupmgr restore` commands to back up and restore your Capella cluster.

* cbbackupmgr version 7.6 or later
* cbbackupmgr version 7.2

Use the `--capella` option to disable the backup or restore of data that cannot be read or written by your Capella cluster access credentials.

```console
$ cbbackupmgr config --archive /home/couchbase/backups --repo capella_db1 --capella
```

Back up all buckets

```console
$ cbbackupmgr backup --archive /home/couchbase/backups --repo capella_db1 --cluster couchbases://cb.zjhxs-12ab3cd4e5.cloud.couchbase.com --username dbuser --password '******' --cacert /root/capella.pem --full-backup --threads 4
```

To only restore `mybucket1` data, and restore it to bucket `newbucket1`:

```console
$ cbbackupmgr restore --archive /home/couchbase/backups --repo capella_db1 --cluster couchbases://cb.zjhxs-12ab3cd4e5.cloud.couchbase.com --username dbuser --password '******' --cacert /root/capella.pem --include-data mybucket1 --map-data mybucket1=newbucket1 --threads 4
```

For production environments, use the secure `--cacert <cert_file>` option shown in the examples. For development environments, replace `--cacert <cert_file>` with `--no-ssl-verify`.

Use --disable options to disable backup or restore of data that cannot be read or written by your Capella cluster access credentials.

With Capella clusters running Couchbase Server 7.2, use the following `--disable` options with cbbackupmgr config to configure the backup repository:

```console
--disable-analytics --disable-cluster-analytics --disable-bucket-query --disable-cluster-query
```

> [!WARNING]
> If you did not set these `--disable` options when you created your repository, you must add them to the `cbbackupmgr restore` command when you restore a backup form your repository to Capella.

If you’re restoring data backed up from a self-managed cluster to a Capella cluster with `cbbackupmgr restore`, use `--disable-views`. Capella clusters do not support [views](#7.1@server:learn:views/views-basics.adoc).

If you want to restore a backup of the `beer-sample` and `gamesim-sample` data sets, you must use `--disable-views`.

```console
$ cbbackupmgr config --archive /home/couchbase/backups --repo capella_db1 --disable-eventing --disable-analytics --disable-cluster-analytics --disable-bucket-query --disable-cluster-query
```

Back up all buckets

```console
$ cbbackupmgr backup --archive /home/couchbase/backups --repo capella_db1 --cluster couchbases://cb.zjhxs-12ab3cd4e5.cloud.couchbase.com --username dbuser --password '******' --cacert /root/capella.pem --full-backup --threads 4
```

To only restore `mybucket1` data, and restore it to bucket `newbucket1`:

```console
$ cbbackupmgr restore --archive /home/couchbase/backups --repo capella_db1 --cluster couchbases://cb.zjhxs-12ab3cd4e5.cloud.couchbase.com --username dbuser --password '******' --cacert /root/capella.pem --include-data mybucket1 --map-data mybucket1=newbucket1 --threads 4
```

## [](#backup-free-cluster)Back up a Free Tier Capella Operational Cluster and Restore to a Paid Operational Cluster

This example uses `cbbackupmgr` CLI to migrate data from a free tier operational cluster to a paid operational cluster.

### [](#back-up-a-free-tier-operational-cluster)Back Up a Free Tier Operational Cluster

To configure the `cbbackupmgr` archive repository to hold the backup:

* cbbackupmgr version 7.6 or later
* cbbackupmgr version 7.2

```console
$ cbbackupmgr config --archive /home/couchbase/backups --repo capella_free --capella
```

To back up a free tier Capella operational cluster:

```console
$ cbbackupmgr backup --archive /home/couchbase/backups --repo capella_free -c couchbases://cb.ubibrahu6aizk5rm.cloud.couchbase.com -u freeuser -p '******' --cacert /root/capella.pem --full-backup --threads 2
```

```console
$ cbbackupmgr config --archive /home/couchbase/backups --repo capella_free --disable-analytics --disable-cluster-analytics --disable-bucket-query --disable-cluster-query --disable-views
```

To backup a free tier Capella cluster:

```console
$ cbbackupmgr backup --archive /home/couchbase/backups --repo capella_free -c couchbases://cb.ubibrahu6aizk5rm.cloud.couchbase.com -u freeuser -p '******' --cacert /root/capella.pem --full-backup --threads 2
```

### [](#restore-to-a-paid-provisioned-cluster)Restore to a Paid Provisioned Cluster

Make sure you have created the Couchbase buckets to restore to your paid provisioned cluster. Cluster access credentials do not have privileges to create a bucket, so you cannot use the `cbbackupgmr restore` option `--auto-create-buckets` when restoring to a Capella cluster.

To restore to a paid provisioned cluster:

* cbbackupmgr version 7.6 or later
* cbbackupmgr version 7.2

```console
$ cbbackupmgr restore --archive /home/couchbase/backups --repo capella_free -c couchbases://cb.20xa2skdftoygjxe.cloud.couchbase.com -u dbuser -p '******' --cacert /root/capella.pem --capella
```

The `--purge` option cleans up restore progress information from the previous restore attempt. Add the `--purge` option to the restore command to rerun the restore if you get an error at the start of the restore.

```console
$ cbbackupmgr restore --archive /home/couchbase/backups --repo capella_free -c couchbases://cb.20xa2skdftoygjxe.cloud.couchbase.com -u dbuser -p '******' --cacert /root/capella.pem --disable-analytics --disable-cluster-analytics --disable-bucket-query --disable-cluster-query --disable-views
```

You do not need to use the same disable options again during the restore because you used them when configuring the archive repository. There may be cases where you may not know how the backup was done.

The `--purge` option cleans up restore progress information from the previous restore attempt. Add the `--purge` option to the restore command to rerun the restore if you get an error at the start of the restore.

See [Allowed IPs Tips](#allowed-ips-tips) and [Restore Tips](#restore-tips) for more restoring tips.

### [](#build-indexes)Build Indexes

Index definitions are restored but not built.

To build the indexes in your cluster:

1. Open your cluster in the Capella UI.
2. Go to **Data Tools** **Indexes**.
3. Build the indexes that are in a "Created" state.

## [](#backup-a-self-managed-cluster-and-restore-to-a-capella-provisioned-cluster)Backup a Self-Managed Cluster and Restore to a Capella Provisioned Cluster

This example uses `cbbackupmgr` CLI to migrate data from a self-managed cluster to a provisioned cluster.

A self-managed cluster can be either an Enterprise or Community Edition cluster. If you’re using the Community Edition of Couchbase Server, you need to use the `cbbackupmgr` CLI from the command line tools package to restore to the Capella provisioned cluster. You can also use the `cbbackupmgr` CLI from the command line tools package for backup.

### [](#backup-a-self-managed-cluster)Backup a Self-Managed Cluster

You can backup a self-managed cluster or use an existing backup. The example below is when you do not have an existing backup.

To configure the `cbbackupmgr` archive repository to hold the backup:

```console
$ cbbackupmgr config --archive /home/couchbase/backups --repo repo_mydb
```

To backup a self-managed cluster:

```console
$ cbbackupmgr backup --archive /home/couchbase/backups --repo repo_mydb -c localhost -u Administrator -p '******'
```

### [](#restore-to-a-paid-provisioned-cluster-2)Restore to a Paid Provisioned Cluster

If your self-managed cluster is using the Community Edition Couchbase Server, you must use the `cbbackupmgr` CLI from the command line tools package to restore to the Capella provisioned cluster.

Ensure you have created the Couchbase buckets to restore to your paid provisioned cluster. Capella cluster access credentials do not have privileges to create a bucket, so you cannot use the `cbbackupgmr restore` option `--auto-create-buckets` when restoring to a Capella cluster.

To restore to a paid provisioned cluster:

```console
$ cbbackupmgr restore --archive /home/couchbase/backups --repo repo_mydb -c couchbases://cb.eqwqztkw5e5kf6l.cloud.couchbase.com --cacert /root/capella.pem -u dbuser -p '******' --disable-analytics --disable-cluster-analytics --disable-bucket-query --disable-cluster-query --disable-views
```

> [!TIP]
> While this example works with all `cbbackupmgr` versions, when using `cbbackupmgr` version 7.6 or later, you can use `--capella` instead of the `--disable-analytics` `--disable-cluster-analytics`, `--disable-bucket-query`, `--disable-cluster-query`, and `--disable-views` options.

The `--purge` option cleans up restore progress information from the previous restore attempt. Add the `--purge` option to the restore command to rerun the restore if you get an error at the start of the restore.

See [Allowed IPs Tips](#allowed-ips-tips) and [Restore Tips](#restore-tips) for more restoring tips.

### [](#build-indexes-2)Build Indexes

Index definitions are restored but not built.

To build the indexes in your cluster:

1. Open your cluster in the Capella UI.
2. Go to **Data Tools** **Indexes**.
3. Build the indexes that are in a "Created" state.

## [](#allowed-ips-tips)Allowed IPs Tips

If you’re running `cbbackupmgr` CLI from a VPC-peered environment, the Capella connection string may resolve to a private IP address in your environment. In this situation, you do not need to add the IP address of the machine you’re running `cbbackupmgr` on to the Capella cluster’s list of allowed IPs.

If you have a private endpoint set up in your Capella provisioned cluster, and you’re using the Capella private endpoint DNS name to connect, you do not need to add the IP address of the machine you’re running `cbbackupmgr` on to the list of allowed IPs.

Example private endpoint DNS name connection:  
`couchbases://private-endpoint.iml6stsfy4njxkx0.cloud.couchbase.com`

## [](#restore-tips)Restore Tips

The `--purge` option cleans up restore progress information from the previous restore attempt.

Add the `--purge` option to the restore command to rerun the restore if you get an error at the start of the restore because you omitted to do the following:

* Create the buckets in the provisioned cluster.
* Create the cluster access credential.
* Specify the certificate option.

If the restore process is running, and gets interrupted due to a temporary network issue, try restoring again from where you left off using the `--resume` option.

Other specific restore options are shown in the following table:

| Option          | Description                                                                                                                                                                                                             | Example                                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| \--map-data     | Restore to different bucket names.                                                                                                                                                                                      | \--map-data oldbucket1=newbucket1,oldbucket2=newbucket2   |
| \--include-data | Restore only specific buckets, scopes, and collections.                                                                                                                                                                 | \--include-data bucket1.scope1,bucket2.scope2.collection3 |
| \--exclude-data | Exclude specific buckets, scopes, and collections from the restore.                                                                                                                                                     | \--exclude-data bucket2.scope1                            |
| \--threads      | Specify the number of concurrent clients to use during backup or restore. The default is 1\. More clients means more resource usage. The value should not exceed the number of CPUs on the machine running cbbackupmgr. | \--threads 4                                              |

There are other `cbbackupmgr restore` options. For example, if the backup you’re restoring also includes [Search indexes](../search/search.md), you may want to restore the data first, followed by restoring the Search indexes. If you restore the data and the Search indexes concurrently, the restore starts by creating the Search indexes, followed by the restore data, which puts a very high load on the Search nodes.

GSI indexes do not have the same issue as the Search indexes because they’re restored deferred. The index definitions are restored, but the indexes are not built. You must build the GSI indexes manually after the restore completes.

To disable restoring Search indexes, add the following disable options to your `cbbackupmgr restore` command:  
`--disable-ft-indexes and --disable-ft-alias`

Example:

```console
$ cbbackupmgr restore --archive /home/couchbase/backups --repo repo_mydb -c couchbases://cb.eqwqztkw5e5kf6l.cloud.couchbase.com --cacert /root/capella.pem -u dbuser -p '******' --disable-analytics --disable-cluster-analytics --disable-bucket-query --disable-cluster-query --disable-views --disable-ft-indexes --disable-ft-alias
```

After restoring your data, GSI indexes, and eventing functions, to restore the Search indexes by adding the disable options for data, GSI indexes, and eventing, run another `cbbackupmgr restore` command:  
`--disable-data --disable-gsi-indexes --disable-eventing`

Example:

```console
$ cbbackupmgr restore --archive /home/couchbase/backups --repo repo_mydb -c couchbases://cb.eqwqztkw5e5kf6l.cloud.couchbase.com --cacert /root/capella.pem -u dbuser -p '******' --disable-analytics --disable-cluster-analytics --disable-bucket-query --disable-cluster-query --disable-views --disable-data --disable-gsi-indexes --disable-eventing
```