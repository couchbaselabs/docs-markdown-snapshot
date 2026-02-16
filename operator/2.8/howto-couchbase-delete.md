[View original HTML](/operator/2.8/howto-couchbase-delete.html)

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