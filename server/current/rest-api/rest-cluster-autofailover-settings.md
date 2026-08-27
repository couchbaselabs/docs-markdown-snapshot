---
title: Retrieving Auto-Failover Settings
description: Use the  <code>/settings/autoFailover</code> endpoint to get the
  current auto-failover settings.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-cluster-autofailover-settings.adoc
  xref: xref:server:rest-api:rest-cluster-autofailover-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/rest-api/rest-cluster-autofailover-settings.html)

# Retrieving Auto-Failover Settings

> Use the `/settings/autoFailover` endpoint to get the current auto-failover settings. 

## [](#http-method-and-uri)HTTP Method and URI

```bourne
GET /settings/autoFailover
```

## [](#description)Description

The `GET /settings/autoFailover` HTTP method and URI retrieve auto-failover settings for the cluster.

Auto-failover settings are global, applying to all nodes in the cluster.

## [](#curl-syntax)Curl Syntax

```bourne
curl -X GET http://<ip-address-or-hostname>:8091/settings/autoFailover \
     -u <username>:<password>
```

## [](#required-permissions)Required Permissions

You must have one of the following roles to be able to read the auto-failover settings:

* [Full Admin](../learn/security/roles.md#full-admin)
* [Backup Full Admin](../learn/security/roles.md#backup-full-admin)
* [Bucket Admin](../learn/security/roles.md#bucket-admin)
* [Cluster Admin](../learn/security/roles.md#cluster-admin)
* [Eventing Full Admin](../learn/security/roles.md#eventing-full-admin)
* [XDCR Admin](../learn/security/roles.md#xdcr-admin)
* [Read-Only Admin](../learn/security/roles.md#read-only-admin)
* [Read-Only Security Admin](../learn/security/roles.md#ro-security-admin)
* [Security Admin](../learn/security/roles.md#security-admin)
* [External User Admin](../learn/security/roles.md#external-user-security-admin)
* [Local User Admin](../learn/security/roles.md#local-user-security-admin)
* [Views Admin](../learn/security/roles.md#views-admin)

## [](#responses)Responses

200 OK

The call was successful. Also returns an object containing the current state of the auto-failover settings. See [Example](#example) for an example of the response.

401 Unauthorized

The user credentials supplied with the call do not have the correct permissions to read the auto-failover settings.

404 Not Found

The URL was incorrect.

## [](#example)Example

The following example returns the auto-failover settings for the cluster. It pipes the output through the [jq](https://stedolan.github.io/jq) command to improve readability.

```console
curl -X GET http://localhost:8091/settings/autoFailover \
     -u Administrator:password | jq '.'
```

If successful, execution returns the auto-failover settings for the cluster. For example:

```json
{
  "enabled": true,
  "timeout": 120,
  "count": 0,
  "failoverOnDataDiskIssues": {
    "enabled": false,
    "timePeriod": 120
  },
  "maxCount": 1,
  "canAbortRebalance": true,
  "failoverPreserveDurabilityMajority": false,
  "failoverOnDataDiskNonResponsiveness": {
    "enabled": false,
    "timePeriod": 120
  },
  "allowFailoverEphemeralNoReplicas": false
}
```

The keys in the object returned in the example are:

* `enabled`Whether automatic failover is on (a value of `true`) or off (`false`).
* `timeout`The number of seconds Couchbase Server waits after a node has become unavailable before it performs an automatic failover. This value can be between 5 and 3600\. The default value is 120.
* `count`. The number of nodes that Couchbase Server has auto-failed over. Couchbase Server resets this value to zero either when the cluster rebalances to remove or rejoin the failed nodes, or when an administrator manually resets the count (see [Resetting Auto-Failover](rest-cluster-autofailover-reset.md)). The parameter's default value is 0\. If number of failed-over nodes reaches the maximum count set by `maxCount`, Couchbase Server refuses to auto-failover more nodes until you reset the count or resolve the auto-failovers with a recovery and rebalance.
* `failoverOnDataDiskIssues`. This object contains two keys:

  * `enabled` indicates whether auto-failover can occur when a disk has been unresponsive, and which can be `true` or `false` (the default).
  * `timePeriod`, which indicates the administrator-specified time-period, in seconds, after which auto-failover is triggered, when a disk is unresponsive. The value is an integer between 5 and 3600.
* `maxCount`. The maximum number of nodes that can be auto-failed over at the same time. When the count of auto-failed over nodes reaches this value, Couchbase Server does not trigger additional auto-failovers. You must either resolve the auto-failovers through rebalancing the cluster to remove or recover the failed-over nodes or reset the count of failed over nodes. The default value is 1.
* `canAbortRebalance`Whether or not Couchbase Server can auto-failover a node while a rebalance is taking place. This feature is only available in Couchbase Server Enterprise Edition. The value can be either `true` (the default) or `false`.
* `failoverPreserveDurabilityMajority`Indicates whether Couchbase Server refuses to auto-failover a node if doing so could result in the loss of durably written data.
* `failoverOnDataDiskNonResponsiveness`This object contains two keys that control auto-failover when a data disk is non-responsive:

  * `enabled` indicates whether Couchbase Server initiates an auto-failover on a node when its data disk has failed to complete an operation in the period set by `timePeriod`. This value can be `true`, which enables the auto-failover, or the default `false` which does not trigger a failover due to disk unresponsiveness.
  * `timePeriod`Indicates amount of time a data disk on a node has to be unresponsive before Couchbase Server can trigger an auto-failover. This value defaults to 120.  
For more information about these values, see [Failover on Data Disk Non-Responsiveness](../learn/clusters-and-availability/automatic-failover.md#failover-on-data-disk-non-responsiveness).
* `allowFailoverEphemeralNoReplicas`Indicates whether Couchbase Server can auto-failover a node that contains vBuckets for an unreplicated ephemeral bucket. This value can be `true`, which allows auto-failover of such nodes, or the default `false` which prevents auto-failover of such nodes.  
For more information about this value, see [Auto-failover for Ephemeral Buckets with No Replicas](../learn/clusters-and-availability/automatic-failover.md#ephemeral-buckets-with-no-replicas).

## [](#see-also)See Also

* For information about setting auto-failover parameters with the REST API, see [Enabling and Disabling Auto-Failover](rest-cluster-autofailover-enable.md).
* The Couchbase Server command line tool [setting-autofailover](../cli/cbcli/couchbase-cli-setting-autofailover.md) lets you manage auto-failover.
* For information about managing auto-failover with Couchbase Server Web Console, see [Node Availability](../manage/manage-settings/general-settings.md#node-availability).
* For information about auto-failover see [Automatic Failover](../learn/clusters-and-availability/automatic-failover.md).