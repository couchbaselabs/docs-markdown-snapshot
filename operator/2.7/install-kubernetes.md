---
title: Install the Operator on Kubernetes
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.7/modules/ROOT/pages/install-kubernetes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.7@operator::install-kubernetes.adoc[]
---

[View original HTML](/operator/2.7/install-kubernetes.html)

# Install the Operator on Kubernetes

> This guide walks through the recommended procedure for installing the Couchbase Autonomous Operator on an open source Kubernetes cluster that has _RBAC enabled_. 

> [!IMPORTANT]
> If you are looking to upgrade an existing installation of the Operator, see [Upgrading the Autonomous Operator](howto-operator-upgrade.md).

## [](#helm-installation)Helm Installation

The Operator is able to be installed via Helm, see [Helm Deployment](helm-setup-guide.md) for setup instructions.

The guide below is for installing the Operator package _directly_.

## [](#prerequisites)Prerequisites

Download the Operator [package](https://www.couchbase.com/downloads) and unpack it on the same computer where you normally run `kubectl`. The Operator package contains YAML configuration files and command-line tools that you will use to install the Operator.

> [!IMPORTANT]
> After you unpack the download, the resulting directory will be titled something like `couchbase-autonomous-operator-kubernetes_x.x.x-linux_x86_64`. Make sure to `cd` into this directory before you run the commands in this guide.

All commands in this guide are run as a system administrator account; they require the creation of cluster scoped resources or the granting of roles to service accounts (privilege escalation).

## [](#install-the-crd)Install the CRD

The first step in installing the Operator is to install the custom resource definitions (CRD) that describe the Couchbase resource types. This can be achieved with the following command:

```console
$ kubectl apply -f crd.yaml
```

## [](#install-the-operator)Install the Operator

The operator is composed of two components; a per-cluster dynamic admission controller (DAC) and a per-namespace Operator. Refer to the [operator architecture document](concept-operator.md) for additional information on what is required and security considerations.

The following command will install both the DAC and the Operator into the `default` namespace.

```console
$ bin/cao create admission
$ bin/cao create operator
```

### [](#custom-installation)Custom Installation

Alternatively, you may wish to install just the DAC in the `camelot` namespace:

```console
$ bin/cao create admission --namespace camelot
```

And then install just the Operator into the `asgard` namespace:

```console
$ bin/cao create operator --namespace asgard
```

For further installation options please see the [cao](tools/cao.md) reference manual.

## [](#check-the-status-of-the-operator)Check the Status of the Operator

You can use the following command to check on the status of the deployments:

```console
$ kubectl get deployments
NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
couchbase-operator             1/1     1            1           8s
couchbase-operator-admission   1/1     1            1           8s
```

The Operator is ready to deploy `CouchbaseCluster` resources when both the DAC and Operator deployments are fully ready and available.

## [](#uninstalling-the-operator)Uninstalling the Operator

Uninstalling the DAC and Operator is the reverse of the installation process:

> [!IMPORTANT]
> If you are performing an uninstall in order to upgrade the Operator to a newer version, do not delete the CRDs as this is only relevant for a full uninstall. Failure to do so will result in the deletion of all Couchbase clusters.

```console
$ bin/cao delete operator
$ bin/cao delete admission
$ kubectl delete -f crd.yaml
```

## [](#next-steps)Next Steps

* [How-to Deploy a Couchbase Cluster, a basic configuration](howto-couchbase-create.md)
* [CouchbaseCluster Reference Architecture, an advanced production configuration](reference-reference-architecture.md)