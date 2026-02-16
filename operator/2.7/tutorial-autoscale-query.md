[View original HTML](/operator/2.7/tutorial-autoscale-query.html)

> Learn how to configure auto-scaling for Query Service nodes using the Autonomous Operator. 

|  | Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#introduction)Introduction

In this tutorial you’ll learn how to use the Autonomous Operator to automatically scale the Couchbase Query Service in order to maintain a target CPU utilization threshold. You’ll also learn more about how the Kubernetes [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) (HPA) initiates a request to scale the Query Service in order to maintain desired performance thresholds.

## [](#before-you-begin)Before You Begin

Before you begin this tutorial, you’ll need to set up a few things first:

* You’ll need a Kubernetes cluster with at least 10 available worker nodes.

  * Worker nodes should have 4 vCPU and 16 GiB memory in order to exhibit the expected auto-scaling behavior that you’ll be initiating later on in this tutorial.
* You’ll need [Helm version 3.1](https://helm.sh/docs/intro/install/) or higher for installing the necessary dependencies (e.g. the Autonomous Operator, the Couchbase cluster, etc.)

  * Once you have Helm installed, you’ll need to add the Couchbase chart repository:  
  ```console  
  $ helm repo add couchbase https://couchbase-partners.github.io/helm-charts/  
  ```  
  Then make sure to update the repository index:  
  ```console  
  $ helm repo update  
  ```

## [](#deploy-metrics-server)Deploy Metrics Server

Your Kubernetes cluster must have [Metrics Server](https://github.com/kubernetes-sigs/metrics-server) deployed. Metrics Server collects resource metrics such as `cpu` and `memory` from pods and nodes, and exposes them through the [Metrics API](https://kubernetes.io/docs/tasks/debug-application-cluster/resource-metrics-pipeline/#the-metrics-api). These metrics need to be available later on in this tutorial when we set up our Couchbase cluster to automatically scale the number of Query Service nodes based on `cpu` utilization.

Metrics Server may not be deployed by default in your Kubernetes cluster. Run the following command to verify that Metrics Server is properly installed and exposing the necessary resource metrics:

```console
$ kubectl get --raw /apis/metrics.k8s.io/v1beta1
```

The response should contain an `APIResourceList` with the type of resources that can be fetched:

{"kind":"APIResourceList","apiVersion":"v1","groupVersion":"metrics.k8s.io/v1beta1","resources":[{"name":"nodes","singularName":"","namespaced":false,"kind":"NodeMetrics","verbs":["get","list"]},{"name":"pods","singularName":"","namespaced":true,"kind":"PodMetrics","verbs":["get","list"]}]}

If you receive a `NotFound` error, then you’ll need to [install Metrics Server](https://github.com/kubernetes-sigs/metrics-server#installation):

```console
$ kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

Verify Metrics Server has been successfully deployed:

```console
kubectl get deployment metrics-server -n kube-system
```

NAME             READY   UP-TO-DATE   AVAILABLE   AGE
metrics-server   1/1     1            1           2m2s

## [](#reserve-nodes-for-the-workload-generator)Reserve Nodes for the Workload Generator

Later on in this tutorial we’ll be using a separate application to generate a query workload that will induce auto-scaling. So before we deploy anything, we need to reserve one of our Kubernetes worker nodes for exclusively running this application. We can do this by applying a scheduling tolerance with the following commands:

```console
$ APP_NODE=$(kubectl get nodes | grep Ready | head -1  | awk '{print $1}')
```

```console
$ kubectl taint nodes $APP_NODE type=app:NoSchedule
```

## [](#create-the-couchbase-cluster-deployment)Create the Couchbase Cluster Deployment

Now that we’ve reserved a worker node for our query generator, we can start setting up our Couchbase deployment. To speed up the process, we’ll be using the Couchbase Helm chart to conveniently install a Couchbase cluster that has auto-scaling enabled for the nodes running the Query Service nodes.

Run the following command to create a file with the necessary override values for the Couchbase chart:

```console
$ cat << EOF > autoscale_values.yaml
---
cluster:
  cluster:
    dataServiceMemoryQuota: 4Gi
    indexServiceMemoryQuota: 6Gi
  autoscaleStabilizationPeriod: 30s (1)
  name: scale-couchbase-cluster
  servers:
    default:
      size: 3
      services:
        - data
        - index
      resources:
        limits:
          cpu: 3
          memory: 12Gi
        requests:
          cpu: 3
          memory: 12Gi
    query:
      size: 2
      autoscaleEnabled: true (2)
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
    kind: CouchbaseEphemeralBucket
    evictionPolicy: nruEviction
EOF
```

| **1** | autoscaleStabilizationPeriod: Setting this to 30 seconds allows time for the Query Service to stabilize after new nodes have been added to cluster. This value is used for demonstration purposes only. Please refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance about what values you should use in production. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | autoscaleEnabled: Setting this field to true enables auto-scaling for the server class that contains the Query Service.                                                                                                                                                                                                                                                                          |

Now, install the Couchbase chart, making sure to specify the values override file we just created:

```console
$ helm install -f autoscale_values.yaml scale couchbase/couchbase-operator
```

|  | The Couchbase chart deploys the Autonomous Operator by default. If you already have the Autonomous Operator deployed in the current namespace, then you’ll need to specify additional overrides during chart installation so that only the Couchbase cluster is deployed: $ helm install -f autoscale\_values.yaml --set install.couchbaseOperator=false,install.admissionController=false scale couchbase/couchbase-operator |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#verify-the-installation)Verify the Installation

The configuration we’re using calls for a five-node Couchbase cluster (three `default` nodes and two `query` nodes), which will take a few minutes to be created. You can run the following command to verify the deployment status:

```console
$ kubectl describe couchbasecluster scale-couchbase-cluster
```

In the console output, you should check for the events that signal the creation of the five nodes in the Couchbase cluster, as well as the creation of a [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource for the `query` server class configuration:

Events:
  Type    Reason                  Age   From  Message
  ----    ------                  ----  ----  -------
  Normal  EventNewMemberAdded     22m         New member scale-couchbase-cluster-0004 added to cluster
  ...
  Normal  EventAutoscalerCreated  22m         Autoscaler for config `query` added

The Autonomous Operator automatically creates a [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource for each server class configuration that has [couchbaseclusters.spec.servers.autoscaleEnabled](resource/couchbasecluster.md#couchbaseclusters-spec-servers-autoscaleenabled) set to `true`. The Operator also keeps the size of the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource in sync with the size of its associated server class configuration.

Run the following command to verify that the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource exists and matches the size of its associated server configuration:

```console
$ kubectl get couchbaseautoscalers
```

NAME                            SIZE   SERVERS
query.scale-couchbase-cluster   2      query **(1)** **(2)**

In the console output, you’ll see:

| **1** | NAME: The Autonomous Operator creates [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resources with the name format _<server-class>_._<cluster-name>_. Considering that we enabled auto-scaling for the query server class configuration, and the name of our cluster is scale-couchbase-cluster, we can determine that the name of the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource created by the Autonomous Operator will be query.scale-couchbase-cluster.                    |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | SIZE: This is the current number of Couchbase nodes that the Autonomous Operator is maintaining for the query server class. Considering that we set servers.query.size to 2 in our cluster configuration, and because the cluster doesn’t yet have the ability to automatically scale, we can expect that the SIZE listed here will be 2. Once we create an HPA for the query server class, and the number of query nodes begins to scale, the SIZE will update to reflect the number of nodes currently being maintained. |

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

## [](#create-a-horizontal-pod-autoscaler)Create a Horizontal Pod Autoscaler

Now that we’ve confirmed that CPU metrics data are being collected, we can create a `HorizontalPodAutoscaler` resource that targets this metric. For this tutorial, we’ll be configuring an HPA to scale the number of Couchbase `query` nodes in our cluster when the CPU usage of a `query` pod exceeds 70%. When CPU usage exceeds 70%, additional `query` nodes will be added, and when usage falls below 70% then the HPA will consider scaling down to reduce overhead. This example shows both scaling up and scaling down.

Run the following command to create a `HorizontalPodAutoscaler` resource that will take action when the CPU of a `query` pod exceeds 70%:

```console
$ cat << EOF | kubectl apply -f -
---
kind: HorizontalPodAutoscaler
apiVersion: autoscaling/v2
metadata:
  name: query-cpu-hpa
spec:
  scaleTargetRef:
    apiVersion: couchbase.com/v2
    kind: CouchbaseAutoscaler (1)
    name: query.scale-couchbase-cluster (2)
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 30
      policies:
      - type: Pods
        value: 1
        periodSeconds: 15
    scaleDown:
      stabilizationWindowSeconds: 60 (3)
  minReplicas: 2 (4)
  maxReplicas: 6 (5)
  metrics:
  - type: Resource
    resource:
      name: cpu (6)
      target:
        type: Utilization
        averageUtilization: 70 (7)
EOF
```

| **1** | scaleTargetRef.kind: This field must be set to [CouchbaseAutoscaler](resource/couchbaseautoscaler.md), which is the kind of custom resource that gets automatically created by the Autonomous Operator when you enable auto-scaling for a particular server class.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | scaleTargetRef.name: This field needs to reference the name of the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource. Since the Autonomous Operator creates [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resources with the name format _<server-class>_._<cluster-name>_, the name we’ll need specify is query.scale-couchbase-cluster. As described previously in the [Verify the Installation](#verify-the-installation) section, a quick way to view the existing [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resources (and their names) is to run the following command: $ kubectl get couchbaseautoscalers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **3** | scaleDown.stabilizationWindowSeconds: This field can be used to control scaling down behavior, in this instance we indicate to [scale down after 60 seconds](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#example-change-downscale-stabilization-window) as described in the [official documentation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#stabilization-window). Scaling down can also be prevented entirely using a policy of selectPolicy: Disabled. Other policies are available and fully documented in the [Kubernetes documentation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#scaling-policies).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **4** | minReplicas: This field sets the minimum number of Couchbase nodes for the specified server class. Here, we’ve set the minimum number of query nodes to 2. This means that number of query nodes will never be down-scaled to fewer than two nodes, even if the HPA detects that the target metric is relatively below the target value. Setting minReplicas is important for maintaining service availability. Refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance on setting this value in production environments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **5** | maxReplicas: This field sets the maximum number of Couchbase nodes for the specified server class. It cannot be set to a value lower than what is defined for minReplicas. Here, we’ve set the maximum number of query nodes to 6. This means that number of query nodes will never be up-scaled to more than six nodes, even if the HPA detects that the target metric is still relatively above the target value. Setting a value for maxReplicas is required because it provides important protection against runaway scaling events. Refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance on setting this value in production environments. The [prerequisites](#before-you-begin) for this tutorial state that 10 Kubernetes worker nodes are required. So far we’re currently using five worker nodes for our Couchbase cluster (three default nodes and two query nodes), and have reserved one worker node for the workload generator. By setting maxReplicas to 6, we’re allowing the query server class to scale up to an additional four nodes if necessary, thus potentially requiring up to 10 worker nodes for our entire setup. |
| **6** | metrics.resource.name: The name of target metric that will be monitored by the HPA for the purposes of auto-scaling. Here, we’ve specified cpu as the metric that will be used to scale the number query nodes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **7** | metrics.resource.target.averageUtilization: Specifying the averageUtilization type means that the metric will be averaged across all of the pods. Here, by setting a value of 70, the HPA will scale the number of query nodes when the average CPU utilization across all query pods exceeds 70%.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

|  | Details about how sizing decisions are made are discussed in [Couchbase Cluster Auto-scaling](concept-couchbase-autoscaling.md). |
|  | -------------------------------------------------------------------------------------------------------------------------------- |

### [](#verify-horizontalpodautoscaler-status)Verify `HorizontalPodAutoscaler` Status

Now that we’ve created the `HorizontalPodAutoscaler` resource, the HPA will begin to monitor the target metric and report that the initial size (number) of the `query` nodes are within desired range. Run the following command to print these details to the console output:

```console
$ kubectl describe hpa query-cpu-hpa
```

Metrics:                                               ( current / target )
  resource cpu on pods  (as a percentage of request):  1% (50m) / 70% **(1)**
Min replicas:                         2
Max replicas:                         6
CouchbaseAutoscaler pods:             2 current / 2 desired  **(2)**

| **1** | Here we see that the current CPU utilization is currently 1% out of the current 70% target.                          |
| ----- | -------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we see that there are currently 2 query nodes in the cluster, and 2 are desired to maintain the current target. |

## [](#test-the-auto-scaling-behavior)Test the Auto-scaling Behavior

At this point, we’ve completed all the necessary steps to configure our cluster deployment to automatically scale the number of `query` nodes. If the average CPU utilization across current `query` nodes exceeds 70%, an additional `query` node will be added to the cluster.

However, we should test our configuration to be sure that `query` nodes will automatically scale as expected To do this, we’ll be attempting to induce auto-scaling behavior by generating a specific workload for the Query Service.

### [](#load-data)Load Data

Before we can generate a workload for the Query Service, we need to load some data into our cluster. Run the following command to create a Kubernetes Job that loads the Travel Sample data-set provided by the `cbdocloader` tool:

```console
$ cat << EOF | kubectl apply -f -
---
apiVersion: batch/v1
kind: Job
metadata:
  name: travel-sample-dataset
spec:
  template:
    spec:
      containers:
      - name: travel-sample
        image: couchbase/server:7.2.3
        command: ["/opt/couchbase/bin/cbdocloader",
                  "-c", "scale-couchbase-cluster-0000.default.svc",
                  "-u", "developer", "-p", "password",
                  "-b" ,"travel-sample",
                  "-m", "100",
                  "-d", "/opt/couchbase/samples/travel-sample.zip"]
      restartPolicy: Never
      tolerations:
      - key: "type"
        operator: "Equal"
        value: "app"
        effect: "NoSchedule"

EOF
```

You can check the Couchbase Web Console to ensure that the data set has been loaded. You should also see that indexes have been created for querying the documents.

### [](#apply-query-workload)Apply Query Workload

Now that the Travel Sample data has been loaded and indexed, we can put a CPU-intensive load on the Query Service that should trigger auto-scaling to occur. For this tutorial we’ll be using an experimental tool called `n1qlgen` to apply stress for a set duration of time.

Run the following command to initiate the query workload:

```console
$ cat << EOF | kubectl apply -f -
---
apiVersion: batch/v1
kind: Job
metadata:
  name: n1qlgen-1
spec:
  template:
    spec:
      containers:
      - name: n1qlgen
        image: tahmmee/n1qlgen:v2
        imagePullPolicy: Always
        command: ["/go/bin/n1qlgen",
                  "-pod=scale-couchbase-cluster-0003", (1)
                   "-cluster=scale-couchbase-cluster",
                   "-bucket=travel-sample",
                   "-username=developer",
                   "-password=password",
                   "-duration=600", "-concurrency=20", (2)
                   "-seed=1234"] (3)
      restartPolicy: Never
EOF
```

| **1** | This needs to be the name of one of the query pods.                                                                               |
| ----- | --------------------------------------------------------------------------------------------------------------------------------- |
| **2** | You can use duration and concurrency to adjust workload stress, but the example values should work fine for our purposes.         |
| **3** | You can use seed to adjust randomness for running multiple jobs, but again, the example values should work fine for our purposes. |

### [](#verify-auto-scaling)Verify Auto-scaling

CPU utilization of the `query` pods should increase as the query generation tool applies stress to the cluster. Run the following command to view the behavior of the HPA:

```console
$ kubectl describe hpa query-cpu-hpa
```

You should expect output similar to the following:

...
Reference:                                             CouchbaseAutoscaler/query.scale-couchbase-cluster
Metrics:                                               ( current / target )
  resource cpu on pods  (as a percentage of request):  91% (2751m) / 70% **(1)**
Events:
  Type    Reason             Age   From                       Message
  ----    ------             ----  ----                       -------
  Normal  SuccessfulRescale  45s   horizontal-pod-autoscaler  New size: 3; reason: cpu resource utilization (percentage of request) above target **(2)**
  Normal  SuccessfulRescale  2m19s  horizontal-pod-autoscaler  New size: 4; reason: cpu resource utilization (percentage of request) above target

| **1** | The HPA has detected 91% CPU utilization.                                                                                                                                                                                                                                                                                                                                                                                         |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The number of query nodes has been scaled from 2 to 3. The following [scaling algorithm](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details) was applied by the HPA to determine the desired replicas: desiredReplicas = ceil\[currentReplicas \* ( currentMetricValue / desiredMetricValue )\]               3 = ceil\[       2        \* (      91.0        /     70.0            )\] |

After 10 minutes the query generator will complete and the number of `query` nodes will eventually scale back down to the previously-configured minimum of two nodes.

|  | If your CPU utilization didn’t reach the target value, you can try with a lower CPU utilization threshold, or apply additional query generators by adjusting the concurrency and seed values. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#optional-limit-scale-down-rate)Optional: Limit Scale Down Rate

When we created the `HorizontalPodAutoscaler` resource in a [previous step](#create-a-horizontal-pod-autoscaler), we specified a `scaleDown` [stabilization window](concept-couchbase-autoscaling.md#horizontal-pod-stabilization) of 60 seconds. During this time the nodes will be monitored, and if their loading has reduced below the target threshold, then they will be considered for scaling down. They will then scale down according to the rules of the HPA policy being used. Since the query generator cuts off the workload completely after a certain duration, down-scaling will happen rapidly after the generator has completed its run.

You may find that rapid down-scaling is not desirable for your environment and workload, or perhaps you want to disable automatic down-scaling completely in favor of manual down-scaling. These types of configurations can be accomplished by customizing the `scaleDown` policy in the `HorizontalPodAutoscaler` resource.

First, let’s consider the scenario where we want to reduce the rate of down-scaling. We can accomplish this by configuring a policy that scales in smaller [_increments_](concept-couchbase-autoscaling.md#scaling-increments):

```console
$ cat << EOF | kubectl apply -f -
---
kind: HorizontalPodAutoscaler
apiVersion: autoscaling/v2
metadata:
  name: query-cpu-hpa
spec:
  scaleTargetRef:
    apiVersion: couchbase.com/v2
    kind: CouchbaseAutoscaler
    name: query.scale-couchbase-cluster
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 30
      policies:
      - type: Pods
        value: 1
        periodSeconds: 15
    scaleDown:
      stabilizationWindowSeconds: 60
      policies:
      - type: Pods
        value: 1 (1)
        periodSeconds: 60
      selectPolicy: Min (2)
  minReplicas: 2
  maxReplicas: 6
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
EOF
```

| **1** | This policy specifies that the HPA will only make scale-down recommendations in increments of one replica.                  |
| ----- | --------------------------------------------------------------------------------------------------------------------------- |
| **2** | Setting policy selection to Min tells the HPA to always select the policy that results in the least amount of down-scaling. |

To see this configuration in action, run the above command to apply it to the existing `HorizontalPodAutoscaler` resource, and then repeat [Apply Query Workload](#apply-query-workload). You can monitor the pods and see them drop back down eventually to their starting point at a rate of one replica per minute.

If you want to try disabling down-scaling completely, you can instead set policy selection to `Disabled`:

```console
$ cat << EOF | kubectl apply -f -
---
kind: HorizontalPodAutoscaler
apiVersion: autoscaling/v2
metadata:
  name: query-cpu-hpa
spec:
  scaleTargetRef:
    apiVersion: couchbase.com/v2
    kind: CouchbaseAutoscaler
    name: query.scale-couchbase-cluster
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 30
      policies:
      - type: Pods
        value: 1
        periodSeconds: 15
    scaleDown:
      stabilizationWindowSeconds: 60
      policies:
      - type: Pods
        value: 1
        periodSeconds: 60
      selectPolicy: Disabled (1)
  minReplicas: 2
  maxReplicas: 6
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
EOF
```

| **1** | Disabling down-scaling means that the cluster only ever scales up. This can be useful when sizing it to a maximum load and to keep it there. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------- |

To see this configuration in action, run the above command to apply it to the existing `HorizontalPodAutoscaler` resource, and then repeat [Apply Query Workload](#apply-query-workload). You can monitor the pods and see them scale up, after the workload generator finishes its run, the number of pods will never scale down.

## [](#cleaning-up)Cleaning up

Running the commands in this section will uninstall all of the resources that were created during the course of this tutorial.

Remove workload jobs:

```console
$ kubectl delete jobs travel-sample-dataset n1qlgen-1
```

Delete the HPA:

```console
$ kubectl delete hpa query-cpu-hpa
```

Uninstall both the Autonomous Operator and Couchbase cluster by deleting the Helm release:

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

You will very likely need to do some experimentation before settling on a particular metric and target value that makes sense for your workload objectives. Refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance when determining the best target value for CPU utilization when scaling Query Service nodes.

## [](#further-reading)Further Reading

* Concepts: [Couchbase Cluster Auto-scaling](concept-couchbase-autoscaling.md)
* Best Practices: [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md)
* Reference: [CouchbaseAutoscaler Resource](resource/couchbaseautoscaler.md)
* Reference: [Autoscaling Lifecycle Events](reference-couchbasecluster-events.md#autoscaling-lifecycle)