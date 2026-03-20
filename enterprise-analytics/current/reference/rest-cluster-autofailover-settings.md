---
title: Retrieving Auto-Failover Settings
description: Auto-failover settings are retrieved by means of the <code>GET
  /settings/autoFailover</code> HTTP method and URI.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/reference/pages/rest-cluster-autofailover-settings.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:reference:rest-cluster-autofailover-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/reference/rest-cluster-autofailover-settings.html)

# Retrieving Auto-Failover Settings

> Auto-failover settings are retrieved by means of the `GET /settings/autoFailover` HTTP method and URI. 

## [](#http-method-and-uri)HTTP method and URI

```bourne
GET /settings/autoFailover
```

## [](#description)Description

The `GET /settings/autoFailover` HTTP method and URI retrieve auto-failover settings for the cluster.

Auto-failover settings are global, and apply to all nodes in the cluster. To read auto-failover settings, one of the following roles is required: Full Admin, Cluster Admin, Read-Only Admin, Local User Security Admin, External User Security Admin.

## [](#curl-syntax)Curl Syntax

```bourne
curl -X GET http://<ip-address-or-hostname>:8091/settings/autoFailover
  -u <username>:<password>
```

## [](#responses)Responses

Success returns `200 OK`, and an object that contains the following parameters:

* `enabled`. Indicates whether automatic failover is enabled (a value of `true`) or disabled (a value of `false`).
* `timeout`. Returns an integer between 5 and 3600, which specifies the number of seconds set to elapse, after a node has become unavailable, before automatic failover is triggered. The default value is 120.
* `count`. This parameter represents how many auto-failover nodes have occurred since the parameter was itself last reset, to a value of 0, through administrator intervention. The parameter’s default value is 1\. Enterprise Analytics increments this value by 1 for every node that’s auto-failed over, up to the administrator-specified _maximum count_. If nodes are failed over automatically until the _maximum count_ is reached, no further auto-failover is triggered until a parameter-reset is performed.
* `failoverOnDataDiskIssues`. This contains two values, which are:

  * `enabled`, which indicates whether auto-failover can occur when a disk has been unresponsive, and which can be `true` or `false` (the default).
  * `timePeriod`, which indicates the administrator-specified time-period, in seconds, after which auto-failover is triggered, when a disk is unresponsive. The value is an integer between 5 and 3600.
* `maxCount`. The administrator-specified maximum number of nodes that can be concurrently auto-failed over. If nodes are auto-failed over until the value of `maxCount` is reached, no further auto-failover is triggered until a parameter-reset is performed. The default value is 1.
* `canAbortRebalance`. Whether or not auto-failover can be triggered if a _rebalance_ is in progress. This feature is only available in Couchbase Enterprise Edition. The value can be either `true` (the default) or `false`.

Failure to authenticate returns `401 Unauthorized`. An incorrectly specified URL returns `404 Object Not Found`.

## [](#example)Example

The following example returns the auto-failover settings for the cluster. The output is piped to the [jq](https://stedolan.github.io/jq) command, to facilitate readability.

```bourne
curl -X GET http://localhost:8091/settings/autoFailover -u Administrator:password | jq '.'
```

If successful, execution returns the auto-failover settings for the cluster. For example:

```json
{
  "enabled": true,
  "timeout": 72,
  "count": 0,
  "failoverOnDataDiskIssues": {
    "enabled": true,
    "timePeriod": 89
  },
  "maxCount": 2,
  "canAbortRebalance": true
}
```

## [](#see-also)See Also

For information about setting auto-failover parameters with the REST API, see [Enabling and Disabling Auto-Failover](rest-cluster-autofailover-enable.md).

The Couchbase CLI allows auto-failover to be managed by means of the [setting-autofailover](#cli:cbcli/couchbase-cli-setting-autofailover.adoc) command. For information about managing auto-failover with Couchbase Web Console, see [Node Availability](../manage/manage-settings/general-settings.md#node-availability).

A full description of auto-failover is provided in [Automatic Failover](../../../server/current/learn/clusters-and-availability/automatic-failover.md).