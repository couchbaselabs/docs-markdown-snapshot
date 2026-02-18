---
title: Couchbase Web Console
description: The features of Couchbase Server can be managed by means of
  Couchbase Web Console.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/manage/pages/manage-ui/manage-ui.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/manage/manage-ui/manage-ui.html)

# Couchbase Web Console

> The features of Couchbase Server can be managed by means of Couchbase Web Console. 

## [](#understanding-couchbase-web-console)Understanding Couchbase Web Console

_Couchbase Web Console_ is a browser-based, interactive graphical facility that supports the management of Couchbase Server. This includes:

* Monitoring performance and server-state, by means of constantly updated statistics, displayed in customizable, interactive charts.
* Configuring services, including indexes.
* Adding and removing cluster-nodes.
* Setting up Cross Data Center Replication.
* Interactively composing documents, and executing queries.
* Managing security; including the addition of users, the assignment of roles, and the configuration of external authentication mechanisms.

The range of features made available depends on the _roles_ that have been assigned to the user who logs into the console. If the user has been assigned the _Full Administrator_ role, they have complete access to all features; and can therefore read, write, execute, and manage without constraint. Other roles limit the feature-range. For detailed information, see [Roles](../../learn/security/roles.md).

This page provides an overview of the complete feature-set made available by Couchbase Web Console. In many cases, detailed explanations of the user interface is provided elsewhere in the documentation-set, in correspondence with the supported feature. Links are provided in each case.

## [](#accessing-the-console)Accessing the Console

Couchbase Web Console is typically accessible at port _8091_, of the host system, although the port number may be different if _secure_ console-access has been established: see [Manage Console Access](../manage-security/manage-console-access.md), for information. When the appropriate port is accessed, the following interface is displayed:

![setupScreen](../_images/manage-ui/setupScreen.png) 

The interface provides two options:

* **Setup New Cluster**: which establishes the current server as an independent cluster of one node, to which other nodes can subsequently be added.
* **Join Existing Cluster**: which establishes the current server as a node that is part of a pre-existing cluster.

These procedures, which include establishing credentials for administrator-authentication, are described in detail in [Create a Cluster](../manage-nodes/create-cluster.md). The remaining information on this page assumes that a cluster of one node has been established. The features of the console will be portrayed in their entirety, as visible to the _Full Administrator_.

## [](#authenticating-with-the-console)Authenticating with the Console

Once the cluster is running, all its administrators must _authenticate_, in order to access its features. Therefore, when port _8091_ is accessed by means of the browser, the following interface is displayed:

![loginScreen](../_images/manage-ui/loginScreen.png) 

Enter username and password, and left-click on the **Sign In** button to access the console.

Detailed information on authenticating with Couchbase Server is provided in [Authentication](../../learn/security/authentication-overview.md).

## [](#understanding-the-dashboard)Understanding the Dashboard

On the user’s successful login, the console displays the **Dashboard**. If this is the user’s first-time access, the appearance is as follows:

![dashboardInitial](../_images/manage-ui/dashboardInitial.png) 

The display thus consists of a **banner** with interactive controls; a **main panel**, which allows display of data and configuration fields; a **left-hand navigation bar**, which allows the main panel’s content to be determined; and a **lower panel**, which displays current status on the cluster. These are described below.

### [](#console-banner)Banner

At the left, the banner features the name of the console, as determined during server-setup. It also displays the name of the currently displayed screen, **Dashboard**. At the right, it provides information identifying the version of the server that is being run, and the build number.

In the white horizontal band immediately above the banner, at the right-hand side, three interactive options appear:

* **activity**. When Couchbase Server is engaged in an activity of any considerable duration (such as loading data, or distributing data across multiple nodes), an alert is provided; in the form of an interactive, orange icon. Left-click on this, to display the notification. For example:  
![activityAlert](../_images/manage-ui/activityAlert.png)
* **help**. Tabs that respectively allow all customers to access documentation for the server-release; and allow certain customers to contact Couchbase Customer Support.
* **Administrator**. Tabs that respectively allow administrators to redefine their password; and to sign out of the console.

### [](#console-main-panel)Main Panel

