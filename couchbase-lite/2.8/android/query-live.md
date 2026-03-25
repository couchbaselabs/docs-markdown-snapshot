---
title: Live Query&#8201;&#8212;&#8201;Working with Queries
description: Couchbase Lite database data querying concepts -- live queries
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/android/pages/query-live.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:android:query-live.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/android/query-live.html)

# Live Query&#8201;&#8212;&#8201;Working with Queries

> Description — _Couchbase Lite database data querying concepts — live queries_  
> Related Content — [Predictive Query](#couchbase-lite:android:query-predictive.adoc) | [Indexing](../../current/android/indexing.md) | [Queries](../../current/android/querybuilder.md)

## [](#activating-a-live-query)Activating a Live Query

A live query is a query that, once activated, remains active and monitors the database for changes; refreshing the result set whenever a change occurs. As such, it is a great way to build reactive user interfaces — especially table/list views — that keep themselves up to date.

**So, a simple use case may be:** A replicator running and pulling new data from a server, whilst a live-query-driven UI automatically updates to show the data without the user having to manually refresh. This helps your app feel quick and responsive.

Example 1\. Starting a LIve Query

```Java
Query query = QueryBuilder
    .select(SelectResult.all())
    .from(DataSource.database(database));

// Adds a query change listener.
// Changes will be posted on the main queue.
ListenerToken token = query.addChangeListener(change -> { (1)
    for (Result result : change.getResults()) {
        Log.d(TAG, "results: " + result.getKeys());
        /* Update UI */
    }
});

// Start live query.
query.execute(); (2)
```

| **1** | Build the query statements using the QuerybUilder                                                                                                                                                                                   |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Activate the _live_ query by attaching a listener.Save the token in order to detach the listener and stop the query later — se [Example 2](#ex-qry-stop)                                                                            |
| **3** | Start the queryThis will immediately execute the live query and post the result to the change listener. When a change is detected the query automatically runs, and posts the new query result to any observers (change listeners). |

Example 2\. Stop a LIve Query

```Java
query.removeChangeListener(token); (1)
```

| **1** | Here we use the change lister token from [Example 1](#ex-qry-start) to remove the listeners. Doing so stops the live query. |
| ----- | --------------------------------------------------------------------------------------------------------------------------- |

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Queries](../../current/android/querybuilder.md)
* [Live Query](../../current/android/query-live.md)
* [Predictive Query](#couchbase-lite:android:query-predictive.adoc)
* [Full Text Search](../../current/android/fts.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/android/database.md)
* [Documents](../../current/android/document.md)
* [Blobs](../../current/android/blob.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)