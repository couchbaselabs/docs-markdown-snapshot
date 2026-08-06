---
title: Uninstall Enterprise Analytics
description: The Enterprise Analytics application and its associated data can be
  removed from supported systems.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/install/pages/uninstall.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:install:uninstall.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/install/uninstall.html)

# Uninstall Enterprise Analytics

> The Enterprise Analytics application and its associated data can be removed from supported systems. 

Uninstalling Enterprise Analytics from a system involves removing the Enterprise Analytics application along with any directories containing Couchbase configuration files, data, and logs.

This page describes how to uninstall Enterprise Analytics from Linux systems; and assumes that you have already performed a standard package-based install.

## [](#before-you-uninstall)Before You Uninstall

If the system is a part of an active Enterprise Analytics cluster, you must [remove it and rebalance the cluster](../manage/manage-nodes/remove-node-and-rebalance.md) to take the node out of the configuration. You'll also need to update Enterprise Analytics clients to point to an available node within the active cluster.

> [!WARNING]
> The instructions on this page removes Enterprise Analytics, and all configuration and database files. Make sure that you backup your configuration and data before proceeding, as this process cannot be undone.

## [](#linux)Linux

1. Stop the Enterprise Analytics process if it's running.  
```console  
sudo systemctl stop enterprise-analytics  
```  
For more information, see [Start and Stop Enterprise Analytics](start-stop-cb-enterprise-analytics.md).
2. Remove the application and packages.

  * RHEL
  * Ubuntu and Debian  
```console  
sudo rpm -e enterprise-analytics  
```  
```console  
sudo dpkg -r enterprise-analytics  
```
3. Remove the data and log directories.  
```console  
sudo rm -rf /opt/enterprise-analytics  
```  
If you specified non-default locations for Couchbase data, indexes and so on during initial setup of the node, you must delete them to complete the uninstall process.