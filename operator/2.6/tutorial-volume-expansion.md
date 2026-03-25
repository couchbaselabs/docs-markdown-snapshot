---
title: Online Persistent Volume Expansion
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/tutorial-volume-expansion.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.6@operator::tutorial-volume-expansion.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/tutorial-volume-expansion.html)

# Online Persistent Volume Expansion

> Learn how to use the Autonomous Operator to perform online persistent volume expansion for Couchbase Server deployments in Kubernetes. 

> [!WARNING]
> Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer.

## [](#introduction)Introduction

In this tutorial you’ll learn how to use the Autonomous Operator to expand persistent volumes that are already in use by Couchbase clusters without needing to perform an upgrade on the underlying storage subsystem. The Autonomous Operator performs storage upgrades by working in conjunction with [Kubernetes Persistent Volume Expansion](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims) to claim additional storage for running pods without any downtime.

## [](#before-you-begin)Before You Begin

This tutorial uses the context of Azure Kubernetes Service (AKS), but the steps generally apply to any Kubernetes environment.

Before you begin, you’ll need to set up a few things first:

* You’ll need a Kubernetes cluster with at least 3 available worker nodes that have at least 20GiB of storage capacity.

  * If you need to set up a cluster on AKS, refer to [Quickstart: Deploy an AKS cluster using the Azure portal](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough-portal).
* Your environment needs to have a `StorageClass` capable of performing volume expansions. Refer to [Online Volume Expansion](howto-persistent-volumes.md#online-volume-expansion) for more information about supported storage classes.

  * This tutorial references the `azurefile` storage class which is provided by the Azure Kubernetes Service (AKS). You’ll need to use the name of your particular storage class if installing in a non-AKS Kubernetes environment.
* You’ll need [Helm version 3.1](https://helm.sh/docs/intro/install/) or higher for installing the necessary dependencies (e.g. the Autonomous Operator, the Couchbase cluster, etc.)

  * Once you have Helm installed, you’ll need to add the Couchbase chart repository:  
  ```console  
  $ helm repo add couchbase https://couchbase-partners.github.io/helm-charts/  
  ```  
  Then make sure to update the repository index:  
  ```console  
  $ helm repo update  
  ```
  * If needed, the following guide can be helpful to familiarize yourself with Helm on AKS: [Install existing applications with Helm in AKS](https://docs.microsoft.com/en-us/azure/aks/kubernetes-helm).

## [](#create-the-couchbase-cluster-deployment)Create the Couchbase Cluster Deployment

Let’s start by setting up our Couchbase deployment. To speed up the process, we’ll be using the Couchbase Helm chart to conveniently install a Couchbase cluster with persistent volumes.

Run the following command to create a file with the necessary override values for the Couchbase chart:

```console
$ cat << EOF > pvc_resize_values.yaml
---
cluster:
  cluster:
    dataServiceMemoryQuota: 4Gi
    indexServiceMemoryQuota: 6Gi
  name:
  enableOnlineVolumeExpansion: true (1)
  servers:
    default:
      size: 2
      services:
        - data
      volumeMounts:
        default: default
        data: data-expanding  (2)
    search:
      size: 1
      services:
        - query
        - index
  volumeClaimTemplates: (3)
  - metadata:
      name: data-expanding
    spec:
      storageClassName: azurefile
      resources:
        requests:
          storage: 5Gi
  - metadata:
      name: default
    spec:
      storageClassName: default
      resources:
        requests:
          storage: 2Gi
EOF
```

| **1** | [couchbaseclusters.spec.enableOnlineVolumeExpansion](resource/couchbasecluster.md#couchbaseclusters-spec-enableonlinevolumeexpansion): Setting this field to true enables online expansion of persistent volumes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | [couchbaseclusters.spec.servers.volumeMounts](resource/couchbasecluster.md#couchbaseclusters-spec-servers-volumemounts): With this configuration we’re telling the Autonomous Operator to provision persistent volume claims for the data mount path according to the data-expanding claim template.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **3** | [couchbaseclusters.spec.volumeClaimTemplates](resource/couchbasecluster.md#couchbaseclusters-spec-volumeclaimtemplates): This configuration defines the data-expanding claim template. volumeClaimTemplates.spec.storageClassName: This field refers to the name of the storage class that services volume claims. The storage class **must** support volume expansion in order to add additional storage in-place. Here we’re using the [azurefile](https://docs.microsoft.com/en-us/azure/aks/concepts-storage#storage-classes) storage class. volumeClaimTemplates.spec.resources: This field defines the size of the volume that will be allocated. Here we’re requesting 5Gi volumes. Volume expansion is triggered when this value is increased. |

Now, install the Couchbase chart, making sure to specify the values override file we just created:

```console
$ helm install -f pvc_resize_values.yaml expand couchbase/couchbase-operator
```

> [!NOTE]
> The Couchbase chart deploys the Autonomous Operator by default. If you already have the Autonomous Operator deployed in the current namespace, then you’ll need to specify additional overrides during chart installation so that only the Couchbase cluster is deployed:
> 
> ```console
> $ helm install -f pvc_resize_values.yaml --set install.couchbaseOperator=false,install.admissionController=false expand couchbase/couchbase-operator
> ```

### [](#verify-the-installation)Verify the Installation

The configuration we’re using calls for a three-node Couchbase cluster (two `data` nodes and one `search` node), which will take a few minutes to be created. You can run the following command to verify the deployment status:

```console
$ kubectl describe couchbasecluster expand-couchbase-cluster
```

In the console output, you should check for the events that signal the creation of the three nodes in the Couchbase cluster:

Events:
  Type    Reason                  Age   From  Message
  ----    ------                  ----  ----  -------
  Normal  EventNewMemberAdded     22m         New member scale-couchbase-cluster-0002 added to cluster

## [](#expand-the-persistent-volume)Expand the Persistent Volume

Now let’s modify the [CouchbaseCluster](resource/couchbasecluster.md) resource in order to initiate volume expansion.

```console
$ kubectl edit couchbasecluster scale-couchbase-cluster
```

In the editor, modify the [couchbaseclusters.spec.volumeClaimTemplates](resource/couchbasecluster.md#couchbaseclusters-spec-volumeclaimtemplates) section as follows:

and change the requested storage of the `data-expanding` template from `5Gi` to `10Gi`.

```yaml
  volumeClaimTemplates:
  - metadata:
      name: data-expanding
    spec:
      resources:
        requests:
          storage: 10Gi (1)
```

| **1** | Here we’re changing the requested storage of the data-expanding template from 5Gi to 10Gi. This will trigger the expansion of _all_ the Couchbase services that reference data-expanding template. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Save the configuration changes to initiate the volume expansion task.

### [](#verify-volume-expansion)Verify Volume Expansion

Run the following command to verify the status of the volume expansion task by checking events on the `CouchbaseCluster` resource:

```console
$ kubectl describe couchbasecluster expand-couchbase-cluster
```

If the volume expansion was successful, you should expect output similar to the following:

Normal  ExpandVolumeStarted    46s          Expanding Volume scale-couchbase-cluster-0003-data-01 from 5Gi to 10Gi **(1)**
Normal  ExpandVolumeSucceeded  41s          Successfully expanded volume scale-couchbase-cluster-0002-default-01
Normal  ExpandVolumeStarted    18s          Expanding Volume scale-couchbase-cluster-0004-data-01 from 5Gi to 10Gi **(1)**
Normal  ExpandVolumeSucceeded  6s           Successfully expanded volume scale-couchbase-cluster-0002-default-01

| **1** | The persistent volume on each of the Couchbase data pods has been expanded in place. |
| ----- | ------------------------------------------------------------------------------------ |

## [](#cleaning-up)Cleaning up

Running the commands in this section will uninstall all of the resources that were created during the course of this tutorial.

Uninstall both the Autonomous Operator and Couchbase cluster by deleting the Helm release:

```console
$ helm delete scale
```

## [](#further-reading)Further Reading

* Concepts: [Couchbase Persistent Volumes](concept-persistent-volumes.md)