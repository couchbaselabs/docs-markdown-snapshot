---
title: Enterprise Analytics Web Console
description: The features of Enterprise Analytics can be managed by means of
  Enterprise Analytics Web Console.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/manage-ui/manage-ui.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.0@enterprise-analytics:manage:manage-ui/manage-ui.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/manage/manage-ui/manage-ui.html)

# Enterprise Analytics Web Console

> The features of Enterprise Analytics can be managed by means of Enterprise Analytics Web Console. 

## [](#understanding-enterprise-analytics-web-console)Understanding Enterprise Analytics Web Console

_Enterprise Analytics Web Console_ is a browser-based, interactive graphical facility that supports the management of Enterprise Analytics. This includes:

* Monitoring performance and server-state, by means of constantly updated statistics, displayed in customizable, interactive charts.
* Adding and removing cluster-nodes.
* Interactively executing queries.
* Managing security including the addition of users, the assignment of roles, and the configuration of external authentication mechanisms.

The range of features made available depends on the _roles_ that have been assigned to the user who logs into the console. If the user has been assigned the _Full Administrator_ role, they have complete access to all features; and can therefore read, write, execute, and manage without constraint. Other roles limit the feature-range. For detailed information, see [Roles](../../../../server/current/learn/security/roles.md).

This page provides an overview of the complete feature-set made available by Enterprise Analytics Web Console. In many cases, detailed explanations of the user interface is provided elsewhere in the documentation-set, in correspondence with the supported feature. Links are provided in each case.

## [](#accessing-the-console)Accessing the Console

Enterprise Analytics Web Console is typically accessible at port _8091_, of the host system, although the port number may be different if _secure_ console-access has been established: see [Manage Console Access](../manage-security/manage-console-access.md), for information.

When the appropriate port is accessed, an initial setup interface is displayed with two options:

* **Setup New Cluster** \- Establishes the current server as an independent cluster of one node, to which other nodes can subsequently be added.
* **Join Existing Cluster** \- Establishes the current server as a node that is part of a pre-existing cluster.

These procedures, which include establishing credentials for administrator-authentication, are described in detail in [Create a Cluster](../manage-nodes/create-cluster.md). The remaining information about this page assumes that a cluster of one node has been established. The features of the console will be portrayed in their entirety, as visible to the _Full Administrator_.

## [](#authenticating-with-the-console)Authenticating with the Console

Once the cluster is running, all its administrators must _authenticate_, in order to access its features. Therefore, when port _8091_ is accessed by means of the browser, a login interface is displayed.

Enter username and password, and click on the **Sign In** button to access the console.

Detailed information about authenticating with Enterprise Analytics is provided in [Authentication](../../../../server/current/learn/security/authentication.md).

## [](#understanding-the-dashboard)Understanding the Dashboard

On the user's successful login, the console displays the **Dashboard**. If this is the user's first-time access, the interface displays a clean dashboard layout.

The display consists of several key areas:

* A **banner** with interactive controls.
* A **main panel**, which allows display of data and configuration fields.
* A **left-hand navigation bar**, which allows the main panel's content to be determined.
* A **lower panel**, which displays current status on the cluster.

These are described in detail below.

### [](#console-banner)Banner

The banner contains several important elements:

* At the left, the banner features the name of the console, as determined during server-setup
* It displays the name of the currently displayed screen (for example, **Dashboard**)
* At the right, it provides information identifying the version of the server that is being run, and the build number

In the horizontal band immediately above the banner, at the right-hand side, three interactive options appear:

* **activity** \- Shows notifications for ongoing operations in Enterprise Analytics. Click on this to view details about current activities and their progress.
* **help** \- Provides tabs that respectively allow all customers to access documentation for the server-release; and allow certain customers to contact Couchbase Customer Support.
* **admin** \- Provides tabs that respectively allow administrators to redefine their password; and to sign out of the console.

### [](#console-main-panel)Main Panel

The content of the main panel changes, based on selections made by the user in the left-hand navigation bar. The default display is that of the **Dashboard**.

All statistics presented here are in relation to existing nodes, databases, and collections.

The user is also able to add charts incrementally, in order to display continuously updated sets of statistics. In consequence, the **Dashboard** is assembled differently by each user. Detailed information about incrementally adding charts and on how to read them is provided in [Manage Statistics](../manage-statistics/manage-statistics.md).

### [](#console-left-hand-nav)Navigation Bar

The vertical _navigation bar_, which appears at the left-hand side, provides a tab for each of the major features that can be accessed and managed. On initial console-access, the **Dashboard** tab, at the top, is selected by default. Information is provided below on each of the possible selections.

When the mouse cursor is hovered over elements in the navigation bar, a toggle appears at the lower left. Clicking on this causes the navigation bar to be collapsed, thereby freeing up more horizontal space for the main panel.

The toggle remains accessible, and can be used to restore the navigation bar at any time.

### [](#console-lower-panel)Lower Panel

The _lower panel_ provides information about cluster status:

* _Nodes_ are represented by icons in green, orange, or red; according to whether they are _active_, _failed-over_, _pending-rebalance_, or _inactive_. Detailed information about nodes, their status, and how they can be managed is provided in [Manage Nodes and Clusters](../manage-nodes/node-management-overview.md).
* Installed _Services_ and _Cross Data Center Replication_ are represented by icons in green or grey. If a service-icon is green, this indicates that it is installed and running. If it is grey, it is not installed.

