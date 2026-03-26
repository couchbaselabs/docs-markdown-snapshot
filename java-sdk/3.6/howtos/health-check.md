---
title: Diagnosing and preventing Network Problems with Health Check
description: In today's distributed and virtual environments, users will often
  not have full administrative control over their whole network.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/temp/3.6/modules/howtos/pages/health-check.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.6@java-sdk:howtos:health-check.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.6/howtos/health-check.html)

# Diagnosing and preventing Network Problems with Health Check

> In today's distributed and virtual environments, users will often not have full administrative control over their whole network. Health Check introduces _Ping_ to check nodes are still healthy, and to force idle connections to be kept alive in environments with eager shutdowns of unused resources. _Diagnostics_ requests a report from all the connected sockets against the cluster (from a client point of view), giving instant, but passive health check information. 

Diagnosing problems in distributed environments is far from easy, so Couchbase provides a _Health Check API_ with `Ping()` for active monitoring, and `Diagnostics()` for a look at what the client believes is the current state of the cluster. More extensive discussion of the uses of Health Check can be found in the [Health Check Concept Guide](../concept-docs/health-check.md).

## [](#ping)Ping

At its simplest, `ping` provides information about the current state of the connections in the Couchbase Cluster, by actively polling:

```java
        PingResult pingResult = cluster.ping();
        for (Map.Entry<ServiceType, List<EndpointPingReport>> service : pingResult.endpoints().entrySet()) {
            for (EndpointPingReport er : service.getValue()) {
                System.err.println(service.getKey() + ": " + er.remote() + " took " + er.latency());
            }
        }
```

This will print the latency for each socket (endpoint) connected per service. More information is available on the classes. Usually though, you want to regularly perform the ping and then print the results into the log. This is made easy by the `exportToJson` method:

```java
        PingResult pingResult = cluster.ping();
        System.out.println(pingResult.exportToJson());
```

By default the SDK will ping all services available on the target cluster. You can customize the type of services to ping through the `PingOptions`:

```java
        PingResult pingResult = cluster.ping(pingOptions().serviceTypes(EnumSet.of(ServiceType.QUERY)));
        System.out.println(pingResult.exportToJson());
```

In this example, only the Query service is included in the ping report.

Note that `ping` is available both on the `Cluster` and the `Bucket` level. The difference is that at the cluster level, the key-value service might not be included based on the Couchbase Server version in use. If you want to make sure the key-value service is included, perform it at the bucket level.

## [](#diagnostics)Diagnostics

Diagnostics works in a similar fashion to `ping` in the sense that it returns a report of how all the sockets/endpoints are doing, but the main difference is that it is passive. While a ping proactively sends an operation across the network, a diagnostics report just returns whatever current state the client is in. This makes it much cheaper to call on a regular basis, but does not provide any live insight into network slowness, etc.

```java
        DiagnosticsResult diagnosticsResult = cluster.diagnostics();
        for (Map.Entry<ServiceType, List<EndpointDiagnostics>> service : diagnosticsResult.endpoints().entrySet()) {
            for (EndpointDiagnostics ed : service.getValue()) {
                System.err.println(
                        service.getKey() + ": " + ed.remote() + " last activity  " + ed.lastActivity()
                );
            }
        }
```

Because it is passive, diagnostics are only available at the `Cluster` level and cover everything in the current SDK state. Also, because it is not doing any I/O you cannot proactively filter the list of services that are returned, all you need to do is look only at the ones that are interesting to you.

A `DiagnosticsResult` has one interesting property over a ping result: It provides a cumulative `ClusterState` through the `state()` method. The state can be `ONLINE`, `DEGRADED` or `OFFLINE`. This allows to give a single, although simplistic, view on how your cluster is doing from a client point of view. The state is determined as follows:

* If at least one socket is open and all of them are connected, it is `ONLINE`
* If at least one is connected but not all are, it is `DEGRADED`
* If none are connected, it is `OFFLINE`

Of course you can iterate over the individual states and apply a different algorithm if needed.