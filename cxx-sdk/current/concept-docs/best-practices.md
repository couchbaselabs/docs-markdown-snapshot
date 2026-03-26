---
title: Best Practices
description: Speed up your application development, with some best practices for
  using Couchbase SDKs.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.3/modules/concept-docs/pages/best-practices.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cxx-sdk:concept-docs:best-practices.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/current/concept-docs/best-practices.html)

# Best Practices

> Speed up your application development, with some best practices for using Couchbase SDKs. 

From batching and reactive APIs, to unit tests and handling errors. There's plenty that can be done to remove bottlenecks in development and in performance, and this page can be your checklist of areas not to neglect as you develop your app.

## [](#security)Security

But before worrying about bottlenecks, let's put security concerns first.

Security is a process, and not just a set of checkboxes — but

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

### [](#dealing-with-timeout-errors)Dealing with Timeout Errors

* LAN-type connection of client and server is recommended in production, but WAN development is a reality pre-production. Ensure that you're familiar with the [best timeout options for WAN environments](../ref/client-settings.md#constrained-network-environments), or at least set a [WAN development Configuration Profile](../ref/client-settings.md#wan-development).

### [](#concurrency-and-async-apis)Concurrency and Async APIs

See the [Async & Reactive APIs page](../howtos/concurrent-async-apis.md) for practical examples.

## [](#error-handling)Error Handling

Best practices for error handling in C++ depend somewhat upon your choice of API: future, or callback based, as covered in the [async and reactive API guide](#concurrent-async-apis.adoc). That guide also covers how errors are actually returned and handled. Your application should always check if an operation returned an error, and potentially handle any specific error codes that may have returned. See also the [error handling guide](../howtos/error-handling.md), which covers specific errors, along with a broader look at error handling strategies.

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