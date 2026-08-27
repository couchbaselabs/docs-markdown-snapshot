---
title: Collections and Scopes
description: Fully supported in Couchbase Server 7.0.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.5/modules/concept-docs/pages/collections.adoc
  xref: xref:4.5@python-sdk:concept-docs:collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.5/concept-docs/collections.html)

# Collections and Scopes

> Fully supported in Couchbase Server 7.0\. 

The Collections feature in Couchbase Server is fully implemented in the 3.2 API version of the Couchbase SDK.

Information on _Collections_ can be found in the [server docs](#8.0@server:learn:data:scopes-and-collections.adoc).

## [](#using-collections-scope)Using Collections & Scope

Access a non-default collection, in the default scope, with:

```python
bucket.collection("flights")
```

And for a non-default scope:

```python
bucket.scope("marlowe_agency").collection("flights")
```

## [](#further-reading)Further Reading

* Please see the [Collections Overview documents](../../../server/current/learn/data/scopes-and-collections.md) in the Server docs.
* To see Collections in action, take a look at our [Collections-enabled Travel Sample page](../hello-world/sample-application.md).