---
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/android/pages/thread-safety.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:android:thread-safety.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/android/thread-safety.html)

# undefined

## [](#thread-safetydata-model)Thread Safety — Data Model

> Description — _Couchbase database data model api thread safety_  
> Related Content — [Databases](../../current/android/database.md) | [Documents](../../current/android/document.md) | [Indexing](../../current/android/indexing.md) |

The Couchbase Lite API is thread safe except for calls to mutable objects: `MutableDocument`, `MutableDictionary` and `MutableArray`.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/android/gs-prereqs.md)
* [Install](../../current/android/gs-install.md)
* [Build and Run](../../current/android/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/android/database.md)
* [Documents](../../current/android/document.md)
* [Blobs](../../current/android/blob.md)
* [Remote Sync using Sync Gateway](../../current/android/replication.md)
* [Handling Data Conflicts](../../current/android/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)