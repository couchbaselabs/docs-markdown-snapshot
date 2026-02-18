---
title: "Function: Advanced Sub-Document MUTATEIN Operation"
description: Perform the Advanced Sub-Document MUTATEIN operation on a field
  where Eventing interacts with the Data Service.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-handler-advancedMutateInField.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/eventing/eventing-handler-advancedMutateInField.html)

# Function: Advanced Sub-Document MUTATEIN Operation

Perform the Advanced Sub-Document MUTATEIN operation on a field where Eventing interacts with the Data Service.

The `advancedMutateInField` function:

* Demonstrates the CAS-free Sub-Document MUTATEIN operation on a document field
* Requires Eventing Storage (or a metadata collection) and a source collection
* Requires a binding of type `bucket alias`
* Operates on any mutation where the `meta.id` or KEY starts with `mutateinfield:`

For more information about the Advanced Sub-Document MUTATEIN operation , see [Sub-Document MUTATEIN Operation](eventing-advanced-keyspace-accessors.md#advanced-subdoc-array-op-mutatein).

* advancedMutateInField
* Input data
* Output data

```javascript
// Configure the settings for the advancedMutateInField function as follows:
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

function OnUpdate(doc, meta) {
  if (meta.id.startsWith("mutateinfield:") === false) return;

  var meta = { "id": meta.id };
  var res;
  var opcnt = 1;

  res =
    couchbase.mutateIn(src_col, meta, [
      couchbase.MutateInSpec.insert("testField", "insert")
    ]);
  log(opcnt++,res);

  res =
    couchbase.mutateIn(src_col, meta, [
      couchbase.MutateInSpec.replace("testField", "replace")
    ]);
  log(opcnt++,res);

  res =
    couchbase.mutateIn(src_col, meta, [
      couchbase.MutateInSpec.remove("testField")
    ]);
  log(opcnt++,res);
}
```

```json
INPUT: KEY mutateinfield:001

{
    "id": "mutateinfield:001",
}
```

```json
2024-03-15T14:42:53.314-07:00 [INFO] 1 {"meta":{"id":"mutateinfield:001","cas":"1710538973313433600"},"success":true}

2024-03-15T14:42:53.316-07:00 [INFO] 2 {"meta":{"id":"mutateinfield:001","cas":"1710538973315596288"},"success":true}

2024-03-15T14:42:53.317-07:00 [INFO] 3 {"meta":{"id":"mutateinfield:001","cas":"1710538973316841472"},"success":true}
```