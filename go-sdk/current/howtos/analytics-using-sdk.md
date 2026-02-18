---
title: Analytics
description: Parallel data management for complex queries over many records,
  using a familiar SQL-like syntax.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.11/modules/howtos/pages/analytics-using-sdk.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/go-sdk/current/howtos/analytics-using-sdk.html)

# Analytics

> Parallel data management for complex queries over many records, using a familiar SQL-like syntax. 

This page covers using our operational Go SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase’s analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](#home::analytics-sdk.adoc) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](#home::columnar-sdk.adoc) for more information.

For complex and long-running queries, involving large ad hoc join, set, aggregation, and grouping operations, Couchbase Data Platform offers the [Couchbase Analytics Service (CBAS)](../../../server/current/analytics/introduction.md). This is the analytic counterpart to our [operational data focussed Query Service](n1ql-queries-with-sdk.md).

The analytics service is available in [Capella operational](../../../cloud/clusters/analytics-service/analytics-service.md)or the Enterprise Edition of self-managed Couchbase Server.

## [](#getting-started)Getting Started

After familiarizing yourself with our [introductory primer](../../../server/current/analytics/primer-beer.md), in particular creating a dataset and linking it to a bucket to shadow the operational data, try Couchbase Analytics using the Go SDK. Intentionally, the API for analytics is very similar to that of the query service. In these examples we will be using an `airports` dataset created on the `travel-sample` bucket.

In Go SDK 1.x, Analytics was only available on the `Bucket` object; in Go SDK 2.x, Analytics queries are submitted using the Cluster reference, not a Bucket or Collection:

> [!NOTE]
> When using a Couchbase version < 6.5 you must create a valid Bucket connection using `cluster.Bucket(name)` before you can use Analytics.

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

	results, err := cluster.AnalyticsQuery("SELECT \"hello\" as greeting;", nil)
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

	// always check for errors after iterating.
	err = results.Err()
	if err != nil {
		panic(err)
	}
```

## [](#queries)Queries

A query can either be `simple` or be `parameterized`. If parameters are used, they can either be `positional` or `named`. Here is one example of each:

```golang
	results, err := cluster.AnalyticsQuery("select airportname, country from airports where country = 'France';", nil)
	if err != nil {
		panic(err)
	}
```

The query may be performed with positional parameters:

```golang
	results, err := cluster.AnalyticsQuery(
		"select airportname, country from airports where country = ?;",
		&gocb.AnalyticsOptions{
			PositionalParameters: []interface{}{"France"},
		},
	)
```

Alternatively, the query may be performed with named parameters:

```golang
	results, err := cluster.AnalyticsQuery(
		"select airportname, country from airports where country = $country;",
		&gocb.AnalyticsOptions{
			NamedParameters: map[string]interface{}{"country": "France"},
		},
	)
```

> [!NOTE]
> As timeouts are propagated to the server by the client, a timeout set on the client side may be used to stop the processing of a request, in order to save system resources. See example in the next section.

## [](#options)Options

Additional parameters may be sent as part of the query. There are currently three parameters:

* **Client Context ID**, sets a context ID that is returned back as part of the result. Uses `ClientContextID string` default is a random UUID
* **Timeout**, customizes the timeout sent to the server. Does not usually have to be set, as the client sets it based on the timeout on the operation. Uses `Timeout time.Duration`, and defaults to the Analytics timeout set on the client (75s). This can be adjusted at the [cluster global config level](../ref/client-settings.md#timeout-options).
* **Priority**, set if the request should have priority over others. The `Priority bool` option defaults to `false`.

Here, we give the request priority over others, and set a custom, server-side timeout value:

```golang
	results, err = cluster.AnalyticsQuery(
		"select airportname, country from airports where country = 'France';",
		&gocb.AnalyticsOptions{
			Priority: true,
			Timeout:  100 * time.Second,
		},
	)
```

## [](#handling-the-response)Handling the Response

These query results may contain various sorts of data and metadata, depending upon the nature of the query, as you will have seen when working through our [introductory primer](../../../server/current/analytics/primer-beer.md).

Results are iterated using the `Next` function. Within the `for` loop the result is read using the `Row` by supplying a pointer to the variable in which to store the value. Always remember to check the error value of `Err` after iterating the results, this is where any errors occurring whilst calling `Next` will be returned.

```golang
	var rows []interface{}
	for results.Next() {
		var row interface{}
		if err := results.Row(&row); err != nil {
			panic(err)
		}
		rows = append(rows, row)
	}

	if err := results.Err(); err != nil {
		panic(err)
	}
```

Common errors are listed in our [Errors Reference doc](../ref/error-codes.md#analytics-errors), with errors caused by resource unavailability (such as timeouts and _Operation cannot be performed during rebalance_ messages) leading to an [automatic retry](error-handling.md#retry) by the SDK.

If you only expect a single result or only want to use the first result in a resultset then you can use `One`(note: this function will iterate any remaining rows in the resultset so can only be called once and should only be used on small resultsets):

```golang
	rows, err := cluster.AnalyticsQuery("select airportname, country from airports where country = 'France' LIMIT 1;", nil)
	// check query was successful
	if err != nil {
		panic(err)
	}

	var result interface{}
	err = rows.One(&result)
	if err != nil {
		panic(err)
	}
	fmt.Println(result)
```

### [](#metadata)MetaData

The `AnalyticsResultsMetadata` object contains useful metadata, such as `Metrics` and `ClientContextID`. Note that before metadata can be accessed the results object rows must be fully iterated. Here is a snippet using several items of metadata

```golang
	// make sure that results has been iterated (and therefore closed) before calling this.
	metadata, err := results.MetaData()
	if err != nil {
		panic(err)
	}

	fmt.Printf("Client context id: %s\n", metadata.ClientContextID)
	fmt.Printf("Elapsed time: %d\n", metadata.Metrics.ElapsedTime)
	fmt.Printf("Execution time: %d\n", metadata.Metrics.ExecutionTime)
	fmt.Printf("Result count: %d\n", metadata.Metrics.ResultCount)
	fmt.Printf("Error count: %d\n", metadata.Metrics.ErrorCount)
```

For a listing of available `Metrics` in `MetaData`, see the [Understanding Analytics](../concept-docs/analytics-for-sdk-users.md) SDK doc.

## [](#scoped-queries-on-named-collections)Scoped Queries on Named Collections

In addition to creating a dataset with a WHERE clause to filter the results to documents with certain characteristics, you can also create a dataset against a named collection, for example:

```sqlpp
ALTER COLLECTION `travel-sample`.inventory.airport ENABLE ANALYTICS;

-- NB: this is more or less equivalent to:
CREATE DATAVERSE `travel-sample`.inventory;
CREATE DATASET `travel-sample`.inventory.airport ON `travel-sample`.inventory.airport;
```

We can then query the Dataset as normal, using the fully qualified keyspace:

```golang
results, err := cluster.AnalyticsQuery("select airportname, country from `travel-sample`.inventory.airport where country = 'France' limit 3;", nil)
if err != nil {
	panic(err)
}
```

Note that using the `CREATE DATASET` syntax we could choose any Dataset name in any Dataverse, including the default. However the SDK supports this standard convention, allowing us to query from the Scope object:

```golang
scope := bucket.Scope("inventory")
results, err := scope.AnalyticsQuery("SELECT airportname, country FROM `airport` WHERE country='France' LIMIT 2", nil)
if err != nil {
	panic(err)
}
```

## [](#additional-resources)Additional Resources

To learn more about using [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) for Analytics see our [Tutorial Introduction to SQL++ for SQL users](https://sqlplusplus-tutorial.couchbase.com/tutorial/#1).