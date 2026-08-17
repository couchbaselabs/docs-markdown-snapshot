---
title: Deploying with Couchbase Kubernetes Operator
description: How to deploy Cloud Native Gateway as a sidecar alongside Couchbase
  Server pods using the CouchbaseKubernetes Operator in Kubernetes and
  OpenShift.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/Deployment/pages/deploying-CAO.adoc
  xref: xref:cloud-native-gateway:Deployment:deploying-CAO.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/Deployment/deploying-CAO.html)

# Deploying with Couchbase Kubernetes Operator

> How to deploy Cloud Native Gateway as a sidecar alongside Couchbase Server pods using the CouchbaseKubernetes Operator in Kubernetes and OpenShift. 

## [](#prerequisites)Prerequisites

Before deploying Cloud Native Gateway with the Couchbase Kubernetes Operator, verify the following:

* **Couchbase Kubernetes Operator** version 2.6.1 or later — You have installed the operator in your Kubernetes or OpenShift cluster.
* **Couchbase Server** version 7.2.2 or later is the target cluster image.
* **TLS certificates** — You have provisioned TLS certificates for Cloud Native Gateway, it requires a TLS certificate to serve both the gRPC/Protostellar and Data API interfaces. Store this certificate in a Kubernetes Secret.
* **Container image** — You can use the `couchbase/cloud-native-gateway` image from your container registry.

## [](#sidecar-deployment-per-couchbase-node)Sidecar Deployment per Couchbase Node

Cloud Native Gateway runs as a `sidecar` image to every Couchbase Server node in a cluster. The Couchbase Kubernetes Operator configures and manages this sidecar. The operator handles injecting the Cloud Native Gateway container, creating the Kubernetes Service, and managing the lifecycle.

To enable Cloud Native Gateway, add the `cloudNativeGateway` section to your `CouchbaseCluster` resource definition:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: mycluster
spec:
  networking:
    cloudNativeGateway:
      image: couchbase/cloud-native-gateway:latest
      tls:
        serverSecretName: cng-server-tls
```

The `serverSecretName` references a Kubernetes Secret containing the TLS certificate and key that Cloud Native Gateway uses for its gRPC and Data API endpoints.

When you apply this configuration, the operator:

1. Add a Cloud Native Gateway sidecar container to every Couchbase Server pod.
2. Create a Kubernetes `Service` that selects all Cloud Native Gateway containers, making them available as a single endpoint.
3. Configure Cloud Native Gateway to connect to the local Couchbase node on each pod.

> [!CAUTION]
> Adding Cloud Native Gateway to an existing cluster requires a rolling restart of pods, which triggers a rebalance. Plan for this operation during a maintenance window. The Couchbase Kubernetes Operator cannot yet use the later Kubernetes sidecar container APIs on most platforms, so changes to the Cloud Native Gateway configuration require pod recreation.

### [](#verifying-the-deployment)Verifying the Deployment

After applying the configuration, verify that Cloud Native Gateway pods are running:

```console
$ kubectl get pods -l app=couchbase
```

Each Couchbase pod should show an additional container in the `READY` column. For example, a pod that showed `1/1` should now show `2/2`.

Verify that the Cloud Native Gateway service exists:

```console
$ kubectl get services | grep cloud-native-gateway
```

You should see a service named `<cluster-name>-cloud-native-gateway-service`.

### [](#tls-certificate-setup)TLS Certificate Setup

Create a Kubernetes Secret with your TLS certificate and private key:

```console
$ kubectl create secret tls cng-server-tls \
    --cert=path/to/tls.crt \
    --key=path/to/tls.key
```

If you need Cloud Native Gateway to trust a custom Certificate Authority for client certificate authentication, include the CA certificate in the secret. You can also provide it through additional operator configuration.

For development and testing, Cloud Native Gateway supports a `--self-sign` flag that generates a self-signed certificate at startup. Do not use this in production.

## [](#kubernetes-networking-and-service-configuration)Kubernetes Networking and Service Configuration

Once you deploy Cloud Native Gateway, you need to expose it to client applications. The approach depends on where the clients are running.

### [](#clients-inside-the-kubernetes-cluster)Clients Inside the Kubernetes Cluster

If your applications run inside the same Kubernetes cluster, they can connect directly to the Cloud Native Gateway service using its cluster-internal DNS name:

```none
couchbase2://<cluster-name>-cloud-native-gateway-service.<namespace>.svc
```

You do not need additional networking configuration.

### [](#exposing-cloud-native-gateway-outside-kubernetes)Exposing Cloud Native Gateway Outside Kubernetes

To allow applications running outside the Kubernetes cluster to connect to Cloud Native Gateway, you must create a Kubernetes networking resource that exposes the service externally.

#### [](#openshift-routes)OpenShift Routes

OpenShift Routes are the standard method for exposing HTTP/2 services outside an OpenShift cluster. The operator-created Cloud Native Gateway service exposes 2 ports:

* **Port 443** — Protostellar gRPC interface, used by `couchbase2://` SDK connections
* **Port 18008** — Data API over HTTPS

To create a `passthrough` Route for the Protostellar gRPC interface that secures communication between the application and Cloud Native Gateway via TLS, create a `Route` with the `oc` command line:

```console
$ oc create route passthrough --service <cluster-name>-cloud-native-gateway-service --port 443
```

To also expose the Data API, create a separate route for port 18008:

```console
$ oc create route passthrough --service <cluster-name>-cloud-native-gateway-service --port 18008
```

Use `oc get services` to find the exact service name for your deployment.

The Route receives a hostname that external clients can use to connect. For example: `mycluster-cng.apps.openshift.example.com`.

#### [](#kubernetes-loadbalancer)Kubernetes LoadBalancer

On cloud-hosted Kubernetes — EKS, GKE, or AKS — create a `LoadBalancer` Service to expose Cloud Native Gateway through a cloud load balancer:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: <cluster-name>-cng-lb
spec:
  type: LoadBalancer
  selector:
    app: <cluster-name>-cloud-native-gateway-service
  ports:
    - name: protostellar
      protocol: TCP
      port: 443
      targetPort: 443
    - name: data-api
      protocol: TCP
      port: 18008
      targetPort: 18008
```

Apply the configuration and wait for the cluster to assign the external IP or hostname:

```console
$ kubectl apply -f cng-loadbalancer.yaml
$ kubectl get service mycluster-cng-lb
```

#### [](#kubernetes-ingress-gateway-api)Kubernetes Ingress / Gateway API

For environments using the Kubernetes Gateway API or Ingress resources with gRPC support:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: mycluster-cng-route
spec:
  parentRefs:
    - name: my-gateway
  rules:
    - backendRefs:
        - name: mycluster-cloud-native-gateway-service
          port: 443
```

Verify that your Ingress controller or Gateway implementation supports HTTP/2 and gRPC pass-through. Not all Ingress controllers handle gRPC as expected — see [Load Balancer Considerations](../sizing-performance-guidance/load-balancer-considerations.md) for guidance.

### [](#sdk-connection-configuration)SDK Connection Configuration

After you expose Cloud Native Gateway, configure your Couchbase SDK to connect using the `couchbase2://` scheme:

```java
Cluster cluster = Cluster.connect(
    "couchbase2://mycluster-cng.apps.openshift.example.com",
    "username",
    "password"
);
```

```go
cluster, err := gocb.Connect(
    "couchbase2://mycluster-cng-lb.example.com",
    gocb.ClusterOptions{
        Username: "username",
        Password: "password",
    },
)
```

The SDK establishes a single gRPC connection to the Cloud Native Gateway endpoint and sends all operations through it. You do not need further topology configuration.