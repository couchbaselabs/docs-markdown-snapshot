---
title: "Function: Advanced Sub-Document MUTATEIN Array Operation"
description: Perform the Advanced Sub-Document MUTATEIN operation on an array
  where Eventing interacts with the Data Service.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-handler-advancedMutateInArray.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:eventing:eventing-handler-advancedMutateInArray.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/eventing/eventing-handler-advancedMutateInArray.html)

# Function: Advanced Sub-Document MUTATEIN Array Operation

Perform the Advanced Sub-Document MUTATEIN operation on an array where Eventing interacts with the Data Service.

The `advancedMutateInArray` function:

* Demonstrates the CAS-free Sub-Document MUTATEIN operation on a document array field
* Requires Eventing Storage (or a metadata collection) and a source collection
* Requires a binding of type `bucket alias`
* Operates on any mutation where the `meta.id` or KEY is `combine_landmark_names`

For example, you can generate an input document with the KEY `combine_landmark_names` and the DATA `{ "id": "combine_landmark_names", "landmark_names": [] }`, then set the number of workers in the Eventing Function’s setting to 18\. Running the Function adds 4,495 landmark names to an array without conflict and in no particular order.

For more information about the Advanced Sub-Document MUTATEIN operation, see [Sub-Document MUTATEIN Operation](eventing-advanced-keyspace-accessors.md#advanced-subdoc-array-op-mutatein).

* advancedMutateInArray
* Input data before deployment
* Output data after deployment

```javascript
// Configure the settings for the advancedMutateInArray function as follows:
//
// Version 7.6+
//   "Function Scope"
//     *.* (or try bulk.data if non-privileged)
//   "Listen to Location"
//     travel-sample.inventory.landmark
//   "Eventing Storage"
//     rr100.eventing.metadata
//   Binding(s)
//    1. "binding type", "alias name...", "bucket.scope.collection", "Access"
//       "bucket alias", "dst_col",       "bulk.data.source",        "read and write"

function OnUpdate(doc, meta) {
 var accum_meta = {"id": "combine_landmark_names" };
 couchbase.mutateIn(dst_col, accum_meta, [
    couchbase.MutateInSpec.arrayAppend("landmark_names", doc.name),
  ]);
}
```

```json
INPUT: KEY combine_landmark_names

{
  "id": "combine_landmark_names",
  "landmark_names": []
}
```

```json
OUTPUT: KEY combine_landmark_names

{
  "id": "combine_landmark_names",
  "landmark_names": [
    "Gabriel's Wharf",
    "Blue Bear Performance Hall",
    "Circle Bar",
        *** 4490 lines removed ***
    "Quarry Bank Mill & Styal Estate",
    "Mad Cat Brewery",
    "Casbah Café"
  ]
}
```