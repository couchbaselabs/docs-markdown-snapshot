---
title: Choose Your Next Steps
description: To complete the Getting Started sequence, consider your options as
  to what to do next to continue improving your knowledge.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/getting-started/pages/choose-your-next-steps.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/getting-started/choose-your-next-steps.html)

# Choose Your Next Steps

> To complete the Getting Started sequence, consider your options as to what to do next to continue improving your knowledge. The Couchbase documentation set provides detailed information on all aspects of the platform; and this topic lists some of the important areas you can visit. 

## [](#where-to-learn-more)Where to Learn More

By navigating to the sections in this topic, you can increase your knowledge in the areas you’ve already looked at — installation, configuration, and SQL++ — and also learn about new and (in some cases) quite advanced topics; such as multi-node clustering, failover, replication, and statistical analysis.

## [](#installation-and-configuration)Installation and Configuration

Couchbase Server can be deployed and installed in several different ways, including on traditional bare-metal servers, virtual machines, containers, and in the cloud. Take a look at the information provided in [Couchbase Server Deployment Options](../install/get-started.md) to find the right deployment for you.

Couchbase Server can be configured in a variety of ways. You can perform the configuration using the Couchbase Server Web Console, the Couchbase Command Line Interface (CLI), or with the Couchbase REST API. See [Create a Cluster](../manage/manage-nodes/create-cluster.md) for details.

Periodically, you will need to stop and start individual server nodes. Information on doing this is provided in the section [Couchbase Server Startup and Shutdown](../install/startup-shutdown.md).

## [](#development)Development

The [Developer Tutorial: Student Record System](../tutorials/couchbase-tutorial-student-records.md) provides an introductory worked example for developers, showing how to use a software development kit with a simple database.

The [Developer Guides](../develop/intro.md) section contains practical how-to guides that walk you through common Couchbase Server development tasks.

The Develop section also contains important background detail that you will need for development using Couchbase Server. Refer to [Query](../n1ql/query.md) for details about querying Couchbase Server using the SQL++ query language; [Full Text Search](../search/search.md) for information on text search and geospatial queries; [Eventing](../eventing/eventing-overview.md) for server-side programming using Eventing functions; or [Analytics](../analytics/introduction.md) for ad-hoc analytical queries.

## [](#using-the-couchbase-sdk)Using the Couchbase SDK

The Couchbase SDK is available for several different programming languages. Take a look at the section [home:ROOT:sdk.adoc](#home:ROOT:sdk.adoc). You can select a language, and the page for that language provides information on installing supportive modules and libraries, and also includes code-examples to help you with development.

## [](#concepts-and-architecture)Concepts and Architecture

Your hands-on progress with Couchbase Server will be greatly helped by a good _conceptual_ knowledge. Start by looking at the [Architecture Overview](../learn/architecture-overview.md), and then go from there.

## [](#authorization)Authorization

Couchbase Server resources are protected by means of _role-based access control_ (RBAC). This means that different _roles_ are assigned to different _users_, each role being associated with a subset of _privileges_ on one or more resources. This makes it possible, for example, for one user to be granted read-access on a particular bucket, while another user is granted both read and write-access on the same bucket. For a detailed explanation, see [Authorization](../learn/security/authorization-overview.md).

## [](#administration)Administration

If you are an administrator, your priority will be to learn about system setup and cluster management. Start by reading an overview of management tasks in [Management Overview](../manage/management-overview.md).

## [](#integration)Integration

In some cases, you may wish to integrate Couchbase Server with another, different data-repository. For example, you might wish to continue using your current Elasticsearch database for the performance of free text searches, and extend these searches to Couchbase Server-data, so that Couchbase-documents can be retrieved. For this to be possible, data must be shared between the repositories, and your querying coordinated between them.

See [Connector Guides](../connectors/intro.md) for information about Elasticsearch and all other repositories with which you can integrate Couchbase Server.

## [](#additional-reference-information)Additional Reference Information

When you start interacting with Couchbase in more advanced ways, make sure to explore some of the reference documentation, such as [REST API reference](../rest-api/rest-intro.md) and [CLI Reference](../cli/cli-intro.md).