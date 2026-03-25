---
title: Operator Deployment Settings
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/reference-operator-configuration.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.6@operator::reference-operator-configuration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/reference-operator-configuration.html)

# Operator Deployment Settings

## [](#operator-deployment)Operator Deployment

The Couchbase Autonomous Operator configuration is defined below. This is intended as a reference only, and you should prefer the use of the [cao utility](tools/cao.md) or [Helm](helm-setup-guide.md), as these will handle configuration for you and provide an abstraction layer, less prone to modification.

> [!IMPORTANT]
> Most of the fields in the Operator configuration should never be changed and it is recommended that you use the configuration as is. However, there are some exceptions noted below.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: couchbase-operator
spec:
  replicas: 1 (1)
  selector:
    matchLabels:
      app: couchbase-operator
  template:
    metadata:
      labels:
        app: couchbase-operator
    spec:
      containers:
      - name: couchbase-operator
        image: couchbase/operator:2.0.0 (2)
        command:
        - couchbase-operator
        args: (3)
        - --pod-create-timeout=10m0s
        env: (4)
        - name: WATCH_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        ports:
        - containerPort: 8080 (5)
          name: http
        - containerPort: 8383 (6)
          name: prometheus
      serviceAccountName: couchbase-operator (7)
```

| **1** | The number of replicas should not be changed. The deployment will ensure the Operator is always running. The Operator uses leadership election to ensure only one instance is processing data at once, so replicas are redundant. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The image should remain unchanged unless you are using a custom image. The Operator is a static binary; the use of an operating system image is redundant and a potential security vulnerability.                                 |
| **3** | The container arguments can be modified to suit your requirements. Valid flags are documented [below](#command-line-arguments).                                                                                                   |
| **4** | The WATCH\_NAMESPACE and POD\_NAME environment variables are required by the underlying library and can not be modified.                                                                                                          |
| **5** | The HTTP container port can be modified, however this will affect log collection with the [cao](tools/cao.md) tool.                                                                                                               |
| **6** | The Prometheus container port is fixed and cannot be modified at present.                                                                                                                                                         |
| **7** | The Operator must be run as a service account with the [correct roles](reference-operator-rbac.md) to function.                                                                                                                   |

## [](#command-line-arguments)Command-line Arguments

\--concurrency

**Type**: `integer`

**Default**: `4`

This argument controls how many Couchbase clusters can be reconciled at the same time.

The Operator can manage multiple Couchbase clusters regardless of this setting, however if set too low clusters may have to wait for a worker to become available before being inspected and reconciled. This is especially relevant where a Couchbase cluster can block others from being repaired due to a long running process such as a rebalance.

\--listen-addr <integer>

**Type**: `integer`

**Default**: `8080`

This argument controls the Operator HTTP server. It is primarily used to expose debugging information for support requests.

\--pod-create-timeout

**Type**: `string`

**Default**: `10m`

The Operator allows the timeout of pod creation to be manually configured. It is primarily intended for use on cloud platforms where the deployment of multiple volumes and pulling of a Couchbase Server container image may take a longer time than the default timeout period.

Valid values are any string that is a [Go language duration](https://golang.org/pkg/time/#ParseDuration).

\--zap-devel | --zap-devel=false

**Type**: `boolean`

**Default**: `false`

Enables development mode logging, which while more human readable, is less easily integrated into centralized log shipping and collection infrastructure. Development mode sets `-zap-encoder` default to `console`, `-zap-log-level` to `debug`, and `-zap-stacktrace-level` to `warn`. Production mode sets `-zap-encoder` default to `json`, `-zap-log-level` to `info`, and `-zap-stacktrace-level` to `error`.

\--zap-encoder

**Type**: `string`

**Enumeration**: `json`, `console`

**Default**: see `-zap-devel`

Allows log format to be specified. By default, `json` logging provides a machine readable format easily integrated into centralized logging platforms. The alternative `console` logging, is more easily readable to the human, but less easily integrated into centralized log shipping and collection infrastructure.

\--zap-log-level

**Type**: `string`

**Enumeration**: `debug`, `info`, `error`, `2`

**Default**: see `-zap-devel`

Controls the verbosity of log output. Informational logging displays errors and informational messages. Debug logging displays basic debug, error and informational messages. Level 2 debug logging displays full debug, error and informational messages, including Couchbase server API calls.

> [!IMPORTANT]
> When using logging level `2` be aware this will print all data payloads to and from Couchbase server. This data may contain user names and passwords in plain text along with any other sensitive information concerning naming of resources.

\--zap-stacktrace-level

**Type**: `string`

**Enumeration**: `info`, `error`

**Default**: see `-zap-devel`

Controls at what level a log message generates a stack trace for debugging purposes.

## [](#environment-variables)Environment Variables

When running in different contexts such as Red Hat Marketplace in [disconnected mode](https://docs.openshift.com/container-platform/4.6/operators/operator%5Fsdk/osdk-generating-csvs.html#olm-enabling-operator-for-restricted-network%5Fosdk-generating-csvs), additional environment variables may be added to adjust behavior of the Autonomous Operator.

The following example shows supported image variables that can be used to override the default images provided to the Autonomous Operator.

```yaml
  spec:
    containers:
    - args:
      - --pod-create-timeout=10m0s
      env:
      - name: RELATED_IMAGE_COUCHBASE_SERVER (1)
        value: registry.connect.redhat.com/couchbase/server@sha256:76f227833f929115adbbbc28988f721b2af9aa825219ee9429482a2287a91603
      - name: RELATED_IMAGE_COUCHBASE_BACKUP
        value: registry.connect.redhat.com/couchbase/operator-backup@sha256:e46c4e32e645df4b9a6a2cfda04fbf8ecb66da1fdf47d073de9ec49796bd3935
      - name: RELATED_IMAGE_COUCHBASE_METRICS
        value: registry.connect.redhat.com/couchbase/exporter@sha256:fda5d8278acb72682ebc0151ab77f4c212ba3c7b850e3074b54408cd85cf0df6
```

| **1** | The Couchbase Server image which is equivalent to the [spec.Image](https://docs.couchbase.com/operator/current/resource/couchbasecluster.html#couchbaseclusters-spec-image) of the Couchbase Cluster resource. When used in disconnected mode for Red Hat Marketplace, the image tag must be a sha256 value. During deployment OpenShift will pre-download all related images used by Operator for offline use on premises. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The [spec.EnvImagePrecedence](https://docs.couchbase.com/operator/current/resource/couchbasecluster.html#couchbaseclusters-spec-env-image-precedence) of the CouchbaseCluster resource must also be set to true to give environment variables precedence over default images provided for Couchbase Server and sidecar images.