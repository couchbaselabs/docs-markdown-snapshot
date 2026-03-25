---
title: Couchbase Resource Label Selection
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.5/modules/ROOT/pages/concept-label-selection.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.5@operator::concept-label-selection.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/concept-label-selection.html)

# Couchbase Resource Label Selection

> The Autonomous Operator manages a Couchbase deployment by aggregating many different types of Kubernetes custom resources. By labeling resources, the Autonomous Operator knows which resources to select and aggregate into a logical configuration. 

## [](#overview)Overview

The `CouchbaseCluster` resource does not contain a single, monolithic configuration for an entire Couchbase cluster. Instead, configurations for things like buckets, replications, users, etc. are defined as separate resources, which the Autonomous Operator then selects and aggregates into a logical configuration. (One of the main reasons for this design is to allow for [custom resource RBAC](concept-rbac.md).)

All of the Couchbase resources outside of the main `CouchbaseCluster` type are collected by the Autonomous Operator using a list operation in the namespace of the Couchbase cluster. The list operation is optionally supplied with a user-defined _label selector_. Any resource that has the same set of _labels_ that match the label selector of a `CouchbaseCluster` resource will be aggregated.

## [](#default-selection-behavior)Default Selection Behavior

Let’s take the `CouchbaseBucket` resource for example. By default, when bucket management is enabled in the `CouchbaseCluster`, but no label selector is defined, the Autonomous Operator will select and aggregate any "label-less" bucket resources for management on the cluster. Refer to diagram below:

![selection default](_images/selection-default.png) 

Figure 1\. Default selection for a single cluster when no resource labels are defined

This default arrangement is well suited for when a single `CouchbaseCluster` resource is deployed in a single namespace. However, when _multiple_ `CouchbaseCluster` resources are deployed in the same namespace, this arrangement results in the Autonomous Operator selecting and aggregating all `CouchbaseBucket` resources to all `CouchbaseCluster` resources — meaning that each cluster would be managing the same buckets. Refer to diagram below:

![selection default shared](_images/selection-default-shared.png) 

Figure 2\. Default selection for multiple clusters when no resource labels are defined

While you might desire the sharing of resources for the purposes of reducing configuration overhead, it can lead to surprising outcomes if you are not aware of the underlying selection algorithm. For this reason, it is recommended that you specify explicit labels for resources, along with their corresponding label selectors for `CouchbaseCluster` resources. This ensures that the Autonomous Operator will only select and aggregate the appropriate resource for each cluster.

## [](#using-resource-labels)Using Resource Labels

To properly use resource labels, you’ll need to specify a label for each resource, as well as a corresponding label selector for each `CouchbaseCluster` resource.

It’s recommended that you start by adding a label selector to the `CouchbaseCluster` resource.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: my-cluster
spec:
  buckets:
    managed: true
    selector:
      matchLabels:
        cluster: my-cluster
```

The `CouchbaseCluster` configuration above will only select `CouchbaseBucket` resources that are labeled with `cluster: my-cluster`.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseBucket
metadata:
  name: my-bucket
  labels:
    cluster: my-cluster
```

The reason for defining the label selector first is that without a label selector defined, the Autonomous Operator will immediately aggregate any unlabeled resources to the `CouchbaseCluster` once it’s deployed. As discussed in the previous section, this can have deleterious effects if you have more than one `CouchbaseCluster` resource already deployed in the same namespace. However, by deploying the `CouchbaseCluster` resource with the bucket label selector `cluster: my-cluster` in this example, you can ensure that the cluster will only select `CouchbaseBucket` resources that have the matching `cluster: my-cluster` label.

![selection label selection basic](_images/selection-label-selection-basic.png) 

Figure 3\. Label selection with multiple clusters

> [!NOTE]
> You might notice that in the above configuration examples, the cluster has the same name as the bucket label (`my-cluster`). This is not a requirement and has no bearing on label selection. Only what is specified in the `selector` and `labels` fields is used. However, using the cluster name as the resource label can be helpful when you need to identify which cluster a resource is aggregated to.

## [](#sharing-resources)Sharing Resources

Resource sharing can still be achieved with label selection in the following ways:

1. Multiple `CouchbaseCluster` resources can have the same label selector defined. When a resource has the shared label, all of the `CouchbaseCluster` resources will select that resource.
2. A resource can have multiple different labels. When different `CouchbaseCluster` resources use different label selectors, they will share a resource if it has the labels required by both clusters.

In the previous sections, it was demonstrated that a bucket should be labeled such that it is specific to a cluster. With XDCR replications, however, the selector is per-remote cluster. Therefore, it is important to label and select replications so they are specific to a source cluster and a remote cluster. But if you intend to replicate a bucket from a source cluster to all defined remote clusters, the system is flexible enough to do so with a single `CouchbaseReplication` resource.