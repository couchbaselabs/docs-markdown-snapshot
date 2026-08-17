---
title: Stream-based Views
description: "With DCP, data does not need to be persisted to disk before
  retrieving it with a view query. DCP offers the following benefits for views:"
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/learn/pages/views/views-streaming.adoc
  xref: xref:7.6@server:learn:views/views-streaming.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/learn/views/views-streaming.html)

# Stream-based Views

With DCP, data does not need to be persisted to disk before retrieving it with a view query. DCP offers the following benefits for views:

* Views are updated with key-value data sooner.
* Latency for view updates is reduced.
* Views are more closely synchronized with the data.

When submitting a view query, a parameter can be included that specifies data freshness requirements. The name of the parameter is `stale` and it takes the following values:

* `ok`—The server returns the current entries from the index file.
* `update_after`—The server returns the current entries from the index, and then initiates an index update.
* `false`—The server waits for the indexer to finish the changes that correspond to the current key-value document set and then returns the latest entries from the view index.

Every 5 seconds the automatic update process checks whether 5000 changes have occurred. If a minimum of 5000 changes occurred, an index update is triggered. Otherwise, no update is triggered. When triggered, the indexer requests from DCP all changes since it was last run. The default number of changes to check for is 5000, but that number can be configured by setting the `updateMinChanges` option. The update interval can also be configured by setting the `updateInterval` option.

The `stale=false` view query argument has been enhanced. When an application sends a query that has the `stale` parameter set to false, the application receives all recent changes to the documents, including changes that haven't yet been persisted to disk. It considers all document changes that have been received at the time the query was received. This means that using the durability requirements or observe feature to block for persistence in application code before issuing the `stale=false` query is no longer needed. It is recommended that you remove all such application level checks after upgrading.

> [!TIP]
> For better scalability and throughput, we recommend that you set the value of the `stale` parameter to `ok`. With the stream-based views, data returned when `stale` is set to `ok` is closer to the key-value data, even though it might not include all of it.