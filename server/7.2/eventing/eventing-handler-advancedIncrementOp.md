---
title: "Function: Advanced INCREMENT operation"
description: Perform the Advanced INCREMENT operation where Eventing interacts
  with the Data service.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/eventing/pages/eventing-handler-advancedIncrementOp.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/eventing/eventing-handler-advancedIncrementOp.html)

# Function: Advanced INCREMENT operation

**Goal**: Perform the Advanced INCREMENT operation where Eventing interacts with the Data service.

* This function **advancedIncrementOp** merely demonstrates the Advanced INCREMENT operation.
* Requires Eventing Storage (or metadata collection) and a "source" collection.
* Needs a Binding of type "bucket alias" (as documented in the Scriptlet).
* Will operate on any mutation and count the mutations subject to DCP dedup.
* For more information refer to [Advanced INCREMENT operation](eventing-advanced-keyspace-accessors.md#advanced-increment-op) in the detailed documentation.

* advancedIncrementOp
* Input Data/Mutation
* Output Data
* Output Log

```javascript
// To run configure the settings for this Function, advancedIncrementOp, as follows:
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
    if (!meta.id.startsWith("inc:")) return;
    // log('input meta', meta);
    // log('input doc ', doc);

    // if doc.count doesn't exist it will be created
    var ctr_meta = {"id": "my_atomic_counter:1" };
    var result = couchbase.increment(src_col,ctr_meta);
    if (result.success) {
        log('success adv. increment: result',result);
    } else {
        log('failure adv. increment: id',ctr_meta.id,'result',result);
    }
}
```

```json
UPSERT INTO `bulk`.`data`.`source` (KEY,VALUE)
  VALUES ( "inc:1",  {"somekey":"someValue"} ),
  VALUES ( "inc:2",  {"somekey":"someValue"} ),
  VALUES ( "inc:3",  {"somekey":"someValue"} ),
  VALUES ( "inc:4",  {"somekey":"someValue"} ),
  VALUES ( "inc:5",  {"somekey":"someValue"} ),
  VALUES ( "inc:6",  {"somekey":"someValue"} ),
  VALUES ( "inc:7",  {"somekey":"someValue"} ),
  VALUES ( "inc:8",  {"somekey":"someValue"} ),
  VALUES ( "inc:9",  {"somekey":"someValue"} ),
  VALUES ( "inc:10", {"somekey":"someValue"} );
```

We insert ten (10) documents and count the mutations

```json
KEY: my_atomic_counter:1

{
  "count": 10
}
```

```json
2021-01-08T12:30:59.910-08:00 [INFO] "success adv. increment: result"
{"doc":{"count":1},"meta":{"id":"my_atomic_counter:1","cas":"1610137859908960256"},"success":true}

2021-01-08T12:30:59.910-08:00 [INFO] "success adv. increment: result"
{"doc":{"count":2},"meta":{"id":"my_atomic_counter:1","cas":"1610137859909222400"},"success":true}

2021-01-08T12:30:59.911-08:00 [INFO] "success adv. increment: result"
{"doc":{"count":3},"meta":{"id":"my_atomic_counter:1","cas":"1610137859911385088"},"success":true}

2021-01-08T12:30:59.931-08:00 [INFO] "success adv. increment: result"
{"doc":{"count":4},"meta":{"id":"my_atomic_counter:1","cas":"1610137859929997312"},"success":true}

2021-01-08T12:30:59.931-08:00 [INFO] "success adv. increment: result"
{"doc":{"count":5},"meta":{"id":"my_atomic_counter:1","cas":"1610137859930193920"},"success":true}

2021-01-08T12:30:59.932-08:00 [INFO] "success adv. increment: result"
{"doc":{"count":6},"meta":{"id":"my_atomic_counter:1","cas":"1610137859932160000"},"success":true}

2021-01-08T12:30:59.932-08:00 [INFO] "success adv. increment: result"
{"doc":{"count":7},"meta":{"id":"my_atomic_counter:1","cas":"1610137859932356608"},"success":true}

2021-01-08T12:30:59.948-08:00 [INFO] "success adv. increment: result"
{"doc":{"count":8},"meta":{"id":"my_atomic_counter:1","cas":"1610137859946381312"},"success":true}

2021-01-08T12:30:59.948-08:00 [INFO] "success adv. increment: result"
{"doc":{"count":9},"meta":{"id":"my_atomic_counter:1","cas":"1610137859946708992"},"success":true}

2021-01-08T12:30:59.948-08:00 [INFO] "success adv. increment: result"
{"doc":{"count":10},"meta":{"id":"my_atomic_counter:1","cas":"1610137859948412928"},"success":true}
```