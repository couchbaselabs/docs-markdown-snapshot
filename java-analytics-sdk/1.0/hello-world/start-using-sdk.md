---
title: Java Analytics SDK Quickstart Guide
description: Install, connect, try. A quick start guide to get you up and
  running with Enterprise Analytics and the Java Analytics SDK.
editUrl: https://github.com/couchbase/docs-analytics-sdk-java/edit/release/1.0/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:1.0@java-analytics-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-analytics-sdk/1.0/hello-world/start-using-sdk.html)

# Java Analytics SDK Quickstart Guide

> Install, connect, try. A quick start guide to get you up and running with Enterprise Analytics and the Java Analytics SDK. 

[Enterprise Analytics](../../../analytics/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Although maintaining some syntactic similarities with [the operational SDKs](../../../home/sdk.md), the Java Analytics SDK is developed from the ground-up for column-based analytical use cases, and supports streaming APIs to handle large datasets.

## [](#before-you-start)Before You Start

Install and configure an [Enterprise Analytics Cluster](../../../enterprise-analytics/current/intro/intro.md).

### [](#minimum-java-version)Minimum Java Version

The Java Analytics SDK requires Java 8 or later. We recommend using the most recent long-term support (LTS) version of OpenJDK.

> [!TIP]
> Remember to keep your Java installation up to date with the latest patches.

## [](#maven-project-template)Maven Project Template

The SDK's source code repository includes an [example Maven project](https://github.com/couchbaselabs/couchbase-analytics-jvm-clients/tree/main/couchbase-analytics-java-client/examples/maven-project-template)you can copy to get started quickly.

## [](#adding-the-sdk-to-an-existing-project)Adding the SDK to an Existing Project

Declare a dependency on the SDK using its [Maven Coordinates](../project-docs/sdk-full-installation.md).

To see log messages from the SDK, [include an SLF4J binding in your project](../howtos/logging.md).

## [](#connecting-and-executing-a-query)Connecting and Executing a Query

```java
import com.couchbase.analytics.client.java.Cluster;
import com.couchbase.analytics.client.java.Credential;
import com.couchbase.analytics.client.java.QueryResult;

import java.util.List;

public class Example {
  public static void main(String[] args) {
    var connectionString = "https://<your_hostname>:" + PORT;
    var username = "...";
    var password = "...";

    try (Cluster cluster = Cluster.newInstance(
      connectionString,
      Credential.of(username, password),
      // The third parameter is optional.
      // This example sets the default query timeout to 2 minutes.
      clusterOptions -> clusterOptions
        .timeout(it -> it.queryTimeout(Duration.ofMinutes(2)))
    )) {

      // Execute a query and buffer all result rows in client memory.
      QueryResult result = cluster.executeQuery("select 1");
      result.rows().forEach(row -> System.out.println("Got row: " + row));

      // Execute a query and process rows as they arrive from server.
      cluster.executeStreamingQuery(
          "select 1",
          row -> System.out.println("Got row: " + row)
      );

      // Execute a streaming query with positional arguments.
      cluster.executeStreamingQuery(
        "select ?=1",
        row -> System.out.println("Got row: " + row),
        options -> options
          .parameters(List.of(1))
      );

      // Execute a streaming query with named arguments.
      cluster.executeStreamingQuery(
        "select $foo=1",
        row -> System.out.println("Got row: " + row),
        options -> options
          .parameters(Map.of("foo", 1))
      );
    }
  }
}
```

### [](#connection-string)Connection String

The `connStr` in the above example should take the form of "https://<your\_hostname>:" + PORT

The default port is 443, for TLS connections. You do not need to give a port number if you are using port 443 — `hostname = "https://<your_hostname>"` is effectively the same as \`hostname = "https://<your\_hostname>:" + "443"

If you are using a different port — for example, connecting to a cluster without a load balancer, directly to the Analytics port, `18095` — or not using TLS, then see the [Connecting to Enterprise Analytics](../howtos/managing-connections.md) page.

## [](#migration-from-row-based-analytics)Migration from Row-Based Analytics

If you are migrating a project from CBAS — our Analytics service on Capella Operational and Couchbase Server, using our operational SDKs — then information on migration can be found in the [Enterprise Analytics docs](../../../enterprise-analytics/current/migration/overview.md).

In particular, refer to the [SDK section](../../../enterprise-analytics/current/migration/migration-process.md#sdk-migration) of the Enterprise Analytics migration pages.