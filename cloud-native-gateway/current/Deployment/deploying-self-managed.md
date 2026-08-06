---
title: Deploying in Self-Managed Environments
description: How to deploy Cloud Native Gateway as a standalone container or
  process for self-managed Couchbase Server environments outside of Kubernetes.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/Deployment/pages/deploying-self-managed.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:Deployment:deploying-self-managed.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/Deployment/deploying-self-managed.html)

# Deploying in Self-Managed Environments

> How to deploy Cloud Native Gateway as a standalone container or process for self-managed Couchbase Server environments outside of Kubernetes. 

## [](#container-based-deployment)Container-Based Deployment

You can deploy Cloud Native Gateway as a standalone Docker container that connects to an existing Couchbase Server cluster over the network.

### [](#basic-container-deployment)Basic Container Deployment

Docker Hub hosts Cloud Native Gateway container images. You may run containers with any number of different container execution platforms. This serves as a simple example which you may adapt to your environment. Run one instance connected to a Cluster in the docker network with:

```console
$ docker run -d \
    --name cloud-native-gateway \
    -p 9091:9091 \
    -p 18098:18098 \
    -p 18100:18100 \
    couchbase/cloud-native-gateway:{cng-version} \
    --cb-host couchbase-server.example.com \
    --cb-user couchbaseServerAdmin \
    --cb-pass Password123 \
    --dapi-port 18100 \
    --self-sign
```

Containers are also available on the Red Hat container registry. Pull and run them with Docker or podman:

```console
$ podman run -d \
    --name cloud-native-gateway \
    -p 9091:9091 \
    -p 18098:18098 \
    -p 18100:18100 \
    registry.connect.redhat.com/couchbase/cloud-native-gateway:{cng-version} \
    --cb-host couchbase-server.example.com \
    --cb-user couchbaseServerAdmin \
    --cb-pass Password123 \
    --dapi-port 18100 \
    --self-sign
```

These commands pull the container from different places, but both start Cloud Native Gateway with:

* Port 9091 exposed for the web port.
* Port 18098 exposed for the Protostellar gRPC interface.
* Port 18100 exposed for the Data API HTTPS interface.
* Username couchbaseServerAdmin used to connect to the Couchbase Server cluster.
* Password Password123 used to connect to the Couchbase Server cluster.
* Self-signed generated certificates — insecure, only use for development.
* Connection to a Couchbase Server cluster at `couchbase-server.example.com`.

Use the health endpoint to verify the gateway is healthy and reachable:

```console
$ curl localhost:9091/health
ok
```

### [](#container-deployment-with-tls)Container Deployment with TLS

Pull and run the Cloud Native Gateway container image with a secure TLS cert:

```console
$ docker run -d \
    --name cloud-native-gateway \
    -p 9091:9091 \
    -p 18098:18098 \
    -p 18100:18100 \
    -v /path/to/certs:/certs:ro \
    couchbase/cloud-native-gateway:{cng-version} \
    --cb-host couchbase-server.example.com \
    --cb-user couchbaseServerAdmin \
    --cb-pass Password123 \
    --dapi-port 18100 \
    --cert /certs/tls.crt \
    --key /certs/tls.key
```

This starts Cloud Native Gateway with:

* Port 9091 exposed for the web port.
* Port 18098 exposed for the Protostellar gRPC interface.
* Port 18100 exposed for the Data API HTTPS interface.
* Username couchbaseServerAdmin used to connect to the Couchbase Server cluster.
* Password Password123 used to connect to the Couchbase Server cluster.
* TLS certificates mounted from the host.
* Connection to a Couchbase Server cluster at `couchbase-server.example.com`.

If the Couchbase cluster uses TLS with the `couchbases://` connection scheme, provide the cluster's CA certificate:

```console
$ docker run -d \
    --name cloud-native-gateway \
    -p 18098:18098 \
    -p 18100:18100 \
    -v /path/to/certs:/certs:ro \
    couchbase/cloud-native-gateway:{cng-version} \
    --cb-host couchbases://couchbase-server.example.com \
    --cb-user couchbaseServerAdmin \
    --cb-pass Password123 \
    --dapi-port 18100 \
    --cert /certs/tls.crt \
    --key /certs/tls.key \
    --cluster-cert /certs/cluster-ca.crt
```

