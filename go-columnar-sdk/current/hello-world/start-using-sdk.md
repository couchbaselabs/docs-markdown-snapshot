---
title: Hello Columnar&#8201;&#8212;&#8201;Go SDK Quickstart Guide
description: Install, connect, try. A quick start guide to get you up and
  running with Columnar and the Go Columnar SDK.
editUrl: https://github.com/couchbase/docs-columnar-sdk-go/edit/release/1.0/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:go-columnar-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-columnar-sdk/current/hello-world/start-using-sdk.html)

# Hello Columnar&#8201;&#8212;&#8201;Go SDK Quickstart Guide

> Install, connect, try. A quick start guide to get you up and running with Columnar and the Go Columnar SDK. 

[Capella Columnar](../../../analytics/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Although maintaining some syntactic similarities with [the operational SDKs](#home:sdk.adoc), the Go Columnar SDK is developed from the ground-up for Columnar's analytical use cases, and supports streaming APIs to handle large datasets.

## [](#before-you-start)Before You Start

Sign up for a [Capella account](../../../cloud/get-started/create-account.md), and choose a [Columnar](../../../analytics/intro/intro.md) cluster.

After creating the cluster, add your IP address to the list of allowed IP addresses.

### [](#minimum-java-version)Minimum Go Version

The Go Columnar SDK requires Go 1.22 or 1.23, using [Go Modules](https://go.dev/blog/using-go-modules).

## [](#adding-the-sdk-to-an-existing-project)Adding the SDK to an Existing Project

Declare a dependency on the SDK using its [Full Installation](../project-docs/sdk-full-installation.md).

To see log messages from the SDK, [enable logging](../howtos/logging.md).

## [](#connecting-and-executing-a-query)Connecting and Executing a Query

```go
package main

import (
	"context"
	"fmt"
	"time"

	"github.com/couchbase/gocbcolumnar"
)

func helloWorld() {
	cluster, err := cbcolumnar.NewCluster(
		connStr,
		cbcolumnar.NewCredential(username, password),
		// The third parameter is optional.
		// This example sets the default server query timeout to 3 minutes,
		// that is the timeout value sent to the query server.
		cbcolumnar.NewClusterOptions().SetTimeoutOptions(
			cbcolumnar.NewTimeoutOptions().SetQueryTimeout(3*time.Minute),
		),
	)
	handleErr(err)

	// We create a new context with a timeout of 2 minutes.
	// This context will apply timeout/cancellation on the client side.
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Minute)
	defer cancel()

	printRows := func(result *cbcolumnar.QueryResult) {
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
		cbcolumnar.NewQueryOptions().SetPositionalParameters([]interface{}{1}),
	)
	handleErr(err)

	printRows(result)

	// Execute a query with named arguments.
	result, err = cluster.ExecuteQuery(
		ctx,
		"select $foo=1",
		cbcolumnar.NewQueryOptions().SetNamedParameters(map[string]interface{}{"foo": 1}),
	)
	handleErr(err)

	printRows(result)

	err = cluster.Close()
	handleErr(err)
}
```