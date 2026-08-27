---
title: Introduction
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/overview.adoc
  xref: xref:2.6@operator::overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/overview.html)

# Introduction

The Couchbase Autonomous Operator provides native integration of Couchbase Server with open source Kubernetes and Red Hat OpenShift. It enables you to automate the management of common Couchbase tasks such as the configuration, creation, scaling, and recovery of Couchbase clusters. By reducing the complexity of running a Couchbase cluster, it lets you focus on the desired configuration and not worry about the details of manual deployment and life-cycle management.

## [](#what-does-it-support)What Does it Support?

The Operator can deploy and manage:

* Couchbase Server Enterprise Edition

The Operator is certified on the following platforms:

* [Kubernetes](install-kubernetes.md)
* [Red Hat OpenShift](install-openshift.md)
* Amazon EKS
* Google GKE
* Microsoft AKS

> [!NOTE]
> For more information on supported platforms and versions see the [system requirements documentation](prerequisite-and-setup.md).

## [](#how-does-it-work)How Does it Work?

The Operator extends Kubernetes by defining types that represent Couchbase clusters and resources. These types are declarative; they define what the cluster should look like. The Operator monitors Kubernetes for Couchbase resources, creating or updating Couchbase clusters to match the declarative specification.

> [!NOTE]
> For more information on what the Operator does, its behavior and its architecture see the [Operator architecture concepts documentation](concept-operator.md).

## [](#what-features-does-it-provide)What Features Does it Provide?

The goal of the Operator is to fully manage one or more Couchbase deployments so that you don't need to worry about the operational complexities of running Couchbase. The following is a list of the management tasks that are currently supported:

* Cluster life-cycle

  * [Cluster provisioning](howto-couchbase-create.md)
  * [Cluster scaling](howto-couchbase-scale.md)
  * [Cluster upgrade](howto-couchbase-upgrade.md)
  * Cluster auto-recovery
* Cluster configuration

  * [Persistent volumes](howto-persistent-volumes.md)
  * [Server groups](howto-server-groups.md)
  * [Cross data center replication (XDCR)](howto-xdcr.md)
  * [TLS and certificate rotation](howto-tls.md)
  * User and group management
  * [Backup and restore](howto-backup.md)
  * [Prometheus monitoring](howto-prometheus.md)

## [](#essential-reading)Essential Reading

Kubernetes and the Operator are complex systems — you shouldn't go in unprepared. The following is a selection of documentation that should be read and understood fully before continuing:

* [Best practices](best-practices.md) \- understand the best way to deploy Couchbase clusters
* [System requirements](prerequisite-and-setup.md) \- understand supported platforms, software and resource requirements
* [Public cloud prerequisites](prerequisite-cloud.md) \- understand how to prepare public clouds to run the Operator
* [Custom resource label selection](concept-label-selection.md) \- understand how Couchbase cluster specifications are built
* [Network architectures](concept-couchbase-networking.md) \- understand how to correctly configure networking for the best experience

## [](#getting-started)Getting Started

Once you have read the essential guides, you are ready to install the Operator and create your first Couchbase cluster.

* [Installing the Operator on Kubernetes](install-kubernetes.md)
* [Installing the Operator on Red Hat OpenShift](install-openshift.md)
* [Deploying a Couchbase cluster](howto-couchbase-create.md)
* [Connecting to the Couchbase web console](howto-ui.md)

## [](#finding-your-way-around)Finding Your Way Around

The documentation is organized into easy to navigate sections that are targeted to specific users. The sections are defined as follows:

Getting Started

Important platform information and best practice guidelines must be read before proceeding. This section is also the home of quick-start installation guides.

Learn

High level architectural documentation and feature descriptions. This section should be read if you wish to correctly plan and size your Couchbase clusters before deployment.

Manage

Simple how-to guides. This section documents how to configure your Couchbase cluster resources with simple copy and paste style tutorials.

Reference

Detailed resource and component guides. This section details low-level functionality of all the resources and fields exposed to the user, their formats and constraints. Individual Operator containers and tools are fully documented with detailed command line argument manuals.

Tutorials

How to integrate with and configure 3rd party components. The Operator itself can provision and manage simple clusters for most use cases. In more complex situations that involve complex networking or interaction with other, external services, we need to provide guidance on how to integrate. These tutorial are provided as-is and may become inaccurate as 3rd party dependencies evolve.

### [](#conventions)Conventions

Resource Names

Kubernetes resources names, such as `Service` or `CouchbaseCluster`, will be rendered verbatim. These are distinguished by the use of bumpy-capitals, or camel-case, with an upper case first character. These are the names of resources when specified as `kind` in a resource's YAML definition.

Attribute Paths

Resources contain attributes, such as `spec.security.authSecret` will be rendered verbatim. These are distinguished by the use of bumpy-capitals, or camel-case, with a lower case first character. Paths are based on the JSON path specification, and consecutive elements are separated by periods (`.`).

Where attribute paths are used in the documentation, they have been prefixed with the resource name, and can be used directly with `kubectl explain` to [access online documentation](reference-resources.md).

## [](#further-reading)Further Reading

* [What's New?](whats-new.md)
* [Release Notes](release-notes.md)