---
title: Introduction
editUrl: https://github.com/couchbaselabs/mobile-training-todo/edit/tutorials/content/modules/todo-app/pages/introduction.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:tutorials:todo-app:introduction.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/todo-app/introduction.html)

# Introduction

Couchbase Mobile brings the power of NoSQL to mobile. It is comprised of three different components: Couchbase Lite, an embedded NoSQL database, Sync Gateway, an internet-facing synchronization mechanism that securely syncs data between device and cloud, and Couchbase Server, a highly scalable and performant NoSQL database in the cloud.

Couchbase Mobile simplifies "offline first" development. As shown on the diagram below, Couchbase Lite runs locally on the device and persists data as JSON and binary format. You can perform CRUD operations directly to the local database.

![image57](_images/image57.png)

Sync Gateway is the web tier that exposes a database API for Couchbase Lite databases to replicate to and from Couchbase Server (data is not persisted in Sync Gateway). Couchbase Server is used as a storage engine by Sync Gateway.

In this developer tutorial series, you will build a ToDo List application with Couchbase Mobile and learn how to use the database, add synchronization, and add security.

![iOS](_images/image11.png) 

Figure 1\. iOS

![Android](_images/image11a.png) 

Figure 2\. Android

![Xamarin Android](_images/image11xa.png) 

Figure 3\. Xamarin Android

![Windows](_images/image11w.png) 

Figure 4\. Windows

## [](#course-outline)Course Outline

### [](#data-modeling)Data Modeling

How to choose the data structure for entities and relationships between those entities.

* Documents types
* Relationships between Documents

### [](#design)Design

How to convert a set of application requirements and business rules into security rules for Couchbase Mobile.

* Access to Channels
* User privileges

### [](#using-the-database)Using the Database

How to use the persistence APIs and query language for simple queries and data aggregation to perform query operations across different model types.

* Querying Data
* Writing Data
* Aggregating Data

### [](#adding-synchronization)Adding Synchronization

How to install Sync Gateway on your development environment, start the synchronization from the application and manage conflicts.

* Installation
* Synchronizing
* Detecting and resolving Conflicts

### [](#adding-security)Adding Security

How to add access control rules based on each authenticated user and how to add security locally with database encryption and offline login.

* User Authentication
* Read/Write Access Controls
* Database Encryption
* Offline Login