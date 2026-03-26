---
title: Using Full-Text Search
description: Working with Couchbase Lite's data model  -- Querying the database
  using full text search
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/c/pages/fts.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@couchbase-lite:c:fts.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/c/fts.html)

# Using Full-Text Search

> Description — _Working with Couchbase Lite's data model — Querying the database using full text search_  
> Related Content — [Predictive Queries](#c:querybuilder.adoc#lbl-predquery) | [Indexing](indexing.md) | [QueryBuilder](#c:querybuilder.adoc)

## [](#overview)Overview

To run a full-text search (FTS) query, you must create a full-text index on the expression being matched. Unlike regular queries, the index is not optional.

The following examples use the data model introduced in [Indexing](indexing.md). They create and use an FTS index built from the hotel's `Overview` text.

## [](#create-index)Create Index

N1QL provides a configuration object to define Full Text Search indexes — `FullTextIndexConfiguration`.

Example 1\. Using N1QL's FullTextIndexConfiguration

```c
// NOTE: No error handling, for brevity (see getting started)

CBLError err;
CBLFullTextIndexConfiguration config = {
    kCBLN1QLLanguage,
    FLSTR("name"),
    false
};

CBLDatabase_CreateFullTextIndex(db, FLSTR("nameFTSIndex"), config, &err);
```

## [](#use-index)Use Index

FullTextSearch is enabled using the SQL++ match() function.

With the index created, you can construct and run a Full-text search (FTS) query using the indexed properties.

The index will omit a set of common words, to avoid words like "I", "the", "an" from overly influencing your queries. See [full list of these **stopwords**](https://github.com/couchbasedeps/sqlite3-unicodesn/blob/HEAD/stopwords%5Fen.h).

The following example finds all hotels mentioning _Michigan_ in their _Overview_ text.

Example 2\. Using SQL++ Full Text Search

```c
// NOTE: No error handling, for brevity (see getting started)

CBLError err;
CBLQuery* query = CBLDatabase_CreateQuery(db, kCBLN1QLLanguage,
    FLSTR("SELECT meta().id FROM _ WHERE MATCH(nameFTSIndex, \"'buy'\")"),
    NULL, &err);

CBLResultSet* results = CBLQuery_Execute(query, &err);
while(CBLResultSet_Next(results)) {
    FLString id = FLValue_AsString(CBLResultSet_ValueAtIndex(results, 0));
    printf("Document id :: %.*s\n", (int)id.size, (const char *)id.buf);
}

CBLResultSet_Release(results);
CBLQuery_Release(query);
```

## [](#operation)Operation

In the examples above, the pattern to match is a word, the full-text search query matches all documents that contain the word "michigan" in the value of the `doc.overview` property.

Search is supported for all languages that use whitespace to separate words.

Stemming, which is the process of fuzzy matching parts of speech, like "fast" and "faster", is supported in the following languages: Danish, Dutch, English, Finnish, French, German, Hungarian, Italian, Norwegian, Portuguese, Romanian, Russian, Spanish, Swedish and Turkish.

## [](#pattern-matching-formats)Pattern Matching Formats

As well as providing specific words or strings to match against, you can provide the pattern to match in these formats.

### [](#prefix-queries)Prefix Queries

The query expression used to search for a term prefix is the prefix itself with a "\*" character appended to it.

Example 3\. Prefix query

Query for all documents containing a term with the prefix "lin".

"lin*"

This will match

* All documents that contain "linux"
* And …​ those that contain terms "linear","linker", "linguistic" and so on.

### [](#overriding-the-property-name)Overriding the Property Name

Normally, a token or token prefix query is matched against the document property specified as the left-hand side of the `match` operator. This may be overridden by specifying a property name followed by a ":" character before a basic term query. There may be space between the ":" and the term to query for, but not between the property name and the ":" character.

Example 4\. Override indexed property name

Query the database for documents for which the term "linux" appears in the document title, and the term "problems" appears in either the title or body of the document.

'title:linux problems'

### [](#phrase-queries)Phrase Queries

A _phrase query_ is one that retrieves all documents containing a nominated set of terms or term prefixes in a specified order with no intervening tokens.

Phrase queries are specified by enclosing a space separated sequence of terms or term prefixes in double quotes (").

Example 5\. Phrase query

Query for all documents that contain the phrase "linux applications".

"linux applications"

### [](#near-queries)NEAR Queries

A NEAR query is a query that returns documents that contain a two or more nominated terms or phrases within a specified proximity of each other (by default with 10 or less intervening terms). A NEAR query is specified by putting the keyword "NEAR" between two phrase, token or token prefix queries. To specify a proximity other than the default, an operator of the form "NEAR/" may be used, where is the maximum number of intervening terms allowed.

Example 6\. Near query

Search for a document that contains the phrase "replication" and the term "database" with not more than 2 terms separating the two.

"database NEAR/2 replication"

### [](#and-or-not-query-operators)AND, OR & NOT Query Operators::

The enhanced query syntax supports the AND, OR and NOT binary set operators. Each of the two operands to an operator may be a basic FTS query, or the result of another AND, OR or NOT set operation. Operators must be entered using capital letters. Otherwise, they are interpreted as basic term queries instead of set operators.

Example 7\. Using And, Or and Not

Return the set of documents that contain the term "couchbase", and the term "database".

"couchbase AND database"

### [](#operator-precedence)Operator Precedence

When using the enhanced query syntax, parenthesis may be used to specify the precedence of the various operators.

Example 8\. Operator precedence

Query for the set of documents that contains the term "linux", and at least one of the phrases "couchbase database" and "sqlite library".

'("couchbase database" OR "sqlite library") AND "linux"'

## [](#ordering-results)Ordering Results

It's very common to sort full-text results in descending order of relevance. This can be a very difficult heuristic to define, but Couchbase Lite comes with a ranking function you can use.

In the `OrderBy` array, use a string of the form `Rank(X)`, where `X` is the property or expression being searched, to represent the ranking of the result.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [SQL++ for Mobile](query-n1ql-mobile.md)
* [Live Queries](query-live.md)
* [Full Text Search](fts.md)

###### [](#-2)

Learn more . . .

* [SQL++ Mobile - SQL++ Server Differences](query-n1ql-mobile-server-diffs.md)
* [Query Resultsets](query-resultsets.md)
* [Query Troubleshooting](query-troubleshooting.md)
* [Live Queries](query-live.md)
* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)