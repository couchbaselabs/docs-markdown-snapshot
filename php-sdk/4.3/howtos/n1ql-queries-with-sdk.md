---
title: Query
description: You can query for documents in Couchbase using the SQL++ query
  language, a language based on SQL, but designed for structured and flexible
  JSON documents.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.3/modules/howtos/pages/n1ql-queries-with-sdk.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/php-sdk/4.3/howtos/n1ql-queries-with-sdk.html)

# Query

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. Querying can solve typical programming tasks such as finding a user profile by email address, facebook login, or user ID. 

Our query service uses SQL++ (formerly N1QL), which will be fairly familiar to anyone who’s used any dialect of SQL. [Further resources](#additional%5Fresources) for learning about SQL++ are listed at the bottom of the page. Before you get started you may wish to checkout the [SQL++ intro page](#7.1@server:n1ql:n1ql-language-reference/index.adoc), or just dive in with a query against our travel sample data set. In this case, the one thing that you need to know is that in order to make a Bucket queryable, it must have at least one index defined. You can define a _primary_ index on a bucket. When a primary index is defined you can issue non-covered queries on the bucket as well.

Use [cbq](#7.1@server::tools/cbq-shell.html), our interactive Query shell. Open it, and enter the following:

```n1ql
CREATE PRIMARY INDEX ON `travel-sample`
```

or replace _travel-sample_ with a different Bucket name to build an index on a different dataset.

> [!NOTE]
> The default installation places cbq in `/opt/couchbase/bin/` on Linux, `/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/cbq` on OS X, and `C:\Program Files\Couchbase\Server\bin\cbq.exe` on Microsoft Windows.

Note that building indexes is covered in more detail on the [Query concept page](../concept-docs/n1ql-query.md#index-building) — and in the [API Reference](https://docs.couchbase.com/sdk-api/couchbase-php-client/namespaces/couchbase-management.html).

## [](#queries-placeholders)Queries & Placeholders

Placeholders allow you to specify variable constraints for an otherwise constant query. There are two variants of placeholders: postional and named parameters. Positional parameters use an ordinal placeholder for substitution and named parameters use variables. A named or positional parameter is a placeholder for a value in the WHERE, LIMIT or OFFSET clause of a query. Note that both parameters and options are optional.

Positional parameter example:

```php
$options = new QueryOptions();
$options->positionalParameters(["France"]);
// NOTE: string is single-quoted to avoid PHP variable substitutions and pass '$1' as is
$result = $cluster->query('SELECT x.* FROM `travel-sample`.inventory.hotel x WHERE x.`country`=$1 LIMIT 10;', $options);
```

Named parameter example:

```php
$options = new QueryOptions();
$options->namedParameters(['country' => "France"]);
$result = $cluster->query('SELECT x.* FROM `travel-sample`.inventory.hotel x WHERE x.`country`=$country LIMIT 10;', $options);
```

The complete code for this page’s examples can be found [here](https://github.com/couchbase/docs-sdk-php/blob/release/3.2/modules/howtos/examples/query.php:)

## [](#handling-results)Handling Results

In most cases your query will return more than one result, and you may be looking to iterate over those results:

```php
$options = new QueryOptions();
$options->positionalParameters(["France"]);
$result = $cluster->query('SELECT x.* FROM `travel-sample`.inventory.hotel x WHERE x.`country`=$1 LIMIT 10;', $options);

foreach ($result->rows() as $row) {
    printf("Name: %s, Address: %s, Description: %s\n", $row["name"], $row["address"], $row["description"]);
}
```

You can also get metrics for your query. See the [QueryMetaData API docs](https://docs.couchbase.com/sdk-api/couchbase-php-client-3.2.2/classes/Couchbase-QueryMetaData.html#method%5Fmetrics) for further details.

```php
printf("Execution Time: %d\n", $res->metaData()->metrics()['executionTime']);
```

## [](#scan-consistency)Scan Consistency

Setting a staleness parameter for queries, with `scan_consistency`, enables a tradeoff between latency and (eventual) consistency.

* A SQL++ query using the default **Not Bounded** Scan Consistency will not wait for any indexes to finish updating before running the query and returning results, meaning that results are returned quickly, but the query will not return any documents that are yet to be indexed.
* With Scan Consistency set to **RequestPlus**, all document changes and index updates are processed before the query is run. Select this when consistency is always more important than performance.
* For a middle ground, **AtPlus** is a "read your own write" (RYOW) option, which means it just waits for the new documents that you specify to be indexed, rather than an entire index of multiple documents.

ScanConsisteny (RYOW)

```php
$query = 'SELECT x.* FROM `travel-sample`.inventory.hotel x WHERE x.`country`="France" LIMIT 10';
$opts = new QueryOptions();
$opts->scanConsistency(QueryScanConsistency::REQUEST_PLUS);
$res = $cluster->query($query, $opts);
```

## [](#querying-at-scope-level)Querying at Scope Level

It is possible to query off the [Scope level](#7.1@server:learn:data/scopes-and-collections.adoc) _as of Couchbase Server release 7.0 onwards_, using the `query()` method. It takes the statement as a required argument, and then allows additional options if needed.

A complete list of `QueryOptions` can be found in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-QueryOptions.html).

```php
$opts = new QueryOptions();
$opts->namedParameters(['country' => "France"]);

$scope = $bucket->scope("inventory");
$result = $scope->query('SELECT x.* FROM `airline` x WHERE x.`country`=$country LIMIT 10;', $opts);

foreach ($result->rows() as $row) {
    printf("Name: %s, Callsign: %s, Country: %s\n", $row["name"], $row["callsign"], $row["country"]);
}
```

## [](#additional-resources)Additional Resources

> [!NOTE]
> SQL++ is not the only query option in Couchbase. Be sure to check that your use case fits your selection of query service.

The [Server doc SQL++ intro](#7.1@server:n1ql:n1ql-language-reference/index.adoc) introduces up a complete guide to the SQL++ language, including all of the latest additions.

The [SQL++ interactive tutorial](http://query.pub.couchbase.com/tutorial/#1) is a good introduction to the basics of SQL++ use.