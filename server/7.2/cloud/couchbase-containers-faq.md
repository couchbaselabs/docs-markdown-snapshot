---
title: Frequently Asked Questions about Couchbase Containers
description: Frequently asked questions about Couchbase Containers
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cloud/pages/couchbase-containers-faq.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:cloud:couchbase-containers-faq.adoc[]
---

[View original HTML](/server/7.2/cloud/couchbase-containers-faq.html)

# Frequently Asked Questions about Couchbase Containers

> Frequently asked questions about Couchbase Containers 

## [](#do-we-support-modifying-the-official-couchbase-container)Do we support modifying the official Couchbase container?

No. The official Couchbase container images on DockerHub and Red Hat Registry are actual binaries which get built with our [Dockerfile](https://github.com/docker-library/docs/tree/master/couchbase), which consists of commands to assemble the image and some best practices.

The Couchbase containers are published with the `automated build` flag turned on and will automatically be rebuilt and updated when new vulnerabilities are detected or when new versions of the base OS image is available.

## [](#do-we-support-custom-containers-that-is-containers-not-based-on-the-official-couchbase-container)Do we support custom containers, that is, containers not based on the official Couchbase container?

Yes, we support modifying the Dockerfile to build a customized Couchbase container image.

Customizing Couchbase container images by updating and rebuilding the Dockerfile with your environment-specific settings or best practice guidelines, and not changing or altering the Couchbase binaries is supported.

## [](#can-we-provide-alternative-containers-with-different-base-operating-systems)Can we provide alternative containers with different base operating systems?

We currently support the following base operating systems: \* Ubuntu for DockerHub \* RHEL for Red Hat Registry

## [](#are-there-any-restrictions-on-using-a-container-we-make-for-openshiftrhcc-in-a-non-openshift-environment)Are there any restrictions on using a container we make for OpenShift/RHCC in a non-OpenShift environment?

The official Couchbase image for Red Hat Catalog is built with Red Hat Enterprise Linux (RHEL) as the base OS. There are no restrictions on the usage of the image itself.

## [](#do-we-support-kubernetes-deployments-that-do-not-use-couchbase-autonomous-operator)Do we support Kubernetes deployments that do not use Couchbase Autonomous Operator?

If you are considering deploying and running Couchbase Server on the Kubernetes platform, we highly recommend using Couchbase Autonomous Operator. However, if you choose to deploy Couchbase Server on the Kubernetes platform on your own, note that Couchbase will only support Couchbase Server product issues and the container images.