---
title: Install Enterprise Analytics
description: Follow this process to install Enterprise Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/install/pages/introduction-linux-installation.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:install:introduction-linux-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/install/introduction-linux-installation.html)

# Install Enterprise Analytics

> Follow this process to install Enterprise Analytics. 

__Table 1\. Installing Enterprise Analytics__
| Step       | Action                                                   | Description                                                                                                                                                                                                                                                                                |
| ---------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Step 1** | Review the system requirements and deployment guidelines | Enterprise Analytics has a set of system requirements and deployment guidelines that vary depending on your deployment. Make sure that you plan your environment accordingly before installation. [System Requirements](sys-resource-req.md) [Deployment Guidelines](deploy-guidelines.md) |
| **Step 2** | Install Enterprise Analytics on each node in the cluster | Couchbase is a clustered database and requires that you install Enterprise Analytics and run it on each node before joining them together into a cluster. [Installing on Linux](linux-installation.md)                                                                                     |
| **Step 3** | Verify the installation and node availability            | After you install Enterprise Analytics on a node, you can verify the installation by opening the Enterprise Analytics Web Console. You can also do other advanced verifications, depending on your needs. [Verifying the Enterprise Analytics Installation](verify-installation.md)        |
| **Step 4** | Initialize the Enterprise Analytics cluster              | After you install Enterprise Analytics on all of the nodes, you need to join them together into a cluster. [Create a Cluster](../manage/manage-nodes/create-cluster.md)                                                                                                                    |