---
title: Add a Node and Rebalance
description: A new Enterprise Analytics node can be added to an existing cluster.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/manage-nodes/add-node-and-rebalance.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/2.0/manage/manage-nodes/add-node-and-rebalance.html)

# Add a Node and Rebalance

> A new Enterprise Analytics node can be added to an existing cluster. 

## [](#understanding-node-addition)Understanding Node-Addition

_Full_ and _Cluster_ administrators can use the UI, CLI, or REST API to add Enterprise Analytics nodes to existing clusters. On each node to be added, Enterprise Analytics must have been _installed and started_. The process of node-addition grants to the new node the settings already established for the parent cluster. (See [Manage Settings](../manage-settings/manage-settings.md) for details.) The process allows services to be assigned to the new node. These can either be retained or modified if the new node was _initialized_ with custom disk-paths. All aspects of _provisioning_ that may have occurred on the new node are eliminated: this includes database, services, and settings.

Following node-addition, _rebalance_ is required, to make the new node an active member of the cluster.

### [](#connectivity-considerations)Connectivity Considerations

When adding a node to a cluster, it’s important to follow the connectivity best practices outlined in [Cluster Connectivity and Topology Management](cluster-connectivity-topology-management.md). The scale out procedures vary based on the addressing model in use (Active Load Balancer, Passive Load Balancer, or DNS-Only). To minimize disruptions to client applications, ensure that you follow the procedures detailed in [Rebalance Out (Scale-In)](cluster-connectivity-topology-management.md#rebalance-out-scale-in) section.

### [](#node-addition-and-certificate-management)Node-Addition and Certificate-Management

The examples on this page assume that the default, _system-generated_ certificates provided by Enterprise Analytics continue to be resident on the cluster and the node to be added. In a production or similar context, to ensure security, only administrator-configured certificates should be used on a cluster: these should rely on a well known _Certificate Authority_, whose certificate is loaded as the cluster’s _root_ certificate. (For more information, see [Default Certificates and Certificate Substitution](../../../../server/current/learn/security/certificates.md#server-certificates).)

In such a context, until compatible administrator-configured certificates have been loaded onto it, no node can be added to the cluster. Such activities need to be performed in addition to those shown by the examples on this page.

For more information, see [Adding and Joining New Nodes](../manage-security/configure-server-certificates.md#adding-new-nodes). A complete overview of Couchbase-Server certificate-management is provided in [Certificates](../../../../server/current/learn/security/certificates.md).

### [](#node-certificate-validation)Validating Node Certificates

In Couchbase Enterprise Server, the node-name _must_ be correctly identified in the node certificate as a Subject Alternative Name. If such identification is not correctly configured, failure may occur when uploading the certificate, or when attempting to add or join the node to a cluster. For information, see [Node-Certificate Validation](../../../../server/current/learn/security/certificates.md#node-certificate-validation).

This requirement is automatically handled by the default, _system-generated_ certificates provided by Enterprise Analytics.

## [](#examples-on-this-page-node-addition)Examples on This Page

The examples in the subsections below show how to add the same node to the same one-node cluster; using the [UI](#add-a-node-with-the-ui), the [CLI](#add-a-node-with-the-cli), and the [REST API](#add-a-node-with-the-rest-api) respectively.

* A new node has been started. This is named after its IP address: `127.0.0.2`. It has not been initialized or provisioned.
* The cluster has the Full Administrator username of `Administrator`, and password of `password`.
* The cluster is protected by the default Enterprise Analytics certificate-configuration.

## [](#add-a-node-with-the-ui)Add a Node and Rebalance with the UI

Proceed as follows:

1. Bring up Enterprise Analytics Web Console, and log into cluster `127.0.0.1`, using the Full Administrator username and password. Access the **Servers** tab in the left-hand navigation bar. The **Servers** screen for the cluster displays the name of the only node currently in the cluster, `127.0.0.1`, plus additional information.
2. Ensure that the node to be added has been started. This can be accomplished by checking the IP address and port number for the new node in the address bar of the browser. When you access the new node’s address, you’ll see a welcome interface indicating that Enterprise Analytics is installed and running on the new node, but has not yet been provisioned. Do not use this interface: instead, return to Enterprise Analytics Web Console for the cluster, `127.0.0.1`.
3. In the **Servers** panel for the cluster, click on the **ADD SERVER** button at the upper right. The **Add Server Node** dialog is now displayed.  
> [!NOTE]  
> A warning provided at the top of the dialog - "If the node to be added has already been provisioned, the results of such provisioning will be eliminated and replaced on the node’s addition to the current cluster."
4. Specify the IP address of the node to be added in the **Server IP Address** field. A placeholder password must be specified in the **Password** field, even though the node has not yet been provisioned with one.

Optionally, the **Customize disk storage paths (this node)** checkbox can be checked to display interactive fields that allow to modify the storage paths for the node. When checked, the dialog extends vertically to display interactive fields for **Metadata Disk** and **Cache Disk** data paths. For the current example, the displayed default paths do not need modification.

\+ Click on the **Add Server** button to save the settings. The **Servers** screen is redisplayed, showing that the new node `127.0.0.2` has been successfully added. However, it is not yet taking traffic, and will be activated following a _rebalance_.

1. To perform a rebalance, click on the **Rebalance** button at the upper right. The new node is rebalanced into the cluster, meaning that storage partition ownership that were previously distributed across the original cluster nodes are redistributed across the superset of nodes created by the addition.  
A **Rebalance** dialog is displayed, indicating rebalance progress.  
A new panel appears at the bottom of the **Servers** screen, which also reports rebalance progress with a progress bar and status information.  
When the rebalance is complete, the panel at the bottom of the screen disappears, and the dialog shows completion status with time-completion figures for all services. Additionally, a complete report on the concluded rebalance activity can be downloaded by clicking on the **Download Report** button.  
See the [Rebalance Reference](#rebalance-reference:rebalance-reference.adoc), for information about the contents of the report.
2. Click on the **X** at the upper-right of the dialog to dismiss the dialog.  
The **Servers** screen now displays two rows — one each for servers `127.0.0.1` and `127.0.0.2`. Click on the row for `127.0.0.2` to open it.

#### [](#node-information-within-the-ui)Node Information Within the UI

When the row for a node is open, as is the case here for `127.0.0.2`, information about the node is displayed under its **name**:

* **Addresses** provides at a minimum the _internal_ IP address of the node; and also lists _external_ (that is, _alternate_) IP addresses, if they have been defined — see [Managing Alternate Addresses](../../reference/rest-set-up-alternate-address.md), for information.
* The **Address Family** of the node is specified as either **IPv4** or **IPv6**: see [Manage Address Families](manage-address-families.md), for information.
* **Node-to-Node Encryption** for the cluster is specified as either **enabled** or **disabled**: see [Manage Node-to-Node Encryption](apply-node-to-node-encryption.md).
* The **Version** of the Enterprise Analytics instance on the node, its current **Uptime**, and the **OS** on which it runs are also specified.
* The **RAM Quotas** for each service on the node, and each established **Metadata & Storage Path(s)** are specified. See [Create a Cluster](create-cluster.md) for examples of how to establish these.

### [](#rebalance-failure-notification)Rebalance Failure Notification

If rebalance fails — for example, due to a node’s becoming non-responsive — Enterprise Analytics Web Console displays a notification message indicating the failure.

As this indicates, detailed information can be found by clicking on the **Logs** tab in the left-hand, vertical navigation bar. This brings up the **Logs** screen, containing detailed information about the rebalance failure, including error messages and timestamps.

Information is also provided on the **Rebalance** dialog, showing specific details about which operations failed and any error codes returned.

If an unresponsive node become responsive again, rebalance can be reattempted manually. Alternatively, the handling of a rebalance-failure can be configured to occur automatically, as described immediately [below](#automated-rebalance-failure-handling).

Before attempting rebalance with a reduced number of nodes, assess whether the available resources can support the intended number of replicas. See [Removal](../../../../server/current/learn/clusters-and-availability/removal.md), for guidance.

### [](#automated-rebalance-failure-handling)Automated Rebalance-Failure Handling

The handling of a rebalance-failure can be configured to occur automatically. Configuration occurs by means of the **General** settings screen. Up to 3 _retries_ can be configured. Each retry occurs after the elapsing of a time-period specified by the administrator, in seconds. By default, automated rebalance-failure handling is _not_ enabled. For detailed information, see [Rebalance Settings](../manage-settings/general-settings.md#rebalance-settings).

If automated rebalance-failure handling has been enabled (meaning that between 1 and 3 retries have been specified), following a rebalance failure, notifications appear at the lower left of the main screen of Enterprise Analytics Web Console indicating:

* The rebalance failure status.
* That a retry is planned, in accordance with the configuration made on the **General** settings screen.
* A countdown showing the number of seconds remaining before the retry is commenced, which gradually decrements from the configured maximum to zero, at which point retry is commenced.

If a retry fails, additional retries occur successively; until the maximum configured number have been attempted.

### [](#retry-cancellation)Retry-Cancellation

If one or more retries have been configured, and, following a rebalance failure, a retry is pending, no administrative tasks should be performed on the cluster. Instead, _either_ allow configured retries continue occurring — until one has succeeded, or all have failed; _or_ cancel the entire retry sequence. Then, continue performing administrative tasks as appropriate.

To cancel, left-click on the **CANCEL RETRY** link, on the retry notification. This cancels **all** currently scheduled retries. However, the configured number of retries will be rescheduled for each subsequent, manually initiated rebalance.

Retries can also be cancelled by means of the CLI and the REST API. See [Cancel Retries with the CLI](#cancel-retries-with-the-cli) and [Cancel Retries with the REST API](#cancel-retries-with-the-rest-api), below.

#### [](#restricting-the-addition-of-nodes)Restricting the Addition of Nodes

To ensure cluster-security, in Enterprise Analytics, restrictions can be placed on addition, based on the establishment of _node-naming conventions_. Only nodes whose names correspond to at least one of the stipulated conventions can be added. For information, see [Restrict Node-Addition](../../reference/rest-specify-node-addition-conventions.md).

## [](#add-a-node-with-the-cli)Add a Node and Rebalance with the CLI

To add a new Enterprise Analytics-node to an existing cluster, use the [server-add](../../cli/couchbase-cli-server-add.md) command.

> [!NOTE]
> This command requires that arguments be provided for its `--server-add-username` and `--server-add-password` flags.

In this case, meaningful arguments do not exist, since the new node features an instance of Enterprise Analytics that’s running, but has not been provisioned with a username or password. Therefore, specify placeholder arguments. Additionally, specify that the `data` service be run on the node, once it’s part of the cluster.

> [!NOTE]
> A server to be added (as specified by the value of the `server-add` parameter) can be prefixed with the scheme `https://`, and/or with the port `8091`: if no scheme and no port is specified, `https://` and `8091` are used as defaults. The scheme `http://` cannot be used, nor can the port `8091`: addition must occur over a secure connection.

/opt/enterprise-analytics/bin/couchbase-cli server add -c 127.0.0.1:8091
--username Administrator \
--password password \
--server-add 172.xx.xx.xx
--server-add-username someName \
--server-add-password somePassword \

If successful, the command returns the following:

SUCCESS: Server added

The newly added node must now be rebalanced into the cluster. Use the [rebalance](../../cli/couchbase-cli-rebalance.md) command:

/opt/enterprise-analytics/bin/couchbase-cli
--username Administrator \
--password password

During rebalance, progress is displayed as console output:

Rebalancing
[=====                                                          ] 4.56%

If successful, the command returns the following:

SUCCESS: Rebalance complete

> [!NOTE]
> When the operation is highly complex, it may be desirable to get status on its progress, or stop the operation. See the command reference for [rebalance-status](#cli:cbcli/couchbase-cli-rebalance-status.adoc) and [rebalance-stop](../../cli/couchbase-cli-rebalance-stop.md), for more information.

### [](#cancel-retries-with-the-cli)Cancel Retries with the CLI

_Retries_ (described above, in [Automated Rebalance-Failure Handling](#automated-rebalance-failure-handling)) can be cancelled with the CLI, by means of the [setting-rebalance](../../cli/couchbase-cli-setting-rebalance.md) command.

> [!NOTE]
> Use of `setting-rebalance` for setting and getting the current rebalance-failure configuration is documented in [General Settings](../manage-settings/general-settings.md).

If, following a rebalance failure, a retry is pending, retrieve information about the pending retry as follows.

> [!NOTE]
> The command is piped to the [jq](https://stedolan.github.io/jq/) program, to facilitate readability:

/opt/enterprise-analytics/bin/couchbase-cli
-c 10.143.192.101 \
-u Administrator \
-p password \
--pending-info | jq '.'

This returns the following object:

{
  "retry_rebalance": "pending",
  "rebalance_id": "29d89aa757097523898588c28efd3b4a",
  "type": "rebalance",
  "attempts_remaining": 2,
  "retry_after_secs": 184,
  "known_nodes": [
    "ns_1@10.143.192.101",
    "ns_1@10.143.192.103"
  ],
  "eject_nodes": [],
  "delta_recovery_buckets": "all"
}

The current rebalance sequence can be cancelled by means of the `setting-rebalance` command, specifying the retrieved `rebalance_id`. Enter the following:

/opt/enterprise-analytics/bin/couchbase-cli
-c 10.143.192.101 \
-u Administrator \
-p password \
--cancel \
--rebalance-id 29d89aa757097523898588c28efd3b4a

If successful, the command returns the following:

SUCCESS: Rebalance retry canceled

## [](#add-a-node-with-the-rest-api)Add a Node and Rebalance with the REST API

To add a new Enterprise Analytics-node to an existing cluster, use the `/controller/addNode` URI.

The following command adds node `127.0.0.2` to cluster `127.0.0.1`.

> [!NOTE]
> A server to be added can be prefixed with the scheme `https://`, and/or can be suffixed with the port `18091`: if no scheme or port is specified, `https://` and `18091` are used as defaults.

The scheme `http://` cannot be used; nor can the port `8091`, since in 7.1+, node-addition takes place only over a secure connection.

curl -u Administrator:password -v -X POST \
10.142.181.101:8091/controller/addNode \
-d 'hostname=127.0.0.2&user=someName&password=somePassword'

As with the CLI command shown above, a username and password are expected, even though in this case, the new node has not been provisioned: therefore, placeholders are used. If successful, the command returns the name of the newly added node:

{"otpNode":"ns_1@127.0.0.2"}

The newly added node must now be rebalanced into the cluster. Use the `/controller/rebalance` URI, as follows:

curl -u Administrator:password -v -X POST \
10.142.181.101:8091/controller/rebalance \
-d 'knownNodes=ns_1@10.142.181.101,ns_1@127.0.0.2'

> [!NOTE]
> The `knownNodes` argument lists each of the nodes in the cluster. If successful, the command returns no output.

For further information about adding nodes with the REST API, see [Adding Nodes to Clusters](../../reference/rest-cluster-addnodes.md); on rebalancing, see [Rebalancing the Cluster](../../reference/rest-cluster-rebalance.md).

### [](#cancel-retries-with-the-rest-api)Cancel Retries with the REST API

_Retries_ (described above, in [Automated Rebalance-Failure Handling](#automated-rebalance-failure-handling)) can be cancelled with the REST API.

> [!NOTE]
> Use of the REST API for setting and getting the current rebalance-failure configuration is documented in [Rebalance Settings via REST](../manage-settings/general-settings.md#rebalance-settings-via-rest).

If, following a rebalance failure, a retry is pending, use the `GET /pools/default/pendingRetryRebalance` http method and URI to identify the pending retry, as follows.

> [!NOTE]
> This example uses the [jq](https://stedolan.github.io/jq/) tool, to facilitate readability of output.

curl -u Administrator:password -v -X GET \
http://10.143.192.101:8091/pools/default/pendingRetryRebalance | jq '.'

The output is as follows:

{
  "retry_rebalance": "pending",
  "rebalance_id": "ff5845cdce693db2dce9a9308cbf885d",
  "type": "rebalance",
  "attempts_remaining": 2,
  "retry_after_secs": 291,
  "known_nodes": [
    "ns_1@10.143.192.101",
    "ns_1@10.143.192.103"
  ],
  "eject_nodes": [],
  "delta_recovery_buckets": "all"
}

This indicates that the status of `retry_rebalance` is `pending`; and provides a `rebalance_id` for the process, of `ff5845cdce693db2dce9a9308cbf885d`. This id can be used to cancel the retry. The output also lists the cluster’s nodes, indicates that `2` retry attempts are scheduled to occur if necessary after the current one, and indicates that `291` seconds are still to elapse before the pending retry.

To cancel the pending retry, use the `POST /controller/cancelRebalanceRetry` http method and URI, specifying the retrieved `rebalance_id` as the endpoint:

curl -u Administrator:password -v -X POST \
http://10.143.192.101:8091/controller/cancelRebalanceRetry/ff5845cdce693db2dce9a9308cbf885d

If successful, this produces a `HTTP/1.1 200 OK` success message. Subsequently, the `GET /pools/default/pendingRetryRebalance` http method and URI can again be used, to verify that there is no longer a retry pending. This would be indicated by the following output:

{
  "retry_rebalance": "not_pending"
}

All scheduled retries have thus been successfully cancelled.

Reference pages for these commands are provided at [Get Rebalance-Retry Status](../../reference/rest-get-rebalance-retry.md) and [Cancel Rebalance Retries](../../reference/rest-cancel-rebalance-retry.md).

## [](#next-steps-after-adding-and-rebalancing)Next Steps

As well as supporting a cluster’s adding a node to itself, Enterprise Analytics also supports a node’s joining itself to a cluster (which is essentially the same operation, but proceeding from the node, rather than from the cluster). See [Join a Cluster and Rebalance](join-cluster-and-rebalance.md) for details.