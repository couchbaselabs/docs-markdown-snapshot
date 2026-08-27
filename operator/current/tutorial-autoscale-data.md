---
title: Auto-scaling the Couchbase Data Service
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.9/modules/ROOT/pages/tutorial-autoscale-data.adoc
  xref: xref:operator::tutorial-autoscale-data.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/tutorial-autoscale-data.html)

# Auto-scaling the Couchbase Data Service

> Learn how to configure auto-scaling for Data Service nodes using the Kubernetes Operator. 

> [!WARNING]
> Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer.

## [](#introduction)Introduction

In this tutorial you'll learn how to use the Kubernetes Operator to automatically scale the Couchbase Data Service in order to maintain a target memory utilization threshold for an [Ephemeral bucket](../../server/current/learn/buckets-memory-and-storage/buckets.md). You'll also learn more about how the Kubernetes [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) (HPA) initiates a request to scale the Data Service in order to maintain desired thresholds.

## [](#before-you-begin)Before You Begin

Before you begin this tutorial, you'll need to set up a few things first:

* You'll need a Kubernetes cluster with at least seven available worker nodes.

  * Worker nodes should have 4 vCPU and 16 GiB memory in order to exhibit the expected auto-scaling behavior that you'll be initiating later on in this tutorial.
* You'll need [Helm version 3.1](https://helm.sh/docs/intro/install/) or higher for installing the necessary dependencies (e.g. the Kubernetes Operator, the Couchbase cluster, etc.)

  * Once you have Helm installed, you'll need to add the Couchbase chart repository:  
  ```console  
  $ helm repo add couchbase https://couchbase-partners.github.io/helm-charts/  
  ```  
  Then make sure to update the repository index:  
  ```console  
  $ helm repo update  
  ```

## [](#create-the-couchbase-cluster-deployment)Create the Couchbase Cluster Deployment

The first thing we're going to do is set up our Couchbase deployment. To speed up the process, we'll be using the Couchbase Helm chart to conveniently install a Couchbase cluster that has auto-scaling enabled for the nodes running the Data Service.

Run the following command to create a file with the necessary override values for the Couchbase chart:

```console
$ cat << EOF > autoscale_values.yaml
---
cluster:
  cluster:
    dataServiceMemoryQuota: 4Gi
    indexServiceMemoryQuota: 6Gi
  autoscaleStabilizationPeriod: 0s (1)
  name: scale-couchbase-cluster
  servers:
    default:
      autoscaleEnabled: true (2)
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
    query:
      size: 1
      services:
        - index
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
    kind: CouchbaseEphemeralBucket (3)
    evictionPolicy: noEviction
    memoryQuota: 1Gi (4)
EOF
```

