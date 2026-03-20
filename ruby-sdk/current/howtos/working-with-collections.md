---
title: Working with Collections
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.7/modules/howtos/pages/working-with-collections.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:ruby-sdk:howtos:working-with-collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/current/howtos/working-with-collections.html)

# Working with Collections

> The 3.x API SDKs all work with all features of Collections and Scopes. 

The [Collections feature](../../../server/current/learn/data/scopes-and-collections.md) in Couchbase Server 7.x is fully implemented in the 3.x API versions of the Couchbase SDKs.

> [!NOTE]
> When working with versions earlier than 7.0, the `defaultcollection` is used from the SDK.

Read more about [Collections and Scopes](../concept-docs/collections.md).

## [](#sample-application)Sample Application

The [Travel Sample Application](../hello-world/sample-application.md) has been updated with a motivating example for Collections - a multi-tenanted travel application. Imagine that we are providing a white-label Flight and Hotel booking service to multiple travel agents. Each tenant agent will get the same underlying service, but interact only with their own data.

The `travel-sample` bucket has been split into _Scopes_ for multiple tenant travel agents (for example `tenant_agent_00`, `tenant_agent_01`, …​) and a shared `inventory` which is further subdivided into _Collections_ such as `hotels` and `airports`.

Read more about the new travel-sample [Data Model](../ref/travel-app-data-model.md).

The app is currently implemented for the following SDKs:

* [Go](#2.3@go-sdk:hello-world:sample-application.adoc)
* [Java](#3.2@java-sdk:hello-world:sample-application.adoc)
* [Java Spring Data](#3.2@java-sdk:hello-world:spring-data-sample-application.adoc)
* [.NET](#3.2@dotnet-sdk:hello-world:sample-application.adoc)
* [Node.js](#3.2@nodejs-sdk:hello-world:sample-application.adoc)
* [PHP](#3.2@php-sdk:hello-world:sample-application.adoc)
* [Python](#3.2@python-sdk:hello-world:sample-application.adoc)
* [Scala](#1.2@scala-sdk:hello-world:sample-application.adoc)
* [Ruby](#3.2@ruby-sdk:hello-world:sample-application.adoc)