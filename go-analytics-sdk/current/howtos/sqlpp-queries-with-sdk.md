[View original HTML](/go-analytics-sdk/current/howtos/sqlpp-queries-with-sdk.html)

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. 

On this page we dive straight into using the Query Service API from the Go Analytics SDK. For a deeper look at the concepts, to help you better understand the Query Service, and the SQL++ language, see the links in the [Further Information](#further-information) section at the end of this page.

Here we show queries against the Travel Sample collection, at cluster and scope level, and give links to information on adding other collections to your data.

## [](#before-you-start)Before You Start

This page assumes that you have [installed the Go Analytics SDK](../hello-world/start-using-sdk.md), and created an [Enterprise Analytics cluster](../../../enterprise-analytics/current/install/introduction-linux-installation.md).

Create a collection to work upon by [importing the travel-sample dataset](../../../enterprise-analytics/current/intro/connecting-to-data-sources.md#import-the-travel-sample-collections) into your cluster.

## [](#querying-your-dataset)Querying Your Dataset

Execute a query and print all rows:

```golang
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

```golang
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

```golang
	result, err := cluster.ExecuteQuery(
		ctx,
		"select ?=1",
		cbanalytics.NewQueryOptions().SetPositionalParameters([]interface{}{1}),
	)
	handleErr(err)
```

Execute a streaming query with named arguments:

Named Parameters

```golang
	result, err := cluster.ExecuteQuery(
		ctx,
		"select $foo=1",
		cbanalytics.NewQueryOptions().SetNamedParameters(map[string]interface{}{"foo": 1}),
	)
	handleErr(err)
```

Access query metadata:

Metadata

```golang
	meta, err := result.MetaData()
	handleErr(err)

	fmt.Printf("Got meta: %v", meta)
```

## [](#query-options)Query Options

The query service provides an array of options to customize your query. The following table lists them all:

__Table 1\. Available Query Options__
| Name                                     | Description                                                          |
| ---------------------------------------- | -------------------------------------------------------------------- |
| ClientContextID string                   | An optional identifier for the query.                                |
| NamedParameters map\[string\]interface{} | Allows to set named arguments for a parameterized query.             |
| PositionalParameters \[\]interface{}     | Allows to set positional arguments for a parameterized query.        |
| Raw map\[string\]interface{}             | Escape hatch to add arguments that are not covered by these options. |
| ReadOnly bool                            | Tells the client and server that this query is readonly.             |
| ScanConsistency QueryScanConsistency     | Sets a different scan consistency for this query.                    |
| Unmarshaler Unmarshaler                  | Sets a different Unmarshaler for this query.                         |

## [](#further-information)Further Information

The [SQL++ for Analytics Reference](../../../server/current/analytics/1%5Fintro.md)offers a complete guide to the SQL++ language for both of our analytics services, including all of the latest additions.