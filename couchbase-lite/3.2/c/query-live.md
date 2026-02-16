[View original HTML](/couchbase-lite/3.2/c/query-live.html)

> Description — _Couchbase mobile database live query concepts_  

## [](#overview)Overview

## [](#activating-a-live-query)Activating a Live Query

A live query is a query that, once activated, remains active and monitors the database for changes; refreshing the result set whenever a change occurs. As such, it is a great way to build reactive user interfaces — especially table/list views — that keep themselves up to date.

**So, a simple use case may be:** A replicator running and pulling new data from a server, whilst a live-query-driven UI automatically updates to show the data without the user having to manually refresh. This helps your app feel quick and responsive.

To activate a LiveQuery just add a change listener to the query statement. It will be immediately active. When a change is detected the query automatically runs, and posts the new query result to any observers (change listeners).

Example 1\. Starting a Live Query

```c
/*
static void query_change_listener(void* context, CBLQuery* query, CBLListenerToken* token) {
    CBLError err{};
    CBLResultSet* results = CBLQuery_CopyCurrentResults(query, token, &err);
    while(CBLResultSet_Next(results)) {
        // Update UI
    }
}
*/

// NOTE: No error handling, for brevity (see getting started)

CBLError err{};
CBLQuery* query = CBLDatabase_CreateQuery(database, kCBLN1QLLanguage,
    FLSTR("SELECT * FROM _"), NULL, &err); (1)

CBLListenerToken* token = CBLQuery_AddChangeListener(query, query_change_listener, NULL); (2)
```

| **1** | Build the query statements                                                                                                                                |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Activate the _live_ query by attaching a listener. Save the token in order to detach the listener and stop the query later — se [Example 2](#ex-qry-stop) |

Example 2\. Stop a LIve Query

```c
CBLListener_Remove(token); // The token received from AddChangeListener
CBLQuery_Release(query);
```

| **1** | Here we use the change lister token from [Example 1](#ex-qry-start) to remove the listener. Doing so stops the live query. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |