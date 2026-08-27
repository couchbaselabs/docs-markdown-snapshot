---
title: Interaction with Auto-Scaling
description: How Cloud Native Gateway interacts with Kubernetes auto-scaling,
  including Horizontal Pod Autoscaler, Cluster Autoscaler, and Couchbase cluster
  scaling.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/availability-and-failover/pages/interaction-with-auto-scaling.adoc
  xref: xref:cloud-native-gateway:availability-and-failover:interaction-with-auto-scaling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/availability-and-failover/interaction-with-auto-scaling.html)

# Interaction with Auto-Scaling

> How Cloud Native Gateway interacts with Kubernetes auto-scaling, including Horizontal Pod Autoscaler, Cluster Autoscaler, and Couchbase cluster scaling. 

## [](#couchbase-cluster-scaling)Couchbase Cluster Scaling

This section describes how Cloud Native Gatewat adapts to changes in the Couchbase cluster size and how it interacts with Kubernetes scaling mechanisms.

### [](#scale-up-adding-nodes)Scale Up (Adding Nodes)

When new Couchbase Server nodes are added to the cluster:

1. The Couchbase Kubernetes Operator creates new pods with Cloud Native Gateway sidecars.
2. Cloud Native Gateway instances on existing pods detect the new nodes through configuration updates and update their internal routing tables.
3. New Cloud Native Gateway instances on the added pods connect to the cluster and begin accepting traffic.
4. A rebalance distributes data to the new nodes. During rebalance, Cloud Native Gateway instances transparently handle vbucket map changes and `NOT_MY_VBUCKET` responses by retrying against the correct nodes.
5. After rebalance completes, the Cloud Native Gateway Kubernetes Service includes the new Cloud Native Gateway instances, and the load balancer distributes client connections across all instances.

From the client perspective, scale-up is transparent. Clients do not need to reconfigure or reconnect.

### [](#scale-down-removing-nodes)Scale Down (Removing Nodes)

When Couchbase Server nodes are removed:

1. A rebalance moves data off the nodes being removed.
2. During rebalance, Cloud Native Gateway adapts to the changing vbucket map.
3. Once the rebalance completes, the removed pods (and their Cloud Native Gateway sidecars) are terminated.
4. Cloud Native Gateway instances on remaining pods update their routing tables to exclude the removed nodes.
5. The Kubernetes Service is updated to remove the terminated Cloud Native Gateway endpoints.

Clients with connections to the removed Cloud Native Gateway instances experience connection drops and reconnect through the load balancer to remaining instances. To minimize disruption, ensure the load balancer performs health checks and removes draining instances from the rotation before they are terminated.

## [](#horizontal-pod-autoscaler-hpa)Horizontal Pod Autoscaler (HPA)

he Horizontal Pod Autoscaler (HPA) automatically scales the number of Cloud Native Gateway pods based on resource utilization or custom metrics. The behavior depends on whether Cloud Native Gateway is deployed as a sidecar or standalone.

### [](#sidecar-deployments)Sidecar Deployments

In sidecar deployments, Cloud Native Gateway is part of the Couchbase pod and cannot be independently scaled by HPA. Cloud Native Gateway capacity is tied to the Couchbase cluster size.

If Cloud Native Gateway becomes a bottleneck (e.g., CPU-bound due to high connection counts or throughput), the options are:

* Increase the CPU resource allocation for the Cloud Native Gateway sidecar container.
* Scale the Couchbase cluster to add more nodes (and therefore more Cloud Native Gateway instances).

### [](#standalone-deployments)Standalone Deployments

In standalone deployments where Cloud Native Gateway runs as a separate Kubernetes Deployment, HPA can scale Cloud Native Gateway independently:

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: cng-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: cloud-native-gateway
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

Recommended scaling metrics:

* **CPU utilization** \- The primary indicator of Cloud Native Gateway capacity. Scale up when average CPU utilization exceeds 70%.
* **Active connection count** \- If available through custom metrics, scale based on the number of active gRPC connections per instance.

### [](#scaling-considerations)Scaling Considerations

* **Connection redistribution** \- When new Cloud Native Gateway instances are added, existing client connections are not redistributed. New connections will be balanced across all instances (including new ones), but existing connections remain on their current instance. Over time, as connections are recycled, traffic will naturally rebalance.
* **Cooldown periods** \- Set appropriate cooldown periods on the HPA to avoid thrashing. Cloud Native Gateway takes a few seconds to start and establish cluster connections, so rapid scale-up/scale-down can be counterproductive.
* **Minimum replicas** \- Always maintain at least 2 Cloud Native Gateway instances for high availability. A single Cloud Native Gateway instance is a single point of failure.

## [](#cluster-autoscaler)Cluster Autoscaler

The Kubernetes Cluster Autoscaler provisions and deprovisions worker nodes based on pod scheduling demands. Cloud Native Gateway does not have any special interaction with the Cluster Autoscaler.

Considerations:

* Ensure that the node pool used for Couchbase pods (with Cloud Native Gateway sidecars) has sufficient capacity and that the Cluster Autoscaler's maximum node count allows for the expected cluster size.
* Cloud Native Gateway's startup time (connecting to the cluster, initializing cbauth) adds to the time between a new node being provisioned and Cloud Native Gateway being ready to serve traffic.
* Configure Cloud Native Gateway's `--daemon` mode to handle the case where the Couchbase pod starts before the Couchbase cluster is ready.