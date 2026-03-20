---
title: Read Data and Return Results
description: How to use a SQL++ selection query to read data from a data source
  and return results.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/guides/pages/select.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:guides:select.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/guides/select.html)

# Read Data and Return Results

> How to use a SQL++ selection query to read data from a data source and return results. 

## [](#introduction)Introduction

The [Query Service](../n1ql/query.md) enables you to create, read, update, and delete data by means of [SQL++](../n1ql/n1ql-language-reference/index.md), the Couchbase Server query language. To read data from a data source using SQL++, you must use a selection query; in other words, a query using the `SELECT` statement.

## [](#before-you-begin)Before You Begin

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset.

## [](#query-tools)Query Tools

Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md)  
cbq>
* [Query Workbench](../tools/query-workbench.md)  
![queryTab](../manage/_images/manage-ui/queryTab.png)

## [](#selecting)Selecting

A selection query enables you to read information from a data source, perform operations on the data, and return the results.

To specify what the query should return, use the SELECT clause.

* SQL++
* .NET
* Java
* Node.js
* Python

The following example uses the SELECT clause by itself to evaluate an expression.

Query

```sqlpp
SELECT "Hello world" AS greeting;
```

Result

```json
[
  {
    "greeting": "Hello world"
  }
]
```

The following example uses the `Cluster.QueryAsync<T>` method to execute the query. The result includes each row found.

```csharp
// Call the QueryAsync() function on the scope object and store the result.
var inventoryScope = bucket.Scope("inventory");
var queryResult = await inventoryScope.QueryAsync<dynamic>("SELECT * FROM airline WHERE id = 10");

// Iterate over the rows to access result data and print to the terminal.
await foreach (var row in queryResult) {
    Console.WriteLine(row);
}
```

Click the  View button to see this code in context.

The following example uses the `query()` method to execute the query. The result object includes each row found.

```java
// Call the query() method on the scope object and store the result.
Scope inventoryScope = bucket.scope("inventory");
QueryResult result = inventoryScope.query("SELECT * FROM airline WHERE id = 10;");

// Return the result rows with the rowsAsObject() method and print to the terminal.
System.out.println(result.rowsAsObject());
```

Click the  View button to see this code in context.

The following example uses the `query()` function to execute a query. The result object includes an array of rows found.

```nodejs
// Call the query() function on the cluster object and store the result.
const result = await cluster.query('SELECT "Hello World" as greeting')

// Iterate over the rows to access result data and print to the terminal.
result.rows.forEach((row) => {
  console.log(row)
})
```

Click the  View button to see this code in context.

The following example uses the `query()` function to execute a query. The result object includes an array of rows found.

```python
# Call the query() function on the cluster object and store the result.
result = cluster.query("SELECT \"Hello World\" as greeting")

# Iterate over the rows to access result data and print to the terminal.
for row in result.rows():
    print(row)
```

Click the  View button to see this code in context.

For more information and examples, see [SELECT Clause](../n1ql/n1ql-language-reference/selectclause.md).

## [](#specifying-a-data-source)Specifying a Data Source

To specify the data source for a query, use the FROM clause. For example, to get data from a collection, specify the path to that collection in a FROM clause.

When you specify a FROM clause, you can use the SELECT clause to specify the fields that you want to return from that data source. The set of fields returned by the query is known as the projection.

The following query gets the name and city of every airport.

Query

```sqlpp
SELECT airportname, city
FROM `travel-sample`.inventory.airport;
```

Wrap backticks around the travel-sample dataset because its name contains a hyphen.

Result

```json
[
  {
    "airportname": "Calais Dunkerque",
    "city": "Calais"
  },
  {
    "airportname": "Peronne St Quentin",
    "city": "Peronne"
  },
// ...
]
```

For more information and examples, see [FROM Clause](../n1ql/n1ql-language-reference/from.md).

## [](#query-context)Setting the Query Context

The query context enables you to specify a bucket and scope to resolve partial keyspace references within your queries. When the query context is set, you can specify the data source in your queries using the collection name only. This enhances the portability of your queries.

> [!NOTE]
> The query context is only used to resolve partial keyspace references. When a query specifies a data source using the full path to a keyspace, the query context is not used to resolve that keyspace.

* Query Workbench
* CBQ Shell

To set the query context:

1. Using the **context** controls at the top right of the query editor, open the bucket drop-down menu and select the required bucket.  
When a bucket is selected, a scope drop-down menu is displayed to the right.
2. Open the scope drop-down menu and select the required scope.

