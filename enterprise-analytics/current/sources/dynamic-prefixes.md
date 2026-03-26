---
title: Design a Location Path
description: To make querying an external data source more efficient, you supply
  a location path that consists of prefixes.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sources/pages/dynamic-prefixes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:enterprise-analytics:sources:dynamic-prefixes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sources/dynamic-prefixes.html)

# Design a Location Path

> To make querying an external data source more efficient, you supply a location path that consists of prefixes. 

By supplying the prefixes, you reduce the number of files that Enterprise Analytics needs to read when you query an external data source.

## [](#about-static-and-dynamic-prefixes)About Static and Dynamic Prefixes

When you create an external collection in Enterprise Analytics, the location path that you provide acts as a filter on the target bucket. The more precise you can be when you define the path, the better your query performance. How you define the path can also affect hosting service costs by decreasing the number of requests to scan files and transfer results.

When you define a location path, you can include:

* Static prefixes, which are the exact names of the prefixes that define a location in your S3 bucket. Using static prefixes results in a full scan of every file found under that prefix or set of prefixes, every time you query the collection.
* Dynamic prefixes, which are placeholders or tokens for the actual path prefixes. You supply the values for these tokens in the `WHERE` clause of your queries. Using dynamic prefixes gives you more flexibility in how you set up your collections, helping you reduce the number of collections that you need to maintain.

A path can include either static or dynamic prefixes or both.

For more information about how you create an external collection, see [Set Up an External Data Source](manage-external.md) or [CREATE an External Collection](../sqlpp/5%5Fddl%5Fexternal.md).

For information about using prefixes in your S3 buckets, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the AWS documentation.

## [](#examples-of-paths-and-queries-for-external-collections)Examples of Paths and Queries for External Collections

A cloud storage bucket `myBucket` contains files in the following locations:

```none
reviews/2021/jan/reviews.json
reviews/2021/feb/reviews.json
reviews/2021/mar/reviews.json
...
reviews/2022/nov/reviews.json
reviews/2022/dec/reviews.json
```

The bucket contains 24 files named `reviews.JSON`, 1 for each month in 2021 and 2022.

These locations, called prefixes (or folders if you use the Amazon S3 console), make the date range covered by a given file easier to find.

Each `reviews.JSON` file contains the following data:

```json
{
  "year" : 2022,
  "month" : "dec",
  "id" : int,
  "date" : "dd/MM/yyyy",
  "propertyName" : "value",
  "comment" : "value",
  "guestName" : "value"
},
```

### [](#example-static-prefixes)Example: Static Prefixes

To query these files as efficiently as possible, you want your collections to include the full path.

Using static prefixes, you create an external collection for each month:

`collection2021jan` with the path `reviews/2021/jan`

`collection2021feb` with the path `reviews/2021/feb`

and so on, until you set up the 24th collection:

`collection2022dec` with the path `reviews/2022/dec`

When you query any 1 of these collections, the collection supplies a precise location, and Enterprise Analytics reads only files found under that complete path.

You may find that querying 24 different collections using these different names is manageable. Over time however, that number will grow as you add a new collection for each month in 2023, 2024, and so on.

In addition, consider a path structure that includes prefixes like `mobile/customer/1` through `mobile/customer/99999999`, representing data for millions of different customers. Setting up individual collections using only static prefixes would result in millions of collections, which would be difficult to manage.

### [](#example-static-prefixes-and-where-clauses)Example: Static Prefixes and WHERE Clauses

Returning to the `reviews.JSON` files, you decide to make collection management easier by creating just 1 collection for the `reviews` path:

`reviewsCollection` with the path `reviews`

When you query this collection, you supply a `WHERE` clause to retrieve a specific set of results.

```SQL++
SELECT *
FROM reviews
WHERE year = 2021 and month = "jan";
```

This query returns the results you were looking for, the reviews from January 2021\. To do so, Enterprise Analytics uses the path defined in the external collection to determine which files to read in the bucket. As a result, this query scans all of the files under the `reviews/` path. The `WHERE year = 2021 and month = "jan"` clause is applied only afterwards, to the data in the files found in `reviews`, to filter the results after all files have been read.

While this approach limits the number of collections that you need to maintain, it does not provide any efficiencies for querying.

If you used this approach for the `mobile/customer/1` through `mobile/customer/99999999` example, every query would read files for millions of customers.

### [](#example-dynamic-prefixes-and-where-clauses)Example: Dynamic Prefixes and WHERE Clauses

Another approach for your `reviews.json` files is to set up a collection that uses dynamic prefixes instead of static prefixes.

Instead of 24 collections with static paths like `reviews/2022/dec`, you set up a single collection:

`reviewsCollection` with the path `reviews/{year:int}/{month:string}`

Dynamic prefixes use the format `{TOKEN_NAME:DATA_TYPE}`, where:

