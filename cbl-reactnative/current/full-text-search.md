---
title: Using Full Text Search
pubDate: 2026-10-01T04:32:27.613Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-react-native/edit/release/1.1/modules/ROOT/pages/full-text-search.adoc
  xref: xref:cbl-reactnative::full-text-search.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cbl-reactnative/current/full-text-search.html)

# Using Full Text Search

> Description - _Couchbase Lite database data querying concepts - full text search_Related Content - [Indexing](indexes.md)

## [](#overview)Overview

To run a full-text search (FTS) query, you must create a full-text index on the expression being matched. Unlike regular queries, the index is not optional.

The following examples use the data model introduced in Indexing. They create and use an FTS index built from the hotel's `Overview` text.

## [](#sql)SQL++

### [](#create-index)Create Index

SQL++ provides a configuration object to define Full Text Search indexes using `FullTextIndexItem` and `IndexBuilder`.

#### [](#using-sqls-fulltextindexitem-and-indexbuilder)Using SQL++'s FullTextIndexItem and IndexBuilder

```typescript
const indexProperty = FullTextIndexItem.property('overview');
const index = IndexBuilder.fullTextIndex(indexProperty).setIgnoreAccents(false);
await collection.createIndex('overviewFTSIndex', index);
```

### [](#use-index)Use Index

FullTextSearch is enabled using the SQL++ match() function.

With the index created, you can construct and run a Full-text search (FTS) query using the indexed properties.

The index will omit a set of common words, to avoid words like "I", "the", "an" from overly influencing your queries. See [full list of these stopwords](https://github.com/couchbasedeps/sqlite3-unicodesn/blob/HEAD/stopwords%5Fen.h).

The following example finds all hotels mentioning _Michigan_ in their _Overview_ text.

#### [](#example-2-using-sql-full-text-search)Example 2\. Using SQL++ Full Text Search

```typescript
const ftsQueryString = `
    SELECT _id, overview
    FROM _default
    WHERE MATCH(overviewFTSIndex, 'michigan')
    ORDER BY RANK(overviewFTSIndex)
`;
const ftsQuery = database.createQuery(ftsQueryString);

const results = await ftsQuery.execute();

for(const result of results) {
    console.log(result.getString('_id') + ": " + result.getString('overview'));
}
```

## [](#operation)Operation

In the examples above, the pattern to match is a word, the full-text search query matches all documents that contain the word "michigan" in the value of the `doc.overview` property.

Search is supported for all languages that use whitespace to separate words.

Stemming, which is the process of fuzzy matching parts of speech, like "fast" and "faster", is supported in the following languages: Danish, Dutch, English, Finnish, French, German, Hungarian, Italian, Norwegian, Portuguese, Romanian, Russian, Spanish, Swedish and Turkish.

## [](#pattern-matching-formats)Pattern Matching Formats

As well as providing specific words or strings to match against, you can provide the pattern to match in these formats.

### [](#prefix-queries)Prefix Queries

The query expression used to search for a term prefix is the prefix itself with a "\*" character appended to it.

#### [](#example-5-prefix-query)Example 5\. Prefix query

Query for all documents containing a term with the prefix "lin".

"lin*"

This will match

* All documents that contain "linux"
* And …​ those that contain terms "linear","linker", "linguistic" and so on.

### [](#overriding-the-property-name)Overriding the Property Name

Normally, a token or token prefix query is matched against the document property specified as the left-hand side of the `match` operator. This may be overridden by specifying a property name followed by a ":" character before a basic term query. There may be space between the ":" and the term to query for, but not between the property name and the ":" character.

#### [](#example-6-override-indexed-property-name)Example 6\. Override indexed property name

Query the database for documents for which the term "linux" appears in the document title, and the term "problems" appears in either the title or body of the document.

'title:linux problems'

### [](#phrase-queries)Phrase Queries

A `phrase query`is one that retrieves all documents containing a nominated set of terms or term prefixes in a specified order with no intervening tokens.

Phrase queries are specified by enclosing a space separated sequence of terms or term prefixes in double quotes (").

#### [](#example-7-phrase-query)Example 7\. Phrase query

Query for all documents that contain the phrase "linux applications".

"linux applications"

### [](#near-queries)NEAR Queries

Search for a document that contains the phrase "replication" and the term "database" with not more than 2 terms separating the two.

"database NEAR/2 replication"

### [](#and-or-not-query-operators)AND, OR & NOT Query Operators::

The enhanced query syntax supports the AND, OR and NOT binary set operators. Each of the two operands to an operator may be a basic FTS query, or the result of another AND, OR or NOT set operation. Operators must be entered using capital letters. Otherwise, they are interpreted as basic term queries instead of set operators.

#### [](#example-9-using-and-or-and-not)Example 9\. Using And, Or and Not

Return the set of documents that contain the term "couchbase", and the term "database".

"couchbase AND database"

### [](#operator-precedence)Operator Precedence

When using the enhanced query syntax, parenthesis may be used to specify the precedence of the various operators.

#### [](#example-10-operator-precedence)Example 10\. Operator precedence

Query for the set of documents that contains the term "linux", and at least one of the phrases "couchbase database" and "sqlite library".

'("couchbase database" OR "sqlite library") AND "linux"'

## [](#ordering-results)Ordering Results

It's very common to sort full-text results in descending order of relevance. This can be a very difficult heuristic to define, but Couchbase Lite comes with a ranking function you can use.

In the `OrderBy` array, use a string of the form `Rank(X)`, where `X` is the property or expression being searched, to represent the ranking of the result.