| **1** | [couchbaseclusters.spec.autoscaleStabilizationPeriod](resource/couchbasecluster.md#couchbaseclusters-spec-autoscalestabilizationperiod): Setting this field to 0s serves two purposes: 1.) It disables additional auto-scaling while the cluster is rebalancing; and 2.) it re-enables auto-scaling immediately after rebalance is complete, without any additional delay to allow for cluster stabilization. The reason that no additional delay is required in this case is because memory metrics for the Data Service are relatively stable after rebalance is complete. However, please refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance about what values you should use in production. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | [couchbaseclusters.spec.servers.autoscaleEnabled](resource/couchbasecluster.md#couchbaseclusters-spec-servers-autoscaleenabled): Setting this field to true enables auto-scaling for the server class that contains the Data Service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **3** | We're going to create an Ephemeral bucket in order to demonstrate the benefits of auto-scaling in situations when persisting to disk isn't an option. Please refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional information about how the bucket type affects auto-scaling behavior when scaling the Data Service based on bucket memory utilization.                                                                                                                                                                                                                                                                                                                                                    |
| **4** | We're setting the bucket memory quota relatively low (1Gi) so that we can more quickly and easily induce auto-scaling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

Now, install the Couchbase chart, making sure to specify the values override file we just created:

```console
$ helm upgrade --install -f autoscale_values.yaml scale couchbase/couchbase-operator
```

> [!NOTE]
> The Couchbase chart deploys the Kubernetes Operator by default. If you already have the Kubernetes Operator deployed in the current namespace, then you'll need to specify additional overrides during chart installation so that only the Couchbase cluster is deployed:
> 
> ```console
> $ helm upgrade --install -f autoscale_values.yaml --set install.couchbaseOperator=false,install.admissionController=false scale couchbase/couchbase-operator
> ```

### [](#verify-the-installation)Verify the Installation

The configuration we're using calls for a three-node Couchbase cluster (two `default` nodes and one `query` node), which will take a few minutes to be created. You can run the following command to verify the deployment status:

```console
$ kubectl describe couchbasecluster scale-couchbase-cluster
```

In the console output, you should check for the events that signal the creation of the four nodes in the Couchbase cluster, as well as the creation of a [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource for the `default` server class configuration:

Events:
  Type    Reason                  Age   From  Message
  ----    ------                  ----  ----  -------
  Normal  EventNewMemberAdded     22m         New member scale-couchbase-cluster-0003 added to cluster
  ...
  Normal  EventAutoscalerCreated  22m         Autoscaler for config `default` added

The Kubernetes Operator automatically creates a [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource for each server class configuration that has [couchbaseclusters.spec.servers.autoscaleEnabled](resource/couchbasecluster.md#couchbaseclusters-spec-servers-autoscaleenabled) set to `true`. The Operator also keeps the size of the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource in sync with the size of its associated server class configuration.

Run the following command to verify that the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource exists and matches the size of its associated server configuration:

```console
$ kubectl get couchbaseautoscalers
```

NAME                               SIZE   SERVERS
default.scale-couchbase-cluster    2      default **(1)** **(2)**

In the console output, you'll see:

| **1** | NAME: The Kubernetes Operator creates [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resources with the name format _<server-class>_._<cluster-name>_. Considering that we enabled auto-scaling for the default server class configuration, and the name of our cluster is scale-couchbase-cluster, we can determine that the name of the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource created by the Kubernetes Operator will be default.scale-couchbase-cluster.                        |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | SIZE: This is the current number of Couchbase nodes that the Kubernetes Operator is maintaining for the default server class. Considering that we set servers.default.size to 2 in our cluster configuration, and because the cluster doesn't yet have the ability to automatically scale, we can expect that the SIZE listed here will be 2. Once we create an HPA for the default server class, and the number of default nodes begins to scale, the SIZE will update to reflect the number of nodes currently being maintained. |

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

For Couchbase server versions 7.0+, it is possible to collect metrics from the native metrics endpoint. More information on how to do this can be found [here](https://docs.couchbase.com/operator/current/howto-prometheus.html).

## [](#create-a-horizontal-pod-autoscaler)Create a Horizontal Pod Autoscaler

Now that we've confirmed that metrics data are being collected for bucket memory quota, we can create a `HorizontalPodAutoscaler` resource that targets this metric. For this tutorial, we'll be configuring an HPA to scale the number of Couchbase `default` nodes in our cluster when the memory utilization for the `travel-sample` bucket exceeds 70% of its `1Gi` quota. (When memory utilization exceeds 70%, additional `default` nodes will be added, and when usage falls below 70% then the HPA will consider scaling down to reduce overhead.)

Run the following command to create a `HorizontalPodAutoscaler` resource that will take action when the memory utilization for the `travel-sample` bucket exceeds 70% of its quota:

```console
$ cat << EOF | kubectl apply -f -
---
kind: HorizontalPodAutoscaler
apiVersion: autoscaling/v2
metadata:
  name: data-hpa
spec:
  scaleTargetRef:
    apiVersion: couchbase.com/v2
    kind: CouchbaseAutoscaler (1)
    name: default.scale-couchbase-cluster (2)
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 30
      policies:
      - type: Pods
        value: 1
        periodSeconds: 15
    scaleDown:
      stabilizationWindowSeconds: 300
  minReplicas: 2 (3)
  maxReplicas: 6 (4)
  metrics:
  - type: Pods
    pods:
      metric:
        name: cbbucketinfo_basic_quota_user_percent (5)
      target:
        type: AverageValue
        averageValue: 70 (6)
EOF
```

| **1** | scaleTargetRef.kind: This field must be set to [CouchbaseAutoscaler](resource/couchbaseautoscaler.md), which is the kind of custom resource that gets automatically created by the Kubernetes Operator when you enable auto-scaling for a particular server class.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | scaleTargetRef.name: This field needs to reference the name of the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource. Since the Kubernetes Operator creates [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resources with the name format _<server-class>_._<cluster-name>_, the name we'll need to specify is default.scale-couchbase-cluster. As described previously in the [Verify the Installation](#verify-the-installation) section, a quick way to view the existing [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resources (and their names) is to run the following command: $ kubectl get couchbaseautoscalers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **3** | minReplicas: This field sets the minimum number of Couchbase nodes for the specified server class. Here, we've set the minimum number of default nodes to 2. This means that the number of default nodes will never be down-scaled to fewer than two nodes, even if the HPA detects that the target metric is relatively below the target value. Setting minReplicas is important for maintaining service availability. Refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance on setting this value in production environments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **4** | maxReplicas: This field sets the maximum number of Couchbase nodes for the specified server class. It cannot be set to a value lower than what is defined for minReplicas. Here, we've set the maximum number of default nodes to 6. This means that number of default nodes will never be up-scaled to more than six nodes, even if the HPA detects that the target metric is still relatively above the target value. Setting a value for maxReplicas is required because it provides important protection against runaway scaling events. Refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance on setting this value in production environments. The [prerequisites](#before-you-begin) for this tutorial state that seven Kubernetes worker nodes are required. So far we're currently using three worker nodes for our Couchbase cluster (two default nodes and one query node). By setting maxReplicas to 6, we're allowing the default server class to scale up to an additional four nodes if necessary, thus potentially requiring up to seven worker nodes for our entire setup. |
| **5** | metrics.pods.metric.name: The name of the target metric that will be monitored by the HPA for the purposes of auto-scaling. Here, we've specified cbbucketinfo\_basic\_quota\_user\_percent as the metric that will be used to scale the number default nodes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **6** | metrics.pods.target.type: Specifying the AverageValue type means that the metric will be averaged across all of the pods. Here, by setting a value of 70, the HPA will scale the number of default nodes when the average bucket memory utilization across all default pods exceeds 70%.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

> [!NOTE]
> Details about how sizing decisions are made are discussed in [Couchbase Cluster Auto-scaling](concept-couchbase-autoscaling.md).

### [](#verify-horizontalpodautoscaler-status)Verify `HorizontalPodAutoscaler` Status

Now that we've created the `HorizontalPodAutoscaler` resource, the HPA will begin to monitor the target metric and report that the initial size (number) of `default` nodes are within the desired range. Run the following command to print these details to the console output:

```console
$ kubectl describe hpa data-hpa
```

Metrics:                                               ( current / target )
  "cbbucketinfo_basic_quota_user_percent" on pods:  2771m / 70 **(1)**
Min replicas:                         2
Max replicas:                         6
CouchbaseAutoscaler pods:             2 current / 2 desired  **(2)**

| **1** | Here we see that the current bucket memory utilization is **\~2%** (again, on a scale of 1000) out of the 70 percent target. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we see that there are currently 3 default nodes in the cluster, and 3 are desired to maintain the current target.       |

## [](#test-the-auto-scaling-behavior)Test the Auto-scaling Behavior

At this point, we've completed all the necessary steps to configure our cluster deployment to automatically scale the number of `default` nodes. If the average bucket memory utilization across current `default` nodes exceeds 70%, an additional `default` node will be added to the cluster.

However, we should test our configuration to be sure that `default` nodes will automatically scale as expected. To do this, we'll be attempting to induce auto-scaling behavior by loading enough data into the `travel-sample` bucket to exceed 70% of its memory quota.

### [](#load-data)Load Data

Let's start loading some data into `travel-sample` bucket to increase memory usage towards the auto-scaling threshold. Run the following command to create a Kubernetes Job that runs the Couchbase [cbworkloadgen](../../server/current/cli/cbtools/cbworkloadgen.md) tool:

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
        command: ["/opt/couchbase/bin/cbworkloadgen", "-n","scale-couchbase-cluster-0000.scale-couchbase-cluster.default.svc:8091", "-u", "developer", "-p", "password", "-t", "4", "-r", ".7", "-j", "-s", "1024","--prefix=wrote-a","-i", "2000000", "-b", "travel-sample"]
      restartPolicy: Never
EOF
```

You can check the Couchbase Web Console that we [accessed previously](#accessing-the-couchbase-web-console) to ensure that the data set is being loaded.

### [](#verify-auto-scaling)Verify Auto-scaling

Memory utilization of the `travel-sample` bucket should increase as [cbworkloadgen](../../server/current/cli/cbtools/cbworkloadgen.md) loads documents. In the Couchbase Web Console, you should see the [RAM used/quota](../../server/current/manage/manage-ui/manage-ui.md#console-buckets) increasing for the `travel-sample` bucket as `cbworkloadgen` loads documents.

The workload generator will create 2 M documents at 1 KB each. Auto-scaling should occur once memory usage reaches just above 1.4 GB since there are two `default` nodes providing `1Gi` memory _each_ to the `travel-sample` bucket.

Run the following command to view the behavior of the HPA as it monitors the bucket memory utilization as it approaches the target metric:

```console
$ kubectl describe hpa data-hpa
```

You should expect output similar to the following:

...
Reference:                                             CouchbaseAutoscaler/default.scale-couchbase-cluster
Metrics:                                               ( current / target )
  "cbbucketinfo_basic_quota_user_percent" on pods:  81930m / 70 **(1)**
Events:
  Type    Reason             Age   From                       Message
  ----    ------             ----  ----                       -------
  Normal  SuccessfulRescale  21s   horizontal-pod-autoscaler  New size: 3; reason: pods metric cbbucketinfo_basic_quota_user_percent above target **(2)**
  Normal  SuccessfulRescale  48s    horizontal-pod-autoscaler  New size: 4; reason: pods metric cbbucketinfo_basic_quota_user_percent above target

| **1** | The HPA has detected **81%** memory utilization.                                                                                                                                                                                                                                                                                                                                                                                            |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The number of default nodes has been scaled from **2** to **3**. The following [scaling algorithm](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details) was applied by the HPA to determine the desired replicas: desiredReplicas = ceil\[currentReplicas \* ( currentMetricValue / desiredMetricValue )\]               3 = ceil\[       2        \* (      91.0        /     70.0            )\] |

## [](#cleaning-up)Cleaning up

Running the commands in this section will uninstall all of the resources that were created during the course of this tutorial.

Remove workload jobs:

```console
$ kubectl delete jobs cb-workload-gen
```

Delete the HPA:

```console
$ kubectl delete hpa data-hpa
```

Uninstall both the Kubernetes Operator and Couchbase cluster by deleting the Helm release:

```console
$ helm delete scale
```

## [](#conclusion)Conclusion

You will very likely need to do some experimentation before settling on a particular metric and target value that makes sense for your workload objectives. Refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance when determining the best target value for bucket memory utilization when scaling Data Service nodes.

## [](#further-reading)Further Reading

* Concepts: [Couchbase Cluster Auto-scaling](concept-couchbase-autoscaling.md)
* Best Practices: [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md)
* Reference: [CouchbaseAutoscaler Resource](resource/couchbaseautoscaler.md)
* Reference: [Autoscaling Lifecycle Events](reference-couchbasecluster-events.md#autoscaling-lifecycle)