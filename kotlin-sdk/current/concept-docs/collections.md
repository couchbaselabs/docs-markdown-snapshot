---
title: Collections &amp; Scopes
description: Fully supported in Couchbase Server 7.x
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/3.12/modules/concept-docs/pages/collections.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:kotlin-sdk:concept-docs:collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/current/concept-docs/collections.html)

# Collections &amp; Scopes

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