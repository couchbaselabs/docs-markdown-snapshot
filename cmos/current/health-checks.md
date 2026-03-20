---
title: Health Checks
editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/health-checks.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cmos::health-checks.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cmos/current/health-checks.html)

# Health Checks

> [!NOTE]
> The "CB900XX" system of IDs is subject to change in future releases.

## [](#cluster-checks)Cluster Checks

### [](#CB90002)Single or Two Node Cluster (CB90002)

**Background**: Couchbase recommends that all production clusters have at least three nodes. Clusters with fewer than three nodes mean that automatic failover is not possible and the number of bucket replicas is limited to 0 or 1, leading to reduced durability.

**Condition**: Only one or two nodes detected in the cluster.

**Remediation**: Add more nodes to the cluster.

**Further Reading**: [About Deploying Clusters With Less Than Three Nodes](https://docs.couchbase.com/server/current/install/deployment-considerations-lt-3nodes.html)

### [](#CB90004)Mixed Version Cluster (CB90004)

**Background**: While Couchbase Server does support running multiple versions as part of a cluster, this is only recommended during an upgrade, rather than as a long-term state. The cluster features available will be those of the lowest-version node.

**Condition**: Multiple nodes detected with differing Couchbase Server versions.

**Remediation**: Upgrade all nodes to the same version. If this alert is present during an upgrade, it can safely be disregarded until the upgrade is complete.

**Further Reading**: [Feature Availability during Upgrade](https://docs.couchbase.com/server/current/install/upgrade-feature-availability.html), [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html)

### [](#CB90006)Auto Compaction Enabled (CB90006)

**Background**: Couchbase Server uses an append-only store on disk to ensure data durability. This needs to be compacted periodically, otherwise performance can be degraded or the disk can fill up. This is done automatically by default.

**Condition**: No auto-compaction threshold set.

**Remediation**: Enable auto-compaction in the cluster settings

**Further Reading**: [Storage](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/storage.html#append-only-writes-and-auto-compaction)

### [](#CB90007)Auto-Failover Enabled (CB90007)

**Background**: Couchbase Server can automatically fail over dead or unhealthy nodes, to ensure continuity of cluster operations. If auto-failover is disabled, node failure will result in some requests being unable to be serviced.

**Condition**: Auto-failover is disabled.

**Remediation**: Adjust auto-failover settings

**Further Reading**: [Automatic Failover](https://docs.couchbase.com/server/current/learn/clusters-and-availability/automatic-failover.html)

### [](#CB90008)Number of Buckets (CB90008)

**Background**: Couchbase Server supports up to 30 buckets in a cluster as of version 6.5\. Going above this number may cause performance degradation.

**Condition**: More than 30 buckets in the cluster.

**Remediation**: Reduce the number of buckets in the cluster.

**Further Reading**: [Buckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/buckets.html)

### [](#CB90011)Data Loss Messages (CB90011)

**Background**: If a node is failed over, and the active vBuckets stored on it have no replicas, data loss can result. Note that this is only possible if manually performing a hard failover, as Couchbase Server will never perform an automatic failover if there is a risk of data loss.

**Condition**: Messages indicating data loss due to failover detected in the cluster logs.

**Remediation**: Contact Couchbase Technical Support _immediately_. Isolate the failed-over node, and do not make _any_ changes to its configuration or attempt to recover it unless instructed by Couchbase Technical Support. There is a risk of permanent, irrecoverable data loss.

**Further Reading**: [Hard Failover](https://docs.couchbase.com/server/current/learn/clusters-and-availability/hard-failover.html)

### [](#CB90016)All Nodes are Active (CB90016)

**Background**: The Couchbase Cluster Manager periodically contacts all nodes in the cluster to check their status. If a node fails to respond, it is marked as inactive.

**Condition**: One or more inactive nodes are present.

**Remediation**: Rebalance the unhealthy nodes out of the cluster, and replace them if appropriate. Examine the other health check results to identify the potential cause, or contact Couchbase Technical Support for a root cause analysis.

**Further Reading**: [Clusters and Availability](https://docs.couchbase.com/server/current/learn/clusters-and-availability/clusters-and-availability.html), [Detecting Node Failure](https://docs.couchbase.com/server/current/learn/clusters-and-availability/failover.html#detecting-node-failure)

### [](#CB90019)Asymmetrical Cluster (CB90019)

**Background**: Couchbase recommends that all nodes in the cluster have identical hardware. Since clients may access any node in the cluster to service a request, differing hardware can lead to unpredictable application performance.

**Condition**: Nodes with differing amounts of CPUs or RAM detected.

**Remediation**: Ensure all nodes have identical hardware.

**Further Reading**: [Sizing Guidelines](https://docs.couchbase.com/server/current/install/sizing-general.html)

### [](#CB90020)Bucket Count Checks (CB90020)

**Background**: Couchbase recommends that there are at least as many CPUs on each node as there are buckets. If fewer CPUs are available, the buckets will compete with each other for resources, potentially causing degraded performance. If this is not possible due to resource constraints, Couchbase recommends that each bucket have at least 0.4 CPU cores on Couchbase Server 6.x and below, and 0.2 on 7.x. Additionally, no more than 10 (on versions below 6.5) or 30 (on 6.5 and later) total buckets are supported. When these limits are reached, the cluster can get failures across nodes.

**Condition**: Fewer CPUs than buckets detected on the node. Less than or equal to 0.4 cores/bucket on 6.x and less than or equal to 0.2 cores/bucket on 7.x. More than 30 buckets in the cluster.

**Remediation**: Upgrade the nodes' hardware or reduce the number of buckets.

**Further Reading**: [Sizing Guidelines](https://docs.couchbase.com/server/current/install/sizing-general.html)

### [](#CB90022)Backup Location Check (CB90022)

**Background**: If the Couchbase Backup Service cannot access the backup archive location, backup failures may result, leading to reduced durability.

**Relevant To Versions**: 7.0.0 and above **Condition**: The number of backup location errors has increased in the past three days.

**Remediation**: Ensure the Backup Service has consistent access to its archive location.

**Further Reading**: [Backup Service](https://docs.couchbase.com/server/current/learn/services-and-indexes/services/backup-service.html)

### [](#CB90023)Orphaned Backup Tasks (CB90023)

**Background**: An "orphaned" backup task is a task that is marked as running, but no node is actually executing it. This can happen if that node cannot for some reason send a status report to the Backup Service leader (for example it suffered a power cut or a network outage). These may be transient errors, but seeing a consistent increase in the number of orphaned tasks can indicate a problem with the Backup Service.

**Relevant To Versions**: 7.0.0 and above **Condition**: The number of orphaned backup tasks has increased in the past three days.

**Remediation**: Review the Backup Service logs to identify the cause of the problem, or contact Couchbase Technical Support.

**Further Reading**: [Backup Service](https://docs.couchbase.com/server/current/learn/services-and-indexes/services/backup-service.html)

### [](#CB90027)Index Service Log Level (CB90027)

**Background**: While the log level of the Index Service can be configured, only the default setting of `Info` is supported. Higher levels can mean valuable information is missing from the logs, while lower levels can mean the logs are rotated more frequently. Both of these can make it difficult to diagnose issues with the Index Service.

**Condition**: Index Service log level is set to a non-default value.

**Remediation**: Change the log level to `Info`.

**Further Reading**: [Index Settings](https://docs.couchbase.com/server/current/manage/manage-settings/general-settings.html#index-settings-via-rest)

### [](#CB90030)Index With No Redundancy (CB90030)

**Background**: By default, a Global Secondary Index is only situated on one Index Service node, meaning that if that node is failed over for any reason, queries using that index will either use a primary index (causing severely degraded performance) or start failing completely. In production use cases we always recommend indexes have either replicas or equivalent indexes (indexes with a different name but the same definition).

**Condition**: An index with no replicas or equivalent indexes is detected.

**Remediation**: Either increase the number of replicas or add equivalent indexes.

**Further Reading**: [Index Availability and Performance](https://docs.couchbase.com/server/current/learn/services-and-indexes/indexes/index-replication.html)

### [](#CB90031)Bad Redundant Index (CB90031)

**Background**: When using index replicas, the Index Service will place replicas on different nodes to ensure their availability in the event of a node failover. However equivalent indexes do not have this protection, and it is possible to place two or more equivalent indexes on the same node. This provides effectively no redundancy, as should that node be failed over all the equivalent indexes will be lost and queries may start failing or experience severely degraded performance.

**Condition**: Multiple equivalent indexes on the same node.

**Remediation**: Move the indexes to different Index Service nodes. Consider using index replicas instead.

**Further Reading**: [Index Availability and Performance](https://docs.couchbase.com/server/current/learn/services-and-indexes/indexes/index-replication.html)

### [](#CB90032)Too Many Index Replicas (CB90032)

**Background**: After an index node is failed over, it is possible that an index has more replicas than there are Index Service nodes. This does not provide the desired level of redundancy and durability.

**Condition**: Index with more replicas than there are Index Service nodes.

**Remediation**: Either reduce the number of replicas, or add more Index Service nodes.

### [](#CB90035)Empty Server Group (CB90035)

**Background**: There is no practical use for having an empty server group, so if one is present it is most likely a mistake.

**Condition**: One or more server groups exist that do not contain any nodes.

**Remediation**: Remove the empty server group.

**Further Reading**: [Manage Server Groups](https://docs.couchbase.com/server/current/manage/manage-groups/manage-groups.html)

### [](#CB90059)Developer Preview (CB90059)

**Background**: Developer Preview provides early access to features which may become generally available (“GA”) in future releases and enables you to experiment with these features to get a sense of how they work. However, this mode is unsupported, so it should not be used in production.

**Condition**: Cluster is in Developer Preview mode.

**Remediation**: If this is a development only cluster, you do not need to do anything, otherwise create a new cluster that is not in Developer Preview mode.

**Further Reading**: [Developer Preview Mode](https://docs.couchbase.com/server/current/developer-preview/preview-mode.html)

### [](#CB90063)Duplicate Node UUID Check (CB90063)

**Background**: Couchbase expects the node UUID to uniquely identify each node for Cluster Manager purposes. If this condition is not met, serious issues with rebalances and other operations may be experienced.

**Condition**: At least one node UUID is not unique in the cluster.

**Remediation**: Contact Couchbase Technical support.

**Further Reading**: [MB-17132](https://issues.couchbase.com/browse/MB-17132)

### [](#CB90065)Too many FTS Index replicas (CB90065)

**Background**: If there are more replicas configured than FTS nodes, these replicas cannot be distributed properly and may cause rebalance issues.

**Condition**: The number of FTS replicas configured is greater than or equal to the number of nodes running the Search service.

**Remediation**: Ensure there are strictly fewer FTS index replicas than nodes running the Search Service.

**Further Reading**: [FTS Replicas](#7.0@server:fts:fts-index-replicas)

### [](#CB90068)Missing Index Partition (CB90068)

**Background**: If a index is missing index partitions, it can cause queries that use this index to fail which can lead to client errors.

**Condition**: If the number of index partitions present is less than what was originally defined when making the index.

**Remediation**: Check if a node has been failed over. If this is not the case, recreate the index again and contact Couchbase Technical Support.

**Further Reading**: [Index Partitioning](#7.0@server:n1ql:n1ql-language-reference:index-partitioning)

### [](#CB90069)Imbalanced Index Partition (CB90069)

**Background**: If an index partition is hashed on an invalid field, it results in one partition being larger than the partitions on other Index Service nodes. This means a large chunk of a node’s memory will be used by the Index Service which can then cause the `indexer` process to be killed by the Linux OOM killer.

**Condition**: An Index Service node contains an index partition which is 20% larger than partitions for the same index on other nodes.

**Remediation**: Recreate imbalanced index to redistribute index partition data, making sure the index partitions are hashed to valid fields.

**Further Reading**: [Index Partitioning](https://docs.couchbase.com/server/current/n1ql/n1ql-language-reference/index-partitioning.html)

### [](#CB90079)Default VBucket Count (CB90079)

**Background**: The vBucket count set in cluster configuration, if changed from default value (64 on macOS, 1024 on Windows/Linux) can cause failures across nodes and services. This may impact cluster integrity and is not recommended in production environment.

**Condition**: Non-default vBucket number

**Remediation**: Set the vBucket number back to the default value (64 on macOS, 1024 on Windows/Linux).

### [](#CB90038)Stats Collection Failed (CB90038)

**Background**: The CMOS Prometheus server will scrape all Couchbase Server nodes periodically (every 30 seconds by default) for statistics. If a node fails to respond, this can indicate that the node is down, its CPU is overloaded, or there is a network issue preventing Prometheus from communicating with it.

**Condition**: Prometheus has failed to scrape a Couchbase Server node.

**Remediation**: Check the node’s status and resource usage.

### [](#CB90073)Dropped DCP Mutations (CB90073)

**Background**: This can be an indication of a Couchbase Server Issue (MB-41255) which was fixed in versions: 6.0.5, 6.5.2 and 6.6.1\. This issue can affect data integrity. DCP mutations track any documents made to Couchbase Server and do Documents. If you drop DCP mutations, then changes to documents may be lost.

**Condition**: Dropped DCP mutations found in memcached.log.

**Remediation**: If you experience data integrity issues, update to a more recent version of Couchbase Server.

**Further Reading**: [MB-41255](https://issues.couchbase.com/browse/MB-41255)

## [](#node-checks)Node Checks

### [](#CB90001)One Service Per Node (CB90001)

**Background**: Couchbase recommends that only one Multi-Dimensional Scaling service per node is run in production. Colocating services increases the overall resource requirements of the nodes and can cause resource contention, leading to degraded performance.

**Condition**: More than one service detected per node.

**Remediation**: Move services to their own dedicated nodes.

**Further Reading**: [Sizing Guidelines](https://docs.couchbase.com/server/current/install/sizing-general.html)

### [](#CB90003)Unhealthy or Inactive Node (CB90003)

**Background**: If the Cluster Manager detects that a node is unhealthy, it will mark it as such and fail it over (if Auto-Failover is enabled and the conditions are met). This will mean the cluster is in a degraded state with reduced durability and capacity.

**Condition**: One or more nodes are reported as unhealthy by the Couchbase Cluster Manager.

**Remediation**: Rebalance the unhealthy nodes out of the cluster, and replace them if appropriate. Examine the other health check results to identify the potential cause, or contact Couchbase Technical Support for a root cause analysis.

**Further Reading**: [Clusters and Availability](https://docs.couchbase.com/server/current/learn/clusters-and-availability/clusters-and-availability.html), [Detecting Node Failure](https://docs.couchbase.com/server/current/learn/clusters-and-availability/failover.html#detecting-node-failure)

### [](#CB90005)Server Quota (CB90005)

**Background**: Each Couchbase Server node has a memory quota, which limits how much memory it is allowed to use. We recommend that this is set no higher than 80-90% of the host’s memory, otherwise the operating system may not have enough memory remaining to function.

**Condition**: Memory allocated to Couchbase Server nodes is greater than 80% of the hosts' memory.

**Remediation**: Increase the amount of memory on the nodes, or reduce the Couchbase Server memory quota.

**Further Reading**: [Sizing Guidelines](https://docs.couchbase.com/server/current/install/sizing-general.html)

### [](#CB90012)Server Version Supportability (CB90012)

**Background**: Couchbase Server versions are only supported for a period of time as defined in the Enterprise Software Support Policy. Outside this period, limited or no support can be provided by Couchbase Technical Support. We recommend you always run a supported version of Couchbase Server to take advantage of your Enterprise Support agreement.

**Condition**: Nodes running unsupported versions of Couchbase Server detected.

**Remediation**: Upgrade the nodes in question to a supported version of Couchbase Server. If this is not possible, contact your Couchbase Account Manager.

**Further Reading**: [Couchbase Enterprise Software Support Policy](https://www.couchbase.com/support-policy/enterprise-software), [Upgrading Couchbase Server](https://docs.couchbase.com/server/current/install/upgrade.html)

### [](#CB90014)Generally Available Build (CB90014)

**Background**: Only generally available, officially released builds of Couchbase Server are supported, unless you have a specific agreement with Couchbase to use a non-GA build in production.

**Condition**: Node running non-GA build of Couchbase Server detected.

**Remediation**: Upgrade the node to a generally available build of Couchbase Server. If you have a specific agreement with Couchbase to operate a non-GA build (for example a Maintenance Patch), it is safe to disregard this warning.

### [](#CB90018)Node Swap Usage (CB90018)

**Background**: Couchbase Server should always have sufficient RAM available without needing to use swap space. Couchbase Server can manage its own disk storage using ejection, so its memory being in swap can negatively affect performance.

**Condition**: Node swap usage above zero. Upgraded to an alert if swap usage is above 90% of available swap memory.

**Remediation**: Increase available RAM on the nodes.

**Further Reading**: [Memory](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/memory.html)

### [](#CB90021)Disk Space Usage (CB90021)

**Background**: Couchbase Server nodes should always have sufficient disk space to store all data. If a node runs out of storage, it will stop accepting writes and may potentially be automatically failed over.

**Condition**: Over 90% disk usage on the node.

**Remediation**: Increase the amount of disk space available.

**Further Reading**: [Storage](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/storage.html)

### [](#CB90025)Transparent Huge Pages (CB90025)

**Background**: The Linux kernel supports _transparent huge pages_ (THP), a feature that reduces memory management overhead. Although it is often beneficial for general purpose workloads, it can cause performance degradation for databases like Couchbase Server. Therefore, we recommend disabling THP.

**Condition**: Transparent Huge Pages set to `always`. (Requires the Couchbase Health Agent to be installed.)

**Remediation**: Set the THP configuration to `madvise` or `never`.

**Further Reading**: [Disabling Transparent Huge Pages](https://docs.couchbase.com/server/current/install/thp-disable.html)

### [](#CB90026)Service Status (CB90026)

**Background**: Couchbase Server uses a number of ports to communicate between clients and services. If these are blocked by a firewall, this can cause connection failures for clients or other cluster problems.

**Condition**: Cluster Monitor cannot communicate with the node on the specified ports.

**Remediation**: Ensure there is no firewall blocking communication. Review your infrastructure for networking issues.

**Further Reading**: [Couchbase Server Ports](https://docs.couchbase.com/server/current/install/install-ports.html)

### [](#CB90028)Services Sharing File Systems (CB90028)

### [](#CB90034)Below Minimum Node Memory (CB90034)

**Background**: The recommended minimum memory for each node in your Couchbase Server cluster to have is 4 Gigabytes. Any less than this and Couchbase Server could display unwanted behaviour.

**Condition**: A node has less than 4GB of RAM.

**Remediation**: Upgrade the node’s hardware.

**Further Reading**: [System Resource Requirements](https://docs.couchbase.com/server/current/install/pre-install.html)

### [](#CB90040)Supported/Deprecated OS (CB90040)

**Background**: Each version of Couchbase Server supports certain operating systems. Using unsupported OS versions may cause various issues, including Couchbase Server or its services failing to start, and may render your cluster unsupportable.

**Condition**: A node has an operating system version not supported for the version of Couchbase Server in use. (Requires the Couchbase Health Agent to be installed.)

**Remediation**: Upgrade the operating system of the node.

**Further Reading**: [Supported Operating Systems](https://docs.couchbase.com/server/current/install/install-platforms.html)

### [](#CB90042)Segmentation Faults (CB90042)

**Background**: A segmentation fault (segfault) occurs when a process reads invalid or restricted memory. Segmentation faults are nearly always a bug, and often cause processes to crash, leading to degraded availability and system instability.

**Condition**: Segmentation faults seen in the system logs. (Requires the Couchbase Health Agent to be installed.)

**Remediation**: Examine the system logs. If a Couchbase process was the one to crash, contact Couchbase Technical Support.

### [](#CB90044)Managed Service Crash (CB90044)

**Background**: The "babysitter" is part of Couchbase Server’s cluster manager which is responsible for maintaining a variety of Couchbase Server processes. If any of the processes managed by the babysitter die, it is responsible for restarting them.

**Condition**: A process managed by babysitter crashes. (Requires the Couchbase Health Agent to be installed.)

**Remediation**: A process can crash for a number of reasons, so if it happens once or twice it is not indicative of a Couchbase Server issue. However, if it is happening repeatedly or you do notice disruption in your cluster please contact Couchbase Technical Support.

**Further Reading**: [Cluster Manager](https://docs.couchbase.com/server/current/learn/clusters-and-availability/cluster-manager.html)

### [](#CB90045)Used Memory Percentage Check (CB90045)

**Background**: If more than 90% of RAM is in use then Couchbase Server performance may be negatively affected. This is because there needs to be enough RAM for the operating system and to avoid swapping.

**Condition**: More than 90% of available RAM is used.

**Remediation**: Add more RAM to the node, or review the resource usage of other applications on the server.

**Further Reading**: [Service Memory Quotas](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/memory.html), [Sizing Guidelines](https://docs.couchbase.com/server/current/install/sizing-general.html)

### [](#CB90058)Open File / Process Limits (CB90058)

**Background**: Linux processes have a limit of how many file descriptors (files, network sockets, etc.) can be open at a time, and how many processes a user can create. These limits are in place to prevent issues such as fork bombs, but the default values are often too low on many distros. Exceeding these limits can cause hard-to-diagnose issues, including Couchbase Server failing to start.

You can verify the values of the limits using the `ulimit -n` and `ulimit -u` commands respectively.

**Condition**: Open file / process limits for the Couchbase Server `babysitter` process are below the recommended value. (Requires the Couchbase Health Agent to be installed.)

**Remediation**: Increase the open file / process limit for the Couchbase Server processes.

**Further Reading**: [Setting Max Process Limits](https://docs.couchbase.com/server/current/install/rhel-suse-install-intro.html#setting-max-process-limits), [Establish Limits for User Processes and File Descriptors](https://docs.couchbase.com/server/current/install/non-root.html#establish-limits-for-user-processes-and-file-descriptors)

### [](#CB90060)Out-Of-Memory Killer Activity (CB90060)

**Background**: Linux will engage the Out-Of-Memory (OOM) Killer when the system is critically low on available RAM. Since the OOM killer will kill the fewest possible processes to reclaim as much memory as possible, and since Couchbase Server processes generally use a lot of memory, they are often the first to be killed.

Even if Couchbase Server processes are not themselves killed, OOM killer activity is generally a sign that the node may be underprovisioned.

**Condition**: OOM kill messages are seen in the kernel log (`dmesg`). (Requires the Couchbase Health Agent to be installed.)

**Remediation**: Review available memory on the node.

**Further Reading**: [Memory](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/memory.html), [Sizing Guidelines](https://docs.couchbase.com/server/current/install/sizing-general.html)

### [](#CB90064)Node-to-Node Communication Issues (CB90064)

**Background**: Couchbase Server requires a number of ports to be open between all nodes in the cluster. If these ports are not open, it can cause various problems as the services cannot communicate with each other.

Note that this list of ports is different to the ports needed for application clients to communicate with the cluster.

**Condition**: A node detects that it cannot establish TCP connections to another node.

> [!NOTE]
> Not all internal ports are currently checked, so there may still be intra-cluster communication issues even if this health check is good. You should ensure that all ports on the below page are unblocked between all nodes.

(Requires the Couchbase Health Agent to be installed.)

**Remediation**: Verify the ports listed in the alert, and ensure there are no firewalls or other network configuration issues between the listed nodes.

**Further Reading**: [Couchbase Server Ports](https://docs.couchbase.com/server/current/install/install-ports.html)

### [](#CB90074)SYN Flooding (CB90074)

**Background**: SYN packets are normally generated when a client attempts to start a TCP connection to a node. SYN flooding occurs when the buffer used to store SYN packets becomes full. This can be a result of the node not being able to keep up with the rate of incoming connections, which may be because of a Denial of Service attack.

**Condition**: SYN flooding message detected in `dmesg`. (Requires the Couchbase Health Agent to be installed.)

**Remediation**: Reduce the number of incoming connections to specified port.

**Further Reading**: [Manage Cluster Connections](https://docs.couchbase.com/server/current/rest-api/rest-manage-cluster-connections.html)

### [](#CB90075)CPU Soft Lockup (CB90075)

**Background**: Soft lockup is a symptom of a task/kernel thread using and not releasing CPU for a period of time. It can usually occur as a kernel bug or when deploying Couchbase Server in an overcommitted Virtual Environment.

**Condition**: Soft lockup message detected in Linux 'dmesg'. (Requires the Couchbase Health Agent to be installed.)

**Remediation**: If deploying Couchbase Server in a Virtual Environment check if said enviroment is overcommitted.

**Further Reading**: [Deployment Considerations for Virtual Machines and Containers](https://docs.couchbase.com/server/current/install/best-practices-vm.html)

### [](#CB90076)Connection Tracking Table Full (CB90076)

**Background**: If The connection tracking table (`conntrack`) becomes full, packets may be lost and clients might start timing out. The connection table being full can be a sign that clients are not properly closing connections to Couchbase Server.

**Condition**: Connection table full message found in `dmesg`. (Requires the Couchbase Health Agent to be installed.)

**Remediation**: Check your clients are closing connections to Couchbase Server properly.

### [](#CB90082)Couchbase Ports Status Check (CB90082)

**Background**: If the couchbase ports used by different couchbase processes are allocated to other processes then it can cause bind failures. Also couchbase ports which are reserved for future use must be left alone, or can cause failures in upgrades.

**Condition**: Couchbase port is used by another process. (Requires the Couchbase Health Agent to be installed.)

**Remediation**: Allocate another port not used by couchbase to the other process.

### [](#CB90083)Auto Failover Limit for VM (CB90083)

**Background**: Due to the fact that the VM is running on top of a hypervisor or container engine, there will be a minor CPU performance overhead. In certain circumstances, the default auto-failover timeout in Couchbase can cause some issues. It is recommended that you change the threshold from 30 seconds (the default), to 45, or even 60 seconds, depending on how CPU-intensive your workload is.

**Condition**: Auto-failover on virtual machine is set under 30 seconds. (Requires the Couchbase Health Agent to be installed.)

**Remediation**: Adjust auto-failover timeout to 45 or above, depending on your workload.

**Further Reading**: [Auto-Failover Threshold](https://docs.couchbase.com/server/current/install/best-practices-vm.html)

### [](#CB90084)Possible shared storage (CB90084)

**Background**: Couchbase Server ensures high availability by removing single points of failure from the deployment. If a shared storage layer (such as SAN) is used in the deployment then issues with this part of the stack could lead to cluster-wide adverse effects.

**Condition**: Dmesg output indicates that a shared storage device layer might be present in the cluster. (Requires the Couchbase Health Agent to be installed.)

**Remediation**: Ensure each node has an independent storage layer to remove a single point of failure.

### [](#CB90085)Check High Prometheus Load Time (CB90085)

**Background**: Starting from Couchbase Server 7.0, An instance of Prometheus runs on each node of the cluster; and the metrics for each node are duly stored in that node’s instance of Prometheus. It has been observed that lack/delay of reverse DNS resolution on the node can affect the Configuration load time of Prometheus.

**Condition**: Prometheus reporting "Completed loading of configuration file" with more than 1s totalDuration.

**Remediation**: Validate reverse DNS lookup for all the IP addresses associated with the node’s hostname.

### [](#CB90086)Document Size Too Big (CB90086)

**Background**: If a document is 19.5MB and metadata is 1MB, then the document is more than 20MB and registers DCP stream errors.

**Condition**: The document with metadata exceeds 20MB limit.

**Remediation**: Reduce document size.

### [](#CB90088)Analytics JRE Check (CB90088)

**Background**: The Analytics Service requires a Java Runtime Environment to be installed. Only HotSpot-based JVMs, which includes the ones provided by OpenJDK and Oracle’s JDK, are supported.

**Condition**: The Java Runtime Environment is not supported.

**Remediation**: Install a Java Runtime Environment version provided by a supported vendor.

**Further Reading**: <https://docs.couchbase.com/server/current/install/install-environments.html>

### [](#CB90089)XDCR Invalid Datatype (CB90089)

**Background**: If the user has improperly configuration, XDCR won’t go through and give EINVAL error. Follows by SET\_WITH\_META errors or 403 permission error.

**Condition**: Improperly configured RBAC user.

**Remediation**: Configure RBAC User properly.

**Further Reading**: [RBAC](https://docs.couchbase.com/server/current/rest-api/rbac.html)

### [](#CB90036)`memcached` Crashes (CB90036)

**Background**: If the Data Service process (`memcached`) crashes, it will be restarted within a few seconds. However, repeated crashes should be investigated as they may be caused by an underlying issue.

**Condition**: A crash is seen in the `memcached` logs.

**Remediation**: Contact Couchbase Technical Support.

### [](#CB90041)CPU Steal (CB90041)

**Background**: Steal time is the percentage of time a virtual CPU waits for a real CPU while the hypervisor is servicing another virtual processor. In virtual environments, high CPU steal indicates that the virtual machines might be undersized or the hypervisor may be overcommitted.

**Condition**: CPU steal rate is greater than 3%.

**Remediation**: Increase resources available to virtual machine.

**Further Reading**: [Virtualisation Best Practices](https://docs.couchbase.com/server/current/install/best-practices-vm.html)

### [](#CB90043)Disk Commit Fail (CB90043)

**Background**: A disk commit failure is when Couchbase Server cannot write data from memory to the file system.

**Condition**: An item failed to be written to disk.

**Remediation**: Review your infrastructure for signs of disk problems or any other issues, or contact Couchbase Technical Support.

**Further Reading**: [Storage](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/storage.html)

### [](#CB90044)Babysitter Managed Process Crash (CB90044)

**Background**: Babysitter is part of Couchbase Server’s cluster manager which is responsible for maintaining a variety of Couchbase Server processes. If any of the processes managed by the babysitter die, it is responsible for restarting them.

**Condition**: A process managed by babysitter crashes.

**Remediation**: A process can crash for a number of reasons, so if it happens once or twice it is not indicative of a Couchbase Server issue. However, if it is happening repeatedly or you do notice disruption in your cluster please contact Couchbase Technical Support.

**Further Reading**: [Cluster Manager](https://docs.couchbase.com/server/current/learn/clusters-and-availability/cluster-manager.html)

### [](#CB90046)Indexer Crash (CB90046)

**Background**: If the Index Service process (`indexer`) crashes, it will be restarted within a few seconds by the cluster manager. However, repeated crashes should be investigated as they may be caused by an underlying issue.

**Condition**: A crash is seen in `indexer` logs.

**Remediation**: Review `indexer.log` to identify the cause, or contact Couchbase Technical Support.

**Further Reading**: [Index Service](https://docs.couchbase.com/server/current/learn/services-and-indexes/services/index-service.html)

### [](#CB90048)Cross Data Center Replication (XDCR) Crash (CB90048)

**Background**: If the XDCR process (`goxdcr`) crashes, it will be restarted within a few seconds by the cluster manager. However, repeated crashes should be investigated as they may be caused by an underlying issue.

**Condition**: A crash is seen in `goxdcr` logs.

**Remediation**: Review `goxdcr.log` to identify the cause, or contact Couchbase Technical Support.

**Further Reading**: [Cross Data Center Replication](https://docs.couchbase.com/server/current/learn/clusters-and-availability/xdcr-overview.html)

### [](#CB90049)Full Text Search (FTS) Crash (CB90049)

**Background**: If the FTS Service process (`cbft`) crashes, it will be restarted within a few seconds by the cluster manager. However, repeated crashes should be investigated as they may be caused by an underlying issue.

**Condition**: A crash is seen in `cbft` logs.

**Remediation**: Review `fts.log` to identify the cause, or contact Couchbase Technical Support.

**Further Reading**: [Search Service](https://docs.couchbase.com/server/current/learn/services-and-indexes/services/search-service.html)

### [](#CB90050)Eventing Crash (CB90050)

**Background**: If the Eventing Service process crashes, it will be restarted within a few seconds by the cluster manager. However, repeated crashes should be investigated as they may be caused by an underlying issue.

**Condition**: A crash is seen in `eventing.log`.

**Remediation**: Review `eventing.log` to identify the cause, or contact Couchbase Technical Support.

**Further Reading**: [Eventing Service](https://docs.couchbase.com/server/current/learn/services-and-indexes/services/eventing-service.html)

### [](#CB90051)Analytics Crash (CB90051)

**Background**: If the Analytics Service process (`cbas`) crashes, it will be restarted within a few seconds by the cluster manager. However, repeated crashes should be investigated as they may be caused by an underlying issue.

**Condition**: A crash is seen in `cbas` logs.

**Remediation**: Review `analytics_debug.log` to identify the cause, or contact Couchbase Technical Support.

**Further Reading**: [Analytics Service](https://docs.couchbase.com/server/current/learn/services-and-indexes/services/analytics-service.html)

### [](#CB90056)Memcached Connections Rejected (CB90056)

**Background**: If `memcached` (the Data Service) has too many open connections then it won’t allow any new ones to be made. This will result in client errors on applications attempting to connect to Couchbase Server

**Condition**: The number of open connections to `memcached` reaches its limit.

**Remediation**: Contact your network/application team to see if there are any applications keeping open a large number of connections.

**Further Reading**: [Manage Cluster Connections](https://docs.couchbase.com/server/current/rest-api/rest-manage-cluster-connections.html)

### [](#memcached-time-jumps-cb90057)Memcached Time Jumps (CB90057)

**Background**: Memcached time jumps occur when the `memcached` process has not been scheduled by the CPU, or not scheduled enough for a significant period of time. Time jumps are the result of underlying issues (e.g. over provisioning or VM resource contention) with the machine that Couchbase Server is running on, particularly in virtualised environments.

**Condition**: Memcached detected a time jump.

**Remediation**: Check for evidence of your node being over provisioned or for evidence of VM resource contention.

**Further Reading**: [Virtualisation Best Practices](https://docs.couchbase.com/server/current/install/best-practices-vm.html)

### [](#dropped-ticks-cb90062)Dropped Ticks (CB90062)

**Background**: Couchbase Server nodes regularly send heartbeat ticks to each other. If the Cluster Manager logs `dropped ticks` this means when it tried to process a tick, it found other ticks that had not been processed yet. In other words, due to a scheduling issue the Cluster Manager was not able to process the previous tick in time. Dropped ticks are usually a sign of resource contention, specifically CPU contention.

**Condition**: Can be triggered by either detecting over 10 dropped ticks on a node or by detecting over 4 instances of dropped ticks occurring on a node within a one hour time frame.

**Remediation**: Increase number of CPUs available to Couchbase Server or, if you are running a virtualised environment, check for VM overcommitment.

**Further Reading**: [Sizing Guidelines](#7.0@server:install:sizing-general)

### [](#CB90067)Service DCP Rollback to Zero (CB90067)

**Background**: A service has been forced to DCP rollback to zero. A DCP rollback is when the Data Service connects to a client with newer mutations that are not present on the Data Service. The client must rollback or undo some mutations to align with the mutations on the Data Service. If the client is rolled back to 0, it means the service is attempting to resynchronize the entirety of the data set.

**Condition**: A DCP rollback to zero is seen in the `memcached` logs in the last hour.

**Remediation**: This is typically a symptom of another problem, you should monitor your cluster closely for any further issues. If you experience any, then please contact Couchbase Technical Support.

**Further Reading**: [Couchbase DCP Rollback](https://blog.couchbase.com/couchbase-dcp-rollback-qa-tests/)

### [](#CB90070)Permission Denied Errors (CB90070)

**Background**: Couchbase Server has been denied permission to access resources. This is potentially due to other applications locking Couchbase Server files, or misconfiguration.

**Condition**: Found permission denied errors in memcached.log.

**Remediation**: Check that there are no other applications locking files in your Couchbase Server directory, and that permissions are correctly configured. If this does not solve the problem, please contact Couchbase Support.

### [](#CB90072)Data Service Connection Limit (CB90072)

**Background**: By default, the maximum number of connections to the Data Service is limited to 65,000, of which 5,000 are reserved for internal system services. If this limit is exceeded, clients will fail to connect to your Couchbase cluster.

The default limit is high enough that it is unlikely to be legitimately exceeded in production. If it is exceeded, the most likely cause is application code failing to shut down connections properly.

**Condition**: Warning if the number of connections is above 80% of the default limit (60,000). Upgraded to an alert if the limit is exceeded, or log messages are seen that indicate that client connections are being rejected because of the limit.

> [!NOTE]
> It is possible to modify this limit. However, if this is done, you will need to adjust this health check’s threshold accordingly, otherwise it may produce false positives or negatives.

**Remediation**: Review your application code to ensure that it is closing Couchbase connections properly.

**Further Reading**: [Managing Cluster Connections](https://docs.couchbase.com/server/current/rest-api/rest-manage-cluster-connections.html)

## [](#bucket-checks)Bucket Checks

### [](#CB90009)Missing Active vBuckets (CB90009)

**Background**: Couchbase Server buckets are sharded into a number of vBuckets, which are distributed among the nodes in the cluster. This check verifies that all vBuckets in the cluster are in the correct state.

**Condition**: Buckets reported missing by the Cluster Manager.

**Remediation**: Rebalance the cluster, adding new nodes as necessary.

**Further Reading**: [vBuckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/vbuckets.html)

### [](#CB90010)Missing Replica vBuckets (CB90010)

**Background**: Couchbase Server buckets are sharded into a number of vBuckets, which are distributed among the nodes in the cluster. This check verifies that all vBuckets in the cluster are in the correct state.

**Condition**: Buckets reported missing by the Cluster Manager.

**Remediation**: Rebalance the cluster, adding new nodes as necessary.

**Further Reading**: [vBuckets](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/vbuckets.html)

### [](#CB90013)Resident Ratio (CB90013)

**Background**: The resident ratio of a bucket is the percentage of its data that is stored in RAM. Low resident ratio values may be an indication of insufficient resource allocation to the cluster. However, they may not directly indicate a problem.

**Condition**: Resident ratio below 10%. Upgraded to an alert if it is below 5%.

**Remediation**: Increase the bucket’s memory quota.

**Further Reading**: [Memory](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/memory.html)

### [](#CB90015)Number of Nodes for Replication (CB90015)

**Background**: Depending on the requested number of replica vBuckets, a certain number of Couchbase Server nodes are recommended - 5 or more for 2 replicas, or 10 or more for 3 replicas. While it is possible to use 2 or 3 replicas with fewer nodes, this can cause performance degradation.

**Condition**: Insufficient nodes present to support the requested number of replicas.

**Remediation**: Add more nodes to the cluster, or reduce the number of replicas.

**Further Reading**: [Sizing Guidelines](https://docs.couchbase.com/server/current/install/sizing-general.html)

### [](#CB90017)Bucket Memory Usage (CB90017)

**Background**: If a bucket’s memory usage crosses the high water mark, ejection will be triggered. By default, the high water mark is set to 85% of the bucket’s quota. If the bucket’s memory usage exceeds this for a long period of time, it is possible that not enough data can be ejected to bring it down below the low water mark, and there is a risk of an out-of-memory condition.

**Condition**: The bucket’s memory usage is at or above 95% of its quota for more than 5 seconds.

**Remediation**: Increase the bucket’s memory quota.

**Further Reading**: [Memory](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/memory.html)

### [](#CB90024)DCP active writes (CB90024)

**Background**: known bug, [MB-46482](https://issues.couchbase.com/browse/MB-46482), can manifest itself as DCP replications pausing. This can result in slow replication or rejected writes.

**Relevant To Versions**: Between 6.5.0 and 6.6.2 (inclusive)

**Condition**: Warns if the size of synchronous writes accepted is higher than the maximum DCP buffer. Upgraded to an alert if the DCP replication is paused.

**Remediation**: Upgrade to Couchbase Server 6.6.3\. If this is not viable, contact Couchbase Technical Support.

**Further Reading**: [MB-46482](https://issues.couchbase.com/browse/MB-46482)

### [](#CB90029)Large Checkpoints (CB90029)

**Background**: Checkpoints are a feature of the Database Change Protocol (DCP) to avoid needing to re-stream large amounts of data. Large checkpoints can indicate issues with the Data Service, potentially necessitating a Couchbase Server upgrade to a version where these are resolved.

**Condition**: vBucket checkpoints are larger than either 50Mb or 1% of the bucket quota.

**Remediation**: Contact Couchbase Technical Support for analysis.

**Further Reading**: [checkpoint](https://docs.couchbase.com/server/current/cli/cbstats/cbstats-checkpoint.html)

### [](#CB90039)Memcached Fragmentation Check (CB90039)

**Background**: When the memcached heap gets fragmented, all fragmented memory becomes irretrievable and cannot be returned to the OS. If memory keeps getting fragmented for an extended period of time then the amount of usable memory becomes limited.

**Condition**: Over 15% of the memcached heap is fragmented.

**Remediation**: Contact Couchbase Technical Support for analysis.

**Further Reading**: [Memory](https://docs.couchbase.com/server/current/learn/buckets-memory-and-storage/memory.html)

### [](#CB90053)Unknown Storage Engine Check (CB90053)

**Background**: If a bucket uses a storage engine other than "couchstore", ephemeral", or "magma", it is registered as 'Unknown'.

**Condition**: The bucket uses an unknown storage engine.

**Remediation**: Contact Couchbase Technical Support for analysis.

### [](#CB90077)Timing Histogram Underflow (MB-40967) (CB90077)

**Background**: A known issue, [MB-40967](https://issues.couchbase.com/browse/MB-40967) affecting Couchbase Server versions between 6.5.0 and 6.6.0 inclusive, can cause _command timing histograms_ (which track how long Data Service operations take) to no longer return any data once 2.1 billion operations have been executed. This means that there will no longer be any data on how long operations take, which may make it more difficult to diagnose Couchbase Server performance issues.

This issue is fixed in version 6.6.1.

**Condition**: Informational if a susceptible version is in use. Upgraded to a warning if the threshold is breached or exceeded for GET or SET operations.

**Remediation**: Upgrade to Couchbase Server 6.6.1 or later. If this is not feasible, you can use [cbstats reset](https://docs.couchbase.com/server/6.6/cli/cbstats/cbstats-reset.html) to reset these histograms, however the issue will reoccur once 2.1 billion operations are performed again.

**Further Reading**: [MB-40967](https://issues.couchbase.com/browse/MB-40967)

### [](#CB90078)Max TTL of Bucket (CB90078)

**Background**: For versions 5.5.x and <6.0.4, the max TTL for an item in a bucket is applied incorrectly if it exceeds 30 days. Instead of the max TTL being applied as an offset from the current time, it is instead applied as an offset from when memcached started. This will cause all of the documents inside the bucket to expire at the same time.

This issue is fixed in version 6.0.4.

**Relevant To Versions**: Between 5.5.0 and 6.0.3 (inclusive)

**Condition**: Maximum TTL equals or exceeds 30 days on a susceptible version.

**Remediation**: Upgrade to Couchbase Server 6.0.4 or later. If not feasible at the moment, use absolute time if the TTL exceeds 30 days.

**Further Reading**: [MB-37643](https://issues.couchbase.com/browse/MB-37643)

### [](#CB90081)Nodes for Bucket (CB90081)

**Background**: The Data Service nodes on a cluster may not host a particular bucket due to rebalance issues or a node not being accessible. If a bucket is not present on all data nodes then it would introduce bias among the buckets and will be problematic as biased nodes will have to serve more requests for the bucket. This may cause slow requests and compromise cluster integrity.

**Condition**: One or more buckets not present on every data service node in the cluster.

**Remediation**: Verify all nodes are online, and rebalance if necessary. If this still persists, contact Couchbase Technical Support.

### [](#CB90033)Long DCP Names (CB90033)

**Background**: All Database Change Protocol (DCP) streams, including internal replication streams, have an internal name. Before Couchbase Server 7.0, this was implicitly limited to 255 characters (or fewer in some cases), and DCP names that exceed this threshold could result in rebalance failures and other issues. As of Couchbase Server 7.0, these names are explicitly limited to 200 characters. This means that an online upgrade to 7.0 could fail if names longer than 200 but shorter than 255 characters are present.

**Condition**: DCP stream names longer than 200 characters are present, or errors related to them are seen.

**Remediation**: Contact Couchbase Technical Support for analysis.

**Further Reading**: [MB-34280](https://issues.couchbase.com/browse/MB-34280)

### [](#CB90037)Slow Operations (CB90037)

**Background**: Data Service operations that take longer than 500ms will be logged. Seeing one or two should not always be cause for concern, but consistent numbers of slow operations may indicate resource contention on your Data Service nodes. Note that this is different to slow operations logged by the Couchbase SDKs - this health check is purely server-side.

**Condition**: Slow operations logged by the Data Service.

**Remediation**: Verify that your Data Service nodes have adequate system resources.

### [](#CB90052)Malformed vBuckets (CB90052)

**Background**: Files stored in a Bucket have become corrupted and attempting to read specific parts of those files results in a checksum error. This is normally the result of some issue with the underlying disk / file system / OS - either the data on-disk was corrupted at the time it was written, or the data has subsequently become corrupted and hence it cannot be successfully read.

**Condition**: vBucket detected by Couchbase Server containing corrupted data.

**Remediation**: Review your infrastructure for signs of disk problems or any other issues. Alternatively, navigate to your Data storage directory and enter the following command, making sure to fill in the correct data: `/opt/couchbase/bin/couch_dbck --verbose --json <couchbase_server_data_directory>/<bucket>/<malformed_vb_file>`, then take the response and provide it to Couchbase Technical Support.

### [](#CB90055)Metadata Overhead (CB90055)

**Background**: As Couchbase Server stores all of its working documents in memory, if a large portion of that memory is taken up by metadata it can impact performance and force useful documents to be stored on disk rather than memory.

**Condition**: Over 50% of memory is taken up by metadata.

**Remediation**: Increase memory allocation for bucket or change the [evictionPolicy](https://docs.couchbase.com/server/current/manage/manage-buckets/edit-bucket.html#making-changes) of the bucket from `Value-only` (be aware this will have an adverse effect on performance).

**Further Reading**: [Metadata](https://docs.couchbase.com/server/current/learn/data/data.html#metadata), [evictionPolicy](https://docs.couchbase.com/server/current/rest-api/rest-bucket-create.html#evictionpolicy).

### [](#CB90061)Disk Write Queue (CB90061)

**Background**: Having items in the Disk Write Queue for too long could cause applications to backoff and writes to fail. This usually indicates either a sizing issue, or a storage medium failing.

**Condition**: If the time since the object most recently persisted to disk was added to the Disk Write Queue is over 50 seconds, a warning is produced. If that time breaches 100 seconds, then a critical alert is produced.

**Remediation**: Review your hardware for malfunctions or sizing issues. If the problem persists, then please contact Couchbase Technical Support.

**Further Reading**: [Data Service Metrics](#7.0@server:metrics-reference:data-service-metrics.adoc#kv%5Fep%5Fstorage%5Fage%5Fsecond), [Sizing Data Service Nodes](#7.0@server:install:sizing-general.adoc#sizing-data-service-nodes)

### [](#CB90071)Compaction Failure (CB90071)

**Background**: Auto-Compaction can be set to run either at a specific time, or when fragmentation hits a specific level. Auto-Compaction requires some free space on disk in order to run, so if there is none available then compaction cannot run.

**Condition**: Auto-Compaction on bucket can fail if there is insufficient disk space available.

**Remediation**: Allocate more storage to existing Data Service nodes, or more Data Service nodes to the cluster, and attempt to rerun Auto-Compaction. You may also create a new cluster, with more storage, and use unidirectional XDCR to transfer the files over, which should give you the space required for Auto-Compaction. If that is not possible, please contact Couchbase Technical Support.

**Further Reading**: [Auto-Compaction](https://docs.couchbase.com/server/current/manage/manage-settings/configure-compact-settings.html)