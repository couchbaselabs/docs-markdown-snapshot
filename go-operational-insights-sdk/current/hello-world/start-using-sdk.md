---
title: Go Operational Insights SDK Quickstart Guide
description: Install, connect, try. A quick start guide to get you up and
  running with Enterprise Operational Insights and the Go Operational Insights
  SDK.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Go Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-go/edit/release/1.0/modules/hello-world/pages/start-using-sdk.adoc
  xref: xref:go-operational-insights-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-operational-insights-sdk/current/hello-world/start-using-sdk.html)

# Go Operational Insights SDK Quickstart Guide

> Install, connect, try. A quick start guide to get you up and running with Enterprise Operational Insights and the Go Operational Insights SDK. 

[Operational Insights](../../../operational-insights-cloud/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Although maintaining some syntactic similarities with [the operational SDKs](../../../home/sdk.md), the Go Operational Insights SDK is developed from the ground-up for column-based analytical use cases, and supports streaming APIs to handle large datasets.

## [](#before-you-start)Before You Start

Install and configure an [Operational Insights Enterprise Cluster](../../../operational-insights/current/intro/intro.md).

### [](#minimum-go-version)Minimum Go Version

In line with the Golang project, the Go Operational Insights SDK supports both the current, and the previous, versions of Go. Earlier versions may work, but are not supported.

## [](#adding-the-sdk-to-an-existing-project)Adding the SDK to an Existing Project

Declare a dependency on the SDK using its [Full Installation](../project-docs/sdk-full-installation.md).

To see log messages from the SDK, [consult the logging documentation](../howtos/logging.md).

## [](#connecting-and-executing-a-query)Connecting and Executing a Query

The 2.2 Operational Insights Enterprise Cluster introduced support for JWT and client certificate authentication, as well as a new poll-based Server Asynchronous Request API that uses request handles to fetch results. This API eliminates the need for long-running server connections.

The examples in this first section of the page are for the standard API, working with all releases of Operational Insights (with Server Asynchronous Request API examples following in the [Server Async section](#server-asynchronous-api)). Note, you can still use this API with 2.2+ releases of Operational Insights, in addition to the new API.

### [](#server-synchronous-request-api)Server Synchronous Request API

```go
package main

import (
	"context"
	"fmt"
	"time"

	cbinsights "github.com/couchbase/gocbinsights"
)

func helloWorld() {
	cluster, err := cbinsights.NewCluster(
		connStr,
		cbinsights.NewBasicAuthCredential(username, password),
		// The third parameter is optional.
		// This example sets the default server query timeout to 3 minutes,
		// that is the timeout value sent to the query server.
		cbinsights.NewClusterOptions().SetTimeoutOptions(
			cbinsights.NewTimeoutOptions().SetQueryTimeout(3*time.Minute),
		),
	)
	handleErr(err)

	// We create a new context with a timeout of 2 minutes.
	// This context will apply timeout/cancellation on the client side.
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Minute)
	defer cancel()

	printRows := func(result *cbinsights.QueryResult) {
		for row := result.NextRow(); row != nil; row = result.NextRow() {
			var content map[string]interface{}

			err = row.ContentAs(&content)
			handleErr(err)

			fmt.Printf("Got row content: %v", content)
		}
	}

	// Execute a query and process rows as they arrive from server.
	// Results are always streamed from the server.
	result, err := cluster.ExecuteQuery(ctx, "select 1")
	handleErr(err)

	printRows(result)

	// Execute a query with positional arguments.
	result, err = cluster.ExecuteQuery(
		ctx,
		"select ?=1",
		cbinsights.NewQueryOptions().SetPositionalParameters([]interface{}{1}),
	)
	handleErr(err)

	printRows(result)

	// Execute a query with named arguments.
	result, err = cluster.ExecuteQuery(
		ctx,
		"select $foo=1",
		cbinsights.NewQueryOptions().SetNamedParameters(map[string]interface{}{"foo": 1}),
	)
	handleErr(err)

	printRows(result)

	err = cluster.Close()
	handleErr(err)
}
```

### [](#server-asynchronous-api)Server Asynchronous Request API

Operational Insights 2.2 introduced a Server Asynchronous Request API. The SDK sends a request, polls for results, and then fetches once the result is available.

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

### [](#connection-string)Connection String

The `connStr` in the above example should take the form of "https://<your\_hostname>:" + PORT

The default port is 443, for TLS connections. You do not need to give a port number if you are using port 443 — `hostname = "https://<your_hostname>"` is effectively the same as \`hostname = "https://<your\_hostname>:" + "443"

If you are using a different port — for example, connecting to a cluster without a load balancer, directly to the Analytics port, `18095` — or not using TLS, then see the [Connecting to Operational Insights](../howtos/managing-connections.md) page.

```go
const (
		connStr  = "https://analytics.example.com:18095"
		username = "user"
		password = "password"
	)
```

## [](#migration-from-row-based-analytics)Migration from Row-Based Analytics

If you are migrating a project from CBAS — our Analytics service on Capella Operational and Couchbase Server, using our operational SDKs — then information on migration can be found in the [Operational Insights docs](../../../operational-insights/current/migration/overview.md).

In particular, refer to the [SDK section](../../../operational-insights/current/migration/migration-process.md#sdk-migration) of the Operational Insights migration pages.