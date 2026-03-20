---
title: Removing Nodes from Clusters
description: Remove nodes from clusters with the <code>POST
  /controller/ejectNode</code> HTTP method and URI.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/reference/pages/rest-cluster-removenode.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:reference:rest-cluster-removenode.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/reference/rest-cluster-removenode.html)

# Removing Nodes from Clusters

> Remove nodes from clusters with the `POST /controller/ejectNode` HTTP method and URI. 

## [](#http-method-and-uri)HTTP method and URI

Server nodes are typically removed from a cluster when the node is temporarily or permanently down.

The method `/controller/ejectNode` cannot remove active nodes. It can be used only on failed over nodes, nodes in pending state, or nodes that have been recently added or joined but not yet rebalanced into the cluster. Removing an active node must be done with the `/controller/rebalance` endpoint.

POST /controller/ejectNode

## [](#syntax)Syntax

HTTP request syntax:

POST /controller/ejectNode
Host: [localhost]:8091
Authorization: Basic xxxxxxxxxxxx
Accept: */*
Content-Length: xxxxxxxxxx
Content-Type: application/x-www-form-urlencoded
otpNode=[node@hostname]

Curl request syntax:

curl -u admin:password -d otpNode=[node@hostname] \
  http://[localhost]:8091/controller/ejectNode

## [](#example)Example

HTTP request example:

POST /controller/ejectNode
Host: 192.168.0.106:8091
Authorization: Basic xxxxxxxxxxxx
Accept: */*
Content-Length: xxxxxxxxxx
Content-Type: application/x-www-form-urlencoded
otpNode=ns_1@192.168.0.107

Curl request example:

curl -u Administrator:password -d 'otpNode=ns_1@192.168.0.107' \
  http://192.168.0.106:8091/controller/ejectNode

## [](#response-codes)Response codes

200 OK - node ejected
400 Error, the node to be ejected does not exist
401 Unauthorized - Credentials were not supplied and are required
403 Forbidden - Credentials were supplied and are incorrect