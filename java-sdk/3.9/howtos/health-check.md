---
title: Health Check
description: Health Check provides <code>ping()</code> and
  <code>diagnostics()</code> tests for the health of the network and the
  cluster.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.9/modules/howtos/pages/health-check.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.9@java-sdk:howtos:health-check.adoc[]
---

[View original HTML](/java-sdk/3.9/howtos/health-check.html)

# Health Check

> Health Check provides `ping()` and `diagnostics()` tests for the health of the network and the cluster. 

In today’s distributed and virtual environments, users will often not have full administrative control over their whole network. Working in distributed environments is hard. Latencies come and go, so do connections in their entirety. Is it a network glitch, or is the remote cluster down? Sometimes just knowing the likely cause is enough to get a good start on a workaround, or at least avoid hours wasted on an inappropriate solution.

Health Check features _Ping_ to check nodes are still healthy, and to force idle connections to be kept alive in environments with eager shutdowns of unused resources. _Diagnostics_ requests a report from a node, giving instant health check information.

## [](#uses)Uses

'Ping\` provides a raw JSON payload suitable for feeding into reactive log and aggregation components, including monitoring systems like _Splunk_, _ElasticSearch_, and _Nagios_. It can also help keep connections alive if you are operating across an environment which aggressively closes down unused connections.

`Diagnostics` provides a strongly typed API for proactive, pull-based monitoring systems, such as:

* [Kubernetes Liveness and Readiness Probes via HTTP or CLI commands](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/).
* [Docker Health Check with CLI commands](https://docs.docker.com/engine/reference/builder/#healthcheck).
* [AWS ELB through HTTP](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html).

This API does not provide binary yes/no answers about the health of the cluster; rather it summarizes as much information as possible, for the application developer to assemble a complete, contextual view and come to a conclusion.

Note: `Ping` may reopen a connection, so is not without side-effects. `Diagnostics` shows what the SDK _perceives_ as the current state of the network and services — it is without side-effects, but may not be up to date.

## [](#ping)Ping

`Ping` _actively_ queries the status of the specified services, giving status and latency information for every node reachable. In addition to its use as a monitoring tool, a regular `Ping` can be used in an environment which does not respect keep alive values for a connection.

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

Note that `ping` is available both at the `Cluster` and the `Bucket` level. The difference is that at the cluster level, the key-value (Data) service might not be included based on the Couchbase Server version in use. If you want to make sure the key-value service is included, perform it at the bucket level.

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

A `DiagnosticsResult` has one interesting property over a ping result — it provides a cumulative `ClusterState` through the `state()` method. The state can be `ONLINE`, `DEGRADED` or `OFFLINE`. This allows to give a single, although simplistic, view on how your cluster is doing from a client point of view. The state is determined as follows:

* If at least one socket is open and all of them are connected, it is `ONLINE`
* If at least one is connected but not all are, it is `DEGRADED`
* If none are connected, it is `OFFLINE`

You can iterate over the individual states and apply a different algorithm if needed.