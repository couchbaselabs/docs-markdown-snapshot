---
title: Query
description: You can query for documents in Couchbase using the SQL++ query
  language, a language based on SQL, but designed for structured and flexible
  JSON documents.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/release/2.7/modules/howtos/pages/n1ql-queries-with-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.7@go-sdk:howtos:n1ql-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.7/howtos/n1ql-queries-with-sdk.html)

# Query

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. Querying can solve typical programming tasks such as finding a user profile by email address, facebook login, or user ID. 

Our query service uses [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql), which will be fairly familiar to anyone who's used any dialect of SQL. [Further resources](#<em>additional%5Fresources) for learning about SQL++ are listed at the bottom of the page. Before you get started you may wish to checkout the [SQL++ intro page](#7.1@server:n1ql:n1ql-language-reference/index.adoc), or just dive in with a query against our travel sample data set. In this case, the one thing that you need to know is that in order to make a Bucket queryable, it must have at least one index defined. You can define a \_primary index on a bucket. When a primary index is defined you can issue non-covered queries on the bucket as well.

Use [cbq](#7.1@server::tools/cbq-shell.html), our interactive Query shell. Open it, and enter the following:

```sqlpp
CREATE PRIMARY INDEX ON `travel-sample`
```

or replace _travel-sample_ with a different Bucket name to build an index on a different dataset.

> [!NOTE]
> The default installation places cbq in `/opt/couchbase/bin/` on Linux, `/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/cbq` on OS X, and `C:\Program Files\Couchbase\Server\bin\cbq.exe` on Microsoft Windows.

Note that building indexes is covered in more detail on the [Query concept page](../concept-docs/n1ql-query.md#index-building) — and in the [API Reference](https://pkg.go.dev/github.com/couchbase/gocb/v2#CollectionQueryIndexManager).

## [](#getting-started)Getting Started

After familiarizing yourself with the basics on how the SQL++ query language works and how to query it from the UI you can use it from the Go SDK. Here's a complete example of doing an query and handling the results:

```golang
	opts := gocb.ClusterOptions{
		Authenticator: gocb.PasswordAuthenticator{
			Username: "Administrator",
			Password: "password",
		},
	}
	cluster, err := gocb.Connect("localhost", opts)
	if err != nil {
		panic(err)
	}

	// For Server versions 6.5 or later you do not need to open a bucket here
	b := cluster.Bucket("travel-sample")

	// We wait until the bucket is definitely connected and setup.
	// For Server versions 6.5 or later if we hadn't opened a bucket then we could use cluster.WaitUntilReady here.
	err = b.WaitUntilReady(5*time.Second, nil)
	if err != nil {
		panic(err)
	}

	results, err := cluster.Query("SELECT \"hello\" as greeting;", &gocb.QueryOptions{
		// Note that we set Adhoc to true to prevent this query being run as a prepared statement.
		Adhoc: true,
	})
	if err != nil {
		panic(err)
	}

	var greeting interface{}
	for results.Next() {
		err := results.Row(&greeting)
		if err != nil {
			panic(err)
		}
		fmt.Println(greeting)
	}

	// always check for errors after iterating
	err = results.Err()
	if err != nil {
		panic(err)
	}
```

> [!NOTE]
> When using a Couchbase version < 6.5 you must create a valid Bucket connection using `cluster.Bucket(name)` before you can use SQL++.

Let's break it down. A query is always performed at the `Cluster` level, using the `Query` method. It takes the statement as a required argument and then allows to provide additional options if needed (in the example above, no options are specified).

Once a result returns you can iterate the returned rows and/or access the `QueryMetaData` associated with the query.

## [](#queries-placeholders)Queries & Placeholders

Placeholders allow you to specify variable constraints for an otherwise constant query. There are two variants of placeholders: postional and named parameters. Positional parameters use an ordinal placeholder for substitution and named parameters use variables. A named or positional parameter is a placeholder for a value in the WHERE, LIMIT or OFFSET clause of a query. Note that both parameters and options are optional.

The first example shows how to provide them by name:

```golang
	query := "SELECT x.* FROM `travel-sample`.inventory.hotel x WHERE x.`city`=$city LIMIT 10;"
	params := make(map[string]interface{}, 1)
	params["city"] = "San Francisco"
	rows, err := cluster.Query(query, &gocb.QueryOptions{NamedParameters: params, Adhoc: true})
```

The second example by position:

```golang
	query := "SELECT x.* FROM `travel-sample`.inventory.hotel x WHERE x.`city`=$1 LIMIT 10;"
	rows, err := cluster.Query(query, &gocb.QueryOptions{PositionalParameters: []interface{}{"San Francisco"}, Adhoc: true})
```

What style you choose is up to you, for readability in more complex queries we generally recommend using the named parameters. Note that you cannot use parameters in all positions. If you put it in an unsupported place the server will respond with a `ErrPlanningFailure` or similar.

## [](#the-query-result)The Query Result

When performing a query, the response you receive is a `QueryResult`. If no error is returned then the request succeeded and the result provides access to both the rows returned and also associated `QueryMetaData`.

```golang
	query := "SELECT x.* FROM `travel-sample`.inventory.hotel x LIMIT 10;"
	rows, err := cluster.Query(query, &gocb.QueryOptions{Adhoc: true})
	// check query was successful
	if err != nil {
		panic(err)
	}

	type hotel struct {
		Name string `json:"name"`
	}

	var hotels []hotel
	// iterate over rows
	for rows.Next() {
		var h hotel // this could also just be an interface{} type
		err := rows.Row(&h)
		if err != nil {
			panic(err)
		}
		hotels = append(hotels, h)
	}

	// always check for errors after iterating
	err = rows.Err()
	if err != nil {
		panic(err)
	}
```

There are two places that row iteration can return errors - `result.Row` and `result.Err`. `result.Row` will return an `ErrNoResult` if it is called when there are no rows available. This call will also return an error if there are any json unmarshalling issues. `result.Err` will return any errors that occurred on the stream, it is important to always check this value after iterating.

If you only expect a single result or only want to use the first result in a resultset then you can use `One` (note: this function will iterate any remaining rows in the resultset so can only be called once and should only be used on small resultsets):

```golang
	query := "SELECT x.* FROM `travel-sample`.inventory.hotel x WHERE x.`type`=$1 LIMIT 1;"
	rows, err := cluster.Query(query, &gocb.QueryOptions{PositionalParameters: []interface{}{"hotel"}, Adhoc: true})

	// check query was successful
	if err != nil {
		panic(err)
	}

	var hotel interface{} // this could also be a specific type like Hotel
	err = rows.One(&hotel)
	if err != nil {
		panic(err)
	}
	fmt.Println(hotel)
```

The `QueryMetaData` provides insight into some basic profiling/timing information as well as information like the `ClientContextID`. The `MetaData()` call can only be made once all the query rows have been iterated.

__Table 1\. QueryMetaData__
| Name                      | Description                                                                      |
| ------------------------- | -------------------------------------------------------------------------------- |
| RequestID string          | Returns the request identifer of this request.                                   |
| ClientContextID string    | Returns the context ID either generated by the SDK or supplied by the user.      |
| Status QueryStatus        | An enum simply representing the state of the result.                             |
| Metrics QueryMetrics      | Returns metrics provided by the query for the request if enabled.                |
| Signature interface{}     | If a signature is present, it will be available to consume in a generic fashion. |
| Warnings \[\]QueryWarning | Non-fatal errors are available to consume as warnings on this method.            |
| Profile interface{}       | If enabled returns additional profiling information of the query.                |

For example, here is how you can print the `executionTime` of a query:

```golang
	query := "SELECT x.* FROM `travel-sample`.inventory.airport x LIMIT 10;"
	rows, err := cluster.Query(query, &gocb.QueryOptions{
		Metrics: true,
		Adhoc:   true,
	})
	// check query was successful
	if err != nil {
		panic(err)
	}

	// iterate over rows
	for rows.Next() {
	}

	// always check for errors after iterating
	err = rows.Err()
	if err != nil {
		panic(err)
	}

	metadata, err := rows.MetaData()
	if err != nil {
		panic(err)
	}

	fmt.Printf("Execution Time: %d\n", metadata.Metrics.ExecutionTime)
```

## [](#query-options)Query Options

The query service provides an array of options to customize your query. The following table lists them all:

__Table 2\. Available Query Options__
| Name                                     | Description                                                                         |
| ---------------------------------------- | ----------------------------------------------------------------------------------- |
| ClientContextID string                   | Sets a context ID returned by the service for debugging purposes.                   |
| PositionalParameters \[\]interface{}     | Allows to set positional arguments for a parameterized query.                       |
| NamedParameters map\[string\]interface{} | Allows to set named arguments for a parameterized query.                            |
| Raw interface{}                          | Escape hatch to add arguments that are not covered by these options.                |
| ReadOnly bool                            | Tells the client and server that this query is readonly.                            |
| Adhoc bool                               | If set to false will prepare the query and later execute the prepared statement.    |
| ConsistentWith MutationState             | Allows to be consistent with previously written mutations ("read your own writes"). |
| MaxParallelism uint32                    | Tunes the maximum parallelism on the server.                                        |
| Metrics bool                             | Enables the server to send metrics back to the client as part of the response.      |
| PipelineBatch uint32                     | Sets the batch size for the query pipeline.                                         |
| PipelineCap uint32                       | Sets the cap for the query pipeline.                                                |
| Profile QueryProfileMode                 | Allows to enable additional query profiling as part of the response.                |
| ScanWait time.Duration                   | Allows to specify a maximum scan wait time.                                         |
| ScanCap uint32                           | Specifies a maximum cap on the query scan size.                                     |
| ScanConsistency QueryScanConsistency     | Sets a different scan consistency for this query.                                   |

> [!NOTE]
> Unlike other SDKs the Go SDK defaults to sending queries as [prepared statements](https://docs.couchbase.com/server/current/guides/prep-statements.html). Care should be taken to set `Adhoc` to true for any queries that are not explicitly intended to be prepared.

## [](#scan-consistency)Scan Consistency

By default, the query engine will return whatever is currently in the index at the time of query (this mode is also called `QueryScanConsistencyNotBounded`). If you need to include everything that has just been written, a different scan consistency must be chosen. If `QueryScanConsistencyRequestPlus` is chosen, it will likely take a bit longer to return the results but the query engine will make sure that it is as up-to-date as possible.

```golang
	query := "SELECT x.* FROM `travel-sample`.inventory.hotel x WHERE x.`city`= $1 LIMIT 10"
	rows, err := cluster.Query(query, &gocb.QueryOptions{
		ScanConsistency:      gocb.QueryScanConsistencyRequestPlus,
		PositionalParameters: []interface{}{"San Francisco"},
		Adhoc:                true,
	})
	if err != nil {
		panic(err)
	}
```

### [](#client-context-id)Client Context ID

The SDK will always send a client context ID with each query, even if none is provided by the user. By default a UUID will be generated that is mirrored back from the query engine and can be used for debugging purposes. A custom string can always be provided if you want to introduce application-specific semantics into it (so that for example in a network dump it shows up with a certain identifier). Whatever is chosen, we recommend making sure it is unique so different queries can be distinguished during debugging or monitoring.

### [](#readonly)ReadOnly

If the query is marked as readonly, both the server and the SDK can improve processing of the operation. On the client side, the SDK can be more liberal with retries because it can be sure that there are no state-mutating side-effects happening. The query engine will ensure that actually no data is mutated when parsing and planning the query.

## [](#querying-at-scope-level)Querying at Scope Level

It is possible to query off the [Scope level](#7.1@server:learn:data/scopes-and-collections.adoc) with _Couchbase Server release 7.0_ onwards, using the `scope.Query()` method. It takes the statement as a required argument, and then allows additional options if needed.

The code snippet below shows how to run a simple query to fetch 10 random rows from travel-sample and print the results, the assumption is that the `airline` collection exists within a scope `inventory`.

```golang
	scope := cluster.Bucket("travel-sample").Scope("inventory")
	results, err = scope.Query("SELECT x.* FROM `airline` x LIMIT 10;", &gocb.QueryOptions{})
	// check query was successful
	if err != nil {
		panic(err)
	}

	var airline interface{}
	for results.Next() {
		err := results.Row(&airline)
		if err != nil {
			panic(err)
		}
		fmt.Println(airline)
	}
```

A complete list of `QueryOptions` can be found in the [API docs](https://pkg.go.dev/github.com/couchbase/gocb/v2#Scope.Query).

## [](#additional-resources)Additional Resources

The [Server doc SQL++ intro](#7.1@server:n1ql:n1ql-language-reference/index.adoc) introduces up a complete guide to the SQL++ language, including all of the latest additions.

The [SQL++ interactive tutorial](http://query.pub.couchbase.com/tutorial/#1) is a good introduction to the basics of SQL++ use.