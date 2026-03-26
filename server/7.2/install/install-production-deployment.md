---
title: Deployment Guidelines
description: Before you install Couchbase Server, follow the recommended
  deployment guidelines for setting up your production environment.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/install-production-deployment.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:install:install-production-deployment.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/install/install-production-deployment.html)

# Deployment Guidelines

> Before you install Couchbase Server, follow the recommended deployment guidelines for setting up your production environment. 

__Table 1\. Couchbase Server Deployment Guidelines__
| Guideline                                     | Description                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sizing**                                    | Evaluate the overall performance and capacity requirements of your deployment, and determine the hardware and other resources. [Sizing Guidelines](sizing-general.md) [Services](../learn/services-and-indexes/services/services.md)                                                                                                                      |
| **Time keeping**                              | Keeping accurate time is essential to a properly-functioning database. Ensure that you follow the guidelines for synchronizing each Couchbase node using Network Time Protocol (NTP). [Clock Sync with NTP](synchronize-clocks-using-ntp.md)                                                                                                              |
| **Disable Transparent Huge Pages**            | You must disable the THP memory management system on each node that runs Couchbase Server. [Disabling Transparent Huge Pages (THP)](thp-disable.md)                                                                                                                                                                                                       |
| **Set kernel swappiness**                     | The _kernel swappiness_ setting defines how aggressively the kernel will swap memory pages versus dropping pages from the page cache. You need to set the swappiness setting to 0, or at most 1, for optimal Couchbase Server operation. [Swap Space and Kernel Swappiness](install-swap-space.md)                                                        |
| **Couchbase client deployment**               | Deploy client applications that incorporate Couchbase SDKs to enable interaction with Couchbase clusters. [SDKs & Connectors](../../../home/sdk.md)                                                                                                                                                                                                       |
| **Security**                                  | Couchbase Server provides security features that allow administrators to implement various security controls to ensure secure deployment. You should take Couchbase security best practices into consideration before, during, and after deployment. [Security](../learn/security/security-overview.md) [Couchbase Server Processes](server-processes.md) |
| **Virtualized and containerized deployments** | Certain considerations must be made when you're deploying Couchbase Server on a virtual machine or container. [Deployment Considerations for Virtual Machines and Containers](best-practices-vm.md)                                                                                                                                                       |
| **Clusters with less than three nodes**       | Couchbase Server clusters with less than three nodes are not recommended in production. However, you might find a need to have a smaller deployment for test and development purposes. [About Deploying Clusters With Less Than Three Nodes](deployment-considerations-lt-3nodes.md)                                                                      |

## [](#general-guidelines)General Guidelines

Disk Configuration

To reduce the likelihood of disk failure affecting data integrity, consider using a disk configuration such as RAID with mirroring (RAID 1, RAID10) or parity (RAID 5, 6) to ensure that a single disk failure does not lose data.

If bucket replicas are set to 2 or higher, the administrator might rely on database-level replication for data durability.

Linux OS

* When deploying Couchbase Server on production Linux, you should use either the XFS or ext4 file system.  
XFS is preferred because it provides more consistent latency (fairer scheduling) when multiple IO streams are accessing the file system, such as during Data Service compaction or when the working set exceeds the memory quota and the data is read from disk.
* The Couchbase Linux installer requires the ability to create a normal local Unix user with the name `couchbase`, if such a user doesn't already exist. This can be particularly important if you are using a directory service for user management, such as LDAP.

Windows OS

For Windows OS, use 64k allocation sizes on NTFS file systems.