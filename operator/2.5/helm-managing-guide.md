---
title: Helm Management Guide
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.5/modules/ROOT/pages/helm-managing-guide.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.5@operator::helm-managing-guide.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/helm-managing-guide.html)

# Helm Management Guide

> When you install a Helm chart, Helm creates a release. You can manage the release by updating, upgrading, or uninstalling it. 

When you install a Helm chart, the Helm client creates an instance of the chart in your Kubernetes cluster. This instance is called a _release_, and Helm uses it to manage all of the objects and resources that the chart creates. When you deploy the Autonomous Operator or another component via the Couchbase Helm Chart, you will manage the deployed resources by making updates to the release in Helm.

The sections on this page describe how to manage the Helm releases that make up your deployments.

## [](#modify-deployment)Modify a Deployment

During the lifecycle of your deployment, it’s likely that you will want to make changes to your deployment’s configuration (e.g. add/remove nodes from a cluster, etc). To make configuration updates to a deployment, you’ll need to modify the release in Helm.

To modify a release, you’ll specify overrides via the [\--values or --set options](helm-setup-guide.md#custom-installation) much like you did when you installed the Couchbase Helm Chart to begin with. However, when modifying a release, you use the `helm upgrade` command instead of `helm install`. For example:

```console
helm upgrade --values myvalues.yaml <release-name> couchbase/couchbase-operator
```

It’s important that you make your updates using the `helm upgrade` command instead of using `kubectl` or simply editing chart resources. This is to ensure that Helm can continue to update and manage all resources appropriately.

## [](#upgrade-a-deployment)Upgrade a Deployment

### [](#upgrading-the-autonomous-operator)Upgrading the Autonomous Operator

Upgrading the Autonomous Operator and Admission Controller to a newer version requires that you upgrade the _release_ to a newer version of its _chart_. This allows Helm to ensure that all dependencies specified by the chart get updated appropriately.

> [!IMPORTANT]
> An upgrade also requires the CRDs to be updated, this is something that Helm is [unable to do](https://github.com/helm/community/blob/f9e06c16d89ccea1bea77c01a6a96ae3b309f823/architecture/crds.md#upgrading-crds). The CRDs must be replaced (not deleted as this will remove any existing clusters) with the version for the release you want to upgrade to. Refer to the [Operator upgrade documentation](howto-operator-upgrade.md#update-crd) for detailed information on this stage.

To replace the CRDs:

To replace the CRDs pull the current helm chart:

```console
helm pull couchbase/couchbase-operator
tar -xf couchbase-operator-<version>.tgz
```

Then update the CRDs with the latest version:

```console
kubectl apply -f  couchbase-operator/crds/couchbase.crds.yaml
```

The point is to ensure any new CRDs are added and the old ones are updated. Once the CRD upgrade is complete, then upgrade the chart version:

```console
helm upgrade --version <chart-version> <release-name> couchbase/couchbase-operator
```

Where `<chart-version>` is the version of the Couchbase Helm Chart that you want to upgrade to, and `<release-name>` is the name of the release that is managing the instance of the Autonomous Operator that you wish to upgrade.

> [!WARNING]
> Chart versions 2.2 and below are at risk of encountering an issue when upgrading to chart version 2.3 due to [Cluster name limitations](https://issues.couchbase.com/browse/MB-34280). In general if your Couchbase Server version is 6.6.3 and below, and you plan to upgrade to a higher version then your cluster will be at risk of this issue.

To determine if your cluster is potentially at risk of [Cluster name limitations](https://issues.couchbase.com/browse/MB-34280), you will need to deduce what sort of stream name Couchbase Server will derive from your Couchbase Pods. The stream name is what Couchbase Server uses internally to replicate data between nodes. Since the stream name consists of the Couchbase Custer name as both the hostname and domain in both source and target endpoints, a good general rule is the multiply your cluster name by `6` to account for additional bucket name and various other bits:

```console
name=<cluster_name>
echo $(( `echo $cluster | wc -c`  * 6 ))
```

**If this value exceeds `200` you should proceed with caution.**If upgrade fails you will need to rebuild your cluster.

#### [](#limitations)Limitations

* It is not possible to upgrade the 1.2.x Autonomous Operator chart to 2.x.x. If you have a previous installation of the Autonomous Operator chart, you will need to [delete the release](#delete-deployment), as well as delete the CRD.
* If you didn’t originally install the Autonomous Operator using Helm, then you cannot upgrade the Autonomous Operator using Helm. At this time, installations of the Autonomous Operator that weren’t created with Helm cannot be ported over to using Helm.

### [](#upgrading-a-couchbase-cluster)Upgrading a Couchbase Cluster

There are two methods for upgrading a Couchbase cluster with Helm. The first method is to upgrade the release to a newer version of the Couchbase Helm Chart that uses the desired Couchbase Server version as a default. The second method is to update the existing release to use a newer Couchbase Server image. The first method is preferred, since upgrading the entire chart will ensure that any potential new parameters required to configure the cluster are defined.

> [!IMPORTANT]
> When upgrading a Couchbase cluster, you should first upgrade the Autonomous Operator to the latest compatible version so as to ensure that the cluster can be properly managed.

To upgrade a Couchbase cluster by using a newer chart

1. Check the default Couchbase Server version of a chart to make sure that it uses the version that you want to upgrade your cluster to.  
```console  
helm inspect  --version <chart-version> values couchbase/couchbase-operator | grep  "couchbase/server"  
```  
Where `<chart-version>` is the version number of a newer chart.
2. Upgrade to the newer chart.  
```console  
helm upgrade --version <chart-version> <release-name> couchbase/couchbase-operator  
```  
Where `<chart-version>` is the version of the Couchbase Helm Chart that you want to upgrade to, and `<release-name>` is the name of the release that is managing the Couchbase cluster that you wish to upgrade.

To upgrade a Couchbase cluster without upgrading the chart

```console
helm upgrade --set cluster.image=<image> <release-name> couchbase/couchbase-operator
```

Where `<image>` is the name of the container image. For example, to upgrade a cluster to Couchbase Server 7.2.0:

```console
helm upgrade --set cluster.image=couchbase/server:7.2.0 <release-name> couchbase/couchbase-operator
```

## [](#delete-deployment)Delete a Deployment

To delete a Helm deployment, run `helm uninstall` on each of the releases that make up the deployment:

```console
helm delete <release-name>
```

## [](#rotate-webhook-certificates)Rotate Webhook Certificates

By default, the certificate created for use with the validating webhook is valid for 365 days. If the certificate is allowed to expire, the Operator will be unable to perform any tasks, and manual intervention is required.

To resolve this issue, both the validating webhook and the secret containing the certificate must be replaced.

1. Delete the existing resources.  
```console  
kubectl delete validatingwebhookconfigurations.admissionregistration.k8s.io <deployment-name>-couchbase-admission-controller  
kubectl delete mutatingwebhookconfigurations.admissionregistration.k8s.io <deployment-name>-couchbase-admission-controller # only required pre 2.3.0  
kubectl delete secrets <deployment-name>-couchbase-admission-controller  
```
2. Create new resources.  
```console  
helm upgrade <deployment-name> couchbase/couchbase-operator -f <override-values.yaml> --version <version>  
```  
> [!IMPORTANT]  
> To prevent accidental upgrades, it is important to use the the chart version and overriding values corresponding to the current deployment.