[View original HTML](/ruby-sdk/current/howtos/n1ql-queries-with-sdk.html)

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. Querying can solve typical programming tasks such as finding a user profile by email address, facebook login, or user ID. 

Our query service uses SQL++ (formerly N1QL), which will be fairly familiar to anyone who’s used any dialect of SQL. [Further resources](#additional%5Fresources) for learning about SQL++ are listed at the bottom of the page. Before you get started you may wish to checkout the [SQL++ intro page](../../../server/current/n1ql/n1ql-language-reference/index.md), or just dive in with a query against our travel sample data set. In this case, the one thing that you need to know is that in order to make a Bucket queryable, it must have at least one index defined. You can define a _primary_ index on a bucket. When a primary index is defined you can issue non-covered queries on the bucket as well.

Use [cbq](#8.0@server::tools/cbq-shell.html), our interactive Query shell. Open it, and enter the following:

```n1ql
CREATE PRIMARY INDEX ON `travel-sample`
```

or replace _travel-sample_ with a different Bucket name to build an index on a different dataset.

|  | The default installation places cbq in /opt/couchbase/bin/ on Linux, /Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/cbq on OS X, and C:\\Program Files\\Couchbase\\Server\\bin\\cbq.exe on Microsoft Windows. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Note that building indexes is covered in more detail on the [Query concept page](../concept-docs/n1ql-query.md#index-building) — and in the [API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/QueryIndex.html).

## [](#a-simple-query)A Simple Query

Here’s the basics of how to run a simple query to fetch 10 random rows from travel-sample and print the results:

```ruby
options = Cluster::QueryOptions.new
options.metrics = true
result = cluster.query('SELECT * FROM `travel-sample` LIMIT 10', options)
result.rows.each do |row|
  puts row
end
#=>
# {"travel-sample"=>{"callsign"=>"MILE-AIR", "country"=>"United States", "iata"=>"Q5", "icao"=>"MLA", "id"=>10, "name"=>"40-Mile Air", "type"=>"airline"}}
# {"travel-sample"=>{"callsign"=>"TXW", "country"=>"United States", "iata"=>"TQ", "icao"=>"TXW", "id"=>10123, "name"=>"Texas Wings", "type"=>"airline"}}
# ...

puts "Reported execution time: #{result.meta_data.metrics.execution_time}"
#=> Reported execution time: 11.377766ms
```

A query is always performed at the `Cluster` level, using the `query()` method. It takes the statement as a required argument and then allows additional options if needed.

A complete list of `QueryOptions` can be found in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Options/Query.html). Here we pass `readonly` to explicitly mark a query as being read only, and not mutating any documents on the server side.

```ruby
options = Cluster::QueryOptions.new
options.readonly = true
cluster.query(
    'SELECT COUNT(*) AS airport_count FROM `travel-sample` WHERE type = "airport"',
    options)
```

## [](#queries-placeholders)Queries & Placeholders

Placeholders allow you to specify variable constraints for an otherwise constant query. There are two variants of placeholders: _postional_ and _named_ parameters. Positional parameters use an ordinal placeholder for substitution and named parameters use variables. A named or positional parameter is a placeholder for a value in the WHERE, LIMIT or OFFSET clause of a query. Note that both parameters and options are optional.

Positional parameter example:

```ruby
options = Cluster::QueryOptions.new
options.positional_parameters(["France"])
result = cluster.query(
    'SELECT COUNT(*) AS airport_count FROM `travel-sample` WHERE type = "airport" AND country = ?',
    options)
puts "Airports in France: #{result.rows.first["airport_count"]}"
#=> Airports in France: 221
```

Named parameter example:

```ruby
options = Cluster::QueryOptions.new
options.named_parameters({"country" => "France"})
result = cluster.query(
    'SELECT COUNT(*) AS airport_count FROM `travel-sample` WHERE type = "airport" AND country = $country',
    options)
puts "Airports in France: #{result.rows.first["airport_count"]}"
#=> Airports in France: 221
```

## [](#the-query-result)The Query Result

When performing a query, the response you receive is a `QueryResult`. If no exception gets raised the request succeeded and provides access to both the rows returned and also associated `QueryMetaData`.

```ruby
options = Cluster::QueryOptions.new
options.client_context_id = "user-44-#{rand}"
result = cluster.query(
    'SELECT COUNT(*) AS airport_count FROM `travel-sample` WHERE type = "airport"',
    options)
puts "client_context_id: #{result.meta_data.client_context_id}"
#=> client_context_id: user-44-0.9899233780544747
```

The `QueryMetaData` provides insight into some basic profiling/timing information as well as information like the `clientContextId`.

__Table 1\. QueryMetaData__
| Name                         | Description                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------- |
| String #request\_Id          | Returns the request identifer string of the query request.                                  |
| String #client\_context\_id  | Returns the context ID either generated by the SDK or supplied by the user.                 |
| Symbol #status               | Returns raw query execution status as returned by the query engine.                         |
| QueryMetrics #metrics        | Metrics as returned by the query engine, if enabled.                                        |
| Hash #signature              | Returns the signature as returned by the query engine which is then decoded as JSON object. |
| List<QueryWarning> #warnings | Non-fatal errors are available to consume as warnings on this method.                       |
| Hash #profile                | If enabled returns additional profiling information of the query.                           |

For example, here is how you can print the `executionTime` of a query:

```ruby
options = Cluster::QueryOptions.new
options.metrics = true
result = cluster.query(
    'SELECT COUNT(*) AS airport_count FROM `travel-sample` WHERE type = "airport"',
    options)
puts "Reported execution time: #{result.meta_data.metrics.execution_time}"
#=> Reported execution time: 2.516245ms
```

## [](#scan-consistency)Scan Consistency

Setting a staleness parameter for queries, with `scan_consistency`, enables a tradeoff between latency and (eventual) consistency.

* A SQL++ query using the default **Not Bounded** Scan Consistency will not wait for any indexes to finish updating before running the query and returning results, meaning that results are returned quickly, but the query will not return any documents that are yet to be indexed.
* With Scan Consistency set to **request\_plus**, all document changes and index updates are processed before the query is run. Select this when consistency is always more important than performance.
* For a middle ground, **AtPlus** is a "read your own write" (RYOW) option, which means it just waits for the new documents that you specify to be indexed, rather than an entire index of multiple documents.

ScanConsisteny (request\_plus)

```ruby
options = Cluster::QueryOptions.new
options.scan_consistency = :request_plus
result = cluster.query(
    'SELECT COUNT(*) AS airport_count FROM `travel-sample` WHERE type = "airport"',
    options)
puts "Airports in the database: #{result.rows.first["airport_count"]}"
#=> Airports in the database: 1968
```

## [](#querying-at-scope-level)Querying at Scope Level

It is possible to query off the [Scope level](../../../server/current/learn/data/scopes-and-collections.md), using the `query()` method. It takes the statement as a required argument, and then allows additional options if needed.

The code snippet below shows how to run a simple query to fetch 10 random rows from travel-sample and print the results, the assumption is that the `airline` collection exists within a scope `us`.

```ruby
bucket = cluster.bucket("travel-sample")

myscope = bucket.scope("us")
mycollection = "airline"

options = Couchbase::Cluster::QueryOptions.new
options.metrics = true
result = myscope.query("SELECT * FROM #{mycollection} LIMIT 10", options)
result.rows.each do |row|
  puts row
end
puts "Reported execution time: #{result.meta_data.metrics.execution_time}"

#=>
#{"airline"=>{"callsign"=>"TXW", "iata"=>"TQ", "icao"=>"TXW", "name"=>"Texas Wings"}}
#{"airline"=>{"callsign"=>"SASQUATCH", "iata"=>"K5", "icao"=>"SQH", "name"=>"SeaPort Airlines"}}

#Reported execution time: 3.620224ms
```

A complete list of `QueryOptions` can be found in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Options/Query.html).

## [](#additional-resources)Additional Resources

|  | SQL++ is not the only query option in Couchbase. Be sure to check that your [use case](../concept-docs/data-services.md#use-cases) fits your selection of query service. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

For a deeper dive into SQL++ from the SDK, refer to our [SQL++ SDK concept doc](../concept-docs/n1ql-query.md).

The [Server doc SQL++ intro](../../../server/current/n1ql/n1ql-language-reference/index.md) introduces up a complete guide to the SQL++ language, including all of the latest additions.

The [SQL++ interactive tutorial](http://query.pub.couchbase.com/tutorial/#1) is a good introduction to the basics of SQL++ use.