### [](#docker-and-docker-compose)Docker and Docker Compose

Use Docker Compose to manage and share the desired configuration for Cloud Native Gateway:

```yaml
version: '3'
services:
  couchbase:
    image: couchbase/server:7.6.0
    ports:
      - "8091-8096:8091-8096"
      - "11210:11210"

  cloud-native-gateway:
    image: couchbase/cloud-native-gateway:{cng-version}
    ports:
      - "9091:9091"
      - "18098:18098"
      - "18100:18100"
    volumes:
      - ./certs:/certs:ro
    command:
      - "--cb-host"
      - "couchbase"
      - "--cb-user"
      - "couchbaseServerAdmin"
      - "--cb-pass"
      - "Password123"
      - "--dapi-port"
      - "18100"
      - "--cert"
      - "/certs/tls.crt"
      - "--key"
      - "/certs/tls.key"
      - "--daemon"
    depends_on:
      - couchbase
```

## [](#supported-hosting-environments)Supported Hosting Environments

You can deploy Cloud Native Gateway in any environment that supports running containers or Go binaries:

### [](#virtual-machines-and-bare-metal)Virtual Machines and Bare Metal

You can build and run Cloud Native Gateway as a native Go binary from the source code at <https://github.com/couchbase/stellar-gateway>:

```console
$ git clone https://github.com/couchbase/stellar-gateway.git
$ cd stellar-gateway
$ go build -o stellar-gateway ./cmd/gateway
$ ./stellar-gateway \
    --cb-host 192.168.1.100 \
    --cert /etc/cng/tls.crt \
    --key /etc/cng/tls.key
```

For production VM deployments, run Cloud Native Gateway as a systemd service to verify automatic restart and log management.

### [](#multiple-instances)Multiple Instances

For greater throughput on multi-core machines, Cloud Native Gateway can run multiple internal server instances within a single process. The first instance binds to the configured ports. Additional instances bind to randomized ports. Use a local load balancer or service mesh to distribute traffic across all instances:

```console
$ ./stellar-gateway --self-sign --num-instances 4
```

### [](#kubernetes-without-the-couchbase-kubernetes-operator)Kubernetes Without the Couchbase Kubernetes Operator

If you're running Couchbase Server in Kubernetes but without the Couchbase Kubernetes Operator, you can deploy Cloud Native Gateway as a standalone Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloud-native-gateway
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cloud-native-gateway
  template:
    metadata:
      labels:
        app: cloud-native-gateway
    spec:
      containers:
        - name: cng
          image: couchbase/cloud-native-gateway:{cng-version}
          ports:
            - containerPort: 18098
              name: protostellar
            - containerPort: 18100
              name: data-api
          args:
            - "--cb-host"
            - "couchbase-cluster.couchbase.svc"
            - "--cb-user"
            - "couchbaseServerAdmin"
            - "--cb-pass"
            - "Password123"
            - "--dapi-port"
            - "18100"
            - "--cert"
            - "/certs/tls.crt"
            - "--key"
            - "/certs/tls.key"
          volumeMounts:
            - name: tls-certs
              mountPath: /certs
              readOnly: true
      volumes:
        - name: tls-certs
          secret:
            secretName: cng-tls
---
apiVersion: v1
kind: Service
metadata:
  name: cloud-native-gateway
spec:
  selector:
    app: cloud-native-gateway
  ports:
    - name: protostellar
      port: 18098
      targetPort: 18098
    - name: data-api
      port: 18100
      targetPort: 18100
