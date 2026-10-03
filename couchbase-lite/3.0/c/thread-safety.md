---
title: Thread Safety
description: Couchbase mobile database thread safety concepts
pubDate: 2026-10-03T04:27:21.374Z
meta:
  component:
    title: Couchbase Lite
    version: "3.0"
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/c/pages/thread-safety.adoc
  xref: xref:3.0@couchbase-lite:c:thread-safety.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/c/thread-safety.html)

# Thread Safety

> Description — _Couchbase mobile database thread safety concepts_  

The Couchbase Lite API is thread safe except for calls to mutable objects: `MutableDocument`, `MutableDictionary` and `MutableArray`.