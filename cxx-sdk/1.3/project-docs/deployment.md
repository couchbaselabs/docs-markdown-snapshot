---
title: Deployment
description: Transition from dev environment to prod, and keep up with the latest fixes.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.3/modules/project-docs/pages/deployment.adoc
  xref: xref:1.3@cxx-sdk:project-docs:deployment.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/1.3/project-docs/deployment.html)

# Deployment

> Transition from dev environment to prod, and keep up with the latest fixes. 

One of Couchbase's strengths is speedy response, so deployment of apps should be in the same region as the Server — whether Capella, or your own self-managed cluster.

We always recommend the [latest version](sdk-release-notes.md#latest-release) of the SDK. This not only contains the latest security updates and bug fixes, but will be compatible with the latest Couchbase Server release (note, Capella always runs a recent version of Couchbase Server).

Before deploying, take note of any [compatibility](compatibility.md) issues for the language platform and underlying OS. The [full installation guide](sdk-full-installation.md) should cover any special cases for all supported environments.

> [!TIP]
> No Load Balancer Required
> 
> Your Couchbase cluster will take care of balancing the load and distribution of data between nodes, in tandem with the SDK's use of the cluster map. A load balancer would negatively affect this work — so the use of a load balancer between your app server, where you're running the SDK and client code, and your Couchbase operational cluster, is strongly discouraged.

## [](#development-testing-environments)Development & Testing Environments

During development, some shortcuts are taken to get up and running which would not be acceptable during deployment. These include use of administrator permissions, connecting from your laptop instead of a secure app server, and even disabling certificate verification for TLS. Testing environments may also differ from deployment.

The C++ SDK docs note whenever a shortcut is being taken, but here is a non-exhaustive list of those development practices which should not be carried over to production deployments:

* Over-priveleged access
* Geographical separation of app server and database
* Skipping certificate verification

The best way to accommodate developing an application that is to be deployed to production is to use the platform's default approach for configuration files.

All of the SDKs have API compatibility with most of the features in Couchbase Operational Clusters — whether self-managed, or Capella. The following table covers possible exceptions, and gives the version of the C++ SDK and Couchbase Server with which some features were introduced.

__Table 1\. Couchbase Server and SDK Supported Version Matrix__
|                                                                                              | Server 7.2  | Server 7.6.x     | Server 8.0 |
| -------------------------------------------------------------------------------------------- | ----------- | ---------------- | ---------- |
| KV Range Scan                                                                                | N/A         | From 1.0.0       |            |
| Zone aware replica reads                                                                     | N/A         | From 1.0.0       |            |
| Vector Search with Search Vector Index                                                       | N/A         | From 1.0.0       |            |
| Vector Query using Hyperscale Vector Index                                                   | N/A         | From SDK 1.2.0 ① |            |
| Vector Query using Composite (GSI & vector) index                                            | N/A         | From SDK 1.2.0 ① |            |
| Distributed ACID Transactions                                                                | From 1.0.0  |                  |            |
| DNS SRV refresh for serverless environments (AWS Lambda, Azure Functions, and GCP Functions) | From 1.0.0  |                  |            |
| Circuit Breakers                                                                             | From 1.3.2  |                  |            |
| OTel                                                                                         | From 1.3.0  |                  |            |
| Field Level Encryption                                                                       | From 1.0.0  |                  |            |
| Cloud Native Gateway                                                                         | Unsupported |                  |            |

| **1** | As part of the standard SDK SQL++ API, it should be compatible with all earlier versions of the SDK — but it has not been tested. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------- |

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