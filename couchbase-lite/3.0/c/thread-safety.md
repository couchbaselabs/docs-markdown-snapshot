---
title: Thread Safety
description: Couchbase mobile database thread safety concepts
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/c/pages/thread-safety.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@couchbase-lite:c:thread-safety.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/c/thread-safety.html)

# Thread Safety

> Description — _Couchbase mobile database thread safety concepts_  

The Couchbase Lite API is thread safe except for calls to mutable objects: `MutableDocument`, `MutableDictionary` and `MutableArray`.