---
title: Go Analytics SDK Quickstart Guide
description: Install, connect, try. A quick start guide to get you up and
  running with Enterprise Analytics and the Go Analytics SDK.
editUrl: https://github.com/couchbase/docs-analytics-sdk-go/edit/release/1.0/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:1.0@go-analytics-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-analytics-sdk/1.0/hello-world/start-using-sdk.html)

# Go Analytics SDK Quickstart Guide

> Install, connect, try. A quick start guide to get you up and running with Enterprise Analytics and the Go Analytics SDK. 

[Enterprise Analytics](../../../analytics/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Although maintaining some syntactic similarities with [the operational SDKs](../../../home/sdk.md), the Go Analytics SDK is developed from the ground-up for column-based analytical use cases, and supports streaming APIs to handle large datasets.

## [](#before-you-start)Before You Start

Install and configure an [Enterprise Analytics Cluster](../../../enterprise-analytics/current/intro/intro.md).

### [](#minimum-go-version)Minimum Go Version

In line with the Golang project, the Go Analytics SDK supports both the current, and the previous, versions of Go. Earlier versions may work, but are not supported.

## [](#adding-the-sdk-to-an-existing-project)Adding the SDK to an Existing Project

Declare a dependency on the SDK using its [Full Installation](../project-docs/sdk-full-installation.md).

To see log messages from the SDK, [consult the logging documentation](../howtos/logging.md).

## [](#connecting-and-executing-a-query)Connecting and Executing a Query

```go
package main

import (
	"context"
	"fmt"
	"time"

	"github.com/couchbase/gocbanalytics"
)

func helloWorld() {
	cluster, err := cbanalytics.NewCluster(
		connStr,
		cbanalytics.NewBasicAuthCredential(username, password),
		// The third parameter is optional.
		// This example sets the default server query timeout to 3 minutes,
		// that is the timeout value sent to the query server.
		cbanalytics.NewClusterOptions().SetTimeoutOptions(
			cbanalytics.NewTimeoutOptions().SetQueryTimeout(3*time.Minute),
		),
	)
	handleErr(err)

	// We create a new context with a timeout of 2 minutes.
	// This context will apply timeout/cancellation on the client side.
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Minute)
	defer cancel()

	printRows := func(result *cbanalytics.QueryResult) {
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
		cbanalytics.NewQueryOptions().SetPositionalParameters([]interface{}{1}),
	)
	handleErr(err)

	printRows(result)

	// Execute a query with named arguments.
	result, err = cluster.ExecuteQuery(
		ctx,
		"select $foo=1",
		cbanalytics.NewQueryOptions().SetNamedParameters(map[string]interface{}{"foo": 1}),
	)
	handleErr(err)

	printRows(result)

	err = cluster.Close()
	handleErr(err)
}
```

### [](#connection-string)Connection String

The `connStr` in the above example should take the form of "https://<your\_hostname>:" + PORT

The default port is 443, for TLS connections. You do not need to give a port number if you are using port 443 — `hostname = "https://<your_hostname>"` is effectively the same as \`hostname = "https://<your\_hostname>:" + "443"

If you are using a different port — for example, connecting to a cluster without a load balancer, directly to the Analytics port, `18095` — or not using TLS, then see the [Connecting to Enterprise Analytics](../howtos/managing-connections.md) page.

```go
const (
		connStr  = "https://analytics.example.com:18095"
		username = "user"
		password = "password"
	)
```

## [](#migration-from-row-based-analytics)Migration from Row-Based Analytics

If you are migrating a project from CBAS — our Analytics service on Capella Operational and Couchbase Server, using our operational SDKs — then information on migration can be found in the [Enterprise Analytics docs](../../../enterprise-analytics/current/migration/overview.md).

In particular, refer to the [SDK section](../../../enterprise-analytics/current/migration/migration-process.md#sdk-migration) of the Enterprise Analytics migration pages.