---
title: Collections and Scopes
description: Fully supported in Couchbase Server 7.0.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-scala/edit/temp/1.6/modules/concept-docs/pages/collections.adoc
  xref: xref:1.6@scala-sdk:concept-docs:collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.6/concept-docs/collections.html)

# Collections and Scopes

> Fully supported in Couchbase Server 7.0\. 

The Collections feature in Couchbase Server 7.0 is fully implemented in the Scala SDK version 1.2.

Please see the [Scopes and Collections page](../../../server/7.6/learn/data/scopes-and-collections.md) in the Server docs.

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