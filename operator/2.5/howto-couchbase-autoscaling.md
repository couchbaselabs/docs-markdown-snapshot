---
title: Configure Couchbase Cluster Auto-scaling
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.5/modules/ROOT/pages/howto-couchbase-autoscaling.adoc
  xref: xref:2.5@operator::howto-couchbase-autoscaling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/howto-couchbase-autoscaling.html)

# Configure Couchbase Cluster Auto-scaling

> Configure Couchbase clusters to automatically scale based on observed usage metrics. 

## [](#overview)Overview

The Autonomous Operator supports [Multi-Dimensional Scaling](concept-mds.md) through independently-configurable server classes, which are [manually scalable](howto-couchbase-scale.md) by default. However, the Autonomous Operator optionally supports the automatic scaling of Couchbase clusters through an integration with the [Horizontal Pod Autoscaler (HPA)](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/).

The sections on this page describe how to enable and configure auto-scaling for Couchbase clusters managed by the Autonomous Operator. For a conceptual description of this feature, please refer to [Couchbase Cluster Auto-scaling](concept-couchbase-autoscaling.md).

## [](#preparing-for-auto-scaling)Preparing for Auto-scaling

Metrics play the most important role in Couchbase cluster auto-scaling. Metrics provide the means for the Horizontal Pod Autoscaler to measure cluster performance and respond accordingly when target thresholds are crossed.

Auto-scaling can be configured to use _resource metrics_ or _Couchbase metrics_. Resource metrics include pod CPU and memory, whereas Couchbase metrics can be stats like bucket memory utilization and query latency. Refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance on how various metrics can be used as a measure of cluster performance.

