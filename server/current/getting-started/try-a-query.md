---
title: Run Your First SQL++ Query
description: Now that you have a basic understanding of buckets, scopes and
  collections, and documents, you can try querying them using SQL++, the
  Couchbase Server query language.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/getting-started/pages/try-a-query.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:getting-started:try-a-query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/getting-started/try-a-query.html)

# Run Your First SQL++ Query

> Now that you have a basic understanding of buckets, scopes and collections, and documents, you can try querying them using SQL++, the Couchbase Server query language. 

## [](#about-sql)About SQL++

SQL++ embraces the JSON document model and uses SQL-like syntax. In SQL++, you operate on JSON documents, and the result of your operation is another JSON document. You can run SQL++ queries from the command line, using the [cbq](../cli/cbq-tool.md) tool, or from the Query Workbench in the Couchbase Server Web Console.

A basic SQL++ query has the following parts:

* `SELECT` — The fields of each document to return.
* `FROM` — The data source in which to look.
* `WHERE` — The conditions that the document must satisfy.

In Couchbase Server 7.0 and later, documents are stored in _collections_, which are stored in _scopes_, which are in turn stored in _buckets_ within a _namespace_. The query engine needs to be aware of the full path of the collection. The fully qualified path of a collection has the following format:

`namespace:bucket.scope.collection`

Here's an example of a basic SQL++ query and the JSON document it returns. The following query asks for the country that is associated with the airline _Excel Airways_ in the collection `` default:`travel-sample`.inventory.airline ``.

```sqlpp
SELECT a.country FROM default:`travel-sample`.inventory.airline a
WHERE a.name = "Excel Airways";
```

