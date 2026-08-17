---
title: Cloud Native Gateway
description: A direct gRPC interface to key Couchbase services, abstracting
  topology details behind a service endpoint.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.8/modules/ROOT/pages/concept-cloud-native-gateway.adoc
  xref: xref:2.8@operator::concept-cloud-native-gateway.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.8/concept-cloud-native-gateway.html)

# Cloud Native Gateway

> A direct gRPC interface to key Couchbase services, abstracting topology details behind a service endpoint. 

## [](#overview)Overview

The Couchbase Cloud Native Gateway (CNG) allows applications to access Couchbase through a set of RPC network endpoints based on [gRPC](https://grpc.io/), a [Cloud Native Computing Foundation](https://cncf.io/) project.

In deployments without CNG, applications using Couchbase SDKs dynamically adjust to the cluster topology, building connections to individual nodes using a combination of memcached binary protocol and HTTP. There are some deployment scenarios, typically in cloud deployments based on Kubernetes and Red Hat OpenShift, where it is preferable to be able to abstract the topology details behind a service endpoint. This allows applications to connect to a single hostname and port and be load balanced across that service. All of the scale and elastic properties of Couchbase Server remain intact — such as scaling up or down the cluster, and upgrading the version being run. In these deployments, the application uses the [Couchbase SDK](../../home/sdk.md) with only configuration changes, and the Cloud Native Gateway handles topological changes.

For Kubernetes and OpenShift, this means the Cloud Native Gateway service can be _exposed outside Kubernetes_ through standard Kubernetes networking configuration. Specifically, this means when deployed, you can build upon the Ingress and Gateway networking in Kubernetes to expose that service outside the Kubernetes / OpenShift cluster to applications running outside Kubernetes. You can define Kubernetes `LoadBalancers` and OpenShift `Routes` to access the `CouchbaseCluster` with the Cloud Native Gateway service defined.

This also allows deployers to work with other parts of the Cloud Native ecosystem, such as Istio, Krakkend, many gRPC proxies, many observability tools, and so on. There is a direct gRPC interface to the Data, Query, and FTS (Search) services in the Couchbase Cluster. This can be useful in the rare cases where an SDK may not exist for your language or you want to just use a small feature such as a Functions as a Service (FaaS, a.k.a. Lambda) type deployment.

> [!NOTE]
> gRPC was chosen because it aligns well to the low latency performance of Couchbase — gRPC over HTTP/2 is an efficient binary wire protocol which can be efficiently marshaled to the native services of Couchbase Server.

## [](#how-it-is-deployed)How it is Deployed

The Cloud Native Gateway runs as a _sidecar_ image to every Couchbase Server node in a cluster. This sidecar is set up and managed by the Couchbase Kubernetes Operator.

When deploying a Couchbase Cluster in Kubernetes, you will define a `CouchbaseCluster` Object. Starting with release 2.6.1, the object definition allows you to add a `cloudNativeGateway` object to add the Cloud Native Gateway to your cluster and create a `Service` object. For example:

```yaml
networking:
   cloudNativeGateway:
     image: couchbase/cloud-native-gateway:1.1.0
     tls:
       serverSecretName: secret-for-cng
```

> [!CAUTION]
> At the moment, adding CNG to an existing cluster requires a rebalance which will create new pods and move data. For compatibility with commonly deployed Kubernetes and OpenShift releases, the Couchbase Kubernetes Operator cannot yet use some of the newer features for sidecar management.

## [](#monitoring-health)Monitoring Health

### [](#metrics)Metrics

Metrics for a number of CNG functions are available.

> [!WARNING]
> In this release, metrics are _volatile_ interface stability. This means that the metrics may change in updated releases, even maintenance releases. Please consider this interface stability when planning system monitoring.

### [](#logs)Logs

Logs for the Cloud Native Gateway are available via `kubectl logs` and are collected with the [cbopinfo](tools/cbopinfo.md) command when creating a logs archive.

One way you may view the logs is through the standard `kubectl logs` specifying the container:

```console
$ kubectl logs pod/mycluster-0000 -c cloud-native-gateway
```

### [](#using-grpcurl-to-verify)Using grpcurl to Verify

A common utility, [gRPCurl](https://github.com/fullstorydev/grpcurl), which is "like curl, but for gRPC", can be used to verify that the Cloud Native Gateway is accessible from another environment. The [gRPC standard health check](https://grpc.io/docs/guides/health-checking/) is a simple way to do this.

First, forward a port to any of the nodes in your defined cluster:

```console
$ kubectl port-forward pod/mycluster-0000 18098:18098
```

Then call it with `grpcurl` against a default `Health/Check` once you have the definition. To get the RPC definition:

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

## [](#upgrade-considerations)Upgrade Considerations

The Cloud Native Gateway container can be upgraded independently of the rest of a deployment. This makes applying maintenance fixes easy and targeted while allowing deployments to minimize the software running. To upgrade to a newer version of CNG listed as compatible in the [system requirements](prerequisite-and-setup.md), simply update the `image` in the deployment via normal Kubernetes or OpenShift tooling.

> [!IMPORTANT]
> Changing the image used for the `cloudNativeGateway` requires a rebalance at this time. In the future, we expect to be able to improve this through the Kubernetes sidecar APIs. At the time of writing (February 2024), these are not available on OpenShift or from Kubernetes at popular Cloud Service Providers.

## [](#platform-integration)Platform Integration

As the Cloud Native Gateway is a standard gRPC over HTTP/2 service, it can be accessed as a service within Kubernetes. More often though, the reason to deploy CNG is to expose it outside K8S.

The details of deploying an HTTP service should be taken from the Kubernetes documentation, or the documentation from the platform you are using. Here are some examples of configurations we have used and tested.

### [](#creating-openshift-routes)Creating OpenShift Routes

OpenShift has a number of ways you may create and manage routes. Any method is acceptable.

To create a `passthrough` Route, which secures communication between the application and CNG via TLS, you would create a `Route` with the `oc` command line:

```console
$ oc create route passthrough --service mycluster-cloud-native-gateway-service --port 443
```

Note, you can run `oc get services` to get the name of the service associated with your `CouchbaseCluster` deployment.

### [](#creating-aws-elastic-kubernetes-service-loadbalancers)Creating AWS Elastic Kubernetes Service LoadBalancers

The most common way to create a `LoadBalancer` through EKS is to create a deployment YAML file which you would then `kubectl apply`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mycluster-cng-service-loadbalancer
spec:
  type: LoadBalancer
  selector:
    app: mycluster-cloud-native-gateway-service
  ports:
    - protocol: TCP
      port: 443
      targetPort: 443
```

[AWS LoadBalancers](https://docs.aws.amazon.com/eks/latest/userguide/network-load-balancing.html) have a number of advanced options which you may want to use for your deployment. For example, you may wish to use a different DNS domain to match the planned certificate you will use with CNG.