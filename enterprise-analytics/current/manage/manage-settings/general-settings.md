---
title: General Settings
description: <em>General</em> settings allow configuration of <em>cluster
  name</em>, <em>memory quotas</em>, <em>storage modes</em>, and <em>node
  availability</em> for the cluster.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/manage/pages/manage-settings/general-settings.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/current/manage/manage-settings/general-settings.html)

# General Settings

> _General_ settings allow configuration of _cluster name_, _memory quotas_, _storage modes_, and _node availability_ for the cluster. 

## [](#configuring-general-settings-examples-on-this-page)Examples on This Page

Full and Cluster Administrators can configure general settings by means of [Enterprise Analytics Web Console](#configure-general-settings-with-the-ui), the [CLI](#configure-general-settings-with-the-cli), or the [REST API](#configure-general-settings-with-the-rest-api).

## [](#configure-general-settings-with-the-ui)Configure General Settings with the UI

The **General** screen provides access to various cluster configuration options organized into several panels. Each panel contains specific settings that can be modified to customize your Enterprise Analytics deployment.

The panels and their UI elements are described in the following sections.

### [](#cluster-name)Cluster Name

The **Cluster Name** is the name that was given during initial setup. This name can be changed at any time using the interactive text field in this section.

### [](#current-version)Current Version

This panel displays the current version of Enterprise Analytics and provides an option to manage update notifications.

The **Current Version** panel shows the installed version number and includes a checkbox labeled **Share usage information with Couchbase and get software update notifications**. This checkbox is checked by default, meaning that Enterprise Analytics Web Console will display adjacent notifications whenever a new version of Enterprise Analytics is available. If the checkbox is unchecked, notifications are not provided.

Additionally, if the checkbox is checked, Enterprise Analytics Web Console communicates with Enterprise Analytics to ascertain the following information, which is then transmitted to Couchbase:

* The server-version of the current installation.
* Information about data-size and performance.
* The cluster-configuration, including which services are deployed.

> [!NOTE]
> Data is transmitted to Couchbase from the browser accessing the Enterprise Analytics Web Console, not from the cluster itself. The update-notification process works anonymously: data cannot be tracked. No identifiable information is transmitted.

### [](#node-availability)Node Availability

The options in the **Node Availability** panel control whether and how **Automatic Failover** is applied. For detailed information about policy and constraints, see [Automatic Failover](../../../../server/current/learn/clusters-and-availability/automatic-failover.md).

The **Node Availability** panel provides several checkboxes and input fields to configure auto-failover behavior.

The following checkboxes are provided:

* **Auto-failover after _x_ seconds for up to _y_ node**: After the timeout period set here as _x_ seconds has elapsed, an unresponsive or malfunctioning node is failed over, provided that the limit on actionable events set here as _y_ (with the default value of 1) has not yet been reached. Data replicas are promoted to active on other nodes, as appropriate. This feature can only be used when three or more nodes are present in the cluster. The number of seconds to elapse is configurable: the default is 120; the minimum permitted is 5; the maximum 3600\. This option is selected by default.
* **Auto-failover for sustained data disk read/write failures after _z_ seconds**: After the timeout period set here as _z_ seconds has elapsed, a node is failed over if it has experienced sustained data disk read/write failures. The timeout period is configurable: the default length is 120 seconds; the minimum permitted is 5; the maximum 3600\. This checkbox can only be checked if **Auto-failover after _x_ seconds for up to _y_ node** has also been checked. This option is unchecked by default.
* **Preserve durable writes**: If this checkbox is checked, a node is _not_ failed over if this might result in the loss of durably written data. The default is that the checkbox is unchecked. For information, see server:learn:data/durability.adoc#preserving-durable-writes\[Preserving Durable Writes\].

The **Node Availability** panel also contains a **For Ephemeral Buckets** option. When opened, this provides an **Enable auto-reprovisioning** checkbox, with a configurable number of nodes. Checking this ensures that if a node containing _active_ Ephemeral buckets becomes unavailable, its replicas on the specified number of other nodes are promoted to active status as appropriate, to avoid data-loss. Note, however, that this may leave the cluster in an unbalanced state, requiring a rebalance.

#### [](#auto-failover-and-durability)Auto-Failover and Durability

Enterprise Analytics provides _durability_, which ensures the greatest likelihood of data-writes surviving unexpected anomalies, such as node-outages. The auto-failover maximum should be established to support guarantees of durability. See [Durability](../../../../server/current/learn/data/durability.md), for information.

### [](#rebalance-settings)Rebalance Settings

_Rebalance_ redistributes data, indexes, event processing, and query processing among available nodes. For an overview, see [Rebalance](../../../../server/current/learn/clusters-and-availability/rebalance.md).

The **Rebalance Settings** panel provides options to configure rebalance behavior.

The **Retry rebalance** option allows rebalance to be _retried_, in cases where it has failed. Check the checkbox, to enable. The specifiable, _maximum number of retries_ must be in the range of 1 to 3, inclusive. The specifiable, _maximum number of seconds_ must be in the range of 5 to 3600, inclusive.

Note that this option should _not_ be enabled if the cluster is managed by _Couchbase Autonomous Operator_, or if custom scripts are already being used to trigger rebalance.

Note also that no administrative tasks should be attempted when rebalance-retries are pending.

However, pending rebalance-retries can be cancelled: see [Automated Rebalance-Failure Handling](../manage-nodes/add-node-and-rebalance.md#automated-rebalance-failure-handling), for information.

### [](#saving-settings)Saving Settings

To save any changes made in the panels, click on the **Save** button, located at the lower left of the screen.

Alternatively, to discard recently entered values and revert to the previous settings, click on **Cancel/Reset**.

## [](#configure-general-settings-with-the-cli)Configure General Settings with the CLI

To configure _name and memory_, _index storage_, and _auto-failover_ via CLI, use the appropriate CLI command; as described below. Note that no CLI support is provided for configuring _query settings_. As an alternative, see [Configure General Settings with the REST API](#configure-general-settings-with-the-rest-api), below. Additionally, For information about URL access lists via the SQL++ `CURL()` function, see [CURL Function](../../../../server/current/n1ql/n1ql-language-reference/curl.md).

### [](#name-and-memory-settings-via-cli)Name and Memory Settings via CLI

Name and memory settings are established with the [setting-cluster](../../cli/couchbase-cli-setting-cluster.md) command.

```shell
/opt/enterprise-analytics/bin/couchbase-cli
--cluster 10.143.192.101:8091 \
--username Administrator \
--password password \
--cluster-ramsize 256 \
--cluster-name 10.143.192.101 \
```

This establishes the cluster-name as `10.143.192.101`, the memory allocation for Data and Index Services each as 256 megabytes, and the memory allocation for each other service as zero.

If successful, the call produces the following output:

```shell
SUCCESS: Cluster settings modified
```

Note that settings for an individual server may be retrieved with the [server-info](../../cli/couchbase-cli-server-info.md) command, the output for which can be filtered, as appropriate, by `grep`:

```shell
/opt/enterprise-analytics/bin/couchbase-cli
-c 10.143.192.101 -u Administrator -p password | grep data
```

This returns the setting for data in the cluster:

```shell
"path": "/data",
"dataStatus": "unknown",
"dataStatus": "encrypted",
"dataStatus": "unencrypted",
"/opt/enterprise-analytics/var/lib/couchbase/data"
"path": "/opt/enterprise-analytics/var/lib/couchbase/data"
```

```shell
If successful, the call produces the following output:

[source,shell]
```

SUCCESS: Indexer settings modified

[#software-update-settings-via-cli]
=== Software-Update Settings via CLI

You can enable and disable software update notifications in Enterprise Analytics Enterprise Edition using the xref:cli:couchbase-cli-setting-notification.adoc[setting-notification] command.

[source,shell]

/opt/enterprise-analytics/bin/couchbase-cli -c 10.143.192.101 -u Administrator -p password \\ --enable-notifications 1

Setting value of 1 for `--enable-notifications` enables update-notifications. A value of 0 disables notifications.
If successful, the command produces the following output:

[source,shell]

SUCCESS: Notification settings updated

NOTE: You cannot disable software update notifications in Enterprise Analytics Community Edition.

[#auto-failover-settings-via-cli]
=== Auto-Failover Settings via CLI

Auto-failover can be configured with the xref:cli:couchbase-cli-setting-autofailover.adoc[setting-autofailover] command.

[source,shell]

/opt/enterprise-analytics/bin/couchbase-cli -c 10.143.192.101:8091 \\ -u Administrator \\ -p password \\ --enable-auto-failover 1 \\ --auto-failover-timeout 120 \\ --max-failovers 2

This enables auto-failover, with a timeout of 120 seconds, and an event-maximum of 2.

If successful, the command returns the following output:

[source,shell]

SUCCESS: Auto-failover settings modified

For a detailed description of auto-failover settings, policy, and constraints, see xref:server:learn:clusters-and-availability/automatic-failover.adoc[Automatic Failover].


[#rebalance-settings-via-cli]
=== Rebalance Settings via CLI

To obtain the cluster's current rebalance settings by means of the CLI, use the xref:cli:couchbase-cli-setting-rebalance.adoc[setting-rebalance] command, with the `--get` option:

[source,shell]

/opt/enterprise-analytics/bin/couchbase-cli -c 10.143.192.101 \\ -u Administrator \\ -p password \\ --get

If successful, the command returns the current rebalance settings:

[source,shell]

Automatic rebalance retry disabled Retry wait time: 300 Maximum number of retries: 2

To modify the current rebalance settings, use the `--set` option; and specify appropriate values for the `--max-attempts` and `--wait-for` flags:

[source,shell]

/opt/enterprise-analytics/bin/couchbase-cli -c 10.143.192.101 \\ -u Administrator \\ -p password \\ --set \\ --max-attempts 3 \\ --wait-for 200

If successful, the command displays the following success message:

[source,shell]

SUCCESS: Automatic rebalance retry settings updated

For more information, see the reference page xref:reference:rest-configure-rebalance-retry.adoc[Configure Rebalance Retries].


[#configure-general-settings-with-the-rest-api]
== Configure General Settings with the REST API

Multiple REST API methods are provided to support configuration of general settings.
These are described below.

[#name-and-memory-settings-via-rest]
=== Name and Memory Settings via REST

To establish name and memory settings, use the `/pools/default` method.

[source,shell]

curl -v -X POST -u Administrator:password \\ <http://10.143.192.101:8091/pools/default> \\ -d clusterName=10.143.192.101 \\ -d cbasMemoryQuota=1024 \\

This establishes the cluster's IP address as its name, and assigns memory-quotas for each node.

Note that when used with GET, `/pools/default` returns configuration-settings.
The output can be filtered, by means of a tool such as https://stedolan.github.io/jq/[jq]:

[source,shell]

curl -s -u Administrator:password \\ <http://10.143.192.101:8091/pools/default> | jq '.cbasMemoryQuota'

If successful, this returns the value of the key `cbasMemoryQuota`:

[source,shell]

## [](#256)256

### [](#software-update-settings-via-rest)Update Notification and Statistics Settings via REST

In Enterprise Analytics Enterprise Edition, you can use the `/setting/stats` endpoint to turn off notifications about new server versions and reporting of cluster statistics back to Couchbase:

```shell
curl -v -X POST -u Administrator:password \
http://10.143.192.101:8091/settings/stats \
-d sendStats=false
```

You cannot change this setting in Enterprise Analytics Community Edition. The `sendStats` setting is always `true` in this edition.

See the [update-notifications](../../cli/couchbase-cli-cluster-init.md#:~:text=software%20update%20notifications) option in the [cluster-init](../../cli/couchbase-cli-cluster-init.md) command line interface reference for details of what `sendStats` shares.

### [](#node-availability-settings-via-rest)Node Availability Settings via REST

To establish node availability settings, use the `/settings/autoFailover` method.

```shell
curl -v -X POST -u Administrator:password \
http://10.143.192.101:8091/settings/autoFailover \
-d enabled=true \
-d timeout=120 \
-d failoverOnDataDiskIssues[enabled]=false \
-d failoverOnDataDiskIssues[timePeriod]=120 \
-d maxCount=2 \
-d failoverPreserveDurabilityMajority=true
```

This enables auto-failover, with a timeout of 120 seconds, and a maximum failover-count of 2\. Auto-failover is enabled in the event of suboptimal disk responsiveness, with a time-period of 120 seconds specified. Auto-failover is prohibited in cases where this might result in the loss of durably written data.

For more information about these options, see the descriptions provided above, for the [UI](#node-availability).

Additionally, the `/settings/autoReprovision` method can be used; to specify that if a node containing _active_ Ephemeral buckets becomes unavailable, its replicas on the specified number of other nodes are promoted to active status as appropriate, to avoid data-loss.

```shell
curl -v -X POST -u Administrator:password \
http://10.143.192.101:8091/settings/autoReprovision \
-d enabled=true \
-d maxNodes=1
```

This enables auto-reprovisioning, specifying 1 as the maximum number of nodes.

### [](#rebalance-settings-via-rest)Rebalance Settings via REST

By means of the REST API, both _rebalance retries_ and _maximum concurrent moves per node_ can be configured.

#### [](#rebalance-retries-via-rest)Rebalance Retries via REST

To obtain the cluster’s current settings for _rebalance retries_ by means of the REST API, use the `GET /settings/retryRebalance` HTTP method and URI, as follows:

```shell
curl -X GET -u Administrator:password \
http://10.143.192.101:8091/settings/retryRebalance
```

If successful, the command returns the following object:

```json
{"enabled":true,"afterTimePeriod":200,"maxAttempts":3}
```

This output shows that rebalance retry is enabled, with `200` seconds required to elapse before a retry is attempted, and a maximum of `3` retries possible.

To change the rebalance settings, use the `POST` method with the same URI, specifying appropriate values:

```shell
curl -X POST -u Administrator:password \
http://10.143.192.101:8091/settings/retryRebalance \
-d enabled=false \
-d afterTimePeriod=100 \
-d maxAttempts=2
```

If successful, the command returns the following object:

```json
{"enabled":false,"afterTimePeriod":100,"maxAttempts":2}
```

This verifies that rebalance retry is disabled, the required period between retries changed to `100` seconds, and the maximum number of retries changed to `2`.

For more information about getting and setting the rebalance retry status, see [Configure Rebalance Retries](../../reference/rest-configure-rebalance-retry.md), [Get Rebalance-Retry Status](../../reference/rest-get-rebalance-retry.md), and [Cancel Rebalance Retries](../../reference/rest-cancel-rebalance-retry.md).