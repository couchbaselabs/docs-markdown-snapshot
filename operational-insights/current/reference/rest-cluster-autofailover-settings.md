---
title: Retrieving Auto-Failover Settings
description: Use the  <code>/settings/autoFailover</code> endpoint to get the
  current auto-failover settings.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-cluster-autofailover-settings.adoc
  xref: xref:enterprise-analytics:reference:rest-cluster-autofailover-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-cluster-autofailover-settings.html)

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

* Full Admin
* Cluster Admin
* Read-Only Admin
* Read-Only Security Admin
* Security Admin
* External User Admin
* Local User Admin

For information about roles, see [Role Based Access Control (RBAC)](../manage/manage-security/rbac-overview.md).

## [](#responses)Responses

200 OK

The call was successful. Also returns an object containing the current state of the auto-failover settings. See [Example](#example) for an example of the response.

401 Unauthorized

The user credentials supplied with the call do not have the correct permissions to read the auto-failover settings.

404 Not Found

The URL was incorrect.

## [](#example)Example

The following example returns the auto-failover settings for the cluster. It pipes the output through the [jq](https://jqlang.org/) command to improve readability.

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
  "maxCount": 1,
  "canAbortRebalance": true
}
```

The response also contains keys that do not apply to Operational Insights; they are omitted from the example above.

The keys in the object returned in the example are:

* `enabled`Whether automatic failover is on (a value of `true`) or off (`false`).
* `timeout`The number of seconds Operational Insights waits after a node has become unavailable before it performs an automatic failover. This value can be between 5 and 3600\. The default value is 120.
* `count`. The number of nodes that Operational Insights has auto-failed over. Operational Insights resets this value to zero either when the cluster rebalances to remove or rejoin the failed nodes, or when an administrator manually resets the count (see [Resetting Auto-Failover](rest-cluster-autofailover-reset.md)). The parameter's default value is 0\. If number of failed-over nodes reaches the maximum count set by `maxCount`, Operational Insights refuses to auto-failover more nodes until you reset the count or resolve the auto-failovers with a recovery and rebalance.
* `maxCount`. The maximum number of nodes that can be auto-failed over at the same time. When the count of auto-failed over nodes reaches this value, Operational Insights does not trigger additional auto-failovers. You must either resolve the auto-failovers through rebalancing the cluster to remove or recover the failed-over nodes or reset the count of failed over nodes. The default value is 1.
* `canAbortRebalance`Whether or not Operational Insights can auto-failover a node while a rebalance is taking place. This feature is available in Operational Insights. The value can be either `true` (the default) or `false`.

## [](#see-also)See Also

* For information about setting auto-failover parameters with the REST API, see [Enabling and Disabling Auto-Failover](rest-cluster-autofailover-enable.md).
* The Operational Insights command line tool [setting-autofailover](../cli/couchbase-cli-setting-autofailover.md) lets you manage auto-failover.
* For information about managing auto-failover with Operational Insights Web Console, see [Node Availability](../manage/manage-settings/general-settings.md#node-availability).
* For information about failover, see [Failover](../manage/manage-nodes/fail-nodes-over.md).