---
title: Thread Safety
description: Couchbase mobile database API thread safety concepts
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/swift/pages/thread-safety.adoc
  xref: xref:2.8@couchbase-lite:swift:thread-safety.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/swift/thread-safety.html)

# Thread Safety

> Couchbase mobile database API thread safety concepts 

## [](#overview)Overview

The Couchbase Lite API is thread safe except for calls to mutable objects: `MutableDocument`, `MutableDictionary` and `MutableArray`.