* `TOKEN_NAME` identifies a placeholder. You can supply the name of a data field in the target file, or any other name you find memorable or useful. For information about how the choice of name can affect query results, see [Example: "embed-filter-values": "true" Adds Only](#embed-adds).
* `DATA_TYPE` identifies the value found in that position of the path. Accepts `int`, `double`, or `string`.

When your queries include a `WHERE` clause with values specified for the `year` and `month`, Enterprise Analytics uses them to replace the path tokens before reading the bucket:

```SQL++
-- this query reads every file under reviews, 24 files:
SELECT *
FROM reviews;

-- this query reads every file under the reviews/2022 path, 12 files:
SELECT *
FROM reviews
WHERE year = 2022;

-- this query reads every file under the reviews/2022/dec path, 1 file only:
SELECT *
FROM reviews
WHERE year = 2022 AND month = "dec";
```

By using dynamic prefixes in the collection's path, the `WHERE` clause of each query acts first as a filter on the files to read, and then again as a filter on the results returned from each file.

To use a dynamic prefix for the data in the `mobile/customer/1` through `mobile/customer/99999999` example, you could set up an external collection `customersCollection` with the path `mobile/customer/{customerId:int}`.

and write queries that replace the `customerId` token to filter what needs to be read:

```SQL++
SELECT *
FROM customer
WHERE customerId = SOME_INTEGER;
```

The `WHERE` clause can use the following operators: `=`, `!=`, `<`, `>`, `BETWEEN`, `IN`.

## [](#embed)Adding the Filter Value to Results

When you create an external collection that uses dynamic prefixes, you can include an `embed-filter-values` parameter.

```SQL++
CREATE EXTERNAL COLLECTION reviewsCollection
ON `myBucket`
USING "reviews/{year:int}/{month:string}"
AT myLink
WITH {"format": "json", "embed-filter-values": "true"};
```

The `embed-filter-values` parameter defines whether Enterprise Analytics modifies the objects returned in the query results.

* `"embed-filter-values": "false"` **does not** modify the objects

  * If a data field with the same name as the `TOKEN_NAME` **is not** present, do not include the object in the results.
  * If a data field with the same name **is** present, leave its value unchanged.
* `"embed-filter-values": "true"` **can** modify the objects

  * If a data field with the same name as the `TOKEN_NAME` **is not** present, append it to each object as a new data field. As its value, supply the value found in the path position that the dynamic prefix represents.
  * If a data field with the same name **is** present, overwrite its value with the value found in the path position that the dynamic prefix represents.

The `embed-filter-values` parameter defaults to true.

## [](#examples-of-modified-and-unchanged-results)Examples of Modified and Unchanged Results

The objects in the `reviews.json` documents have the following data fields:

```json
{
  "year" : 2022,
  "month" : "dec",
  "id" : int,
  "date" : "dd/MM/yyyy",
  "propertyName" : "value",
  "comment" : "value",
  "guestName" : "value"
},
```

One of the objects is incomplete and **does not** include a `month` value. Another was misfiled: it includes a month, but it's not `` dec` ``.

```json
{"id" : 1, "year" : 2022, "propertyName" : "El San Juan", "comment" : "value"},
{"id" : 2, "year" : 2022, "month" : "dec", "day": "7", "propertyName" : "San-Severin", "comment" : "value"},
{"id" : 3, "year" : 2022, "month" : "jul", "day": "14", "propertyName" : "The Mark", "comment" : "value"}
```

### [](#example-embed-filter-values-false)Example: `"embed-filter-values": "false"`

With `"embed-filter-values": "false"` defined for the external collection:

```SQL++
SELECT *
FROM reviewsCollection
WHERE year = 2022 AND month = "dec";
```

The query returns only 1 object, with `month = "dec"`, in the results.

{"id" : 2, "year" : 2022, "month" : "dec", "day": "7", "propertyName" : "San-Severin", "comment" : "value"},

The query filters out the 2 objects that do not have `month = "dec"`.

### [](#example-embed-filter-values-true-adds-and-overwrites)Example: `"embed-filter-values": "true"` Adds and Overwrites

With `"embed-filter-values": "true"` defined for the external collection:

SELECT *
FROM reviewsCollection
WHERE year = 2022 AND month = "dec";

This query returns all 3 objects in the results:

{"id" : 1, "year" : 2022, "month" : "dec", "propertyName" : "El San Juan", "comment" : "value"},
{"id" : 2, "year" : 2022, "month" : "dec", "day": "7", "propertyName" : "San-Severin", "comment" : "value"},
{"id" : 3, "year" : 2022, "month" : "dec", "day": "14", "propertyName" : "The Mark", "comment" : "value"}

In these results, all of the objects now include `"month" : "dec"`:

* The object that did not have a value for the `"month"` now includes `"month" : "dec"`.
* The object that had a different value for the `"month"` now has `"month" : "dec"`.

### [](#embed-adds)Example: `"embed-filter-values": "true"` Adds Only

An option to consider is that your dynamic prefixes can have any name. They do not have to match the names of data fields in your files.

You set up your collection with a dynamic prefix token of `"mmm"` instead of `"month"`:

CREATE EXTERNAL COLLECTION reviewsCollection ON myBucket USING "reviews/{year:int}/{mmm:string}" AT myLink WITH {"format": "json", "embed-filter-values": "true"};

A query with a `WHERE year = 2022 AND mmm = "dec"` clause returns all 3 objects in the results:

 {"id" : 1, "year" : 2022, "mmm" : "dec", "propertyName" : "El San Juan", "comment" : "value"},
{"id" : 2, "year" : 2022, "mmm" : "dec", "month" : "dec", "day": "7", "propertyName" : "San-Severin", "comment" : "value"},
{"id" : 3, "year" : 2022, "mmm" : "dec", "month" : "jul", "day": "14", "propertyName" : "The Mark", "comment" : "value"}

In these results all of the objects now include `"mmm" : "dec"`.

* The object that did not include a `"month"` still does not include the `"month"`.
* The object that had a different value for the `"month"` still has that same value.

For additional examples, see [Optimize Performance of External Analytics Collections in Couchbase](https://www.couchbase.com/blog/optimize-performance-of-external-analytics-collections-in-couchbase/).