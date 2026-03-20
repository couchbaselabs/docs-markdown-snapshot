---
title: Delete a Replication
description: Deleting an XDCR <em>replication</em> stops the replication of
  data, and removes the defined replication from Couchbase Server.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/manage/pages/manage-xdcr/delete-xdcr-replication.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:manage:manage-xdcr/delete-xdcr-replication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/manage/manage-xdcr/delete-xdcr-replication.html)

# Delete a Replication

> Deleting an XDCR _replication_ stops the replication of data, and removes the defined replication from Couchbase Server. 

## [](#examples-on-this-page-delete-xdcr-replication)Examples on This Page

The examples in the subsections below show how to delete a replication; using the [UI](#delete-an-xdcr-replication-with-the-ui), the [CLI](#delete-an-xdcr-replication-with-the-cli), and the [REST API](#delete-an-xdcr-replication-with-the-rest-api) respectively. As their starting-point, the examples assume the scenario that concluded the page [Resume a Replication](resume-xdcr-replication.md).

## [](#delete-an-xdcr-replication-with-the-ui)Delete an XDCR Replication with the UI

Proceed as follows:

1. Access Couchbase Web Console. Left-click on the **XDCR** tab, in the right-hand navigation menu.  
![left click on xdcr tab](../_images/manage-xdcr/left-click-on-xdcr-tab.png)  
This displays the **XDCR Replications** screen. The lower part of the main panel features an **Outgoing Replications** panel that currently has the following appearance:  
![xdcr outgoing replications with replication](../_images/manage-xdcr/xdcr-outgoing-replications-with-replication.png)  
This features information on a single, currently defined replication. In the `status` column, this replication is shown to be `Replicating`.
2. To delete the replication, left-click on the row for the replication. When the `Delete` button appears, left-click on it:  
![left click on delete replication tab](../_images/manage-xdcr/left-click-on-delete-replication-tab.png)  
The following confirmation dialog is now displayed:  
![xdcr confirm delete](../_images/manage-xdcr/xdcr-confirm-delete.png)  
Left-click on **Delete Replication**, to confirm. The **Outgoing Replications** panel now reappears, showing no replications:  
![xdcr outgoing replications initial](../_images/manage-xdcr/xdcr-outgoing-replications-initial.png)

The replication has now been deleted.

## [](#delete-an-xdcr-replication-with-the-cli)Delete an XDCR Replication with the CLI

From the starting-point defined above, in [Examples on This Page](#examples-on-this-page-delete-xdcr-replication), use the `xdcr-replicate` command to delete an XDCR replication as follows.

couchbase-cli xdcr-replicate -c 10.142.180.101 \
-u Administrator \
-p password \
--delete \
--xdcr-replicator=570d0ca2db3b1e128e2fafd362a1bfd4/travel-sample/travel-sample

The value specified for the `--xdcr-replicator` flag is that retrieved by means of the `--list` flag, shown in [Pause an XDCR Replication with the CLI](pause-xdcr-replication.md#pause-an-xdcr-replication-with-the-cli). The `--delete` flag signifies that the replication is to be deleted. If successful, the command returns the following:

SUCCESS: XDCR replication deleted

## [](#delete-an-xdcr-replication-with-the-rest-api)Delete an XDCR Replication with the REST API

From the starting-point defined above, in [Examples on This Page](#examples-on-this-page-delete-xdcr), use the REST API to delete an XDCR replication as follows.

curl -X DELETE -u Administrator:password  \
http://10.142.180.101:8091/controller/cancelXDCR/570d0ca2db3b1e128e2fafd362a1bfd4%2Ftravel-sample%2Ftravel-sample

Note the encoded form of the endpoint, which is required. This consists of the `id`, the name of the source bucket, and the name of the target bucket. These were obtained in [Pause an XDCR Replication with the REST API](pause-xdcr-replication.md#pause-an-xdcr-replication-with-the-rest-api).

If the call is successful, no output is displayed. The replication has been deleted.

For more information, see [Deleting a Replication](../../rest-api/rest-xdcr-delete-replication.md).

## [](#next-xdcr-steps-after-delete-replication)Next Steps

Once a replication has been deleted, you may also wish to delete the _reference_ on which it was based. See [Delete a Reference](delete-xdcr-reference.md).