[View original HTML](/enterprise-analytics/current/manage/manage-nodes/join-cluster-and-rebalance.html)

> An independent Enterprise Analytics-node can be joined to an existing cluster. 

## [](#understanding-the-join-operation)Understanding the Join Operation

_Full_ and _Cluster_ administrators can use the UI or REST API to join an Enterprise Analytics nodes to an existing cluster. On each node to be added, Enterprise Analytics must have been _installed and started_. The process of node-addition grants to the new node the settings already established for the parent cluster. (See [Manage Settings](../manage-settings/manage-settings.md) for details.) The process allow services to be assigned to the new node. If the new node was previously _initialized_ with custom disk-paths, these are retained (although if the UI is used for the join operation, these paths can be revised).

Following node-addition, _rebalance_ is required, to make the new node an active member of the cluster.

Note that this process has a similar effect to that described in [Add a Node and Rebalance](add-node-and-rebalance.md). The difference is that here, the process is inverted: rather than a cluster adding a node to itself, a node is joining itself to a cluster.

Note also, however, that a node _cannot_ join itself to a cluster if the node has already been provisioned (that is, has had Full Administrator username and password defined, and may also have had services and memory quotas defined). If the node has been provisioned, the cluster must _add_ the node.

### [](#connectivity-considerations)Connectivity Considerations

