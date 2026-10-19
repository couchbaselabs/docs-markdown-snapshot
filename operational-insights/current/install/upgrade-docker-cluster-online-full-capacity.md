---
title: Upgrade an Online Docker Cluster, Full Capacity
description: You can upgrade a cluster of Enterprise Analytics Docker containers
  to Operational Insights while it stays online and at full capacity.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: procedure
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/upgrade-docker-cluster-online-full-capacity.adoc
  xref: xref:enterprise-analytics:install:upgrade-docker-cluster-online-full-capacity.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/upgrade-docker-cluster-online-full-capacity.html)

# Upgrade an Online Docker Cluster, Full Capacity

> You can upgrade a cluster of Enterprise Analytics Docker containers to Operational Insights while it stays online and at full capacity. 

## [](#understanding-the-docker-upgrade)Understanding the Docker Upgrade

A container is never upgraded in place. Instead, each Enterprise Analytics container is removed from the cluster and deleted, then re-created from the Operational Insights image and added back. A spare container joins the cluster first, so that the cluster stays at full capacity, and so that you can manage the cluster while the container whose ports you normally use is being replaced.

For the background, see [Upgrade Procedure Selection](upgrade-procedure-selection.md). Each rebalance in the procedure suspends ingestion from the cluster's links until it completes, and queries against the partitions that changed hands run with higher latency until the new containers have cached their data, which they do lazily, on first access. See [Swap Rebalance](upgrade-procedure-selection.md#swap-rebalance). You should also be familiar with [Install with Docker](getting-started-docker.md).

The procedure assumes that:

* The cluster must continue to serve requests throughout the upgrade.
* The cluster runs Enterprise Analytics 2.1.x (other than 2.1.0-MP3) or 2.2.x, from the `couchbase/enterprise-analytics` image. For other versions, see [Upgrade Paths](upgrade.md#supported-upgrade-paths).
* The host has the resources to run one more container than the cluster has nodes.
* Containers are replaced one at a time.

In the examples, the cluster's containers are named `ea1`, `ea2`, and `ea3`, and `ea3` publishes the cluster's ports on the host.

## [](#prepare-the-cluster)1\. Prepare the Cluster

1. Confirm that the cluster is healthy: every node is active, and no rebalance is running or needed.
2. Record the cluster's configuration, so that you can compare it after the upgrade. This includes the databases, scopes, collections, and links, and the settings you have changed from their defaults.

## [](#create-the-spare-node)2\. Create the Spare Container

Create a container from the Operational Insights image, publishing its ports on host ports that do not clash with those of the existing containers:

```console
docker run -d --name spare \
  -p 28091:8091 -p 28095:8095 -p 28191:18091 -p 28195:18095 \
  couchbase/operational-insights:3.0.0
```

Do not initialize the new node, or create a cluster on it.

## [](#add-the-spare-node)3\. Add the Spare Container to the Cluster

Find the spare container's address on the Docker network:

```console
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' spare
```

Add it to the cluster, and rebalance. Every Operational Insights node runs the same fixed set of services, so do not specify any:

```console
docker exec ea3 /opt/enterprise-analytics/bin/couchbase-cli server-add \
  -c localhost:8091 -u ${USERNAME} -p ${PASSWORD} \
  --server-add https://${SPARE_ADDRESS}:18091 \
  --server-add-username Administrator --server-add-password password

docker exec ea3 /opt/enterprise-analytics/bin/couchbase-cli rebalance \
  -c localhost:8091 -u ${USERNAME} -p ${PASSWORD}
```

You can also use the Operational Insights Web Console, as described in [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md). From now on, you can reach the Web Console on the spare container's host port, `28091` in this example.

## [](#remove-node-for-upgrading)4\. Remove a Container from the Cluster

Rebalance one Enterprise Analytics container out of the cluster. Run the command from a container that remains in the cluster, such as the spare:

```console
docker exec spare /opt/couchbase/bin/couchbase-cli rebalance \
  -c localhost:8091 -u ${USERNAME} -p ${PASSWORD} \
  --server-remove ${EA_CONTAINER_ADDRESS}:8091
```

Wait for the rebalance to complete before you continue.

## [](#delete-the-container)5\. Delete the Container

Delete the container that you removed, together with its volumes:

```console
docker rm -f -v ea1
```

The container's volumes hold the state of a node that's no longer part of the cluster, and are not needed again. Do not attach them to the new container: it joins the cluster as a new node. If you mounted a named volume, delete it with `docker volume rm`.

## [](#upgrade-the-container)6\. Create the Operational Insights Container

Create a container from the Operational Insights image. If the container you deleted published ports on the host, publish the same ports, so that applications and administrators can reach the cluster as before.

```console
docker run -d --name oi1 couchbase/operational-insights:3.0.0
```

For the container that publishes the cluster's ports, `ea3` in this example:

```console
docker run -d --name oi3 \
  -p 8091:8091 -p 8095:8095 -p 18091:18091 -p 18095:18095 \
  couchbase/operational-insights:3.0.0
```

## [](#add-new-node-and-rebalance)7\. Add the New Container to the Cluster and Rebalance

Use the spare container to add the new container to the cluster, then rebalance:

```console
docker exec spare /opt/couchbase/bin/couchbase-cli server-add \
  -c localhost:8091 -u ${USERNAME} -p ${PASSWORD} \
  --server-add https://${NEW_CONTAINER_ADDRESS}:18091 \
  --server-add-username Administrator --server-add-password password

docker exec spare /opt/couchbase/bin/couchbase-cli rebalance \
  -c localhost:8091 -u ${USERNAME} -p ${PASSWORD}
```

## [](#repeat-for-all-nodes)8\. Repeat for Every Enterprise Analytics Container

Repeat the steps from [Section 4](#remove-node-for-upgrading) to [Section 7](#add-new-node-and-rebalance) for each remaining Enterprise Analytics container.

> [!CAUTION]
> Do not remove the spare container by mistake. You use it to manage the cluster until every other container has been replaced.

## [](#remove-the-spare-node)9\. Remove the Spare Container

Use a container other than the spare to rebalance the spare out of the cluster, then delete it:

```console
docker exec oi3 /opt/couchbase/bin/couchbase-cli rebalance \
  -c localhost:8091 -u ${USERNAME} -p ${PASSWORD} \
  --server-remove ${SPARE_ADDRESS}:8091

docker rm -f -v spare
```

## [](#finish-the-upgrade)10\. Confirm the Upgrade

Shortly after the last Enterprise Analytics container leaves the cluster, the cluster moves to Operational Insights 3.0, and the Analytics Service restarts on every node to switch to the new version. Requests that are running at that moment fail, and can be retried.

To check, read the cluster's compatibility version, which each node reports as `3.0.0` when the upgrade is complete:

```console
curl -s -u ${USERNAME}:${PASSWORD} http://localhost:8091/pools/default \
  | jq -r '.nodes[].prodCompatVersion'
```

Compare the cluster's configuration with the record you made in [Section 1](#prepare-the-cluster).

The cluster is now fully upgraded. New features of Operational Insights 3.0 are now available. See [Feature Availability During Upgrade](upgrade-feature-availability.md).