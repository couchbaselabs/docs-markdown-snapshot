---
title: About These Docs
description: Meta documentation -- what you might need to know to get the best
  from these docs, from their intent to their Information Architecture.
editUrl: https://github.com/couchbase/docs-analytics-sdk-python/edit/release/1.0/modules/project-docs/pages/metadoc-about-these-sdk-docs.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:1.0@python-analytics-sdk:project-docs:metadoc-about-these-sdk-docs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-analytics-sdk/1.0/project-docs/metadoc-about-these-sdk-docs.html)

# About These Docs

> Meta documentation — what you might need to know to get the best from these docs, from their intent to their Information Architecture. 

Welcome to the [Python Analytics SDK 1.0](compatibility.md#api-version) docs — this is an _afterword_ to the documentation, rather than something most people will read as a _foreword_. Why so? On most occasions you will arrive at a page directly from a search engine or LLM, perhaps follow a link to another page or two, and then depart (with, we hope, your questions answererd). This page is to help with those occasions when you are unsure precisely what you want, but you are after understanding — so this page is a guide to the SDK docs, to help you to get the most from them.

## [](#assumptions-presumptions)Assumptions & Presumptions

Couchbase is a complex and powerful product, with many components. The Analytics SDKs simply interact with Enterprise Analytics, not Couchbase Server and its various services — but some of that complexity spills across into the Analytics SDKs and their documentation.

Some concepts, such as Role-Based Access Control, do need to be understood in greater depth — but this is documented [in the appropriate place in the Server docs](../../../server/current/learn/security/roles.md), and the [Capella docs](../../../cloud/projects/project-roles.md), and linked from the [Getting Started Guide](../hello-world/start-using-sdk.md). Additionally, things which are essential in production can be a barrier to getting up and running quickly in order to try something out — so the _Full Admin_ RBAC role is used in the _Hello World_ code example, contrary to best practice (but this is, of course, called out).

### [](#concepts-howtos-and-reference-information)Concepts, Howtos, and Reference Information

Earlier Server SDK docs led with sections of Howto guides, with reference and discussion (concept) docs appended to the end along with project docs such as release notes. Whilst howtos, with their easily parseable code snippets, are what the majority of developers want most of the time, a broader context is often needed go ensure that any SDK API is used appropriately.

Furthermore, for developers with less experience of databases in the distributed world, some discussion of the issues of consistency and isolation can ensure that the right decisions are made once your app use starts to scale up. Hence each section carries a broad introduction, highlighting points to consider, but skippable by those who already know the territory.

### [](#limits-of-the-sdk-docs)Limits of the SDK Docs

Large as this docset is, it can only cover a subset of the complete Analytics SDK API. For a comprehensive answer to anything not completely covered in these docs, your first port of call should always be the [API reference](https://docs.couchbase.com/sdk-api/analytics-python-client). For many languages, you will also access this from your chosen IDE.

## [](#getting-started)Getting Started

* [Hello World](../hello-world/start-using-sdk.md)

The Getting Started section contains tutorial pages — in intention, if not always in style — covering [how to install and start using](../hello-world/start-using-sdk.md) the SDK.

It also contains information on connecting to the database, and a section of troubleshooting information for when the application code is remote from the database — such as developing an app on your laptop, with the Cluster in the Cloud Service Provider's Zone some distance away — a set-up not supported in production, but typical in development or evaluation.

## [](#querying-your-data)Querying Your Data

* [Querying Your Data](../concept-docs/querying-your-data.md)

The heart of the Analytics Cluster — real-time OLAP querying, with Couchbase's familiar SQL++ query language.

## [](#sdk-deployment)SDK Deployment

* [SDK Deployment](deployment.md)

A section on those non-programmatic considerations — [compatibility guides](compatibility.md), [licensing](sdk-licenses.md), and [release notes](#project-docs:sdk-release-notes.adoc).

## [](#reference-docs)Reference Docs

* [Reference Pages](../ref/index.md)

The key reference doc is the API guide, which should be an accurate and complete source of truth for programming with the Python SDK's API. Any error here should be filed directly against the individual SDKs bug tracker — via the GitHub issues on <https://github.com/couchbaselabs/analytics-python-client> — although a ticket against the docs [here](https://issues.couchbase.com/projects/DOC/issues) will always be converted to the correct project.

> [!TIP]
> You can also file JIRA tickets against these docs by clicking the **Leave Additional Feedback?** link on most pages in the docs.

The first link in the navigation for the Reference Section is to the API Guide for the _latest version_ of the SDK. Links to previous versions can be found with the [Release Notes](#project-docs:sdk-release-notes.adoc).

Other reference material includes the [Client Settings](../ref/client-settings.md) that can be adjusted, and a listing of all [Error Codes](../ref/error-codes.md).

## [](#another-route-through)Another Route Through?

Each page contains several links to related pages in the docs, as well as to relevant sections of the latest generated API docs. Links are made to cover as many common user journeys as we could think of. For cases where we didn't anticipate your needs, every page in each SDK is linked from the left-hand navigation, and the paragraphs above detail the broad purpose of these groupings and some of their content.

### [](#site-search)Site Search

Our internal _Site Search_ is an excellent resource for finding information across Couchbase components and (supported) versions.