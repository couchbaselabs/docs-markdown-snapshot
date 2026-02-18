---
title: Install
description: Follow this process to install Couchbase Server.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/install/pages/install-intro.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/install/install-intro.html)

# Install

> Follow this process to install Couchbase Server. 

__Table 1\. Installing Couchbase Server__
| Step       | Action                                                   | Description                                                                                                                                                                                                                                                                                           |
| ---------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Step 1** | Review the system requirements and deployment guidelines | Couchbase Server has a set of system requirements and deployment guidelines that vary depending on your deployment. Make sure that you plan your environment accordingly before installation. [System Requirements](plan-for-production.md) [Deployment Guidelines](install-production-deployment.md) |
| **Step 2** | Install Couchbase Server on each node in the cluster     | Couchbase is a clustered database and requires that Couchbase Server is installed and running on each node before joining them together into a cluster. [Installing on Linux](install-linux.md) [Installing on Mac OS X](macos-install.md) [Installing on Windows](install-package-windows.md)        |
| **Step 3** | Verify the installation and node availability            | After installing Couchbase Server on a node, you can do a basic verification of the installation by confirming access to the Couchbase Server Web Console. You can also do other advanced verifications, depending on your needs. [Verifying the Couchbase Server Installation](testing.md)           |
| **Step 4** | Initialize the Couchbase Server cluster                  | After you install Couchbase Server on all of the nodes, you need to join them together into a cluster. [Create a Cluster](../manage/manage-nodes/create-cluster.md)                                                                                                                                   |