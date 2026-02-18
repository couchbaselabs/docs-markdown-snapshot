---
title: Prerequisites and System Requirements
editUrl: https://github.com/couchbaselabs/observability/edit/0.2.x/docs/modules/ROOT/pages/prerequisite-and-setup.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cmos/current/prerequisite-and-setup.html)

# Prerequisites and System Requirements

> CMOS supports both on-premise and Kubernetes deployments using a standard container deployment in each case. 

> [!NOTE]
> For all supported software versions listed on this page, maintenance/patch releases (x.x**.X**) inherit the same support level, unless noted otherwise.

## [](#couchbase-server-compatibility)Couchbase Server Compatibility

This release supports the monitoring of the following Couchbase software:

| Software                            | Version  |
| ----------------------------------- | -------- |
| Couchbase Server Enterprise Edition | 6.6, 7.0 |

If you are using Couchbase Server 6.6, you will need the [Couchbase Prometheus Exporter](https://github.com/couchbase/couchbase-exporter) set up on each of your Couchbase Server nodes.

## [](#cpu-and-memory-requirements)CPU and Memory Requirements

Using this feature will require:

* 2 CPUs per container instance/pod.
* 512MiB of memory per container instance/pod.

## [](#graphics-requirements)Graphics Requirements

CMOS supports the following resolutions for the Grafana dashboards supplied:

* Recommended: 1920x1080
* Minimum: 1366x768

The dashboards will still function for any resolution supported by Grafana but may appear sub-optimal.

## [](#rbac-and-networking-requirements)RBAC and Networking Requirements

CMOS needs to be able to route network traffic to and from the clusters to monitor. It needs appropriate credentials supplied to access the monitoring information. CMOS does not need to monitor the host it is running on.

## [](#container-requirements)Container Requirements

CMOS is deployed as a container instance even on-premise so requires a functional container runtime to be installed and configured appropriately. We recommend using [Docker](https://docs.couchbase.com/cloud-native-database/containers/docker-basic-install.html).

The container runtime will need access to the CMOS container from an appropriate registry or pre-loaded directly on to the node running the container.

If your Couchbase Server is running in Docker, you may need to set [extra options](https://docs.docker.com/network/) to permit them to communicate with CMOS.