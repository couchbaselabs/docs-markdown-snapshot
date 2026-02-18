---
title: Identifying the Orchestrator Node
description: The node currently running the <em>orchestrator</em> (sometimes
  referred to as the <em>Master Services</em>) can be identified by means of the
  REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-identify-orchestrator.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/rest-api/rest-identify-orchestrator.html)

# Identifying the Orchestrator Node

> The node currently running the _orchestrator_ (sometimes referred to as the _Master Services_) can be identified by means of the REST API. 

## [](#http-method-and-uri)HTTP Method and URI

GET /pools/default/terseClusterInfo

## [](#description)Description

The _orchestrator_ handles operations with cluster-wide impact; such as failover, rebalance, and adding and deleting buckets. Every Couchbase-Server node contains an instance of the orchestrator. However, at any given time, on a multi-node cluster, only one instance of the orchestrator, on one particular node, is active; and thereby responsible for performing _all_ the cluster-wide operations. If a hitherto active instance becomes unavailable, another instance, on another node, takes over.

The `GET /pools/default/terseClusterInfo` http method and URI identify the node on which the active orchestrator currently resides.

For more information on the orchestrator and the cluster manager, see [Cluster Manager](../learn/clusters-and-availability/cluster-manager.md).

This http method and URI are available in Couchbase Server Version 6.6.1 and later.

## [](#curl-syntax)Curl Syntax

curl -v -X GET -u <username>:<password>
  http://<ip-address-or-domain-name>:8091/pools/default/terseClusterInfo

The `ip-address-or-domain-name` should specify a node within the cluster whose orchestrator-location is to be determined: information returned by the call is that which is _known to the specified node_. The `username` and `password` must a user with one of the roles listed in the next section.

## [](#required-privileges)Required Privileges

You must have one of the following roles to call this method:

* [Full Admin](../learn/security/roles.md#full-admin)
* [Analytics Admin](../learn/security/roles.md#analytics-admin)
* [Analytics Manager](../learn/security/roles.md#analytics-manager)
* [Analytics Reader](../learn/security/roles.md#analytics-reader)
* [Analytics Select](../learn/security/roles.md#analytics-select)
* [Backup Full Admin](../learn/security/roles.md#backup-full-admin)
* [Bucket Admin](../learn/security/roles.md#bucket-admin)
* [Application Access](../learn/security/roles.md#application-access)
* [Cluster Admin](../learn/security/roles.md#cluster-admin)
* [Data Backup & Restore](../learn/security/roles.md#data-backup-and-restore)
* [Data DCP Reader](../learn/security/roles.md#data-dcp-reader)
* [Data Monitor](../learn/security/roles.md#data-monitor)
* [Data Reader](../learn/security/roles.md#data-reader)
* [Data Writer](../learn/security/roles.md#data-writer)
* [Eventing Full Admin](../learn/security/roles.md#eventing-full-admin)
* [Manage Scope Functions](../learn/security/roles.md#manage-scope-functions)
* [Search Admin](../learn/security/roles.md#search-admin)
* [Search Reader](../learn/security/roles.md#search-reader)
* [Sync Gateway](../learn/security/roles.md#sync-gateway)
* [Query Delete](../learn/security/roles.md#query-delete)
* [Execute Scope External Functions](../learn/security/roles.md#execute-scope-external-functions)
* [Execute Scope Functions](../learn/security/roles.md#execute-scope-functions)
* [Execute Global External Functions](../learn/security/roles.md#execute-global-external-functions)
* [Execute Global Functions](../learn/security/roles.md#execute-global-functions)
* [Query CURL Access](../learn/security/roles.md#query-curl-access)
* [Query Insert](../learn/security/roles.md#query-insert)
* [Query List Index](../learn/security/roles.md#query-list-index)
* [Manage Scope External Functions](../learn/security/roles.md#manage-scope-external-functions)
* [Manage Scope Functions](../learn/security/roles.md#manage-scope-functions)
* [Manage Global External Functions](../learn/security/roles.md#manage-global-external-functions)
* [Manage Global Functions](../learn/security/roles.md#manage-global-functions)
* [Query Manage Index](../learn/security/roles.md#query-manage-index)
* [Manage Sequences](../learn/security/roles.md#query%5Fmanage%5Fsequences)
* [Query Manage System Catalog](../learn/security/roles.md#query%5Fmanage%5Fsystem%5Fcatalog)
* [Query Select](../learn/security/roles.md#query-select)
* [Query System Catalog](../learn/security/roles.md#query-system-catalog)
* [Query Update](../learn/security/roles.md#query-update)
* [Use Sequences](../learn/security/roles.md#query%5Fuse%5Fsequences)
* [XDCR Admin](../learn/security/roles.md#xdcr-admin)
* [XDCR Inbound](../learn/security/roles.md#xdcr-inbound)
* [Read-Only Admin](../learn/security/roles.md#read-only-admin)
* [Read-Only Security Admin](../learn/security/roles.md#ro-security-admin)
* [Security Admin](../learn/security/roles.md#security-admin)
* [External User Admin](../learn/security/roles.md#external-user-security-admin)
* [Local User Admin](../learn/security/roles.md#local-user-security-admin)
* [Views Admin](../learn/security/roles.md#views-admin)
* [Views Reader](../learn/security/roles.md#views-reader)

## [](#responses)Responses

Success returns `200 OK`, and an object that contains the following key-value pairs:

* `clusterUUID`. The universally unique identifier of the cluster whose orchestrator-node is being returned.
* `orchestrator`. A reference to the node on which the orchestrator is believed, by the specified node, to be running at the time the call is executed. This value is `"undefined"` if, for any reason, the specified node is unaware of the orchestrator-location. In particular, if the orchestrator node is rebalanced out, the value of this attribute will be `"undefined"` during the time-period that starts immediately after the node is rebalanced out, and lasts until a new orchestrator is elected: this period is _10 seconds_ in duration.  
Note that the location of the orchestrator may change at any time, including at a point subsequent to execution of the call but prior to the return of a value; meaning that the returned value is already incorrect. Note also that in cases where the cluster has undergone an unexpected network partition, different specified nodes may return different values.
* `isBalanced`. The value is `true` if the specified node believes that data is distributed evenly, topology-aware services are in balance, and no rebalance is required. Otherwise, the value is `false`.
* `clusterCompatVersion`. The minimum Couchbase-Server _compatibilty version_ for the cluster. For example, if a cluster of ten nodes has eight running Couchbase Server Version 6.6, and two running 6.0, the returned `clusterCompatVersion` value is `"6.0"`.

Failure to authenticate returns `401 Unauthorized`. An incorrectly specified URI returns `404 Object Not Found`.

## [](#example)Example

The following example returns the orchestrator-location for a cluster that includes a node whose IP address is `10.143.210.102`. Note that the output is piped to the [jq](https://stedolan.github.io/jq) command, to facilitate readability:

curl -v -X GET -u Administrator:password \
http://10.143.210.102:8091/pools/default/terseClusterInfo | jq '.'

If the call is successful, `200 OK` is returned, with the following output:

{
  "clusterUUID": "58ea8d6385837b4aa60755a9a6ab81bb",
  "orchestrator": "ns_1@node3.",
  "isBalanced": true,
  "clusterCompatVersion": "8.0"
}

The output thus provides the UUID of the cluster, and the orchestrator-location (which is the node whose IP address is `10.143.210.101`). It also verifies that the cluster currently does not require rebalance, and that its minimum compatibility version is 6.6.

## [](#see-also)See Also

For more information on the orchestrator and the cluster manager, see [Cluster Manager](../learn/clusters-and-availability/cluster-manager.md).