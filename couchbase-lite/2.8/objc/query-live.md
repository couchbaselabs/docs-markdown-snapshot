---
title: Live Queries
description: Couchbase mobile database live query concepts
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/objc/pages/query-live.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:objc:query-live.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/objc/query-live.html)

# Live Queries

> Description — _Couchbase mobile database live query concepts_  

## [](#overview)Overview

## [](#activating-a-live-query)Activating a Live Query

A live query is a query that, once activated, remains active and monitors the database for changes; refreshing the result set whenever a change occurs. As such, it is a great way to build reactive user interfaces — especially table/list views — that keep themselves up to date.

**So, a simple use case may be:** A replicator running and pulling new data from a server, whilst a live-query-driven UI automatically updates to show the data without the user having to manually refresh. This helps your app feel quick and responsive.

Example 1\. Starting a LIve Query

```objc
CBLQuery *query = [CBLQueryBuilder select:@[[CBLQuerySelectResult all]]
                                     from:[CBLQueryDataSource database:database]];

// Adds a query change listener.
// Changes will be posted on the main queue.
id<CBLListenerToken> token = [query addChangeListener:^(CBLQueryChange * _Nonnull change) // <.>{
    for (CBLQueryResultSet *result in [change results]) {
        NSLog(@"%@", result);
        /* Update UI */
    }
}];

// Start live query.
[query execute: &error]; (1)
```

| **1** | Build the query statements using the QuerybUilder                                                                                                                                                                                   |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Activate the _live_ query by attaching a listener.Save the token in order to detach the listener and stop the query later — se [Example 2](#ex-qry-stop)                                                                            |
| **3** | Start the queryThis will immediately execute the live query and post the result to the change listener. When a change is detected the query automatically runs, and posts the new query result to any observers (change listeners). |

Example 2\. Stop a LIve Query

```objc
[query removeChangeListenerWithToken:token]; (1)
```

| **1** | Here we use the change lister token from [Example 1](#ex-qry-start) to remove the listeners. Doing so stops the live query. |
| ----- | --------------------------------------------------------------------------------------------------------------------------- |