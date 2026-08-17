---
title: Collections and Scopes
description: Fully supported in Couchbase Server 7.1.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.8/modules/concept-docs/pages/collections.adoc
  xref: xref:2.8@go-sdk:concept-docs:collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.8/concept-docs/collections.html)

# Collections and Scopes

> Fully supported in Couchbase Server 7.1\. 

The Collections feature in Couchbase Server is fully implemented in the 2.6 API version of the Couchbase SDK.

Information on _Collections_ can be found in the [server docs](#7.1@server:learn:data:scopes-and-collections.adoc).

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