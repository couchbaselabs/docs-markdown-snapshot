---
title: Couchbase Mobile
description: Couchbase Mobile delivers the power of NoSQL to the Edge
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/couchbase-mobile-index.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.1@sync-gateway::couchbase-mobile-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/couchbase-mobile-index.html)

# Couchbase Mobile

> Couchbase Mobile delivers the power of NoSQL to the Edge 

## [](#)

Couchbase Mobile is the complete NoSQL database solution for all data storage, access, sync and security across the entire application stack. It comprises an embedded database, _Couchbase Lite_ and a web gateway for orchestrated synchronisations, _Sync Gateway_.

### [](#sync-gateway)Sync Gateway

Couchbase Mobile includes synchronization between Couchbase Lite and Couchbase Server, and peer-to-peer synchronization between Couchbase Lite instances. Synchronization is orchestrated by Sync Gateway, our secure web gateway.

[Learn More …​](../current/introduction.md)

### [](#couchbase-lite)Couchbase Lite

Couchbase Lite, our **embedded database**, manages and stores data locally on the device. It has full CRUD and query functionality, and supports all major platforms including iOS, OSX, Android, Linux, Windows, Xamarin.

[Learn More …​](../../couchbase-lite/current/index.md)

## [](#-2)

### [](#security)Security

![security](_images/icons/security.png) 

Built-in enterprise level security includes user authentication, user and role based data access control (RBAC), secure transport over TLS, and 256-bit AES full database encryption.

### [](#events)Events

![events](_images/icons/events.png) 

Couchbase Mobile raises events when data changes in the database. These events can be subscribed to on both the device and server

### [](#rest-api)Rest API

![restapi](_images/icons/restapi.png) 

REST APIs provide full programmatic access for reading and writing data over the web. Input and output is JSON, and it's easy to integrate with existing apps and REST architectures

### [](#stream-batch-api)Stream & Batch API

![streambatch](_images/icons/streambatch.png) 

Stream and Batch APIs enable low latency access to streams of data changes and bulk get and put operations. These APIs balance latency, throughput and fault-tolerance, providing comprehensive management of batch data while using stream processing to provide real-time access to data changes.

### [](#json-data-modelling)JSON data modelling

![json](_images/icons/json.png) 

Couchbase Mobile uses JSON as its lightweight and flexible data modeling language. All data is stored and transmitted as JSON, including the embedded database, the database server, REST APIs, stream APIs, and batch APIs

### [](#database-server)Database Server

![couchbaseserver](_images/icons/couchbaseserver.png) 

Couchbase Server, our database server, manages and stores data in the cloud. It scales easily to billions of records and terabytes of data, supports millions of concurrent users, and provides 24x365 uptime.