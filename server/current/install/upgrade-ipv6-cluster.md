---
title: Upgrade an IPv6 Cluster
description: "All pre-7.0 clusters using the IPv6 address family can be upgraded
  to Couchbase Server Enterprise Edition 7.0: in some cases, additional steps
  are required in the upgrade-procedure."
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/install/pages/upgrade-ipv6-cluster.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/install/upgrade-ipv6-cluster.html)

# Upgrade an IPv6 Cluster

> All pre-7.0 clusters using the IPv6 address family can be upgraded to Couchbase Server Enterprise Edition 7.0: in some cases, additional steps are required in the upgrade-procedure. 

## [](#ipv6-cluster-upgrade-to-7-0)IPv6 Cluster-Upgrade to 7.0+

A pre-7.0 Couchbase Server-cluster that is currently using the IPv6 address family can be upgraded to run 7.0+ _and_ to continue using IPv6:

* _All_ IPv6 clusters running a pre-7.0 version of Couchbase Server Enterprise Edition can perform _online_ upgrade as explained in [Performing the Rolling Online Upgrade](upgrade-cluster-online.md).
* IPv6 clusters currently running Couchbase Server Enterprise Edition Version 6.0.1 or higher can perform _offline_ upgrade as explained in [Upgrade an Offline Cluster](upgrade-cluster-offline.md).
* IPv6 clusters currently running Couchbase Server Enterprise Edition Version 6.0.0 can perform _offline_ upgrade as explained in [Upgrade and Offline Cluster](upgrade-cluster-offline.md), but must then perform the additional steps described below.

Note that pre-7.0 clusters that are to be upgraded to 7.0+, and whose address family is to be changed, should _first_ be upgraded to 7.0+, and _subsequently_ be assigned the new address family (since upgrade and address-family change _cannot_ be performed simultaneously). Note also that if a pre-7.0 cluster is not using IPv6 and no address-family change is required, the cluster can be upgraded to 7.0+ by either an _offline_ or an _online_ procedure, with its address-family setting remaining unchanged.

### [](#additional-upgrade-steps-for-some-clusters)Additional Upgrade Steps for Some Clusters

To complete _offline_ upgrade to 7.0+ for a 6.0.0 cluster that has already been running IPv6 and is intended to continue doing so, after completion of the instructions in [Performing the Offline Upgrade](upgrade-cluster-offline.md), proceed as follows:

1. Stop Couchbase Server. For instructions on stopping a server installed by the standard, _package-based_ procedure, see [Start and Stop Couchbase Server](startup-shutdown.md). For instructions on stopping a server installed by the _non-root_ procedure, see [Non-Root Install and Upgrade](non-root.md), in the section [Stop, Start, and Get Status](non-root.md#start-stop-and-get-status).
2. As either _root_ or _couchbase user_, enter the following command:  
if [ -e /opt/couchbase/var/lib/couchbase/config/dist_cfg ] && [ ! -s /opt/couchbase/var/lib/couchbase/config/dist_cfg ]; then  
  echo "[{preferred_external_proto,inet6_tcp_dist}, {preferred_local_proto, inet6_tcp_dist}]." > /opt/couchbase/var/lib/couchbase/config/dist_cfg;  
fi
3. Start Couchbase Server.

This concludes the upgrade-process.