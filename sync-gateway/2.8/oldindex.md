---
title: Introduction
description: This content gives a brief introduction to sync gateway and
  includes link to topics with more detail
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/oldindex.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::oldindex.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/oldindex.html)

# Introduction

# Introducing Sync Gateway

> This content gives a brief introduction to sync gateway and includes link to topics with more detail  

Related _Sync Gateway Concepts_ topics: [Sync with Couchbase Server](../current/sync/sync-with-couchbase-server.md) | [Users](../current/access-control/users.md) | [Configuration Properties](../current/configuration/configuration-properties-legacy.md) | [Public REST API](../current/rest-api/rest-api.md) | [Admin REST API](../current/rest-api/rest-api-admin.md) | [More …​](#related-content)

Sync Gateway is the synchronization server in a Couchbase for Mobile and Edge deployment. It is designed to provide data synchronization for large-scale interactive web, mobile, and IoT applications — see: [Figure 1](#mobile-server).

![cbm architecture](_images/cbm-architecture.png) 

Figure 1\. Couchbase Mobile — Couchbase Server Deployment Architecture

You can read more about the Data Synchronization process in [Sync with Couchbase Server](../current/sync/sync-with-couchbase-server.md). Amongst its most important and commonly used features is secure **Access Control**.

Sync Gateway assures secure access control using:

* **User authentication**, which ensures that only authorized users can connect to Sync Gateway. For more information see the [Users](../current/access-control/users.md) and [User Authentication](../current/security/authentication-users.md) content.
* **Data Routing**, which ensures that authorized users can only access documents in those [Channels](../current/access-control/channels.md) assigned to them and only in accordance with their assigned privileges. You can set those privileges to confer [Read Access](#sync-gateway::read-access.adoc) and-or [Write Access](../current/access-control/access-control-how-control-document-access.md) as required.  
The business logic behind the validation and authorization of document access is provided by the customizable [Sync Function](../current/access-control/sync-function/sync-function.md).

## Related Content

###### 

Getting Started

* [Prepare](#sync-gateway::get-started-prepare.adoc)
* [Install](#sync-gateway::get-started-install.adoc)
* [Verify](#sync-gateway::get-started-verify-install.adoc)

###### 

Product Information

* [Release Notes](../current/product-notes/release-notes.md)
* [Compatibility Matrix](#sync-gateway::compatibility.adoc)
* [Supported OS](#sync-gateway::pn-supported-os.adoc)

###### 

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)