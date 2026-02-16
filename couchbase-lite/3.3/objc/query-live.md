[View original HTML](/couchbase-lite/3.3/objc/query-live.html)

> Description — _Couchbase mobile database live query concepts_  

## [](#activating-a-live-query)Activating a Live Query

A live query is a query that, once activated, remains active and monitors the database for changes; refreshing the result set whenever a change occurs. As such, it is a great way to build reactive user interfaces — especially table/list views — that keep themselves up to date.

**So, a simple use case may be:** A replicator running and pulling new data from a server, whilst a live-query-driven UI automatically updates to show the data without the user having to manually refresh. This helps your app feel quick and responsive.

To activate a LiveQuery just add a change listener to the query statement. It will be immediately active. When a change is detected the query automatically runs, and posts the new query result to any observers (change listeners).

Example 1\. Starting a Live Query

```objc
CBLQuery *query = [CBLQueryBuilder select:@[[CBLQuerySelectResult all]]
                                     from:[CBLQueryDataSource collection:collection]]; (1)

// Adds a query change listener.
// Changes will be posted on the main queue.
id<CBLListenerToken> token = [query addChangeListener:^(CBLQueryChange  *change) { (2)
    for (CBLQueryResultSet *results in [change results]) {
        NSLog(@"%@", results);
        /* Update UI */
    }
}]; (3)
```

| **1** | Build the query statements                                                                                                                                |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Activate the _live_ query by attaching a listener. Save the token in order to detach the listener and stop the query later — se [Example 2](#ex-qry-stop) |

Example 2\. Stop a LIve Query

```objc
[query removeChangeListenerWithToken:token]; (1)
```

| **1** | Here we use the change lister token from [Example 1](#ex-qry-start) to remove the listener. Doing so stops the live query. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |