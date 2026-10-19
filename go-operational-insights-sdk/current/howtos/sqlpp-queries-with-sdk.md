---
title: Querying with SQL++
description: You can query for documents in Couchbase using the SQL++ query
  language -- a language based on SQL, but designed for structured and flexible
  JSON documents.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Go Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-go/edit/release/1.0/modules/howtos/pages/sqlpp-queries-with-sdk.adoc
  xref: xref:go-operational-insights-sdk:howtos:sqlpp-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-operational-insights-sdk/current/howtos/sqlpp-queries-with-sdk.html)

# Querying with SQL++

> You can query for documents in Couchbase using the SQL++ query language — a language based on SQL, but designed for structured and flexible JSON documents. 

On this page we dive straight into using the Query Service API from the Go Operational Insights SDK. For a deeper look at the concepts, to help you better understand the Query Service, and the SQL++ language, see the links in the [Further Information](#further-information) section at the end of this page.

## [](#before-you-start)Before You Start

This page assumes that you have [installed the Go Operational Insights SDK](../hello-world/start-using-sdk.md) and [created an Insights Enterprise cluster](../../../operational-insights/current/manage/manage-nodes/create-cluster.md#cluster).

Create a collection to work upon by [importing the travel-sample dataset](#analytics:intro:connecting-to-data-sources.adoc#import-the-travel-sample-collections) into your cluster.

## [](#querying-your-dataset)Querying Your Dataset

> [!TIP]
> API Enhancements & Async
> 
> The 2.2 Operational Insights Enterprise Cluster introduced support for JWT and client certificate authentication, as well as a new poll-based Server Asynchronous Request API that uses request handles to fetch results. This API eliminates the need for long-running server connections.
> 
> The examples in this first section of the page are for the standard API, working with all releases of Operational Insights (with Server Asynchronous Request API examples following in the [Server Async section](#server-asynchronous-api)). Note, you can still use this API with 2.2+ releases of Operational Insights, in addition to the new API.

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
		cbinsights.NewQueryOptions().SetPositionalParameters([]interface{}{1}),
	)
	handleErr(err)
```

Execute a streaming query with named arguments:

Named Parameters

```golang
	result, err := cluster.ExecuteQuery(
		ctx,
		"select $foo=1",
		cbinsights.NewQueryOptions().SetNamedParameters(map[string]interface{}{"foo": 1}),
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

## [](#server-asynchronous-api)Server Asynchronous Request API

Operational Insights 2.2 added a Server Asynchronous Request API. The SDK will send a request, poll for results, and then fetch once the result is available.

Server Asynchronous API Example

```go
package main

import (
	"context"
	"fmt"
	"log"
	"time"

	cbinsights "github.com/couchbase/gocbinsights"
)

func waitForQueryResults(ctx context.Context, handle *cbinsights.QueryHandle, delay time.Duration) (*cbinsights.QueryResultHandle, error) {
	var lastStatus *cbinsights.QueryStatus
	deadline, _ := ctx.Deadline()

	for {
		status, err := handle.FetchStatus(ctx)
		if err != nil {
			fmt.Printf("Error fetching query results: %v\n", err)
		} else {
			if status.ResultsReady() {
				return status.ResultHandle()
			}
			lastStatus = status
		}

		nextPoll := time.Now().Add(delay)
		if deadline.Before(nextPoll) {
			return nil, fmt.Errorf("query results not ready")
		}

		if lastStatus != nil {
			fmt.Printf("Query status: %s\n", lastStatus)
		}
		fmt.Printf("Query results not ready yet, sleeping for %s...\n", delay)
		time.Sleep(delay)
	}
}

func main() {
	endpoint := "https://localhost"
	username := "Administrator"
	password := "password"

	cred := cbinsights.NewBasicAuthCredential(username, password)
	cluster, err := cbinsights.NewCluster(endpoint, cred)
	if err != nil {
		log.Fatalf("failed to create cluster: %v", err)
	}
	defer func() {
		if err := cluster.Close(); err != nil {
			log.Printf("failed to close cluster: %v", err)
		}
	}()

	ctx, cancel := context.WithTimeout(context.Background(), 60*time.Second)
	defer cancel()

	statement := `SELECT VALUE SLEEP("x", 100) FROM RANGE(1, 100) AS id;`

	handle, err := cluster.StartQuery(ctx, statement)
	if err != nil {
		log.Fatalf("failed to start query: %v", err)
	}

	resultHandle, err := waitForQueryResults(ctx, handle, 2500*time.Millisecond)
	if err != nil {
		log.Fatalf("waiting for results: %v", err)
	}

	res, err := resultHandle.FetchResults(ctx)
	if err != nil {
		log.Fatalf("failed to fetch results: %v", err)
	}

	for row := res.NextRow(); row != nil; row = res.NextRow() {
		var val interface{}
		if err := row.ContentAs(&val); err != nil {
			log.Printf("failed to decode row: %v", err)
			continue
		}
		fmt.Printf("Found row: %v\n", val)
	}

	if err := res.Err(); err != nil {
		log.Fatalf("result error: %v", err)
	}

	metadata, err := res.MetaData()
	if err != nil {
		log.Fatalf("failed to get metadata: %v", err)
	}
	fmt.Printf("metadata=%+v\n", metadata)

	if err := resultHandle.DiscardResults(ctx); err != nil {
		log.Printf("failed to discard results: %v", err)
	}
}
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

The [SQL++ for Analytics Reference](../../../operational-insights-cloud/sqlpp/1%5Fintro.md)offers a complete guide to the SQL++ language for both of our analytics services, including all of the latest additions.