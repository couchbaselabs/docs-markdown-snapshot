---
title: "Function: Advanced Sub-Document LOOKUPIN Operation"
description: Perform the Advanced Sub-Document LOOKUPIN operation on a field
  where Eventing interacts with the Data Service.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/eventing/pages/eventing-handler-advancedLookupInOp.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/eventing/eventing-handler-advancedLookupInOp.html)

# Function: Advanced Sub-Document LOOKUPIN Operation

Perform the Advanced Sub-Document LOOKUPIN operation on a field where Eventing interacts with the Data Service.

The `advancedLookupInField` function:

* Demonstrates the CAS-free Sub-Document LOOKUPIN operation on a document field
* Requires Eventing Storage (or a metadata collection) and a source collection
* Requires a binding of type `bucket alias`
* Operates on any mutation where the `meta.id` or KEY starts with `lookupinfield:`

For more information about the Advanced Sub-Document LOOKUPIN operation, see [Sub-Document LOOKUPIN Operation](eventing-advanced-keyspace-accessors.md#advanced-subdoc-array-op-lookupin).

* advancedLookupInField
* Input data
* Output data

```javascript
// Configure the settings for the advancedLookupInField function as follows:
//
// Version 7.6+
//   "Function Scope"
//     *.* (or try bulk.data if non-privileged)
//   "Listen to Location"
//     bulk.data.source
//   "Eventing Storage"
//     rr100.eventing.metadata
//   Binding(s)
//    1. "binding type", "alias name...", "bucket.scope.collection", "Access"
//       "bucket alias", "src_col",       "bulk.data.source",        "read and write"

function OnUpdate(doc, meta, xattrs) {
  if (meta.id.startsWith("lookupinfield:") === false) return;

  var meta = { "id": meta.id };
  var res;
  var opcnt = 1;

  res =
    couchbase.lookupIn(src_col, meta, [
      couchbase.LookupInSpec.get("<doc_path_0>", {"xattrs": false}),
      couchbase.LookupInSpec.get("<doc_path_1>")
    ]);
  log(opcnt++,res);
}
```

```json
INPUT: KEY lookupinfield:001

{
    "id": "lookupinfield:001",
}
```

```json
2024-03-15T14:42:53.314-07:00 [INFO] 1 {"meta":{"id":"lookupinfield:001","cas":"1710538973313433600"},"success":true}

2024-03-15T14:42:53.316-07:00 [INFO] 2 {"meta":{"id":"lookupinfield:001","cas":"1710538973315596288"},"success":true}

2024-03-15T14:42:53.317-07:00 [INFO] 3 {"meta":{"id":"lookupinfield:001","cas":"1710538973316841472"},"success":true}
```