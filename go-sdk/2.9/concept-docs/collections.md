---
title: Collections and Scopes
description: Fully supported in Couchbase Server 7.1.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.9/modules/concept-docs/pages/collections.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.9@go-sdk:concept-docs:collections.adoc[]
---

[View original HTML](/go-sdk/2.9/concept-docs/collections.html)

# Collections and Scopes

> Fully supported in Couchbase Server 7.1\. 

The Collections feature in Couchbase Server is fully implemented in all current supported versions of the Go SDK.

Information on _Collections_ can be found in the [server docs](#7.6@server:learn:data:scopes-and-collections.adoc).

## [](#using-collections-and-scopes)Using Collections and Scopes

Access a non-default collection, in the default scope, with:

```golang
bucket.Collection("bookings") // in default scope
```

And for a non-default scope:

```golang
bucket.Scope("tenant_agent_00").Collection("bookings")
```

## [](#further-reading)Further Reading

To see Collections in action, take a look at our [Collections-enabled Travel Sample page](../howtos/working-with-collections.md).