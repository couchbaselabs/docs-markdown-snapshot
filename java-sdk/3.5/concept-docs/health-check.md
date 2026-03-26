---
title: Health Check
description: Health Check provides ping() and diagnostics() tests for the health
  of the network and the cluster.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.5/modules/concept-docs/pages/health-check.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.5@java-sdk:concept-docs:health-check.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.5/concept-docs/health-check.html)

# Health Check

> Health Check provides ping() and diagnostics() tests for the health of the network and the cluster. 

Working in distributed environments is _hard_. Latencies come and go, so do connections in their entirety. Is it a network glitch, or is the remote cluster down? Sometimes just knowing the likely cause is enough to get a good start on a workaround, or at least avoid hours wasted on an inappropriate solution.

Health Check enables useful diagnostics on the state of Couchbase Clusters across networks. `Ping` and `diagnostics` methods on the bucket and cluster objects respectively, can give us information about the current state of nodes, and their connections.

## [](#uses)Uses

'Ping\` provides a raw JSON payload suitable for feeding into reactive log and aggregation components, including monitoring systems like _Splunk_, _ElasticSearch_, and _Nagios_. It can also help keep connections alive if you are operating across an environment which aggressively closes down unused connections.

`Diagnostics` provides a strongly typed API for proactive, pull-based monitoring systems, such as:

* [Kubernetes Liveness and Readiness Probes via HTTP or CLI commands](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/).
* [Docker Health Check with CLI commands](https://docs.docker.com/engine/reference/builder/#healthcheck).
* [AWS ELB through HTTP](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html).

This API does not provide binary yes/no answers about the health of the cluster; rather it summarizes as much information as possible, for the application developer to assemble a complete, contextual view and come to a conclusion.

Note: `Ping` may reopen a connection, so is not without side-effects. `Diagnostics` shows what the SDK _perceives_ as the current state of the network and services — it is without side-effects, but may not be up to date.

## [](#ping)Ping

A call to `ping` actively sends requests to the different services on the target cluster, measuring the latency and returning any errors as part of the report.

A `ping` can be performed either at the `Cluster` or at the `Bucket` level. They are very similar, although at the `Bucket` level also the Key/Value and View connections for the specific bucket are taken into account.

The report can either be analyzed in code or can be turned into JSON and printed:

```java
PingResult pingResult = cluster.ping();

System.out.println(pingResult.exportToJson());
```

You will see an output similar to this:

```json
{
   "services":{
      "query":[
         {
            "latency_us":1622,
            "state":"ok",
            "id":"0x01e2bef7",
            "remote":"10.143.200.101:8093",
            "local":"10.143.200.1:59775"
         },
         {
            "latency_us":1911,
            "state":"ok",
            "id":"0x8dff2eb6",
            "remote":"10.143.200.102:8093",
            "local":"10.143.200.1:59778"
         }
      ]
   },
   "sdk":"java/0.0.0 (Mac OS X 10.15.4 x86_64; OpenJDK 64-Bit Server VM 13+33)",
   "id":"fcc08fb8-5a56-40aa-8967-47bc7517382d",
   "version":2
}
```

On the target system, only the query service has been enabled at the cluster level according to this report. If you have more services configured (for example analytics or search) you could achieve the same effect by asking for only the query service to ping explicitly:

```java
      PingResult pingResult = cluster.ping(pingOptions().serviceTypes(EnumSet.of(ServiceType.QUERY)));

      System.out.println(pingResult.exportToJson());
```

If the ping is performed at the bucket level, the Key/Value and View sockets are also visible:

```json
{
   "services":{
      "query":[
         {
            "latency_us":1364,
            "state":"ok",
            "id":"0x178a666c",
            "remote":"10.143.200.102:8093",
            "local":"10.143.200.1:59864"
         },
         {
            "latency_us":1343,
            "state":"ok",
            "id":"0x65cda678",
            "remote":"10.143.200.101:8093",
            "local":"10.143.200.1:59865"
         }
      ],
      "kv":[
         {
            "latency_us":703,
            "namespace":"travel-sample",
            "state":"ok",
            "id":"0x2e2abd35",
            "remote":"10.143.200.102:11210",
            "local":"10.143.200.1:59869"
         },
         {
            "latency_us":1260,
            "namespace":"travel-sample",
            "state":"ok",
            "id":"0xf3fc7e9f",
            "remote":"10.143.200.101:11210",
            "local":"10.143.200.1:59868"
         }
      ],
      "views":[
         {
            "latency_us":9547,
            "namespace":"travel-sample",
            "state":"ok",
            "id":"0x712e8eca",
            "remote":"10.143.200.102:8092",
            "local":"10.143.200.1:59871"
         },
         {
            "latency_us":7863,
            "namespace":"travel-sample",
            "state":"ok",
            "id":"0x2c988f93",
            "remote":"10.143.200.101:8092",
            "local":"10.143.200.1:59873"
         }
      ]
   },
   "sdk":"java/0.0.0 (Mac OS X 10.15.4 x86_64; OpenJDK 64-Bit Server VM 13+33)",
   "id":"3ffecdae-5abe-413b-aa26-c2b2774ef872",
   "version":2
}
```

## [](#diagnostics)Diagnostics

Performing a `diagnostics()` call at the `Cluster` level is conceptually different from a ping, but still very useful. It returns information about the current state of all the connections inside the SDK without actually performing any I/O. So if you haven't done any operations against a service with a pool (i.e. Query) you might not see any sockets show up.

Similar to ping, you can turn a diagnostics result into JSON. The following code and output shows a state directly after bootstrap, without performing any query operations:

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

```json
{
   "services":{
      "kv":[
         {
            "state":"connecting"
         }
      ]
   },
   "sdk":"java/0.0.0 (Mac OS X 10.15.4 x86_64; OpenJDK 64-Bit Server VM 13+33)",
   "id":"484f20c4-f9c8-47c9-90b1-6901279066b0",
   "state":"offline",
   "version":2
}
```

If you perform a query and look at the diagnostics again, you'll see them show up in the report:

```json
{
   "services":{
      "query":[
         {
            "last_activity_us":3306,
            "state":"connected",
            "id":"0x809fa38a",
            "remote":"10.143.200.1:61127",
            "local":"10.143.200.101:8093"
         },
         {
            "state":"connected",
            "id":"0xc292ca2d",
            "remote":"10.143.200.1:61128",
            "local":"10.143.200.102:8093"
         }
      ],
      "kv":[
         {
            "last_activity_us":751662,
            "state":"connected",
            "id":"0x35b05053",
            "remote":"10.143.200.1:61125",
            "local":"10.143.200.101:11210"
         },
         {
            "last_activity_us":751304,
            "state":"connected",
            "id":"0x4510d5e8",
            "remote":"10.143.200.1:61126",
            "local":"10.143.200.102:11210"
         }
      ]
   },
   "sdk":"java/0.0.0 (Mac OS X 10.15.4 x86_64; OpenJDK 64-Bit Server VM 13+33)",
   "id":"167f0f08-a6e0-4aca-8832-4e3ab688820e",
   "state":"online",
   "version":2
}
```