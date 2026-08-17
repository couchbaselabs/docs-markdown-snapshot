---
title: Resume a Replication
description: After an XDCR replication has been paused, resuming it restarts the
  replication of data from the source bucket to the target.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/manage/pages/manage-xdcr/resume-xdcr-replication.adoc
  xref: xref:7.2@server:manage:manage-xdcr/resume-xdcr-replication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/manage/manage-xdcr/resume-xdcr-replication.html)

# Resume a Replication

> After an XDCR replication has been paused, resuming it restarts the replication of data from the source bucket to the target. 

## [](#examples-on-this-page-resume-xdcr)Examples on This Page

The examples in the subsections below show how to resume a replication; using the [UI](#resume-an-xdcr-replication-with-the-ui), the [CLI](#resume-an-xdcr-replication-with-the-cli), and the [REST API](#resume-an-xdcr-replication-with-the-rest-api) respectively. As their starting-point, the examples assume the scenario that concluded the page [Pause a Replication](pause-xdcr-replication.md).

## [](#resume-an-xdcr-replication-with-the-ui)Resume an XDCR Replication with the UI

Proceed as follows:

1. Access Couchbase Web Console. Left-click on the **XDCR** tab, in the right-hand navigation menu.  
![left click on xdcr tab](../_images/manage-xdcr/left-click-on-xdcr-tab.png)  
This displays the **XDCR Replications** screen. The lower part of the main panel features an **Outgoing Replications** panel that currently has the following appearance:  
![xdcr outgoing replications panel replication paused](../_images/manage-xdcr/xdcr-outgoing-replications-panel-replication-paused.png)  
This features information on a single, currently defined replication. In the `status` column, this replication is shown to be `paused`, and a **Run** button is displayed.
2. To resume the replication, left-click on the **Run** button:  
![xdcr left click on resume replication button before](../_images/manage-xdcr/xdcr-left-click-on-resume-replication-button-before.png)  
The word `paused` changes to `replicating`, and the **Run** button is again displayed as a **Pause** button.  
![xdcr resume replication button after](../_images/manage-xdcr/xdcr-resume-replication-button-after.png)

Replication has now been resumed.

## [](#resume-an-xdcr-replication-with-the-cli)Resume an XDCR Replication with the CLI

From the starting-point defined above, in [Examples on This Page](#examples-on-this-page-resume-xdcr), use the CLI `xdcr-replicate` command with the `--resume` flag, to pause an XDCR replication as follows:

couchbase-cli xdcr-replicate -c 10.142.180.101 \
-u Administrator \
-p password \
--resume \
--xdcr-replicator=570d0ca2db3b1e128e2fafd362a1bfd4/travel-sample/travel-sample

The value specified for the `--xdcr-replicator` flag is that retrieved by means of the `--list` flag, shown in [Pause an XDCR Replication with the CLI](pause-xdcr-replication.md#pause-an-xdcr-replication-with-the-cli).

If successful, the command returns the following:

SUCCESS: XDCR replication resume

Replication has now been resumed.

## [](#resume-an-xdcr-replication-with-the-rest-api)Resume an XDCR Replication with the REST API

From the starting-point defined above, in [Examples on This Page](#examples-on-this-page-resume-xdcr), use the REST API to resume an XDCR replication as follows.

curl -X POST -u Administrator:password \
http://10.142.180.101:8091/settings/replications/570d0ca2db3b1e128e2fafd362a1bfd4%2Ftravel-sample%2Ftravel-sample \
-d pauseRequested=false

The endpoint used here features, in sequence, the `id` of the reference, the name of the source bucket, and the name of the remote bucket. These were obtained in [Pause an XDCR Replication with the REST API](pause-xdcr-replication.md#pause-an-xdcr-replication-with-the-rest-api ). The value of the `pauseRequested` flag is here set to `false`.

The output is as follows:

{
  "checkpointInterval": 600,
  "compressionType": "Auto",
  "docBatchSizeKb": 2048,
  "failureRestartInterval": 10,
  "filterExpression": "",
  "logLevel": "Info",
  "networkUsageLimit": 0,
  "optimisticReplicationThreshold": 256,
  "pauseRequested": false,
  "sourceNozzlePerNode": 2,
  "statsInterval": 1000,
  "targetNozzlePerNode": 2,
  "type": "xmem",
  "workerBatchSize": 500
}

Replication has now been restarted.

For more information, see see [Pausing and Resuming a Replication](../../rest-api/rest-xdcr-pause-resume.md).

## [](#next-xdcr-steps-after-resume-replication)Next Steps

Once a replication is no longer needed, you can _delete_ it. See [Delete a Replication](delete-xdcr-replication.md).