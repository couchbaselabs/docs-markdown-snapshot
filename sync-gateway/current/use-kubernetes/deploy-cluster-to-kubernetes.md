---
title: Deploying a Sync Gateway Cluster
description: Connect Sync Gateway to a Server Cluster Deployed with CAO 1.2.x
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/use-kubernetes/pages/deploy-cluster-to-kubernetes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:sync-gateway:use-kubernetes:deploy-cluster-to-kubernetes.adoc[]
---

[View original HTML](/sync-gateway/current/use-kubernetes/deploy-cluster-to-kubernetes.html)

# Deploying a Sync Gateway Cluster

> Connect Sync Gateway to a Server Cluster Deployed with CAO 1.2.x  
> Provides access to instruction on deploying a Sync Gateway cluster on Kubernetes and connecting with a Couchbase Server cluster

## [](#how-to)How to

Follow the instructions in this tutorial to connect Sync Gateway deployed on _Kubernetes_ to a Couchbase Server cluster — [Connect Sync Gateway to a Couchbase Cluster](../../../operator/current/tutorial-sync-gateway.md). See also the prerequisites in the tutorial’s [Connecting Sync Gateway to Server (Prerequisites)](../../../operator/current/tutorial-sync-gateway.md#prerequisites) section.

**If the Couchbase Server was deployed using Couchbase Autonomous Operater 1.2**, then the following deviations from those instructions apply:

* You cannot configure Mutual TLS (mTLS, or two-way TLS) to connect to the Couchbase Server, although you _can_ use one-way TLS (see: the tutorial’s [Enabling TLS Connectivity to Couchbase Server](../../../operator/current/tutorial-sync-gateway.md#enabling-tls-connectivity-to-couchbase-server) section).
* If you are using RBAC users to connect, you need to create the sync gateway user as shown in [Create an RBAC User](../start-here/get-started-prepare.md#step-2create-rbac-user).  
This user is referenced in the tutorial’s [Configuring RBAC User for Sync Gateway](../../../operator/current/tutorial-sync-gateway.md#configuring-rbac-user-for-sync-gateway) section.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Deploying Sync Gateway](../../../operator/current/tutorial-sync-gateway.md#deploying-sync-gateway)
* [Expose Sync Gateway to Couchbase Lite clients](../../../operator/current/tutorial-sync-gateway-clients.md)
* [Manage a Sync Gateway Cluster](../../../operator/current/tutorial-sync-gateway-manage.md)

###### [](#-3)

Reference material …​

* [Inter Cluster Replication](../sync/sync-inter-syncgateway-run.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Blog — [Deploy Sync Gateway Clusters on Kubernetes](https://blog.couchbase.com/couchbase-sync-gateway-on-kubernetes/)