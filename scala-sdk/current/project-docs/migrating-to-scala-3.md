---
title: Differences between Scala 2 and 3 SDK versions
description: The Scala 3 version of the SDK has some differences from the Scala 2 versions.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.11/modules/project-docs/pages/migrating-to-scala-3.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:scala-sdk:project-docs:migrating-to-scala-3.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/current/project-docs/migrating-to-scala-3.html)

# Differences between Scala 2 and 3 SDK versions

> The Scala 3 version of the SDK has some differences from the Scala 2 versions. But we expect the majority of Scala 2 applications will be able to migrate to Scala 3 and the Scala 3 version of the SDK with minimal or even no differences. 

If any of the following changes impact you as either an existing Scala 2 SDK user or an interested Scala 3 user, then please let us know. For some of these migrations we can offer alternative approaches, or discuss re-adding desired functionality.

The Scala 3 version of the SDK:

* Does not carry forward support for the Reactor API, as the Scala Reactor Extensions library that it depends on is long end-of-life. The `Future` API offers most of the same functionality while being considerably easier to use, and more Scala-centric. It is also easily adapted to other Scala libraries such as Cats Effect and ZIO.
* Does not carry forward the built-in support for JSON libraries (`Circe`, `json4s`, etc.), as this has increasingly become problematic to maintain as those libraries migrate to new majors.
* Does not carry forward support for views, analytics, replica reads, management operations, and datastructures.
* There are two overloads for most API methods, one that takes an options block, and one that tries to be a convenience method offering a few popular settings. The latter is removed in the Scala 3 version, significantly simplifying the API.