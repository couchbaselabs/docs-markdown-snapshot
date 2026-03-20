---
title: Deployment Guidelines
description: Before you install Enterprise Analytics, follow the recommended
  deployment guidelines for setting up your production environment.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/install/pages/deploy-guidelines.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:install:deploy-guidelines.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/install/deploy-guidelines.html)

# Deployment Guidelines

> Before you install Enterprise Analytics, follow the recommended deployment guidelines for setting up your production environment. 

__Table 1\. Enterprise Analytics Deployment Guidelines__
| Guideline                                     | Description                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Time keeping**                              | Keeping accurate time is essential to a properly functioning database. Make sure that you follow the guidelines for synchronizing each Couchbase node using Network Time Protocol (NTP). [Clock Sync with NTP](synchronize-clocks-using-ntp.md)                                                                          |
| **Disable Transparent Huge Pages (THP)**      | You must disable the THP memory management system on each node that runs Enterprise Analytics. [Disabling Transparent Huge Pages (THP)](thp-disable.md)                                                                                                                                                                  |
| **Set kernel swappiness**                     | The kernel swappiness setting defines how aggressively the kernel swaps memory pages versus dropping pages from the page cache. You need to set the swappiness setting to 0, or at most 1, for optimal Enterprise Analytics operation. [Swap Space and Kernel Swappiness](swap-space-kernel-swappiness.md)               |
| **Couchbase client deployment**               | Deploy client applications that incorporate SDKs to enable interaction with Enterprise Analytics clusters. [home:ROOT:sdk.adoc](#home:ROOT:sdk.adoc)                                                                                                                                                                     |
| **Security**                                  | Enterprise Analytics provides security features that allow administrators to implement various security controls for a secure deployment. You should take Couchbase security best practices into consideration before, during, and after deployment. [Enterprise Analytics Processes](enterprise-analytics-processes.md) |
| **Virtualized and containerized deployments** | Couchbase recommends following specific guidelines and considerations for deploying Enterprise Analytics on a virtual machine or container. [Deployment Considerations for Virtual Machines and Containers](vm-container-guidelines.md)                                                                                  |
| **Clusters with less than 3 nodes**           | Enterprise Analytics clusters with less than 3 nodes are not recommended in production. You can use a smaller deployment for test and development purposes. [Two-Node and Single-Node Clusters](single-two-node-clusters.md)                                                                                             |

## [](#general-guidelines)General Guidelines

Disk Configuration

To reduce the risk of disk failure affecting data integrity, use a disk configuration such as RAID with mirroring (RAID 1, RAID10) or parity (RAID 5, 6) to make sure that a single disk failure does not lose data.

Linux OS

* When deploying Enterprise Analytics on production Linux, you should use either the XFS or ext4 filesystem.  
XFS is preferred because it provides more consistent latency, through fairer scheduling, when multiple IO streams are accessing the filesystem. For example, during Data Service compaction or when the working set exceeds the memory quota and the data is read from disk.
* The Enterprise Analytics installer requires the ability to create a normal local Unix user with the name `couchbase`, if such a user does not already exist. This can be important if you’re using a directory service for user management, such as LDAP.