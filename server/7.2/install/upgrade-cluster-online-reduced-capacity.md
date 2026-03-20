---
title: Upgrade a Reduced-Capacity, Online Cluster
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/upgrade-cluster-online-reduced-capacity.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:install:upgrade-cluster-online-reduced-capacity.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/install/upgrade-cluster-online-reduced-capacity.html)

# Upgrade a Reduced-Capacity, Online Cluster

> A cluster can be upgraded while still online, without additional nodes required — provided that it is permitted to serve data at reduced-capacity, for the duration of the cluster-upgrade. 

## [](#online-upgrade-with-reduced-capacity)Understanding Reduced-Capacity Upgrade

The context and overall requirements for upgrading a live cluster without the introduction of one or more additional nodes are described in [Upgrade-Procedure Selection](upgrade-procedure-selection.md): this fully explains the node-by-node upgrade of the cluster, using _swap rebalance_ to minimize overhead. It also explains how, if additional nodes are not available, the procedure can be completed with no more than the existing cluster-nodes, provided that the cluster can perform acceptably at reduced capacity, during the upgrade.

The precise steps for this _reduced-capacity_ procedure are provided on this page, below. A full understanding of the information in [Upgrade-Procedure Selection](upgrade-procedure-selection.md) should be acquired, before proceeding. The procedure assumes that:

