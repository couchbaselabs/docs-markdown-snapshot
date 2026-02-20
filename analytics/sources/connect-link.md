---
title: Connect or Disconnect a Remote Link
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/connect-link.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:analytics:sources:connect-link.adoc[]
---

[View original HTML](/analytics/sources/connect-link.html)

# Connect or Disconnect a Remote Link

> This topic describes how you start and stop data event streaming from a remote data source through a link. 

You incur charges when you connect a remote link.

## [](#connect-link)Connect a Remote Link

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name. The workbench opens.
3. Use the explorer to locate the link you want to connect. Each link’s status displays next to its name.
4. Move your cursor over the name of the link and then choose **⋮ (More)** **Connect**.

![Selecting Connect from the More menu](_images/connect_remote_link.png) 

Capella Analytics begins setting up the required infrastructure for the connection. Automatic data ingestion from the connected data source to all linked collections begins as soon as set up is complete. If more than one collection uses the link, data ingestion begins for all of them. The link’s status changes to connected.

After you connect the link and your initial data ingest is complete, you can run `ANALYZE COLLECTION` on each collection associated with the link. The `ANALYZE` statement samples data in the collection so that cost-based optimization (CBO) can be applied instead of rule-based optimization. As data in the collections changes, you can run `ANALYZE COLLECTION` periodically to refresh the samples. See [Cost-Based Optimizer for Capella Analytics Services](../sqlpp/5b%5Fcbo.md).

You can also use an SQL++ for Capella Analytics statement to connect a remote link. See [CONNECT Statements](../sqlpp/5%5Fddl%5Fconnect.md).

## [](#get-status)Get Data Event Stream Status

To verify that a remote collection is receiving data through a connected link, you can compare the count of documents in the collection at different points in time.

1. In the workbench, use the **Query Context** lists to specify the database and scope for the collection.  
![The Query Context lists with 'travel-sample' and 'inventory' selected](../sqlpp/_images/workbench-context-set.png)
2. Get the current count of documents in the Capella Analytics collection:  
SELECT count(*) FROM airline;
3. Repeat the previous step to see the number of documents received into this collection increase.

## [](#stop-stream)Stop Data Event Streaming

You can stop a data event stream from continuously updating the collection or collections associated with a link, and then restart it at a later time.

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click a cluster name. The workbench opens.
3. Use the explorer to locate the link you want to disconnect. Each link’s status appears next to its name.
4. Move your cursor over the name of the link and then choose **⋮ (More)** **Disconnect**.

You can also use an SQL++ for Capella Analytics statement to disconnect a remote link. See [DISCONNECT Statements](../sqlpp/5%5Fddl%5Fdisconnect.md).

After you disconnect a link, you can restart data event streaming by connecting again.

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Access and Organize Data in Capella Analytics Services](database-objects.md)
* [Stream Data from Remote Sources](manage-remote.md)
* [SQL++ for Capella Analytics](../sqlpp/1%5Fintro.md)