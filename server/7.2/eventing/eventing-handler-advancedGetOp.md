---
title: "Function: Advanced GET operation"
description: Perform the Advanced GET operation where Eventing interacts with
  the Data service.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/eventing/pages/eventing-handler-advancedGetOp.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:eventing:eventing-handler-advancedGetOp.adoc[]
---

[View original HTML](/server/7.2/eventing/eventing-handler-advancedGetOp.html)

# Function: Advanced GET operation

**Goal**: Perform the Advanced GET operation where Eventing interacts with the Data service.

* This function **advancedGetOp** merely demonstrates the Advanced GET operation.
* Requires Eventing Storage (or metadata collection) and a "source" collection.
* Needs a Binding of type "bucket alias" (as documented in the Scriptlet).
* Will operate on any mutation where doc.type === "test\_adv\_get".
* For more information refer to [Advanced GET operation](eventing-advanced-keyspace-accessors.md#advanced-get-op) in the detailed documentation.

* advancedGetOp
* Input Data/Mutation
* Output Data/Logged

```javascript
// To run configure the settings for this Function, advancedGetOp, as follows:
//
// Version 7.1+
//   "Function Scope"
//     *.* (or try bulk.data if non-privileged)
// Version 7.0+
//   "Listen to Location"
//     bulk.data.source
//   "Eventing Storage"
//     rr100.eventing.metadata
//   Binding(s)
//    1. "binding type", "alias name...", "bucket.scope.collection", "Access"
//       "bucket alias", "src_col",       "bulk.data.source",        "read and write"
//
// Version 6.6.1
//   "Source Bucket"
//     source
//   "MetaData Bucket"
//     metadata
//   Binding(s)
//    1. "binding type", "alias name...", "bucket",     "Access"
//       "bucket alias", "src_col",       "source",     "read and write"

function OnUpdate(doc, meta) {
    // filter out non-intersting documents
    if (!doc.type || doc.type !== "test_adv_get") return;
    log('input doc ', doc);
    log('input meta', meta);
    // let's read the same item and then try to read a non existent item
    var meta_ary = [{"id":"test_adv_get::1"}, {"id":"not_present::1"}];
    for (var i = 0; i < meta_ary.length; i++) {
        var result = couchbase.get(src_col,meta_ary[i]);
        if (result.success) {
            log('success adv. get: result',result);
        } else {
            log('failure adv. get: id',meta_ary[i].id,'result',result);
        }
    }
}
```

```json
INPUT: KEY test_adv_get::1

{
    "id": 1,
    "type": "test_adv_get"
}
```

```json
2021-01-07T07:57:24.706-08:00 [INFO] "input doc "
{
    "id": 1,
    "type": "test_adv_get"
}
2021-01-07T07:57:24.706-08:00 [INFO] "input meta"
{
    "cas": "1610034762747412480",
    "id": "test_adv_get::1",
    "expiration": 0,
    "flags": 33554438,
    "vb": 324,
    "seq": 1
}
2021-01-07T07:57:24.707-08:00 [INFO] "success adv. get: result"
{
    "doc": {
        "id": 1,
        "type": "test_adv_get"
    },
    "meta": {
        "id": "test_adv_get::1",
        "cas": "1610034762747412480",
        "data_type": "json"
    },
    "success": true
}
2021-01-07T07:57:24.707-08:00 [INFO] "failure adv. get: id" "not_present::1" "result"
{
    "error": {
        "code": 272,
        "name": "LCB_KEY_ENOENT",
        "desc": "The document key does not exist on the server",
        "key_not_found": true
    },
    "success": false
}
```