* The cluster to be upgraded must continue to serve data throughout the cluster-upgrade process.
* No additional node is available, to act as a _spare_ node. Therefore, a spare node must be _created_; by withdrawal of a node from the cluster — thereby reducing the capacity of the cluster.
* During the cluster-upgrade process, _swap_ nodes and _upgraded_ nodes will be introduced to the cluster by the _node-addition_ procedure; while _failed over spare nodes_ and _nodes to be upgraded_ will be withdrawn from the cluster by means of the _node removal_ and _swap rebalance_ procedures.  
For information on node-addition, see [Clusters](../learn/clusters-and-availability/nodes.md#clusters). For information on node-removal, see [Removal](../learn/clusters-and-availability/removal.md). For information on _swap rebalance_, see [Swap Rebalance](upgrade-procedure-selection.md#swap-rebalance).
* Nodes will be upgraded _one at a time_.

The overall procedure is described in six stages, below.

## [](#prepare-the-cluster)Stage One: Prepare the Cluster

Back up all cluster-data. This can be performed either with [cbbackupmgr](../backup-restore/enterprise-backup-restore.md) or with the [Backup Service](../learn/services-and-indexes/services/backup-service.md); and should be a _full_ (rather than an incremental) backup.

For example, to use `cbbackupmgr` to configure an archive and repository for the backup, a command of the following form should be entered:

```bash
cbbackupmgr config --archive ${ABS_PATH_TO_ARCHIVE} --repo ${REPO_NAME}
```

Here, `ABS_PATH_TO_ARCHIVE` is an absolute path to a filesystem location that will serve as the archive within which the backed up data will reside. The `REPO_NAME` is the name of the repository that will be associated with the location.

Once the archive and repository have been created, a command such as the following performs a full backup:

```bash
cbbackupmgr backup --archive ${ABS_PATH_TO_ARCHIVE} --repo ${REPO_NAME} \
--cluster ${CLUSTER_ADDRESS} --username ${USERNAME} --password ${PASSWORD} \
--full-backup
```

Here, the `CLUSTER_ADDRESS` is the IP address or domain name of the cluster that is being backed up. The `--full-backup` flag ensures that the backup is indeed a _full_ backup.

For the equivalent procedure as performed by the Backup Service, see [Run an Immediate Backup](../manage/manage-backup-and-restore/manage-backup-and-restore.md#run-an-immediate-backup).

## [](#remove-a-node)Stage Two: Remove a Node

Remove a node from the cluster. This node will function as a _spare_ node; allowing _swap rebalance_ to be performed on each successive node to be upgraded; and in consequence, the cluster will continue to serve data with reduced capacity. For information, see [Using Spare Nodes](upgrade-procedure-selection.md#using-spare-nodes).

For examples of removing a node, see [Remove a Node and Rebalance](../manage/manage-nodes/remove-node-and-rebalance.md). To remove a node with the Couchbase CLI, a command such as the following can be used:

```bash
couchbase-cli rebalance -c ${CLUSTER_NODE_HOSTNAME_OR_IP} \
-u ${USERNAME} -p ${PASSWORD} \
--server-remove ${TARGET_NODE_HOSTNAME_OR_IP}
```

Here, the `CLUSTER_NODE_HOSTNAME_OR_IP` is the IP address or domain name of any node in the cluster. The `NODE_HOSTNAME_OR_IP` is the IP address or domain name of the node that is to be removed from the cluster.

For a full description of steps whereby nodes can be removed from the cluster — using the UI, CLI, and REST API — see [Remove a Node and Rebalance](../manage/manage-nodes/remove-node-and-rebalance.md).

From this point until the end of the cluster-upgrade process, the online cluster continues to serve data with its current number of nodes, which is one less than previously.

## [](#upgrade-the-removed-node)Stage Three: Upgrade the Removed Node

Upgrade the node that has just been removed, by proceeding as follows:

1. Stop the `couchbase-server.service` service, on the node. Enter the following command:  
```bash  
systemctl stop couchbase-server.service  
```  
This _stops_ the service; and so allows it to be restarted after reboot. Note that, optionally, at this point, the service can also be _disabled_; which prevents it from restarting after reboot. This may be useful if additional tasks, such as OS upgrade, need to be performed. If such disabling is desired, enter the following command:  
```bash  
systemctl disable --now couchbase-server.service  
```
2. Back up the configuration files for the removed node. On a Linux system, these files are to be found in `/opt/couchbase/var/lib/couchbase/config`. Ideally, these should be backed up onto a different machine. The command takes the following form:  
```bash  
cp -r /opt/couchbase/var/lib/couchbase/config ${PATH_TO_A_SAFE_LOCATION}/${NODE_IP}_config_files  
```
3. Uninstall `couchbase-server` and its dependencies from the removed node. Enter the command that is appropriate for the platform. Note that the following examples remove _Enterprise Edition_ of Couchbase Server: to remove _Community Edition_, specify `couchbase-server-community` (instead of `couchbase-server`).

  * RedHat & Centos
  * Ubuntu & Debian  
```bash  
yum autoremove couchbase-server  
```  
```bash  
apt autoremove --purge couchbase-server  
```
4. Manually remove files from `/opt/couchbase`. This folder contains configuration files for the previous server-version; which need to be overwritten by configuration files for the new version. If the administrator has manually included in this folder any files that were not provided by Couchbase Server, and need to be retained, these should be individually identified and backed up with with [cbbackupmgr](../backup-restore/enterprise-backup-restore.md) or with the [Backup Service](../learn/services-and-indexes/services/backup-service.md). Note also that care should taken regarding the potential removal of files used in network sharing.  
Enter the following command:  
```bash  
rm -r /opt/couchbase  
```
5. Determine whether any other files, still resident on the node, need to be either removed, or backed up and removed. If such files exist, deal with them accordingly.
6. Install Couchbase Server on the node. Follow steps 1, 2, and 3; provided in [Install](install-intro.md).
7. _Pin_ (or _hold_) automated Couchbase-Server updates for the node. This ensures that no further upgrade can occur to this node until the next time the administrator electively performs the process.  
RedHat & Centos  
For Couchbase Server Enterprise Edition, ensure that the package-name appears in the list that follows the `exclude` statement, in the file `/etc/yum/yum.conf`. For example:  
```bash  
exclude=couchbase-server  
```  
(For Couchbase Server Community edition, specify `couchbase-server-community`, instead of `couchbase-server`).  
Ubuntu & Debian  
For Couchbase Server Enterprise Edition, run the following command:  
```bash  
apt-mark hold couchbase-server  
```  
(For Couchbase Server Community edition, specify `couchbase-server-community`, instead of `couchbase-server`).
8. Assuming that the `couchbase-server.service` service was _stopped_ on the node to be upgraded prior to that node’s upgrade, restart the service.  
Note that if the service was also _disabled_, it must be _re-enabled_, prior to being started. To re-enable the service, if necessary, enter the following command:  
```bash  
systemctl enable --now couchbase-server.service  
```  
To restart the service, enter the following command:  
```bash  
systemctl start couchbase-server.service  
```

## [](#add-back-the-upgraded-node-and-remove-another-node)Stage Four: Add Back the Upgraded Node, and Remove Another Node

_Add_ the upgraded, removed node back into the cluster, and _remove_ a node that is currently part of the cluster. The node that is being added should be configured to run the same service (or services) on the node that is to be removed. For example, if the node to be removed is running the Data Service, configure the node to be added to run the Data Service. Couchbase Server will execute the rebalance as a _swap rebalance_, to maximize efficiency.

For an overview of node-removal, see [Removal](../learn/clusters-and-availability/removal.md); and for practical examples of performing removal, see [Clusters](#manage:manage-nodes/remove-node-and-rebalance.adoc.
For an overview of node-addition, see xref:learn:clusters-and-availability/nodes.html#clusters); and for practical examples of node-addition, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md).

Note that for the CLI and REST API, the staging of a swap rebalance requires _two_ separate commands.

* The first specifies that one or more nodes be _added_ to the cluster: however, this command requires a subsequent rebalance to be performed, to complete the process.  
For an example of performing addition with the CLI, see [Add a Node and Rebalance with the CLI](../manage/manage-nodes/add-node-and-rebalance.md#add-a-node-with-the-cli). For an example of performing addition with the REST API, see [Add a Node and Rebalance with the REST API](../manage/manage-nodes/add-node-and-rebalance.md#add-a-node-with-the-rest-api).
* The second command indeed specifies that subsequent rebalance, but also includes an instruction to _remove_ one or more nodes from the cluster: therefore, as the rebalance occurs, it finalizes both node-addition and node-removal.  
For an example of using rebalance to remove a node with the CLI, see [Remove a Node with the CLI](../manage/manage-nodes/remove-node-and-rebalance.md#remove-a-node-with-the-cli). For an example of using rebalance to remove a node with the REST API, see [Remove a Node with the REST API](../manage/manage-nodes/remove-node-and-rebalance.md#remove-a-node-with-the-rest-api).

## [](#repeat-stages-three-and-four)Stage Five: Continually Repeat Stages Three and Four

Repeat [Stage Three: Upgrade the Removed Node](#upgrade-the-removed-node) and [Stage Four: Add Back the Upgraded Node, and Remove Another Node](#add-back-the-upgraded-node-and-remove-another-node) until all nodes have been upgraded and added back into the cluster, except one.

## [](#add-back-the-last-node)Stage Six: Add Back the Last Node

When the last node to be upgraded has been upgraded, add this node back into the cluster without removing any other node; and perform a rebalance. This will be executed by Couchbase Server as a _full_ rebalance.

The cluster is now fully upgraded, and is at full capacity.