[View original HTML](/server/current/install/upgrade-procedures.html)

> Multiple procedures are provided for the upgrade of a Couchbase-Server cluster. 

This section provides step-by-step instructions for the upgrade of multi-node Couchbase-Server clusters. Each procedure addresses a specific context and its associated dependencies: for information on how to select the appropriate procedure, see the information provided in [Upgrade Procedure-Selection](upgrade-procedure-selection.md).

Additionally provided on this page is guidance for [Upgrading Developer Clusters](#upgrading-developer-clusters) — which are frequently _single-node_ clusters.

## [](#upgrading-multi-node-clusters)Upgrading Multi-Node Clusters

The procedures for upgrading multi-node clusters are presented as follows:

* [Upgrade an Offline Cluster](upgrade-cluster-offline.md). This is the simplest procedure for the upgrade of a multi-node cluster. Note, however, that it requires cluster-downtime.
* [Upgrade an Online Cluster](upgrade-cluster-online.md). This allows the cluster to continue serving data, for the duration of the upgrade. Two options are provided:

  * [Upgrade a Reduced-Capacity, Online Cluster](upgrade-cluster-online-reduced-capacity.md). If no additional nodes are available to facilitate the upgrade-procedure, the procedure can be completed with the existing cluster-nodes, provided that it is acceptable for the cluster to serve data, during the upgrade, at reduced capacity.
  * [Upgrade a Full-Capacity, Online Cluster](upgrade-cluster-online-full-capacity.md). If additional nodes are available to facilitate the upgrade-procedure, the procedure can be completed with the cluster continuing to serve data at full capacity.
* [Upgrade an IPv6 Cluster](upgrade-ipv6-cluster.md). Special instructions are provided for the upgrade of IPv6 clusters.

## [](#upgrading-developer-clusters)Upgrading Developer Clusters

Clusters are frequently established for development purposes. When these are _multi-node_, the upgrade procedures listed above, in [Upgrading Multi-Node Clusters](#upgrading-multi-node-clusters), can be followed.

However, clusters established for development purposes are frequently _single-node_ clusters. Single-node clusters are _unsupported_: nevertheless, they can be upgraded by following subsets of the instructions provided for multi-node clusters; as described below. Before following these procedures, developers should become familiar with the [Upgrade Paths](upgrade.md#supported-upgrade-paths); and, if appropriate, with the information provided in [Upgrade an IPv6 Cluster](upgrade-ipv6-cluster.md).

### [](#upgrading-linux-and-windows-based-single-node-clusters)Upgrading Linux- and Windows-Based Single-Node Clusters

The cluster should be taken _offline_ (such that no application access is possible) for the duration of the upgrade process. Therefore, the step-by-step procedure provided in [Upgrade an Offline Cluster](upgrade-cluster-offline.md) can be followed. Note that when following the steps in the stage named [Upgrade Each Individual Node](upgrade-cluster-offline.md#upgrade-each-individual-node), the final step can be omitted (since only one node needs to be upgraded).

### [](#upgrading-macos-based-single-node-clusters)Upgrading MacOS-Based Clusters

Command-line expressions for _upgrade_ are not supported for MacOS: therefore, a MacOS-based cluster must be upgraded by means of _install_ command-line expressions. As with Linux- and Windows-based single-node clusters, a MacOS-based single-node cluster should remain offline for the duration of the upgrade process.

Therefore, to upgrade a MacOS-based single-node cluster, proceed as follows:

1. Follow the instructions provided for offline multi-node clusters, in [Stage One: Prepare the Cluster](upgrade-cluster-offline.md#prepare-the-cluster) (which is part of the procedure [Upgrade an Offline Cluster](upgrade-cluster-offline.md)).
2. Follow the instructions provided for online multi-node clusters, in [Stage Three: Upgrade the Removed Node](upgrade-cluster-online-reduced-capacity.md#upgrade-the-removed-node) (which is part of the procedure [Upgrade a Reduced-Capacity, Online Cluster](upgrade-cluster-online-reduced-capacity.md)).
3. Follow the instructions provided for offline multi-node clusters, in [Stage Three: Bring the Cluster Back Online](upgrade-cluster-offline.md#bring-the-cluster-back-online) (which is part of the procedure [Upgrade an Offline Cluster](upgrade-cluster-offline.md)).

This concludes the upgrade procedure.