```

This approach gives you full control over Cloud Native Gateway scaling, resource allocation, and placement independently of the Couchbase cluster.

### [](#configuration-options)Configuration Options

Cloud Native Gateway accepts the following key command-line options as flags:

| Option                       | Description                                                                                | Default       |
| ---------------------------- | ------------------------------------------------------------------------------------------ | ------------- |
| \--alpha-endpoints           | Enables alpha endpoints                                                                    | false         |
| \--auto-restart              | In auto-restart mode, runs in a child process to auto-restart on failure                   | false         |
| \--bind-address              | The local address to bind to                                                               | 0.0.0.0       |
| \--cb-creds-aws-id           | ID of secret in AWS Secrets Manager storing Couchbase Server credentials                   | None          |
| \--cb-creds-aws-region       | Region of the cb-creds-aws-id secret                                                       | None          |
| \--cb-creds-azure-id         | ID of secret in Azure Key Vault storing Couchbase Server credentials                       | None          |
| \--cb-creds-azure-vault-name | Name of key vault storing cb-creds-azure-id                                                | None          |
| \--cb-creds-gcp-id           | ID of secret in GCP Secret Manager storing Couchbase Server password                       | None          |
| \--cb-creds-gcp-project-id   | ID of project containing cb-creds-gcp-id                                                   | None          |
| \--cb-host                   | The Couchbase Server host                                                                  | localhost     |
| \--cb-host-is-local          | Specifies if the cb-host node is running locally                                           | false         |
| \--cb-pass                   | The Couchbase Server password                                                              | password      |
| \--cb-user                   | The Couchbase Server username                                                              | Administrator |
| \--cert                      | Path to default TLS cert                                                                   | None          |
| \--client-ca-cert            | Path to TLS CA cert for client certs for mTLS                                              | None          |
| \--cluster-cert              | Path to cluster TLS CA cert                                                                | None          |
| \--config                    | Specifies a config file to load                                                            | None          |
| \--cpuprofile                | Write CPU profile to a file                                                                | None          |
| \--daemon                    | In daemon mode, stellar-gateway does not exit on initial failure                           | false         |
| \--dapi-cert                 | Path to Data API TLS cert                                                                  | None          |
| \--dapi-key                  | Path to Data API private TLS key                                                           | None          |
| \--dapi-no-proxy-admin       | Disables administrator endpoints through proxies                                           | false         |
| \--dapi-port                 | The Data API port                                                                          | \-1           |
| \--dapi-proxy-services       | Specifies services exposed via \_p endpoint proxies                                        | None          |
| \--data-port                 | The Protostellar gRPC listen port                                                          | 18098         |
| \--debug                     | Enable debug mode                                                                          | false         |
| \--disable-metrics           | Disable metrics                                                                            | false         |
| \--disable-otlp-metrics      | Disable sending metrics to OTLP                                                            | false         |
| \--disable-otlp-traces       | Disable sending traces to OTLP                                                             | false         |
| \--disable-traces            | Disable tracing                                                                            | false         |
| \--grpc-cert                 | Path to gRPC TLS cert                                                                      | None          |
| \--grpc-key                  | Path to gRPC private TLS key                                                               | None          |
| \-h, --help                  | Help for stellar-gateway                                                                   | N/A           |
| \--key                       | Path to default private TLS key                                                            | None          |
| \--log-level                 | The log level to run at                                                                    | info          |
| \--num-instances             | Number of internal gateway instances to run for multi-core utilization                     | 1             |
| \--otel-exporter-headers     | A comma-separated list of OTLP exporter headers, for example header1=value1,header2=value2 | None          |
| \--otlp-endpoint             | OpenTelemetry endpoint to send telemetry to                                                | None          |
| \--pprof                     | Enable pprof endpoints                                                                     | false         |
| \--rate-limit                | Specifies the maximum requests per second to allow                                         | None          |
| \--self-sign                 | Specifies to allow a self-signed certificate                                               | false         |
| \--server-group              | Specifies the server group name                                                            | None          |
| \--shutdown-timeout          | The graceful shutdown timeout                                                              | 30s           |
| \--single-user-auth          | Enables single-user authenticating to gRPC and Data API                                    | false         |
| \--trace-everything          | Enables tracing of all components                                                          | false         |
| \-v, --version               | Version for stellar-gateway                                                                | N/A           |
| \--watch-config              | Indicates whether to watch the config file for changes                                     | false         |
| \--web-port                  | The web metrics/health port                                                                | 9091          |

You can also provide the config through a TOML config file. A sample config file for a basic deployment would be:

```toml
cb-host = "couchbase-server.example.com"
cb-user = "couchbaseServerAdmin"
cb-pass = "Password123"
dapi-port = 18100
cert = "/certs/tls.crt"
key = "/certs/tls.key"
```

Once saved, this is then passed to the Cloud Native Gateway process through the --config flag:

```toml
$ ./stellar-gateway --config "config.toml"
```

When using a config file you can make the process watch for changes to the config file by specifying `--watch-config=true`. This allows for dynamic configuration of the log-level or rate-limit for Cloud Native Gateway. Changes to any other settings require a restart of the process to take effect.