---
title: Create a Cluster
description: A new Enterprise Analytics node can be <em>provisioned</em>, to
  establish its Full Administrator credentials, its service-assignments, and its
  memory quotas. At this point, it becomes a <em>cluster</em> of one node.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/manage/pages/manage-nodes/create-cluster.adoc
pubDate: 2026-04-15T05:26:28.652Z
link: xref:enterprise-analytics:manage:manage-nodes/create-cluster.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-nodes/create-cluster.html)

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

The **Welcome** screen lets you either **Setup New Cluster**, or **Join Existing Cluster**. Information about joining an existing cluster is provided in [Join a Cluster and Rebalance](join-cluster-and-rebalance.md). To set up a new cluster, click **Setup New Cluster**.

### [](#set-up-a-new-cluster)Set Up a New Cluster

The **New Cluster** screen now appears. It contains fields for initial cluster configuration.

The fields displayed on the screen are:

* **Cluster Name**: Your choice of name for the cluster to be created. For information about cluster-naming, see [Naming Clusters and Nodes](../../../../server/current/learn/clusters-and-availability/nodes.md#naming-clusters-and-nodes).
* **Create Admin Username**: Your choice of username, for yourself: the _Full Administrator_ for this cluster. You'll have read-write access to all Enterprise Analytics resources, including the ability to create new users with defined roles and corresponding privileges.  
> [!NOTE]  
> Enterprise Analytics prohibits use of the following characters in usernames: `( ) < > @ , ; : \ " / [ ] ? = { }`. Usernames _may not_ be more than 128 UTF-8 characters in length. Couchbase recommends keeping them to no more than 64 UTF-8 characters in length so they display correctly onscreen.  
For more information, see [Usernames and Passwords](../../../../server/current/learn/security/usernames-and-passwords.md).
* **Create Password**: Your choice of password, for yourself: the Full Administrator for this cluster. The only default format-requirement is that the password be at least 6 characters in length. However, following cluster-initialization, you can modify and improve the default password-policy, by means of the Couchbase CLI [setting-password-policy](../../cli/couchbase-cli-setting-password-policy.md) command.

For more information, see [Usernames and Passwords](../../cli/couchbase-cli-setting-password-policy.md).

When you have entered appropriate data into each field, click **Next: Accept Terms**.

### [](#accept-terms)Accept Terms and Register for Updates

The **New Cluster** screen now changes to show the **Terms and Conditions** for Enterprise Analytics.

The terms and conditions for the product are displayed in a panel. To view a web-based document containing the terms and conditions, click the **terms and conditions** link.

After reviewing the terms and conditions, select **I accept the terms & conditions**.

Next, determine whether you want to share usage information with Couchbase. Couchbase recommends sharing usage information to benefit from regular software update notifications. **Share usage information with Couchbase and get software update notifications** is selected by default. For more information about sharing usage with Couchbase, see the **Privacy FAQ** and **Couchbase Privacy Policy**.

If you click **Finish With Defaults**, cluster-initialization is performed with default settings, provided by Couchbase. The Enterprise Analytics Web Console **Dashboard** appears, and your configuration is complete. _All_ Couchbase services will have been deployed.

### [](#configure-couchbase-server)Configure Enterprise Analytics

The **Configure** screen now appears. It provides detailed configuration options for the new cluster.

The displayed fields are:

* **Host Name / IP Address**: The data in this field determines the name that will be used for this node. The field has been populated with the _loopback_ address, `127.0.0.1`, which can be used until a second node is added to the cluster, at which point the name will automatically be changed to the IP address of the underlying host. If you want, you can substitute the IP address of the underlying host now, or you can substitute the fully qualified hostname of the underlying host, if one exists. If you want to use a fully qualified hostname, you _must_ specify it now, since a node's name cannot be changed from an IP address to a hostname once the cluster has become a multi-node cluster. For information about naming, see [Naming Clusters and Nodes](../../../../server/current/learn/clusters-and-availability/nodes.md#naming-clusters-and-nodes).
* **enable node encryption**: Select to enable _node-to-node_ encryption for the cluster. Use of IP address families and node-to-node encryption is described in [Node-to-Node Encryption](../../cli/couchbase-cli-node-to-node-encryption.md).
* **IP Family Preference**: Select the appropriate radio-button. If **IPv4** or **IPv6** is selected, the corresponding address family is required, but the other supported address family can also be used. (This is the default setting, with the IPv4 address family being required.) If **IPv4-only** or **IPv6-only** is selected, only the corresponding address family can be used.

> [!NOTE]
> The **IPv4-only** and **IPv6-only** options are available only with Enterprise Analytics Version 7.0.2 and later.

* **Enterprise Analytics Memory Quota**: A field that allows specify how much memory should be allocated. Select for both the current node and for each node you may subsequently add to the cluster.

The total RAM available is displayed below this figure, at the center. If your memory allocation is excessive, a notification warns you, and you must lessen your allocation.

* **Blob Storage Configuration**: This category allows you to specify the path and region to the directory in which blob data is stored.

  * **Storage Scheme**: Select the storage scheme to be used for blob data. The options are:

    * AWS S3
    * S3-Compatible Storage
    * Azure Blob Storage

    * **Bucket Name**: Enter the name of the bucket to be used for blob data.
    * **Bucket Path Prefix**: Enter the path prefix to be used for blob data. This is the path to the directory in which blob data is stored.
    * **Bucket Region**: Enter the region to be used for blob data.

    * **Storage Endpoint** — The URL of the S3-compatible storage endpoint. For example: `<https://my-object-storage:18082>`. You can edit this field.
    * **Bucket Name** — Enter the name of the bucket to be used for blob data.
    * **Bucket Region** — Enter the region to be used for blob data.
    * **Bucket Path Prefix** — Enter the path prefix to be used for blob data. This is the path to the directory in which blob data is stored.
    * **Storage Endpoint Certificates** — One or more PEM-encoded certificates to trust when connecting to the storage endpoint. Provide multiple certificates to support certificate rotation. Displayed only when the endpoint uses HTTPS and **Disable SSL Verification** is unchecked.

    * **Blob service endpoint** — The URL of the Azure Blob Storage service endpoint. For example: `<https://myaccount.blob.core.windows.net>`.
    * **Container (Bucket) Name** — Enter the name of the container to be used for blob data.
    * **Container Path Prefix** — Enter the path prefix to be used for blob data. This is the path to the directory in which blob data is stored.
* **Authentication** — Specifies how Enterprise Analytics authenticates with selected object storage. Select one of the following options:

  * **Standard Credential Chain** — Uses the default AWS provider chain to obtain credentials automatically. This includes instance profiles, environment variables, and other standard credential sources.
  * **Static Credentials** — Allows you to supply credentials directly. When selected, the following fields appear:

    * **Access Key ID** — The access key ID for the selected object storage.
    * **Secret Access Key** — The secret access key for the selected object storage. If a key is already configured, the field displays the placeholder **Enter new value to change**. Leave the field empty to retain the existing key.
  * **Anonymous** — Accesses the bucket without credentials. Use this only for publicly accessible buckets.
* **Local Storage Configuration**: This category allows you to specify the path to the directory in which local data is stored.

  * **Metadata Disk Path**: Enter the path to the directory in which metadata is stored. This is the directory in which Enterprise Analytics stores its metadata, such as cluster configuration and user data.
  * **Cache Disk Paths**: Enter the path to the directory in which cache data is stored.  
> [!NOTE]  
> You cannot change cache disk paths after setup.

When you have finished entering your configuration-details, click **Save & Finish**. This configures the server accordingly, and brings up the Enterprise Analytics Web Console **Dashboard**, for the first time.

The Dashboard is the main landing page after logging in. It consists of a **banner** with interactive controls; a **main panel**, which allows display of data and configuration fields (and which, on initial appearance, is unpopulated); a **left-hand navigation bar**, which allows the main panel's content to be determined; and a **lower panel**, which displays current status on the cluster. These are described in [Understanding the Dashboard](../manage-ui/manage-ui.md#understanding-the-dashboard), which is part of the page that introduces all features of [Enterprise Analytics Web Console](../manage-ui/manage-ui.md).

### [](#new-custer-set-up-next-steps)New-Cluster Set-Up: Next Steps

If this is the first node in the cluster, a notification appears, stating that no nodes are currently defined. A _node_ is the principal unit of data-storage used by Enterprise Analytics. To save and subsequently use documents and other objects, you must create one or more databases.

As specified by the notification, you can go to **Workbench**, and begin database-creation; or add a **sample database**. A description of how to create, edit, flush, and delete databases can be found in the section [intro:connecting-to-data-sources.adoc#import-the-travel-sample-collections](../../intro/connecting-to-data-sources.md#import-the-travel-sample-collections).

For more details on Databases, see [Manage Databases](../../sources/manage-databases.md).

Three different kinds of database exist, so you may want to familiarize yourself with their properties before you start database-creation.

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

If the node is successfully provisioned, it's thereby initialized as a cluster. The following output is displayed:

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

The provisioned node is now initialized as a cluster, and is available at the given IP address and port number. The default disk-paths for data, indexes, and analytics are used, since no custom paths were specified by means of `/nodes/self/controller/settings` (see [Initialize a Node with the REST API](initialize-node.md#initialize-node-with-the-rest-api).)

## [](#next-steps-after-provisioning)Next Steps

Following provisioning, an Enterprise Analytics node constitutes a _Couchbase Cluster_ of one node. From this point, more nodes can be _added_ to the cluster. See [Add a Node and Rebalance](add-node-and-rebalance.md), for details.