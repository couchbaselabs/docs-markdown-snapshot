---
title: Using Full-Text Search
description: Working with Couchbase Lite's data model  -- Querying the database
  using full text search
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/swift/pages/fts.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@couchbase-lite:swift:fts.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/swift/fts.html)

# Using Full-Text Search

> Description — _Working with Couchbase Lite's data model — Querying the database using full text search_  
> Related Content — [Predictive Query](#couchbase-lite:swift:query-predictive.adoc) | [Indexing](../../current/swift/indexing.md) | [Queries](../../current/swift/querybuilder.md)

## [](#overview)Overview

To run a full-text search (FTS) query, you must have created a full-text index on the expression being matched. Unlike regular queries, the index is not optional.

## [](#using-indexbuilder)Using IndexBuilder

The following example inserts documents and creates an FTS index on the `name` property.

Example 1\. Using the IndexBuilder method

```swift
// Insert documents
let tasks = ["buy groceries", "play chess", "book travels", "buy museum tickets"]
for task in tasks {
    let doc = MutableDocument()
    doc.setString("task", forKey: "type")
    doc.setString(task, forKey: "name")
    try database.saveDocument(doc)
}

// Create index
do {
    let index = IndexBuilder.fullTextIndex(items: FullTextIndexItem.property("name")).ignoreAccents(false)
    try database.createIndex(index, withName: "nameFTSIndex")
} catch let error {
    print(error.localizedDescription)
}
```

Example 2\. Indexing multiple properties

Multiple properties to index can be specified using the following method:

```swift
IndexBuilder.FullTextIndex(params FullTextIndexItem[] items)
```

## [](#constructing-a-query)Constructing a Query

With the index created, you can construct and run a Full-text search (FTS) query on the indexed properties.

The index will omit a set of common words, to avoid words like "I", "the", "an" from overly influencing your queries. See [full list of these **stopwords**](https://github.com/couchbasedeps/sqlite3-unicodesn/blob/HEAD/stopwords%5Fen.h).

The full-text search criteria is defined as a `FullTextExpression`. The left-hand side is the _full-text index_ to use and the right-hand side is the _pattern to match_.

Example 3\. Using the build index

```swift
let whereClause = FullTextExpression.index("nameFTSIndex").match("'buy'")
let query = QueryBuilder
    .select(SelectResult.expression(Meta.id))
    .from(DataSource.database(database))
    .where(whereClause)

do {
    for result in try query.execute() {
        print("document id \(result.string(at: 0)!)")
    }
} catch let error {
    print(error.localizedDescription)
}
```

In the example above, the pattern to match is a word, the full-text search query matches all documents that contain the word "buy" in the value of the `doc.name` property.

Search is supported for all languages that use whitespace to separate words.

Stemming, which is the process of fuzzy matching parts of speech, like "fast" and "faster", is supported in the following languages: danish, dutch, english, finnish, french, german, hungarian, italian, norwegian, portuguese, romanian, russian, spanish, swedish and turkish.

## [](#pattern-matching-formats)Pattern Matching Formats

As well as providing specific words or strings to match against, you can provide the pattern to match in these formats.

### [](#prefix-queries)Prefix Queries

The query expression used to search for a term prefix is the prefix itself with a "\*" character appended to it.

Example 4\. Prefix query

Query for all documents containing a term with the prefix "lin".

"'lin*'"

This will match

* All documents that contain "linux"
* And …​ those that contain terms "linear","linker", "linguistic" and so on.

### [](#overriding-the-property-name)Overriding the Property Name

Normally, a token or token prefix query is matched against the document property specified as the left-hand side of the `match` operator. This may be overridden by specifying a property name followed by a ":" character before a basic term query. There may be space between the ":" and the term to query for, but not between the property name and the ":" character.

Example 5\. Override indexed property name

Query the database for documents for which the term "linux" appears in the document title, and the term "problems" appears in either the title or body of the document.

'title:linux problems'

### [](#phrase-queries)Phrase Queries

A phrase query is a query that retrieves all documents that contain a nominated set of terms or term prefixes in a specified order with no intervening tokens. Phrase queries are specified by enclosing a space separated sequence of terms or term prefixes in double quotes (").

Example 6\. Phrase query

Query for all documents that contain the phrase "linux applications".

"'"linux applications"'"

### [](#near-queries)NEAR Queries

A NEAR query is a query that returns documents that contain a two or more nominated terms or phrases within a specified proximity of each other (by default with 10 or less intervening terms). A NEAR query is specified by putting the keyword "NEAR" between two phrase, token or token prefix queries. To specify a proximity other than the default, an operator of the form "NEAR/" may be used, where is the maximum number of intervening terms allowed.

Example 7\. Near query

Search for a document that contains the phrase "replication" and the term "database" with not more than 2 terms separating the two.

"'database NEAR/2 "replication"'"

### [](#and-or-not-query-operators)AND, OR & NOT Query Operators::

The enhanced query syntax supports the AND, OR and NOT binary set operators. Each of the two operands to an operator may be a basic FTS query, or the result of another AND, OR or NOT set operation. Operators must be entered using capital letters. Otherwise, they are interpreted as basic term queries instead of set operators.

Example 8\. Using And, Or and Not

Return the set of documents that contain the term "couchbase", and the term "database".

'couchbase AND database'

### [](#operator-precedence)Operator Precedence

When using the enhanced query syntax, parenthesis may be used to specify the precedence of the various operators.

Example 9\. Operator precedence

Query for the set of documents that contains the term "linux", and at least one of the phrases "couchbase database" and "sqlite library".

'("couchbase database" OR "sqlite library") AND linux'

## [](#ordering-results)Ordering Results

It's very common to sort full-text results in descending order of relevance. This can be a very difficult heuristic to define, but Couchbase Lite comes with a ranking function you can use.

In the `OrderBy` array, use a string of the form `Rank(X)`, where `X` is the property or expression being searched, to represent the ranking of the result.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Queries](../../current/swift/querybuilder.md)
* [Live Query](../../current/swift/query-live.md)
* [Predictive Query](#couchbase-lite:swift:query-predictive.adoc)
* [Full Text Search](../../current/swift/fts.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/swift/database.md)
* [Documents](../../current/swift/document.md)
* [Blobs](../../current/swift/blob.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)