[View original HTML](/dotnet-sdk/current/concept-docs/collections.html)

> Fully supported from Couchbase Server version 7.0\. 

The Collections feature in Couchbase Server is fully implemented in the 3.2 API version of the Couchbase SDK.

Information on _Collections_ can be found in the [server docs](#8.0@server:learn:data:scopes-and-collections.adoc).

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