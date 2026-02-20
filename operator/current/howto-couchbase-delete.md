---
title: Delete a Couchbase Deployment
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.9/modules/ROOT/pages/howto-couchbase-delete.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:operator::howto-couchbase-delete.adoc[]
---

[View original HTML](/operator/current/howto-couchbase-delete.html)

# Delete a Couchbase Deployment

You can delete a cluster either by using the cluster configuration file that you created the cluster with, or by deleting the cluster directly.

## [](#deleting-a-cluster-using-the-cluster-configuration-file)Deleting a Cluster Using the Cluster Configuration File

To delete a cluster using the cluster configuration file, say `my-cluster.yaml`, run the following command:

On Kubernetes:

```console
$ kubectl delete -f my-cluster.yaml
```

On OpenShift:

```console
$ oc delete -f my-cluster.yaml
```

## [](#deleting-a-cluster-directly)Deleting a Cluster Directly

To delete a cluster directly, say `my-cluster`, run the following command:

On Kubernetes:

```console
$ kubectl delete couchbasecluster my-cluster
```

On OpenShift:

```console
$ oc delete couchbasecluster my-cluster
```