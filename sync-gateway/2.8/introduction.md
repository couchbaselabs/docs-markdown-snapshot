---
title: Introduction
description: A short introduction to <em>Couchbase's Sync Gateway</em> and how
  to get started using it.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/introduction.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::introduction.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/introduction.html)

# Introduction

> A short introduction to _Couchbase's Sync Gateway_ and how to get started using it.  
> This is **Step 1** in Sync Gateway's Start Here! topic group.

Related _Start Here!_ topics: [Prepare](#sync-gateway::get-started-prepare.adoc) | [Install](#sync-gateway::get-started-install.adoc) | [Verify](#sync-gateway::get-started-verify-install.adoc)

## [](#getting-started-with-sync-gateway)Getting Started with Sync Gateway

Steps in Getting Started

**Introduction**| [Prepare](#sync-gateway::get-started-prepare.adoc)| [Install](#sync-gateway::get-started-install.adoc)| [Verify](#sync-gateway::get-started-verify-install.adoc)

Sync Gateway is the synchronization server in a Couchbase for Mobile and Edge deployment. It is designed to provide data synchronization for large-scale interactive web, mobile, and IoT applications — see: [Figure 1](#fig-mobile-server).

![cbm architecture](_images/cbm-architecture.png) 

Figure 1\. Couchbase Mobile — Deployment Architecture

As you can see from [Figure 1](#fig-mobile-server) Sync Gateway synchronizes changes made by web clients through its REST API, Couchbase Lite mobile-device applications, and Couchbase Server buckets.

You can read more about the Data Synchronization process in [Sync with Couchbase Server](../current/sync/sync-with-couchbase-server.md). Some of its most central, and commonly used features, are those used to ensure secure **Access Control**.

Sync Gateway assures secure access control using:

* **User authentication**, which ensures that only authorized users can connect to Sync Gateway. For more information see the [Users](../current/access-control/users.md), [Roles](../current/access-control/roles.md) and [User Authentication](../current/security/authentication-users.md) content.
* **Data Routing**, which ensures that authorized users can only access documents in those [Channels](../current/access-control/channels.md) assigned to them and only in accordance with their assigned privileges. You can set those privileges to confer [Read Access](#sync-gateway::read-access.adoc) and-or [Write Access](../current/access-control/access-control-how-control-document-access.md) as required.

The business logic behind the validation and authorization of document access is provided by the customizable [Sync Function](../current/access-control/sync-function/sync-function.md).

## [](#related-content)Related Content

###### [](#)

Getting Started

* [Prepare](#sync-gateway::get-started-prepare.adoc)
* [Install](#sync-gateway::get-started-install.adoc)
* [Verify](#sync-gateway::get-started-verify-install.adoc)

###### [](#-2)

Product Information

* [Release Notes](../current/product-notes/release-notes.md)
* [Compatibility Matrix](#sync-gateway::compatibility.adoc)
* [Supported OS](#sync-gateway::pn-supported-os.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)