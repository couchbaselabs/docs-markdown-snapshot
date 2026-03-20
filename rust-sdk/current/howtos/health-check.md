---
title: Health Check
description: Health Check provides <code>ping()</code> and
  <code>diagnostics()</code> tests for the health of the network and the
  cluster.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/health-check.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:rust-sdk:howtos:health-check.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/howtos/health-check.html)

# Health Check

> Health Check provides `ping()` and `diagnostics()` tests for the health of the network and the cluster. 

In today’s distributed and virtual environments, users will often not have full administrative control over their whole network. Working in distributed environments is hard. Latencies come and go, so do connections in their entirety. Is it a network glitch, or is the remote cluster down? Sometimes just knowing the likely cause is enough to get a good start on a workaround, or at least avoid hours wasted on an inappropriate solution.

Health Check features _Ping_ to check nodes are still healthy, and to force idle connections to be kept alive in environments with eager shutdowns of unused resources. _Diagnostics_ requests a report from a node, giving instant health check information.

## [](#ping)Ping

`Ping` _actively_ queries the status of the specified services, giving status and latency information for every node reachable. In addition to its use as a monitoring tool, a regular `Ping` can be used in an environment which does not respect keep alive values for a connection.

```rust
let result = cluster
    .ping(PingOptions::new().service_types(vec![ServiceType::KV, ServiceType::QUERY]))
    .await?;

println!("Ping result: {result}");
/*
{
  "config_rev": 939408,
  "id": "f3af8565-197d-49f6-8248-ce59ebf585fb",
  "sdk": "rust",
  "services": {
    "Kv": [
      {
        "id": "e8ab555c-b561-4d79-8653-b694434cab4f",
        "latency_us": 294,
        "remote": "192.168.107.130:11207",
        "state": "ok"
      },
      {
        "id": "54362aa1-83a6-4514-9e13-579a43534649",
        "latency_us": 309,
        "remote": "192.168.107.129:11207",
        "state": "ok"
      },
      {
        "id": "67620757-f549-4cf9-a11a-188bee40bb98",
        "latency_us": 269,
        "remote": "192.168.107.128:11207",
        "state": "ok"
      }
    ],
    "Query": [
      {
        "latency_us": 6103,
        "remote": "https://192.168.107.130:18093",
        "state": "ok"
      },
      {
        "latency_us": 8512,
        "remote": "https://192.168.107.129:18093",
        "state": "ok"
      },
      {
        "latency_us": 6549,
        "remote": "https://192.168.107.128:18093",
        "state": "ok"
      }
    ]
  },
  "version": 2
}
     */
```

## [](#diagnostics)Diagnostics

`Diagnostics` returns a list of the nodes that the SDK currently has (or had) a connection to, and the current status of the connection. However this call _does not_ actively poll the nodes, reporting instead the state the last time it tried to access each node. If you want the _current_ status, then use [Ping](#Ping).

```rust
  let result = cluster.diagnostics(None).await?;

  println!("Diagnostics result: {result}");
  /*
  {
    "version": 2,
    "config_rev": 8101,
    "id": "a84ef919-abc2-4dd2-8c4d-2220cc645d7c",
    "sdk": "rust",
    "services": {
      "Kv": [
        {
          "service_type": "Kv",
          "id": "701259c9-d43c-4898-832a-f62e2934014b",
          "local_address": "192.168.106.1:60774",
          "remote_address": "192.168.106.128:11210",
          "last_activity": 2395,
          "state": "Connected"
        },
        {
          "service_type": "Kv",
          "id": "c7c24770-0746-4493-b0d3-b5013de48bf4",
          "local_address": "192.168.106.1:60775",
          "remote_address": "192.168.106.129:11210",
          "last_activity": 9495,
          "state": "Connected"
        },
        {
          "service_type": "Kv",
          "id": "fc883157-95f6-409a-8795-0776e788e6db",
          "local_address": "192.168.106.1:60773",
          "remote_address": "192.168.106.130:11210",
          "last_activity": 357556,
          "state": "Connected"
        }
      ]
}
*/
```