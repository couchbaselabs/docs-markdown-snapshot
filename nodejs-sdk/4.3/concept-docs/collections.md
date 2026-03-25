---
title: Collections and Scopes
description: Fully supported in Couchbase Server 7.0.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.3/modules/concept-docs/pages/collections.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:4.3@nodejs-sdk:concept-docs:collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.3/concept-docs/collections.html)

# Collections and Scopes

> Fully supported in Couchbase Server 7.0\. 

The Collections feature in Couchbase Server is fully implemented in the 3.2 API version of the Couchbase SDK.

Information on _Collections_ can be found in the [server docs](#7.6@server:learn:data:scopes-and-collections.adoc).

## [](#using-collections-scope)Using Collections & Scope

Access a non-default collection, in the default scope, with:

```javascript
bucket.collection("flights")
```

And for a non-default scope:

```javascript
bucket.scope("marlowe_agency").collection("flights") too
```

* Please see the [Collections Overview documents](#7.6@server:collections/collections-overview.adoc) in the Server docs.
* To see Collections in action, take a look at our [Collections-enabled Travel Sample page](../howtos/working-with-collections.md).