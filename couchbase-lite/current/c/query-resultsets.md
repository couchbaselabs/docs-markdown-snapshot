---
title: Result Sets
description: How to use Couchbase Lite Query's Result Sets
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/c/pages/query-resultsets.adoc
pubDate: 2026-03-24T03:43:23.693Z
link: xref:couchbase-lite:c:query-resultsets.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/c/query-resultsets.html)

# Result Sets

> Description — _How to use Couchbase Lite Query’s Result Sets_  
> Related Content — [QueryBuilder](#c:querybuilder.adoc) | [SQL++ for Mobile](query-n1ql-mobile.md) | [Predictive Queries](#c:querybuilder.adoc#lbl-predquery) | [Live Queries](query-live.md) | [Indexing](indexing.md)

## [](#query-execution)Query Execution

The execution of a Couchbase Lite for C’s database query returns an array of results, a result set.

Each row of the result set represents the data returned from a document that met the conditions defined by the `WHERE` statement of your query. The composition of each row is determined by the `SelectResult` expressions provided in the `SELECT` statement.

## [](#lbl-process-resultset)Processing Results

[Access Document Properties - All Properties](#lbl-acc-all)| [Access Document Properties - ID](#lbl-acc-id)| [Access Document Properties - Selected Properties](#lbl-acc-specific)

To retrieve the results of your query, you need to execute it using `Query.execute`.

The output from the execution is an array, with each array element representing the data from a document that matched your search criteria.

To unpack the results you need to iterate through this array. Alternatively, you can convert the result to a JSON string — see:

### [](#lbl-acc-all)Access Document Properties - All Properties

Here we look at how to access document properties when you have used SelectResult.all.

In this case each array element is a dictionary structure with the database name as its key. The properties are presented in the value as an array of key-value pairs (property name/property value).

You access the retrieved document properties by converting each row’s value, in turn, to a dictionary — as shown in [Example 1](#ex-acc-all).

Example 1\. Access All Properties

```c
CBLResultSet* results = CBLQuery_Execute(query, &err);
while(CBLResultSet_Next(results)) {
    FLDict dict = FLValue_AsDict(CBLResultSet_ValueForKey(results, FLSTR("_")));

    FLString id = FLValue_AsString(FLDict_Get(dict, FLSTR("id")));
    FLString type = FLValue_AsString(FLDict_Get(dict, FLSTR("type")));
    FLString name = FLValue_AsString(FLDict_Get(dict, FLSTR("name")));
    FLString city = FLValue_AsString(FLDict_Get(dict, FLSTR("city")));

    printf("ID :: %.*s\n", (int)id.size, (const char *)id.buf);
    printf("Type :: %.*s\n", (int)type.size, (const char *)type.buf);
    printf("Name :: %.*s\n", (int)name.size, (const char *)name.buf);
    printf("City :: %.*s\n", (int)city.size, (const char *)city.buf);
}

// All results will be available from the above query
CBLResultSet_Release(results);
```

| **1** | Here we get the dictionary of document properties using the database name as the key. You can add this dictionary to an array of returned matches, for processing elsewhere in the app. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Alternatively, you can access the document properties here, by using the property names as keys to the dictionary object.                                                               |

### [](#lbl-acc-id)Access Document Properties - ID

Here we look at how to access document properties when you have returned only the document IDs for documents that matched your selection criteria.

This is something you may do when retrieval of the properties directly by the query may consume excessive amounts of memory and-or processing time.

In this case each array element is a dictionary structure where `ID` is the key and the required document ID is the value.

Access the required document properties by retrieving the document from the database using its document ID — as shown in [Example 2](#ex-acc-id).

Example 2\. Access by ID

```c
// NOTE: No error handling, for brevity (see getting started)

CBLResultSet* results = CBLQuery_Execute(query, &err);
while(CBLResultSet_Next(results)) {
    FLString id = FLValue_AsString(CBLResultSet_ValueForKey(results, FLSTR("id")));
    printf("Document ID :: %.*s\n", (int)id.size, (const char *)id.buf);
}
```

| **1** | Extract the Id value from the dictionary and use it to get the document from the database |
| ----- | ----------------------------------------------------------------------------------------- |

### [](#lbl-acc-specific)Access Document Properties - Selected Properties

Here we look at how to access properties when you have used SelectResult to get a specific subset of properties.

In this case each array element is an array of key value pairs (property name/property value).

Access the retrieved properties by converting each row into a dictionary — as shown in [\[ex-acc-specific\]](#ex-acc-specific).

```c
// NOTE: No error handling, for brevity (see getting started)

CBLError err{};
CBLQuery* query = CBLDatabase_CreateQuery(database, kCBLN1QLLanguage,
    FLSTR("SELECT type, name, city FROM _"), NULL, &err);

CBLResultSet* results = CBLQuery_Execute(query, &err);
while(CBLResultSet_Next(results)) {
    FLString type = FLValue_AsString(CBLResultSet_ValueForKey(results, FLSTR("type")));
    FLString name = FLValue_AsString(CBLResultSet_ValueForKey(results, FLSTR("name")));
    FLString city = FLValue_AsString(CBLResultSet_ValueForKey(results, FLSTR("city")));

    printf("Type :: %.*s\n", (int)type.size, (const char *)type.buf);
    printf("Name :: %.*s\n", (int)name.size, (const char *)name.buf);
    printf("City :: %.*s\n", (int)city.size, (const char *)city.buf);
}
```

## [](#json-result-sets)JSON Result Sets

Example 3\. Using JSON Results

Use [FLValue\_ToJSON()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-c/C/html/group%5F%5Fjson.html#ga3450acc0690101545d75986b91e4080) to transform your result string into a JSON string, which can easily be serialized or used as required in your application. See [Example 3](#ex-json) for a working example.

```c
CBLResultSet* results = CBLQuery_Execute(query, &err);
while(CBLResultSet_Next(results)) {
    FLDict result = CBLResultSet_ResultDict(results);
    FLStringResult json = FLValue_ToJSON((FLValue)result);
    printf("JSON Result :: %.*s\n", (int)json.size, (const char *)json.buf);
    FLSliceResult_Release(json);
}
CBLResultSet_Release(results);
```

JSON String Format

If your query selects ALL then the JSON format will be:

```JSON
{
  database-name: {
    key1: "value1",
    keyx: "valuex"
  }
}
```

If your query selects a sub-set of available properties then the JSON format will be:

```JSON
{
  key1: "value1",
  keyx: "valuex"
}
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.