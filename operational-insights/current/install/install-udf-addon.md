---
title: Install the Python UDF Add-on
description: The Python UDF add-on is an optional package that lets Operational
  Insights run Python user-defined functions. Install it on every node,
  alongside Operational Insights.
pubDate: 2026-10-23T04:31:18.652Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/install-udf-addon.adoc
  xref: xref:enterprise-analytics:install:install-udf-addon.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/install-udf-addon.html)

# Install the Python UDF Add-on

> The Python UDF add-on is an optional package that lets Operational Insights run Python user-defined functions. Install it on every node, alongside Operational Insights. 

[Python user-defined functions (UDFs)](../sqlpp/9b%5Fpython%5Fudf.md) run in a sandbox that Operational Insights does not install by default. The `operational-insights-udf` add-on package provides it: the gVisor `runsc` container runtime, and a service that runs the `couchbase/operational-insights-udf` container image.

Install the add-on on every node in the cluster. The add-on is available as `.deb` and `.rpm` packages, for nodes that you install from packages.

> [!IMPORTANT]
> The add-on does not apply to nodes that run in Docker containers. Do not install it inside an Operational Insights container, or on the host that runs one. On the host, `apt-get` and `yum` satisfy the add-on's dependency by installing Operational Insights on the host as well, and the add-on restarts the host's Docker daemon, which stops the containers that run on it.

## [](#before-you-install)Before You Install

Make sure that each node meets the following requirements:

* Operational Insights is installed, at the same version as the add-on. For example, the 3.0.0 add-on requires Operational Insights 3.0.0\. The package declares this dependency, so a package manager refuses to install a mismatched add-on. To install Operational Insights, see [Install on Red Hat Enterprise](red-hat-installation.md) or [Install on Ubuntu and Debian](ubuntu-debian-install.md).
* Docker Engine is installed, running, and managed by systemd. The package does not declare Docker as a dependency, and does not install it. Instead, the installation checks for a running Docker daemon, and fails if it does not find one. To install Docker, see [Install Docker Engine](https://docs.docker.com/engine/install/).
* The node can pull container images from Docker Hub. The installation pulls the `couchbase/operational-insights-udf` image that matches the add-on's version. To pull the image from a different registry, see [Pull the Image from a Private Registry](#private-registry).

> [!WARNING]
> The add-on takes over the Docker configuration of the host it's installed on. It does the following:
> 
> * Replaces `/etc/docker/daemon.json`, to register the `runsc` runtime. Any settings that you had in this file are lost.
> * Adds the systemd drop-in `/etc/systemd/system/docker.service.d/udf-cache-and-socket.conf`.
> * Installs `runsc` and `containerd-shim-runsc-v1` in `/usr/local/bin`.
> * Enables the `docker` service, and restarts it. Restarting Docker stops any other containers that run on the host.
> 
> Install the add-on only on hosts that are dedicated to Operational Insights.

## [](#install-the-add-on)Install the Add-on

You must log in as root (superuser) or use `sudo` to run the installation commands.

You can install the add-on from the Couchbase package repository, or from a package file.

### [](#install-from-repository)Install from the Package Repository

If you installed Operational Insights from the Couchbase package repository, install the add-on the same way:

* Red Hat
* Ubuntu and Debian

```console
sudo yum install operational-insights-udf
```

```console
sudo apt-get install operational-insights-udf
```

The package manager selects the add-on version that matches the installed Operational Insights package.

### [](#install-from-file)Install from a Package File

1. Download the add-on package for your platform from the Couchbase [downloads page](https://www.couchbase.com/downloads). Choose the same version and package format as the Operational Insights package installed on the node.
2. Install the add-on:

  * Red Hat
  * Ubuntu and Debian  
```console  
sudo yum install ./operational-insights-udf-version-linux.arch.rpm  
```  
```console  
sudo apt-get install ./operational-insights-udf_[.var]version-linux_[.var]arch.deb  
```

To install Operational Insights and the add-on on a new node in a single step, pass both package files to the same command. The package manager installs Operational Insights first.

### [](#private-registry)Pull the Image from a Private Registry

If the node cannot reach Docker Hub, copy the `couchbase/operational-insights-udf` image into a registry that the node can reach. Then set the `UDF_EXECUTOR_IMAGE` environment variable to the full image reference when you install the add-on:

* Red Hat
* Ubuntu and Debian

```console
sudo UDF_EXECUTOR_IMAGE=registry/couchbase/operational-insights-udf:[.var]tag \
  yum install operational-insights-udf
```

```console
sudo UDF_EXECUTOR_IMAGE=registry/couchbase/operational-insights-udf:[.var]tag \
  apt-get install operational-insights-udf
```

The node records the image reference, and uses it whenever it starts the sandbox.

Set `UDF_EXECUTOR_IMAGE` again whenever you upgrade the add-on. An upgrade does not reuse the recorded reference: without the variable, it pulls the image from Docker Hub.

## [](#verify)Verify the Installation

The add-on starts the sandbox container, named `udf-executor`, as soon as Operational Insights has started on the node. You can install the add-on before or after you initialize the node, and you do not need to restart Operational Insights.

To confirm that the sandbox is running, run the following command:

```console
sudo docker ps --filter name=udf-executor
```

If the command lists no container, check the status of the service that starts it:

```console
sudo systemctl status operational-insights-udf-appdir.service
```

After you install the add-on on every node, you can create Python UDFs. See [Python User-Defined Functions](../sqlpp/9b%5Fpython%5Fudf.md).

## [](#upgrade)Upgrade the Add-on

The add-on's version must always match the version of Operational Insights on the node. When you upgrade Operational Insights on a node that has the add-on, upgrade both packages in the same command. Otherwise, the package manager refuses to upgrade Operational Insights, because the installed add-on depends on the earlier version.

* Red Hat
* Ubuntu and Debian

```console
sudo yum upgrade operational-insights operational-insights-udf
```

```console
sudo apt-get install operational-insights operational-insights-udf
```

To upgrade from package files, pass both files to the same command.

If you pull the image from a private registry, set `UDF_EXECUTOR_IMAGE` for the upgrade too, as described in [Pull the Image from a Private Registry](#private-registry).

If you _hold_ the Operational Insights package, to prevent unplanned upgrades, hold the add-on package too:

* Red Hat
* Ubuntu and Debian

Add both package names to the `exclude` line of `/etc/dnf/dnf.conf` (or `/etc/yum.conf`):

```console
exclude=operational-insights operational-insights-udf
```

```console
sudo apt-mark hold operational-insights operational-insights-udf
```

Enterprise Analytics has no UDF add-on. When you upgrade a cluster from Enterprise Analytics, install the add-on on each node after you install Operational Insights 3.0 on it. Python UDFs are not available until every node in the cluster runs Operational Insights. See [Feature Availability During Upgrade](upgrade-feature-availability.md).

## [](#uninstall)Uninstall the Add-on

To remove the add-on and keep Operational Insights, run the following command:

* Red Hat
* Ubuntu and Debian

```console
sudo rpm -e operational-insights-udf
```

```console
sudo dpkg -r operational-insights-udf
```

Removing the add-on stops and removes the `udf-executor` container and its image. It also deletes the files that it installed, including `/etc/docker/daemon.json` and the Docker drop-in. Docker itself remains installed.

After you remove the add-on from a node, that node can no longer run Python UDFs.

To remove Operational Insights as well, see [Uninstall](uninstall.md).

## [](#see-also)See Also

* [Python User-Defined Functions](../sqlpp/9b%5Fpython%5Fudf.md)
* [Security Considerations](security-considerations.md)
* [Uninstall](uninstall.md)