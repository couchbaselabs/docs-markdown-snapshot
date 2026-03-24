---
title: QueryBuilder
description: How to use QueryBuilder to build effective queries with Couchbase Lite on Swift
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/swift/pages/querybuilder.adoc
pubDate: 2026-03-24T03:43:23.693Z
link: xref:couchbase-lite:swift:querybuilder.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/swift/querybuilder.html)

# QueryBuilder

> Description — _How to use QueryBuilder to build effective queries with Couchbase Lite on Swift_  
> Related Content — [Live Queries](query-live.md) | [Indexing](indexing.md)

> [!NOTE]
> The examples used here are based on the _Travel Sample_ app and data introduced in the [Couchbase Mobile Workshop](https://docs.couchbase.com/tutorials/mobile-travel-tutorial/introduction.html) tutorial

## [](#introduction)Introduction

Couchbase Lite for Swift provides two ways to build and run database queries; the QueryBuilder API described in this topic and [SQL++ for Mobile](query-n1ql-mobile.md).

Database queries defined with the QueryBuilder API use the query statement format shown in [Example 1](#ex-query-form). The structure and semantics of the query format are based on Couchbase’s [SQL++ query language](../../../server/current/learn/data/n1ql-versus-sql.md).

Example 1\. Query Format

```SQL
SELECT ____
FROM 'data-source'
WHERE ____,
JOIN ____
GROUP BY ____
ORDER BY ____
```

Query Components

| Component                        | Description                                                                                                          |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [SELECT statement](#lbl-select)  | The document properties that will be returned in the result set                                                      |
| FROM                             | The data source to query the documents from - the collection of the database.                                        |
| [WHERE statement](#lbl-where)    | The query criteriaThe \`SELECT\`ed properties of documents matching this criteria will be returned in the result set |
| [JOIN statement](#lbl-join)      | The criteria for joining multiple documents                                                                          |
| [GROUP BY statement](#lbl-group) | The criteria used to group returned items in the result set                                                          |
| [ORDER BY statement](#lbl-order) | The criteria used to order the items in the result set                                                               |

> [!TIP]
> We recommend working through the query section of the [Couchbase Mobile Workshop](https://docs.couchbase.com/tutorials/mobile-travel-tutorial/introduction.html) tutorial as a good way to build your skills in this area.

## [](#lbl-select)SELECT statement

In this section

[Return Selected Properties](#lbl-return-properties) | [Return All Properties](#lbl-return-all)

Related

[Handling result sets](#lbl-resultsets)

Use the `SELECT` statement to specify which properties you want to return from the queried documents. You can opt to retrieve entire documents, or just the specific properties you need.

### [](#lbl-return-all)Return All Properties

Use the `SelectResult.all()` method to return all the properties of selected documents — see: [Example 2](#ex-select-all).

Example 2\. Using SELECT to Retrieve All Properties

This query shows how to retrieve all properties from all documents in your database.

```swift
query = QueryBuilder
    .select(SelectResult.all())
    .from(DataSource.collection(self.collection))
```

The query.execute statement returns the results in a dictionary, where the key is the database name — see [Example 3](#ex-return-all).

Example 3\. ResultSet Format from SelectResult.all()

```json
[
  {
    "travel-sample": { (1)
      "callsign": "MILE-AIR",
      "country": "United States",
      "iata": "Q5",
      "icao": "MLA",
      "id": 10,
      "name": "40-Mile Air",
      "type": "airline"
    }
  },
  {
    "travel-sample": { (2)
      "callsign": "ALASKAN-AIR",
      "country": "United States",
      "iata": "AA",
      "icao": "AAA",
      "id": 10,
      "name": "Alaskan Airways",
      "type": "airline"
    }
  }
]
```

| **1** | The result for the first document matching the query criteria. |
| ----- | -------------------------------------------------------------- |
| **2** | The result for the next document matching the query criteria.  |

See: [Result Sets](#lbl-resultsets) for more on processing query results.

### [](#lbl-return-properties)Return Selected Properties

To access only specific properties, specify a comma-separated list of `SelectResult` expressions, one for each property, in the select statement of your query — see: [Example 4](#ex-select-properties)

Example 4\. Using SELECT to Retrieve Specific Properties

In this query we retrieve and then print the `_id`, `type` and `name` properties of each document.

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("type"),
        SelectResult.property("name")
    )
    .from(DataSource.collection(self.collection))

do {
    for result in try query.execute() {
        print("document id :: \(result.string(forKey: "id")!)")
        print("document name :: \(result.string(forKey: "name")!)")
    }
} catch {
    print(error)
}
```

The `query.execute` statement returns one or more key-value pairs, one for each SelectResult expression, with the property-name as the key — see [Example 5](#ex-return-properties)

Example 5\. Select Result Format

```json
[
  { (1)
    "id": "hotel123",
    "type": "hotel",
    "name": "Hotel Ghia"
  },
  { (2)
    "id": "hotel456",
    "type": "hotel",
    "name": "Hotel Deluxe",
  }
]
```

| **1** | The result for the first document matching the query criteria. |
| ----- | -------------------------------------------------------------- |
| **2** | The result for the next document matching the query criteria.  |

See: [Result Sets](#lbl-resultsets) for more on processing query results.

## [](#lbl-where)WHERE statement

In this section

[Comparison Operators](#lbl-comp-ops) | [Collection Operators](#lbl-coll-ops) | [Like Operator](#lbl-like-ops) | [Regex Operator](#lbl-regex-ops) | [Deleted Document](#lbl-deleted-ops)

Like SQL, you can use the `WHERE` statement to choose which documents are returned by your query. The select statement takes in an `Expression`. You can chain any number of Expressions in order to implement sophisticated filtering capabilities.

### [](#lbl-comp-ops)Comparison Operators

The [Expression Comparators](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-swift/Classes/Expression.html) can be used in the WHERE statement to specify on which property to match documents. In the example below, we use the `equalTo` operator to query documents where the `type` property equals "hotel".

```json
[
  { (1)
    "id": "hotel123",
    "type": "hotel",
    "name": "Hotel Ghia"
  },
  { (2)
    "id": "hotel456",
    "type": "hotel",
    "name": "Hotel Deluxe",
  }
]
```

Example 6\. Using Where

```swift
let query = QueryBuilder
    .select(SelectResult.all())
    .from(DataSource.collection(self.collection))
    .where(Expression.property("type").equalTo(Expression.string("hotel")))
    .limit(Expression.int(10))

do {
    for result in try query.execute() {
        if let dict = result.dictionary(forKey: "travel-sample") {
            print("document name :: \(dict.string(forKey: "name")!)")
        }
    }
} catch {
    print(error)
}
```

### [](#lbl-coll-ops)Collection Operators

[Array Collection Operators](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-swift/Classes/ArrayExpression.html) are useful to check if a given value is present in an array.

#### [](#contains-operator)CONTAINS Operator

The following example uses the `[ArrayFunction](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-swift/Classes/ArrayFunction.html)` to find documents where the `public_likes` array property contains a value equal to "Armani Langworth".

```json
{
    "_id": "hotel123",
    "name": "Apple Droid",
    "public_likes": ["Armani Langworth", "Elfrieda Gutkowski", "Maureen Ruecker"]
}
```

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("name"),
        SelectResult.property("public_likes")
    )
    .from(DataSource.collection(self.collection))
    .where(Expression.property("type").equalTo(Expression.string("hotel"))
            .and(ArrayFunction.contains(Expression.property("public_likes"),
                                        value: Expression.string("Armani Langworth")))
    )

do {
    for result in try query.execute() {
        print("public_likes :: \(result.array(forKey: "public_likes")!.toArray())")
    }
}
```

#### [](#in-operator)IN Operator

The `IN` operator is useful when you need to explicitly list out the values to test against. The following example looks for documents whose `first`, `last` or `username` property value equals "Armani".

```swift
let properties = [
    Expression.property("first"),
    Expression.property("last"),
    Expression.property("username")
]

let query = QueryBuilder.select(SelectResult.all())
    .from(DataSource.collection(self.collection))
    .where(Expression.string("Armani").in(properties))
```

### [](#lbl-like-ops)Like Operator

In this section

[String Matching](#lbl-string-match) | [Wildcard Match](#lbl-wild-match) | [Wildcard Character Match](#lbl-wild-chars)

#### [](#lbl-string-match)String Matching

The [like(\_:)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-swift/Protocols/ExpressionProtocol.html#/#/s:18CouchbaseLiteSwift18ExpressionProtocolP4likeyAaB%5FpAaB%5FpF) operator can be used for string matching — see [Example 7](#ex-like-case-insensitive)

> [!NOTE]
> The `like` operator performs **case sensitive** matches.  
> To perform case insensitive matching, use `Function.lower` or `Function.upper` to ensure all comparators have the same case, thereby removing the case issue.

This query returns `landmark` type documents where the `name` matches the string "Royal Engineers Museum", regardless of how it is capitalized (so, it selects "royal engineers museum", "ROYAL ENGINEERS MUSEUM" and so on).

Example 7\. Like with case-insensitive matching

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("country"),
        SelectResult.property("name")
    )
    .from(DataSource.collection(self.collection))
    .where(Expression.property("type").equalTo(Expression.string("landmark"))
            .and(Function.lower(Expression.property("name"))
                    .like(Expression.string("royal engineers museum")))
    )
    .limit(Expression.int(10))

do {
    for result in try query.execute() {
        print("name property :: \(result.string(forKey: "name")!)")
    }
}
```

**Note** the use of `Function.lower` to transform `name` values to the same case as the literal comparator.

#### [](#lbl-wild-match)Wildcard Match

We can use `%` sign within a `like` expression to do a wildcard match against zero or more characters. Using wildcards allows you to have some fuzziness in your search string.

In [Example 8](#ex-wldcd-match) below, we are looking for documents of `type` "landmark" where the name property matches any string that begins with "eng" followed by zero or more characters, the letter "e", followed by zero or more characters. Once again, we are using `Function.lower` to make the search case insensitive.

So "landmark" documents with names such as "Engineers", "engine", "english egg" and "England Eagle". Notice that the matches may span word boundaries.

Example 8\. Wildcard Matches

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("country"),
        SelectResult.property("name")
    )
    .from(DataSource.collection(self.collection))
    .where(Expression.property("type").equalTo(Expression.string("landmark"))
            .and(Function.lower(Expression.property("name"))
                    .like(Expression.string("eng%e%")))
    )
    .limit(Expression.int(10))
```

#### [](#lbl-wild-chars)Wildcard Character Match

We can use an `_` sign within a like expression to do a wildcard match against a single character.

In [Example 9](#ex-wldcd-char-match) below, we are looking for documents of type "landmark" where the `name` property matches any string that begins with "eng" followed by exactly 4 wildcard characters and ending in the letter "r". The query returns "landmark" type documents with names such as "Engineer", "engineer" and so on.

Example 9\. Wildcard Character Matching

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("country"),
        SelectResult.property("name")
    )
    .from(DataSource.collection(self.collection))
    .where(Expression.property("type").equalTo(Expression.string("landmark"))
            .and(Expression.property("name").like(Expression.string("eng____r")))
    )
    .limit(Expression.int(10))
```

### [](#lbl-regex-ops)Regex Operator

Similar to the wildcards in `like` expressions, `regex` based pattern matching allow you to introduce an element of fuzziness in your search string — see the code shown in [Example 10](#ex-regex).

> [!NOTE]
> The `regex` operator is case sensitive, use `upper` or `lower` functions to mitigate this if required.

Example 10\. Using Regular Expressions

This example returns documents with a `type` of "landmark" and a `name` property that matches any string that begins with "eng" and ends in the letter "e".

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("name")
    )
    .from(DataSource.collection(self.collection))
    .where(Expression.property("type").equalTo(Expression.string("landmark"))
            .and(Expression.property("name").regex(Expression.string("\\bEng.*e\\b"))) (1)
    )
    .limit(Expression.int(10))
```

| **1** | The \\b specifies that the match must occur on word boundaries. |
| ----- | --------------------------------------------------------------- |

> [!TIP]
> For more on the regex spec used by Couchbase Lite see [cplusplus regex reference page](http://www.cplusplus.com/reference/regex/ECMAScript/)

### [](#lbl-deleted-ops)Deleted Document

You can query documents that have been deleted (tombstones) \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] as shown in [Example 11](#ex-del-qry).

Example 11\. Query to select Deleted Documents

This example shows how to query deleted documents in the database. It returns is an array of key-value pairs.

```swift
// Query documents that have been deleted
let query = QueryBuilder
    .select(SelectResult.expression(Meta.id))
    .from(DataSource.collection(self.collection))
    .where(Meta.isDeleted)
```

## [](#lbl-join)JOIN statement

The JOIN clause enables you to select data from multiple documents that have been linked by criteria specified in the JOIN statement. For example to combine airline details with route details, linked by the airline id — see [Example 12](#ex-join).

Example 12\. Using JOIN to Combine Document Details

This example JOINS the document of type `route` with documents of type `airline` using the document ID (_id) on the \_airline_ document and `airlineid` on the _route_ document. 

```swift
guard let airlines = try self.database.collection(name: "airlines") else { return }
guard let routes = try self.database.collection(name: "routes") else { return }
let query = QueryBuilder
    .select(
        SelectResult.expression(Expression.property("name").from("airline")),
        SelectResult.expression(Expression.property("callsign").from("airline")),
        SelectResult.expression(Expression.property("destinationairport").from("route")),
        SelectResult.expression(Expression.property("stops").from("route")),
        SelectResult.expression(Expression.property("airline").from("route"))
    )
    .from(
        DataSource.collection(airlines).as("airline")
    )
    .join(
        Join.join(DataSource.collection(routes).as("route"))
            .on(
                Meta.id.from("airline")
                    .equalTo(Expression.property("airlineid").from("route"))
            )
    )
    .where(
        Expression.property("type").from("route").equalTo(Expression.string("route"))
            .and(Expression.property("type").from("airline")
                    .equalTo(Expression.string("airline")))
            .and(Expression.property("sourceairport").from("route")
                    .equalTo(Expression.string("RIX")))
    )
```

## [](#lbl-group)GROUP BY statement

You can perform further processing on the data in your result set before the final projection is generated.

The following example looks for the number of airports at an altitude of 300 ft or higher and groups the results by country and timezone.

Data Model for Example

```json
{
    "_id": "airport123",
    "type": "airport",
    "country": "United States",
    "geo": { "alt": 456 },
    "tz": "America/Anchorage"
}
```

Example 13\. Query using GroupBy

This example shows a query that selects all airports with an altitude above 300ft. The output (a count, $1) is grouped by country, within timezone.

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Function.count(Expression.all())),
        SelectResult.property("country"),
        SelectResult.property("tz"))
    .from(DataSource.collection(self.collection))
    .where(
        Expression.property("type").equalTo(Expression.string("airport"))
            .and(Expression.property("geo.alt").greaterThanOrEqualTo(Expression.int(300)))
    ).groupBy(
        Expression.property("country"),
        Expression.property("tz")
    )

do {
    for result in try query.execute() {
        print("""
            There are \(result.int(forKey: "$1")) airports on
                        the \(result.string(forKey: "tz")!)timezone located
                        in \(result.string(forKey: "country")!) and above 300 ft
        """)
    }
}
```

The query shown in [Example 13](#ex-grpby-qry) generates the following output:

There are 138 airports on the Europe/Paris timezone located in France and above 300 ft  
There are 29 airports on the Europe/London timezone located in United Kingdom and above 300 ft  
There are 50 airports on the America/Anchorage timezone located in United States and above 300 ft  
There are 279 airports on the America/Chicago timezone located in United States and above 300 ft  
There are 123 airports on the America/Denver timezone located in United States and above 300 ft

## [](#lbl-order)ORDER BY statement

It is possible to sort the results of a query based on a given expression result — see [Example 14](#ex-orderby-qry)

Example 14\. Query using OrderBy

This example shows a query that returns documents of type equal to "hotel" sorted in ascending order by the value of the title property.

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("title"))
    .from(DataSource.collection(self.collection))
    .where(Expression.property("type").equalTo(Expression.string("hotel")))
    .orderBy(Ordering.property("title").ascending())
    .limit(Expression.int(10))
```

The query shown in [Example 14](#ex-orderby-qry) generates the following output:

```text
Aberdyfi
Achiltibuie
Altrincham
Ambleside
Annan
Ardèche
Armagh
Avignon
```

## [](#lbl-date-time)Date/Time Functions

Couchbase Lite documents support a [date type](#initializers) that internally stores dates in ISO 8601 with the GMT/UTC timezone.

Couchbase Lite’s Query Builder API \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]includes four functions for date comparisons.

`Function.StringToMillis(Expression.Property("date_time"))`

The input to this will be a validly formatted ISO 8601 `date_time` string. The end result will be an expression (with a numeric content) that can be further input into the query builder.

`Function.StringToUTC(Expression.Property("date_time"))`

The input to this will be a validly formatted ISO 8601 `date_time` string. The end result will be an expression (with string content) that can be further input into the query builder.

`Function.MillisToString(Expression.Property("date_time"))`

The input for this is a numeric value representing milliseconds since the Unix epoch. The end result will be an expression (with string content representing the date and time as an ISO 8601 string in the device’s timezone) that can be further input into the query builder.

`Function.MillisToUTC(Expression.Property("date_time"))`

The input for this is a numeric value representing milliseconds since the Unix epoch. The end result will be an expression (with string content representing the date and time as a UTC ISO 8601 string) that can be further input into the query builder.

## [](#lbl-resultsets)Result Sets

In this section

[Processing](#lbl-process-resultset) | [Select All Properties](#lbl-all-sel) | [Select Specific Properties](#lbl-specific-sel) | [Select Document Id Only](#lbl-id-sel) | [Select Count-only](#lbl-count-sel) | [Handling Pagination](#lbl-pagination)

### [](#lbl-process-resultset)Processing

This section shows how to handle the returned result sets for different types of `SELECT` statements.

The result set format and its handling varies slightly depending on the type of SelectResult statements used. The result set formats you may encounter include those generated by :

* SelectResult.all — see: [All Properties](#lbl-all-sel)
* SelectResult.expression(property("name")) — see: [Specific Properties](#lbl-specific-sel)
* SelectResult.expression(meta.id) — Metadata (such as the `_id`) — see: [Document ID Only](#lbl-id-sel)
* SelectResult.expression(Function.count(Expression.all())).as("mycount") — see: [Select Count-only](#lbl-count-sel)

To process the results of a query, you first need to execute it using `Query.execute`.

The execution of a Couchbase Lite for Swift’s database query typically returns an array of results, a result set.

* The result set of an aggregate, count-only, query is a key-value pair — see [Select Count-only](#lbl-count-sel) — which you can access using the count name as its key.
* The result set of a query returning document properties is an array.  
Each array row represents the data from a document that matched your search criteria (the `WHERE` statements) The composition of each row is determined by the combination of `SelectResult` expressions provided in the `SELECT` statement. To unpack these result sets you need to iterate this array.

### [](#lbl-all-sel)Select All Properties

#### [](#query)Query

The `Select` statement for this type of query, returns all document properties for each document matching the query criteria — see [Example 15](#ex-all-qry)

Example 15\. Query selecting All Properties

```swift
let query = QueryBuilder.select(SelectResult.all()).from(DataSource.collection(self.collection))
```

#### [](#result-set-format)Result Set Format

The result set returned by queries using `SelectResult.all` is an array of dictionary objects — one for each document matching the query criteria.

For each result object, the key is the database name and the 'value' is a dictionary representing each document property as a key-value pair — see: [Example 16](#ex-all-rtn).

Example 16\. Format of Result Set (All Properties)

```json
[
  {
    "travel-sample": { (1)
      "callsign": "MILE-AIR",
      "country": "United States",
      "iata": "Q5",
      "icao": "MLA",
      "id": 10,
      "name": "40-Mile Air",
      "type": "airline"
    }
  },
  {
    "travel-sample": { (2)
      "callsign": "ALASKAN-AIR",
      "country": "United States",
      "iata": "AA",
      "icao": "AAA",
      "id": 10,
      "name": "Alaskan Airways",
      "type": "airline"
    }
  }
]
```

| **1** | The result for the first document matching the query criteria. |
| ----- | -------------------------------------------------------------- |
| **2** | The result for the next document matching the query criteria.  |

#### [](#result-set-access)Result Set Access

In this case access the retrieved document properties by converting each row’s value, in turn, to a dictionary — as shown in [Example 17](#ex-all-acc).

Example 17\. Using Document Properties (All)

```swift
results = try query.execute()
for row in results {
    let docsProps = row.dictionary(at: 0)! (1)

    let docid = docsProps.string(forKey: "id")!
    let name = docsProps.string(forKey: "name")!
    let type = docsProps.string(forKey: "type")!
    let city = docsProps.string(forKey: "city")!

    print("\(docid): \(name), \(type), \(city)")
    let hotel = row.dictionary(at: 0)!  (2)
    guard let hotelId = hotel.string(forKey: "id") else {
        continue
    }

    hotels[hotelId] = hotel
}
```

| **1** | The dictionary of document properties using the database name as the key. You can add this dictionary to an array of returned matches, for processing elsewhere in the app. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Alternatively you can access the document properties here, by using the property names as keys to the dictionary object.                                                    |

### [](#lbl-specific-sel)Select Specific Properties

#### [](#query-2)Query

Here we use `SelectResult.expression(property("<property-name>")))` to specify the document properties we want our query to return — see: [Example 18](#ex-specific-qry).

Example 18\. Query selecting Specific Properties

```swift
let query = QueryBuilder
    .select(SelectResult.expression(Meta.id).as("metaId"),
            SelectResult.expression(Expression.property("id")),
            SelectResult.expression(Expression.property("name")),
            SelectResult.expression(Expression.property("city")),
            SelectResult.expression(Expression.property("type")))
    .from(DataSource.collection(self.collection))
```

#### [](#result-set-format-2)Result Set Format

The result set returned when selecting only specific document properties is an array of dictionary objects — one for each document matching the query criteria.

Each result object comprises a key-value pair for each selected document property — see [Example 19](#ex-specific-rtn)

Example 19\. Format of Result Set (Specific Properties)

```json
[
  { (1)
    "id": "hotel123",
    "type": "hotel",
    "name": "Hotel Ghia"
  },
  { (2)
    "id": "hotel456",
    "type": "hotel",
    "name": "Hotel Deluxe",
  }
]
```

| **1** | The result for the first document matching the query criteria. |
| ----- | -------------------------------------------------------------- |
| **2** | The result for the next document matching the query criteria.  |

#### [](#result-set-access-2)Result Set Access

Access the retrieved properties by converting each row into a dictionary — as shown in [Example 20](#ex-specific-acc).

Example 20\. Using Returned Document Properties (Specific Properties)

```swift
for result in try! query.execute() {
    let docID = result.string(forKey: "metaId")!
    print("processing doc: \(docID)")

    let id = result.string(forKey: "id")!
    var hotel = Hotel(id: id)
    hotel.name = result.string(forKey: "name")
    hotel.city = result.string(forKey: "city")
    hotel.type = result.string(forKey: "type")
    hotels[id] = hotel
}
```

### [](#lbl-id-sel)Select Document Id Only

#### [](#query-3)Query

You would typically use this type of query if retrieval of document properties directly would consume excessive amounts of memory and-or processing time — see: [Example 21](#ex-id-qry).

Example 21\. Query selecting only Doc Id

```swift
let collection = try self.database.createCollection(name: "hotel")
let query = QueryBuilder.select(SelectResult.expression(Meta.id).as("metaId"))
    .from(DataSource.collection(self.collection))
```

#### [](#result-set-format-3)Result Set Format

The result set returned by queries using a SelectResult expression of the form `SelectResult.expression(meta.id)` is an array of dictionary objects — one for each document matching the query criteria. Each result object has `id` as the key and the ID value as its value — -see [Example 22](#ex-id-rtn).

Example 22\. Format of Result Set (Doc Id only)

```json
[
  {
    "id": "hotel123"
  },
  {
    "id": "hotel456"
  },
]
```

#### [](#result-set-access-3)Result Set Access

In this case, access the required document’s properties by unpacking the `id` and using it to get the document from the database — see: [Example 23](#ex-id-acc).

Example 23\. Using Returned Document Properties (Document Id)

```swift
let results = try query.execute()
for result in results {

    print(result.toDictionary())

    let docId = result.string(forKey: "metaId")! (1)
    print("Document Id is -- \(docId)")

    // Now you can get the document using the ID
    if let doc = try collection.document(id: docId) {
        let hotelId = doc.string(forKey: "id")!
        let name = doc.string(forKey: "name")!
        let city = doc.string(forKey: "city")!
        let type = doc.string(forKey: "type")!

        // ... process document properties as required
        print("Result properties are: \(hotelId), \(name), \(city), \(type)")
    }
}
```

| **1** | Extract the Id value from the dictionary and use it to get the document from the database |
| ----- | ----------------------------------------------------------------------------------------- |

### [](#lbl-count-sel)Select Count-only

#### [](#query-4)Query

Example 24\. Query selecting a Count-only

```swift
let query = QueryBuilder
    .select(SelectResult.expression(Function.count(Expression.all())).as("mycount"))
    .from (DataSource.collection(self.collection)).groupBy(Expression.property("type"))
```

| **1** | The alias name, mycount, is used to access the count value. |
| ----- | ----------------------------------------------------------- |

#### [](#result-set-format-4)Result Set Format

The result set returned by a count such as `Select.expression(Function.count(Expression.all)))` is a key-value pair. The key is the count name, as defined using `SelectResult.as` — see: [Example 25](#ex-count-rtn) for the format and [Example 24](#ex-count-qry) for the query.

Example 25\. Format of Result Set (Count)

```json
{
  "mycount": 6
}
```

| **1** | The key-value pair returned by a count. |
| ----- | --------------------------------------- |

#### [](#result-set-access-4)Result Set Access

Access the count using its alias name (`mycount` in this example) — see [Example 26](#ex-count-acc)

Example 26\. Using Returned Document Properties (Count)

```swift
for result in try query.execute() {
    let count = result.int(forKey: "mycount") (1)
    print("There are ", count, " rows")
}
```

| **1** | Get the count using the SelectResult.as alias, which is used as its key. |
| ----- | ------------------------------------------------------------------------ |

### [](#lbl-pagination)Handling Pagination

One way to handle pagination in high-volume queries is to retrieve the results in batches. Use the `limit` and `offset` feature, to return a defined number of results starting from a given offset — see: [Example 27](#ex-pagination).

Example 27\. Query Pagination

```swift
let offset = 0;
let limit = 20;

let query = QueryBuilder
    .select(SelectResult.all())
    .from(DataSource.collection(self.collection))
    .limit(Expression.int(limit), offset: Expression.int(offset))
```

| **1** | Return a maximum of limit results starting from result number offset |
| ----- | -------------------------------------------------------------------- |

> [!TIP]
> For more on using the QueryBuilder API, see our blog: [Introducing the Query Interface in Couchbase Mobile](https://blog.couchbase.com/sql-for-json-query-interface-couchbase-mobile/)

## [](#json-result-sets)JSON Result Sets

Couchbase Lite for Swift provides a convenience API to convert query results to JSON strings.

Example 28\. Using JSON Results

Use [result.toJSON()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-swift/Classes/Result.html#/s:18CouchbaseLiteSwift6ResultC6toJSONSSyF) to transform your result string into a JSON string, which can easily be serialized or used as required in your application. See [Example 28](#ex-json) for a working example.

```swift
// In this example the Hotel class is defined using Codable
//
// class Hotel : Codable {
//   var id : String = "undefined"
//   var type : String = "hotel"
//   var name : String = "undefined"
//   var city : String = "undefined"
//   var country : String = "undefined"
//   var description : String? = ""
//   var text : String? = ""
//   ... other class content
// }

results = try query.execute()
for row in  results {

    // get the result into a JSON String
    let jsonString = row.toJSON()

    let thisJsonObj:Dictionary =
    try (JSONSerialization.jsonObject(
        with: jsonString.data(using: .utf8)!,
        options: .allowFragments)
         as? [String: Any])!

    // Use Json Object to populate Native object
    // Use Codable class to unpack JSON data to native object
    var this_hotel: Hotel = try JSONDecoder().decode(Hotel.self, from:jsonString.data(using: .utf8)!) (1)

    // ALTERNATIVELY unpack in steps
    this_hotel.id = thisJsonObj["id"] as! String
    this_hotel.name = thisJsonObj["name"] as? String
    this_hotel.type = thisJsonObj["type"] as? String
    this_hotel.city = thisJsonObj["city"] as? String
    hotels[this_hotel.id] = this_hotel
}
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

## [](#lbl-predquery)Predictive Query

> [!IMPORTANT]
> Enterprise Edition only
> 
> Predictive Query is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

Predictive Query enables Couchbase Lite queries to use machine learning, by providing query functions that can process document data (properties or blobs) via trained ML models.

Let’s consider an image classifier model that takes a picture as input and outputs a label and probability.

![predictive diagram](../_images/predictive-diagram.png) 

To run a predictive query with a model as the one shown above, you must implement the following steps.

1. [Integrate the Model](#integrate-the-model)
2. [Register the Model](#register-the-model)
3. [Create an Index (Optional)](#create-an-index)
4. [Run a Prediction Query](#run-a-prediction-query)
5. [Deregister the Model](#Deregister-the-model)

### [](#integrate-the-model)Integrate the Model

To integrate a model with Couchbase Lite, you must implement the `PredictiveModel` interface which has only one function called `predict()` — see: [Example 29](#int-pred-model).

Example 29\. Integrating a predictive model

```swift
// `myMLModel` is a fake implementation
// this would be the implementation of the ml model you have chosen
class myMLModel {
    static func predictImage(data: Data) -> [String : AnyObject] { return [:] }
}

class ImageClassifierModel: PredictiveModel {
    func predict(input: DictionaryObject) -> DictionaryObject? {
        guard let blob = input.blob(forKey: "photo") else {
            return nil
        }

        let imageData = blob.content!
        // `myMLModel` is a fake implementation
        // this would be the implementation of the ml model you have chosen
        let modelOutput = myMLModel.predictImage(data: imageData)

        let output = MutableDictionaryObject(data: modelOutput)
        return output (1)
    }
}
```

| **1** | The predict(input) -> output method provides the input and expects the result of using the machine learning model. The input and output of the predictive model is a DictionaryObject. Therefore, the supported data type will be constrained by the data type that the DictionaryObject supports. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#register-the-model)Register the Model

To register the model you must create a new instance and pass it to the `Database.prediction.registerModel` static method.

Example 30\. Registering a predictive model

```swift
let model = ImageClassifierModel()
Database.prediction.registerModel(model, withName: "ImageClassifier")
```

### [](#create-an-index)Create an Index

Creating an index for a predictive query is highly recommended. By computing the predictions during writes and building a prediction index, you can significantly improve the speed of prediction queries (which would otherwise have to be computed during reads).

There are two types of indexes for predictive queries:

* [Value Index](#value-index)
* [Predictive Index](#predictive-index)

#### [](#value-index)Value Index

The code below creates a value index from the "label" value of the prediction result. When documents are added or updated, the index will call the prediction function to update the label value in the index.

Example 31\. Creating a value index

```swift
let input = Expression.dictionary(["photo": Expression.property("photo")])
let prediction = Function.prediction(model: "ImageClassifier", input: input)

let index = IndexBuilder.valueIndex(items: ValueIndexItem.expression(prediction.property("label")))
try self.collection.createIndex(index, name: "value-index-image-classifier")
```

#### [](#predictive-index)Predictive Index

Predictive Index is a new index type used for predictive query. It differs from the value index in that it caches the predictive results and creates a value index from that cache when the predictive results values are specified.

Example 32\. Creating a predictive index

Here we create a predictive index from the `label` value of the prediction result.

```swift
let input = Expression.dictionary(["photo": Expression.property("photo")])

let index = IndexBuilder.predictiveIndex(model: "ImageClassifier", input: input)
try self.collection.createIndex(index, name: "predictive-index-image-classifier")
```

### [](#run-a-prediction-query)Run a Prediction Query

The code below creates a query that calls the prediction function to return the "label" value for the first 10 results in the database.

Example 33\. Creating a value index

```swift
let input = Expression.dictionary(["photo": Expression.property("photo")])
let prediction = Function.prediction(model: "ImageClassifier", input: input) (1)

let query = QueryBuilder
    .select(SelectResult.all())
    .from(DataSource.collection(self.collection))
    .where(
        prediction.property("label").equalTo(Expression.string("car"))
            .and(
                prediction.property("probablity")
                    .greaterThanOrEqualTo(Expression.double(0.8))
            )
    )

// Run the query.
do {
    let result = try query.execute()
    print("Number of rows :: \(result.allResults().count)")
} catch {
    fatalError("Error running the query")
}
```

| **1** | The PredictiveModel.predict() method returns a constructed Prediction Function object which can be used further to specify a property value extracted from the output dictionary of the PredictiveModel.predict() function. The null value returned by the prediction method will be interpreted as MISSING value in queries. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#deregister-the-model)Deregister the Model

To deregister the model you must call the `Database.prediction.unregisterModel` static method.

Example 34\. Deregister a value index

```swift
Database.prediction.unregisterModel(withName: "ImageClassifier")
```

### [](#integrate-a-model-with-coremlpredictivemodel)Integrate a Model with CoreMLPredictiveModel

> [!NOTE]
> iOS Only

`CoreMLPredictiveModel` is a Core ML based implementation of the `PredictiveModel` protocol that facilitates the integration of Core ML models with Couchbase Lite.

The following example describes how to load a Core ML model using `CoreMLPredictiveModel`. All other steps (register, indexing, query, unregister) are the same as with a model that is integrated using your own `PredictiveModel` implementation.

```swift
// Load MLModel from `ImageClassifier.mlmodel`
let modelURL = Bundle.main.url(forResource: "ImageClassifier", withExtension: "mlmodel")!
let compiledModelURL = try MLModel.compileModel(at: modelURL)
let model = try MLModel(contentsOf: compiledModelURL)
let predictiveModel = CoreMLPredictiveModel(mlModel: model)

// Register model
Database.prediction.registerModel(predictiveModel, withName: "ImageClassifier")
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
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

---

[1](#%5Ffootnoteref%5F1). Starting in Couchbase Lite 2.5