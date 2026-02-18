---
title: Quick Start with Prometheus Monitoring
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.7/modules/ROOT/pages/tutorial-prometheus.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/operator/2.7/tutorial-prometheus.html)

# Quick Start with Prometheus Monitoring

> Enable and setup Prometheus Monitoring for the Couchbase Autonomous Operator. 

> [!WARNING]
> Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer.

This guide walks through recommended procedures for enabling and configuring Prometheus monitoring of the Couchbase Autonomous Operator.

## [](#prerequisites)Prerequisites

Clone the [kube-prometheus](https://github.com/coreos/kube-prometheus) repository from GitHub, but do not create any manifests just yet.

```console
$ git clone https://github.com/coreos/kube-prometheus
```

Make sure you have a Kubernetes cluster running the Autonomous Operator with [monitoring enabled](howto-prometheus.md) and follow the Prerequisites section in the [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus) documentation.

## [](#manifests-setup)Manifests Setup

Currently, the `kube-prometheus` project includes a folder called `manifests` that includes all the resources necessary to run the Prometheus Operator. The Prometheus Operator creates our Prometheus deployment which scrapes endpoints continuously for Prometheus metrics. We will be creating these manifests in a [later step](#Create-the-manifests).

The Autonomous Operator, with monitoring enabled, exposes the Couchbase Prometheus metrics using Couchbase Server native support for metrics collection. Couchbase native support is available for Couchbase Server versions 7.0 or higher Our task is then to get Prometheus to discover and scrape these endpoints in order to monitor the overall cluster through the Prometheus UI and with custom Grafana dashboards.

In order for our Prometheus deployment to recognize and scrape Couchbase endpoints, we need to create a Couchbase specific service monitor, and a Couchbase metrics specific service.

> [!NOTE]
> This tutorial works on the basis that the manifests which bring up the relevant resources for Prometheus Operator are still located in the folder `manifests`. Please adjust accordingly if changes have been made since as the repository is experimental and subject to change.

### [](#create-the-couchbase-metrics-service)Create the Couchbase Metrics `Service`

The Couchbase Metrics `Service` will define the set of pods we want to monitor and the port to scrape on each.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: couchbase-metrics
  namespace: default (1)
  labels:
    app: couchbase
spec:
  ports:
  - name: metrics
    port: 8091 (2)
    protocol: TCP
  selector:
    app: couchbase
    couchbase_cluster: cb-example (3)
  sessionAffinity: ClientIP
```

| **1** | Make sure that the Service is in the same namespace as the Couchbase Cluster that you wish to scrape metrics from, otherwise no pods will be selected and no endpoints will be displayed on the Prometheus targets page (at http://localhost:9090/targets). |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | When Couchbase Cluster has TLS enabled, port 18091 must be used.                                                                                                                                                                                            |
| **3** | app:couchbase will select all Couchbase server pods in the specified namespace regardless of which cluster they belong to. Adding the couchbase\_cluster: cb-example selector will constrain the label selector to a specific cluster.                      |

Copy this YAML into a file named, for example, `couchbase-service.yaml` and make sure it is placed in the `manifests` directory.

### [](#create-the-couchbase-servicemonitor)Create the Couchbase `ServiceMonitor`

The `ServiceMonitor` tells Prometheus to monitor the `Service` resource we just defined which then enables Prometheus to scrape for metrics provided by Couchbase Server.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: cb-example-auth
  namespace: default
stringData:
  username: <my-cb-username>
  password: <my-cb-password>
---
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: couchbase
  namespace: default (1)
  labels:
    app: couchbase
spec:
  endpoints:
  - port: metrics       (2)
    interval: 5s        (3)
    basicAuth:          (4)
      password:
        name: cb-example-auth
        key: password
      username:
        name: cb-example-auth
        key: username
    tlsConfig: {}       (5)
  namespaceSelector:
    matchNames:
    - default (6)
  selector:
    matchLabels:
      app: couchbase (7)
```

| **1** | You may wish to include our Couchbase ServiceMonitor in the monitoring namespace along with the other ServiceMonitors included in the provided kube-prometheus manifests. For examples of this tutorial we have just left it in the default namespace for ease of use.                                                                                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The port may be a literal port number as defined in the couchbase-metrics service, or may reference the port in the same service by name.                                                                                                                                                                                                                                                   |
| **3** | interval tells Prometheus how often to scrape the endpoint.                                                                                                                                                                                                                                                                                                                                 |
| **4** | Prometheus Operator can authenticate to Couchbase using the same username and password as the Couchbase Operator as long as the authentication Secret also exists in the same namespace as the ServiceMonitor resource.                                                                                                                                                                     |
| **5** | The tlsConfig is required when the metric target is exposed over TLS. Refer to the [TLS Configuration Reference](https://prometheus-operator.dev/docs/operator/api/#monitoring.coreos.com/v1.TLSConfig) documentation for supported attributes. In production you should ensure that your client certificates are signed by the same root CA that is installed within the Couchbase Server. |
| **6** | Here we want to match the namespace of the Couchbase Metrics Service we have just created.                                                                                                                                                                                                                                                                                                  |
| **7** | Similar to the namespaceSelector, this is a simple [labelSelector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) that will look for our Service through label discovery.                                                                                                                                                                                       |

Copy this YAML into a file named `couchbase-serviceMonitor.yaml` for example, and save it in the `manifests` directory. If we were to just run with this `ServiceMonitor` and without any defined `Service` we would see on our Prometheus targets page a section for Couchbase endpoints but none showing.

## [](#create-the-manifests)Create the Manifests

Follow the specific commands given in the `kube-prometheus` documentation to bring up our created resources along with the other provided default manifests.

Components such as Prometheus, Alertmanager, Node Exporter and Grafana should then startup and we can confirm this by inspecting the pods in the namespace `monitoring`.

* Kubernetes
* OpenShift

```console
$ kubectl get pods -n monitoring
```

```console
$ oc get pods -n monitoring
```

Check that our `ServiceMonitor` and `Service` have been created.

* Kubernetes
* OpenShift

```console
$ kubectl get servicemonitor couchbase
$ kubectl get service couchbase-metrics
```

```console
$ oc get servicemonitor couchbase
$ oc get service couchbase-metrics
```

To check that all is working correctly with the Prometheus Operator deployment, run the following command to view the logs:

* Kubernetes
* OpenShift

```console
$ kubectl logs -f deployments/prometheus-operator -n monitoring prometheus-operator
```

```console
$ oc logs -f deployments/prometheus-operator -n monitoring prometheus-operator
```

Any potential issues that may arise should be fairly straight forward to debug and understand. One you may run into is the `ServiceMonitor` reporting problems due to your bearer token Secret not being created.

Once all pods are ready and running, in order to access Prometheus and Grafana, follow the relevant steps in the `kube-prometheus` documentation.