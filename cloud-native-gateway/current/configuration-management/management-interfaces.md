---
title: Management Interfaces
description: The web management interface, health checks, and runtime
  configuration options for Cloud Native Gateway.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/configuration-management/pages/management-interfaces.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:configuration-management:management-interfaces.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/configuration-management/management-interfaces.html)

# Management Interfaces

> The web management interface, health checks, and runtime configuration options for Cloud Native Gateway. 

Cloud Native Gateway provides a lightweight HTTP management interface for health monitoring, metrics, and runtime diagnostics. This interface uses a dedicated web port, separate from the client-facing gRPC and Data API ports. The default port is `9091`.

## [](#rest-api)REST API

### [](#health-and-readiness-endpoints)Health and Readiness Endpoints

Cloud Native Gateway exposes Kubernetes-compatible health and readiness probes:

| Endpoint | Method | Description                                                                                                                                                                                                                                                        |
| -------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| /live    | GET    | Liveness probe. Returns 200 OK as soon as the Cloud Native Gateway process is running. Use this for Kubernetes livenessProbe configuration.                                                                                                                        |
| /ready   | GET    | Readiness probe. Returns 200 OK once Cloud Native Gateway has connected to Couchbase Server and is ready to serve traffic. Returns 503 Service Unavailable while Cloud Native Gateway is still initializing. Use this for Kubernetes readinessProbe configuration. |
| /health  | GET    | Alias for /ready. Returns the same readiness status.                                                                                                                                                                                                               |
| /metrics | GET    | Prometheus metrics endpoint. See [Monitoring and Metrics](monitoring-metrics.md) for details on available metrics.                                                                                                                                                 |

### [](#example-kubernetes-probe-configuration)Example Kubernetes Probe Configuration

```yaml
containers:
  - name: cloud-native-gateway
    livenessProbe:
      httpGet:
        path: /live
        port: 9091
      initialDelaySeconds: 5
      periodSeconds: 10
    readinessProbe:
      httpGet:
        path: /ready
        port: 9091
      initialDelaySeconds: 10
      periodSeconds: 5
```

### [](#go-runtime-profiling-endpoints)Go Runtime Profiling Endpoints

The `--pprof` flag enables Go runtime profiling endpoints under `/debug/pprof/` on the web port:

| Endpoint               | Description                                      |
| ---------------------- | ------------------------------------------------ |
| /debug/pprof/          | Index of available profiles.                     |
| /debug/pprof/profile   | CPU profile. The default duration is 30 seconds. |
| /debug/pprof/heap      | Heap memory profile.                             |
| /debug/pprof/goroutine | Stack traces of all current goroutines.          |
| /debug/pprof/allocs    | Allocation profile.                              |
| /debug/pprof/block     | Blocking profile.                                |
| /debug/pprof/mutex     | Mutex contention profile.                        |
| /debug/pprof/trace     | Execution trace.                                 |

> [!IMPORTANT]
> pprof endpoints expose detailed runtime internals. Enable them only when actively investigating a performance issue, and do not use `--pprof` in production deployments.

### [](#grpc-health-check)gRPC Health Check

In addition to the HTTP health endpoints, Cloud Native Gateway implements the [standard gRPC health checking protocol](https://grpc.io/docs/guides/health-checking/) on the Protostellar gRPC port. Verify this using [gRPCurl](https://github.com/fullstorydev/grpcurl), which is "like curl, but for gRPC". The [gRPC standard health check](https://grpc.io/docs/guides/health-checking/) is a simple way to do this.

Call `grpcurl` against a default `Health/Check` once you have the definition. To get the RPC definition:

```console
$ curl -o health.proto https://raw.githubusercontent.com/grpc/grpc-proto/master/grpc/health/v1/health.proto
```

Then check against the `healthcheck` endpoint with:

```console
$ grpcurl --insecure -proto health.proto -d '{ "service": "hello" }' localhost:18098 grpc.health.v1.Health/Check
```

And you should see a response:

```console
{
  "status": "SERVING"
}
```

Individual gRPC services also report their health status, so you can query a specific service:

```console
$ grpcurl --insecure -proto health.proto localhost:18098 grpc.health.v1.Health/Check \
    -d '{"service": "couchbase.kv.v1.KvService"}'
```