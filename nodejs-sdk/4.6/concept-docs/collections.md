---
title: Collections and Scopes
description: Fully supported in Couchbase Server 7.0.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.6/modules/concept-docs/pages/collections.adoc
  xref: xref:4.6@nodejs-sdk:concept-docs:collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.6/concept-docs/collections.html)

# Collections and Scopes

> Fully supported in Couchbase Server 7.0\. 

The Collections feature in Couchbase Server is fully implemented in the 3.2 API version of the Couchbase SDK.

Information on _Collections_ can be found in the [server docs](#8.0@server:learn:data:scopes-and-collections.adoc).

## [](#using-collections-scope)Using Collections & Scope

Access a non-default collection, in the default scope, with:

```javascript
bucket.collection("flights")
```

And for a non-default scope:

```javascript
bucket.scope("marlowe_agency").collection("flights") too
```

* Please see the [Collections Overview documents](#8.0@server:collections/collections-overview.adoc) in the Server docs.
* To see Collections in action, take a look at our [Collections-enabled Travel Sample page](../howtos/working-with-collections.md).