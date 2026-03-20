---
title: Use the Agent Catalog Tools and Prompts Hub
description: Use the Tools Hub or the Prompts Hub to view all the tools and
  prompts published to Agent Catalog from your agent projects.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/tools-prompts-hub.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:ai:build:tools-prompts-hub.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/tools-prompts-hub.html)

# Use the Agent Catalog Tools and Prompts Hub

> Use the Tools Hub or the Prompts Hub to view all the tools and prompts published to Agent Catalog from your agent projects. 

View the source code directly from the Git commits in your project to aid in troubleshooting.

## [](#prerequisites)Prerequisites

* You have completed the [Prerequisites](integrate-agent-with-catalog.md#prerequisites) and [Installed and Set Up Environment Variables](integrate-agent-with-catalog.md#install) for the Agent Catalog.
* You have deployed a single node or multi-node Capella operational cluster that has the Search Service enabled.  
This should be the same cluster you add to your environment variables for the Agent Catalog.  
For more information about how to add Services to a cluster, see [Modify the Cluster Configuration](../../cloud/clusters/modify-database.md#modify-existing-service).
* You have [indexed and published tools and prompts to the Agent Catalog](integrate-agent-with-catalog.md#index-publish).
* Your user account has the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Creator](../../cloud/organizations/organization-user-roles.md#organization-role-project-creator) organization role, or 1 of the following project roles:

  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Cluster Viewer](../../cloud/projects/project-roles.md#project-cluster-viewer-role)
  * [Data Reader](../../cloud/projects/project-roles.md#project-cluster-data-reader)
  * [Data Writer](../../cloud/projects/project-roles.md#project-cluster-data-reader-writer)
* You have logged into the Capella UI.

## [](#tools-hub)View Tools in the Tools Hub

To view published tools in your Agent Catalog project in the Capella UI:

1. In the Capella UI, go to **AI Services** **Tools Hub**.
2. In the **Operational Cluster** list, select the cluster you added to your environment variables and configured as the publish destination for your tools.
3. To filter the displayed tools, do any of the following:

  1. In the search bar, choose to search for a **Name**, **Description**, or **Tags** from the specific tool you want to view.
  2. Click the **Bucket**, **Date Range**, or **Type** filters to filter the displayed tools.
4. Click the name of the tool you want to view.  
> [!TIP]  
> You can also click to copy the **Catalog ID** or **Source** for a listed tool.
5. Do any of the following:

  1. To view a specific version of your tool, click its Git commit hash.
  2. To filter the displayed Git commit hashes by date, click the **Date Range** filter.
  3. To copy the path for the tool file, click **Copy**.
  4. To copy the full file contents of the tool for the selected version, click **Copy** or click the source code for the tool.

## [](#prompts-hub)View Prompts in the Prompts Hub

To view published prompts in your Agent Catalog project in the Capella UI:

1. In the Capella UI, go to **AI Services** **Prompts Hub**.
2. In the **Operational Cluster** list, select the cluster you added to your environment variables and configured as the publish destination for your prompts.
3. To filter the displayed prompts, do any of the following:

  1. In the search bar, choose to search for a **Name**, **Description**, or **Tags** from the specific prompt you want to view.
  2. Click the **Bucket** or **Date Range** filters to filter the displayed prompts.
4. Click the name of the prompt you want to view.  
> [!TIP]  
> You can also click to copy the **Catalog ID** or **Source** for a listed prompt.
5. Do any of the following:

  1. To view a specific version of your prompt, click its Git commit hash.
  2. To filter the displayed Git commit hashes by date, click the **Date Range** filter.
  3. To copy the path for the prompt file, click **Copy**.
  4. To copy the full file contents of the prompt for the selected version, click **Copy** or click the text of the prompt.

## [](#next-steps)Next Steps

To view logs from your agent’s activity, see [Monitor and Observe with Agent Tracer](agent-tracer/agent-tracer.md).

For more information about how to use the Agent Catalog, see [Integrate an Agent with the Agent Catalog](integrate-agent-with-catalog.md).