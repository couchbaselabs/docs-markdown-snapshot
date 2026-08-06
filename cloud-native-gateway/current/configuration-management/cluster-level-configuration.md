---
title: Cluster Level Configuration
description: Ports, TLS certificates, and service enablement options for Cloud
  Native Gateway.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/configuration-management/pages/cluster-level-configuration.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:configuration-management:cluster-level-configuration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/configuration-management/cluster-level-configuration.html)

# Cluster Level Configuration

> Ports, TLS certificates, and service enablement options for Cloud Native Gateway. 

Cloud Native Gateway accepts configuration through command-line flags, environment variables prefixed with `STG_`, or a configuration file. You can also reload the configuration at runtime by sending a `SIGHUP` signal or by enabling `--watch-config` on a configuration file.

## [](#ports)Ports

Cloud Native Gateway exposes up to 3 network listeners, each serving a distinct role.

| Service        | Default Port | Flag         | Description                                                                                                                 |
| -------------- | ------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| gRPC           | 18098        | \--data-port | The gRPC interface used by Couchbase SDKs connecting with the couchbase2:// scheme.                                         |
| Data API HTTPS | Disabled     | \--dapi-port | The RESTful HTTPS interface for document operations and service passthrough. Defaults to \-1, which disables the interface. |
| Web / Metrics  | 9091         | \--web-port  | An HTTP endpoint that serves Prometheus metrics, health checks, and optional pprof debug endpoints.                         |

All listeners bind to the address specified by `--bind-address`. The default is `0.0.0.0`. Cloud Native Gateway automatically determines the address advertised to clients from the bind address.

Setting a port to `-1` disables that listener entirely. Setting a port to `0` causes the operating system to assign an available ephemeral port.

## [](#tls-configuration)TLS Configuration

All client-facing services (gRPC and Data API) require TLS. Cloud Native Gateway supports several certificate configurations.

### [](#self-signed-certificates-for-development)Self-Signed Certificates for Development

For development and testing, Cloud Native Gateway can generate a self-signed certificate at startup:

```console
$ ./cloud-native-gateway --self-sign
```

> [!WARNING]
> Do not use self-signed certificates in production deployments.

### [](#shared-certificate)Shared Certificate

You can share a single certificate and private key across both the gRPC and Data API interfaces:

```console
$ ./cloud-native-gateway --cert /path/to/cert.pem --key /path/to/key.pem
```

### [](#per-service-certificates)Per-Service Certificates

You can provide separate certificates for the gRPC and Data API interfaces. Per-service flags take precedence compared to the shared `--cert` / `--key` flags:

| Flag                       | Description                                              |
| -------------------------- | -------------------------------------------------------- |
| \--grpc-cert / \--grpc-key | Certificate and key for the Protostellar gRPC interface. |
| \--dapi-cert / \--dapi-key | Certificate and key for the Data API HTTPS interface.    |

### [](#cluster-ca-certificate)Cluster CA Certificate

When connecting to Couchbase Server over TLS with `couchbases://`, provide the cluster's CA certificate so Cloud Native Gateway can verify the server:

```console
$ ./cloud-native-gateway --cb-host couchbases://my-cluster --cluster-cert /path/to/cluster-ca.pem
```

### [](#mutual-tls-authentication)Mutual TLS Authentication

Cloud Native Gateway supports mutual TLS for client authentication. Provide the CA certificate that signed the client certificates:

```console
$ ./cloud-native-gateway --cert /path/to/cert.pem --key /path/to/key.pem \
    --client-ca-cert /path/to/client-ca.pem
```

When you configure a client CA, Cloud Native Gateway verifies client certificates if presented. If the client sends no certificate, Cloud Native Gateway allows the connection anyway. Clients that do not present a certificate can still authenticate using Basic authentication.

### [](#certificate-reloading)Certificate Reloading

Cloud Native Gateway does not support automatic certificate file watching. Certificate changes require restarting the gateway.

## [](#enable-and-disable-cloud-native-gateway)Enable and Disable Cloud Native Gateway

You can enable or disable each Cloud Native Gateway interface independently by setting its port flag. Use a positive port number to enable a service, `-1` to disable it, or `0` to let the OS choose an ephemeral port.

### [](#enabling-individual-services)Enabling Individual Services

The gRPC interface runs on port 18098 by default. The Data API does not run by default. To enable the Data API, set `--dapi-port` to a valid port number:

```console
$ ./cloud-native-gateway --self-sign --dapi-port 18099
```

### [](#disabling-individual-services)Disabling Individual Services

To run Cloud Native Gateway with only the Data API and no gRPC interface:

```console
$ ./cloud-native-gateway --self-sign --data-port -1 --dapi-port 18099
```

### [](#daemon-mode)Daemon Mode

By default, Cloud Native Gateway exits if it cannot connect to Couchbase Server at startup. In daemon mode, Cloud Native Gateway retries the connection every 5 seconds until the cluster becomes available:

```console
$ ./cloud-native-gateway --self-sign --daemon
```

Use daemon mode in Kubernetes deployments where Cloud Native Gateway may start before Couchbase Server is ready.

### [](#auto-restart-mode)Auto-Restart Mode

Cloud Native Gateway includes a built-in watchdog that automatically restarts the gateway process on unexpected crashes:

```console
$ ./cloud-native-gateway --self-sign --auto-restart
```

The watchdog runs as a parent process and restarts the gateway child process with a 1-second delay after a crash.

### [](#graceful-shutdown)Graceful Shutdown

Cloud Native Gateway performs a graceful shutdown on `SIGINT` or `SIGTERM`. The default shutdown timeout is 30 seconds. To change it:

```console
$ ./cloud-native-gateway --shutdown-timeout 60s
```

During graceful shutdown, Cloud Native Gateway stops accepting new connections and drains in-flight requests before exiting. A second `SIGINT` forces an immediate shutdown.