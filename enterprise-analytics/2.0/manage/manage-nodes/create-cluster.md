---
title: Create a Cluster
description: A new Enterprise Analytics node can be <em>provisioned</em>, to
  establish its Full Administrator credentials, its service-assignments, and its
  memory quotas. At this point, it becomes a <em>cluster</em> of one node.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/manage-nodes/create-cluster.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.0@enterprise-analytics:manage:manage-nodes/create-cluster.adoc[]
---

[View original HTML](/enterprise-analytics/2.0/manage/manage-nodes/create-cluster.html)

# Create a Cluster

> A new Enterprise Analytics node can be _provisioned_, to establish its Full Administrator credentials, its service-assignments, and its memory quotas. At this point, it becomes a _cluster_ of one node. 

## [](#understanding-provisioning)Understanding Provisioning

_Provisioning_ establishes the Full Administrator credentials for the server, and specifies its service-assignments and memory-quota allocations. Provisioning can occur as part of establishing the node as either:

* The first in a new cluster. Credentials will apply to all other nodes subsequently added, as will memory allocations. Service-assignments are for this node only.
* A new member of an existing cluster. Credentials and memory allocations are inherited. Service-assignments are made independently for this node.

## [](#examples-on-this-page-node-initialization)Examples on This Page

The examples in the subsections below show how to provision the same node, so that it becomes the first in a new cluster, using the [UI](#provision-a-node-with-the-ui), the [CLI](#provision-a-node-with-the-cli), and the [REST API](#provision-a-node-with-the-rest-api) respectively.

The examples assume that the node has _not_ previously been initialized.

## [](#provision-a-node-with-the-ui)Provision a Node with the UI

Enterprise Analytics Web Console is, by default, available on port `8091`. Therefore, once Enterprise Analytics has been installed on a machine, the console can be accessed over the network at `http://<machine-ip-address>:8091/` or `http://<machine-hostname>:8091/`. It can be accessed from the machine on which Enterprise Analytics was installed at `http://localhost:8091`.

If you have chosen to run Enterprise Analytics on a port other than `8091`, connect on that specific port.

For additional, detailed information about using hostnames and IP addresses, see [Naming Clusters and Nodes](../../../../server/current/learn/clusters-and-availability/nodes.md#naming-clusters-and-nodes).

Once you have connected, the **Welcome** screen appears. It presents two main options: **Setup New Cluster** and **Join Existing Cluster**.

The **Welcome** screen lets you either **Setup New Cluster**, or **Join Existing Cluster**. information about joining an existing cluster is provided in [Join a Cluster and Rebalance](join-cluster-and-rebalance.md). To set up a new cluster, click on **Setup New Cluster**.

### [](#set-up-a-new-cluster)Set Up a New Cluster

The **New Cluster** screen now appears. It contains fields for initial cluster configuration.

The fields displayed on the screen are:

* **Cluster Name**: Your choice of name for the cluster to be created. For information about cluster-naming, see [Naming Clusters and Nodes](../../../../server/current/learn/clusters-and-availability/nodes.md#naming-clusters-and-nodes).
* **Create Admin Username**: Your choice of username, for yourself: the _Full Administrator_ for this cluster. You will have read-write access to all Enterprise Analytics resources; including the ability to create new users with defined roles and corresponding privileges.  
> [!NOTE]  
> Enterprise Analytics prohibits use of the following characters in usernames: `( ) < > @ , ; : \ " / [ ] ? = { }`. Usernames _may not_ be more than 128 UTF-8 characters in length; and it is recommended that they be no more than 64 UTF-8 characters in length, in order to ensure successful onscreen display.  
For more information, see [Usernames and Passwords](../../../../server/current/learn/security/usernames-and-passwords.md).
* **Create Password**: Your choice of password, for yourself: the Full Administrator for this cluster. The only default format-requirement is that the password be at least 6 characters in length. However, following cluster-initialization, you can modify (and indeed strengthen) the default password-policy, by means of the Couchbase CLI [setting-password-policy](../../cli/couchbase-cli-setting-password-policy.md) command.

For more information, see [Usernames and Passwords](../../cli/couchbase-cli-setting-password-policy.md).

When you have entered appropriate data into each field, click on the **Next: Accept Terms** button, at the lower right.

### [](#accept-terms)Accept Terms and Register for Updates

The **New Cluster** screen now changes to show the **Terms and Conditions** for Enterprise Analytics.

The terms and conditions for use of the product are displayed in a panel. Check the **I accept the terms & conditions** checkbox, which is immediately below the panel.

You may click in the **terms and conditions** link, to access a web-based document, containing the text.

Next, determine whether you wish to share usage information with Couchbase: a full account of this process is provided in the panel beneath the header **Software Updates & Sharing Usage Information With Couchbase**. You are strongly recommended to share information, and thereby benefit from regular software update notifications: the checkbox marked **Share usage information with Couchbase and get software update notifications** is checked by default. (Note that if you wish, you may click on the **Privacy FAQ** and **Couchbase Privacy Policy** links, to read web-based versions of those documents.)

You now have two options for proceeding. If you click on the **Finish With Defaults** button, cluster-initialization is performed with default settings, provided by Couchbase; the Enterprise Analytics Web Console **Dashboard** appears, and your configuration is complete. _All_ Couchbase services will have been deployed.

### [](#configure-couchbase-server)Configure Enterprise Analytics

The **Configure** screen now appears. It provides detailed configuration options for the new cluster.

The displayed fields are:

* **Host Name / IP Address**: The data in this field determines the name that will be used for this node. The field has been populated with the _loopback_ address, `127.0.0.1`, which can be used until a second node is added to the cluster, at which point the name will automatically be changed to the IP address of the underlying host. If you wish, you can substitute the IP address of the underlying host now, or you can substitute the fully qualified hostname of the underlying host, if one exists. If you _do_ wish to use a fully qualified hostname, you _must_ specify it now, since a node’s name cannot be changed from an IP address to a hostname once the cluster has become a multi-node cluster. For information about naming, see [Naming Clusters and Nodes](../../../../server/current/learn/clusters-and-availability/nodes.md#naming-clusters-and-nodes).
* **enable node encryption**: Check the checkbox to enable _node-to-node_ encryption for the cluster. Use of IP address families and node-to-node encryption is described in [Node-to-Node Encryption](../../cli/couchbase-cli-node-to-node-encryption.md).
* **IP Family Preference**: Select the appropriate radio-button. If **IPv4** or **IPv6** is selected, the corresponding address family is required, but the other supported address family can also be used. (This is the default setting, with the IPv4 address family being required.) If **IPv4-only** or **IPv6-only** is selected, only the corresponding address family can be used. (Note that the **IPv4-only** and **IPv6-only** options are available only with Enterprise Analytics Version 7.0.2 and later.)
* **Enterprise Analytics Memory Quota**: A field that allows specify how much memory should be allocated. Select for both the current node and for each node you may subsequently add to the cluster.

The total RAM available is displayed below this figure, at the center. If your memory allocation is excessive, a notification warns you, and you must lessen your allocation.

* **Blob Storage Configuration**: This category allows you to specify the path and region to the directory in which blob data is stored.

  * **Blob Storage Scheme**: Select the storage scheme to be used for blob data. The options are **AWS S3** (the default) and [S3-Compatible Storage](object-storage.md).
  * **Bucket name**: Enter the name of the bucket to be used for blob data.
  * **Bucket path prefix**: Enter the path prefix to be used for blob data. This is the path to the directory in which blob data is stored.
  * **Bucket Region**: Enter the region to be used for blob data.
  * **Use Anonymous Authentication**: When enabled, you can interact with the blob storage without requiring explicit credentials.
  * **Use Path Style Addressing**: When enabled, the S3-compatible storage uses path-style URLs for accessing storage.
  * **Disable SSL Verification**: When enabled, SSL certificate verification is disabled for S3-compatible storage.
* **Local Storage Configuration**: This category allows you to specify the path to the directory in which local data is stored.

  * **Metadata Disk Path**: Enter the path to the directory in which metadata is stored. This is the directory in which Enterprise Analytics stores its metadata, such as cluster configuration and user data.
  * **Cache Disk Path(s)**: Enter the path to the directory in which cache data is stored.

> [!NOTE]
> Path(s) cannot be changed after setup.

When you have finished entering your configuration-details, click on the **Save & Finish** button, at the lower right. This configures the server accordingly, and brings up the Enterprise Analytics Web Console **Dashboard**, for the first time.

The Dashboard is the main landing page after logging in. It consists of a **banner** with interactive controls; a **main panel**, which allows display of data and configuration fields (and which, on initial appearance, is unpopulated); a **left-hand navigation bar**, which allows the main panel’s content to be determined; and a **lower panel**, which displays current status on the cluster. These are described in [Understanding the Dashboard](../manage-ui/manage-ui.md#understanding-the-dashboard), which is part of the page that introduces all features of [Enterprise Analytics Web Console](../manage-ui/manage-ui.md).

### [](#new-custer-set-up-next-steps)New-Cluster Set-Up: Next Steps

If this is the first node in the cluster, a notification appears, stating that no nodes are currently defined. A _node_ is the principal unit of data-storage used by Enterprise Analytics. In order to save and subsequently access documents and other objects, you must create one or more databases.

As specified by the notification, you can go to **Workbench**, and begin database-creation; or add a **sample database**. A description of how to create, edit, flush, and delete databases can be found in the section [intro:connecting-to-data-sources.adoc#import-the-travel-sample-collections](../../intro/connecting-to-data-sources.md#import-the-travel-sample-collections).

For more details on Databases, see [Manage Databases](../../sources/manage-databases.md).

There are three different kinds of database, so you may wish to familiarize yourself with their properties, before you start database-creation.

> [!NOTE]
> _Sample_ databases already contain data, and so are ready for your immediate experimentation and testing.

The database that you create must be accessed securely: therefore, Enterprise Analytics provides a system of _Role-Based Access Control_ (RBAC), which must be used by administrators and applications that wish to access databases. Each administrator and application is considered to be a _user_, and must perform database-access by passing a username and password. For information about how to set up RBAC users so that they can access the databases you create, see [Authorization](../../../../server/current/learn/security/authorization-overview.md).

To continue building your cluster by means of node-addition, proceed to [Add a Node and Rebalance](add-node-and-rebalance.md).

## [](#provision-a-node-with-the-cli)Provision a Node with the CLI

To provision a node with the CLI, use the `cluster-init` command, as follows:

couchbase-cli cluster-init -c 10.142.181.101 \
--cluster-username Administrator \
--cluster-password password \
--data \
----cluster-analytics-ramsize 1024\

This provisions node `10.142.181.101` with the Full Administrator username and password, and establishes three services. It also specifies the memory quota.

If the node is successfully provisioned, it’s thereby initialized as a cluster. The following output is displayed:

SUCCESS: Cluster initialized

> [!NOTE]
> The IP-address family and the disk-paths for data, indexes, and analytics are, by this use of `cluster-init`, either left as the defaults, or as the values already specified by prior use of the `node-init` command: see [Initialize a Node with the CLI](initialize-node.md#initialize-node-with-the-cli).

For more information about the `cluster-init` command, including additional flags that can be specified, see the command reference for [cluster-init](../../cli/couchbase-cli-cluster-init.md).

## [](#provision-a-node-with-the-rest-api)Provision a Node with the REST API

The following REST API examples set up a single-node Couchbase-Server cluster, administrative credentials, and a RAM quota. The following methods are used:

* `/pools/default`: Allows memory quotas to be specified.
* `/settings/web`: Allows Full Administrator username and password to be specified. Requires the REST API port to be specified also, with `SAME` accepted as the default.

Enter the following, to provision a node to establish quotas for Data Service and Index Service, and to establish Full Administrator credentials.

curl  -v -X POST http://10.142.181.101:8091/pools/default \
-d 'cbasMemoryQuota=1024'

curl  -u Administrator:password -v -X POST \
http://10.142.181.101:8091/settings/web \
-d 'password=password&username=Administrator&port=SAME'

The last command, which establishes credentials, completes provisioning. The following output is provided:

{"newBaseUri":"http://10.142.181.101:8091/"}

The provisioned node has thus been initialized as a cluster, and is available at the given IP address and port number. Note that the default disk-paths for data, indexes, and analytics will be used, since no custom paths were specified by means of `/nodes/self/controller/settings` (see [Initialize a Node with the REST API](initialize-node.md#initialize-node-with-the-rest-api).)

## [](#next-steps-after-provisioning)Next Steps

Following provisioning, an Enterprise Analytics node constitutes a _Couchbase Cluster_ of one node. From this point, more nodes can be _added_ to the cluster. See [Add a Node and Rebalance](add-node-and-rebalance.md), for details.