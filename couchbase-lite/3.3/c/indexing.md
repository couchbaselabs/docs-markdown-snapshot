---
title: Indexing your Data
description: Couchbase Lite database data model concepts - indexes
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/c/pages/indexing.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.3@couchbase-lite:c:indexing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.3/c/indexing.html)

# Indexing your Data

> Description — _Couchbase Lite database data model concepts - indexes_  
> Related Content — [Databases](database.md) | [Documents](document.md) | [Indexing](indexing.md) |

## [](#introduction)Introduction

Querying documents using a pre-existing database index is much faster because an index narrows down the set of documents to examine — see: the [Query Troubleshooting](#c:query-troubleshooting.adoc) topic.

When planning the indexes you need for your database, remember that while indexes make queries faster, they may also:

* Make writes slightly slower, because each index must be updated whenever a document is updated
* Make your Couchbase Lite database slightly larger.

Too many indexes may hurt performance. Optimal performance depends on designing and creating the _right_ indexes to go along with your queries.

> [!NOTE]
> Constraints
> 
> Couchbase Lite for c does not currently support partial value indexes; indexes with non-property expressions. You should only index with properties that you plan to use in the query.

## [](#creating-a-new-index)Creating a new index

You can use SQL++ or QueryBuilder syntaxes to create an index

[Example 2](#ex-create-index) creates a new index for the `type` and `name` properties, shown in this data model:

Example 1\. Data Model

```json
{
    "_id": "hotel123",
    "type": "hotel",
    "name": "The Michigander",
    "overview": "Ideally situated for exploration of the Motor City and the wider state of Michigan. Tripadvisor rated the hotel ...",
    "state": "Michigan"
}
```

### [](#sql)SQL++

The code to create the index will look something like this:

Example 2\. Create index

```c
// For value types, this is optional but provides performance enhancements
// NOTE: No error handling, for brevity (see getting started)

// Syntax for second argument is the same as taking from a N1QL SELECT
// i.e. SELECT (type, name) FROM _;
CBLValueIndexConfiguration config{};
config.expressionLanguage = kCBLN1QLLanguage;
config.expressions = FLSTR("type, name");

CBLError err{};
CBLCollection_CreateValueIndex(collection, FLSTR("TypeNameIndex"), config, &err);
```

## [](#partial-index)Partial Index

Couchbase Lite 3.2.2 introduces support for Partial Index - Partial Value and Partial Full-Text Indexes. The Partial Index can create a smaller index, potentially improving index and query performance. You can use Partial Index to specify a `WHERE` clause in your index configuration. If a where clause is specified, the database will index a document only when the where clause condition is met.

Couchbase's query optimizer uses [SQLite's Partial Index rules about queries using Partial Indexes](https://www.sqlite.org/partialindex.html) to determine whether to use partial index in the query or not.

Example 3\. Couchbase and SQLite's Partial Index Rules

In general, Couchbase Lite follows the two rules, with a modification to the second rule.

Below is a summary of the two rules where:

* `X` \- The expression in the `WHERE` clause of a given Partial Index.
* `W` \- The expression in the `WHERE` clause of a given query.

A query can use the Partial Index if the following two rules are satisfied:

1. If `W` is AND-connected terms, and `X` is OR-connected terms and if any terms of `W` appears as a term of `X`, the partial index is allowed to be used.
2. If a term in `X` is of the form `"z IS NOT MISSING"` and if a term in `W` is a comparison operator on `z` other than `"IS"`, the partial index is allowed to be used. The operators include `=`, `==`, `<`, `>`, `<=`, `>=`, `<>`, `IN`, `LIKE`, and `BETWEEN`.

> [!IMPORTANT]
> If `X` is in the form of `"z is NOT NULL"` or `"z is VALUED"`, the first rule must be satisfied.

For example, let the partial index be `c IS NOT NULL` when creating a partial index on collection named `col1` in the default scope.

Then any query that uses operators `=`, `<`, `>`, `<=`, `>=`, `<>`, `IN`, `LIKE`, or `BETWEEN` on column `c` would be usable with the partial index, because those comparison operators are only true if `c` is not NULL.

The following query could use the partial index:

```sqlpp
SELECT * FROM col1 WHERE b=456 AND c<>0;  -- uses partial index
```

Whereas the next query can not use the partial index:

```sqlpp
SELECT * FROM col1 WHERE b=456;  -- cannot use partial index
```

### [](#partial-value-index)Partial Value Index

Partial Value Index is a form of Partial Index in which a value is used in the `WHERE` clause and the query is selected by the query optimizer.

```c
    CBLValueIndexConfiguration config {};
    config.expressionLanguage = kCBLN1QLLanguage;
    config.expressions = FLSTR("city");
    config.where = FLSTR("type = \"hotel\"");

    CBLError err{};
    CBLCollection_CreateValueIndex(collection, FLSTR("HotelCityIndex"), config, &err);
```

### [](#partial-full-text-index)Partial Full-Text Index

A key difference between a Partial Value Index and a Partial Full-Text Index is that a Partial Full-Text Index is not selected by SQLite's query optimizer. Instead, it's explicitly selected by the SQL++ `match(indexName, terms)` function, which runs a Full-Text Search query using the indexed properties. This means that a Partial Full-Text Index will always be used when the `match()` function is invoked, regardless of other predicates in the WHERE clause. For details, see [Using Full-Text Search](fts.md).

```c
    CBLFullTextIndexConfiguration config{};
    config.expressionLanguage = kCBLN1QLLanguage;
    config.expressions = FLSTR("description");
    config.where = FLSTR("type = \"hotel\"");

    CBLError err{};
    CBLCollection_CreateFullTextIndex(collection, FLSTR("HotelDescIndex"), config, &err);
```

## [](#array-indexing)Array Indexing

Couchbase Lite 3.2.1 introduces functionality to optimize querying arrays. [Array UNNEST](query-n1ql-mobile.md#lbl-unnest) to unpack arrays within a document to allow joins with the parent object, and array indexes for indexing unnested array's values to allow more efficient queries with `UNNEST`.

### [](#the-array-index)The Array Index

An array index is a new type of the index for indexing nested array's properties to allow querying with the `UNNEST` more efficiently.

Below is an example array index configuration:

```c
CBLArrayIndexConfiguration config{};
config.expressionLanguage = kCBLN1QLLanguage;
config.path = FLSTR("contacts");
```

### [](#array-index-syntax)Array Index Syntax

The syntax for array index configuration is shown below:

| Name        | Is Optional?               | Description                                                                                                                                                                                                                                                                                                                                                                              |
| ----------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| path        | ![no](../_images/no.png)   | Path to the array to be indexed. Use \[\] to represent a property that is an array of each nested array level. For a single array or the last level array, the \[\] is optional. For instance contacts\[\].phones to specify an array of phones within each contact.                                                                                                                     |
| expressions | ![yes](../_images/yes.png) | An optional array of strings where each string represents values within the array to be indexed. In N1QL/SQL++ syntax, these expressions are separated by commas. In JSON syntax, as supported by Couchbase Lite for C, the expressions are represented as a JSON array. If the array specified by the path contains scalar values, the expressions should be left unset or set to null. |

### [](#using-array-indexes-with-unnest)Using Array Indexes with UNNEST

For the following examples, you can assume we are querying results from the following document, shown below:

```JSON
{
   "Name":"Sam",
   "contacts":[
     {
       "type":"primary",
       "address":{"street":"1 St","city":"San Pedro","state":"CA"},
       "phones":[
         {"type":"home","number":"310-123-4567"},
         {"type":"mobile","number":"310-123-6789"}
       ]
     },
     {
       "type":"secondary",
       "address":{"street":"5 St","city":"Seattle","state":"WA"},
       "phones":[
         {"type":"home","number":"206-123-4567"},
         {"type":"mobile","number":"206-123-6789"}
       ]
     }
   ],
   "likes":["soccer","travel"]
 }
```

Using the document above you can perform queries on a single nested array like so:

```sqlpp
SELECT name, interest FROM _ UNNEST likes as interest WHERE interest = "travel"
```

The query above produces the following output from the document:

```JSON
{"name": "Sam", "like": "travel"}
```

You can also perform the same operation using array indexes like so:

```c
    CBLArrayIndexConfiguration config{};
    config.expressionLanguage = kCBLN1QLLanguage;
    config.path = FLSTR("likes");

    CBLError err{};
    CBLCollection_CreateArrayIndex(collection, FLSTR("myindex"), config, &err);
```

You can perform similar operations on nested arrays:

```sqlpp
SELECT name, contact.type, phone.number
FROM profiles
UNNEST contacts as contact
UNNEST contact.phones as phone
WHERE phone.type = "mobile"
```

The query produces the following output:

```JSON
{"name": "Sam", "type": "primary", "number": "310-123-6789"}
{"name": "Sam", "type": "secondary", "number": "206-123-6789"}
```

The output demonstrates retrieval of both primary and secondary contact numbers listed as type `"mobile"`.

Here's an example of creating an array index on a nested array containing dictionary values:

```c
    CBLArrayIndexConfiguration config{};
    config.expressionLanguage = kCBLN1QLLanguage;
    config.path = FLSTR("contacts[].phones");
    config.expressions = FLSTR("type");

    CBLError err{};
    CBLCollection_CreateArrayIndex(collection, FLSTR("myindex"), config, &err);
```

The above snippet creates an array index to allow you to iterate through `contacts[].phones[].type` in the document, namely `"home"` and `"mobile"`.

> [!IMPORTANT]
> Array literals are not supported in CBL 3.3.0\. Attempting to create a query with array literals will return an error.

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](#c:gs-prereqs.adoc)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.