---
title: Offline Upgrade from Enterprise Analytics to Operational Insights
description: Learn more about the per-node procedure for an offline cluster
  upgrade across the Enterprise Analytics to Operational Insights rename, for
  both .rpm and .deb package formats.
pubDate: 2026-10-23T04:31:18.652Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: procedure
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/upgrade-ea-to-oi.adoc
  xref: xref:enterprise-analytics:install:upgrade-ea-to-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/upgrade-ea-to-oi.html)

# Offline Upgrade from Enterprise Analytics to Operational Insights

> Learn more about the per-node procedure for an offline cluster upgrade across the Enterprise Analytics to Operational Insights rename, for both .rpm and .deb package formats. 

Operational Insights replaces Enterprise Analytics as the product name, starting with this release, and the rename changes both the package name and the install-prefix used on every node. Because standard package managers, such as apt and yum/dnf, have no built-in way to know that the `operational-insights` package is meant to replace `enterprise-analytics`, an ordinary in-place upgrade does not carry a node across this rename safely. Use the following offline, per-node procedure to perform an upgrade that handles the package renaming.

> [!IMPORTANT]
> A plain `apt upgrade` or `yum update` does not pick up Operational Insights, and fails silently: the node stays on Enterprise Analytics with no error.

If you can upgrade with the cluster online, see [Upgrade an Online Cluster](upgrade-cluster-online.md). That procedure does not require any special handling for the Enterprise Analytics to Operational Insights rename. Use this page only if you're upgrading with [the cluster offline](upgrade-cluster-offline.md), which does require the rename-specific steps described here. Complete the cluster-level steps in [Prepare the Cluster](upgrade-cluster-offline.md#prepare-the-cluster) before you start on the first node. For nodes that run in Docker containers, see [Offline Upgrade of a Docker Cluster from Enterprise Analytics to Operational Insights](upgrade-docker-cluster-offline.md) instead.

## [](#prerequisites)Prerequisites

* This is a per-node procedure, and the cluster is down for its entire duration.
* Rolling back from Operational Insights to Enterprise Analytics is not supported.
* Nothing under the node's `var` directory is moved at any point, with one exception: the conditional data-relocation step, which applies only if the node's data directory sits under `/opt/couchbase/var`.
* Note the node's UUID and its configured data path now, so you can verify against them at the end. Both come from the same call:  
```console  
curl -s -u <admin>:<password> http://127.0.0.1:8091/nodes/self \
  | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["nodeUUID"], d["storage"]["hdd"][0]["path"])'  
```

## [](#rhel-procedure)Upgrade Procedure for RHEL (rpm/dnf)

Use this procedure on nodes that run the `.rpm` package format.

### [](#prerequisites-2)Prerequisites

* The successor package refuses to install while Enterprise Analytics is present; the check runs from the package's own `%pre` script, so that an operator cannot reach the install step without first stopping, backing up, and removing the predecessor. Do not try to bypass it: `rpm -i --noscripts` (or `--nopre`, or dnf's `--setopt=tsflags=noscripts`) skips the check and lays both products on top of each other.
* You will not see dnf offer `--allowerasing` or `--skip-broken` for this install, because the successor declares no conflict with the predecessor for either flag to resolve. If you meet either flag in another context on this node, do not take it: `--allowerasing` erases the other product and runs its removal scripts before the install it was meant to enable ever runs, leaving the node stripped and with nothing installed.
* A dnf `versionlock` entry on the predecessor does not block the removal step below; the removal proceeds normally.
* Do not purge, do not delete `/opt/enterprise-analytics`, and do not move the `var` tree yourself. The node's configuration records absolute paths that nothing can rewrite.

### [](#procedure)Procedure

1. Stop the node with the following command:  
```console  
systemctl stop enterprise-analytics  
```
2. Use the following command to copy the node's state aside. This deliberately excludes the bulk data: it's never touched, and copying it would be far too large. If you skip this step, see [If You Skipped the State Backup](#rhel-recovery-no-backup).  
```console  
mkdir -p /var/tmp/ea-state-backup  
tar -C /opt/enterprise-analytics/var/lib/couchbase -cf - --exclude=./data --exclude=./logs . \
  | tar -C /var/tmp/ea-state-backup -xf -  
```
3. Remove the predecessor:  
```console  
dnf remove -y enterprise-analytics  
```  
This deletes 23 paths from the state tree, including `config/chronicle`, `config/certs`, `config/config.dat`, `config/dist_cfg`, and `ip`. It leaves the bulk data, `gosecrets.cfg`, the data encryption keys, and `isasl.pw`, since the package does not own those.
4. Install the successor without letting it start:  
```console  
INSTALL_DONT_START_SERVER=1 dnf install -y ./operational-insights-<version>-linux.<arch>.rpm  
```  
Replace `<arch>` with `x86_64` or `aarch64` to match the node. `uname -m` prints the value to use.  
> [!IMPORTANT]  
> The environment variable is not optional. The package starts the server on install by default, and a server that starts before you restore state in the next step initializes itself as a fresh, empty node.
5. If the data path you noted begins with `/opt/couchbase/var/`, you must move the data out of the way before the next step.  
> [!NOTE]  
> If the data path is anywhere else, such as the Enterprise Analytics default or a separate mount, skip this step.  
Run the following command:  
```console  
DATA=<data_path>  
DEST=/opt/enterprise-analytics/var/${DATA#/opt/couchbase/var/}  
mkdir -p "$(dirname "$DEST")" && mv "$DATA" "$DEST"  
```  
The node is stopped. If you're working within one filesystem, this is a rename and happens instantly. Across multiple filesystems, this process is a real copy. Make sure you have the time and disk space for this process. If you needed to do this and did not, see [If You Skipped the Conditional Data Move](#rhel-recovery-no-data-move).
6. Restore the state, and point the successor at the tree:  
```console  
tar -C /var/tmp/ea-state-backup -cf - . \
  | tar -C /opt/enterprise-analytics/var/lib/couchbase -xf -  
chown -R couchbase:couchbase /opt/enterprise-analytics/var  
rm -rf /opt/couchbase/var  
ln -s /opt/enterprise-analytics/var /opt/couchbase/var  
```
7. If you customized the Enterprise Analytics service with systemd drop-in files, carry them across to the new service name. Removing the package leaves the files under `/etc/systemd/system/enterprise-analytics.service.d/` in place, but the `operational-insights` service does not read them. Without this step, the node starts with the default settings and gives no warning. If you have no drop-in files, the command does nothing but reload systemd.  
```console  
if [ -d /etc/systemd/system/enterprise-analytics.service.d ]; then  
  mkdir -p /etc/systemd/system/operational-insights.service.d  
  cp -a /etc/systemd/system/enterprise-analytics.service.d/. /etc/systemd/system/operational-insights.service.d/  
fi  
systemctl daemon-reload  
```  
If you replaced the whole unit file with `systemctl edit --full`, you have a file at `/etc/systemd/system/enterprise-analytics.service`. Do not copy it to the new name, because it starts the Enterprise Analytics binary that the removal deleted. Left in place, the old unit stays enabled and fails at every boot. Instead, run `systemctl edit operational-insights` and enter only the settings you changed, which systemd saves as a drop-in file. Then disable and remove the old unit file:  
```console  
systemctl disable enterprise-analytics  
rm /etc/systemd/system/enterprise-analytics.service  
systemctl daemon-reload  
```
8. Start the node with the new command for Operational Insights:  
```console  
systemctl start operational-insights  
```
9. If you use Python UDFs, install the [Python UDF add-on](install-udf-addon.md). Enterprise Analytics has no add-on, so this is a new installation rather than an upgrade.

### [](#rhel-recovery-no-backup)If You Skipped the State Backup

rpm renames the packaged configuration files it removes, rather than deleting them, so recovery is usually possible. Look for `config/config.dat.rpmsave` and `ip.rpmsave` under `/opt/enterprise-analytics/var/lib/couchbase`, and rename each back to its original name. Which files are renamed varies with what the node had modified, so restore every `.rpmsave` file you find.

### [](#rhel-recovery-no-data-move)If You Skipped the Conditional Data Move

If you did not [move the data aside](#rhel-data-move-step), you cannot recover your data. Restore it from backup, into the path the node records, which you can read back with the [verify command](#rhel-verify).

### [](#rhel-verify)Verify Before Moving to the Next Node

Run the same check you ran at the start, and confirm the values match:

```console
curl -s -u <admin>:<password> http://127.0.0.1:8091/nodes/self \
  | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["nodeUUID"], d["storage"]["hdd"][0]["path"])'
```

The UUID must match the one you noted at the start. The data path must match too, unless you moved the data in the [conditional data move](#rhel-data-move-step). In that case, the node reports the path with the `/opt/couchbase/var` symbolic link resolved, so it begins with `/opt/enterprise-analytics/var/` rather than the `/opt/couchbase/var/` path you noted. Both name the same directory. To confirm, resolve the path you noted, and check that the result matches the reported path:

```console
realpath "<data_path>"
```

In every case, the data path must still exist:

```console
test -d "<data_path>" && echo data present
```

If you carried drop-in files across in the [drop-in step](#rhel-dropin-step), confirm that the new service lists them:

```console
systemctl cat operational-insights
```

> [!WARNING]
> A different UUID means the node reinitialized itself as a new, empty node. Stop it immediately and do not rebalance. The node might still look healthy.

## [](#deb-procedure)Upgrade Procedure for Ubuntu and Debian (deb/apt)

> [!WARNING]
> The state-backup step below is mandatory on this format, and there is no recovery if you skip it. The `.deb` package declares no `conffiles`, so `dpkg` deletes the node's configuration outright on removal and leaves nothing behind.

### [](#prerequisites-3)Prerequisites

* The successor package refuses to install while Enterprise Analytics is present, whether the predecessor is in its ordinary state or has been pinned with a hold. The check runs from the package's own `preinst` script, so that an operator cannot reach the install step without first stopping, backing up, and removing the predecessor.
* Do not purge, do not delete `/opt/enterprise-analytics`, and do not move the `var` tree yourself. The node's configuration records absolute paths that nothing can rewrite.

### [](#procedure-2)Procedure

1. Run the following command to stop the node:  
```console  
systemctl stop enterprise-analytics  
```
2. Use the following command to make a copy of the node's state aside. On this format, it's the only copy that exists. If you skip this step, see [If You Skipped the State Backup](#deb-recovery-no-backup).  
```console  
mkdir -p /var/tmp/ea-state-backup  
tar -C /opt/enterprise-analytics/var/lib/couchbase -cf - --exclude=./data --exclude=./logs . \
  | tar -C /var/tmp/ea-state-backup -xf -  
```  
Confirm the backup is not empty before continuing:  
```console  
ls /var/tmp/ea-state-backup/config/config.dat  
```
3. Check whether the predecessor is held, then remove it. Use `remove`, not `purge`.  
```console  
dpkg-query -W -f='${Status}\n' enterprise-analytics  
```  
A held package reports `hold ok installed`; an ordinary one reports `install ok installed`. If it's held, clear the hold by resetting the package's selection state to `install`:  
```console  
echo "enterprise-analytics install" | dpkg --set-selections  
```  
Then remove the predecessor:  
```console  
apt-get remove -y enterprise-analytics  
```  
If you skip the hold check and the package is held, the command above stops without removing anything, and displays the following message:  
E: Held packages were changed and -y was used without --allow-change-held-packages.  
Removal deletes 23 paths from the state tree, including `config/chronicle`, `config/certs`, `config/config.dat`, `config/dist_cfg`, and `ip`, and leaves nothing renamed aside. It leaves the bulk data, `gosecrets.cfg`, the data encryption keys, and `isasl.pw`, since the package does not own those.
4. Run the following command to install the successor without letting it start:  
```console  
INSTALL_DONT_START_SERVER=1 apt-get install -y ./operational-insights_<version>-linux_<arch>.deb  
```  
Replace `<arch>` with `amd64` or `arm64` to match the node. `dpkg --print-architecture` prints the value to use.  
> [!IMPORTANT]  
> The environment variable is not optional. The package starts the server on install by default, and a server that starts before you restore state in the next step initializes itself as a fresh, empty node.
5. If the data path you noted begins with `/opt/couchbase/var/`, you must move the data out of the way before the next step.  
> [!NOTE]  
> If the data path is anywhere else, such as the Enterprise Analytics default or a separate mount, skip this step.  
Run the following command:  
```console  
DATA=<data_path>  
DEST=/opt/enterprise-analytics/var/${DATA#/opt/couchbase/var/}  
mkdir -p "$(dirname "$DEST")" && mv "$DATA" "$DEST"  
```  
The node is stopped. If you're working within one filesystem, this is a rename and happens instantly. Across multiple filesystems, this process is a real copy. Make sure you have the time and disk space for this process. If you needed to do this and did not, see [If You Skipped the Conditional Data Move](#deb-recovery-no-data-move).
6. Restore the state, and point the successor at the tree:  
```console  
tar -C /var/tmp/ea-state-backup -cf - . \
  | tar -C /opt/enterprise-analytics/var/lib/couchbase -xf -  
chown -R couchbase:couchbase /opt/enterprise-analytics/var  
rm -rf /opt/couchbase/var  
ln -s /opt/enterprise-analytics/var /opt/couchbase/var  
```
7. If you customized the Enterprise Analytics service with systemd drop-in files, carry them across to the new service name. Removing the package leaves the files under `/etc/systemd/system/enterprise-analytics.service.d/` in place, but the `operational-insights` service does not read them. Without this step, the node starts with the default settings and gives no warning. If you have no drop-in files, the command does nothing but reload systemd.  
```console  
if [ -d /etc/systemd/system/enterprise-analytics.service.d ]; then  
  mkdir -p /etc/systemd/system/operational-insights.service.d  
  cp -a /etc/systemd/system/enterprise-analytics.service.d/. /etc/systemd/system/operational-insights.service.d/  
fi  
systemctl daemon-reload  
```  
If you replaced the whole unit file with `systemctl edit --full`, you have a file at `/etc/systemd/system/enterprise-analytics.service`. Do not copy it to the new name, because it starts the Enterprise Analytics binary that the removal deleted. Left in place, the old unit stays enabled and fails at every boot. Instead, run `systemctl edit operational-insights` and enter only the settings you changed, which systemd saves as a drop-in file. Then disable and remove the old unit file:  
```console  
systemctl disable enterprise-analytics  
rm /etc/systemd/system/enterprise-analytics.service  
systemctl daemon-reload  
```
8. Start the node with the new command for Operational Insights:  
```console  
systemctl start operational-insights  
```
9. If you use Python UDFs, install the [Python UDF add-on](install-udf-addon.md). Enterprise Analytics has no add-on, so this is a new installation rather than an upgrade.

### [](#deb-recovery-no-backup)If You Skipped the State Backup

No recovery is possible on this format. The node's configuration is gone. Restore the node from a cluster backup, or rebuild it and rebalance it back into the cluster.

### [](#deb-recovery-no-data-move)If You Skipped the Conditional Data Move

If you did not [move the data aside](#deb-data-move-step), you cannot recover your data. Restore it from backup, into the path the node records, which you can read back with the [verify command](#deb-verify).

### [](#deb-verify)Verify Before Moving to the Next Node

Run the same check you ran at the start, and confirm the values match:

```console
curl -s -u <admin>:<password> http://127.0.0.1:8091/nodes/self \
  | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["nodeUUID"], d["storage"]["hdd"][0]["path"])'
```

The UUID must match the one you noted at the start. The data path must match too, unless you moved the data in the [conditional data move](#deb-data-move-step). In that case, the node reports the path with the `/opt/couchbase/var` symbolic link resolved, so it begins with `/opt/enterprise-analytics/var/` rather than the `/opt/couchbase/var/` path you noted. Both name the same directory. To confirm, resolve the path you noted, and check that the result matches the reported path:

```console
realpath "<data_path>"
```

In every case, the data path must still exist:

```console
test -d "<data_path>" && echo data present
```

If you carried drop-in files across in the [drop-in step](#deb-dropin-step), confirm that the new service lists them:

```console
systemctl cat operational-insights
```

> [!WARNING]
> A different UUID means the node reinitialized itself as a new, empty node. Stop it immediately and do not rebalance. The node might still look healthy.

## [](#known-limitations)Known Limitations

| Scenario                                                                                                   | Status                                                                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Multi-version jumps, upgrading from an older Enterprise Analytics release straight to Operational Insights | Supported from every previously released version of Enterprise Analytics. The procedure does not depend on the predecessor's version. This applies to offline upgrade only: for online upgrade, see [Upgrade Paths](upgrade.md#supported-upgrade-paths). |
| Mixed-OS clusters, with some nodes on .deb and others on .rpm                                              | Not yet documented. Follow the procedure that matches each node's own package format.                                                                                                                                                                    |
| Rollback or downgrade, from Operational Insights back to Enterprise Analytics                              | Not supported, and not validated.                                                                                                                                                                                                                        |
| Air-gapped environments, with no package repository access during the upgrade                              | Covered. This procedure installs the Operational Insights package file directly, so no repository metadata is needed.                                                                                                                                    |

## [](#see-also)See Also

* [Upgrade an Offline Cluster](upgrade-cluster-offline.md)
* [Upgrade Procedure Selection](upgrade-procedure-selection.md)
* [Uninstall](uninstall.md)