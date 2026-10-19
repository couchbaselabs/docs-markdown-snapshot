---
title: Uninstall
description: The Operational Insights application and its associated data can be
  removed from supported systems.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/uninstall.adoc
  xref: xref:enterprise-analytics:install:uninstall.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/uninstall.html)

# Uninstall

> The Operational Insights application and its associated data can be removed from supported systems. 

Uninstalling Operational Insights from a system involves removing the Operational Insights application along with any directories containing Couchbase configuration files, data, and logs.

This page describes how to uninstall Operational Insights from Linux systems; and assumes that you have already performed a standard package-based install.

## [](#before-you-uninstall)Before You Uninstall

If the system is a part of an active Operational Insights cluster, you must [remove it and rebalance the cluster](../manage/manage-nodes/remove-node-and-rebalance.md) to take the node out of the configuration. You'll also need to update Operational Insights clients to point to an available node within the active cluster.

> [!WARNING]
> The instructions on this page removes Operational Insights, and all configuration and database files. Make sure that you backup your configuration and data before proceeding, as this process cannot be undone.

## [](#linux)Linux

1. Stop the Operational Insights process if it's running.  
```console  
sudo systemctl stop operational-insights  
```  
For more information, see [Start and Stop Operational Insights](start-stop-cb-operational-insights.md).
2. Remove the application and packages.

  * RHEL
  * Ubuntu and Debian  
```console  
sudo rpm -e operational-insights  
```  
```console  
sudo dpkg -r operational-insights  
```
3. Remove the data and log directories.  
```console  
sudo rm -rf /opt/couchbase  
```  
If you specified non-default locations for Couchbase data, indexes and so on during initial setup of the node, you must delete them to complete the uninstall process.