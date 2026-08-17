---
title: "Function: Advanced GET operation (with cache)"
description: Perform the Advanced GET operation where Eventing interacts with
  the Data service.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/eventing/pages/eventing-handler-advancedGetOpWithCache.adoc
  xref: xref:7.2@server:eventing:eventing-handler-advancedGetOpWithCache.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/eventing/eventing-handler-advancedGetOpWithCache.html)

# Function: Advanced GET operation (with cache)

Couchbase Server 7.0.2 **Goal**: Perform the Advanced GET operation where Eventing interacts with the Data service.

* This function **advancedGetOpWithCache** merely demonstrates the Advanced GET operation with Bucket Backed Cache enabled.
* Requires Eventing Storage (or metadata collection) and a "source" collection.
* Needs a Binding of type "bucket alias" (as documented in the Scriptlet).
* Will operate on any mutation where doc.type === "test\_adv\_get".
* The optional third parameter to couchbase.get of **{"cache": true}** enables caching of documents for up to 1 second.
* This RYOW caching is 18X-25X faster than reading near static data directly from the Data Service (or KV).
* For more information refer to [Advanced GET operation](eventing-advanced-keyspace-accessors.md#advanced-get-op) in the detailed documentation.

* advancedGetOpWithCache
* Input Data/Mutation
* Output Data/Logged

```javascript
// To run configure the settings for this Function, advancedGetOpWithCache, as follows:
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