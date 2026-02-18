---
title: Querying with SQL++
description: You can query for documents in Couchbase using the SQL++ query
  language, a language based on SQL, but designed for structured and flexible
  JSON documents.
editUrl: https://github.com/couchbase/docs-columnar-sdk-go/edit/release/1.0/modules/howtos/pages/sqlpp-queries-with-sdk.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/go-columnar-sdk/current/howtos/sqlpp-queries-with-sdk.html)

# Querying with SQL++

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. 

On this page we dive straight into using the Query Service API from the Go Columnar SDK. For a deeper look at the concepts, to help you better understand the Query Service, and the SQL++ language, see the links in the [Further Information](#further-information) section at the end of this page.

Here we show queries against the Travel Sample collection, at cluster and scope level, and give links to information on adding other collections to your data.

## [](#before-you-start)Before You Start

This page assumes that you have [installed the Go Columnar SDK](../hello-world/start-using-sdk.md), added your IP address to the allowlist, and [created a Columnar cluster](../../../analytics/admin/prepare-project.md#cluster).

Create a collection to work upon by [importing the travel-sample dataset](../../../analytics/intro/examples.md#travel-sample) into your cluster.

## [](#querying-your-dataset)Querying Your Dataset

The Go SDK will always return streaming response from the server.

Execute a query:

Scope Level

```go
	scope := cluster.Database("my_database").Scope("my_scope")
	result, err := scope.ExecuteQuery(ctx, "select 1")
	handleErr(err)

	for row := result.NextRow(); row != nil; row = result.NextRow() {
		var content map[string]int

		err = row.ContentAs(&content)
		handleErr(err)

		fmt.Printf("Got row content: %v", content)
	}
```

Cluster Level

```go
	result, err := cluster.ExecuteQuery(ctx, "select 1")
	handleErr(err)

	for row := result.NextRow(); row != nil; row = result.NextRow() {
		var content map[string]int

		err = row.ContentAs(&content)
		handleErr(err)

		fmt.Printf("Got row content: %v", content)
	}
```

### [](#positional-and-named-parameters)Positional and Named Parameters

Supplying parameters as individual arguments to the query allows the query engine to optimize the parsing and planning of the query. You can either supply these parameters by name or by position.

Execute a streaming query with positional arguments:

Positional Parameters

```go
	result, err := cluster.ExecuteQuery(
		ctx,
		"select ?=1",
		cbcolumnar.NewQueryOptions().SetPositionalParameters([]interface{}{1}),
	)
	handleErr(err)
```

Execute a streaming query with named arguments:

Named Parameters

```go
	result, err := cluster.ExecuteQuery(
		ctx,
		"select $foo=1",
		cbcolumnar.NewQueryOptions().SetNamedParameters(map[string]interface{}{"foo": 1}),
	)
	handleErr(err)
```

## [](#query-options)Query Options

The query service provides an array of options to customize your query. The following table lists them all:

__Table 1\. Available Query Options__
| Name                                     | Description                                                                                   |
| ---------------------------------------- | --------------------------------------------------------------------------------------------- |
| NamedParameters map\[string\]interface{} | Allows to set named arguments for a parameterized query.                                      |
| PositionalParameters \[\]interface{}     | Allows to set positional arguments for a parameterized query.                                 |
| Priority bool                            | Allows to set whether this query should be assigned as high priority by the analytics engine. |
| Raw interface{}                          | Escape hatch to add arguments that are not covered by these options.                          |
| ReadOnly bool                            | Tells the client and server that this query is readonly.                                      |
| ScanConsistency QueryScanConsistency     | Sets a different scan consistency for this query.                                             |
| Unmarshaler Unmarshaler                  | Sets a different Unmarshaler for this query.                                                  |

## [](#handling-results)Handling Results

When performing a query, the response you receive is a `QueryResult`. If no error occurs the request succeeded and provides access to both the rows returned and also associated `QueryMetadata`.

Rows are returned through the `NextRow()` function on the result. This function returns a `QueryResultRow` providing access to your data. The data is read using the `ContentAs` function by supplying a pointer to the variable in which to store the value. Always remember to check the error value of `Err` after iterating the results, this is where any errors occurring whilst calling `NextRow` will be returned.

```go
	for row := result.NextRow(); row != nil; row = result.NextRow() {
		var content map[string]int

		err := row.ContentAs(&content)
		handleErr(err)

		fmt.Printf("Got row content: %v", content)
	}

	if err := result.Err(); err != nil {
		handleErr(err)
	}
```

Closing a result stream early can be done by calling the `context.CancelFunc` associated with the `context.Context` provided to `ExecuteQuery`.

### [](#buffered-results)Buffered results

The Go SDK provides a utility function to enable you to buffer all of the results of a query into memory. When using this function there is no need to check the value of `Err` after iterating the results as the function will return an error if one occurs.

```go
	result, err := cluster.ExecuteQuery(ctx, "select 1")
	handleErr(err)

	rows, meta, err := cbcolumnar.BufferQueryResult[map[string]int](result)
	handleErr(err)

	for _, row := range rows {
		fmt.Printf("Got row content: %v", row)
	}

	fmt.Printf("Got meta: %v", meta)
```

### [](#metadata)Metadata

The `QueryMetadata` provides insight into some basic profiling/timing information as well as information like any warnings generated whilst executing the query. Metadata can only be accessed once all rows have been read from the result, early access will result in an error being returned.

__Table 2\. Query MetaData fields__
| Name                      | Description                                            |
| ------------------------- | ------------------------------------------------------ |
| Metrics QueryMetrics      | Metrics generated by the query engine for the request. |
| RequestID string          | The request identifier of this request.                |
| Warnings \[\]QueryWarning | Non-fatal errors that occurred during query execution. |

```go
	meta, err := result.MetaData()
	handleErr(err)

	fmt.Printf("Got meta: %v", meta)
```

## [](#further-information)Further Information

The [SQL++ for Analytics Reference](../../../server/current/analytics/1%5Fintro.md)offers a complete guide to the SQL++ language for both of our analytics services, including all of the latest additions.