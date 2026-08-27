---
title: Configure Prometheus Metrics Collection
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.5/modules/ROOT/pages/howto-prometheus.adoc
  xref: xref:2.5@operator::howto-prometheus.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/howto-prometheus.html)

# Configure Prometheus Metrics Collection

> You can set up the Autonomous Operator to use the Couchbase Exporter or Couchbase Server's native support for metrics collection. The Couchbase Exporter is a ["sidecar" container](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/#how-pods-manage-multiple-containers) that is injected into each Couchbase Server pod. Couchbase native support for metric collection exposes an Prometheus compatible endpoint on all Pods without the use of 3rd party tools. Couchbase native support is available for Couchbase Server versions 7.0 or higher and is the recommended way for collecting metrics with Prometheus. 

## [](#overview)Overview

Prometheus is the de facto metrics collection platform for use in Kubernetes environments. Prometheus can be used in conjunction with Couchbase server for several use cases such as monitoring, metering, and auto scaling. The ["Prometheus Operator"](https://prometheus-operator.dev/) is the recommended project to refer to for deploying and managing Prometheus alongside of Couchbase.

### [](#couchbase-prometheus-endpoint)Couchbase Prometheus Endpoint

As of Couchbase Server 7.0, a metric endpoint exists on each Couchbase Pod that is compatible with Prometheus metric collection. This endpoint exists by default and does not require any configuration within the `CouchbaseCluster` resource to begin receiving metrics into Prometheus. Therefore, the only setup required is to properly direct Prometheus to the Couchbase metric endpoint that requires the creation of a dedicated metric service along with a `ServiceMonitor` resource as outlined below. The `ServiceMonitor` is a Custom Resource created during installation of the Prometheus Operator that will direct Prometheus to monitor the dedicated metric service.

## [](#installing-prometheus-operator)Installing Prometheus Operator

Once you have your Couchbase Cluster running, fetch and install the Prometheus Operator stack. To install the Prometheus Operator stack follow the ["Quickstart Documentation"](https://github.com/prometheus-operator/kube-prometheus#quickstart).

## [](#integrating-couchbase-metrics)Integrating Couchbase Metrics

Create a Kubernetes service which targets the metrics endpoint on the Couchbase Clusters administrative console. This is the raw service that will be used by Prometheus for metric collection. Only one service is necessary for each Couchbase cluster since Couchbase aggregates statistics across all of the Pods. Save the following configuration as a file named `couchbase-prometheus-service.yaml` and make any modifications as described:

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app.couchbase.com/name: couchbase  (1)
  name: cb-metrics
spec:
  ports:
spec:
  ports:
  - name: metrics
    port: 8091 (2)
    protocol: TCP
  selector:
    app: couchbase
    couchbase_cluster: cb-example  (3)
    couchbase_server: "true"
  sessionAffinity: ClientIP
```

| **1** | Label allows service to be selected by the Prometheus ServiceMonitor resource.                                            |
| ----- | ------------------------------------------------------------------------------------------------------------------------- |
| **2** | Port to fetch metrics. When Couchbase Cluster has TLS enabled, port 18091 must be used.                                   |
| **3** | Replace cb-example with the name of your Couchbase cluster to ensure the correct Pods are selected for metric collection. |

Create the service resource in the same namespace as the `CouchbaseCluster` you wish to monitor, in this example we assume `default`:

```console
$ kubectl apply -f couchbase-prometheus-service.yaml
```

Now create a `ServiceMonitor` resource to direct Prometheus to monitor this metric service.

> [!IMPORTANT]
> The `ServiceMonitor` resources are expected to be in the same namespace as Prometheus Operator.
> 
> To use password authentication you will also need to add your authentication secret in the same namespace as the `ServiceMonitor` resource.
> 
> The default location of the Prometheus Operator is the `monitoring` namespace. If, for any reason, this is undesirable, or simply not feasible, the Prometheus Operator deployment resource can be modified to select `ServiceMonitor` resources from a different namespace by modifying the `serviceMonitorNamespaceSelector` as specified in the ["Prometheus Custom Resource Definition"](https://github.com/prometheus-operator/kube-prometheus/blob/f7d3019a8f1bf8b49402c77ad651c95ef16be68d/manifests/prometheus-prometheus.yaml#L46).

The following is an example `ServiceMonitor` configuration. Save as `couchbase-prometheus-monitor.yaml` after making any necessary modifications as described below:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: cb-example-auth
  namespace: monitoring
stringData:
  username: my-username
  password: my-password
---
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: couchbase-prometheus
  namespace: monitoring (1)
spec:
  endpoints:
  - interval: 5s
    port: metrics
    basicAuth:  (2)
      password:
        name: cb-example-auth
        key: password
      username:
        name: cb-example-auth
        key: username
    tlsConfig: {} (3)
  namespaceSelector: (4)
    matchNames:
    - default
    - monitoring
  selector:
    matchLabels:
      app.couchbase.com/name: couchbase (5)
```

| **1** | The ServiceMonitor must be installed in the same namespace as the Prometheus Operator.                                                                                                                                                                                                                                                                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Prometheus Operator can authenticate to Couchbase using the same username and password as the Couchbase Operator as long as the authentication Secret also exists in the same namespace as the ServiceMonitor resource.                                                                                                                                                                     |
| **3** | The tlsConfig is required when the metric target is exposed over TLS. Refer to the [TLS Configuration Reference](https://prometheus-operator.dev/docs/operator/api/#monitoring.coreos.com/v1.TLSConfig) documentation for supported attributes. In production you should ensure that your client certificates are signed by the same root CA that is installed within the Couchbase Server. |
| **4** | You need to explicitly state what namespaces to poll for services.                                                                                                                                                                                                                                                                                                                          |
| **5** | Selects the metric services to monitor. This corresponds to the Service labels used in the previous step.                                                                                                                                                                                                                                                                                   |

Commit the service monitor configuration:

```console
$ kubectl create -f couchbase-prometheus-monitor.yaml -n monitoring
```

## [](#verify)Verify

A quick way to check that metrics are being collected is to forward the Prometheus service port to your local machine and query the dashboard for Couchbase related metrics.

```console
$ kubectl --namespace monitoring port-forward svc/prometheus-k8s 9090
```

Try entering `kv_ops` into the metric search bar. If no results are returned, check Status → Targets for any unhealthy endpoints and also check the Prometheus Operator logs for additional information.

### [](#couchbase-prometheus-exporter)Couchbase Prometheus Exporter

The Autonomous Operator provides Prometheus integration for collecting and exposing Couchbase Server metrics via the [Couchbase Prometheus Exporter](https://github.com/couchbase/couchbase-exporter).

Prometheus metrics collection is enabled in the `CouchbaseCluster` resource. The configuration allows you to specify a Couchbase-provided container image that contains the Prometheus Exporter. The Autonomous Operator injects the image as a ["sidecar" container](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/#how-pods-manage-multiple-containers) in each Couchbase Server pod.

> [!NOTE]
> The Couchbase-supplied Prometheus Exporter container image is only supported on Kubernetes platforms in conjunction with the Couchbase Autonomous Operator.

## [](#couchbase-exporter-configuration)Couchbase Exporter Configuration

Prometheus metrics collection is enabled in the `CouchbaseCluster` resource.

```yaml
apiVersion: couchbase/v2
kind: CouchbaseCluster
spec:
  monitoring:
    prometheus:
      enabled: true (1)
      image: couchbase/exporter:1.0.8 (2)
      authorizationSecret: cb-metrics-token (3)
      refreshRate: 60 (4)
```

| **1** | Setting [couchbaseclusters.spec.monitoring.prometheus.enabled](resource/couchbasecluster.md#couchbaseclusters-spec-monitoring-prometheus-enabled) to true enables injection of the sidecar into Couchbase Server pods.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | If the [couchbaseclusters.spec.monitoring.prometheus.image](resource/couchbasecluster.md#couchbaseclusters-spec-monitoring-prometheus-image) field is left unspecified, then the dynamic admission controller will automatically populate it with the most recent container image that was available when the installed version of the Autonomous Operator was released. The default image for open source Kubernetes comes from [Docker Hub](https://hub.docker.com/r/couchbase/exporter), and the default image for OpenShift comes from [Red Hat Container Catalog](https://access.redhat.com/containers/#/vendor/couchbase). If pulling directly from the the Red Hat Container Catalog, then the path will be something similar to registry.connect.redhat.com/couchbase/exporter:1.0.8 (you can refer to the catalog for the most recent images). If image pull secrets are required to access the image, they are inherited from the Couchbase Server pod and can be set explicitly with the [couchbaseclusters.spec.servers.pod.spec.imagePullSecrets](resource/couchbasecluster.md#couchbaseclusters-spec-servers-pod) field or implicitly with a service account specified with the [couchbaseclusters.spec.servers.pod.spec.serviceAccountName](resource/couchbasecluster.md#couchbaseclusters-spec-servers-pod) field. |
| **3** | You can optionally specify a Kubernetes Secret that contains a bearer token value that clients will need to use to gain access to the Prometheus metrics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **4** | refreshRate changes how often the exporter polls Couchbase Server for bucket metrics. In server 7.0+ this can be an expensive operation depending upon the cluster size and number of buckets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

> [!NOTE]
> If you wish to create a Kubernetes secret with a bearer token, simply edit and create the following definition:
> 
> ```yaml
> apiVersion: v1
> kind: Secret
> metadata:
>   name: cb-metrics-token
> type: Opaque
> stringData:
>   token: your-plain-text-bearer-token-here
> ```
> 
> The `stringData` field allows you to put a non-base64 encoded string directly into the Secret, and Kubernetes will then encode the string for you when the Secret is created or updated.

Important Considerations

* You can enable/disable Prometheus metric collection at any time during the cluster's lifecycle. However, since `Pod` resources are immutable, enabling or disabling metric collection will require a rolling upgrade of the cluster.
* Only official Prometheus images provided by Couchbase are supported (with the exception of user-supplied images that specifically enable [customized metrics](#customizing-metrics)).  
In addition, you should ensure that your image source is trusted. The sidecar container requires access to the Couchbase cluster administrative credentials in order to login and perform collection. Granting these credentials to arbitrary code is potentially harmful.

## [](#customizing-metrics)Customizing Metrics

By default, the exporter collects all metrics from Couchbase Server, with each metric having a default name and default metadata associated with it. The exporter supports certain user-configurable customizations to these defaults.

The Couchbase Prometheus Exporter currently supports the following customizations:

* Change the namespace, subsystem, name, and help text for each metric.
* Enable and disable whether a metric is exported to Prometheus.

These customizations are enabled by building your own custom version of the Couchbase Prometheus Exporter container image. For instructions on how to create a custom metrics configuration and build it into a container image, refer to the [couchbase-exporter README](https://github.com/couchbase/couchbase-exporter#customizing-metrics).

## [](#using-exported-metrics)Using Exported Metrics

Once configured, active metrics can be collected from each Couchbase Server pod on port 9091.

The Autonomous Operator does not create or manage resources for third-party software. Prometheus scrape targets must be manually created by the user.

### [](#couchbase-cluster-auto-scaling)Couchbase Cluster Auto-scaling

The Autonomous Operator supports [auto-scaling Couchbase clusters](concept-couchbase-autoscaling.md). In order to properly take advantage of this feature, users must [expose Couchbase metrics through the Kubernetes custom metrics API](concept-couchbase-autoscaling.md#couchbase-metrics).

Discovery of available metrics can be performed through Prometheus [queries](https://github.com/couchbase/couchbase-exporter#queries). However, the Couchbase Exporter repository contains a convenient [list of the Couchbase metrics being exported](https://github.com/couchbase/couchbase-exporter/blob/master/example/config.json).

Some metric names are further explained in the Couchbase Server documentation:

* Data Service

  * [Getting Bucket Statistics](../../server/current/rest-api/rest-bucket-stats.md)
  * [Getting Bucket Information](../../server/current/rest-api/rest-buckets-summary.md)
  * [cbstats all](../../server/current/cli/cbstats/cbstats-all.md)
* Index Service

  * [Index Statistics API](../../server/current/index-rest-stats/index.md)
* Query Service

  * [Admin Rest API - Statistics](../../server/current/n1ql-rest-admin/index.md#%5Fstatistics)
* Search Service

  * [Getting Search Statistics](../../server/current/fts-rest-stats/index.md)
* Eventing Service

  * [Eventing Statistics API](../../server/current/eventing-rest-api/index.md)
* XDCR

  * [Getting XDCR Stats](../../server/current/rest-api/rest-xdcr-statistics.md)
* Clusters and Nodes

  * [Retrieving Cluster Information](../../server/current/rest-api/rest-cluster-get.md)
  * [Getting Cluster Tasks](../../server/current/rest-api/rest-get-cluster-tasks.md)
  * [Getting Group Information](../../server/current/rest-api/rest-servergroup-get.md)
  * [Getting Server Node Information](../../server/current/rest-api/rest-node-get-info.md)

## [](#related-links)Related Links

You might find the following resources helpful when setting up your Prometheus environment:

* Couchbase Blog — [Part 1](https://blog.couchbase.com/step-by-step-guide-for-running-couchbase-autonomous-operator-2-0-with-prometheus-part-1/) & [Part 2](https://blog.couchbase.com/step-by-step-guide-for-running-couchbase-autonomous-operator-2-0-with-prometheus-part-2/)
* [Couchbase Prometheus Exporter GitHub](https://github.com/couchbase/couchbase-exporter)
* [Prometheus Operator](https://prometheus-operator.dev)
* [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus)