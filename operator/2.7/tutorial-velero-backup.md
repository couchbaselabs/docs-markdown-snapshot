---
title: Backup with VMware Velero
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.7/modules/ROOT/pages/tutorial-velero-backup.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.7@operator::tutorial-velero-backup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.7/tutorial-velero-backup.html)

# Backup with VMware Velero

> How-to backup your Operator and Couchbase clusters against deletion. 

> [!WARNING]
> Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer.

[Velero](https://velero.io/) is a full system backup and restore tool. Unlike a Couchbase backup — that is only concerned with data and requires duplication — [Velero](https://velero.io/) allows an almost instantaneous backup of your data and Kubernetes resources. It achieves this by combining volume snapshots with resource archival to an external bucket.

This tutorial will step through a procedure to backup a Couchbase cluster, simulate a disaster and how to successfully recover.

> [!IMPORTANT]
> Use of [Velero](https://velero.io/) backup will only work with Operator version 2.0.0 or greater.

## [](#installing-velero)Installing Velero

Velero is a stand-alone binary that can be downloaded from their [website](https://velero.io/). This tutorial was tested using [Velero](https://velero.io/) version 1.2.0, using the Google Kubernetes Engine (GKE).

It is important to correctly configure [Velero](https://velero.io/) so that it has the ability to perform volume snapshots. A list of providers are provided in the [Velero support matrix](https://velero.io/docs/v1.2.0/supported-providers/).

## [](#installing-couchbase-autonomous-operator)Installing Couchbase Autonomous Operator

For this tutorial we will install the dynamic admission controller (DAC) in the default namespace:

```console
$ cao create admission -n default
serviceaccount/couchbase-operator-admission created
clusterrole.rbac.authorization.k8s.io/couchbase-operator-admission created
clusterrolebinding.rbac.authorization.k8s.io/couchbase-operator-admission created
secret/couchbase-operator-admission created
deployment.apps/couchbase-operator-admission created
service/couchbase-operator-admission created
mutatingwebhookconfiguration.admissionregistration.k8s.io/couchbase-operator-admission created
validatingwebhookconfiguration.admissionregistration.k8s.io/couchbase-operator-admission created
```

And the Operator in a separate, per-cluster namespace (`test`) as per our recommended best-practices:

```console
$ kubectl create namespace test
namespace/test created
```

```console
$ cao create operator -n test
serviceaccount/couchbase-operator created
role.rbac.authorization.k8s.io/couchbase-operator created
rolebinding.rbac.authorization.k8s.io/couchbase-operator created
deployment.apps/couchbase-operator created
service/couchbase-operator created
```

## [](#installing-couchbase-server)Installing Couchbase Server

Next up, create a Couchbase Server cluster:

```console
$ kubectl apply -n test -f secret.yaml
secret/cb-example-auth created
```

```console
$ kubectl apply -n test -f couchbase-cluster.yaml
couchbasebucket.couchbase.com/default created
couchbasecluster.couchbase.com/cb-example created
```

The Operator will begin to provision the cluster. In the mean time let’s have a look at the configuration:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseBucket
metadata:
  name: default
---
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  image: couchbase/server:7.6.0
  security:
    adminSecret: cb-example-auth
  buckets:
    managed: true (1)
  servers:
  - size: 3 (2)
    name: all_services
    services:
    - data
    - index
    - query
    volumeMounts: (3)
      default: couchbase
  volumeClaimTemplates:
  - metadata:
       name: couchbase
    spec:
      storageClassName: dynamic-bound
      resources:
        requests:
          storage: 1Gi
```

The configuration we have selected is fairly minimal:

| **1** | Buckets are managed, and we have created a default one for use.                                                                                              |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | The cluster has 3 nodes, totally arbitrary, but is a recommended starting point.                                                                             |
| **3** | Persistent volume mounts are in use, therefore data is persisted on a volume. [Velero](https://velero.io/) is able to take snapshots of the backing storage. |

Once the cluster has provisioned you can populate it with some data to prove that backups have worked. List the pod names and forward the console port:

```console
$ kubectl -n test get pods
NAME                                  READY   STATUS    RESTARTS   AGE
cb-example-0000                       1/1     Running   0          2m8s
cb-example-0001                       1/1     Running   0          98s
cb-example-0002                       1/1     Running   0          65s
```

```console
$ kubectl -n test port-forward cb-example-0000 8091
```

From here connect to `http://localhost:8091` and log into the console. Try manually adding some documents to the `default` bucket. From the dashboard home page you can see disk IO as these documents are flushed to disk and persisted.

## [](#creating-a-velero-backup)Creating a Velero Backup

The following is a typical backup command:

```console
$ velero backup create \
  test \ (1)
  --include-namespaces test \ (2)
  --include-resources couchbaseclusters.couchbase.com,couchbasebuckets.couchbase.com,persistentvolumes,persistentvolumeclaims,secrets,deployments,roles.rbac.authorization.k8s.io,rolebindings.rbac.authorization.k8s.io,serviceaccounts,configmaps (3)
```

| **1** | test is the name of the backup we wish to create. This is globally scoped so needs to be unique.                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | We specify that this backup should only look at the test namespace. This is another good reason for deploying Couchbase clusters in their own namespaces — you can limit the scope of and control third party applications.                                                                                                                                                                                                                                                                           |
| **3** | We specify exactly what resources to backup. We want to backup all Couchbase resources — for brevity I’ve used only what is in use. Backing up persistent volumes will create snapshots. Backing up persistent volume claims and ConfigMap resources will save all the persistent metadata required by the Operator for recovery. Backing up secrets will protect the admin username and password. Finally deployments, roles, role bindings and service accounts will allow the Operator to restart. |

You may have noticed that neither pods nor services were backed up. This is because the Operator will be able to recreate them from the cluster `ConfigMap`, metadata attached to the persistent volume claims, and the `CouchbaseCluster` resource itself. Likewise the deployment will be able to recreate the Operator pod.

Once the backup is complete it will look like the following:

```console
$ velero backup describe test
Name:         test
Namespace:    velero
Labels:       velero.io/backup=test
              velero.io/pv=pvc-837e29fa-518b-11ea-8b64-42010a8e021e
              velero.io/storage-location=default
Annotations:  <none>

Phase:  Completed (1)

Namespaces:
  Included:  test
  Excluded:  <none>

Resources:
  Included:        couchbaseclusters.couchbase.com, couchbasebuckets.couchbase.com, persistentvolumes, persistentvolumeclaims, secrets, deployments, roles.rbac.authorization.k8s.io, rolebindings.rbac.authorization.k8s.io, serviceaccounts, configmaps
  Excluded:        <none>
  Cluster-scoped:  auto

Label selector:  <none>

Storage Location:  default

Snapshot PVs:  auto

TTL:  720h0m0s

Hooks:  <none>

Backup Format Version:  1

Started:    2020-02-17 13:46:36 +0000 GMT
Completed:  2020-02-17 13:46:40 +0000 GMT

Expiration:  2020-03-18 13:46:36 +0000 GMT

Persistent Volumes:  3 of 3 snapshots completed successfully (specify --details for more information) (2)
```

| **1** | The backup has completed successfully                                        |
| ----- | ---------------------------------------------------------------------------- |
| **2** | The backup has registered and has take a snapshot of our persistent volumes. |

## [](#disaster-strikes)Disaster Strikes!

The Operator can easily handle pods and persistent volumes being deleted. What it can’t cater for is someone deleting everything, which is where [Velero](https://velero.io/) comes in. So let’s simulate total devastation to see [Velero](https://velero.io/) in action:

```console
$ kubectl delete namespace test
namespace "test" deleted
```

You can double check that the namespace and everything in it are gone before proceeding.

## [](#disaster-recovery)Disaster Recovery

This is where all the hard work correctly configuring the backup — and testing it — pays dividends. In a real-world disaster recovery situation you are probably panicking, and thinking irrationally. [Velero](https://velero.io/) makes restoration very easy, and therefore virtually fool-proof while under pressure:

```console
$ velero restore create --from-backup test
Restore request "test-20200217134839" submitted successfully.
Run `velero restore describe test-20200217134839` or `velero restore logs test-20200217134839` for more details.
```

After a few short moments you will see the namespace and resources being recreated. Eventually the Operator will restart as its deployment recognizes it has not pods running:

```console
$ kubectl -n test logs -f deployment/couchbase-operator
{"level":"info","ts":1581948125.9243767,"logger":"main","msg":"couchbase-operator","version":"2.0.0","revision":"master 948b7d6d5d6a8870c36209e982466f85cb759016"}
{"level":"info","ts":1581948125.9268959,"logger":"leader","msg":"Trying to become the leader."}
{"level":"info","ts":1581948126.068716,"logger":"leader","msg":"Not the leader. Waiting."}
{"level":"info","ts":1581948127.1986287,"logger":"leader","msg":"Not the leader. Waiting."}
```

However, as you will see, the Operator’s leader election hangs. This is because we backed the `ConfigMap` that is used to determine leadership. But this is actually a good thing.

It is worthwhile taking a moment and checking that things are as you expect before continuing. The most important resources to double check are the persistent volume claims as they contain your data and recovery metadata. They should be present and `Bound`, ready to be used.

```console
$ kubectl -n test get all
NAME                                      READY   STATUS    RESTARTS   AGE
pod/couchbase-operator-7b6588c7c6-pkdm4   1/1     Running   0          54s

NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/couchbase-operator   1/1     1            1           55s

NAME                                            DESIRED   CURRENT   READY   AGE
replicaset.apps/couchbase-operator-7b6588c7c6   1         1         1       55s

NAME                                    MEMORY QUOTA   REPLICAS   IO PRIORITY   EVICTION POLICY   CONFLICT RESOLUTION   AGE
couchbasebucket.couchbase.com/default   100Mi          1          low           valueOnly         seqno                 56s

NAME                                        VERSION   SIZE   STATUS   UUID   AGE
couchbasecluster.couchbase.com/cb-example
```

```console
$ kubectl -n test get pvc
NAME                         STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS    AGE
cb-example-0000-default-01   Bound    pvc-8a84b9ff-518d-11ea-8b64-42010a8e021e   1Gi        RWO            dynamic-bound   68s
cb-example-0001-default-01   Bound    pvc-9ea97330-518d-11ea-8b64-42010a8e021e   1Gi        RWO            dynamic-bound   68s
cb-example-0002-default-01   Bound    pvc-adb55be6-518d-11ea-8b64-42010a8e021e   1Gi        RWO            dynamic-bound   68s
```

Once satisfied things look correct, allow the Operator to start up:

```console
$ kubectl -n test delete configmap/couchbase-operator
configmap "couchbase-operator" deleted
```

After a few moments the Operator will recreate a Couchbase pod, then restore the rest of the cluster. You can now reconnect to the Couchbase web console and check that the documents you inserted earlier are fully restored.

## [](#further-reading)Further Reading

* [Velero homepage](https://velero.io/)