---
title: "Function: Advanced GET Operation with Cache"
description: Perform the Advanced GET operation with cache where Eventing
  interacts with the Data Service.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/eventing/pages/eventing-handler-advancedGetOpWithCache.adoc
  xref: xref:server:eventing:eventing-handler-advancedGetOpWithCache.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/eventing/eventing-handler-advancedGetOpWithCache.html)

# Function: Advanced GET Operation with Cache

Perform the Advanced GET operation with cache where Eventing interacts with the Data Service.

The `advancedGetOpWithCache` function:

* Performs the Advanced GET operation with an enabled bucket-backed cache
* Requires Eventing Storage (or a metadata collection) and a source collection
* Requires a binding of type `bucket alias`
* Operates on any mutation where `doc.type === "test_adv_get"`
* Has an optional parameter to `couchbase.get` called `{ "cache": true }`, which enables caching of documents for up to 1 second

For more information about the Advanced Self-Recursion Parameter, see [Optional { "cache": true } Parameter](eventing-advanced-keyspace-accessors.md#optional-cache-true-parameter).

* advancedGetOpWithCache
* Input data
* Output data

```javascript
// Configure the settings for the advancedGetOpWithCache function as follows:
//
// Version 7.1+
//   "Function Scope"
//     *.* (or try bulk.data if non-privileged)
// Version 7.0.2+
//   "Listen to Location"
//     bulk.data.source
//   "Eventing Storage"
//     rr100.eventing.metadata
//   Binding(s)
//    1. "binding type", "alias name...", "bucket.scope.collection", "Access"
//       "bucket alias", "src_col",       "bulk.data.source",        "read and write"

function OnUpdate(doc, meta) {
    // filter out non-intersting documents
    if (!doc.type || doc.type !== "test_adv_get") return;
    log('input doc ', doc);
    log('input meta', meta);
    // let's read the same item and then try to read a non existent item
    var meta_ary = [{"id":"test_adv_get::1"}, {"id":"not_present::1"}];
    for (var i = 0; i < meta_ary.length; i++) {
        var result = couchbase.get(src_col,meta_ary[i],{"cache": true});
        if (result.success) {
            log('success adv. get with cache: result',result);
        } else {
            log('failure adv. get with cache: id',meta_ary[i].id,'result',result);
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
2021-10-04T15:54:31.101-07:00 [INFO] "input doc " {
	"id": 1,
	"type": "test_adv_get"
}
2021-10-04T15:54:31.101-07:00 [INFO] "input meta" {
	"cas": "1633388049399873536",
	"id": "test_adv_get::1",
	"expiration": 0,
	"flags": 33554438,
	"vb": 324,
	"seq": 3,
	"datatype": "json"
}
2021-10-04T15:54:31.102-07:00 [INFO] "success adv. get with cache: result" {
	"doc": {
		"id": 1,
		"type": "test_adv_get"
	},
	"meta": {
		"id": "test_adv_get::1",
		"cas": "1633388049399873536",
		"datatype": "json"
	},
	"success": true
}
2021-10-04T15:54:31.102-07:00 [INFO] "failure adv. get with cache: id" "not_present::1" "result" {
	"error": {
		"code": 1,
		"name": "LCB_KEY_ENOENT",
		"desc": "The document key does not exist on the server",
		"key_not_found": true
	},
	"success": false
}
```