---
title: About These Docs
description: Meta documentation -- what you might need to know to get the best
  from these docs, from their intent to their Information Architecture.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.8/modules/project-docs/pages/metadoc-about-these-sdk-docs.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.8@java-sdk:project-docs:metadoc-about-these-sdk-docs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.8/project-docs/metadoc-about-these-sdk-docs.html)

# About These Docs

> Meta documentation — what you might need to know to get the best from these docs, from their intent to their Information Architecture. 

Welcome to the [Java SDK 3.8](compatibility.md#api-version) docs — this is an _afterword_ to the documentation, rather than something most people will read as a _foreword_. Why so? On most occasions you will arrive at a page directly from a search engine or LLM, perhaps follow a link to another page or two, and then depart (with, we hope, your questions answererd). This page is to help with those occasions when you are unsure precisely what you want, but you are after understanding — so this page is a guide to the SDK docs, to help you to get the most from them.

## [](#assumptions-presumptions)Assumptions & Presumptions

Couchbase is a complex and powerful product, with many components. The SDKs interact with Couchbase Server and its various services; although some links are given to the pages for these services, gaining an understanding of them is not the principal aim of the SDK documentation, rather it is to gain an understanding of how to interact with them programmatically from the SDK, as many application programmers will have the task specced out for them.

Some concepts, such as Role-Based Access Control, do need to be understood in greater depth — but this is documented [in the appropriate place in the Server docs](../../../server/7.6/learn/security/roles.md), and the [Capella docs](../../../cloud/projects/project-roles.md), and linked from the [Getting Started Guide](../hello-world/start-using-sdk.md). Additionally, things which are essential in production can be a barrier to getting up and running quickly in order to try something out — so the _Full Admin_ RBAC role is used in the _Hello World_ code example, contrary to best practice (but this is, of course, called out).

### [](#concepts-howtos-and-reference-information)Concepts, Howtos, and Reference Information

Earlier SDK docs led with sections of Howto guides, with reference and discussion (concept) docs appended to the end along with project docs such as release notes. Whilst howtos, with their easily parseable code snippets, are what the majority of developers want most of the time, a broader context is often needed go ensure that any SDK API is used appropriately.

Furthermore, for developers with less experience of databases in the distributed world, some discussion of the issues of consistency and isolation can ensure that the right decisions are made once your app use starts to scale up. Hence each section carries a broad introduction, highlighting points to consider, but skippable by those who already know the territory.

### [](#limits-of-the-sdk-docs)Limits of the SDK Docs

Large as this docset is, it can only cover a subset of the complette SDK API. For a comprehensive answer to anything not completely covered in these docs, your first port of call should always be the [API reference](https://docs.couchbase.com/sdk-api/couchbase-java-client/). For many languages, you will also access this from your chosen IDE.

## [](#getting-started)Getting Started

* [Hello World](../hello-world/start-using-sdk.md)

The Getting Started section contains tutorial pages — in intention, if not always in style — covering [how to install and start using](../hello-world/start-using-sdk.md) the SDK, as well as a longer [Sample Application](../hello-world/sample-application.md) (which is not present for _every_ SDK).

It also contains information on connecting to the database, and a section of troubleshooting information for when the application code is remote from the database — such as developing an app on your laptop, with the Cluster in the Cloud Service Provider's Zone some distance away — a set-up not supported in production, but typical in development or evaluation.

## [](#data-modelling-durability-and-consistency)Data Modelling, Durability, and Consistency

* [Data Modelling, Durability, and Consistency](../concept-docs/data-durability-acid-transactions.md)

A database has a simple job — storing your data, and giving some of it back to you when you ask. Behind that simplicity is a whole world of difficulty, to ensure the best combination of consistency and availability of documents partitioned across many nodes. Our introduction suggests key areas to consider when scaling up your app.

This section also contains details of interacting with our super fast [Data Service](../howtos/kv-operations.md), bandwidth-saving [Sub-Document APIs](../howtos/subdocument-operations.md), and [compression](../concept-docs/compression.md), [Field-Level Encryption](../howtos/encrypting-using-sdk.md), and [working with non-JSON data](../concept-docs/nonjson.md).

## [](#querying-your-data)Querying Your Data

* [Querying Your Data](../concept-docs/querying-your-data.md)

For developers with an RDBMS, Couchbase's SQL implementation, SQL++, makes querying familiar. But don't be so quick to jump straight to SQL++ — assess your use case carefully.

In addition to [SQL++ queries](../howtos/sqlpp-queries-with-sdk.md), and longer running [analytics queries](../howtos/analytics-using-sdk.md) (OLAP) queries, and a [Search Service](../howtos/full-text-searching-with-sdk.md)(which includes [Vector Search](../howtos/vector-searching-with-sdk.md)), you can quickly access data where you know keys or [key ranges](#howtos:kv-range-scan.adoc), and this can be substantially quicker, thanks to the Data Service's speedy binary protocol.

## [](#distributed-acid-transactions)Distributed ACID Transactions

* [Distributed ACID Transactions from the Java SDK](../howtos/distributed-acid-transactions-from-the-sdk.md)

As with SQL++ queries, ACID transactions may be a familiar tool that you choose automatically — but take time to weigh up your use case against the constraints of such a consistency model.

## [](#dealing-with-delays-outages-and-unreliable-networks)Dealing with Delays, Outages, and Unreliable Networks

* [Failure Considerations](../concept-docs/durability-replication-failure-considerations.md)

A distributed world brings challenges not just of node and network failures, but even of operating with uncertain knowledge of those things. Couchbase is architected to give reliable results but as always, taking time to understand the issue can give you a more reliable application, and a better service to your users.

This section also contains details of the [observability](../concept-docs/response-time-observability.md) stack available within the SDK, to help to identify problems and profile bottlenecks.

## [](#best-practices)Best Practices

* [Best Practices](../concept-docs/best-practices.md)

Choice is the mantra of many programming languages, and Couchbase offers support for many approaches to programming and architectural choices. Where possible, we offer strong recommendations, for what will work best in _most_ circumstances.

This section also contains discussions for some of the [best ways of dealing with errors and exceptions](../howtos/error-handling.md).

## [](#managing-couchbase)Managing Couchbase

* [Managing Couchbase](../concept-docs/management-api.md)

Some will prefer to administer Couchbase programmatically, rather than through UI, REST API, or command line. This section covers the available management APIs in the SDK.

## [](#sdk-deployment)SDK Deployment

* [SDK Deployment](deployment.md)

A section on those non-programmatic considerations — [compatibility guides](compatibility.md), [migration](migrating-sdk-code-to-3.n.md), [third party integrations](third-party-integrations.md), [licensing](sdk-licenses.md), and [release notes](sdk-release-notes.md).

## [](#reference-docs)Reference Docs

* [Reference Pages](../ref/index.md)

The key reference doc is the API guide, which should be an accurate and complete source of truth for programming with the Java SDK's API. Any error here should be filed directly against the individual SDKs bug tracker (JIRA), although a ticket against the docs [here](https://issues.couchbase.com/projects/DOC/issues) will always be converted to the correct project.

The first link in the navigation for the Reference Section is to the API Guide for the _latest version_ of the SDK. Links to previous versions can be found with the [Release Notes](sdk-release-notes.md).

Other reference material includes the [Client Settings](../ref/client-settings.md) that can be adjusted, and a listing of all [Error Codes](../ref/error-codes.md).

## [](#another-route-through)Another Route Through?

Each page contains several links to related pages in the docs, as well as to relevant sections of the latest generated API docs. Links are made to cover as many common user journeys as we could think of. For cases where we didn't anticipate your needs, every page in each SDK is linked from the left-hand navigation, and the paragraphs above detail the broad purpose of these groupings and some of their content.

### [](#site-search)Site Search

Our internal _Site Search_ is an excellent resource for finding information across Couchbase components and (supported) versions.

## [](#older-sdk-versions)Older SDK Versions

All supported versions of the SDKs can be found in the doc set — use the dropdown version selector in the left-hand navigation to reach each one. Documentation on older, unsupported versions of the SDK — that have reached end-of-life — can be found in the [archive](https://docs-archive.couchbase.com/home/index.html).