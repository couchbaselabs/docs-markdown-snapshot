---
title: Thread Safety
description: Couchbase mobile database thread safety concepts
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/csharp/pages/thread-safety.adoc
  xref: xref:2.8@couchbase-lite:csharp:thread-safety.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/csharp/thread-safety.html)

# Thread Safety

> Couchbase mobile database thread safety concepts 

The Couchbase Lite API is thread safe except for calls to mutable objects: `MutableDocument`, `MutableDictionary` and `MutableArray`.