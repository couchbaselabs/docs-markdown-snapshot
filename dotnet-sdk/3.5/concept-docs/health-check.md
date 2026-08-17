---
title: Health Check
description: Health Check provides ping() and diagnostics() tests for the health
  of the network and the cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/release/3.5/modules/concept-docs/pages/health-check.adoc
  xref: xref:3.5@dotnet-sdk:concept-docs:health-check.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.5/concept-docs/health-check.html)

# Health Check

> Health Check provides ping() and diagnostics() tests for the health of the network and the cluster. 

Working in distributed environments is _hard_. Latencies come and go, so do connections in their entirety. Is it a network glitch, or is the remote cluster down? Sometimes just knowing the likely cause is enough to get a good start on a workaround, or at least avoid hours wasted on an inappropriate solution.

Health Check enables useful diagnostics on the state of Couchbase Clusters across networks. `Ping` and `diagnostics` methods on the bucket and cluster objects respectively, can give us information about the current state of nodes, and their connections.

## [](#ping)Ping

`Ping` _actively_ queries the status of the specified services,giving status and latency information for every node reachable. In addition to its use as a monitoring tool, a regular `Ping` can be used in an environment which does not respect keep alive values for a connection.

A `ping` can be performed either at the `Cluster` or at the `Bucket` level. They are very similar, although at the `Bucket` level also the Key/Value and View connections for the specific bucket are taken into account.

The report can either be analyzed in code or can be turned into JSON and printed:

```C#
IPingReport report = await bucket.PingAsync(options =>
{
    options.ServiceTypes(new ServiceType[] {ServiceType.KeyValue, ServiceType.Query});
});

Console.WriteLine(report);

// alternatively, format the output with indenting:
//Console.WriteLine(JsonConvert.SerializeObject(report, Formatting.Indented));
```

You will see an output similar to this:

```JavaScript
{
  "id": "174ad024-43d4-410c-9d80-61788b4f3bf4",
  "version": 1,
  "config_rev": 572,
  "sdk": "couchbase-net-sdk/3.0.7.0 (clr/.NET Core 3.1.9) (os/Microsoft Windows 10.0.18363)",
  "services": {
    "n1ql": [
      {
        "state": "ok",
        "remote": "[::1]:11210",
        "last_activity_us": 0,
        "latency_us": 135751,
        "scope": "Cluster"
      }
    ],
    "kv": [
      {
        "id": "2",
        "state": "ok",
        "local": "[::1]:53183",
        "remote": "[::1]:11210",
        "last_activity_us": 81526,
        "latency_us": 2330,
        "scope": "travel-sample"
      },
      {
        "id": "1",
        "state": "ok",
        "local": "[::1]:53184",
        "remote": "[::1]:11210",
        "last_activity_us": 94655,
        "latency_us": 312,
        "scope": "travel-sample"
      }
    ]
  }
}
```

Notice the `scope` of each service. Bucket level services like key/value will have a bucket name as scope, while cluster level services will have "Cluster" as their scope.

## [](#diagnostics)Diagnostics

`Diagnostics` returns a list of the nodes that the SDK currently has (or had) a connection to, and the current status of the connection. However this call _does not_ actively poll the nodes, reporting instead the state the last time it tried to access each node. If you want the _current_ status, then use [Ping](#ping).

```javascript
IDiagnosticsReport diagnosticsReport = await cluster.DiagnosticsAsync();

Console.WriteLine(diagnosticsReport);

// alternatively, format the output with indenting:
// Console.WriteLine(JsonConvert.SerializeObject(diagnosticsReport, Formatting.Indented));
```

You will see an output similar to this:

```JavaScript
{
  "id": "b084360a-82b1-4602-b983-281d3cc11b3b",
  "version": 1,
  "sdk": "couchbase-net-sdk/3.0.7.0 (clr/.NET Core 3.1.9) (os/Microsoft Windows 10.0.18363)",
  "services": {
    "kv": [
      {
        "id": "2",
        "state": "authenticating",
        "local": "[::1]:53491",
        "remote": "[::1]:11210",
        "last_activity_us": 61153,
        "scope": "travel-sample"
      },
      {
        "id": "1",
        "state": "authenticating",
        "local": "[::1]:53492",
        "remote": "[::1]:11210",
        "last_activity_us": 66101,
        "scope": "travel-sample"
      }
    ],
    "view": [
      {
        "state": "new",
        "remote": "[::1]:11210",
        "last_activity_us": 0,
        "scope": "travel-sample"
      }
    ],
    "n1ql": [
      {
        "state": "new",
        "remote": "[::1]:11210",
        "last_activity_us": 0,
        "scope": "Cluster"
      }
    ],
    "cbas": [
      {
        "state": "new",
        "remote": "[::1]:11210",
        "last_activity_us": 0,
        "scope": "Cluster"
      }
    ],
    "fts": [
      {
        "state": "new",
        "remote": "[::1]:11210",
        "last_activity_us": 0,
        "scope": "Cluster"
      }
    ]
  }
}
```

Like with Ping, notice the `scope` of each service.