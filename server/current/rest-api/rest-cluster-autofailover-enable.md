---
title: Enabling and Disabling Auto-Failover
description: Send a POST message to the <code>/settings/autoFailover</code>
  endpoint to change auto-failover settings.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-cluster-autofailover-enable.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/rest-api/rest-cluster-autofailover-enable.html)

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
  -d 'failoverOnDataDiskIssues[enabled]=[true|false]'
  -d 'failoverOnDataDiskIssues[timePeriod]=<number-of-seconds>'
  -d 'canAbortRebalance=[true|false]'
  -d 'failoverPreserveDurabilityMajority=[true|false]'
  -d 'allowFailoverEphemeralNoReplicas=[true|false]'
  -d 'failoverOnDataDiskNonResponsiveness[enabled]=[true|false]'
  -d 'failoverOnDataDiskNonResponsiveness[timePeriod]=<number-of-seconds>'
```

The parameters are as follows:

* `enabled`: Enables or disables automatic failover. Default setting is `true`. This parameter is required. If you set `enabled` to `true`, you must also supply a value for the `timeout` parameter. Setting `enabled` to `false` automatically sets `failoverOnDataDiskIssues[enabled]` and `failoverOnDataDiskNonResponsiveness` to `false`.  
> [!NOTE]  
> When you set `enabled` to `false`, Couchbase Server ignores any values you supply for additional parameters including `failoverOnDataDiskIssues[enabled]` and `canAbortRebalance`.
* `timeout`: Sets the number of seconds Couchbase Server waits before performing an auto-failover on an unresponsive node. Default setting is 120\. The `timeout` parameter can only be specified when `enabled` is set to `true`. This parameter and its values are ignored if the value for the `enabled` parameter is `false`.  
You can set the value of `timeout` to `1` second. A low setting, such as anything less than 5 seconds, increases the sensitivity of failure detection. This low setting can cause false positives which result in Couchbase Server triggering auto-failovers unnecessarily. It also increases CPU usage.  
If you want to use a low setting, test a representative workload before setting the value of `timeout` to `1` in a production environment. Make sure to measure CPU usage. Monitor the cluster for auto-failovers caused by false positives.

* `maxCount`: Sets the maximum number of nodes Couchbase Server can auto-failover at a time. Once this number of nodes has been auto-failed over, Couchbase Server does not auto-failover more nodes until you reset the count or resolve the auto-failovers with a rebalance to recover or remove the failed-over nodes. The maximum value can be up to the number of configured nodes. The default value is 1\. This parameter is optional, and is only supported by Couchbase Server Enterprise Edition. This parameter and its values are ignored if the value for the `enabled` parameter is `false`.
* `failoverOnDataDiskIssues[enabled]`: Sets whether Couchbase Server performs auto-failovers on nodes where the data disk read or write attempts have resulted in errors continuously throughout at least 60% of the time-period set in `failoverOnDataDiskIssues[timePeriod]`. The default value for `failoverOnDataDiskIssues[enabled]` is `false`. When you set this value to `true`, you must also supply a value for `failoverOnDataDiskIssues[timePeriod]`.
* `failoverOnDataDiskIssues[timePeriod]`: Sets the period of time in seconds that a node’s data disk can return errors before Couchbase Server performs an auto-failover. The valid range for this value is between 5 and 3600 seconds. If you set `failoverOnDataDiskIssues[enabled]` is to `true`, you must also supply a value for this parameter.  
If `failoverOnDataDiskIssues[enabled]` is _not_ specified, but `failoverOnDataDiskIssues[timePeriod]` _is_ specified, the following error message is generated: `The value of "failoverOnDataDiskIssues[enabled]" must be true or false`.  
If you supply a value for this parameter while `failoverOnDataDiskIssues[enabled]` is `false`, Couchbase Server ignores the setting.
* `canAbortRebalance`. Sets whether Couchbase Server can perform an auto-failover while a rebalance is taking place. This parameter is optional, and is only available in Couchbase Enterprise Edition. The value can be either `true` (the default) or `false`. Couchbase Server ignores this setting if you set `enabled` to `false`.

* `failoverPreserveDurabilityMajority`. Sets whether Couchbase Server refuses to auto-failover a node if doing so could result in the loss of durably written data. Can be `true` or `false` (the default). For information, see [Preserving Durable Writes](../learn/data/durability.md#preserving-durable-writes).
* `failoverOnDataDiskNonResponsiveness[enabled]`: Sets whether Couchbase Server performs an auto-failover on a node when the data disk has not completed an operation in the period set by `failoverOnDataDiskNonResponsiveness[timePeriod]`. The default value is `false`. When you set this value to `true`, you must also supply a value for `failoverOnDataDiskNonResponsiveness[timePeriod]`.
* `failoverOnDataDiskNonResponsiveness[timePeriod]`: Sets the period of time in seconds that a node’s data disk has to be unresponsive before Couchbase Server performs an auto-failover. The valid range for this value is between 5 and 3600 seconds. If you set `failoverOnDataDiskNonResponsiveness[enabled]` to `true`, you must also supply a value for this parameter.
* `allowFailoverEphemeralNoReplicas`: Sets whether Couchbase Server can auto-failover a node that contains vBuckets for an unreplicated ephemeral bucket. The default value is `false`, which means Couchbase Server does not perform an auto-failover on a node that contains vBuckets for an unreplicated ephemeral bucket . When you set this value to `true`, Couchbase Server can perform an auto-failover on the node even through it results in the loss of the data from the ephemeral bucket’s vBuckets on the node. This setting is only available in Couchbase Server Enterprise Edition.

## [](#required-permissions)Required Permissions

You must have one of the following roles to make changes to the auto-failover settings:

* [Backup Full Admin](../learn/security/roles.md#backup-full-admin)
* [Cluster Admin](../learn/security/roles.md#cluster-admin)
* [Full Admin](../learn/security/roles.md#full-admin)

## [](#responses)Responses

200 OK

The call succeeded, and the auto-failover settings were changed.

400 Bad Request

The call failed because the request was malformed or lacked required settings.

401 Unauthorized

The call failed because the user did not have the proper permissions to change the auto-failover settings.

## [](#example)Example

The following example enables auto-failover for the cluster, with a `timeout` of 72 seconds, and a `maxCount` of `2`. It also enabled auto-failover on disk issues, and establishes the corresponding time period as `89` seconds.

```console
curl -X POST -u Administrator:password \
http://10.144.231.101:8091/settings/autoFailover \
-d 'enabled=true' \
-d 'timeout=72' \
-d 'maxCount=2' \
-d 'failoverOnDataDiskIssues[enabled]=true' \
-d 'failoverOnDataDiskIssues[timePeriod]=89'
```

This example disables auto-failover for the cluster:

```console
curl -X POST -u Administrator:password \
     http://localhost:8091/settings/autoFailover \
     -d 'enabled=false'
```

## [](#see-also)See Also

* For an overview of auto-failover, see [Automatic Failover](../learn/clusters-and-availability/automatic-failover.md).
* For an overview of durability, see [Durability](../learn/data/durability.md).
* To retrieve the current auto-failover setting using the REST API, see [Retrieving Auto-Failover Settings](rest-cluster-autofailover-settings.md).
* To manage auto-failover using the command line, see [setting-autofailover](../cli/cbcli/couchbase-cli-setting-autofailover.md) command.
* To learn how to manage auto-failover with Couchbase Server Web Console, see [Node Availability](../manage/manage-settings/general-settings.md#node-availability).
* To learn how to change a bucket’s durability settings, see [Creating and Editing Buckets](rest-bucket-create.md).