---
title: Live Queries
description: Couchbase mobile database live query concepts
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/swift/pages/query-live.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite/current/swift/query-live.html)

# Live Queries

> Couchbase mobile database live query concepts 

## [](#activating-a-live-query)Activating a Live Query

A live query is a query that, once activated, remains active and monitors the database for changes; refreshing the result set whenever a change occurs. As such, it is a great way to build reactive user interfaces — especially table/list views — that keep themselves up to date.

**So, a simple use case may be:** A replicator running and pulling new data from a server, whilst a live-query-driven UI automatically updates to show the data without the user having to manually refresh. This helps your app feel quick and responsive.

To activate a LiveQuery just add a change listener to the query statement. It will be immediately active. When a change is detected the query automatically runs, and posts the new query result to any observers (change listeners).

Example 1\. Starting a Live Query

```swift
query = QueryBuilder
    .select(SelectResult.all())
    .from(DataSource.collection(self.collection)) (1)

// Adds a query change listener.
// Changes will be posted on the main queue.
let token = query.addChangeListener { (change) in (2)
    for result in change.results! {
        print(result.keys)
        /* Update UI */
    }
} (3)
```

| **1** | Build the query statements                                                                                                                                |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Activate the _live_ query by attaching a listener. Save the token in order to detach the listener and stop the query later — se [Example 2](#ex-qry-stop) |

Example 2\. Stop a LIve Query

```swift
token.remove() (1)
```

| **1** | Here we use the change lister token from [Example 1](#ex-qry-start) to remove the listener. Doing so stops the live query. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |