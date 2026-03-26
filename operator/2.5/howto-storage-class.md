---
title: Create a Lazy Bound Storage Class
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.5/modules/ROOT/pages/howto-storage-class.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.5@operator::howto-storage-class.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/howto-storage-class.html)

# Create a Lazy Bound Storage Class

> The Operator requires a lazily bound storage class to function correctly. This guide describes how to configure one. 

## [](#listing-storage-classes-on-your-platform)Listing Storage Classes On Your Platform

The first step we need to take is to list any preexisting storage classes available on the platform:

```console
$ kubectl get sc
NAME                 PROVISIONER            AGE
standard (default)   kubernetes.io/gce-pd   47d
```

In the above example the platform is Google GKE, it already has a storage provider configured. If no storage providers are configured on your system then please consult the vendor for instructions related to creating one.

Next examine the storage class to determine whether it already makes use of lazy binding:

```console
$ kubectl get sc standard -o yaml
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
  creationTimestamp: "2019-10-17T10:58:24Z"
  labels:
    addonmanager.kubernetes.io/mode: EnsureExists
    kubernetes.io/cluster-service: "true"
  name: standard
  resourceVersion: "298"
  selfLink: /apis/storage.k8s.io/v1/storageclasses/standard
  uid: 0a615775-f0cd-11e9-bc41-42010a8e00c9
parameters:
  type: pd-standard
provisioner: kubernetes.io/gce-pd
reclaimPolicy: Delete
volumeBindingMode: Immediate
```

The important field is `volumeBindingMode`. If set to `Immediate` a persistent volume is created for a persistent volume claim immediately upon creation. The Operator will have no control over where it is scheduled.

If, however, it is set to `WaitForFirstConsumer` then the a persistent volume isn't created when a persistent volume claim is created. It waits until the persistent volume claim is attached to a pod and inherits its scheduling information. This storage class can be used directly by the Operator.

## [](#creating-a-lazily-bound-storage-class)Creating a Lazily-Bound Storage Class

The exact configuration varies between Kubernetes vendors, however the process is the same. Using the standard storage class as a template we can create our own:

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard-lazy-bound
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-standard
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```

Save to a file then submit to Kubernetes:

```console
$ kubectl apply -f my-storage-class.yaml
storageclass.storage.k8s.io/standard-lazy-bound created
```