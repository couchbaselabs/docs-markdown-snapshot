---
title: Deployment
description: Transition from dev environment to prod, and keep up with the latest fixes.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.10/modules/project-docs/pages/deployment.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.10@java-sdk:project-docs:deployment.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.10/project-docs/deployment.html)

# Deployment

> Transition from dev environment to prod, and keep up with the latest fixes. 

One of Couchbase's strengths is speedy response, so deployment of apps should be in the same region as the Server — whether Capella, or your own self-managed cluster.

We always recommend the [latest version](sdk-release-notes.md#latest-release) of the SDK. This not only contains the latest security updates and bug fixes, but will be compatible with the latest Couchbase Server release (note, Capella always runs a recent version of Couchbase Server).

Before deploying, take note of any [compatibility](compatibility.md) issues for the language platform and underlying OS. The [full installation guide](sdk-full-installation.md) should cover any special cases for all supported environments.

## [](#development-testing-environments)Development & Testing Environments

During development, some shortcuts are taken to get up and running which would not be acceptable during deployment. These include use of administrator permissions, connecting from your laptop instead of a secure app server, and even disabling certificate verification for TLS. Testing environments may also differ from deployment.

The Java SDK docs note whenever a shortcut is being taken, but here is a non-exhaustive list of those development practices which should not be carried over to production deployments:

* Over-priveleged access
* Geographical separation of app server and database
* Skipping certificate verification

The best way to accommodate developing an application that is to be deployed to production is to use the platform's default approach for configuration files.

For the Java SDK, that is to keep a separate properties file for your development and production environments.

## [](#migration)Migration

This section also contains information on [migrating from the previous major version of the SDK API](migrating-sdk-code-to-3.n.md).

## [](#further-reading)Further Reading

* Integrate Couchbase with your data ecosystem:

  * [SDK Integrations](third-party-integrations.md)
  * [Integrations across Couchbase](../../../server/current/third-party/integrations.md)
* [Contribute to the SDK](get-involved.md)

### [](#deploying-couchbase-server)Deploying Couchbase Server

* [Capella](../../../home/cloud.md) — Database as a Service
* [Self-managed Couchbase Server](../../../server/current/install/get-started.md):

  * [Docker Install](../../../server/current/install/getting-started-docker.md)
  * [Couchbase Autonomous Operator](../../../operator/current/overview.md)

    * [Kubernetes](../../../operator/current/install-kubernetes.md)
    * [Openshift](../../../operator/current/install-openshift.md)
  * [Cloud Marketplace](#8.0server:cloud:couchbase-cloud-deployment.adoc):

    * [AWS Marketplace](../../../server/current/cloud/couchbase-aws-marketplace.md)
    * [Azure Marketplace](../../../server/current/cloud/couchbase-azure-marketplace.md)
    * [GCP Marketplace](../../../server/current/cloud/couchbase-gcp-cloud-launcher.md)