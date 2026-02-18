---
title: Health Check
description: Health Check provides <code>ping()</code> tests for the health of
  the network and the cluster.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/health-check.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/rust-sdk/current/howtos/health-check.html)

# Health Check

> Health Check provides `ping()` tests for the health of the network and the cluster. 

In today’s distributed and virtual environments, users will often not have full administrative control over their whole network. Working in distributed environments is hard. Latencies come and go, so do connections in their entirety. Is it a network glitch, or is the remote cluster down? Sometimes just knowing the likely cause is enough to get a good start on a workaround, or at least avoid hours wasted on an inappropriate solution.

Health Check features _Ping_ to check nodes are still healthy, and to force idle connections to be kept alive in environments with eager shutdowns of unused resources.

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