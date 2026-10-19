---
title: Enabling and Disabling Auto-Failover
description: Send a POST message to the <code>/settings/autoFailover</code>
  endpoint to change auto-failover settings.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-cluster-autofailover-enable.adoc
  xref: xref:enterprise-analytics:reference:rest-cluster-autofailover-enable.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-cluster-autofailover-enable.html)

# Enabling and Disabling Auto-Failover

> Send a POST message to the `/settings/autoFailover` endpoint to change auto-failover settings. 

## [](#http-method-and-uri)HTTP Method and URI

POST /settings/autoFailover

## [](#description)Description

You can use the `POST /settings/autoFailover` HTTP method and URI to enable, turn off, and change auto-failover settings.

Auto-failover settings are global, applying to all nodes in the cluster.

## [](#syntax)Syntax

```bourne
curl -X POST http://<ip-address-or-hostname>:8091/settings/autoFailover
  -u <username>:<password>
  -d 'enabled=[true|false]'
  -d 'timeout=<number-of-seconds>'
  -d 'maxCount=<number-of-nodes>'
  -d 'canAbortRebalance=[true|false]'
```

The parameters are as follows:

* `enabled`: Enables or disables automatic failover. Default setting is `true`. This parameter is required. If you set `enabled` to `true`, you must also supply a value for the `timeout` parameter.  
> [!NOTE]  
> When you set `enabled` to `false`, Operational Insights ignores any values you supply for additional parameters including `maxCount` and `canAbortRebalance`.
* `timeout`: Sets the number of seconds Operational Insights waits before performing an auto-failover on an unresponsive node. Default setting is 120\. The `timeout` parameter can only be specified when `enabled` is set to `true`. This parameter and its values are ignored if the value for the `enabled` parameter is `false`.  
You can set the value of `timeout` to `1` second. A low setting, such as anything less than 5 seconds, increases the sensitivity of failure detection. This low setting can cause false positives which result in Operational Insights triggering auto-failovers unnecessarily. It also increases CPU usage.  
If you want to use a low setting, test a representative workload before setting the value of `timeout` to `1` in a production environment. Make sure to measure CPU usage. Monitor the cluster for auto-failovers caused by false positives.

* `maxCount`: Sets the maximum number of nodes Operational Insights can auto-failover at a time. Once this number of nodes has been auto-failed over, Operational Insights does not auto-failover more nodes until you reset the count or resolve the auto-failovers with a rebalance to recover or remove the failed-over nodes. The maximum value can be up to the number of configured nodes. The default value is 1\. This parameter is optional, and is only supported by Operational Insights. This parameter and its values are ignored if the value for the `enabled` parameter is `false`.
* `canAbortRebalance`. Sets whether Operational Insights can perform an auto-failover while a rebalance is taking place. This parameter is optional, and is only available in Operational Insights. The value can be either `true` (the default) or `false`. Operational Insights ignores this setting if you set `enabled` to `false`.

## [](#required-permissions)Required Permissions

You must have one of the following roles to make changes to the auto-failover settings:

* Cluster Admin
* Full Admin

For information about roles, see [Role Based Access Control (RBAC)](../manage/manage-security/rbac-overview.md).

## [](#responses)Responses

200 OK

The call succeeded, and the auto-failover settings were changed.

400 Bad Request

The call failed because the request was malformed or lacked required settings.

401 Unauthorized

The call failed because the user did not have the proper permissions to change the auto-failover settings.

## [](#example)Example

The following example enables auto-failover for the cluster, with a `timeout` of 72 seconds, and a `maxCount` of `2`.

```console
curl -X POST -u Administrator:password \
http://10.144.231.101:8091/settings/autoFailover \
-d 'enabled=true' \
-d 'timeout=72' \
-d 'maxCount=2'
```

This example disables auto-failover for the cluster:

```console
curl -X POST -u Administrator:password \
     http://localhost:8091/settings/autoFailover \
     -d 'enabled=false'
```

## [](#see-also)See Also

* For an overview of failover, see [Failover](../manage/manage-nodes/fail-nodes-over.md).
* To retrieve the current auto-failover setting using the REST API, see [Retrieving Auto-Failover Settings](rest-cluster-autofailover-settings.md).
* To manage auto-failover using the command line, see [setting-autofailover](../cli/couchbase-cli-setting-autofailover.md) command.
* To learn how to manage auto-failover with Operational Insights Web Console, see [Node Availability](../manage/manage-settings/general-settings.md#node-availability).