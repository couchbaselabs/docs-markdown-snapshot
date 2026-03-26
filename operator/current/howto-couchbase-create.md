---
title: Create a Couchbase Deployment
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.9/modules/ROOT/pages/howto-couchbase-create.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:operator::howto-couchbase-create.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/howto-couchbase-create.html)

# Create a Couchbase Deployment

## [](#prerequisites)Prerequisites

Before you attempt to deploy a Couchbase Server cluster with the Couchbase Kubernetes Operator, ensure that you have done the following:

* You have reviewed the [prerequisites](prerequisite-and-setup.md)
* You have downloaded the [Kubernetes Operator package](https://www.couchbase.com/downloads)
* You have [deployed the admission controller and the Kubernetes Operator](install-kubernetes.md), and both are up and running  
The package contains YAML configuration files that will help you set up a Couchbase cluster.  
> [!IMPORTANT]  
> After you unpack the download, the resulting directory will be titled something like `couchbase-autonomous-operator-kubernetes.x.x-linux_x86_64`. Make sure to `cd` into this directory before you run the commands in this guide.

## [](#preparing-the-couchbase-cluster-configuration)Preparing the Couchbase Cluster Configuration

To deploy a Couchbase Server cluster using the Operator, all you have to do is create a `CouchbaseCluster` configuration file that describes what you want the cluster to look like (e.g. number of nodes, types of services, system resources, etc), and then push that configuration file into Kubernetes. Like all Kubernetes configurations, a `CouchbaseCluster` is defined using either YAML or JSON (YAML is preferred by Kubernetes).

The Operator package contains an example `CouchbaseCluster` configuration file (`couchbase-cluster.yaml`), also listed here:

Example `CouchbaseCluster` Configuration for open source Kubernetes (`couchbase-cluster.yaml`)

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: cb-example-auth
type: Opaque
data:
  username: QWRtaW5pc3RyYXRvcg==  # Administrator
  password: cGFzc3dvcmQ=          # password
---
apiVersion: couchbase.com/v2
kind: CouchbaseBucket
metadata:
  name: default  (1)
spec:
  memoryQuota: 128Mi
---
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example  (2)
spec:
  image: couchbase/server:7.6.6  (3)
  security:
    adminSecret: cb-example-auth
  networking:
    exposeAdminConsole: true
    adminConsoleServices:
    - data
  buckets:
    managed: true
  servers:
  - size: 3  (4)
    name: all_services
    services:
    - data
    - index
    - query
    - search
    - eventing
    - analytics
```

By taking a quick look at this configuration file, you can see that it defines a cluster (with buckets) by specifying the following:

| **1** | Buckets: 1 bucket named default                     |
| ----- | --------------------------------------------------- |
| **2** | Cluster name: cb-example                            |
| **3** | Couchbase image: couchbase/server:7.6.6             |
| **4** | Size: 3-node cluster with all services on each node |

You can use this example `CouchbaseCluster` configuration file "as-is" to test out how the Operator deploys a Couchbase Server cluster. However, to deploy a Couchbase cluster that is more specifically tailored to your development and production needs, you need to create your own custom configuration file that conforms to the `CouchbaseCluster` specification.

> [!TIP]
> Ensure that your Kubernetes environment has the [appropriate resources](../../server/current/install/sizing-general.md) for the Couchbase cluster that you're trying to deploy.
> 
> In the case of Minikube, the default memory allocation is 2 GB. This is not sufficient for running a three-node Couchbase cluster like the one in the example configuration. If you're using the example configuration for demo purposes, you should set the memory allocation to 4 GB at a minimum (8 GB recommended). You should also increase the CPU allocation if you experience poor performance.
> 
> You can set the recommended memory and CPU allocation when you start Minikube:
> 
> ```console
> $ minikube start --cpus 2 --memory 8192
> ```

## [](#deploying-the-couchbase-cluster)Deploying the Couchbase Cluster

The next step after creating the `CouchbaseCluster` configuration file is to push it to Kubernetes. To push the configuration, run the following command:

* Kubernetes
* OpenShift

```console
$ kubectl apply -f couchbase-cluster.yaml
```

```console
$ oc create -f couchbase-cluster.yaml
```

After receiving the configuration, the Operator automatically begins creating the cluster. The amount of time it takes to create the cluster depends on the configuration. You can track the progress of cluster creation using the [couchbaseclusters.status](resource/couchbasecluster.md#couchbaseclusters-status) attributes.

### [](#verifying-the-deployment)Verifying the Deployment

Once the cluster has been provisioned, you'll see that various pods, a service, and a Couchbase cluster have been created. If you used the example configuration (which calls for a three-node cluster) you should see three pods created. The Operator also creates an internal headless service that can be used by applications deployed inside the same Kubernetes namespace to connect to the Couchbase cluster.

Run the following command to see the newly created pods:

* Kubernetes
* OpenShift

```console
$ kubectl get pods
```

```console
$ oc get pods
```

The output should look like:

```console
NAME                                  READY     STATUS    RESTARTS   AGE
cb-example-0000                       1/1       Running   0          1m
cb-example-0001                       1/1       Running   0          1m
cb-example-0002                       1/1       Running   0          1m
couchbase-operator-1917615544-pd4q6   1/1       Running   0          8m
```

The `CouchbaseCluster` object status is continually updated during cluster operation and can be used to trigger external events. See the [couchbaseclusters.status](resource/couchbasecluster.md#couchbaseclusters-status) documentation for details.

## [](#next-steps)Next Steps

* [Access the Couchbase Server interfaces](howto-ui.md)