---
title: Introduction
description: A short introduction to <em>Couchbase's Sync Gateway</em> and how
  to get started using it.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/introduction.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@sync-gateway::introduction.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/introduction.html)

# Introduction

> A short introduction to _Couchbase’s Sync Gateway_ and how to get started using it.  
> This is **Step 1** in Sync Gateway’s Start Here! topic group.

Related _Start Here!_ topics: [Prepare](get-started-prepare.md) | [Install](get-started-install.md) | [Verify](get-started-verify-install.md)

## [](#getting-started-with-sync-gateway)Getting Started with Sync Gateway

Steps in Getting Started

**Introduction**| [Prepare](get-started-prepare.md)| [Install](get-started-install.md)| [Verify](get-started-verify-install.md)

Sync Gateway is the synchronization server in a Couchbase Mobile deployment. It is designed to provide data synchronization for large-scale interactive web, mobile, and IoT applications — see: [Figure 1](#fig-mobile-server).

![cbm architecture](_images/cbm-architecture.png) 

Figure 1\. Couchbase Mobile — Deployment Architecture

As you can see from [Figure 1](#fig-mobile-server) Sync Gateway synchronizes changes made by web clients through its REST API, Couchbase Lite mobile-device applications, and Couchbase Server buckets.

You can read more about the Data Synchronization process in [Sync with Couchbase Server](sync-with-couchbase-server.md). Some of its most central, and commonly used features, are those used to ensure secure **Access Control**.

Sync Gateway assures secure access control using:

* **User authentication**, which ensures that only authorized users can connect to Sync Gateway. For more information see the [Users](users.md), [Roles](roles.md) and [User Authentication](authentication-users.md) content.
* **Data Routing**, which ensures that authorized users can only access documents in those [Channels](channels.md) assigned to them and only in accordance with their assigned privileges. You can set those privileges to confer [Read Access](#read-access.adoc) and-or [Write Access](access-control-how-control-document-access.md) as required.

The business logic behind the validation and authorization of document access is provided by the customizable [Sync Function](sync-function.md).

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Getting Started

* [Prepare](get-started-prepare.md)
* [Install](get-started-install.md)
* [Verify](get-started-verify-install.md)

###### [](#-3)

Product Information

* [Release Notes](release-notes.md)
* [Compatibility Matrix](compatibility.md)
* [Supported OS](supported-environments.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)