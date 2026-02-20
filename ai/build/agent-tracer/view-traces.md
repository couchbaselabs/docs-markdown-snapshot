---
title: View Traces in Agent Tracer
description: Use the Agent Tracer inside Capella AI Services to view logs from
  an agent app integrated with Agent Catalog.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/agent-tracer/view-traces.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ai:build:agent-tracer/view-traces.adoc[]
---

[View original HTML](/ai/build/agent-tracer/view-traces.html)

# View Traces in Agent Tracer

> Use the Agent Tracer inside Capella AI Services to view logs from an agent app integrated with Agent Catalog. 

Use these logs to debug problematic user-agent sessions.

For more information about the traces that you can view in Agent Tracer, see [Agent Tracer Trace Types](agent-tracer.md#trace-types).

## [](#prerequisites)Prerequisites

* You have completed the [Prerequisites](../integrate-agent-with-catalog.md#prerequisites) and [Installed and Set Up Environment Variables](../integrate-agent-with-catalog.md#install) for the Agent Catalog.
* You have deployed a single node or multi-node Capella operational cluster running Couchbase Server version 8.0 or later with the Search Service enabled.  
This should be the same cluster you add to your environment variables for the Agent Catalog.  
For more information about how to add Services to a cluster, see [Modify the Cluster Configuration](../../../cloud/clusters/modify-database.md#modify-existing-service).
* You have [indexed and published tools and prompts to the Agent Catalog](../integrate-agent-with-catalog.md#index-publish).
* You have [Add Spans and Callbacks to Your Agent](add-spans-callbacks.md).
* Your user account has the [Organization Owner](../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Creator](../../../cloud/organizations/organization-user-roles.md#organization-role-project-creator) organization role, or 1 of the following project roles:

  * [Project Owner](../../../cloud/projects/project-roles.md#project-owner-role)
  * [Cluster Viewer](../../../cloud/projects/project-roles.md#project-cluster-viewer-role)
  * [Data Reader](../../../cloud/projects/project-roles.md#project-cluster-data-reader)
  * [Data Writer](../../../cloud/projects/project-roles.md#project-cluster-data-reader-writer)
* You have logged into the Capella UI.

## [](#procedure)Procedure

To view agent traces in the Agent Tracer UI:

1. In the Capella UI, go to **AI Services** **Agent Tracer**.
2. In the **Operational Cluster** list, select the cluster you added to your environment variables and configured to collect logs from the Agent Catalog.
3. To filter the displayed logs, do any of the following:

  1. In the search bar, choose to search for a **Session ID** or **Tags** from the specific trace you want to examine.  
  For more information about configuring tags, see [Add Tags to Spans or Logs](add-spans-callbacks.md#add-tags).
  2. Click the **Bucket**, **Date Range**, or **App** filters to change the displayed sessions.  
  > [!TIP]  
  > The app name matches the name of your [root span](add-spans-callbacks.md#root-span) from your logging configuration.
4. Click the name of the session that you want to debug to open its logs.
5. In the **Session Trace Logs**, use the filters to change what messages are displayed from your logs.  
For more information about the available trace types, see [Agent Tracer Trace Types](agent-tracer.md#trace-types).

## [](#next-steps)Next Steps

Make sure to monitor your cluster as Agent Catalog publishes logs from your agent. As your logged traces grow, you might need to scale your cluster to avoid performance issues. For more information about scaling your cluster, see [Sizing a Cluster](../../../cloud/clusters/sizing.md) and [Cluster Scaling](../../../cloud/clusters/scale-database.md).

To view details about specific tools and prompts published to Agent Catalog from your project, see [Use the Agent Catalog Tools and Prompts Hub](../tools-prompts-hub.md).

To query traces and get more details on your agent activity, see [Query Agent Catalog Traces with SQL++](query-traces.md).