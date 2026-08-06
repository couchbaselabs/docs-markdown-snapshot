---
title: Couchbase Mobile
description: Couchbase Mobile brings the power of NoSQL to the edge. The
  combination of Sync Gateway and Couchbase Lite coupled with the power of
  Couchbase Server provides fast, efficient bidirectional synchronization of
  data between the edge and the cloud. This lets you deploy fully featured
  mobile and embedded applications with greater agility on premises or in any
  cloud.
editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/ROOT/pages/mobile.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:home::mobile.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/mobile.html)

# Couchbase Mobile

## Welcome to Couchbase Mobile

###### 

Couchbase Mobile brings the power of NoSQL to the edge. The combination of Sync Gateway and Couchbase Lite coupled with the power of Couchbase Server provides fast, efficient bidirectional synchronization of data between the edge and the cloud. This lets you deploy fully featured mobile and embedded applications with greater agility on premises or in any cloud.

###### 

## How the pieces fit together

Couchbase Mobile supports three deployment patterns.

In a self-managed deployment, Couchbase Lite connects to a Sync Gateway that you deploy and operate, and Sync Gateway pushes data to a self-managed Couchbase Server.

In a fully managed deployment, Couchbase Lite connects directly to Capella App Services, and App Services syncs data to your Capella Operational cluster.

In a hybrid deployment, Couchbase Lite connects to a self-managed Sync Gateway, but that Sync Gateway points to a Capella Operational cluster instead of a self-managed Couchbase Server.

App Services is Capella's managed version of Sync Gateway. It runs the same synchronization engine, hosted and operated by Capella. Feature parity between the two is common but not guaranteed, since some Sync Gateway features may not carry over to App Services, and App Services has features of its own.

For resource-constrained environments, such as single-board computers or point-of-sale terminals, Couchbase Edge Server sits between Couchbase Lite devices and the cloud sync layer.

###### 

## Couchbase Mobile Products

Each product below handles a specific part of the Couchbase Mobile ecosystem, from the embedded database on the device to the sync layer in the cloud.

Select a product to go to its documentation.

Couchbase Lite

Couchbase Lite is an embedded, NoSQL JSON document database for your mobile apps. It natively supports all major operating systems and platforms. Its NoSQL client database provides CRUD, full-text search and query capabilities that runs locally on the device.  
[Go to Couchbase Lite Docs](../couchbase-lite/current/index.md)

Sync Gateway

Sync Gateway is a secure, high-performance gateway designed for cloud-to-edge data synchronization. It serves as the synchronization server in a Couchbase Mobile deployment, enabling mobile, web, and IoT applications to view and sync data with Couchbase Server. You deploy and operate Sync Gateway yourself.  
[Go to Sync Gateway Docs](../sync-gateway/current/introduction.md)

App Services

App Services is Capella's managed version of Sync Gateway, running the same synchronization engine. Feature parity is common but not guaranteed: some Sync Gateway features may not be adopted into App Services, and others are built specifically for App Services as a managed offering.  
[Go to App Services Docs](#app-services:get-started:configuring-app-services.adoc)

Edge Server

Couchbase Edge Server is a lightweight standalone database for resource-constrained edge. It exposes a REST API that enables you to get database information, perform document operations, run SQL++ queries, and manage change feeds and replication.  
[Go to Edge Server Docs](../couchbase-edge-server/current/introduction/intro.md)

Couchbase Lite JavaScript

Couchbase Lite JavaScript is a lightweight, fully featured embedded NoSQL JSON document database for browser-based apps. It provides query, indexing, and data synchronization with Capella App Services or Sync Gateway.  
[Go to Couchbase Lite JavaScript Docs](#couchbase-lite-javascript::introduction.adoc)

Tutorials

Sample tutorials to build Mobile applications on the edge.  
[Couchbase Mobile Tutorials](https://developer.couchbase.com/tutorials)