The content of the main panel changes, based on selections made by the user in the left-hand navigation bar. The default display is that of the **Dashboard**.

Initially, a notification appears; explaining that no _data buckets_ currently exist, and providing options for the addition of buckets. Such addition is required prior to **Dashboard**\-customization; since all statistics will be presented in relation to existing buckets. The procedure for adding a _sample bucket_ is provided in [Install Sample Buckets](../manage-settings/install-sample-buckets.md). After this procedure is followed for the `travel-sample` bucket, the **Dashboard** screen appears as follows:

![ClusterOverview](../_images/manage-ui/ClusterOverview.png) 

The **Cluster Overview** thus displays animated charts that provide a variety of information on the status of data-management on the cluster. Additional information can be displayed by left-clicking on the **Node Resources** tab.

The **Cluster Overview** display can be alternated with the **All Services** display, by means of the pull-down menu at the upper left:

![DashboardToggle](../_images/manage-ui/DashboardToggle.png) 

The user is also able to add charts incrementally, in order to display continuously updated sets of statistics. In consequence, the **Dashboard** is assembled differently by each user. Detailed information on incrementally adding charts and on how to read them is provided in [Manage Statistics](../manage-statistics/manage-statistics.md).

### [](#console-left-hand-nav)Navigation Bar

The vertical _navigation bar_, which appears at the left-hand side, provides a tab for each of the major features that can be accessed and managed. On initial console-access, the **Dashboard** tab, at the top, is selected by default. Information is provided below on each of the possible selections.

Note that when the mouse cursor is hovered over elements in the navigation bar, a toggle appears at the lower left. Left-clicking on this causes the navigation bar to be collapsed, thereby freeing up more horizontal space for the main panel.

![navBarToggle](../_images/manage-ui/navBarToggle.png) 

The toggle remains accessible, and can be used to restore the navigation bar at any time.

### [](#console-lower-panel)Lower Panel

The _lower panel_ provides information on cluster status.

* _Nodes_ are represented by icons in green, orange, or red; according to whether they are _active_, _failed-over_, _pending-rebalance_, or _inactive_. Detailed information on nodes, their status, and how they can be managed is provided in [Manage Nodes and Clusters](../manage-nodes/node-management-overview.md).
* Installed _Services_ and _Cross Data Center Replication_ are represented by icons in green or grey, If a service-icon is green, this indicates that it is installed and running. If it is grey, it is not installed. Cross Data Center Replication (_XDCR_) does not require installation; and is either green or grey depending on whether a replication is in process.

Information on services is provided in [Services](../../learn/services-and-indexes/services/services.md). Information on XDCR is provided in [Cross Data Center Replication (XDCR)](../../learn/clusters-and-availability/xdcr-overview.md).

System notifications are shown, as required, in the lower left-hand corner of the main panel. These are green to indicate success, orange to indicate warnings of actual or potential problems, and red to indicate failure. For example:

![notificationTypes](../_images/manage-ui/notificationTypes.png) 

Note that red notifications provide a red, interactive `X`, which must be left-clicked on, to dismiss the notification. Green and orange notifications are self-dismissive.

## [](#accesing-features)Accessing Features

Couchbase Web Console allows users to access features by left-clicking on _tabs_. Tabs are located:

* _In the left-hand navigation bar_. Whenever a tab is left-clicked on, the appearance of the console’s _main panel_ changes, to display content for the selected feature.
* _In the upper, horizontal navigation bar_. This appears, for _some_ features, immediately above the main panel. Whenever a tab is left-clicked on, the appearance of the main panel changes, to display alternative content for the feature selected from the left-hand navigation bar.

The remaining sections on this page describe in turn the features accessed by left-clicking on the tabs provided.

## [](#console-nav-servers)Servers

Left-click on the **Servers** tab, in the left-hand navigation bar:

![serversTab](../_images/manage-ui/serversTab.png) 

The main panel changes, to display the **Servers** screen. Its initial appearance is as follows:

![serversScreenInitial](../_images/manage-ui/serversScreenInitial.png) 

The **Servers** screen provides information on every node in the cluster. In this case, the cluster consists of a single node: therefore, a single row of information is displayed, for the current node. This information includes the following:

