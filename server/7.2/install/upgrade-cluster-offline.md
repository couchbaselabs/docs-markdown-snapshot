---
title: Upgrade an Offline Cluster
description: A multi-node cluster can most simply be upgraded when entirely
  offline; meaning that it is not serving data.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/upgrade-cluster-offline.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:install:upgrade-cluster-offline.adoc[]
---

[View original HTML](/server/7.2/install/upgrade-cluster-offline.html)

# Upgrade an Offline Cluster

> A multi-node cluster can most simply be upgraded when entirely offline; meaning that it is not serving data. 

## [](#understanding-offline-cluster-upgrade)Understanding Offline Cluster-Upgrade

Offline cluster-upgrade can occur when the cluster is not required to serve data for some period of time. All application-access to the cluster is stopped, and each node in turn is upgraded. Then, the cluster is brought back online, and application-access to it is restored. The page provides step-by-step instructions for upgrading an offline _multi-node_ cluster.

The procedure is presented in three stages, below.

## [](#prepare-the-cluster)Stage One: Prepare the Cluster

Proceed as follows:

1. Stop all applications that access the cluster. Monitor the _disk-write queue_ on each node, to ensure that all data has been persisted to disk. A command of the following form can be used:  
```bash  
curl -s -u '${USERNAME}:${PASSWORD}' ${NODE_HOSTNAME}:${NODE_MANGEMENT_PORT}/pools/default/buckets/${BUCKET}/stats | jq ".op.samples.disk_write_queue[-1]"  
```  
When this command returns `0`, all data has been persisted to disk.
2. Back up the cluster’s user-data. Backup can be performed either with [cbbackupmgr](../backup-restore/enterprise-backup-restore.md) or with the [Backup Service](../learn/services-and-indexes/services/backup-service.md); and should be a _full_ (rather than an incremental) backup.  
For example, to use `cbbackupmgr` to configure an archive and repository for the backup, a command of the following form should be entered:  
```bash  
cbbackupmgr config --archive ${ABS_PATH_TO_ARCHIVE} --repo ${REPO_NAME}  
```  
Here, `ABS_PATH_TO_ARCHIVE` is an absolute path to a filesystem location that will serve as the archive within which the backed up data will reside. The `REPO_NAME` is the name of the repository that will be associated with the location.  
Once the archive and repository have been created, a command such as the following performs a full backup:  
```bash  
cbbackupmgr backup --archive ${ABS_PATH_TO_ARCHIVE} --repo ${REPO_NAME} --cluster ${CLUSTER_ADDRESS} --username ${USERNAME} --password ${PASSWORD} --full-backup  
```  
Here, the `CLUSTER_ADDRESS` is the IP address or domain name of the cluster. The `--full-backup` flag ensures that the backup is indeed a _full_ backup.  
For the equivalent procedure as performed by the Backup Service, see [Run an Immediate Backup](../manage/manage-backup-and-restore/manage-backup-and-restore.md#run-an-immediate-backup).
3. Disable auto-failover (to prevent auto-failover from occuring when individual nodes stop communicating with the rest of the cluster, during their upgrade). Disablement is performed by means of Couchbase-Server [General Settings](../manage/manage-settings/general-settings.md), using the UI, the CLI, or the REST API. Disablement needs to be performed only once, on one node.  
For example, to disable auto-failover by means of the CLI, enter a command of the following form:  
```bash  
couchbase-cli setting-autofailover -c ${NODE_HOSTNAME} -u ${USERNAME} -p ${PASSWORD} --enable-auto-failover 0  
```

## [](#upgrade-each-individual-node)Stage Two: Upgrade Each Individual Node

Each individual node must now be upgraded in turn. Therefore, for each node, proceed as follows:

1. Stop the `couchbase-server.service` service, on the first node that is to be upgraded. Enter the following command:  
```bash  
systemctl stop couchbase-server.service  
```  
This _stops_ the service; and so allows it to be restarted after reboot. Note that, optionally, at this point, the service can also be _disabled_; which prevents it from restarting after reboot. This may be useful if additional tasks, such as OS upgrade, need to be performed. If such disabling is desired, enter the following command:  
```bash  
systemctl disable --now couchbase-server.service  
```  
Note that to disable and/or stop Couchbase Server Community Edition, in these commands, `couchbase-server-community` should be substituted for `couchbase-server`.
2. Manually back up the node’s configuration files. These files reside in `/opt/couchbase/var/lib/couchbase/config`. It is recommended that the path to the backup-location for these files contain the node’s domain name or IP address, to ensure accurate recovery. It is also recommended that the backup-location be on a separate machine.  
Enter a command such as the following;  
```bash  
cp -r /opt/couchbase/var/lib/couchbase/config ${PATH_TO_A_SAFE_LOCATION}/${NODE_IP}_config_files  
```
3. If using Couchbase-provided repositories/PPAs, the Couchbase-Server version should be _unpinned_, to allow it to be upgraded. Proceed as follows, for the appropriate platform:

  * RedHat & Centos
  * Ubuntu & Debian  
By editing the file `/etc/yum/yum.conf`, ensure that the package `couchbase-server` (or the package `couchbase-server-community`, if using Community Edition) is _not excluded_. This means that the package-name must _not_ appear on the list of one or more package-names that follows the `exclude=` statement.  
For example, the line may initially appear as follows:  
```bash  
exclude=couchbase-server  
```  
If so, edit the line so that it appears as follows:  
```bash  
exclude=  
```  
Then, save the file.  
Run the following command (specifying, if using Community Edition, `couchbase-server-community`, rather than `couchbase-server`):  
```bash  
apt-mark unhold couchbase-server  
```
4. Upgrade the Couchbase Server package, using the package manager from the distribution currently running on the cluster.  
If using a Couchbase-provided `yum` repository, enter the following:  
```bash  
yum update couchbase-server  
```  
If Using a Couchbase-provided PPA, enter the following:  
```bash  
apt --only-upgrade install couchbase-server  
```  
If using a downloaded package-archive, enter the command appropriate for the platform, as follows:

  * RedHat & Centos
  * Ubuntu & Debian  
```bash  
yum install ${PATH_TO_RPM_PACKAGE}  
```  
```bash  
dpkg -i ${PATH_TO_DEB_PACKAGE}  
```
5. Enable and start the `couchbase-server` (or `couchbase-server-community`) service. (The package installer may already have performed enablement: however, explicit enablement is nevertheless recommended.)  
Enter the following commands (substituting, if using Community Edition, `couchbase-server-community` for `couchbase-server`).  
```bash  
systemctl enable --now couchbase-server.service  
systemctl is-active --quiet couchbase-server.service || systemctl start couchbase-server.service  
```
6. _Repin_ (or _hold_) future package-upgrades for Couchbase Server, so that none occurs before the administrator’s next, elective, manually driven upgrade. Proceed as follows for the appropriate platform:

  * RedHat & Centos
  * Ubuntu & Debian  
Add the `couchbase-server` (or `couchbase-server-community`) package to the `exclude` section of `/etc/yum/yum.conf`. The line appears as follows:  
```bash  
exclude=couchbase-server  
```  
Run the following command (substituting, if running Community Edition, `couchbase-server-community` for `couchbase-server`):  
```bash  
apt-mark hold couchbase-server  
```
7. Repeat all prior steps in this section, [Upgrade Each Individual Node](#upgrade-each-individual-node), for every other node in the cluster.

## [](#bring-the-cluster-back-online)Stage Three: Bring the Cluster Back Online

Proceed as follows:

1. Wait for the completion of _warmup_, for all _Couchbase_ buckets. Note that this may take some time, if the buckets contain large amounts of data.  
The status of warmup can be checked for each node as follows:  
```bash  
cbstats ${NODE_ADDRESS}:${NODE_KV_PORT} -u ${USERNAME} -p ${PASSWORD} -b ${BUCKET} warmup | grep state  
```  
For example:  
```bash  
/opt/couchbase/bin/cbstats localhost:11210 -u Administrator -p password -b travel-sample warmup | grep state  
```  
When warmup is complete, the command returns the following:  
```bash  
ep_warmup_state:                 done  
```  
Note that _Ephemeral_ buckets do not require warmup. If an Ephemeral bucket is specified in this command, an error is returned.
2. Following warmup, bring the cluster back online, restarting applications.

This concludes the upgrade process for the offline, multi-node cluster.