---
title: QueryBuilder
description: How to use QueryBuilder to build effective queries with Couchbase Lite on C#
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/csharp/pages/querybuilder.adoc
  xref: xref:4.0@couchbase-lite:csharp:querybuilder.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/4.0/csharp/querybuilder.html)

# QueryBuilder

> Description — _How to use QueryBuilder to build effective queries with Couchbase Lite on C#_  
> Related Content — [Predictive Queries](#lbl-predquery) | [Live Queries](query-live.md) | [Indexing](indexing.md)

> [!NOTE]
> The examples used here are based on the _Travel Sample_ app and data introduced in the [Couchbase Mobile Workshop](https://docs.couchbase.com/tutorials/mobile-travel-tutorial/introduction.html) tutorial

## [](#introduction)Introduction

Couchbase Lite for C#.Net provides two ways to build and run database queries; the QueryBuilder API described in this topic and [SQL++ for Mobile](query-n1ql-mobile.md).

Database queries defined with the QueryBuilder API use the query statement format shown in [Example 1](#ex-query-form). The structure and semantics of the query format are based on Couchbase's [SQL++ query language](../../../server/current/learn/data/n1ql-versus-sql.md).

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

```C#
using var query = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Collection(collection));
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

```C#
using var query = QueryBuilder.Select(
    SelectResult.Expression(Meta.ID),
    SelectResult.Property("type"),
    SelectResult.Property("name"))
.From(DataSource.Collection(collection));

foreach (var result in query.Execute()) {
    Console.WriteLine($"Document ID :: {result.GetString("id")}");
    Console.WriteLine($"Document Name :: {result.GetString("name")}");
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

The [Expression Comparators](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.Query.IExpression.html#Couchbase%5FLite%5FQuery%5FIExpression%5F) can be used in the WHERE statement to specify on which property to match documents. In the example below, we use the `equalTo` operator to query documents where the `type` property equals "hotel".

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

```C#
using var query = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Collection(collection))
    .Where(Expression.Property("type").EqualTo(Expression.String("hotel")))
    .Limit(Expression.Int(10));

foreach (var result in query.Execute()) {
    var dict = result.GetDictionary(collection.Name);
    Console.WriteLine($"Document Name :: {dict?.GetString("name")}");
}
```

### [](#lbl-coll-ops)Collection Operators

[ArrayFunction Collection Operators](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.Query.ArrayFunction.html) are useful to check if a given value is present in an array.

#### [](#contains-operator)CONTAINS Operator

The following example uses the `[ArrayFunction](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.Query.ArrayFunction.html)` to find documents where the `public_likes` array property contains a value equal to "Armani Langworth".

```json
{
    "_id": "hotel123",
    "name": "Apple Droid",
    "public_likes": ["Armani Langworth", "Elfrieda Gutkowski", "Maureen Ruecker"]
}
```

```C#
using var query = QueryBuilder.Select(
        SelectResult.Expression(Meta.ID),
        SelectResult.Property("name"),
        SelectResult.Property("public_likes"))
    .From(DataSource.Collection(collection))
    .Where(Expression.Property("type").EqualTo(Expression.String("hotel"))
        .And(ArrayFunction.Contains(Expression.Property("public_likes"),
            Expression.String("Armani Langworth"))));

foreach (var result in query.Execute()) {
    var publicLikes = result.GetArray("public_likes");
    var jsonString = JsonSerializer.Serialize(publicLikes);
    Console.WriteLine($"Public Likes :: {jsonString}");
}
```

#### [](#in-operator)IN Operator

The `IN` operator is useful when you need to explicitly list out the values to test against. The following example looks for documents whose `first`, `last` or `username` property value equals "Armani".

```C#
var values = new IExpression[]
    { Expression.Property("first"), Expression.Property("last"), Expression.Property("username") };

using var query = QueryBuilder.Select(
    SelectResult.All())
    .From(DataSource.Collection(collection))
    .Where(Expression.String("Armani").In(values));

foreach (var result in query.Execute()) {
    var body = result.GetDictionary(0);
    var jsonString = JsonSerializer.Serialize(body);
    Console.WriteLine($"In results :: {jsonString}");
}
```

### [](#lbl-like-ops)Like Operator

In this section

[String Matching](#lbl-string-match) | [Wildcard Match](#lbl-wild-match) | [Wildcard Character Match](#lbl-wild-chars)

#### [](#lbl-string-match)String Matching

The [Like()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.Query.IExpression.html#Couchbase%5FLite%5FQuery%5FIExpression%5FLike%5FCouchbase%5FLite%5FQuery%5FIExpression%5F) operator can be used for string matching — see [Example 7](#ex-like-case-insensitive)

> [!NOTE]
> The `like` operator performs **case sensitive** matches.  
> To perform case insensitive matching, use `Function.lower` or `Function.upper` to ensure all comparators have the same case, thereby removing the case issue.

This query returns `landmark` type documents where the `name` matches the string "Royal Engineers Museum", regardless of how it is capitalized (so, it selects "royal engineers museum", "ROYAL ENGINEERS MUSEUM" and so on).

Example 7\. Like with case-insensitive matching

```C#
using var query = QueryBuilder.Select(
    SelectResult.Expression(Meta.ID),
    SelectResult.Property("name"),
    SelectResult.Property("country"))
    .From(DataSource.Collection(collection))
    .Where(Expression.Property("type").EqualTo(Expression.String("landmark"))
        .And(Function.Lower(Expression.Property("name")).Like(Expression.String("Royal Engineers Museum"))))
    .Limit(Expression.Int(10));

foreach (var result in query.Execute()) {
    Console.WriteLine($"Name Property :: {result.GetString("name")}");
}
```

**Note** the use of `Function.lower` to transform `name` values to the same case as the literal comparator.

#### [](#lbl-wild-match)Wildcard Match

We can use `%` sign within a `like` expression to do a wildcard match against zero or more characters. Using wildcards allows you to have some fuzziness in your search string.

In [Example 8](#ex-wldcd-match) below, we are looking for documents of `type` "landmark" where the name property matches any string that begins with "eng" followed by zero or more characters, the letter "e", followed by zero or more characters. Once again, we are using `Function.lower` to make the search case insensitive.

So "landmark" documents with names such as "Engineers", "engine", "english egg" and "England Eagle". Notice that the matches may span word boundaries.

Example 8\. Wildcard Matches

```C#
using var query = QueryBuilder.Select(
    SelectResult.Expression(Meta.ID),
    SelectResult.Property("name"),
    SelectResult.Property("country"))
    .From(DataSource.Collection(collection))
    .Where(Expression.Property("type").EqualTo(Expression.String("landmark"))
        .And(Function.Lower(Expression.Property("name")).Like(Expression.String("Eng%e%"))))
    .Limit(Expression.Int(10));

foreach (var result in query.Execute()) {
    Console.WriteLine($"Name Property :: {result.GetString("name")}");
}
```

#### [](#lbl-wild-chars)Wildcard Character Match

We can use an `_` sign within a like expression to do a wildcard match against a single character.

In [Example 9](#ex-wldcd-char-match) below, we are looking for documents of type "landmark" where the `name` property matches any string that begins with "eng" followed by exactly 4 wildcard characters and ending in the letter "r". The query returns "landmark" type documents with names such as "Engineer", "engineer" and so on.

Example 9\. Wildcard Character Matching

```C#
using var query = QueryBuilder.Select(
    SelectResult.Expression(Meta.ID),
    SelectResult.Property("name"),
    SelectResult.Property("country"))
    .From(DataSource.Collection(collection))
    .Where(Expression.Property("type").EqualTo(Expression.String("landmark"))
        .And(Expression.Property("name").Like(Expression.String("Royal Eng____rs Museum"))))
    .Limit(Expression.Int(10));

foreach (var result in query.Execute()) {
    Console.WriteLine($"Name Property :: {result.GetString("name")}");
}
```

### [](#lbl-regex-ops)Regex Operator

Similar to the wildcards in `like` expressions, `regex` based pattern matching allow you to introduce an element of fuzziness in your search string — see the code shown in [Example 10](#ex-regex).

> [!NOTE]
> The `regex` operator is case sensitive, use `upper` or `lower` functions to mitigate this if required.

Example 10\. Using Regular Expressions

This example returns documents with a `type` of "landmark" and a `name` property that matches any string that begins with "eng" and ends in the letter "e".

```C#
using var query = QueryBuilder.Select(
    SelectResult.Expression(Meta.ID),
    SelectResult.Property("name"),
    SelectResult.Property("country"))
    .From(DataSource.Collection(collection))
    .Where(Expression.Property("type").EqualTo(Expression.String("landmark"))
        .And(Expression.Property("name").Regex(Expression.String("\\bEng.*e\\b"))))
    .Limit(Expression.Int(10));

foreach (var result in query.Execute()) {
    Console.WriteLine($"Name Property :: {result.GetString("name")}");
}
```

| **1** | The \\b specifies that the match must occur on word boundaries. |
| ----- | --------------------------------------------------------------- |

> [!TIP]
> For more on the regex spec used by Couchbase Lite see [cplusplus regex reference page](http://www.cplusplus.com/reference/regex/ECMAScript/)

### [](#lbl-deleted-ops)Deleted Document

You can query documents that have been deleted (tombstones) \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] as shown in [Example 11](#ex-del-qry).

Example 11\. Query to select Deleted Documents

This example shows how to query deleted documents in the database. It returns is an array of key-value pairs.

```C#
// Query documents that have been deleted
var query = QueryBuilder
    .Select(SelectResult.Expression(Meta.ID))
    .From(DataSource.Collection(collection))
    .Where(Meta.IsDeleted);
```

## [](#lbl-join)JOIN statement

The JOIN clause enables you to select data from multiple documents that have been linked by criteria specified in the JOIN statement. For example to combine airline details with route details, linked by the airline id — see [Example 12](#ex-join).

Example 12\. Using JOIN to Combine Document Details

This example JOINS the document of type `route` with documents of type `airline` using the document ID (_id) on the \_airline_ document and `airlineid` on the _route_ document. 

```C#
using var query = QueryBuilder.Select(
    SelectResult.Expression(Expression.Property("name").From("airline")),
    SelectResult.Expression(Expression.Property("callsign").From("airline")),
    SelectResult.Expression(Expression.Property("destinationairport").From("route")),
    SelectResult.Expression(Expression.Property("stops").From("route")),
    SelectResult.Expression(Expression.Property("airline").From("route")))
    .From(DataSource.Collection(collection).As("airline"))
    .Join(Join.InnerJoin(DataSource.Collection(collection2).As("route"))
        .On(Meta.ID.From("airline").EqualTo(Expression.Property("airlineid").From("route"))))
    .Where(Expression.Property("type").From("route").EqualTo(Expression.String("route"))
        .And(Expression.Property("type").From("airline").EqualTo(Expression.String("airline")))
        .And(Expression.Property("sourceairport").From("route").EqualTo(Expression.String("RIX"))));

foreach (var result in query.Execute()) {
    Console.WriteLine($"Name Property :: {result.GetString("name")}");
}
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

```C#
using var query = QueryBuilder.Select(
    SelectResult.Expression(Function.Count(Expression.All())),
    SelectResult.Property("country"),
    SelectResult.Property("tz"))
    .From(DataSource.Collection(collection))
    .Where(Expression.Property("type").EqualTo(Expression.String("airport"))
        .And(Expression.Property("geo.alt").GreaterThanOrEqualTo(Expression.Int(300))))
    .GroupBy(Expression.Property("country"), Expression.Property("tz"));

foreach (var result in query.Execute()) {
    Console.WriteLine(
        $"There are {result.GetInt("$1")} airports in the {result.GetString("tz")} timezone located in {result.GetString("country")} and above 300 ft");
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

```C#
using var query = QueryBuilder.Select(
    SelectResult.Expression(Meta.ID),
    SelectResult.Property("title"),
    SelectResult.Property("country"))
    .From(DataSource.Collection(collection))
    .Where(Expression.Property("type").EqualTo(Expression.String("hotel")))
    .OrderBy(Ordering.Property("title").Ascending())
    .Limit(Expression.Int(10));

foreach (var result in query.Execute()) {
    Console.WriteLine($"Title :: {result.GetString("title")}");
}
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

Couchbase Lite's Query Builder API \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]includes four functions for date comparisons.

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

The execution of a Couchbase Lite for C#.Net's database query typically returns an array of results, a result set.

* The result set of an aggregate, count-only, query is a key-value pair — see [Select Count-only](#lbl-count-sel) — which you can access using the count name as its key.
* The result set of a query returning document properties is an array.  
Each array row represents the data from a document that matched your search criteria (the `WHERE` statements) The composition of each row is determined by the combination of `SelectResult` expressions provided in the `SELECT` statement. To unpack these result sets you need to iterate this array.

### [](#lbl-all-sel)Select All Properties

#### [](#query)Query

The `Select` statement for this type of query, returns all document properties for each document matching the query criteria — see [Example 15](#ex-all-qry)

Example 15\. Query selecting All Properties

```C#
var database = new Database("hotels");

var query = QueryBuilder
      .Select(SelectResult.All())
      .From(DataSource.Collection(Database!.GetDefaultCollection()));
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

In this case access the retrieved document properties by converting each row's value, in turn, to a dictionary — as shown in [Example 17](#ex-all-acc).

Example 17\. Using Document Properties (All)

```C#
var results = query.Execute().AllResults();
var hotels = new List<Dictionary<string, object?>>();

if (results.Count > 0) {
    foreach (var result in results) {
        // get the result into our dictionary object
        var thisDocsProps = result.GetDictionary("hotels"); (1)

        if (thisDocsProps != null) {
            var docID = thisDocsProps.GetString("id"); (2)
            var docName = thisDocsProps.GetString("name");
            var docCity = thisDocsProps.GetString("city");
            var docType = thisDocsProps.GetString("type");
            var hotel = thisDocsProps.ToDictionary();
            Debug.Assert(hotel != null);
            hotels.Add(hotel);
        }

    }
}
```

| **1** | The dictionary of document properties using the database name as the key. You can add this dictionary to an array of returned matches, for processing elsewhere in the app. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Alternatively you can access the document properties here, by using the property names as keys to the dictionary object.                                                    |

### [](#lbl-specific-sel)Select Specific Properties

#### [](#query-2)Query

Here we use `SelectResult.expression(property("<property-name>")))` to specify the document properties we want our query to return — see: [Example 18](#ex-specific-qry).

Example 18\. Query selecting Specific Properties

```C#
var database = new Database("hotels");

var hotels = new List<Dictionary<string, object?>>();

var query = QueryBuilder.Select(
        SelectResult.Property("type"),
        SelectResult.Property("name"),
        SelectResult.Property("city")).From(DataSource.Collection(Database!.GetDefaultCollection()));
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

```C#
var results = query.Execute().AllResults();
foreach (var result in results) {

    // get the returned array of k-v pairs into a dictionary
    var hotel = result.ToDictionary();

    // add hotel dictionary to list of hotel dictionaries
    hotels.Add(hotel);

    // use the properties of the returned array of k-v pairs directly
    var docType = result.GetString("type");
    var docName = result.GetString("name");
    var docCity = result.GetString("city");

}
```

### [](#lbl-id-sel)Select Document Id Only

#### [](#query-3)Query

You would typically use this type of query if retrieval of document properties directly would consume excessive amounts of memory and-or processing time — see: [Example 21](#ex-id-qry).

Example 21\. Query selecting only Doc Id

```C#
var database = new Database("hotels");

var query = QueryBuilder
        .Select(SelectResult.Expression(Meta.ID).As("this_ID"))
        .From(DataSource.Collection(Database!.GetDefaultCollection()));
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

In this case, access the required document's properties by unpacking the `id` and using it to get the document from the database — see: [Example 23](#ex-id-acc).

Example 23\. Using Returned Document Properties (Document Id)

```C#
var results = query.Execute().AllResults();
foreach (var result in results) {

    var docID = result.GetString("this_ID"); (1)
    Debug.Assert(docID != null);
    var doc = database.GetDefaultCollection().GetDocument(docID);
}
```

| **1** | Extract the Id value from the dictionary and use it to get the document from the database |
| ----- | ----------------------------------------------------------------------------------------- |

### [](#lbl-count-sel)Select Count-only

#### [](#query-4)Query

Example 24\. Query selecting a Count-only

```C#
var database = new Database("hotels");

var query =
  QueryBuilder
    .Select(SelectResult.Expression(Function.Count(Expression.All())).As("mycount")) (1)
    .From(DataSource.Collection(Database!.GetDefaultCollection()));
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

```C#
var results = query.Execute().AllResults();
foreach (var result in results) {
    var numberOfDocs = result.GetInt("mycount"); (1)
}
```

| **1** | Get the count using the SelectResult.as alias, which is used as its key. |
| ----- | ------------------------------------------------------------------------ |

### [](#lbl-pagination)Handling Pagination

One way to handle pagination in high-volume queries is to retrieve the results in batches. Use the `limit` and `offset` feature, to return a defined number of results starting from a given offset — see: [Example 27](#ex-pagination).

Example 27\. Query Pagination

```C#
var database = new Database("hotels");
var limit = 20;
var offset = 0;

// get a count of the number of docs matching the query
var countQuery =
    QueryBuilder
        .Select(SelectResult.Expression(Function.Count(Expression.All())).As("mycount"))
        .From(DataSource.Collection(Database!.GetDefaultCollection()));
var numberOfDocs =
    countQuery.Execute().First().GetInt("mycount");

if (numberOfDocs < limit) {
    limit = numberOfDocs;
}

while (offset < numberOfDocs) {
    var listQuery =
        QueryBuilder
            .Select(SelectResult.All())
            .From(DataSource.Collection(database.GetDefaultCollection()))
            .Limit(Expression.Int(limit), Expression.Int(offset)); (1)

    foreach (var result in listQuery.Execute()) {
        // Display and or process query results batch
    }

    offset += limit;
}
```

| **1** | Return a maximum of limit results starting from result number offset |
| ----- | -------------------------------------------------------------------- |

> [!TIP]
> For more on using the QueryBuilder API, see our blog: [Introducing the Query Interface in Couchbase Mobile](https://blog.couchbase.com/sql-for-json-query-interface-couchbase-mobile/)

## [](#json-result-sets)JSON Result Sets

Couchbase Lite for C#.Net provides a convenience API to convert query results to JSON strings.

Example 28\. Using JSON Results

Use [Result.ToJson()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.Query.Result.html#Couchbase%5FLite%5FQuery%5FResult%5FToJson) to transform your result string into a JSON string, which can easily be serialized or used as required in your application. See [Example 28](#ex-json) for a working example.

```C#
foreach (var result in query.Execute()) {

    // get the result into a JSON String
    var docJSONString = result.ToJSON();

    // Get a native dictionary object using the JSON string
    var dictFromJSONString =
          JsonSerializer.
            Deserialize<Dictionary<string, object>>
              (docJSONString);

    // use the created dictionary
    if (dictFromJSONString != null) {
        var docID = dictFromJSONString["id"].ToString();
        var docName = dictFromJSONString["name"].ToString();
        var docCity = dictFromJSONString["city"].ToString();
        var docType = dictFromJSONString["type"].ToString();
    }

    //Get a custom object using the JSON string
    var hotel = JsonSerializer.Deserialize<Hotel>(docJSONString);

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

Let's consider an image classifier model that takes a picture as input and outputs a label and probability.

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

```C#
// tensorFlowModel is a fake implementation
// this would be the implementation of the ml model you have chosen
internal class TensorFlowModel
{
    public static IDictionary<string, object?>? PredictImage(byte[] data)
    {
        // Do calculations, etc
        return null;
    }
}

internal class ImageClassifierModel : IPredictiveModel
{
    public DictionaryObject? Predict(DictionaryObject input)
    {
        var blob = input.GetBlob("photo");
        if (blob == null) {
            return null;
        }

        var imageData = blob.Content;
        Debug.Assert(imageData != null);
        // tensorFlowModel is a fake implementation
        // this would be the implementation of the ml model you have chosen
        var modelOutput = TensorFlowModel.PredictImage(imageData);
        Debug.Assert(modelOutput != null);
        return new MutableDictionaryObject(modelOutput); (1)
    }
}
```

| **1** | The predict(input) -> output method provides the input and expects the result of using the machine learning model. The input and output of the predictive model is a DictionaryObject. Therefore, the supported data type will be constrained by the data type that the DictionaryObject supports. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#register-the-model)Register the Model

To register the model you must create a new instance and pass it to the `Database.prediction.registerModel` static method.

Example 30\. Registering a predictive model

```C#
var model = new ImageClassifierModel();
Database.Prediction.RegisterModel("ImageClassifier", model);
```

### [](#create-an-index)Create an Index

Creating an index for a predictive query is highly recommended. By computing the predictions during writes and building a prediction index, you can significantly improve the speed of prediction queries (which would otherwise have to be computed during reads).

There are two types of indexes for predictive queries:

* [Value Index](#value-index)
* [Predictive Index](#predictive-index)

#### [](#value-index)Value Index

The code below creates a value index from the "label" value of the prediction result. When documents are added or updated, the index will call the prediction function to update the label value in the index.

Example 31\. Creating a value index

```C#
var index = IndexBuilder.ValueIndex(ValueIndexItem.Property("label"));
collection.CreateIndex("value-index-image-classifier", index);
```

#### [](#predictive-index)Predictive Index

Predictive Index is a new index type used for predictive query. It differs from the value index in that it caches the predictive results and creates a value index from that cache when the predictive results values are specified.

Example 32\. Creating a predictive index

Here we create a predictive index from the `label` value of the prediction result.

```C#
var input = Expression.Dictionary(new Dictionary<string, object>
{
    ["photo"] = Expression.Property("photo")
});

var index = IndexBuilder.PredictiveIndex("ImageClassifier", input);
collection.CreateIndex("predictive-index-image-classifier", index);
```

### [](#run-a-prediction-query)Run a Prediction Query

The code below creates a query that calls the prediction function to return the "label" value for the first 10 results in the database.

Example 33\. Creating a value index

```C#
var input = Expression.Dictionary(new Dictionary<string, object>
{
    ["photo"] = Expression.Property("photo")
});
var prediction = Function.Prediction("ImageClassifier", input); (1)

using var query = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Collection(collection))
    .Where(prediction.Property("label").EqualTo(Expression.String("car"))
        .And(prediction.Property("probability").GreaterThanOrEqualTo(Expression.Double(0.8))));

var result = query.Execute();
Console.WriteLine($"Number of rows: {result.Count()}");
```

| **1** | The PredictiveModel.predict() method returns a constructed Prediction Function object which can be used further to specify a property value extracted from the output dictionary of the PredictiveModel.predict() function. The null value returned by the prediction method will be interpreted as MISSING value in queries. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#deregister-the-model)Deregister the Model

To deregister the model you must call the `Database.prediction.unregisterModel` static method.

Example 34\. Deregister a value index

```C#
Database.Prediction.UnregisterModel("ImageClassifier");
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](#csharp:gs-prereqs.adoc)
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