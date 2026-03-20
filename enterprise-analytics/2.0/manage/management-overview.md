---
title: Overview
description: A Enterprise Analytics Cluster can be created and managed by means
  of the Enterprise Analytics Web Console, the CLI, and the REST API.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/management-overview.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:manage:management-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/manage/management-overview.html)

# Overview

> A Enterprise Analytics Cluster can be created and managed by means of the Enterprise Analytics Web Console, the CLI, and the REST API. 

## [](#cluster-management)Cluster Management

An Enterprise Analytics cluster consists of one or more _nodes_, which are network-accessible systems, each running an instance of Enterprise Analytics. Nodes are added to the cluster incrementally, one by one.

Once the cluster is set up, _databases_ can be defined to store data items. Administrators can also maintain logs, adjust settings, and apply security measures to make sure data availability and reliability.

The pages in this section provide detailed examples of how to perform all key Enterprise Analytics management tasks using the available tools.

## [](#enterprise-analytics-tools)Enterprise Analytics Tools

Enterprise Analytics can be managed using the Enterprise Analytics Web Console, the Command-Line Interface (CLI), and the REST API.

The CLI and REST API allow administrators to specify the IP address or domain name of an Enterprise Analytics node to identify the target server on the network. Both tools can be used in administrator-created scripts and programs, as well as directly on the command line.

The Enterprise Analytics Web Console is browser-based and requires administrator authentication at a login screen. Once logged in, the Full Administrator can view all nodes in the cluster, including details of assigned services, memory quotas, statistics, and more. (This information can also be retrieved using specific CLI and REST API calls.)

Enterprise Analytics enforces _Role-Based Access Control_ (RBAC), where all users are assigned _roles_ that correspond to specific _privileges_ on system resources. Credentials must be provided with each CLI or REST API call. Within the Enterprise Analytics Web Console, features such as node management and cluster monitoring are made available based on the authenticated user’s assigned roles. For more details, see [RBAC](manage-security/rbac-overview.md).

> [!NOTE]
> Both the Enterprise Analytics Web Console and CLI rely on the REST API for their operations, providing consistency across tools. Using the CLI with the `-d` (debug) option reveals the underlying REST methods in the standard output, which can be useful for troubleshooting or scripting.

Similarly, browser _Developer Tools_ (such as those in _Chrome_) allow you to observe ongoing REST API calls while using the Enterprise Analytics Web Console, providing insights into cluster management and monitoring operations.

* For a complete list of CLI commands, see the [CLI Reference](../../../server/current/cli/cli-intro.md).
* For a complete list of REST API methods, see the [REST API Reference](../reference/rest-intro.md).
* For an introduction to Enterprise Analytics Web Console, see [Enterprise Analytics Web Console](manage-ui/manage-ui.md).