---
title: Best Practices
description: Speed up your application development, with some best practices for
  using Couchbase SDKs.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/release/4.6/modules/concept-docs/pages/best-practices.adoc
  xref: xref:python-sdk:concept-docs:best-practices.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/concept-docs/best-practices.html)

# Best Practices

> Speed up your application development, with some best practices for using Couchbase SDKs. 

From async and reactive APIs, to unit tests and handling errors. There's plenty that can be done to remove bottlenecks in development and in performance, and this page can be your checklist of areas not to neglect as you develop your app.

## [](#security)Security

But before worrying about bottlenecks, let's put security concerns first.

Security is a process, and not just a set of checkboxes — but there are key areas you must check off as you move from development, through testing, to deploying in production.

### [](#roles-and-rbac)Roles and RBAC

Self-managed Couchbase Server uses Role-Based Access Control (RBAC), which is reflected in our managed service as a nuanced set of Roles. Data security depends in part on only giving access to

RBAC restrict resources on a Couchbase cluster to an identified user, allocated by role.

#### [](#users-resources-roles-and-privileges)Users, Resources, Roles, and Privileges

Couchbase Server Enterprise Edition uses _Role-Based Access Control_ for applications to restrict _resources_ on a Couchbase cluster to an identified _user_.

Each user who attempts resource-access is identified by means of the _credentials_ they pass to Couchbase Server, for purposes of _authentication_: these consist of a _username_ and (typically) a _password_. Once the user is authenticated, an _authorization_ process checks the _roles_ with which the user is associated. If one or more of these roles correspond to _privileges_ that permit the user-requested level of resource-access, access is duly granted; otherwise, it is denied.

Users who have been assigned the **Admin** role for the cluster are able to create, edit, and remove users. The SDK provides APIs to support these activities.

> [!NOTE]
> Introductory examples in the SDK documentation use the _Administrator_ user to ensure that developers can quickly get up and running; this _should not be used in production_. Elsewhere we use a general "user" which represents whichever permission levels are appropriate to your application.

## [](#performance)Performance

Couchbase's Data Service uses a fast binary protocol, which will always outperform JSON streamed over HTTP from SQL++ queries. If you know the key (ID) of a document, then use the [Data Service](../howtos/kv-operations.md).

If you need pessimistic logging, in particular if you need to lock documents for multi-document ACID transactions, then anything you can do at the schema level to reduce the number of documents locked simultaneously wil remvoe a bottleneck to updating the affected documents.

Note, a slight performance improvement can be found by [turning off observability](#rto-vs-performance), but this is rarely a good idea.

### [](#dealing-with-timeout-errors)Dealing with Timeout Errors

* `waitUntilReady` should be the default setting for `Cluster.connect` and `Cluster.bucket` in most cases, so that resources are fully loaded before the client proceeds with CRUD calls to the cluster.
* LAN-type connection of client and server is recommended in production, but WAN development is a reality pre-production. Ensure that you're familiar with the [best timeout options for WAN environments](../ref/client-settings.md#constrained-network-environments), or at least set a [WAN development Configuration Profile](../ref/client-settings.md#wan-development).

### [](#concurrency-and-async-apis)Concurrency and Async APIs

Choosing between the blocking, asynchronous, and reactive APIs for the Scala SDK is partly bound up with how (and where) you want to handle exceptions.

* Synchronous operations are blocking, and return a Scala `Try` object. This contains either the result or a _Throwable_ exception, which can be pattern matched over (using `flatMap` in more complex cases).
* The asynchronous API returns Scala `Future`, representing the execution of an asynchronous task and the promise of a future result. An `ExecutionContext` must be provided, to give a thread pool for handling whatever is returned.
* The reactive API is a more natural fit for network-aware, fault tolerant programs, and will provide full back pressure for streaming results from large SQL++ or Search queries.

See the [Async & Reactive APIs page](../howtos/concurrent-async-apis.md) for further discussion and practical examples.

## [](#error-handling)Error Handling

Best practices for error handling in Scala depend somewhat upon your choice of API: blocking, asynchronous, or reactive, as covered in the [async and reactive API guide](#concurrent-async-apis.adoc). That guide also covers how errors are actually returned (e.g. via `Try`, `Future`, or `Mono`) and handled. See also the [error handling guide](../howtos/error-handling.md), which covers specific errors, along with a broader look at error handling strategies.

## [](#testing)Testing

Integrate developing with the Python SDK into your accustomed test framework.

## [](#threshold-orphan-logging)Threshold & Orphan Logging

Observability is provided by the SDK in the following ways:

### [](#threshold-logging)Threshold Logging

Threshold logging is the recording of slow operations — useful for diagnosing when and where problems occur in a distributed environment. It is enabled by default.

You will see this information turning up in the logs something like this:

```json
Threshold Log: {"service":"kv","count":2,"top":[{"operation_name":"Insert","total_us":161679},{"operation_name":"Upsert","total_us":161451}]}
```

And as tracing values such as `total_us`, the duration of the total time taken for the operation, expressed as microseconds.

### [](#orphaned-response-reporting)Orphaned Response Reporting

Special reporting capabilities which explicitly collect information about responses which have been abandoned (i.e. timed out) at the time when the SDK tries to complete them. This is also enabled by default.

> [!TIP]
> Observability & SDK Performance
> 
> In version 4.6.0 of the Python SDK, fully featured Observability (switched on by default) replaced the limited information from the underlying C++ core. This slighty reduced overall performance of the SDK,
> 
> If absolute performance is critical to your application, then observability features can be turned off (see `ClusterOptions` in the [API reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/couchbase%5Fapi/options.html#clusteroptions)). But be sure that your performance need is strong — observability information is invaluable in diagnosing network bottlenecks and problems.

## [](#additional-information)Additional Information

SDKs are client to Couchbase Server — whether Capella Database-As-A-Service, or self-managed — and in some areas it would be wise to take a fully rounded approach. Read up on security and performance considerations relevant to your use case.

### [](#couchbase-security-best-practices)Couchbase Security Best Practices

* [Security Best Practices in Capella](../../../cloud/security/security.md)
* [Security for self-managed Couchbase Server](../../../server/current/learn/security/security-overview.md)

### [](#role-based-access-control)Role-Based Access Control

All aspects of the Couchbase RBAC system are covered in the section [Authorization](../../../server/current/learn/security/authorization-overview.md). Specifically, for information on:

* Adding _Users_ and assigning _roles_, by means of the Couchbase Web Console, see [Manage Users and Roles](../../../server/current/manage/manage-security/manage-users-and-roles.md).
* _Roles_ required for resource-access, and the privileges they entail, see [Roles](../../../server/current/learn/security/roles.md).
* _Resources_ controlled by Couchbase RBAC, see [Resources Under Access Control](../../../server/current/learn/security/roles.md).