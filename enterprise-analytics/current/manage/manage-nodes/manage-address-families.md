---
title: Manage Address Families
description: Enterprise Analytics Enterprise Edition supports the IPv4 and IPv6
  address families.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/manage/pages/manage-nodes/manage-address-families.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:manage:manage-nodes/manage-address-families.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-nodes/manage-address-families.html)

# Manage Address Families

> Enterprise Analytics Enterprise Edition supports the IPv4 and IPv6 address families. 

## [](#understanding-address-families)Understanding Address Families

Enterprise Analytics Enterprise Edition supports the IPv4 and IPv6 address families. By default, IPv4 is the address family established for the cluster: this means that IPv4 _must_ be available on all Couchbase-Server ports — if it is _not_ available, the service that is attempting to bind will fail. Provided that IPv4 is available, Enterprise Analytics and its services may also bind using IPv6.

To establish IPv6 as the address family for the cluster, instead of IPv4, configuration changes must be made. An established cluster must be established, both prior to and subsequent to the address-family changeover-process, with _either_ IPv4 _or_ IPv6, for _all_ its nodes.

An Enterprise Analytics-cluster can be established with IPv4 or IPv6 either:

* When the cluster is being created. For information about using the UI, see [Create a Cluster](create-cluster.md). For information about using the CLI, see [Initialize a Node with the CLI](initialize-node.md#initialize-a-node-with-the-cli).
* After the cluster has been created. This procedure, which uses the CLI, is explained on this page, below. Note that the procedure requires the address family to be established with one of the following results specified:

  * The selected address family is required, but the other supported address family can also be used. This is the default setting, with the IPv4 address family being the one required.
  * Only the selected address family can be used.

## [](#changing-address-family-to-IPv6)Changing Address Family

Before attempting to change an existing cluster's address family, note the following:

* The address family can only be changed if each cluster-node is named with a fully qualified domain-name (such as `nodename.clustername.com`). Raw IP addresses _can_ be used to name cluster-nodes, but the cluster must be _created_ with them, and the address family cannot subsequently be changed.
* Each cluster-node must be operating in _dual stack_ mode, thereby supporting both IPv4 and IPv6 addressing.
* DNS records must be managed, to ensure address-resolution to both IPv4 and IPv6 _during_ the changeover, and to either IPv4 or IPv6 _following_ the changeover (at which point, address-resolution can be disabled for the address family no longer used).
* Auto-failover must be disabled prior to the changeover (and can be re-enabled _after_ the changeover).
* Node-to-node encryption must be disabled prior to the changeover (and can be re-enabled _after_ the changeover).
* On each node, when the address-family change occurs, the Analytics Service is restarted.

The following sequence demonstrates how to change the address family for a cluster, using the Couchbase CLI. The sequence assumes:

* Familiarity with the instructions provided in [Manage Node-to-Node Encryption](apply-node-to-node-encryption.md). Since node-to-node encryption-settings are modified during the sequence.
* A pre-existing cluster of two nodes, `node1-devcluster.com` and `node2-devcluster.com`, both running the latest version of Enterprise Analytics Enterprise Edition.
* Node-to-node encryption initially enabled.
* Auto-failover initially enabled.

Proceed as follows:

1. Retrieve the current address-family setting.  
This can be accomplished by means of the [ip-family](../../cli/couchbase-cli-ip-family.md) CLI command, using the `--get` flag:  
/opt/enterprise-analytics/bin/couchbase-cli
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--get  
The output from this command consists of one of the following messages:

  * `Cluster using ipv4`: Every node in the cluster is using IPv4, and may use IPv6.
  * `Cluster using ipv6`: Every node in the cluster is using IPv6, and may use IPv4.
  * `Cluster using ipv4only`: Every node in the cluster is using IPv4, and may _not_ use IPv6\. (This message is generated only by Enterprise Analytics Version 7.0.2 and later.)
  * `Cluster using ipv6only`: Every node in the cluster is using IPv6, and may _not_ use IPv4\. (This message is generated only by Enterprise Analytics Version 7.0.2 and later.)
  * `Cluster is in mixed mode`: The cluster contains some nodes that are using IPv4, and others that are using IPv6: this situation is indicative of an _error_, likely incurred during a previous, attempted reconfiguration of the address family for the cluster. The error should be fixed, by re-establishing the address family for the whole cluster.  
  The remaining steps below assume that the address family of the cluster is to be changed to IPv6.
2. Switch off auto-failover.  
Auto-failover must be disabled, for the address family to be modified. Use the `setting-autofailover` CLI command, as follows:  
/opt/enterprise-analytics/bin/couchbase-cli
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--enable-auto-failover 0  
If successful, this provides the following output:  
SUCCESS: Auto-failover settings modified
3. Switch off node-to-node encryption, if appropriate.  
Node-to-node encryption must be _disabled_, before the address family can be changed. To check the status of node-to-node encryption, use the [node-to-node-encryption](../../cli/couchbase-cli-node-to-node-encryption.md) CLI command, specifying the `--get` flag:  
/opt/enterprise-analytics/bin/couchbase-cli
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--get  
The output from this command is one of two messages: either `Node-to-node encryption is disabled`, indicating that it does _not_ need to be disabled; or `Node-to-node encryption is enabled`. which indicates that it _does_.  
If node-to-node encryption needs to be disabled, ensure that the `clusterEncryptionLevel` for the cluster is set to `control`, rather than all — otherwise node-to-node encryption cannot be disabled. See the instructions provided in [Manage Node-to-Node Encryption](apply-node-to-node-encryption.md).  
When the `clusterEncryptionLevel` for the cluster has been set to `control`, disable node-to-node encryption using the [node-to-node-encryption](../../cli/couchbase-cli-node-to-node-encryption.md) command with the `--disable` flag:  
/opt/enterprise-analytics/bin/couchbase-cli
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--disable  
If this command is successful, the output is as follows:  
Turned off encryption for node: http://node1-devcluster.com:8091  
Turned off encryption for node: http://node2-devcluster.com:8091  
SUCCESS: Switched node-to-node encryption off
4. Change the address family for the cluster to IPv6.  
Use the [ip-family](#cli:cbcli/couchbase-cli-ip-family.adoc) CLI command, using the `--set` and `--ipv6` flags, as follows:  
/opt/enterprise-analytics/bin/couchbase-cli
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--set \
--ipv6  
The `--set` flag indicates that an address-family setting is to be made. The `--ipv6` flag specifies that the cluster will from this point require that the IPv6 family be available for communications — communication with the IPv4 family is still supported. (Note that if communication with the IPv4 family should be absolutely prohibited, the `--ipv6only` flag should be used, instead of the `--ipv6` flag.)  
If successful, the command provides the following output:  
Switched ip family for node: http://node1-devcluster.com:8091  
Switched ip family for node: http://node2-devcluster.com:8091  
SUCCESS: Switched ip family of the cluster  
The output indicates that the IP family has been successfully established, and thus changed for each cluster in the node.
5. If appropriate, switch node-to-node encryption back on. Use the `node-to-node-encryption` CLI command, specifying the `--enable` flag:  
/opt/enterprise-analytics/bin/couchbase-cli
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--enable  
If the command succeeds, the following output is displayed:  
Turned on encryption for node: http://node1-devcluster.com:8091  
Turned on encryption for node: http://node2-devcluster.com:8091  
SUCCESS: Switched node-to-node encryption on
6. If appropriate, switch auto-failover back on.  
/opt/enterprise-analytics/bin/couchbase-cli
-c http://node1-devcluster.com:8091 \
-u Administrator \
-p password \
--enable-auto-failover 1 \
--auto-failover-timeout 120 \
--enable-failover-of-server-groups 1 \
--max-failovers 2 \
--can-abort-rebalance 1  
The parameter values specify that auto-failover be enabled with a timeout of 120 seconds; with a maximum of two, sequential automated failovers able to occur, prior to administrator intervention being required. Automated failover of server groups is enabled, as is the aborting of rebalance.  
If the command succeeds, and the settings are successfully modified, the following output is displayed:  
SUCCESS: Auto-failover settings modified

This concludes the sequence of commands: the cluster is now running with the IPv6 address family.