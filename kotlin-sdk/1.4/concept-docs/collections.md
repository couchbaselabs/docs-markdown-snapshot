[View original HTML](/kotlin-sdk/1.4/concept-docs/collections.html)

> Fully supported in Couchbase Server 7.x 

The Collections feature in Couchbase Server is fully implemented in the 3.2 API version of the Couchbase SDK.

Information on _Collections_ can be found in the [server docs](#7.1@server:learn:data/scopes-and-collections.adoc).

## [](#using-collections-scopes)Using Collections & Scopes

Access a non-default collection, in the default scope, with:

```java
collection = bucket.collection("bookings"); // in default scope
```

And for a non-default scope:

```java
collection = bucket.scope("tenant_agent_00").collection("bookings");
```

## [](#further-reading)Further Reading

To see Collections in action, take a look at our [Collections-enabled Travel Sample page](#howtos:working-with-collections.adoc).