When adding a node to a cluster, it’s important to follow the connectivity best practices outlined in [Cluster Connectivity and Topology Management](cluster-connectivity-topology-management.md). The scale out procedures vary based on the addressing model in use (Active Load Balancer, Passive Load Balancer, or DNS-Only). To minimize disruptions to client applications, ensure that you follow the procedures detailed in [Rebalance Out (Scale-In)](cluster-connectivity-topology-management.md#rebalance-out-scale-in) section.

### [](#node-joining-and-certificate-management)Node-Joining and Certificate-Management

The examples on this page assume that the default, _system-generated_ certificates provided by Enterprise Analytics continue to be resident on the cluster and the node to be joined. In a production or similar context, to ensure security, only administrator-configured certificates should be used on a cluster: these should rely on a well known _Certificate Authority_, whose certificate is loaded as the cluster’s _root_ certificate. (For more information, see [Default Certificates and Certificate Substitution](#server:learn:security/certificates.html#server-certificates).)

In such a context, no node can be joined to the cluster until conformant administrator-configured certificates have been loaded onto it — such activities will thus need to be performed in addition to those shown by the examples on this page.

For more information, see [Adding and Joining New Nodes](../manage-security/configure-server-certificates.md#adding-new-nodes). A complete overview of Couchbase-Server certificate-management is provided in [Certificates](../../../../server/current/learn/security/certificates.md).

### [](#node-certificate-validation)Validating Node Certificates

In Couchbase Enterprise Server, the node-name _must_ be correctly identified in the node certificate as a Subject Alternative Name. If such identification is not correctly configured, failure may occur when uploading the certificate, or when attempting to add or join the node to a cluster. For information, see [Node-Certificate Validation](../../../../server/current/learn/security/certificates.md#node-certificate-validation).

|  | This requirement is automatically handled by the default, _system-generated_ certificates provided by Enterprise Analytics. |
|  | --------------------------------------------------------------------------------------------------------------------------- |

## [](#examples-on-this-page-node-addition)Examples on This Page

The examples in the subsections below show how the same uninitialized and unprovisioned node joins itself to the same existing cluster, using the [UI](#join-a-cluster-with-the-ui) and the [REST API](#join-a-cluster-with-the-rest-api) respectively. Node-join is not supported by the CLI.

The examples assume:

* A one-node cluster already exists; and is named after its IP address: `127.0.0.1`. It’s running on Enterprise Analytics, and has the `travel-sample` datasets installed. To access and install this, see [Connecting to Data Sources](../../intro/connecting-to-data-sources.md).
* A new node has been started. This is named after its IP address: `10.142.181.102`. It has not been initialized or provisioned.
* The cluster has the Full Administrator username of `Administrator`, and password of `password`.
* The cluster is protected by the default Couchbase-Server certificate-configuration.

## [](#join-a-cluster-with-the-ui)Join a Cluster with the UI

Proceed as follows:

1. Access the new node’s Enterprise Analytics Web Console instance, at `10.142.181.102:8091`. The welcome screen is displayed, showing the Enterprise Analytics setup interface with options for setting up a new cluster or joining an existing cluster.
2. Click on the **Join Existing Cluster** button to begin the process of joining this node to an existing cluster. This brings up the **Join Cluster** dialog with initial fields for cluster connection details.
3. Click on the **Configure Services & Settings For This Node** control. The dialog expands vertically to reveal additional configuration options. The expanded dialog allows specification of the name and IP address, and the disk paths for the new node. It also requires the username and password of the **Cluster Admin** (although the credentials of the **Full Admin** for the cluster are equally implied), and the name or IP address of the cluster to be joined.  
The expanded interface includes:

  * **Metadata Disk Path**: Field to specify the disk path for metadata storage
  * **Cache Disk Path(s)**: Field to specify the disk path(s) for cache storage

|  | If you do not specify any services, the node joins the cluster as an [arbiter node](../../../../server/current/learn/clusters-and-availability/nodes.md#adding-arbiter-nodes). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
4. Enter the cluster’s IP address (in this case, `127.0.0.1`) in the appropriate field, provide the administrator credentials, and uncheck all **Services** fields except **Data**. Leave all other details unchanged. Then, click on the **Join Cluster** button at the lower right.  
The dashboard for the cluster now appears, indicating successful connection to the cluster. A notification appears at the lower left of the screen confirming that the server association has been completed successfully.
5. Access the **Servers** screen by clicking on the **Servers** tab on the left-hand navigation bar. The display shows that the new node `10.142.181.102` has successfully joined the cluster. However, it is not yet taking traffic, and will be activated following a _rebalance_. The display shows the figure under the **Items** column for `127.0.0.1` indicating items in _active_ vBuckets and 0 items in _replica_ vBuckets. Meanwhile, the **Items** figure for `10.142.181.102` is 0/0, indicating that no items are yet distributed onto that node in either active or replica form.  
To access information about buckets, vBuckets, and intra-cluster replication, see the architecture [Overview](../../../../server/current/learn/architecture-overview.md).
6. To rebalance the cluster and thereby fully add the new node, click on the **Rebalance** button at the upper right. Rebalance occurs and a progress dialog is shown with details about the rebalancing operation, including:

  * Progress bars showing completion status
  * Estimated time remaining for completion  
Following rebalance, the **Servers** display reflects the successful outcome, showing that cluster `127.0.0.1` now contains two fully functioning nodes: `127.0.0.1` and `10.142.181.102`.

|  | If rebalance fails, notifications are duly provided. |
|  | ---------------------------------------------------- |

These are described in [Rebalance Failure Notification](add-node-and-rebalance.md#rebalance-failure-notification).

See also the information provided on [Automated Rebalance-Failure Handling](add-node-and-rebalance.md#automated-rebalance-failure-handling), and the procedure for its set-up, described in [Rebalance Settings](../manage-settings/general-settings.md#rebalance-settings).

### [](#restricting-the-joining-of-nodes)Restricting the Joining of Nodes

To ensure cluster-security, restrictions can be placed on joining, based on the establishment of _node-naming conventions_. Only nodes whose names correspond to at least one of the stipulated conventions can be joined. For information, see [Restrict Node-Addition](../../reference/rest-specify-node-addition-conventions.md).

## [](#join-a-cluster-with-the-rest-api)Join a Cluster with the REST API

To join a node to a cluster with the REST API, use the `/node/controller/doJoinCluster` URI. Enter the following:

curl -u Administrator:password -v -X POST \
http://10.142.181.102:8091/node/controller/doJoinCluster \
-d 'hostname=10.142.181.101&user=Administrator&password=password'

The `hostname` and `user`(-name) and `password` of the Full Administrator for the cluster to be joined are specified. The service specified to be run on the new node is `kv`, signifying the Data Service.

At this point, the newly joined node must be rebalanced into the cluster. Use the `/controller/rebalance` URI, as follows:

curl -u Administrator:password -v -X POST \
10.142.181.101:8091/controller/rebalance \
-d 'knownNodes=ns_1@10.142.181.101,ns_1@10.142.181.102'

Note that the `knownNodes` argument lists each of the nodes in the cluster. If successful, the command returns no output.

For further information about joining a cluster with the REST API, see [Joining Nodes into Clusters](../../reference/rest-cluster-joinnode.md); on rebalancing, see [Rebalancing Nodes](../../reference/rest-cluster-rebalance.md).

## [](#next-steps-after-joining-and-rebalancing)Next Steps

Enterprise Analytics allows you to list the nodes within a cluster. See [List Cluster Nodes](list-cluster-nodes.md) for details.