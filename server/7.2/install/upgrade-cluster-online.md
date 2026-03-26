---
title: Upgrade an Online Cluster
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/upgrade-cluster-online.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:install:upgrade-cluster-online.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/install/upgrade-cluster-online.html)

# Upgrade an Online Cluster

> A cluster can be upgraded while continuing to serve data. 

## [](#online-upgrade-at-reduced-and-full-capacity)Online Upgrade at Reduced and Full Capacity

A Couchbase-Server cluster can be upgraded while continuing to serve data. A _spare node_ must be used, if the cluster is to serve data at full capacity for the duration of the upgrade. If no spare node is available, the cluster must serve data at reduced capacity, for the duration of the upgrade. The available procedures are provided as follows:

* [Upgrade a Reduced-Capacity, Online Cluster](upgrade-cluster-online-reduced-capacity.md)
* [Upgrade a Full-Capacity, Online Cluster](upgrade-cluster-online-full-capacity.md)
* [Upgrade an Online Docker Cluster, Full Capacity](upgrade-docker-cluster-online-full-capacity.md)  
> [!NOTE]  
> It is not possible to upgrade a Docker cluster with a single node. A second node will needed to ensure data is transferred.

### [](#tls-address-family-restriction-and-node-addition)TLS, Address-Family Restriction, and Node Addition

Couchbase Server Version 7.0.2+ allows TLS to be specified as mandatory for all internal and external cluster-communications — see [Manage On-the-Wire Security](../manage/manage-security/manage-tls.md). It also allows the cluster's address family to be specifically restricted to either IPv4 or IPv6 — see [Manage Address Families](../manage/manage-nodes/manage-address-families.md).

The procedures described in the current section both involve the introduction of upgraded nodes into an existing, online cluster. If the cluster is running Version 6.0.x, and the upgraded node is running Version 7.0.2+, and the upgraded node has TLS specified as mandatory, and/or has its address family restricted to either IPv4 or IPv6, the upgraded node _cannot_ be added to the cluster.

To add the node to the cluster, change the node's TLS setting so that TLS is _not_ mandatory for all communications, and/or change the node's address family so that it is _not_ specifically restricted to either IPv4 or IPv6\. Then, _restart_ the node. After the node has restarted, it can be added to the 6.0.x cluster.