* **name**. The name of the node, established during setup.
* **group**. The group of which the node is currently a member. For conceptual information on groups, see [Server Group Awareness](../../learn/clusters-and-availability/groups.md). For practical information on group management, see [Manage Groups](../manage-groups/manage-groups.md).
* **services**. The services installed on the node. In this case, six of the seven services have been installed and are running: **analytics**, **data**, **eventing**, **index**, **query**, and **search**. Note that five of these six services have an identically named tab corresponding to them, in the left-hand navigation bar; whereby service-specific configuration and management can be performed. The **Backup Service**, which has not been installed on this instance, also has a tab in the left-hand navigation bar. The only service not to have a tab is the **Data Service**; which is managed by means of the **Buckets**, **Documents**, and **Views** tabs. Information on all of these tabs is provided below.  
For conceptual information on services, see [Services](../../learn/services-and-indexes/services/services.md).
* **CPU**, **RAM**, **swap**, **disk used**. Information on resource-consumption, on the specified node.
* **items**. The active and replica data items currently residing on the node. For information on intra-cluster replication, see [Intra-Cluster Replication](../../learn/clusters-and-availability/intra-cluster-replication.md).
* **Statistics**Left-click on this interactive tab, to display interactive statistics-charts for the bucket, on the console’s **Dashboard**. Note that statistics are only available when at least one bucket has been installed.

Above the server-information row, two additional controls are provided:

* **filter servers…​**To filter the display of servers (when there are multiple servers listed), enter a string. Only servers whose names provide a match are then displayed.
* **Rebalance**. Left-clicking on this control causes a _rebalance_ to be performed, across the cluster. For conceptual information on rebalance, see [Rebalance](../../learn/clusters-and-availability/rebalance.md). For practical information on performing rebalance, see [Add a Node and Rebalance](../manage-nodes/add-node-and-rebalance.md).

To the right-hand side of the banner, three further controls appear:

* **Groups**. Allows management of server groups, as described in [Manage Groups](../manage-groups/manage-groups.md).
* **Failover**. Allows one or more nodes to be failed over, as described in [Fail a Node Over and Rebalance](../manage-nodes/fail-nodes-over.md).
* **Add Server**. Allows a server to be added to the current cluster, as described in [Add a Node and Rebalance](../manage-nodes/add-node-and-rebalance.md).

For an example of the **Servers** screen with a cluster of multiple nodes, see the [three node cluster](../manage-xdcr/recover-data-with-xdcr.md#three%5Fnode%5Flocal%5Fcluster) used in [Recover Data with XDCR](../manage-xdcr/recover-data-with-xdcr.md).

### [](#learning-about-and-managing-servers)Servers: Learn and Manage

To learn about servers, see [Nodes](../../learn/clusters-and-availability/nodes.md). To manage servers, see [Manage Nodes and Clusters](../manage-nodes/node-management-overview.md).

## [](#console-buckets)Buckets

To access the **Buckets** screen, left-click on the tab in the left-hand navigation bar:

![bucketsTab](../_images/manage-ui/bucketsTab.png) 

This brings up the **Buckets** screen, which initially appears as follows:

![bucketsScreenInitial](../_images/manage-ui/bucketsScreenInitial.png) 

As with the **Dashboard**, described above, before any bucket has been added to the server, the **Buckets** screen is almost blank. A notification is provided, with options to use the **Add Bucket** control at the upper right, or to [Install Sample Buckets](../manage-settings/install-sample-buckets.md), in order to add a bucket containing data that is ready to support testing and experimentation.

After the `travel-sample` bucket has been added, by means of the procedure described in [Install Sample Buckets](../manage-settings/install-sample-buckets.md), the **Buckets** screen appears as follows:

![bucketsScreenWithBucket](../_images/manage-ui/bucketsScreenWithBucket.png) 

The **Buckets** screen displays each bucket on its own row, with supporting information distributed horizontally, in columns. The column headings are:

* **name**. The name of the bucket.
* **items**. The number of data items (typically referred to as _documents_) within the bucket.
* **resident**. The percentage of the items resident on the current node.
* **ops/sec**. The number of operations per second being performed on the bucket’s data.
* **RAM used/quota**. The amount of memory currently being used by the bucket, against its total allocated quota for this node.
* **disk used**. The amount of disk used by the bucket, on this node.

To the right-hand side of the column, twoe tabs are provided, whereby additional information can be accessed. The **Documents** tab allows the documents within the bucket to be individually read and edited. This facility can also be accessed by means of the **Documents** tab, in the left-hand navigation bar; as explained in [Documents](#console-documents), below. The **Scopes & Collections** tab provides access data-containers within the bucket, whereby documents can be organized according to type: for information, see [Scopes and Collections](../../learn/data/scopes-and-collections.md).

### [](#buckets-learning-and-managing)Buckets: Learn and Manage

A conceptual account of buckets is provided in [Buckets](../../learn/buckets-memory-and-storage/buckets.md). Information on how to manage buckets is provided in [Manage Buckets](../manage-buckets/bucket-management-overview.md).

## [](#console-xdcr)XDCR

To access the **XDCR** screen, left-click on the tab in the left-hand navigation bar:

![xdcrTab](../_images/manage-ui/xdcrTab.png) 

This brings up the **XDCR** screen, which initially appears as follows:

![xdcrScreenInitial](../_images/manage-ui/xdcrScreenInitial.png) 

XDCR (_Cross Data Center Replication_) replicates data between clusters, providing protection against data center failure. Replication occurs from a specific bucket on the source cluster to a specific bucket on a target cluster.

In its initial display, the **XDCR** screen provides a panel named **Remote Clusters**. This will list the clusters that have been defined as targets for replication. It also provides a panel named **Outgoing Replications**, which will list the replications that are in process between source and target clusters.

### [](#xdcr-learning-and-managing)XDCR: Learn and Manage

An extensive conceptual overview of XDCR is provided in [Cross Data Center Replication (XDCR)](../../learn/clusters-and-availability/xdcr-overview.md). Instructions on setting up and performing XDCR are provided in [XDCR Management Overview](../manage-xdcr/xdcr-management-overview.md).

## [](#console-security)Security

To access the **Security** screen, left-click on the tab in the left-hand navigation bar:

![securityTab](../_images/manage-ui/securityTab.png) 

This brings up the **Security** screen:

![securityScreen](../_images/manage-ui/securityScreen.png) 

The **Security** screen can be displayed in four distinct views, each corresponding to a separate area of security-management. These are accessed by means of tabs, distributed across the upper horizontal navigation bar. They are **Users and Groups**, **Certificates**, **Audit**, and **Other Settings**. For information on these screens, and links to further information on the security features they support, see [Manage Security Settings](../manage-security/manage-security-settings.md).

### [](#security-learning-and-managing)Security: Learn and Manage

An extensive conceptual overview of Couchbase Server security is provided in [Security](../../learn/security/security-overview.md). For practical steps towards securing a cluster, see [Security Management Overview](../manage-security/security-management-overview.md).

## [](#console-settings)Settings

To access the **Settings** screen, left-click on the tab in the left-hand navigation bar:

![settingsTab](../_images/manage-ui/settingsTab.png) 

This brings up the **Settings** screen:

![settingsScreen](../_images/manage-ui/settingsScreen.png) 

The **Settings** screen allows configuration of a variety of important parameters within Couchbase Server. Like the **Security** screen, it provides multiple views, each corresponding to a separate feature set, and accessed by means of tabs, distributed across the upper horizontal navigation bar. The tabs are **General** (displayed by default), **Auto-Compaction**, **Alerts**, and **Sample Buckets**.

### [](#settings-learning-and-managing)Manage Settings

Further information is provided in [Manage Settings](../manage-settings/manage-settings.md).

## [](#console-logs)Logs

To access the **Logs** screen, left-click on the tab in the left-hand navigation bar:

![logsTab](../_images/manage-ui/logsTab.png) 

This brings up the **Logs** screen:

![logsScreen](../_images/manage-ui/logsScreen.png) 

The Couchbase Logging facility records important events, and saves the details to log files, on disk. Additionally, subsets of information are provided on the **Logs** screen.

The **Logs** screen offers two views, one of which is the default representation of logged information. The other is a facility for configuring _explicit logging_, which allows comprehensive and fully updated information to be generated as required.

### [](#logs-learning-and-managing)Manage Logs

Full details are provided in [Manage Logging](../manage-logging/manage-logging.md).

## [](#console-documents)Documents

To access the **Documents** screen, left-click on the tab in the left-hand navigation bar:

![documentsTab](../_images/manage-ui/documentsTab.png) 

This brings up the **Documents** screen:

![documentsScreen](../_images/manage-ui/documentsScreen.png) 

This screen displays the documents contained within installed buckets. The screen is currently blank, since no buckets have yet been installed. The **Location** control permits a bucket to be selected from those installed, and for a scope and a collection within the bucket to be selected. Other controls allow specific documents to be displayed, according to configured parameters. (For information on scopes and collections, see [Scopes and Collections](../../learn/data/scopes-and-collections.md)).

The easiest way to install a bucket containing data is described in [Install Sample Buckets](../manage-settings/install-sample-buckets.md). If the `travel-sample` is installed, the screen appears as follows:

![documentsScreenWithDocuments](../_images/manage-ui/documentsScreenWithDocuments.png) 

The internal content of documents can now be displayed and edited.

The **Documents** screen presents two separate panels, which are accessible from the horizontal navigation bar along the top. The **Workbench** panel is the default, currently displayed. A full description of this panel and its contents is provided in [Explore the Server Configuration](../../getting-started/look-at-the-results.md), which is part of the the _Getting Started_ sequence. For an explanation of the **Import** panel, see [Import Documents](../import-documents/import-documents.md).

To edit a document, left-click on a document-id that appears in the **id** column of the **Workbench** panel. This brings up the **Edit Document** dialog, which features an interactive **Data** panel, whereby the document’s contents can be edited:

![editDocumentData](../_images/manage-ui/editDocumentData.png) 

To examine the document’s _metadata_, left-click on the **Metadata** button, at the upper right of the **Edit Document** dialog. This duly brings up the **Metadata** panel (which is _read only_).

![editDocumentMetaData](../_images/manage-ui/editDocumentMetaData.png) 

For instructions on installing a _sample bucket_, which contains documents that are ready to be inspected and experimented with, see [Install Sample Buckets](../manage-settings/install-sample-buckets.md).

### [](#learning-about-documents)Learn about Documents

For a full explanation of _documents_, and an overview of the Couchbase _data model_, see [Data](../../learn/data/data.md).

## [](#console-query)Query

To access the **Query** screen, left-click on the tab in the left-hand navigation bar:

![queryTab](../_images/manage-ui/queryTab.png) 

This brings up the **Query** screen:

![queryScreenInitial](../_images/manage-ui/queryScreenInitial.png) 

Initially, even though the cluster is running the Query Service, no content may be displayed. Content is presently displayed, provided that the cluster is running the Index Service:

![queryScreenAfterInterval](../_images/manage-ui/queryScreenAfterInterval.png) 

This screen now features the Query Workbench: an interactive tool that lets you compose and execute SQL++ queries on the data contained by the bucket. In its initial display, the tool shows the sequence of SQL++ commands that have been executed to create the scopes and collections within `travel-sample`: for information, see [Scopes and Collections](../../learn/data/scopes-and-collections.md).

### [](#query-learn-manage-and-use)Query: Learn, Manage, and Use

For information on the Query Service, see [Query Service](../../learn/services-and-indexes/services/query-service.md). For information on using the Query Workbench to make SQL++ queries, see [Run Your First SQL++ Query](../../getting-started/try-a-query.md), which is part of the _Getting Started_ sequence. For information on SQL++, see the [SQL++ Language Reference](../../n1ql/n1ql-language-reference/index.md).

## [](#console-indexes)Indexes

To access the **Indexes** screen, left-click on the tab in the left-hand navigation bar:

![indexesTab](../_images/manage-ui/indexesTab.png) 

This brings up the **Indexes** screen:

![indexesScreen](../_images/manage-ui/indexesScreen.png) 

The screen is initially blank, since no buckets have yet been added. If a bucket is defined, and data loaded into it, indexes must then be defined on the data, before they are registered on the **Indexes** screen. However, _sample buckets_ have data and indexes predefined. The procedure for adding a _sample bucket_ is provided in [Install Sample Buckets](../manage-settings/install-sample-buckets.md). After this procedure is followed for the `travel-sample` bucket, the **Indexes** screen appears as follows:

![indexScreenWithIndexes](../_images/manage-ui/indexScreenWithIndexes.png) 

Note that initially, the **status** column provides ongoing figures for **mutations remaining**: this indicates that the indexes for the bucket are still being prepared. When the indexes have been fully prepared, the **mutations remaining** notifications are no longer displayed:

![indexesScreenFullyPrepared](../_images/manage-ui/indexesScreenFullyPrepared.png)

### [](#indexes-define-and-manage)Indexes: Define and Manage

For a detailed explanation of indexes, see [Global Secondary Indexes](../../learn/services-and-indexes/indexes/global-secondary-indexes.md). Information on how to manage indexes is given in [Manage Indexes](../manage-indexes/manage-indexes.md).

## [](#console-search)Search

To access the **Search** screen, left-click on the tab in the left-hand navigation bar:

![searchTab](../_images/manage-ui/searchTab.png) 

This brings up the **Full Text Search** screen:

![searchScreen](../_images/manage-ui/searchScreen.png) 

The screen contains panels for Search _Indexes_ and _Aliases_. Both panels are currently blank, since nothing has yet been created.

Creation of both is explained in [Searching from the UI](../../fts/fts-searching-from-the-UI.md).

### [](#search-learn-and-manage)Search: Learn and Manage

For an explanation of the Search Service, and detailed examples of search-index creation, see [Full Text Search: Fundamentals](../../fts/fts-introduction.md).

## [](#console-analytics)Analytics

To access the **Analytics** screen, left-click on the tab in the left-hand navigation bar:

![analyticsTab](../_images/manage-ui/analyticsTab.png) 

This brings up the **Analytics** screen:

![analyticsScreen](../_images/manage-ui/analyticsScreen.png) 

The screen contains an **Analytics Query Editor**, and a panel for **Analytics Query Results**. Both panels are currently blank.

### [](#analytics-learn-and-manage)Analytics: Learn and Manage

For an explanation of the Analytics Service, see the [Introduction](../../analytics/introduction.md) to Analytics.

## [](#console-eventing)Eventing

To access the **Eventing** screen, left-click on the tab in the left-hand navigation bar:

![eventingTab](../_images/manage-ui/eventingTab.png) 

This brings up the **Eventing** screen:

![eventingScreen](../_images/manage-ui/eventingScreen.png) 

The screen is currently blank, since no Eventing functions have yet been defined.

### [](#eventing-learn-and-manage)Eventing: Learn and Manage

For an explanation of the Eventing Service, see [Eventing Service: Fundamentals](../../eventing/eventing-overview.md).

## [](#console-backup)Backup

To access the **Backup** screen, left-click on the tab, in the left-hand navigation bar:

![backupTab](../_images/manage-ui/backupTab.png) 

This brings up the **Repositories** screen, of the Backup Service:

![backupScreen](../_images/manage-ui/backupScreen.png) 

The screen is currently blank, since no Backup-Service repositories have yet been defined.

### [](#backup-learn-and-manage)Backup: Learn and Manage

For an overview of the Backup Service, see [Backup Service](../../learn/services-and-indexes/services/backup-service.md). For step-by-step instructions on how to configure the scheduled backup of cluster-data, see [Manage Backup and Restore](../manage-backup-and-restore/manage-backup-and-restore.md).

## [](#console-views)Views

To access the **Views** screen, left-click on the tab in the left-hand navigation bar:

![viewsTab](../_images/manage-ui/viewsTab.png) 

This brings up the **Views** screen:

![viewsScreen](../_images/manage-ui/viewsScreen.png) 

The screen is currently blank, since no Views have yet been defined.

### [](#views-define-and-manage)Views: Define and Manage

For a detailed explanation of Views, see [Views](../../learn/views/views-intro.md).