The Horizontal Pod Autoscaler can only monitor metrics through the Kubernetes API, therefore metrics affecting the Couchbase cluster must be exposed within the Kubernetes cluster before auto-scaling can be configured. Refer to [About Exposed Metrics](concept-couchbase-autoscaling.md#about-exposed-metrics) in the concept documentation for more information about how metrics can be exposed for the purposes of auto-scaling.

## [](#enabling-auto-scaling)Enabling Auto-scaling

Enabling auto-scaling for a particular Couchbase cluster starts with modifying the relevant [CouchbaseCluster](resource/couchbasecluster.md) resource.

The required configuration parameters for enabling log forwarding are described in the example below. (The Autonomous Operator will set the default values for any fields that are not specified by the user.)

Basic [CouchbaseCluster](resource/couchbasecluster.md) Auto-Scaling Parameters

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  servers:
  - name: data
    size: 3
    services:
    - data
  - name: index
    autoscaleEnabled: true (1)
    size: 2
    services:
    - index
  - name: query
    autoscaleEnabled: true (2)
    size: 2
    services:
    - query
  autoscaleStabilizationPeriod: 600s (3)
```

| **1** | [couchbaseclusters.spec.servers.autoscaleEnabled](resource/couchbasecluster.md#couchbaseclusters-spec-servers-autoscaleenabled): Setting this field to true triggers the Autonomous Operator to create a [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource for the relevant server class. In this example, a [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource will be created for the index server class. Refer to [About the Couchbase Autoscaler](concept-couchbase-autoscaling.md#about-the-couchbase-autoscaler) for a conceptual overview of the role the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource plays in auto-scaling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | In this example, a [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource will also be created for the query server class.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **3** | [couchbaseclusters.spec.autoscaleStabilizationPeriod](resource/couchbasecluster.md#couchbaseclusters-spec-autoscalestabilizationperiod): This field defines the [_Couchbase Stabilization Period_](concept-couchbase-autoscaling.md#couchbase-stabilization-period), which is an internal safety mechanism provided by the Autonomous Operator that is meant to help prevent over-scaling caused by metrics instability during rebalance. The value specified in this field determines how long [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resources will remain in [_maintenance mode_](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#implicit-maintenance-mode-deactivation) after the cluster finishes rebalancing. In this example, the stabilization period has been set to 600s, which means that the Horizontal Pod Autoscaler will not restart monitoring until 10 minutes after the previous rebalance has completed. Refer to [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md) for additional guidance on setting this value in production environments. |

After deploying the [CouchbaseCluster](resource/couchbasecluster.md) resource specification, the Autonomous Operator will create a [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource for each server class configuration that has [couchbaseclusters.spec.servers.autoscaleEnabled](resource/couchbasecluster.md#couchbaseclusters-spec-servers-autoscaleenabled) set to `true`.

> [!IMPORTANT]
> Enabling auto-scaling for a particular server class configuration **does not** immediately subject the cluster to being auto-scaled. The [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource simply acts as an endpoint for the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource to access the pods that are selected for auto-scaling. The [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource is only activated when [referenced](#creating-a-horizontalpodautoscaler-resource) by a [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource.

### [](#verifying-creation-of-couchbaseautoscaler-resources)Verifying Creation of `CouchbaseAutoscaler` Resources

The following command can be used to verify that the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resources exist and match the size of their associated server class configurations:

```console
$ kubectl get couchbaseautoscalers
```

NAME                               SIZE   SERVERS
index.cb-example                   2      index **(1)** **(2)**
query.cb-example                   2      query

| **1** | NAME: Each [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource is named using the format _<server-class>_._<couchbase-cluster>_. The name is important as it must be referenced when [creating the HorizontalPodAutoscaler resource](#creating-a-horizontalpodautoscaler-resource) in order link the two resources together. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | SIZE: This is the current number of Couchbase nodes that the Autonomous Operator is maintaining for the index server class. The Autonomous Operator keeps the size of a [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource in sync with the size of its associated server class configuration.                              |

> [!IMPORTANT]
> [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resources are fully managed by the Autonomous Operator and should not be manually created, modified, or deleted by the user. If one is manually deleted, the Autonomous Operator will re-create it. However, it is possible to edit the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) (refer to [\[scale-subresource\]](#scale-subresource) below).
> 
> A [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource only gets deleted by the Autonomous Operator when [auto-scaling is disabled](#disabling-auto-scaling) for the associated server class, or if the associated [CouchbaseCluster](resource/couchbasecluster.md) resource is deleted altogether.

## [](#creating-a-horizontalpodautoscaler-resource)Creating a `HorizontalPodAutoscaler` Resource

The Autonomous Operator relies on the Kubernetes [Horizontal Pod Autoscaler (HPA)](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) to provide auto-scaling capabilities. The Horizontal Pod Autoscaler is configured via a [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource, which is the primary interface by which auto-scaling is configured. Unlike the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource created by the Autonomous Operator, the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource is created and managed by the user.

The following configuration represents an example to scale the server class from [Enabling Auto-scaling](#enabling-auto-scaling).

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: query-hpa
spec:
  scaleTargetRef: (1)
    apiVersion: couchbase.com/v2
    kind: CouchbaseAutoscaler
    name: query.cb-example
  behavior: (2)
    scaleUp:
      policies: (3)
      - type: Pods
        value: 1
        periodSeconds: 15
      stabilizationWindowSeconds: 30 (4)
    scaleDown:
      stabilizationWindowSeconds: 300
  minReplicas: 2 (5)
  maxReplicas: 6
  metrics: (6)
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

| **1** | The spec.scaleTargetRef section must be configured to reference the relevant [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource. apiVersion: This field must be set to be set to couchbase.com/v2. kind: This field must be set to CouchbaseAutoscaler. name: This field must reference the unique name of the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource. As discussed in the previous section, [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resources are automatically created by the Autonomous Operator using the name format _<server-class>_._<couchbase-cluster>_. Refer to [Referencing the Couchbase Autoscaler](concept-couchbase-autoscaling.md#referencing-the-couchbase-autoscaler) in the concept documentation for more detailed information about these fields. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Fine-grained [_scaling behavior_](concept-couchbase-autoscaling.md#scaling-behavior) is configured via _policies_ specified in the spec.behavior section. Different policies can be specified for scaling up (behavior.scaleUp) and scaling down (behavior.scaleDown). If no user-supplied values are specified in behavior fields, then the [default values](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#default-behavior) are used.                                                                                                                                                                                                                                                                                                                                                                |
| **3** | spec.behavior.\[\].policies: Scaling policies are made up of the following fields: type, value, and periodSeconds. The recommended settings are type: Pods and value: 1, while leaving periodSeconds with the default value. Refer to [Scaling Policies](concept-couchbase-autoscaling.md#scaling-policies) and [Scaling Increments](concept-couchbase-autoscaling.md#scaling-increments) in the concept documentation for more detailed information about these fields.                                                                                                                                                                                                                                                                                                                                                            |
| **4** | behavior.\[\].stabilizationWindowSeconds: A [_stabilization window_](concept-couchbase-autoscaling.md#horizontal-pod-stabilization) can be configured as a means to control undesirable scaling caused by fluctuating metrics. A minimum scaleUp stabilization window of 30 seconds is generally recommended, unless indicated otherwise in [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md).                                                                                                                                                                                                                                                                                                                                                                                       |
| **5** | The spec.minReplicas and spec.maxReplicas fields set the minimum and maximum number of Couchbase nodes for the associated server class. minReplicas sets the boundary for the number of Couchbase nodes that the associated server class can ever be down-scaled to, and defaults to 1. This field is important for maintaining service availability. maxReplicas sets the upper boundary for the number of Couchbase nodes that the associated server class can ever be up-scaled to, and cannot be set to a value lower than what is defined for minReplicas. This field is _required_, as it provides important protection against runaway scaling events. Refer to [Sizing Constraints](concept-couchbase-autoscaling.md#sizing-constraints) in the concept documentation for more detailed information about these fields.     |
| **6** | The spec.metrics section must target a specific _metric_, along with an associated _threshold_ for that metric. In this example, a Kubernetes resource metric (cpu) is being targeted with a threshold set to 70 percent utilization. Refer to [Target Metrics and Thresholds](concept-couchbase-autoscaling.md#target-metrics-and-thresholds) in the concept documentation for more detailed information about targeting metrics in the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource.                                                                                                                                                                                                                                           |

The [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource can be created like any other resource by submitting the specifications in a file using `kubectl`:

```console
$ kubectl apply -f query-hpa.yaml
```

As soon as the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource has been successfully created, the Horizontal Pod Autoscaler will begin to monitor the target metric and the cluster will be subject to auto-scaling if the targeted metric is above or below the configured threshold.

### [](#verifying-horizontalpodautoscaler-status)Verifying `HorizontalPodAutoscaler` Status

When the Horizontal Pod Autoscaler begins to monitor the target metric, it will begin reporting the value of metric along with the current vs desired size of the server class.

Run the following command to print these details to the console output:

```console
$ kubectl describe hpa query-hpa
```

Metrics:                                               ( current / target )
  resource cpu on pods  (as a percentage of request):  1% (50m) / 70% **(1)**
Min replicas:                         2
Max replicas:                         6
CouchbaseAutoscaler pods:             2 current / 2 desired  **(2)**

| **1** | The current observed value of the metric is displayed vs the target threshold.                                                      |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The current size of the server class is displayed vs the desired size currently being recommended by the Horizontal Pod Autoscaler. |

## [](#disabling-scale-down)Disabling Scale Down

In production environments, it may be desirable to only allow a cluster to automatically scale up while requiring manual intervention to scale down. This can be accomplished by modifying the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource as follows:

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: example-hpa
spec:
  behavior:
    scaleDown:
      selectPolicy: Disabled (1)
```

| **1** | spec.behavior.\[\].selectPolicy: This field controls which policy is chosen by the Horizontal Pod Autoscaler if more than one policy is defined. When set to Disabled no policy is chosen, and therefore auto-scaling is disabled in that direction. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

By setting `spec.behavior.scaleDown.selectPolicy` to `Disabled`, the Horizontal Pod Autoscaler will never recommend scaling down the associated server class. Specifying this setting for all [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resources associated with a particular Couchbase cluster ensures that the cluster will never automatically scale down.

Clusters that have automatic down-scaling disabled can be manually scaled down by editing the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource directly:

```console
$ kubectl scale --replicas=2 query.cb-example
```

The above command edits the [_scale subresource_](concept-couchbase-autoscaling.md#scale-subresource) and results in the Autonomous Operator scaling the server class named `query` to a size of `2`.

## [](#disabling-auto-scaling)Disabling Auto-scaling

Auto-scaling, having been [enabled](#enabling-auto-scaling) and configured for a Couchbase cluster, can subsequently be _disabled_.

The recommended method for disabling auto-scaling is to set [couchbaseclusters.spec.servers.autoscaleEnabled](resource/couchbasecluster.md#couchbaseclusters-spec-servers-autoscaleenabled) back to `false` for each of the desired server classes.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  servers:
  - name: index
    autoscaleEnabled: false (1)
    size: 2
    services:
    - index
  - name: query
    autoscaleEnabled: false
    size: 2
    services:
    - query
```

| **1** | [couchbaseclusters.spec.servers.autoscaleEnabled](resource/couchbasecluster.md#couchbaseclusters-spec-servers-autoscaleenabled): Setting this field to false triggers the Autonomous Operator to delete the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) custom resource that had previously been created for the relevant server class. In this example, the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource associated with the index server class will be deleted by the Autonomous Operator upon submitting the configuration. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

Upon deleting the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource, the Autonomous Operator will no longer reconcile the current size of the server class with the recommendations of the Horizontal Pod Autoscaler, and instead the value specified in [couchbaseclusters.spec.servers.size](resource/couchbasecluster.md#couchbaseclusters-spec-servers-size) will become the new source of truth. For example, if the above configuration were to be submitted, it would result in the `index` and `query` server classes each being scaled to `size: 2` from whatever size they had previously been auto-scaled to.

It's important to note, however, that the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource is not managed by the Autonomous Operator, and therefore does not get deleted along with the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource. It will continue to exist in the current namespace until it is manually deleted by the user. Since the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource can continue to be used if auto-scaling is subsequently re-enabled, it is important to [verify the status](#verifying-horizontalpodautoscaler-status) of the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource to ensure that it is persisted as expected.

If the desire is to only temporarily disable auto-scaling, the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource can be left to persist until auto-scaling is eventually re-enabled. This only works if the names of both the server class and the Couchbase cluster remain the same, because when [couchbaseclusters.spec.servers.autoscaleEnabled](resource/couchbasecluster.md#couchbaseclusters-spec-servers-autoscaleenabled) is set back to `true`, the Autonomous Operator will create a [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource that is already [referenced](concept-couchbase-autoscaling.md#referencing-the-couchbase-autoscaler) by the existing [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource. In this case, the cluster will immediately become subject to the recommendations of the Horizontal Pod Autoscaler.

> [!NOTE]
> Deleting just the [HorizontalPodAutoscaler](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#horizontalpodautoscaler-v2-autoscaling) resource will also have the effect of "disabling" auto-scaling. In this scenario, the Autonomous Operator continues to maintain the [CouchbaseAutoscaler](resource/couchbaseautoscaler.md) resource, but it will remain at the same size that was last recommended by the Horizontal Pod Autoscaler before it was deleted.

## [](#related-links)Related Links

* **Learn**: [Couchbase Cluster Auto-scaling](concept-couchbase-autoscaling.md)
* **Learn**: [Couchbase Cluster Auto-scaling Best Practices](concept-couchbase-autoscaling-best-practices.md)
* **Tutorial**: [Auto-scaling the Couchbase Query Service](tutorial-autoscale-query.md)
* **Tutorial**: [Auto-scaling the Couchbase Data Service](tutorial-autoscale-data.md)
* **Tutorial**: [Auto-scaling the Couchbase Index Service](tutorial-autoscale-index.md)
* **Reference**: [CouchbaseAutoscaler Resource](resource/couchbaseautoscaler.md)
* **Reference**: [Auto-scaling Lifecycle Events](reference-couchbasecluster-events.md#autoscaling-lifecycle)