---
title: Reinitializing Nodes
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/reference/pages/rest-reinitialize-node.adoc
  xref: xref:2.1@enterprise-analytics:reference:rest-reinitialize-node.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/reference/rest-reinitialize-node.html)

# Reinitializing Nodes

> After an unsafe failover, failed-over nodes can be individually reinitialized by means of the REST API. 

## [](#http-method-and-uri)HTTP Method and URI

POST /controller/hardResetNode

## [](#description)Description

Reinitializes a node, such that all configuration settings and all data are lost. This HTTP method and URI should be used with caution: a backup of all data on the system is recommended to be performed before reinitialization.

This HTTP method and URI are intended for use subsequent to an _unsafe failover_; which results in multiple failed-over nodes needing reinitialization before they can be added back into the cluster.

The Full Admin role is required.

After its reinitialization, a reinitialized node can be reconfigured. Note that the call is idempotent, and can be used on the same node multiple times, with the same result.

For detailed information about unsafe failover and its consequences, see [Hard Failover in Default and Unsafe Modes](#learn:clusters-and-availability/hard-failover.adoc#default-and-unsafe). For information about reinitialization, see [Cluster Initialization and Provisioning](rest-cluster-init-and-provisioning.md).

## [](#curl-syntax)Curl Syntax

curl -X POST http://<ip-address-or-domain-name>:8091/controller/hardResetNode
  -u <username>:<password>

The `ip-address-or-domain-name` must be that of the node that is to be reinitialized. The `username` and `password` must be those of a user with the Full Admin role.

## [](#responses)Responses

Success returns `200 OK`. Failure to authenticate returns `401 Unauthorized`. A malformed URI returns `404 Object Not Found` with the message `requested resource not found`.

## [](#example)Example

The following example reinitializes node `10.145.250.103`.

curl -v -X POST http://10.145.250.103:8091/controller/hardResetNode -u Administrator:password

## [](#see-also)See Also

For the REST API for hard failover, see [Performing Hard Failover](rest-node-failover.md). For detailed information about unsafe failover and its consequences, see [Hard Failover in Default and Unsafe Modes](#learn:clusters-and-availability/hard-failover.adoc#default-and-unsafe). For information about reinitialization, see [Cluster Initialization and Provisioning](rest-cluster-init-and-provisioning.md).