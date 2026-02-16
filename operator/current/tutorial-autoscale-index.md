[View original HTML](/operator/current/tutorial-autoscale-index.html)

> Learn how to configure auto-scaling for Index Service nodes using the Kubernetes Operator. 

|  | Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#introduction)Introduction

In this tutorial you’ll learn how to use the Kubernetes Operator to automatically scale the Couchbase Index Service in order to maintain a target memory utilization threshold for indexes. You’ll also learn more about how the Kubernetes [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) (HPA) initiates a request to scale the Index Service in order to maintain desired thresholds.

## [](#before-you-begin)Before You Begin

Before you begin this tutorial, you’ll need to set up a few things first:

* You’ll need a Kubernetes cluster with at least eight available worker nodes.

  * Worker nodes should have 4 vCPU and 16 GiB memory in order to exhibit the expected auto-scaling behavior that you’ll be initiating later on in this tutorial.
* You’ll need [Helm version 3.1](https://helm.sh/docs/intro/install/) or higher for installing the necessary dependencies (e.g. the Kubernetes Operator, the Couchbase cluster, etc.)

  * Once you have Helm installed, you’ll need to add the Couchbase chart repository:  
  ```console  
  $ helm repo add couchbase https://couchbase-partners.github.io/helm-charts/  
  ```  
  Then make sure to update the repository index:  
  ```console  
  $ helm repo update  
  ```

## [](#reserve-nodes-for-the-workload-generator)Reserve Nodes for the Workload Generator

Later on in this tutorial we’ll be using a separate application to generate a document-indexing workload that will induce auto-scaling as the memory utilization of indexes increases. So before we deploy anything, we need to reserve one of our Kubernetes worker nodes for exclusively running this application. We can do this by applying a scheduling tolerance with the following commands:

```console
$ APP_NODE=$(kubectl get nodes | grep Ready | head -1  | awk '{print $1}')
```

```console
$ kubectl taint nodes $APP_NODE type=app:NoSchedule
```

## [](#create-the-couchbase-cluster-deployment)Create the Couchbase Cluster Deployment

Now that we’ve reserved a worker node for our document generator, we can start setting up our Couchbase deployment. To speed up the process, we’ll be using the Couchbase Helm chart to conveniently install a Couchbase cluster that has auto-scaling enabled for the nodes running the Index Service.

Run the following command to create a file with the necessary override values for the Couchbase chart:

```console
$ cat << EOF > autoscale_values.yaml
---
cluster:
  cluster:
    dataServiceMemoryQuota: 10Gi
    indexServiceMemoryQuota: 256Mi (1)
  autoscaleStabilizationPeriod: 0s (2)
  name: scale-couchbase-cluster
  servers:
    default:
      size: 2
      services:
        - data
      resources:
        limits:
          cpu: 3
          memory: 12Gi
        requests:
          cpu: 3
          memory: 12Gi
    index:
      size: 1
      autoscaleEnabled: true (3)
      services:
        - index
      resources:
        limits:
          cpu: 3
          memory: 2Gi
        requests:
          cpu: 3
          memory: 2Gi
    query:
      size: 1
      services:
        - query
      resources:
        limits:
          cpu: 3
          memory: 12Gi
        requests:
          cpu: 3
          memory: 12Gi
users:
  developer:
    password: password
    authDomain: local
    roles:
      - name: admin
buckets:
  default:
    name: travel-sample
    kind: CouchbaseBucket
    memoryQuota: 8Gi
    replicas: 2
EOF
```

| **1** | [couchbaseclusters.spec.cluster.indexServiceMemoryQuota](resource/couchbasecluster.md#couchbaseclusters-spec-cluster-indexservicememoryquota): For demonstration purposes, we’re setting the default minimum memory quota for the Index Service (256Mi) so that we can more quickly and easily induce auto-scaling. This cluster configuration uses the default index storage mode set by the Kubernetes Operator, which is memory\_optimized. This allows us to demonstrate the benefits of auto-scaling in situations when persisting to disk isn’t an option.                                                                                                                                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [couchbaseclusters.spec.autoscaleStabilizationPeriod](resource/couchbasecluster.md#couchbaseclusters-spec-autoscalestabilizationperiod): Setting this field to 0s serves two purposes: 1.) It disables additional auto-scaling while the cluster is rebalancing; and 2.) it re-enables auto-scaling immediately after rebalance is complete, without any additional delay to allow for cluster stabilization. The reason that no additional delay is required in this case is because memory metrics for the Index Service are relatively stable after rebalance is complete. However, please refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance about what values you should use in production. |
| **3** | [couchbaseclusters.spec.servers.autoscaleEnabled](resource/couchbasecluster.md#couchbaseclusters-spec-servers-autoscaleenabled): Setting this field to true enables auto-scaling for the server class that contains the Index Service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

Now, install the Couchbase chart, making sure to specify the values override file we just created:

```console
$ helm upgrade --install -f autoscale_values.yaml scale couchbase/couchbase-operator
```

|  | The Couchbase chart deploys the Kubernetes Operator by default. If you already have the Kubernetes Operator deployed in the current namespace, then you’ll need to specify additional overrides during chart installation so that only the Couchbase cluster is deployed: $ helm upgrade --install -f autoscale\_values.yaml --set install.couchbaseOperator=false,install.admissionController=false scale couchbase/couchbase-operator |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#verify-the-installation)Verify the Installation

The configuration we’re using calls for a four-node Couchbase cluster (two `default` nodes and one `index` node, and one `query` node), which will take a few minutes to be created. You can run the following command to verify the deployment status:

```console
$ kubectl describe couchbasecluster scale-couchbase-cluster
```

In the console output, you should check for the events that signal the creation of the five nodes in the Couchbase cluster, as well as the creation of a [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource for the `index` server class configuration:

Events:
  Type    Reason                  Age   From  Message
  ----    ------                  ----  ----  -------
  Normal  NewMemberAdded          21m         New member scale-couchbase-cluster-0003 added to cluster
  ...
  Normal  EventAutoscalerCreated  22m         Autoscaler for config `index` added

The Kubernetes Operator automatically creates a [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource for each server class configuration that has [couchbaseclusters.spec.servers.autoscaleEnabled](resource/couchbasecluster.md#couchbaseclusters-spec-servers-autoscaleenabled) set to `true`. The Operator also keeps the size of the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource in sync with the size of its associated server class configuration.

Run the following command to verify that the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource exists and matches the size of its associated server configuration:

```console
$ kubectl get couchbaseautoscalers
```

NAME                            SIZE   SERVERS
index.scale-couchbase-cluster   1      index **(1)** **(2)**

In the console output, you’ll see:

| **1** | NAME: The Kubernetes Operator creates [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resources with the name format _<server-class>_._<cluster-name>_. Considering that we enabled auto-scaling for the index server class configuration, and the name of our cluster is scale-couchbase-cluster, we can determine that the name of the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource created by the Kubernetes Operator will be index.scale-couchbase-cluster.                    |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | SIZE: This is the current number of Couchbase nodes that the Kubernetes Operator is maintaining for the index server class. Considering that we set servers.index.size to 1 in our cluster configuration, and because the cluster doesn’t yet have the ability to automatically scale, we can expect that the SIZE listed here will be 1. Once we create an HPA for the index server class, and the number of index nodes begins to scale, the SIZE will update to reflect the number of nodes currently being maintained. |

### [](#accessing-the-couchbase-web-console)Accessing the Couchbase Web Console

Having access to the Couchbase Web Console can make it easier to verify the result of certain actions in this tutorial. To gain access, start by checking the `status` of the Helm chart:

```console
$ helm status scale
```

The console output conveniently contains the necessary details for accessing the Couchbase Web Console.

== Connect to Admin console
   kubectl port-forward --namespace default scale-couchbase-cluster-0000 8091:8091

   # open http://localhost:8091
   username: Administrator
   password: <redacted>

Run the `kubectl port-forward` command to forward the necessary port to the listed pod. Once the port has been forwarded, you can access the Couchbase Web Console at `<http://localhost:8091>`. Log in using the listed username and password.

## [](#install-the-monitoring-stack)Install the Monitoring Stack

For Couchbase server versions 7.0+, it is possible to collect metrics from the native metrics endpoint. More information on how to do this can be found here.

## [](#create-a-horizontal-pod-autoscaler)Create a Horizontal Pod Autoscaler

Now that we’ve confirmed that metrics data are being collected for index memory quota, we can create a `HorizontalPodAutoscaler` resource that targets this metric. For this tutorial, we’ll be configuring an HPA to scale the number of Couchbase `index` nodes in our cluster when the memory utilization across `index` nodes exceeds 60% of the quota set for the Index Service. (When memory utilization exceeds 60%, additional `index` nodes will be added, and when usage falls below 60% then the HPA will consider scaling down to reduce overhead.)

Run the following command to create a `HorizontalPodAutoscaler` resource that will take action when the memory utilization of the Index Service exceeds 60% of its quota:

```console
$ cat << EOF | kubectl apply -f -
---
kind: HorizontalPodAutoscaler
apiVersion: autoscaling/v2
metadata:
  name: index-mem-hpa
spec:
  scaleTargetRef:
    apiVersion: couchbase.com/v2
    kind: CouchbaseAutoscaler (1)
    name: index.scale-couchbase-cluster (2)
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 30
      policies:
      - type: Pods
        value: 1
        periodSeconds: 15
    scaleDown:
      stabilizationWindowSeconds: 300
  minReplicas: 1 (3)
  maxReplicas: 4 (4)
  metrics:
  - type: Pods
    pods:
      metric:
        name: cbindex_ram_percent (5)
      target:
        type: AverageValue
        averageValue: 60 (6)
EOF
```

| **1** | scaleTargetRef.kind: This field must be set to [CouchbaseAutoscaler](resource/couchbaseautoscaler.md), which is the kind of custom resource that gets automatically created by the Kubernetes Operator when you enable auto-scaling for a particular server class.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | scaleTargetRef.name: This field needs to reference the name of the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource. Since the Kubernetes Operator creates [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resources with the name format _<server-class>_._<cluster-name>_, the name we’ll need to specify is index.scale-couchbase-cluster. As described previously in the [Verify the Installation](#verify-the-installation) section, a quick way to view the existing [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resources (and their names) is to run the following command: $ kubectl get couchbaseautoscalers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **3** | minReplicas: This field sets the minimum number of Couchbase nodes for the specified server class. Here, we’ve set the minimum number of index nodes to 1 (technically unneeded since the Kubernetes default is 1). This means that the number of index nodes will never be down-scaled to fewer than one node, even if the HPA detects that the target metric is relatively below the target value. Setting minReplicas is important for maintaining service availability. Refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance on setting this value in production environments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **4** | maxReplicas: This field sets the maximum number of Couchbase nodes for the specified server class. It cannot be set to a value lower than what is defined for minReplicas. Here, we’ve set the maximum number of index nodes to 4. This means that the number of index nodes will never be up-scaled to more than four nodes, even if the HPA detects that the target metric is still relatively above the target value. Setting a value for maxReplicas is required because it provides important protection against runaway scaling events. Refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance on setting this value in production environments. The [prerequisites](#before-you-begin) for this tutorial state that eight Kubernetes worker nodes are required. So far we’re currently using four worker nodes for our Couchbase cluster (two default nodes, one index node, and one query node) and have reserved one worker node for the workload generator. By setting maxReplicas to 4, we’re allowing the index server class to scale up to an additional three nodes if necessary, thus potentially requiring up to eight worker nodes for our entire setup. |
| **5** | metrics.pods.metric.name: The name of the target metric that will be monitored by the HPA for the purposes of auto-scaling. Here, we’ve specified cbindex\_ram\_percent as the metric that will be used to scale the number index nodes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **6** | metrics.pods.target.type: Specifying the AverageValue type means that the metric will be averaged across all of the pods. Here, by setting a value of 60, the HPA will scale the number of index nodes when the average memory utilization across all index pods exceeds 60% of the quota set for the Index Service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

|  | Details about how sizing decisions are made are discussed in [Couchbase Cluster Auto-scaling](concept-couchbase-autoscaling.md). |
|  | -------------------------------------------------------------------------------------------------------------------------------- |

### [](#verify-horizontalpodautoscaler-status)Verify `HorizontalPodAutoscaler` Status

Now that we’ve created the `HorizontalPodAutoscaler` resource, the HPA will begin to monitor the target metric and report that the initial size (number) of `index` nodes are within the desired range. Run the following command to print these details to the console output:

```console
$ kubectl describe hpa index-mem-hpa
```

Metrics:                          ( current / target )
  "cbindex_ram_percent" on pods:  25911m / 60 **(1)**

Min replicas:                         1
Max replicas:                         4
CouchbaseAutoscaler pods:             1 current / 1 desired  **(2)**

| **1** | Here we see that the current index memory utilization is **\~25%** (again, on a scale of 1000) out of the 60 percent target. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we see that there is currently 1 index node in the cluster, and 1 are desired to maintain the current target.           |

## [](#test-the-auto-scaling-behavior)Test the Auto-scaling Behavior

At this point, we’ve completed all the necessary steps to configure our cluster deployment to automatically scale the number of `index` nodes. If the average memory utilization across current `index` nodes exceeds 60% of the quota set for the Index Service, an additional `index` node will be added to the cluster.

However, we should test our configuration to be sure that `index` nodes will automatically scale as expected. To do this, we’ll be attempting to induce auto-scaling behavior by creating a large enough index to consume more than 60% of the memory quota.

### [](#create-a-partitioned-index)Create a Partitioned Index

Let’s start by creating an index that will be partitioned across the available Couchbase `index` nodes. As additional `index` nodes are added to the Couchbase cluster, the partitions will be redistributed across the nodes according to the provided `HASH` method on document `id`.

|  | Horizontal scaling of the Index Service requires that indexes be [partitioned](../../server/current/n1ql/n1ql-language-reference/index-partitioning.md). Indexes that don’t utilize partitioning reside on a single node with underlying memory and compute resources that cannot be resized in-place after creation. You will need to delete and re-create any non-partitioned indexes before you can auto-scale the underlying Index nodes. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

To create a partitioned index, open the Couchbase Web Console and navigate to the Query Workbench under the **Query** tab in the left navigation menu. Within the **Query Editor** field, enter the following and click **Execute**:

```n1ql
CREATE INDEX name_age ON `travel-sample`(name, age, id)
 PARTITION BY HASH(META().id);
```

Now we have an index on the `name`, `age`, and `id` fields of all documents in the `travel-sample` bucket.

### [](#load-data)Load Data

Now we will load some data into the `travel-sample` bucket to increase the number of documents being indexed. Run the following command to create a Kubernetes Job that runs the Couchbase [cbworkloadgen](../../server/current/cli/cbtools/cbworkloadgen.md) tool:

```console
$ cat << EOF | kubectl apply -f -
---
apiVersion: batch/v1
kind: Job
metadata:
  name: cb-workload-gen
spec:
  template:
    spec:
      containers:
      - name: doc-loader
        image: couchbase/server:7.6.6
        command: ["/opt/couchbase/bin/cbworkloadgen", "-n","scale-couchbase-cluster-0000.scale-couchbase-cluster.default.svc:8091", "-u", "developer", "-p", "password", "-t", "4", "-r", ".3", "-j", "-s", "16","--prefix=read-write","-i", "150000", "-b", "travel-sample"]
      restartPolicy: Never
      tolerations:
      - key: "type"
        operator: "Equal"
        value: "app"
        effect: "NoSchedule"
EOF
```

You can check the Couchbase Web Console that we [accessed previously](#accessing-the-couchbase-web-console) to ensure that the data set is being loaded.

### [](#verify-auto-scaling)Verify Auto-scaling

The Couchbase [Index Statistics](../../server/current/manage/monitor/monitoring-indexes.md) should show an increasing usage of the available memory as [cbworkloadgen](../../server/current/cli/cbtools/cbworkloadgen.md) loads documents. Auto-scaling should occur once memory usage reaches just above 128 MB.

Run the following command to view the behavior of the HPA as it monitors the index memory utilization as it approaches the target metric:

```console
$ kubectl describe hpa index-mem-hpa
```

You should expect output similar to the following:

...
Reference:                                             CouchbaseAutoscaler/index.scale-couchbase-cluster
Metrics:                                               ( current / target )
  "cbindex_ram_percent" on pods:  66056m / 60 **(1)**
Events:
  Type    Reason             Age   From                       Message
  ----    ------             ----  ----                       -------
  Normal  SuccessfulRescale  17s   horizontal-pod-autoscaler  New size: 2; reason: pods metric cbindex_ram_percent above target **(2)**
  Normal  SuccessfulRescale  3m11s  horizontal-pod-autoscaler  New size: 3; reason: pods metric cbindex_ram_percent above target

| **1** | The HPA has detected **66%** memory utilization.                                                                                                                                                                                                                                                                                                                                                                                          |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The number of index nodes has been scaled from **2** to **3**. The following [scaling algorithm](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details) was applied by the HPA to determine the desired replicas: desiredReplicas = ceil\[currentReplicas \* ( currentMetricValue / desiredMetricValue )\]               2 = ceil\[       1        \* (      66.0        /     60.0            )\] |

### [](#cleaning-up)Cleaning up

Running the commands in this section will uninstall all of the resources that were created during the course of this tutorial.

Remove workload jobs:

```console
$ kubectl delete jobs cb-workload-gen
```

Delete the HPA:

```console
$ kubectl delete hpa index-mem-hpa
```

Uninstall the monitoring stack by deleting the Helm release:

```console
$ helm delete monitor
```

Uninstall both the Kubernetes Operator and Couchbase cluster by deleting the Helm release:

```console
$ helm delete scale
```

Remove the scheduling tolerance that we applied for the workload generator:

```console
$ APP_NODE=$(kubectl get nodes | grep Ready | head -1  | awk '{print $1}')
```

```console
$ kubectl taint nodes $APP_NODE type=app:NoSchedule-
```

## [](#conclusion)Conclusion

You will very likely need to do some experimentation before settling on a particular metric and target value that makes sense for your workload objectives. Refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance when determining the best target value for index memory utilization when scaling Index Service nodes.

## [](#further-reading)Further Reading

* Concepts: [Couchbase Cluster Auto-scaling](concept-couchbase-autoscaling.md)
* Best Practices: [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md)
* Reference: [CouchbaseAutoscaler Resource](resource/couchbaseautoscaler.md)
* Reference: [Autoscaling Lifecycle Events](reference-couchbasecluster-events.md#autoscaling-lifecycle)