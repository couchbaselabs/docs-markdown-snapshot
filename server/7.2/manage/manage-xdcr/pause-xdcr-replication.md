---
title: Pause a Replication
description: Pausing an XDCR <em>replication</em> temporarily suspends the
  replication of data from the source bucket to the target.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/manage/pages/manage-xdcr/pause-xdcr-replication.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:manage:manage-xdcr/pause-xdcr-replication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/manage/manage-xdcr/pause-xdcr-replication.html)

# Pause a Replication

> Pausing an XDCR _replication_ temporarily suspends the replication of data from the source bucket to the target. 

## [](#examples-on-this-page-pause-xdcr)Examples on This Page

The examples in the subsections below show how to pause the same replication; using the [UI](#pause-an-xdcr-replication-with-the-ui), the [CLI](#pause-an-xdcr-replication-with-the-cli), and the [REST API](#pause-an-xdcr-replication-with-the-rest-api) respectively. As their starting-point, the examples assume the scenario that concluded the page [Create a Replication](create-xdcr-replication.md).

## [](#pause-an-xdcr-replication-with-the-ui)Pause an XDCR Replication with the UI

**Step 1**: Access Couchbase Web Console. Left-click on the **XDCR** tab, in the right-hand navigation menu.

![left click on xdcr tab](../_images/manage-xdcr/left-click-on-xdcr-tab.png) 

This displays the **XDCR Replications** screen. The lower part of the main panel, entitled **Outgoing Replications**, currently has the following appearance:

![xdcr outgoing replications with replication](../_images/manage-xdcr/xdcr-outgoing-replications-with-replication.png) 

This shows the single replication that is in progress. Note that the **status** column displays a status of `replicating`.

**Step 2**: To pause replication, left-click on the row for the replication. The row is redisplayed, as follows:

![xdcr outgoing replications with buttons](../_images/manage-xdcr/xdcr-outgoing-replications-with-buttons.png) 

Three interactive buttons are now displayed. These respectively allow you to **Delete**, **Edit**, or **Pause** the replication. To pause, left-click on the **Pause** button:

![xdcr pause replication button](../_images/manage-xdcr/xdcr-pause-replication-button.png) 

Initially, a notification declares that the replication is in the process of being paused:

![xdcr pausing notification](../_images/manage-xdcr/xdcr-pausing-notification.png)

Subsequently, the notification changes to indicate that the replication has been paused:

![xdcr paused notification](../_images/manage-xdcr/xdcr-paused-notification.png)

The **Pause** button has duly become a **Run** button.

## [](#pause-an-xdcr-replication-with-the-cli)Pause an XDCR Replication with the CLI

From the starting-point defined above, in [Examples on This Page](#examples-on-this-page-pause-xdcr), use the CLI `xdcr-replicate` command to pause an XDCR replication as follows.

First, determine the `stream-id` of the replication that you wish to pause. Use `xdcr-replicate` with the `--list` option, in order to list all ongoing replications from the source cluster:

couchbase-cli xdcr-replicate -c 10.142.180.101 -u Administrator -p password \
--list

This produces the following output:

stream id: 570d0ca2db3b1e128e2fafd362a1bfd4/travel-sample/travel-sample
   status: paused
   source: travel-sample
   target: /remoteClusters/570d0ca2db3b1e128e2fafd362a1bfd4/buckets/travel-sample

The `stream-id` consists of three components, which are, in sequence:

* `570d0ca2db3b1e128e2fafd362a1bfd4`: The `uuid` of the reference.
* `travel-sample`: The name of the source bucket.
* `travel-sample`: The name of the target bucket.

With this information, to pause the replication, use the `xdcr-replicate` command with the `--pause` and `--xdcr-replicator` options, as follows:

couchbase-cli xdcr-replicate -c 10.142.180.101 \
-u Administrator \
-p password \
--pause \
--xdcr-replicator=570d0ca2db3b1e128e2fafd362a1bfd4/travel-sample/travel-sample

If successful, this returns the following:

SUCCESS: XDCR replication paused

The replication is now paused.

## [](#pause-an-xdcr-replication-with-the-rest-api)Pause an XDCR Replication with the REST API

From the starting-point defined above, in [Examples on This Page](#examples-on-this-page-pause-xdcr), use the REST API to pause an XDCR replication as follows.

First, determine the `id` of the replication that you wish to pause. Use the `/pools/default/tasks` endpoint, to produce a list of tasks for the source cluster:

curl -i -X GET -u Administrator:password http://10.142.180.101:8091/pools/default/tasks

Formatted, the output is as follows:

[
  {
    "type": "rebalance",
    "status": "notRunning",
    "statusIsStale": false,
    "masterRequestTimedOut": false
  },
  {
    "cancelURI": "/controller/cancelXDCR/570d0ca2db3b1e128e2fafd362a1bfd4%2Ftravel-sample%2Ftravel-sample",
    "settingsURI": "/settings/replications/570d0ca2db3b1e128e2fafd362a1bfd4%2Ftravel-sample%2Ftravel-sample",
    "status": "running",
    "replicationType": "xmem",
    "continuous": true,
    "filterExpression": "",
    "id": "570d0ca2db3b1e128e2fafd362a1bfd4/travel-sample/travel-sample",
    "pauseRequested": false,
    "source": "travel-sample",
    "target": "/remoteClusters/570d0ca2db3b1e128e2fafd362a1bfd4/buckets/travel-sample",
    "type": "xdcr",
    "recommendedRefreshPeriod": 10,
    "changesLeft": 0,
    "docsChecked": 3111,
    "docsWritten": 0,
    "maxVBReps": null,
    "errors": []
  }
]

The value associated with the `id` key is the `stream-id` for the replication: featuring, in sequence, the `id` (`570d0ca2db3b1e128e2fafd362a1bfd4`) of the reference, the name of the source bucket (`travel-sample`), and the name of the target bucket (`travel-sample`).

Secondly, use the `settings/replications` URI with the `pauseRequested` flag set to `true`, to pause the replication:

curl -X POST -u Administrator:password \
> http://10.142.180.101:8091/settings/replications/570d0ca2db3b1e128e2fafd362a1bfd4%2Ftravel-sample%2Ftravel-sample \
>  -d pauseRequested=true

Note the encoded form of the endpoint, which is required. Formatted, the output is as follows:

{
  "checkpointInterval": 600,
  "compressionType": "Auto",
  "docBatchSizeKb": 2048,
  "failureRestartInterval": 10,
  "filterExpression": "",
  "logLevel": "Info",
  "networkUsageLimit": 0,
  "optimisticReplicationThreshold": 256,
  "pauseRequested": true,
  "sourceNozzlePerNode": 2,
  "statsInterval": 1000,
  "targetNozzlePerNode": 2,
  "type": "xmem",
  "workerBatchSize": 500
}

The replication is now paused.

For more information, see [Pausing and Resuming a Replication](../../rest-api/rest-xdcr-pause-resume.md).

## [](#next-xdcr-steps-after-pause-replication)Next Steps

Once a replication has been paused, you can opt to _resume_ it. See [Resume a Replication](resume-xdcr-replication.md).