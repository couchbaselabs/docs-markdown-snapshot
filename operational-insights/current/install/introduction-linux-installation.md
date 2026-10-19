---
title: Install Operational Insights
description: Follow this process to install Operational Insights.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/introduction-linux-installation.adoc
  xref: xref:enterprise-analytics:install:introduction-linux-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/introduction-linux-installation.html)

# Install Operational Insights

> Follow this process to install Operational Insights. 

__Table 1\. Installing Operational Insights__
| Step       | Action                                                   | Description                                                                                                                                                                                                                                                                                |
| ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Step 1** | Review the system requirements and deployment guidelines | Operational Insights has a set of system requirements and deployment guidelines that vary depending on your deployment. Make sure that you plan your environment accordingly before installation. [System Requirements](sys-resource-req.md) [Deployment Guidelines](deploy-guidelines.md) |
| **Step 2** | Install Operational Insights on each node in the cluster | Couchbase is a clustered database and requires that you install Operational Insights and run it on each node before joining them together into a cluster. [Installing on Linux](linux-installation.md)                                                                                     |
| **Step 3** | Verify the installation and node availability            | After you install Operational Insights on a node, you can verify the installation by opening the Operational Insights Web Console. You can also do other advanced verifications, depending on your needs. [Verify the Installation](verify-installation.md)                                |
| **Step 4** | Initialize the Operational Insights cluster              | After you install Operational Insights on all of the nodes, you need to join them together into a cluster. [Create a Cluster](../manage/manage-nodes/create-cluster.md)                                                                                                                    |