---
title: Collections and Scopes
description: Fully supported from Couchbase Server version 7.0.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.7/modules/concept-docs/pages/collections.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.7@dotnet-sdk:concept-docs:collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.7/concept-docs/collections.html)

# Collections and Scopes

> Fully supported from Couchbase Server version 7.0\. 

The Collections feature in Couchbase Server is fully implemented in the 3.2 API version of the Couchbase SDK.

Information on _Collections_ can be found in the [server docs](#7.1@server:learn:data:scopes-and-collections.adoc).

## [](#using-collections-scopes)Using Collections & Scopes

Access a non-default collection, in the default scope, with:

```csharp
var collection_in_default_scope = await bucket.CollectionAsync("bookings");
```

And for a non-default scope:

```charp
var tenant_scope = await bucket.ScopeAsync("tenant_agent_00");
var collection_in_scope = await tenant_scope.CollectionAsync("bookings");
```

## [](#further-reading)Further Reading

To see Collections in action, take a look at our [Collections-enabled Travel Sample page](../howtos/working-with-collections.md).