---
title: QueryBuilder
description: How to use QueryBuilder to build effective queries with Couchbase Lite on Swift
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/swift/pages/querybuilder.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@couchbase-lite:swift:querybuilder.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/swift/querybuilder.html)

# QueryBuilder

> Description — _How to use QueryBuilder to build effective queries with Couchbase Lite on Swift_  
> Related Content — [Predictive Query](#couchbase-lite:swift:query-predictive.adoc) | [Live Query](../../current/swift/query-live.md) | [Indexing](../../current/swift/indexing.md)

> [!NOTE]
> The examples used in this topic are based on the _Travel Sample_ app and data introduced in the [Couchbase Mobile Workshop](https://docs.couchbase.com/tutorials/mobile-travel-sample/introduction.html) tutorial

## [](#introduction)Introduction

Couchbase Lite for Swift's database queries are defined using the QueryBuilder API. This uses query statements of the form shown in [Example 1](#ex-query-form). The structure and semantics of the query format are based on that of Couchbase's [N1QL query language](../../../server/current/learn/data/n1ql-versus-sql.md).

Example 1\. Query Format

```SQL
SELECT ____ (1)
FROM 'database' (2)
WHERE ____, (3)
JOIN ____ (4)
GROUP BY ____ (5)
ORDER BY ____ (6)
```

Query Components

| **1** | The [SELECT statement](#lbl-select) specifies the document properties that will be returned in the result set                                                 |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | FROM specifies the database to query the documents from                                                                                                       |
| **3** | [WHERE statement](#lbl-where) specifies the query criteria.The \`SELECT\`ed properties of documents matching this criteria will be returned in the result set |
| **4** | [JOIN statement](#lbl-join) specifies the criteria for joining multiple documents                                                                             |
| **5** | [GROUP BY statement](#lbl-group) specifies the criteria used to group returned items in the result set                                                        |
| **6** | [ORDER BY statement](#lbl-order) specifies the criteria used to order the items in the result set                                                             |

> [!TIP]
> We recommend working through the query section of the [Couchbase Mobile Workshop](https://docs.couchbase.com/tutorials/mobile-travel-sample/introduction.html) as a good way to build your skills in this area.

## [](#indexing)Indexing

Before we begin querying documents, let's briefly mention the importance of having a query index. A query can only be fast if there's a pre-existing database index it can search to narrow down the set of documents to examine — see: [Example 2](#ex-indexing), which shows how to create an index and our [Query Troubleshooting](../../current/swift/query-troubleshooting.md) topic.

> [!TIP]
> See the [Indexing](../../current/swift/indexing.md) topic to learn more about indexing.

Example 2\. Creating a New Index

This example creates a new index for the `type` and `name` properties in the [Data Format](#lbl-data-format) shown.

Data Format

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

Code to Create Index

```swift
let index = IndexBuilder.valueIndex(items:
    ValueIndexItem.expression(Expression.property("type")),
    ValueIndexItem.expression(Expression.property("name")))
try database.createIndex(index, withName: "TypeNameIndex")
```

> [!NOTE]
> Every index has to be updated whenever a document is updated, so too many indexes can hurt performance. Thus, good performance depends on designing and creating the _right_ indexes to go along with your queries.

## [](#lbl-select)SELECT statement

In this section

[Return Selected Properties](#lbl-return-properties) | [Return All Properties](#lbl-return-all)

Related

[Handling result sets](#lbl-resultsets)

Use the `SELECT` statement to specify which properties you want to return from the queried documents. You can opt to retrieve entire documents, or just the specific properties you need.

### [](#lbl-return-all)Return All Properties

Use the `SelectResult.all()` method to return all the properties of selected documents — see: [Example 3](#ex-select-all).

Example 3\. Using SELECT to Retrieve All Properties

This query shows how to retrieve all properties from all documents in your database.

```swift
let query = QueryBuilder
    .select(SelectResult.all())
    .from(DataSource.database(database))
```

The query.execute statement returns the results in a dictionary, where the key is the database name — see [Example 4](#ex-return-all).

Example 4\. Return Data Format from SelectResult.all()

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

| **1** | Here we see the result for the first document matching the query criteria. |
| ----- | -------------------------------------------------------------------------- |
| **2** | Here we see the result for the next document matching the query criteria.  |

See: [Result Sets](#lbl-resultsets) for more on processing query results.

### [](#lbl-return-properties)Return Selected Properties

To access only specific properties, specify a comma separated list of `SelectResult` expressions, one for each property, in the select statement of your query — see: [Example 5](#ex-select-properties)

Example 5\. Using SELECT to Retrieve Specific Properties

In this query we retrieve and then print the `_id`, `type` and `name` properties of each document.

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("type"),
        SelectResult.property("name")
    )
    .from(DataSource.database(database))

do {
    for result in try query.execute() {
        print("document id :: \(result.string(forKey: "id")!)")
        print("document name :: \(result.string(forKey: "name")!)")
    }
} catch {
    print(error)
}
```

The `query.execute` statement returns one or more key-value pairs, one for each SelectResult expression, with the property-name as the key — see [Example 6](#ex-return-properties)

Example 6\. Select Result Format

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

| **1** | Here we see the result for the first document matching the query criteria. |
| ----- | -------------------------------------------------------------------------- |
| **2** | Here we see the result for the next document matching the query criteria.  |

See: [Result Sets](#lbl-resultsets) for more on processing query results.

## [](#lbl-where)WHERE statement

In this section

[Comparison Operators](#lbl-comp-ops) | [Collection Operators](#lbl-coll-ops) | [Like Operator](#lbl-like-ops) | [Regex Operator](#lbl-regex-ops) | [Deleted Document](#lbl-deleted-ops)

Like SQL, you can use the `WHERE` statement to choose which documents are returned by your query. The select statement takes in an `Expression`. You can chain any number of Expressions in order to implement sophisticated filtering capabilities.

### [](#lbl-comp-ops)Comparison Operators

The [Expression Comparators](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/Expression.html) can be used in the WHERE statement to specify on which property to match documents. In the example below, we use the `equalTo` operator to query documents where the `type` property equals "hotel".

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

```swift
let query = QueryBuilder
    .select(SelectResult.all())
    .from(DataSource.database(database))
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

[Array Collection Operators](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/ArrayExpression.html) are useful to check if a given value is present in an array.

#### [](#contains-operator)CONTAINS Operator

The following example uses the `[ArrayFunction](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/ArrayFunction.html)` to find documents where the `public_likes` array property contains a value equal to "Armani Langworth".

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
    .from(DataSource.database(database))
    .where(Expression.property("type").equalTo(Expression.string("hotel"))
        .and(ArrayFunction.contains(Expression.property("public_likes"), value: Expression.string("Armani Langworth")))
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
let values = [
    Expression.property("first"),
    Expression.property("last"),
    Expression.property("username")
    ]

QueryBuilder
    .select(SelectResult.all())
    .from(DataSource.database(database))
    .where(Expression.string("Armani").in(values))
```

### [](#lbl-like-ops)Like Operator

In this section

[String Matching](#lbl-string-match) | [Wildcard Match](#lbl-wild-match) | [Wildcard Character Match](#lbl-wild-chars)

#### [](#lbl-string-match)String Matching

The [like(\_:)](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Protocols/ExpressionProtocol.html#/#/s:18CouchbaseLiteSwift18ExpressionProtocolP4likeyAaB%5FpAaB%5FpF) operator can be used for string matching.

The `like` operator performs **case sensitive** matches.  
To perform case insensitive matching, use `Function.lower` or `Function.upper` to ensure all comparators have the same case, thereby removing the case issue.

Example 7\. Case-insensitive Matching

This query returns `landmark` type documents where the `name` matches the string "Royal Engineers Museum", regardless of how it is capitalized (so, it selects "royal engineers museum", "ROYAL ENGINEERS MUSEUM" and so on).

Note the use of `Function.lower` to transform `name` values to the same case as the literal comparator.

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("country"),
        SelectResult.property("name")
    )
    .from(DataSource.database(database))
    .where(Expression.property("type").equalTo(Expression.string("landmark"))
        .and(Function.lower(Expression.property("name")).like(Expression.string("royal engineers museum")))
    )
    .limit(Expression.int(10))

do {
    for result in try query.execute() {
        print("name property :: \(result.string(forKey: "name")!)")
    }
}
```

#### [](#lbl-wild-match)Wildcard Match

We can use `%` sign within a `like` expression to do a wildcard match against zero or more characters. Using wildcards allows you to have some fuzziness in your search string.

In the example below, we are looking for documents of `type` "landmark" where the name property matches any string that begins with "eng" followed by zero or more characters, the letter "e", followed by zero or more characters. Once again, we are using `Function.lower` to make the search case insensitive.

The following query will return "landmark" `type` documents with name matching "Engineers", "engine", "english egg" , "England Eagle" and so on. Notice that the matches may span word boundaries.

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("country"),
        SelectResult.property("name")
    )
    .from(DataSource.database(database))
    .where(Expression.property("type").equalTo(Expression.string("landmark"))
        .and(Function.lower(Expression.property("name")).like(Expression.string("eng%e%")))
    )
    .limit(Expression.int(10))
```

#### [](#lbl-wild-chars)Wildcard Character Match

We can use an `_` sign within a like expression to do a wildcard match against a single character.

In the example below, we are looking for documents of type "landmark" where the `name` property matches any string that begins with "eng" followed by exactly 4 wildcard characters and ending in the letter "r". The following query will return "landmark" `type` documents with the `name` matching "Engineer", "engineer" and so on.

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("country"),
        SelectResult.property("name")
    )
    .from(DataSource.database(database))
    .where(Expression.property("type").equalTo(Expression.string("landmark"))
        .and(Expression.property("name").like(Expression.string("eng____r")))
    )
    .limit(Expression.int(10))
```

### [](#lbl-regex-ops)Regex Operator

Similar to the wildcards in `like` expressions, `regex` based pattern matching allow you to introduce an element of fuzziness in your search string.

**Note** though, that the `regex` operator is case sensitive.

> [!TIP]
> For more on the regex spec used by Couchbase Lite see [cplusplus regex reference page](http://www.cplusplus.com/reference/regex/ECMAScript/)

The code shown in [Example 8](#ex-regex) executes a query that will return documents of type "landmark" with a name matching "Engine", "engine" and so on.

Example 8\. Using Regular Expressions

This example returns documents with a `type` of "landmark" and a `name` property that matches any string that begins with "eng" and ends in the letter "e".

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("name")
    )
    .from(DataSource.database(database))
    .where(Expression.property("type").equalTo(Expression.string("landmark"))
        .and(Expression.property("name").regex(Expression.string("\\bEng.*e\\b"))) (1)
    )
    .limit(Expression.int(10))
```

| **1** | The \\b specifies that the match must occur on word boundaries. |
| ----- | --------------------------------------------------------------- |

### [](#lbl-deleted-ops)Deleted Document

You can query documents that have been deleted (tombstones) \[[1](#%5Ffootnotedef%5F1 "View footnote.")\].

Example 9\. Query to select Deleted Documents

This example shows how to query deleted documents in the database. The result set it returns is an array of key-value pairs. One for each document matching the criteria — see [Select Document Id Only](#lbl-id-sel) for how to work with this result set.

```swift
// Query documents that have been deleted
let query = QueryBuilder
    .select(SelectResult.expression(Meta.id))
    .from(DataSource.database(db))
    .where(Meta.isDeleted)
```

## [](#lbl-join)JOIN statement

The JOIN clause enables you to select data from multiple documents that have been linked by criteria specified in the JOIN statement. For example to combine airline details with route details, linked by the airline id — see [Example 10](#ex-join).

Example 10\. Using JOIN to Combine Document Details

This example JOINS the document of type `route` with documents of type `airline` using the document ID (_id) on the \_airline_ document and `airlineid` on the _route_ document. 

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Expression.property("name").from("airline")),
        SelectResult.expression(Expression.property("callsign").from("airline")),
        SelectResult.expression(Expression.property("destinationairport").from("route")),
        SelectResult.expression(Expression.property("stops").from("route")),
        SelectResult.expression(Expression.property("airline").from("route"))
    )
    .from(
        DataSource.database(database!).as("airline")
    )
    .join(
        Join.join(DataSource.database(database!).as("route"))
            .on(
                Meta.id.from("airline")
                    .equalTo(Expression.property("airlineid").from("route"))
        )
    )
    .where(
        Expression.property("type").from("route").equalTo(Expression.string("route"))
            .and(Expression.property("type").from("airline").equalTo(Expression.string("airline")))
            .and(Expression.property("sourceairport").from("route").equalTo(Expression.string("RIX")))
)
```

## [](#lbl-group)GROUP BY statement

You can perform further processing on the data in your result set before the final projection is generated. The following example looks for the number of airports at an altitude of 300 ft or higher and groups the results by country and timezone.

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

Example 11\. Query using GroupBy

This example shows a query that selects all airports with an altitude above 300ft. The output (a count, $1) is grouped by country, within timezone.

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Function.count(Expression.all())),
        SelectResult.property("country"),
        SelectResult.property("tz"))
    .from(DataSource.database(database))
    .where(
        Expression.property("type").equalTo(Expression.string("airport"))
            .and(Expression.property("geo.alt").greaterThanOrEqualTo(Expression.int(300)))
    ).groupBy(
        Expression.property("country"),
        Expression.property("tz")
)

do {
    for result in try query.execute() {
        print("There are \(result.int(forKey: "$1")) airports on the \(result.string(forKey: "tz")!) timezone located in \(result.string(forKey: "country")!) and above 300 ft")
    }
}
```

The query shown in [Example 11](#ex-grpby-qry) generates the following output:

There are 138 airports on the Europe/Paris timezone located in France and above 300 ft  
There are 29 airports on the Europe/London timezone located in United Kingdom and above 300 ft  
There are 50 airports on the America/Anchorage timezone located in United States and above 300 ft  
There are 279 airports on the America/Chicago timezone located in United States and above 300 ft  
There are 123 airports on the America/Denver timezone located in United States and above 300 ft

## [](#lbl-order)ORDER BY statement

It is possible to sort the results of a query based on a given expression result. The example below returns documents of type equal to "hotel" sorted in ascending order by the value of the title property.

Example 12\. Query using OrderBy

```swift
let query = QueryBuilder
    .select(
        SelectResult.expression(Meta.id),
        SelectResult.property("title"))
    .from(DataSource.database(database))
    .where(Expression.property("type").equalTo(Expression.string("hotel")))
    .orderBy(Ordering.property("title").ascending())
    .limit(Expression.int(10))
```

The query shown in [Example 12](#ex-orderby-qry) generates the following output:

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

Couchbase Lite 2.5 adds the ability to run date comparisons in your Couchbase Lite queries. To do so, four functions have been added to the Query Builder API:

`Function.StringToMillis(Expression.Property("date_time"))`

The input to this will be a validly formatted ISO 8601 `date_time` string. The end result will be an expression (with a numeric content) that can be further input into the query builder.

`Function.StringToUTC(Expression.Property("date_time"))`

The input to this will be a validly formatted ISO 8601 `date_time` string. The end result will be an expression (with string content) that can be further input into the query builder.

`Function.MillisToString(Expression.Property("date_time"))`

The input for this is a numeric value representing milliseconds since the Unix epoch. The end result will be an expression (with string content representing the date and time as an ISO 8601 string in the device's timezone) that can be further input into the query builder.

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

The execution of a Couchbase Lite for Swift's database query typically returns an array of results, a result set.

* The result set of an aggregate, count-only, query is a key-value pair — see [Select Count-only](#lbl-count-sel) — which you can access using the count name as its key.
* The result set of a query returning document properties is an array.  
Each array row represents the data from a document that matched your search criteria (the `WHERE` statements) The composition of each row is determined by the combination of `SelectResult` expressions provided in the `SELECT` statement. To unpack these result sets you need to iterate this array.

### [](#lbl-all-sel)Select All Properties

Query

The `Select` statement for this type of query, which returns all document properties for each document matching the query criteria, is fairly straightforward — see [Example 13](#ex-all-qry)

Example 13\. Query selecting All Properties

```swift
        let db = try! Database(name: "hotel")
        var hotels = [String:Any]()
        var hotel:Hotel = Hotel.init()

        let listQuery = QueryBuilder.select(SelectResult.all())
            .from(DataSource.database( db))
```

Result Set Format

The result set returned by queries using `SelectResult.all` is an array of dictionary objects — one for each document matching the query criteria.

For each result object, the key is the database name and the 'value' is a dictionary representing each document property as a key-value pair — see: [Example 14](#ex-all-rtn).

Example 14\. Format of Result Set (All Properties)

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

| **1** | Here we see the result for the first document matching the query criteria. |
| ----- | -------------------------------------------------------------------------- |
| **2** | Here we see the result for the next document matching the query criteria.  |

Result Set Access

In this case access the retrieved document properties by converting each row's value, in turn, to a dictionary — as shown in [Example 15](#ex-all-acc).

Example 15\. Using Document Properties (All)

```swift
        do {

            for row in try! listQuery.execute() {

                let thisDocsProps =
                    row.dictionary(at: 0)?.toDictionary() (1)

                let docid = thisDocsProps!["id"] as! String

                let name = thisDocsProps!["name"] as! String

                let type = thisDocsProps!["type"] as! String

                let city = thisDocsProps!["city"] as! String

                let hotel = row.dictionary(at: 0)?.toDictionary()  (2)

                let hotelId = hotel!["id"] as! String

                hotels[hotelId] = hotel

            } // end for

        } //end do-block
```

| **1** | Here we get the dictionary of document properties using the database name as the key. You can add this dictionary to an array of returned matches, for processing elsewhere in the app. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Alternatively you can access the document properties here, by using the property names as keys to the dictionary object.                                                                |

### [](#lbl-specific-sel)Select Specific Properties

Query

Here we use `SelectResult.expression(property("<property-name>")))` to specify the document properties we want our query to return — see: [Example 16](#ex-specific-qry).

Example 16\. Query selecting Specific Properties

```swift
        let db = try! Database(name: "hotel")
        var hotels = [String:Any]()
        var hotel:Hotel = Hotel.init()

        let listQuery = QueryBuilder
            .select(SelectResult.expression(Meta.id).as("metaId"),
                    SelectResult.expression(Expression.property("id")),
                    SelectResult.expression(Expression.property("name")),
                    SelectResult.expression(Expression.property("city")),
                    SelectResult.expression(Expression.property("type")))
                    .from(DataSource.database(db))
```

Result Set Format

The result set returned when selecting only specific document properties is an array of dictionary objects — one for each document matching the query criteria.

Each result object comprises a key-value pair for each selected document property — see [Example 17](#ex-specific-rtn)

Example 17\. Format of Result Set (Specific Properties)

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

| **1** | Here we see the result for the first document matching the query criteria. |
| ----- | -------------------------------------------------------------------------- |
| **2** | Here we see the result for the next document matching the query criteria.  |

Result Set Access

Access the retrieved properties by converting each row into a dictionary — as shown in [Example 18](#ex-specific-acc).

Example 18\. Using Returned Document Properties (Specific Properties)

```swift
        for (_, result) in try! listQuery.execute().enumerated() {


            let thisDoc = result.toDictionary() as? [String:Any]  (1)
                // Store dictionary data in hotel object and save in array
            hotel.id = thisDoc!["id"] as! String
            hotel.name = thisDoc!["name"] as! String
            hotel.city = thisDoc!["city"] as! String
            hotel.type = thisDoc!["type"] as! String
            hotels[hotel.id] = hotel

            // Use result content directly
            let docid = result.string(forKey: "metaId")
            let hotelId = result.string(forKey: "id")
            let name = result.string(forKey: "name")
            let city = result.string(forKey: "city")
            let type = result.string(forKey: "type")

            // ... process document properties as required
            print("Result properties are: ", docid, hotelId,name, city, type)
          } // end for
```

### [](#lbl-id-sel)Select Document Id Only

Query

You would typically use this type of query if retrieval of document properties directly would consume excessive amounts of memory and-or processing time — see: [Example 19](#ex-id-qry).

Example 19\. Query selecting only Doc Id

```swift
        let db = try! Database(name: "hotel")
        let listQuery = QueryBuilder.select(SelectResult.expression(Meta.id).as("metaId"))
                    .from(DataSource.database(db))
```

Result Set Format

The result set returned by queries using a SelectResult expression of the form `SelectResult.expression(meta.id)` is an array of dictionary objects — one for each document matching the query criteria. Each result object has `id` as the key and the ID value as its value — -see [Example 20](#ex-id-rtn).

Example 20\. Format of Result Set (Doc Id only)

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

Result Set Access

In this case, access the required document's properties by unpacking the `id` and using it to get the document from the database — see: [Example 21](#ex-id-acc).

Example 21\. Using Returned Document Properties (Document Id)

```swift
        for (_, result) in try! listQuery.execute().enumerated() {

            print(result.toDictionary())
            print("Document Id is -- ", result["metaId"].string!)

            let thisDocsId = result["metaId"].string! (1)

            // Now you can get the document using the ID
            var thisDoc = db.document(withID: thisDocsId)!.toDictionary()

            let hotelId = thisDoc["id"] as! String

            let name = thisDoc["name"] as! String

            let city = thisDoc["city"] as! String

            let type = thisDoc["type"] as! String

            // ... process document properties as required
            print("Result properties are: ", hotelId,name, city, type)


        } // end for
```

| **1** | Extract the Id value from the dictionary and use it to get the document from the database |
| ----- | ----------------------------------------------------------------------------------------- |

### [](#lbl-count-sel)Select Count-only

Example 22\. Query selecting a Count-only

```swift
        let db = try! Database(name: "hotel")
        do {
            let listQuery = QueryBuilder
                .select(SelectResult.expression(Function.count(Expression.all())).as("mycount"))
                .from (DataSource.database(db)).groupBy(Expression.property("type"))
```

| **1** | The alias name, mycount, is used to access the count value. |
| ----- | ----------------------------------------------------------- |

Result Set Format

The result set returned by a count such as `Select.expression(Function.count(Expression.all)))` is a key-value pair. The key is the count name, as defined using `SelectResult.as` — see: [Example 23](#ex-count-rtn) for the format and [Example 22](#ex-count-qry) for the query.

Example 23\. Format of Result Set (Count)

```json
{
  "mycount": 6
}
```

| **1** | Here we see the key-value pair returned by a count. |
| ----- | --------------------------------------------------- |

Result Set Access

Access the count using its alias name (`mycount` in this example) — see [Example 24](#ex-count-acc)

Example 24\. Using Returned Document Properties (Count)

```swift
            for result in try! listQuery.execute() {
                let dict = result.toDictionary() as? [String: Int]
                let thiscount = dict!["mycount"]! (1)
                print("There are ", thiscount, " rows")
            } // end for

        } // end do

    } // end function
```

| **1** | Get the count using the SelectResult.as alias, which is used as its key. |
| ----- | ------------------------------------------------------------------------ |

### [](#lbl-pagination)Handling Pagination

One way to handle pagination in high-volume queries is to retrieve the results in batches. Use the `limit` and `offset` feature, to return a defined number of results starting from a given offset — see: [Example 25](#ex-pagination).

Example 25\. Query Pagination

```swift
        let thisOffset = 0;
        let thisLimit = 20;
        //
        let listQuery = QueryBuilder
                .select(SelectResult.all())
                .from(DataSource.database(db))
                .limit(Expression.int(thisLimit),
                  offset: Expression.int(thisOffset))
```

| **1** | Return a maximum of limit results starting from result number offset |
| ----- | -------------------------------------------------------------------- |

> [!TIP]
> For more on using the QueryBuilder API, see our blog: [Introducing the Query Interface in Couchbase Mobile](https://blog.couchbase.com/sql-for-json-query-interface-couchbase-mobile/)

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/swift/gs-prereqs.md)
* [Install](../../current/swift/gs-install.md)
* [Build and Run](../../current/swift/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/swift/database.md)
* [Documents](../../current/swift/document.md)
* [Blobs](../../current/swift/blob.md)
* [Remote Sync using Sync Gateway](../../current/swift/replication.md)
* [Handling Data Conflicts](../../current/swift/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

---

[1](#%5Ffootnoteref%5F1). Starting in Couchbase Lite 2.5