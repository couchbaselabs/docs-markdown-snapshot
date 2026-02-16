[View original HTML](/operator/2.7/howto-operator-upgrade.html)

Upgrading the Couchbase Autonomous Operator is a five-step process:

* [Step 1: Download the New Operator Package](#download-operator)
* [Step 2: Uninstall the Old DAC and Operator](#uninstall-operator)
* [Step 3: Update the CRDs](#update-crd)
* [Step 4: Update Existing Resources](#update-existing-resources)
* [Step 5: Install the New Operator](#install-operator)

|  | When upgrading Couchbase Operator, you must use the uninstaller from the same version of the software you used to install it, then use the newer installer to upgrade. For example: To upgrade the Operator from 2.2 to 2.4, use Version 2.2 to remove the older version of the software, then use the 2.4 release package to upgrade. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#before-upgrading)Before Upgrading

Make sure to consult the [Release Notes](release-notes.md) and the [What’s New?](whats-new.md) pages before upgrading, as there may be additional considerations or steps required on a per-release basis. Clusters with [couchbaseclusters.spec.antiAffinity](resource/couchbasecluster.md#couchbaseclusters-spec-antiaffinity) attribute enabled will require the addition of a temporary node for the upgrade — see [here](concept-sizing.md#rolling-upgrade) for further details.

|  | About Upgrading From Version 1.x.x There is no direct upgrade path to this release from versions prior to 2.0.x. To upgrade from a 1.x.x release, you must first upgrade to 2.0.x, paying particular attention to supported Kubernetes platforms and Couchbase Server versions. Refer to the [2.0.x version of this page](#2.0@operator::howto-operator-upgrade.adoc) if upgrading from a 1.x.x release. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#download-operator)Step 1: Download the New Operator Package

Download the Operator [package](https://www.couchbase.com/downloads) for the version that you want to upgrade to, and unpack it on the same computer where you normally run `kubectl` or `oc`.

The Operator package contains the YAML configuration files and command-line tools that you will use to upgrade and manage the Operator.

|  | After you unpack the download, the resulting directory will be titled something like couchbase-autonomous-operator-kubernetes\_x.x.x-linux\_x86\_64. Make sure to cd into this directory before you run the commands in this guide. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#uninstall-operator)Step 2: Uninstall the Old DAC and Operator

What needs to be uninstalled is dependent on the release you are upgrading from. For example, in releases prior to 1.2.0, the Operator used `ClusterRole` resources for simplicity of configuration. From 1.2.0 onward, the operator uses `Role` resources to increase security.

In general, you’ll need to undo the installation steps in reverse order for the specific version of the Operator you are upgrading from, e.g. uninstall the operator, then uninstall the DAC.

|  | Never delete existing CRDs. If an existing CRD is deleted, any CouchbaseCluster resources will also be deleted. |
|  | --------------------------------------------------------------------------------------------------------------- |

To uninstall the current Operator version, instructions are provided for [Kubernetes](install-kubernetes.md#uninstalling-the-operator) and [OpenShift](install-openshift.md#uninstalling-the-operator).

## [](#update-crd)Step 3: Update the CRDs

In the Operator package you downloaded, you’ll find the updated version of the CRDs: `crd.yaml`. Between releases of the Operator, the CRDs may undergo small changes that don’t affect backward compatibility, and may add new fields or make changes to validation, therefore must be reinstalled. New CRDs may also be introduced that need installing.

|  | CRDs are distributed as a single file. During the upgrade procedure, errors are expected during the apply operation if a CRD was previously created using a create operation. Using apply here allows the CRD to be replaced and created all in one operation. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

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

After all the previous steps, you can move on to upgrading the Operator itself. Upgrading the Operator is exactly the same as the initial installation, except that you don’t re-install the CRD. To re-install the Operator in all namespaces where previous instances operated on, see the relevant documentation for [Kubernetes](install-kubernetes.md) or [OpenShift](install-openshift.md).