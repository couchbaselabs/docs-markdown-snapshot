---
title: Upgrade the Operator
pubDate: 2026-10-17T04:21:50.088Z
meta:
  component:
    title: Kubernetes Operator
    version: "2.9"
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.9/modules/ROOT/pages/howto-operator-upgrade.adoc
  xref: xref:operator::howto-operator-upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/current/howto-operator-upgrade.html)

# Upgrade the Operator

Upgrading the Couchbase Kubernetes Operator is a five-step process:

* [Step 1: Download the New Operator Package](#download-operator)
* [Step 2: Uninstall the Old DAC and Operator](#uninstall-operator)
* [Step 3: Update the CRDs](#update-crd)
* [Step 4: Update Existing Resources](#update-existing-resources)
* [Step 5: Install the New Operator](#install-operator)

For guidance on Operator Rollbacks:

* [Rolling Back](#rollback-operator)

> [!IMPORTANT]
> When upgrading Couchbase Operator, you must use the uninstaller from the same version of the software you used to install it, then use the newer installer to upgrade.
> 
> For example:
> 
> To upgrade the Operator from 2.2 to 2.4, use Version 2.2 to remove the older version of the software, then use the 2.4 release package to upgrade.

## [](#before-upgrading)Before Upgrading

Make sure to consult the [Release Notes](release-notes.md) and the [What's New?](whats-new.md) pages before upgrading, as there may be additional considerations or steps required on a per-release basis. Clusters with [couchbaseclusters.spec.antiAffinity](resource/couchbasecluster.md#couchbaseclusters-spec-antiaffinity) attribute enabled will require the addition of a temporary node for the upgrade — see [here](concept-sizing.md#rolling-upgrade) for further details.

> [!IMPORTANT]
> About Upgrading From Version 1.x.x
> 
> There is no direct upgrade path to this release from versions prior to 2.0.x. To upgrade from a 1.x.x release, you must first upgrade to 2.0.x, paying particular attention to supported Kubernetes platforms and Couchbase Server versions. Refer to the [2.0.x version of this page](#2.0@operator::howto-operator-upgrade.adoc) if upgrading from a 1.x.x release.

> [!WARNING]
> The Operator should not be upgraded while any Couchbase clusters are in hibernation. Instructions to wake the cluster can be found in the [hibernation](concept-hibernation.md) documentation.

## [](#download-operator)Step 1: Download the New Operator Package

Download the Operator [package](https://www.couchbase.com/downloads) for the version that you want to upgrade to, and unpack it on the same computer where you normally run `kubectl` or `oc`.

The Operator package contains the YAML configuration files and command-line tools that you will use to upgrade and manage the Operator.

> [!IMPORTANT]
> After you unpack the download, the resulting directory will be titled something like `couchbase-autonomous-operator-kubernetes_x.x.x-linux_x86_64`. Make sure to `cd` into this directory before you run the commands in this guide.

## [](#uninstall-operator)Step 2: Uninstall the Old DAC and Operator

What needs to be uninstalled is dependent on the release you are upgrading from. For example, in releases prior to 1.2.0, the Operator used `ClusterRole` resources for simplicity of configuration. From 1.2.0 onward, the operator uses `Role` resources to increase security.

In general, you'll need to undo the installation steps in reverse order for the specific version of the Operator you are upgrading from, e.g. uninstall the operator, then uninstall the DAC.

> [!WARNING]
> Never delete existing CRDs. If an existing CRD is deleted, any `CouchbaseCluster` resources will also be deleted.

To uninstall the current Operator version, instructions are provided for [Kubernetes](install-kubernetes.md#uninstalling-the-operator) and [OpenShift](install-openshift.md#uninstalling-the-operator).

## [](#update-crd)Step 3: Update the CRDs

In the Operator package you downloaded, you'll find the updated version of the CRDs: `crd.yaml`. Between releases of the Operator, the CRDs may undergo small changes that don't affect backward compatibility, and may add new fields or make changes to validation, therefore must be reinstalled. New CRDs may also be introduced that need installing.

> [!IMPORTANT]
> CRDs are distributed as a single file. During the upgrade procedure, errors are expected during the `apply` operation if a CRD was previously created using a `create` operation. Using `apply` here allows the CRD to be replaced and created all in one operation.

To update the CRDs, run the following command:

* Kubernetes
* OpenShift

```console
$ kubectl apply -f crd.yaml
```

```console
$ oc apply -f crd.yaml
```

## [](#update-existing-resources)Step 4: Update Existing Resources

Occasionally, it may be necessary to add new attributes to one or more of the CRDs that may impact your cluster if the equivalent settings have been modified from the default.

For example, if a setting was omitted in CAO, then later added, there is a chance that a cluster already has that value set directly by an administrator — if not added to the Custom Resource then the Operator will set it to its default value during reconciliation.

Please refer to the Release Notes and add any new items to your existing resources if you have already set them directly.

## [](#install-operator)Step 5: Install the New Operator

After all the previous steps, you can move on to upgrading the Operator itself. Upgrading the Operator is exactly the same as the initial installation, except that you don't re-install the CRD. To re-install the Operator in all namespaces where previous instances operated on, see the relevant documentation for [Kubernetes](install-kubernetes.md) or [OpenShift](install-openshift.md).

## [](#rollback-operator)Operator Rollbacks

While Operator releases are thoroughly tested, there may be scenarios where you need to roll back to a different version. Rolling back the Operator cannot occur while it is orchestrating Couchbase Server pods. Instead, we can use [hibernation](concept-hibernation.md) to temporarily remove Couchbase Server pods but retain their volumes and give us a window to change the Operator image. During this window, the cluster will be unavailable.

> [!IMPORTANT]
> Rollbacks are only supported between maintenance versions of the Couchbase Operator due to CRD changes between versions that break backwards compatibility. Rollbacks across major or minor versions are not supported (major.minor.maintenance). For example, 2.9.3 can be rolled back to 2.9.1, but cannot be rolled back to 2.8.2.

### [](#step-1-hibernate-the-clusters)Step 1: Hibernate the Clusters

All clusters managed by the Couchbase Operator being rolled back must be hibernated:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  hibernate: true (1)
```

| **1** | hibernate defaults to false. Change it to true to trigger the hibernation process. |
| ----- | ---------------------------------------------------------------------------------- |

> [!WARNING]
> Hibernating your cluster will delete Couchbase Server pods, making it unavailable. It's important to understand how this works before progressing.

### [](#step-2-change-the-operator-image)Step 2: Change the Operator Image

Change the Operator image to the version you want to roll back to:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: couchbase-operator
spec:
  template:
    spec:
      containers:
      - name: couchbase-operator
        image: couchbase/operator:2.9.1 (1)
```

| **1** | The image you want to roll back to. This should be the same major.minor as the previous image. |
| ----- | ---------------------------------------------------------------------------------------------- |

### [](#step-3-wake-the-clusters)Step 3: Wake the Clusters

Once the Couchbase Operator pod has been redeployed, wake the clusters we hibernated earlier by reversing the hibernation field change:

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  hibernate: false (1)
```

| **1** | End hibernation by switching this field back to false. |
| ----- | ------------------------------------------------------ |

The Operator will now recreate the pods and mount the old volumes to them. At this point the rollback has been completed.