Note that if any part of the collection path contains a hyphen character, you need to enclose that part of the path with backtick `` ` `` characters. (Also note that with the introduction of scopes and collections, you no longer need to specify the `type` field in your queries.)

The results:

```json
[
    {
        "country": "United Kingdom"
    }
]
```

The country is thus specified as `United Kingdom`.

To save you from having to enter the full path of the collection for every query, you can specify the _query context_ using the SDK, REST, cbq, or the Query Workbench in the Web Console. You can then reference a collection using its relative path. We'll cover this in more detail in the following sections.

## [](#run-cbq)Try the Interactive Query Shell

To run the interactive query shell, `cbq`, open a console window on your computer and enter the following:

```console
bash -c "clear && docker exec -it db sh"
```

Then, navigate to the Couchbase `bin` directory, and start `cbq`:

```console
cd /opt/couchbase/bin
./cbq -u Administrator -p password -engine=http://127.0.0.1:8091/
```

This displays the `cbq` shell prompt, against which you can enter SQL++ commands, specifying your currently installed buckets. For example, the following query returns the different values that are used by the documents in the `airline` collection for the `callsign` field, limiting the number of results to five:

```sqlpp
SELECT a.callsign FROM default:`travel-sample`.inventory.airline a LIMIT 5;
```

The results:

```json
{
    "requestID": "cfc095c5-d23b-4a81-a4b5-990ad445559f",
    "signature": {
        "callsign": "json"
    },
    "results": [
    {
        "callsign": "MILE-AIR"
    },
    {
        "callsign": "TXW"
    },
    {
        "callsign": "atifly"
    },
    {
        "callsign": null
    },
    {
        "callsign": "LOCAIR"
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "3.197119ms",
        "executionTime": "3.086979ms",
        "resultCount": 5,
        "resultSize": 175,
        "serviceLoad": 3
    }
}
```

The results thus contain five `callsign` values. A `callsign` is associated with an `airline`; and `airline` is one of the collections that the `travel-sample` bucket contains.

The following query returns the names of (at a maximum) ten hotels that accept pets, in the city of Medway:

```sqlpp
SELECT h.name FROM default:`travel-sample`.inventory.hotel h
WHERE h.city="Medway" AND h.pets_ok=true LIMIT 10;
```

The results:

```json
{
    "requestID": "4a6035c9-07af-43d1-be3f-0993957739f2",
    "signature": {
        "name": "json"
    },
    "results": [
    {
        "name": "Medway Youth Hostel"
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "16.742672ms",
        "executionTime": "16.624542ms",
        "resultCount": 1,
        "resultSize": 45,
        "serviceLoad": 3
    }
}
```

The following query returns the `name` and `phone` fields for up to 10 documents for hotels in Manchester, where directions are not missing, and orders the results by name:

```sqlpp
SELECT h.name, h.phone FROM default:`travel-sample`.inventory.hotel h
WHERE h.city="Manchester" AND h.directions IS NOT MISSING ORDER BY h.name LIMIT 10;
```

The results:

```json
{
    "requestID": "56781015-c66c-4ceb-9e46-36e90cfa1bae",
    "signature": {
        "name": "json",
        "phone": "json"
    },
    "results": [
    {
        "name": "Hilton Chambers",
        "phone": "+44 161 236-4414"
    },
    {
        "name": "Sachas Hotel",
        "phone": null
    },
    {
        "name": "The Mitre Hotel",
        "phone": "+44 161 834-4128"
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "3.541059ms",
        "executionTime": "3.407636ms",
        "resultCount": 3,
        "resultSize": 217,
        "serviceLoad": 3,
        "sortCount": 3
    }
}
```

In the cbq shell, you can set the _query context_ by setting the `query_context` parameter. For example, the following cbq command sets the query context to `travel-sample.inventory`. (Note that with this command, you don't need to enclose any part of the path with backticks; and the `default:` namespace is always optional.)

```sqlpp
\SET -query_context travel-sample.inventory;
```

Having set the query context, you can now reference a collection using just the collection name.

```sqlpp
SELECT a.country FROM airline a WHERE a.name = "Excel Airways";
```

This query has the same result as the first example query above.

## [](#try-the-query-workbench)Try the Query Workbench

The Couchbase Server Web Console includes the Query Workbench, an interactive tool that lets you compose and execute SQL++ queries. To use the Query Workbench, log into the Couchbase Server Web Console, and then click **Query**:

![The Query Workbench with no query or results](_images/queryWorkbench.png) 

The Query Workbench has three principal areas:

* **Query Editor**: Where you type your SQL++ query.
* **Explore Your Data**: Provides information on the buckets that are currently maintained by your system. Right now, it shows that just one exists; the bucket `travel-sample`.
* **Results**: Shows query results and provides a number of options for their display. To start with, you will use the default option, which is selectable by the **JSON** button, and duly displays results in JSON-format.

Use the Query Workbench to enter the following SQL++ query:

```sqlpp
SELECT a.name FROM `travel-sample`.inventory.airline a WHERE a.callsign = "MILE-AIR";
```

![The Query Editor showing a query](_images/firstQuery.png) 

To execute your query, click **Execute**.

The results now appear in the **Results** panel:

![The Query results showing query results](_images/queryResultsJSON.png) 

As you can see, a single document was found to match your specified criterion — again, it's the document whose `name` value is `40-Mile Air`.

On the Query Workbench, you can set the _query context_ by selecting a bucket and scope from the drop-down at the top right of the Query Editor. You can then reference a collection using just its relative path.

![The Query Workbench showing a query with the query context set](_images/travelSampleQueryContext.png) 

## [](#other-destinations)Other Destinations

* Execute SQL++ queries programmatically using the official Couchbase SDKs:  
[C](../../../c-sdk/current/howtos/n1ql-queries-with-sdk.md) | [.NET](../../../dotnet-sdk/current/howtos/n1ql-queries-with-sdk.md) | [Go](../../../go-sdk/current/howtos/sqlpp-queries-with-sdk.md) | [Java](../../../java-sdk/current/howtos/sqlpp-queries-with-sdk.md) | [Node.js](../../../nodejs-sdk/current/howtos/n1ql-queries-with-sdk.md) | [PHP](../../../php-sdk/current/howtos/n1ql-queries-with-sdk.md) | [Python](#3.0@python-sdk:howtos:n1ql-queries-with-sdk.adoc) | [Scala](../../../scala-sdk/current/howtos/sqlpp-queries-with-sdk.md)
* [SQL++ Query Language Tutorial](https://query-tutorial.couchbase.com/tutorial/#1): Provides interactive web modules where you can learn about SQL++ without having Couchbase Server installed in your own environment. The modules are self-contained and let you modify and run sample queries. The tutorial covers `SELECT` statements in detail, including examples of `JOIN`, `NEST`, `GROUP BY`, and other typical clauses.
* [SQL++ Cheat Sheet](http://docs.couchbase.com/files/Couchbase-N1QL-CheatSheet.pdf): Provides a concise summary of the basic syntax elements of SQL++. Print it out and keep it on your desk where it'll be handy for quick reference.
* [SQL++ Language Reference](../n1ql/n1ql-language-reference/index.md): Describes the SQL++ language structure, including syntax and usage.
* [Couchbase Webinars](https://www.couchbase.com/resources/webinars): Live and recorded presentations by Couchbase engineers and product managers that highlight features and use-cases of Couchbase Server, including SQL++.
* [Couchbase Blog](https://blog.couchbase.com/) for blogs on various topics including architecture, data modeling, latest Couchbase product features, and more.
* [Couchbase Forum](https://forums.couchbase.com/c/n1ql): A community resource where you can ask questions, find answers, and discuss with the Couchbase community.