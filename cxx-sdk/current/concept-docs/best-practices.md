---
title: Best Practices
description: Speed up your application development, with some best practices for
  using Couchbase SDKs.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: C++ SDK
    version: "1.5"
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.5/modules/concept-docs/pages/best-practices.adoc
  xref: xref:cxx-sdk:concept-docs:best-practices.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/current/concept-docs/best-practices.html)

# Best Practices

> Speed up your application development, with some best practices for using Couchbase SDKs. 

From batching and reactive APIs, to unit tests and handling errors. There's plenty that can be done to remove bottlenecks in development and in performance, and this page can be your checklist of areas not to neglect as you develop your app.

## [](#security)Security

But before worrying about bottlenecks, let's put security concerns first.

Security is a process, and not just a set of checkboxes — but there are key areas you must check off as you move from development, through testing, to deploying in production.

### [](#roles-and-rbac)Roles and RBAC

## [](#performance)Performance

Couchbase's Data Service uses a fast binary protocol, which will always outperform JSON streamed over HTTP from SQL++ queries. If you know the key (ID) of a document, then use the [Data Service](../howtos/kv-operations.md).

If you need pessimistic logging, in particular if you need to lock documents for multi-document ACID transactions, then anything you can do at the schema level to reduce the number of documents locked simultaneously wil remvoe a bottleneck to updating the affected documents.

### [](#dealing-with-timeout-errors)Dealing with Timeout Errors

* LAN-type connection of client and server is recommended in production, but WAN development is a reality pre-production. Ensure that you're familiar with the [best timeout options for WAN environments](../ref/client-settings.md#constrained-network-environments), or at least set a [WAN development Configuration Profile](../ref/client-settings.md#wan-development).

### [](#concurrency-and-async-apis)Concurrency and Async APIs

See the [Async & Reactive APIs page](../howtos/concurrent-async-apis.md) for practical examples.

### [](#bulk-get-multi-get-and-network-latency)Bulk Get, Multi-Get, and Network Latency

In traditional databases, a bulk get or multi-get is often an efficient way of overcoming network latencies as a bottleneck, or simply making more efficent use of your database's performance.

Couchbase is a distributed database, efficiently fetching data from vbuckets spread across several nodes: bulk gets can be an anti-pattern, holding things up on the Server side, compared with the efficiency of fetching your data asynchronously. However, this depends upon your platform language's availability of asynchronous APIs — see the [bulk get and async API page](../howtos/concurrent-async-apis.md) for the specifics for the C++ SDK.

#### [](#when-to-use-bulk-get)When to Use Bulk Get

As stated above, bulk gets are rarely the best way to fetch data from different documents efficently. Nevertheless, if your business logic dictates that all of, say five, results need to be returned before processing for the application's next step, then a bulk get will give you all of the results together, as needed by your app. For this reason we do provide a [batching example](../howtos/concurrent-async-apis.md#batching) for the C++ SDK.

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