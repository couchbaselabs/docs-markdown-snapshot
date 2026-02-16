[View original HTML](/couchbase-lite/3.3/java/query-live.html)

> Description — _Working with Couchbase Lite’s data model — Querying database data using live queries_  
> Related Content — [Predictive Queries](querybuilder.md#lbl-predquery) | [Indexing](indexing.md) | [QueryBuilder](querybuilder.md)

## [](#activating-a-live-query)Activating a Live Query

A live query is a query that, once activated, remains active and monitors the database for changes; refreshing the result set whenever a change occurs. As such, it is a great way to build reactive user interfaces — especially table/list views — that keep themselves up to date.

**So, a simple use case may be:** A replicator running and pulling new data from a server, whilst a live-query-driven UI automatically updates to show the data without the user having to manually refresh. This helps your app feel quick and responsive.

To activate a LiveQuery just add a change listener to the query statement. It will be immediately active. When a change is detected the query automatically runs, and posts the new query result to any observers (change listeners).

Example 1\. Starting a Live Query

```Java
Query query = QueryBuilder
    .select(SelectResult.all())
    .from(DataSource.collection(collection)); (1)

// Adds a query change listener.
// Changes will be posted on the main queue.
ListenerToken token = query.addChangeListener(change -> { (2)
    for (Result result: change.getResults()) {
        Logger.log("results: " + result.getKeys());
        /* Update UI */
    }
});
```

| **1** | Build the query statements                                                                                                                                |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Activate the _live_ query by attaching a listener. Save the token in order to detach the listener and stop the query later — se [Example 2](#ex-qry-stop) |

Example 2\. Stop a LIve Query

```Java
token.remove(); (1)
```

| **1** | Here we use the change lister token from [Example 1](#ex-qry-start) to remove the listener. Doing so stops the live query. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |

## [](#related-content)Related Content

###### [](#)

How to . . .

* [QueryBuilder](querybuilder.md)
* [SQL++ for Mobile](query-n1ql-mobile.md)
* [Live Queries](query-live.md)
* [Full Text Search](fts.md)

.

###### [](#-2)

Learn more . . .

* [SQL++ Mobile - Querybuilder Differences](query-n1ql-mobile-querybuilder-diffs.md)
* [SQL++ Mobile - SQL++ Server Differences](query-n1ql-mobile-server-diffs.md)
* [Query Resultsets](query-resultsets.md)
* [Query Troubleshooting](query-troubleshooting.md)
* [Live Queries](query-live.md)
* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.