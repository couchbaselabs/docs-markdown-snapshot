[View original HTML](/java-columnar-sdk/current/hello-world/start-using-sdk.html)

> Install, connect, try. A quick start guide to get you up and running with Columnar and the Java Columnar SDK. 

[Capella Columnar](../../../analytics/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Although maintaining some syntactic similarities with [the operational SDKs](#home:sdk.adoc), the Java Columnar SDK is developed from the ground-up for Columnar’s analytical use cases, and supports streaming APIs to handle large datasets.

## [](#before-you-start)Before You Start

Sign up for a [Capella account](../../../cloud/get-started/create-account.md), and choose a [Columnar](../../../analytics/intro/intro.md) cluster.

After creating the cluster, add your IP address to the list of allowed IP addresses.

### [](#minimum-java-version)Minimum Java Version

The Java Columnar SDK requires Java 17 or later. We recommend using the most recent long-term support (LTS) version of OpenJDK.

|  | Remember to keep your Java installation up to date with the latest patches. |
|  | --------------------------------------------------------------------------- |

## [](#maven-project-template)Maven Project Template

The SDK’s source code repository includes an [example Maven project](https://github.com/couchbase/couchbase-jvm-clients/tree/columnar-java-client-1.0.7/columnar-java-client/examples) you can copy to get started quickly.

## [](#adding-the-sdk-to-an-existing-project)Adding the SDK to an Existing Project

Declare a dependency on the SDK using its [Maven Coordinates](../project-docs/sdk-full-installation.md).

To see log messages from the SDK, [include an SLF4J binding in your project](../howtos/logging.md).

## [](#connecting-and-executing-a-query)Connecting and Executing a Query

```java
import com.couchbase.columnar.client.java.Cluster;
import com.couchbase.columnar.client.java.Credential;
import com.couchbase.columnar.client.java.QueryResult;

import java.util.List;

public class Example {
  public static void main(String[] args) {
    var connectionString = "couchbases://...";
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