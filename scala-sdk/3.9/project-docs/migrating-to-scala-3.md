[View original HTML](/scala-sdk/3.9/project-docs/migrating-to-scala-3.html)

> The Scala 3 version of the SDK has some differences from the Scala 2 versions. But we expect the majority of Scala 2 applications will be able to migrate to Scala 3 and the Scala 3 version of the SDK with minimal or even no differences. 

If any of the following changes impact you as either an existing Scala 2 SDK user or an interested Scala 3 user, then please let us know. For some of these migrations we can offer alternative approaches, or discuss re-adding desired functionality.

The Scala 3 version of the SDK:

* Does not carry forward support for the Reactor API, as the Scala Reactor Extensions library that it depends on is long end-of-life. The `Future` API offers most of the same functionality while being considerably easier to use, and more Scala-centric. It is also easily adapted to other Scala libraries such as Cats Effect and ZIO.
* Does not carry forward the built-in support for JSON libraries (`Circe`, `json4s`, etc.), as this has increasingly become problematic to maintain as those libraries migrate to new majors.
* Does not carry forward support for views, analytics, replica reads, management operations, and datastructures.
* There are two overloads for most API methods, one that takes an options block, and one that tries to be a convenience method offering a few popular settings. The latter is removed in the Scala 3 version, significantly simplifying the API.