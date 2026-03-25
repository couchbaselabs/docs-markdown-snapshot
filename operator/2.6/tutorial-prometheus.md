---
title: Quick Start with Prometheus Monitoring
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/tutorial-prometheus.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.6@operator::tutorial-prometheus.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/tutorial-prometheus.html)

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

Make sure you have a Kubernetes cluster running the Autonomous Operator with [monitoring enabled](howto-prometheus.md) and follow the Prerequisites section in the `kube-prometheus` documentation.

## [](#manifests-setup)Manifests Setup

Currently, the `kube-prometheus` project includes a folder called `manifests` that includes all the resources necessary to run the Prometheus Operator. The Prometheus Operator creates our Prometheus deployment which scrapes endpoints continuously for Prometheus metrics. We will be creating these manifests in a [later step](#Create-the-manifests).

The Autonomous Operator, with monitoring enabled, exposes the Couchbase Prometheus metrics on the sidecar containers running in each Couchbase Server pod. Our task is then to get Prometheus to discover and scrape these endpoints in order to monitor the overall cluster through the Prometheus UI and with custom Grafana dashboards.

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
    port: 9091 (2)
    protocol: TCP
  selector:
    app: couchbase
    couchbase_cluster: cb-example (3)
```

| **1** | Make sure that the Service is in the same namespace as the Couchbase Cluster that you wish to scrape metrics from, otherwise no pods will be selected and no endpoints will be displayed on the Prometheus targets page (at http://localhost:9090/targets). |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Keep this port as its default value of 9091 as this is the default port the Couchbase Exporter will be writing to.                                                                                                                                          |
| **3** | app:couchbase will select all Couchbase server pods in the specified namespace regardless of which cluster they belong to. Adding the couchbase\_cluster: cb-example selector will constrain the label selector to a specific cluster.                      |

Copy this YAML into a file named, for example, `couchbase-service.yaml` and make sure it is placed in the `manifests` directory.

### [](#create-the-couchbase-servicemonitor)Create the Couchbase `ServiceMonitor`

The `ServiceMonitor` tells Prometheus to monitor the `Service` resource we just defined which then enables Prometheus to scrape for metrics provided by the Couchbase exporter.

```yaml
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
    bearerTokenSecret:  (4)
      key: token (5)
      name: cb-metrics-token (6)
  namespaceSelector:
    matchNames:
    - default (7)
  selector:
    matchLabels:
      app: couchbase (8)
```

| **1** | You may wish to include our Couchbase ServiceMonitor in the monitoring namespace along with the other ServiceMonitors included in the provided kube-prometheus manifests. For examples of this tutorial we have just left it in the default namespace for ease of use.                                                                                                                       |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The port may be a literal port number as defined in the couchbase-metrics service, or may reference the port in the same service by name.                                                                                                                                                                                                                                                    |
| **3** | interval tells Prometheus how often to scrape the endpoint.                                                                                                                                                                                                                                                                                                                                  |
| **4** | If it is specified in the CouchbaseCluster spec, by [spec.monitoring.prometheus.authorizationSecret](howto-prometheus.md#Configuration), we then need to provide the correct Secret details in order for Prometheus to be able to gain access to the scrape endpoints. Please see [Configure Prometheus Metrics Collection](howto-prometheus.md#Configuration) on how to create said Secret. |
| **5** | Pass in the value of the key field in the secret data. In this example the key value is token if we have the corresponding Secret with value {data: {token: base64encodedTokenHere}}.                                                                                                                                                                                                        |
| **6** | name is simply the name of your Secret containing the bearer token.                                                                                                                                                                                                                                                                                                                          |
| **7** | Here we want to match the namespace of the Couchbase Metrics Service we have just created.                                                                                                                                                                                                                                                                                                   |
| **8** | Similar to the namespaceSelector, this is a simple [labelSelector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) that will look for our Service through label discovery.                                                                                                                                                                                        |

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

## [](#working-with-the-prometheus-operator-helm-chart)Working with the Prometheus Operator Helm Chart

It is also possible to instead use the [Prometheus Operator Helm chart](https://github.com/helm/charts/tree/master/stable/prometheus-operator) which closely matches the `kube-prometheus` project. To do so we must make Prometheus aware of the additional Service Monitor to monitor our Couchbase metrics service.

We use a YAML file to include in the `values` argument in `helm install` which will introduce additional configuration into the Helm Chart. The following example YAML is almost an exact replica of the Service Monitor YAML example in the [earlier section](#create-the-couchbase-servicemonitor), but with a few important differences. These differences exist due to the way that the Helm Chart structure has been defined. For further information see the defined [values.yaml](https://github.com/helm/charts/tree/master/stable/prometheus-operator/values.yaml) in the Helm chart GitHub repository.

```yaml
prometheus:
  prometheusSpec:
    additionalServiceMonitors:
      - name: couchbase
        additionalLabels:
          - app: couchbase
        endpoints:
          - port: metrics
            interval: 5s
             bearerTokenFile:
               key: token
               name: cb-metrics-token
        namespaceSelector:
          matchNames:
            - default
        selector:
          matchLabels:
            app: couchbase
```

Once this YAML file is created and saved, we can then deploy the Prometheus Operator with Helm using the following command.

```bash
helm install prometheus-operator stable/prometheus-operator --values your-helm-config.yaml -n your-namespace
```

To make sure the Helm chart will be deployed with the additional configuration, you can add the argument `--dry-run` to the command to view the intended configuration.

```bash
helm install prometheus-operator stable/prometheus-operator --values your-helm-config.yaml -n your-namespace --dry-run
```

If you wish to deploy the Prometheus Operator in a separate namespace, make sure to create that namespace if it does not already exist.

* Kubernetes
* OpenShift

```console
$ kubectl create namespace your-namespace
```

```console
$ oc create namespace your-namespace
```

Now all we need to do is make sure our Couchbase service and Service Monitor are deployed for the Prometheus Operator to recognize. However the Prometheus Operator Helm chart deployment requires an extra bit of configuration to the Service Monitor for the Service Monitor to show up in Prometheus. The Prometheus Operator has a `labelSelector` defined looking for the label `release: prometheus-operator` so we need to add this to our Couchbase Service Monitor. With this label added the Service Monitor will look something like the following.

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: couchbase
  namespace: default
  labels:
    app: couchbase
    release: prometheus-operator
spec:
  endpoints:
  - port: metrics
    interval: 5s
    bearerTokenSecret:
      key: token
      name: cb-metrics-token
  namespaceSelector:
    matchNames:
    - default
  selector:
    matchLabels:
      app: couchbase
```

Deploy this slightly modified `ServiceMonitor` and the Couchbase metrics service.

We can now use commands similar to the ones found in the [kube-prometheus](https://github.com/coreos/kube-prometheus) documentation, to access Prometheus Server and Grafana.

* Kubernetes
* OpenShift

```console
$ kubectl port-forward -n your-namespace pod/prometheus-prometheus-operator-prometheus-0 9090:9090
$ kubectl port-forward -n your-namespace deployment/prometheus-operator-grafana 3000:3000
```

```console
$ oc port-forward -n your-namespace pod/prometheus-prometheus-operator-prometheus-0 9090:9090
$ oc port-forward -n your-namespace deployment/prometheus-operator-grafana 3000:3000
```

An important distinction however is that the Grafana default password will be different. At time of writing the default password is `prom-operator` rather than `admin` as it is in `kube-prometheus`. The default password can be discovered in the `prometheus-operator-grafana` secret through base64 decoding.