System notifications are shown, as required, in the lower left-hand corner of the main panel. These are color-coded to indicate their status:

* Green notifications indicate success
* Orange notifications indicate warnings of actual or potential problems
* Red notifications indicate failure

> [!NOTE]
> Red notifications provide a red, interactive `X`, which must be clicked on to dismiss the notification. Green and orange notifications are self-dismissive.

## [](#accesing-features)Accessing Features

Enterprise Analytics Web Console allows users to access features by clicking on _tabs_. Tabs are located:

* _In the left-hand navigation bar_ \- Whenever a tab is clicked on, the appearance of the console's _main panel_ changes, to display content for the selected feature.
* _In the upper, horizontal navigation bar_ \- This appears, for _some_ features, immediately above the main panel. Whenever a tab is clicked on, the appearance of the main panel changes, to display alternative content for the feature selected from the left-hand navigation bar.

The remaining sections on this page describe in turn the features accessed by clicking on the tabs provided.

## [](#console-nav-servers)Servers

To access the **Servers** screen, navigate to the **Servers** tab in the left-hand navigation bar.

The main panel changes to display the **Servers** screen, which provides information about every node in the cluster.

For a single-node cluster, a single row of information is displayed for the current node. This information includes the following:

* **name** \- The name of the node, established during setup.
* **group** \- The group of which the node is currently a member. For conceptual information about groups, see [Server Group Awareness](../../../../server/current/learn/clusters-and-availability/groups.md). For practical information about group management, see [Manage Groups](../manage-groups/manage-groups.md).
* **CPU**, **RAM**, **swap**, **disk used** \- information about resource-consumption, on the specified node.
* **Statistics** \- Click on this interactive option to display interactive statistics-charts for the database, on the console's **Dashboard**.

> [!NOTE]
> Statistics are only available when at least one database has been installed.

Above the server-information display, two additional controls are provided:

* **filter servers…​** \- To filter the display of servers (when there are multiple servers listed), enter a search string. Only servers whose names provide a match are then displayed.
* **Rebalance** \- Clicking on this control causes a _rebalance_ to be performed across the cluster. For conceptual information about rebalance, see [Rebalance](../../../../server/current/learn/clusters-and-availability/rebalance.md). For practical information about performing rebalance, see [Add a Node and Rebalance](../manage-nodes/add-node-and-rebalance.md).

To the right-hand side of the banner, three further controls appear:

* **Groups** \- Allows management of server groups, as described in [Manage Groups](../manage-groups/manage-groups.md).
* **Failover** \- Allows one or more nodes to be failed over, as described in [Fail a Node Over and Rebalance](../manage-nodes/fail-nodes-over.md).
* **Add Server** \- Allows a server to be added to the current cluster, as described in [Add a Node and Rebalance](../manage-nodes/add-node-and-rebalance.md).

To learn about servers, see [Nodes](../../../../server/current/learn/clusters-and-availability/nodes.md). To manage servers, see [Manage Nodes and Clusters](../manage-nodes/node-management-overview.md).

## [](#console-security)Security

To access the **Security** screen, navigate to the **Security** tab in the left-hand navigation bar.

This displays the **Security** screen, which provides comprehensive security management capabilities.

The **Security** screen can be displayed in six distinct views, each corresponding to a separate area of security-management. These are accessed by means of tabs, distributed across the upper horizontal navigation bar:

* **Users and Groups** \- Manage user accounts and group assignments
* **LDAP** \- Configure LDAP authentication integration
* **SAML** \- Configure SAML authentication integration
* **Certificates** \- Manage SSL/TLS certificates
* **Audit** \- Configure security auditing settings
* **Other Settings** \- Additional security configuration options

For information about these screens, and links to further information about the security features they support, see [Manage Security Settings](../manage-security/manage-security-settings.md). An extensive conceptual overview of Enterprise Analytics security is provided in [Security](#learn:security/security-overview.adoc). For practical steps towards securing a cluster, see [Security Management Overview](../manage-security/security-management-overview.md).

## [](#console-settings)Settings

To access the **Settings** screen, navigate to the **Settings** tab in the left-hand navigation bar.

This displays the **Settings** screen, which allows configuration of a variety of important parameters within Enterprise Analytics.

Like the **Security** screen, it provides multiple views, each corresponding to a separate feature set, and accessed by means of tabs, distributed across the upper horizontal navigation bar:

* **General** (displayed by default) - Configure cluster name, memory quotas, storage modes, and node availability settings.
* **Alerts** \- Configure email alert settings and notification preferences.

Further information is provided in [Manage Settings](../manage-settings/manage-settings.md).

## [](#console-logs)Logs

To access the **Logs** screen, navigate to the **Logs** tab in the left-hand navigation bar.

This displays the **Logs** screen, which provides access to system logging information and configuration.

The Couchbase Logging facility records important events, and saves the details to log files on disk. Additionally, subsets of information are provided on the **Logs** screen.

The **Logs** screen offers two main views:

1. The default representation of logged information - displays recent log entries and system events.
2. A facility for configuring _explicit logging_ \- allows comprehensive and fully updated information to be generated as required.

Full details are provided in [Manage Logging](../manage-logging/manage-logging.md).