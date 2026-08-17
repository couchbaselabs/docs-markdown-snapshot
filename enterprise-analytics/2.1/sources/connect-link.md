---
title: Connect or Disconnect a Remote Link
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sources/pages/connect-link.adoc
  xref: xref:2.1@enterprise-analytics:sources:connect-link.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/sources/connect-link.html)

# Connect or Disconnect a Remote Link

> This topic describes how you start and stop data event streaming from a remote data source through a link. 

You incur charges when you connect a remote link.

## [](#connect-link)Connect a Remote Link

1. In the UI, select the **Workbench** tab.
2. In the explorer, locate the link you want to connect.
3. Click **Link**.

> [!NOTE]
> You can view the link's status when you hover on the link icon.

Enterprise Analytics begins setting up the required infrastructure for the connection. Automatic data ingestion from the connected data source to all linked collections begins as soon as set up is complete. If more than 1 collection uses the link, data ingestion begins for all of them. The link's status changes to connected.

After you connect the link and your initial data import is complete, you can run `ANALYZE COLLECTION` on each collection associated with the link. The `ANALYZE` statement samples data in the collection so that you can apply the cost-based optimization (CBO) instead of rule-based optimization. As data in the collections changes, you can run `ANALYZE COLLECTION` periodically to refresh the samples. For more information, see [Cost-Based Optimizer](../sqlpp/5b%5Fcbo.md). You can also use SQL++ for Enterprise Analytics statement to connect a remote link. See [CONNECT Statements](../sqlpp/5%5Fddl%5Fconnect.md).

You can also use an SQL++ for Enterprise Analytics statement to connect a remote link. See [CONNECT Statements](../sqlpp/5%5Fddl%5Fconnect.md).

## [](#get-status)Get Data Event Stream Status

To verify that a remote collection is receiving data through a connected link, you can compare the count of documents in the collection at different points in time.

1. In the workbench, use the **Query Context** lists to specify the database and scope for the collection.
2. Get the current count of documents in the Enterprise Analytics collection:  
SELECT count(\*) FROM airline;
3. Repeat the previous step to see the number of documents received into this collection increase.

During data ingestion, an indicator below each collection shows the percentage of mutations that remain to be synchronized to that collection. If the indicator is not displayed, the collection is synchronized.

## [](#stop-stream)Stop Data Event Streaming

You can pause a data event stream from continuously updating the collection associated with a link, and then restart it at a later time. Pause data event streaming to stop updates to linked collections. You can restart streaming later by reconnecting the link.

1. In UI, select the **Workbench** tab.
2. In the explorer, locate the link you want to disconnect.
3. Click **Link**.

> [!NOTE]
> You can view the link's status when you hover on the link icon.

You can also use an SQL++ for Enterprise Analytics statement to disconnect a remote link. See [DISCONNECT Statements](../sqlpp/5%5Fddl%5Fdisconnect.md).

After you disconnect a link, you can resume data event streaming by connecting again.

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Access and Organize Data in Enterprise Analytics](database-objects.md)
* [Stream Data from Remote Sources](manage-remote.md)
* [SQL++ for Enterprise Analytics](../sqlpp/1%5Fintro.md)