![The query context menu with `travel-sample.inventory` selected](../tools/_images/query-workbench-context.png) 

To set the query context, use the `\SET` command with the `query_context` parameter.

---

For example, the following command sets the query context to `travel-sample.inventory`.

```sqlpp
\SET -query_context travel-sample.inventory;
```

Some legacy queries contain keyspace references consisting of the bucket name only, referring to the default collection in the default scope. To specify the data source using the bucket name only, you must unset the query context.

* Query Workbench
* CBQ Shell

To unset the query context, using the **context** controls at the top right of the query editor, open the bucket drop-down menu and select `unset`.

The scope drop-down menu disappears.

![The context controls with the query context unset](../tools/_images/query-workbench-context-unset.png) 

To unset the query context, use `\UNSET` command with the `query_context` parameter.

---

For example, the following command unsets the query context.

```sqlpp
\UNSET -query_context;
```

For more information and examples, see [Query Context](../n1ql/n1ql-intro/queriesandresults.md#query-context).

## [](#filtering)Filtering

To filter the results of the query, use the WHERE clause to specify a comparison expression. Only records that satisfy the comparison expression are returned.

For example, the following query finds the name and city of every airport in the Anchorage timezone whose altitude is greater than or equal to 2100.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](#query-context).

Query

```sqlpp
SELECT t.airportname, t.city
FROM   airport t
WHERE  tz = "America/Anchorage"
       AND geo.alt >= 2100;
```

Result

```json
[
  {
        "airportname": "Anaktuvuk Pass Airport",
        "city": "Anaktuvuk Pass",
  }
]
```

For more information and examples, see [WHERE Clause](../n1ql/n1ql-language-reference/where.md).

## [](#limiting-results)Limiting Results

To limit the number of documents returned by a query, use the `LIMIT` clause.

For example, the following query finds only 2 hotels with an empty room.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](#query-context).

Query

```sqlpp
SELECT name, address, city, country, url
FROM hotel
WHERE vacancy = true
LIMIT 2;
```

Result

```json
[
  {
    "address": "Capstone Road, ME7 3JE",
    "city": "Medway",
    "country": "United Kingdom",
    "name": "Medway Youth Hostel",
    "url": "http://www.yha.org.uk"
  },
  {
    "address": "6 rue aux Juifs",
    "city": "Giverny",
    "country": "France",
    "name": "The Robins",
    "url": "http://givernyguesthouse.com/robin.htm"
  }
]
```

For more information and examples, see [LIMIT Clause](../n1ql/n1ql-language-reference/limit.md).

## [](#ordering-results)Ordering Results

To sort the documents in the resultset by one or more fields, use the `ORDER BY` clause.

For example, the following query lists cities in descending order and then landmarks in ascending order.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](#query-context).

Query

```sqlpp
SELECT city, name
FROM landmark
ORDER BY city DESC, name ASC
LIMIT 5;
```

Results:

```json
[
  {
    "city": "Évreux",
    "name": "Cafe des Arts"
  },
  {
    "city": "Épinal",
    "name": "Marché Couvert (covered market)"
  },
  {
    "city": "Épinal",
    "name": "Musée de l'Image/Imagerie d'Épinal"
  },
  {
    "city": "Yosemite Valley",
    "name": "Lower Yosemite Fall"
  },
  {
    "city": "Yosemite Valley",
    "name": "Mirror Lake/Meadow"
  }
]
```

For more information and examples, see [ORDER BY Clause](../n1ql/n1ql-language-reference/orderby.md).

## [](#related-links)Related Links

In-depth explanation:

* [SELECT](../n1ql/n1ql-language-reference/selectintro.md)

Reference:

* [SELECT Syntax](../n1ql/n1ql-language-reference/select-syntax.md)

Tutorials:

* [SQL++ Query Language Tutorial](https://query-tutorial.couchbase.com/tutorial/#1)

Querying with SDKs:

* [C](../../../c-sdk/current/howtos/n1ql-queries-with-sdk.md)| [C++](../../../cxx-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [.NET](../../../dotnet-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Go](../../../go-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Java](../../../java-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Node.js](../../../nodejs-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Kotlin](../../../kotlin-sdk/current/howtos/n1ql-queries.md)| [PHP](../../../php-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Python](../../../python-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Ruby](../../../ruby-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Rust](../../../rust-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Scala](../../../scala-sdk/current/howtos/sqlpp-queries-with-sdk.md)