---
title: Collections and Scopes
description: Fully supported in Couchbase Server 7.0.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/1.5/modules/concept-docs/pages/collections.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:1.5@scala-sdk:concept-docs:collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.5/concept-docs/collections.html)

# Collections and Scopes

> Fully supported in Couchbase Server 7.0\. 

The Collections feature in Couchbase Server 7.0 is fully implemented in the Scala SDK version 1.2.

Please see the [Scopes and Collections page](../../../server/7.2/learn/data/scopes-and-collections.md) in the Server docs.

## [](#using-collections-scopes)Using Collections & Scopes

Access a non-default collection, in the default scope, with:

```scala
collection = bucket.collection("bookings") // in default scope
```

And for a non-default scope:

```scala
collection = bucket.scope("tenant_agent_00").collection("bookings")
```

## [](#further-reading)Further Reading

To see Collections in action, take a look at our [Collections-enabled Travel Sample page](../howtos/working-with-collections.md).