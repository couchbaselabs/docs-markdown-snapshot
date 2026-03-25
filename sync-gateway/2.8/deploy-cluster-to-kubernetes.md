---
title: Deploying a Sync Gateway Cluster
description: Connect Sync Gateway to a Server Cluster Deployed with CAO 1.2.x
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/deploy-cluster-to-kubernetes.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::deploy-cluster-to-kubernetes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/deploy-cluster-to-kubernetes.html)

# Deploying a Sync Gateway Cluster

> Connect Sync Gateway to a Server Cluster Deployed with CAO 1.2.x  
> Provides access to instruction on deploying a Sync Gateway cluster on Kubernetes and connecting with a Couchbase Server cluster

## [](#how-to)How to

Follow the instructions in this tutorial to connect Sync Gateway deployed on kubernetes to a Couchbase Server cluster — [Connect Sync Gateway to a Couchbase Cluster](#2.0@operator::tutorial-sync-gateway.adoc). See also the prerequisites in the tutorial’s [Connecting Sync Gateway to Server (Prerequisites)](#2.0@operator::tutorial-sync-gateway.adoc#prerequisites) section.

**If the Couchbase Server was deployed using Couchbase Autonomous Operater 1.2**, then the following deviations from those instructions apply:

* You cannot configure Mutual TLS (mTLS, or two-way TLS) to connect to the Couchbase Server, although you _can_ use one-way TLS (see: the tutorial’s [Enabling TLS Connectivity to Couchbase Server](#2.0@operator::tutorial-sync-gateway.adoc#enabling-tls-connectivity-to-couchbase-server) section).
* If you are using RBAC users to connect, you need to create the sync gateway user as shown in [Create an RBAC User](#2.8@sync-gateway::start/get-started-configure-server.adoc#step-2lbl-create-rbac-user).  
This user is referenced in the tutorial’s [Configuring RBAC User for Sync Gateway](#2.0@operator::tutorial-sync-gateway.adoc#configuring-rbac-user-for-sync-gateway) section.

## [](#related-content)Related Content

###### [](#)

Learn more …​

* [Deploying Sync Gateway](#2.0@operator::tutorial-sync-gateway.adoc#deploying-sync-gateway)
* [Expose Sync Gateway to Couchbase Lite clients](#2.0@operator::tutorial-sync-gateway-clients.adoc)
* [Manage a Sync Gateway Cluster](#2.0@operator::tutorial-sync-gateway-manage.adoc)

###### [](#-2)

Reference material …​

* [Inter Cluster Replication](sync-inter-syncgateway-run.md)
* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

Blog — [Deploy Sync Gateway Clusters on Kubernetes](https://blog.couchbase.com/couchbase-sync-gateway-on-kubernetes/)