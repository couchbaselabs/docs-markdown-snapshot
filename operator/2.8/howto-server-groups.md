[View original HTML](/operator/2.8/howto-server-groups.html)

> How to configure server groups to provide high availability across data centers. 

Ensure you have read and understood the [server groups concepts](concept-server-groups.md) and how server group scheduling applies to your cluster.

## [](#configuring-kubernetes-node-labels)Configuring Kubernetes Node Labels

The Operator does not, and can not, have any prior knowledge of what Kubernetes node resides where. Kubernetes nodes are cluster scoped resources that we do not grant access to for security reasons.

Most cloud providers will label Kubernetes nodes to describe physical location based on availability zone. You can examine your cluster with the `kubectl get nodes` command to determine whether labels are already configured for your environment. If labeled, take a note of all availability zones and proceed to the [next section](#configuring-couchbase-cluster).

If not labeled, Kubernetes nodes must be in order to describe physical failure domains. The labels may map to any desired failure domain e.g. a data center, rack, switch, etc. This can be done with the following command:

```console
$ kubectl label nodes ip-172-16-0-10 topology.kubernetes.io/zone=us-east-1a
```

`ip-172-16-0-10` is the Kubernetes node name to apply the label to. The label key must be `topology.kubernetes.io/zone`. The label value (`us-east-1a`) can be anything you want.

## [](#configuring-couchbase-cluster)Configuring Couchbase Cluster

When configuring the cluster, you must specify the set of server groups that the Operator is allowed to schedule Couchbase Server pods across. Server group members correspond to Kubernetes `topology.kubernetes.io/zone` labels. For example:

```yaml
apiVersion: couchbase/v2
kind: CouchbaseCluster
spec:
  serverGroups: (1)
  - us-east-1a
  - us-east-1b
  - us-east-1c
  servers:
  - name: ServerClass1 (2)
  - name: ServerClass2 (3)
    serverGroups:
      - us-east-1a
      - us-east-1b
```

| **1** | [couchbaseclusters.spec.serverGroups](resource/couchbasecluster.md#couchbaseclusters-spec-servergroups) is a global default that can used by any server class.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | This server class does not have [couchbaseclusters.spec.servers.serverGroups](resource/couchbasecluster.md#couchbaseclusters-spec-servers-servergroups) defined. When the Operator schedules pods in this class it will default to server groups set with [couchbaseclusters.spec.serverGroups](resource/couchbasecluster.md#couchbaseclusters-spec-servergroups).                                                                                                                                                                                                                                                               |
| **3** | This server class has [couchbaseclusters.spec.servers.serverGroups](resource/couchbasecluster.md#couchbaseclusters-spec-servers-servergroups) defined. When the Operator schedules pods in this class it will override the global defaults set with [couchbaseclusters.spec.serverGroups](resource/couchbasecluster.md#couchbaseclusters-spec-servergroups) and use [couchbaseclusters.spec.servers.serverGroups](resource/couchbasecluster.md#couchbaseclusters-spec-servers-servergroups) instead. This is useful when a server class is sized in a way that cannot be fully balanced across the default set of server groups. |