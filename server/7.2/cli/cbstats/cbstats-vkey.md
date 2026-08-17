---
title: vkey
description: Provides verification for keys.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cli/pages/cbstats/cbstats-vkey.adoc
  xref: xref:7.2@server:cli:cbstats/cbstats-vkey.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/cli/cbstats/cbstats-vkey.html)

# vkey

> Provides verification for keys. 

## [](#syntax)Syntax

cbstats host:11210 [common options] vkey <keyname> <vbid>
  [ <scope>.<collection> | id <collectionID> ]

## [](#options)Options

For common `cbstats` options, see the [cbstats](../cbstats-intro.md) reference page. Command-specific options are as follows:

| Option               | Description                                                                                                                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| vkey <keyname>       | Name of the key.                                                                                                                                                                                              |
| <vbid>               | vBucket ID. To find the vBucket ID associated with a given key, use the cbc-hash command; which is available as part of the Couchbase C SDK (libcouchbase). Examples are provided [below](#find-vbucket-ids). |
| <scope>.<collection> | The scope and collection that contain the key.                                                                                                                                                                |
| id <collectionID>    | The id of the collection that contains the key. For information on retrieving the id of a collection, see the cbstats [collections](cbstats-collections.md) reference page.                                   |

## [](#responses)Responses

Responses contain the following information:

| Stat              | Value                                                 |
| ----------------- | ----------------------------------------------------- |
| key\_cas          | The key's current _cas_ value, as a decimal integer.  |
| key\_exptime      | Expiration time from the epoch, as a decimal integer. |
| key\_flags        | Flags for this key, as a decimal integer.             |
| key\_is\_dirty    | Whether the value is not yet persisted.               |
| key\_is\_resident | Whether the value is resident in memory.              |
| key\_valid        | See the description immediately below this table.     |
| key\_vb\_state    | The vBucket state of this key.                        |

Note that `key_valid` can have any of the following values:

* `this_is_a_bug`. An error has occurred.
* `dirty`. The value in memory has not been persisted yet.
* `length_mismatch`. The key length in memory does not match the length on the disk.
* `data_mismatch`. The data in memory does not match the data on disk.
* `flags_mismatch`. The flags in memory do not match the flags on disk.
* `valid`. The key is both on disk and in memory.
* `ram_but_not_disk`. The value does not yet exist on disk.
* `item_deleted`. The item has been deleted.

## [](#find-vbucket-ids)Examples: Find vBucket IDs

Using `cbc-hash`, the following call searches for the vBucket ID that corresponds to the key `airline_10`; which is provided by default, in the sample bucket `travel-sample`:

/opt/couchbase/bin/cbc-hash airline_10 \
-U couchbase://localhost/travel-sample \
-u Administrator -P password

The response is as follows:

airline_10: [vBucket=361, Index=0] Server: localhost:11210, CouchAPI: http://localhost:8092/travel-sample

The response thus indicates that the document with the key `airline_10` resides in the vBucket whose id is `361`.

The following call searches for the key of a custom-created document, saved by the administrator in the sample bucket `travel-sample`:

/opt/couchbase/bin/cbc-hash newTestDoc \
-U couchbase://localhost/travel-sample \
-u Administrator -P password

The response is as follows:

newTestDoc: [vBucket=4, Index=0] Server: localhost:11210, CouchAPI: http://localhost:8092/travel-sample

The response thus indicates that the document with the key `newTestDoc` resides in the vBucket whose id is 4.

## [](#examples-get-vkey-information)Examples: Get vKey Information

vKey information can be retrieved either by specifying the bucket; or by additionally specifying either a collection or both a scope and a collection, within the bucket.

### [](#get-vkey-information-specifying-bucket)Get vKey Information, Specifying Bucket

The following call requests information on the vkey `airline_10`, contained in the vBucket whose id is `361`:

/opt/couchbase/bin/cbstats -u Administrator -p password \
-b travel-sample localhost:11210 \
vkey 'airline_10' 361

The response is as follows:

verification for key airline_10
 key_cas:         1601426228785053696
 key_exptime:     0
 key_flags:       100663298
 key_is_dirty:    false
 key_is_resident: true
 key_valid:       data_mismatch
 key_vb_state:    active

### [](#get-vkey-information-specifying-bucket-scope-and-collection)Get vKey Information, Specifying Bucket, Scope, and Collection

The following example requests information on the key `airline_10`, which is provided by default in the sample bucket `travel-sample`. The call uses the `<scope>.<collection>` option, to specify that the default scope and collection should be searched:

/opt/couchbase/bin/cbstats -u Administrator -p password \
-b travel-sample localhost:11210 \
vkey 'airline_10' 361 _default._default

The response is as follows:

verification for key airline_10
 key_cas:         1601426228785053696
 key_exptime:     0
 key_flags:       100663298
 key_is_dirty:    false
 key_is_resident: true
 key_valid:       data_mismatch
 key_vb_state:    active

The following example, again using the `<scope>.<collection>` option, requests information on the key `newTestDoc`, contained in the administrator-created collection `MyCollection`; which is in the administrator-created scope `MyScope`, in the `travel-sample` bucket.

/opt/couchbase/bin/cbstats -u Administrator -p password \
-b travel-sample localhost:11210 \
vkey 'newTestDoc' 4 MyScope.MyCollection

The response is as follows:

verification for key newTestDoc
 key_cas:         1602139598762409984
 key_exptime:     0
 key_flags:       100663298
 key_is_dirty:    false
 key_is_resident: true
 key_valid:       valid
 key_vb_state:    active

### [](#get-key-information-specifying-collection-id)Get Key Information, Specifying Collection ID

The following example requests information on the key `airline_10`, which is provided by default in the sample bucket `travel-sample`. The call uses the `id <collectionID>` option, to specify that the default collection should be searched:

/opt/couchbase/bin/cbstats -u Administrator -p password \
-b travel-sample localhost:11210 \
vkey 'airline_10' 361 id 0x0

The response is as follows:

verification for key airline_10
 key_cas:         1601426228785053696
 key_exptime:     0
 key_flags:       100663298
 key_is_dirty:    false
 key_is_resident: true
 key_valid:       data_mismatch
 key_vb_state:    active

The following example, again using the `id <collectionID>` option, requests information on the key `newTestDoc`, contained in the administrator-created collection `MyCollection`, in the `travel-sample` bucket.

/opt/couchbase/bin/cbstats -u Administrator -p password \
-b travel-sample localhost:11210 \
vkey 'newTestDoc' 4 id 0x9

The response is as follows:

verification for key newTestDoc
 key_cas:         1602139598762409984
 key_exptime:     0
 key_flags:       100663298
 key_is_dirty:    false
 key_is_resident: true
 key_valid:       valid
 key_vb_state:    active

## [](#see-also)See Also

For an overview of scopes and collections, see [Scopes and Collections](../../learn/data/scopes-and-collections.md). To use `cbstats` to provide information on collections, see the reference page for the `cbstats` [collections](cbstats-collections.md) command. For information on providing information on keys, see the reference page for the `cbstats` [key](cbstats-key.md) command.