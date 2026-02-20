---
title: JSON Libraries
description: The Scala SDK supports multiple options for working with JSON.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.10/modules/howtos/pages/json.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.10@scala-sdk:howtos:json.adoc[]
---

[View original HTML](/scala-sdk/3.10/howtos/json.html)

# JSON Libraries

> The Scala SDK supports multiple options for working with JSON. 

The Couchbase Server is a key-value store that’s agnostic to what’s stored, but it’s very common to store JSON.

## [](#philosophy)Philosophy

The Scala SDK has these main objectives for JSON:

* Be usable 'out-of-the-box'. A simple JSON library is included, so you can get started right away. Bonus: it’s simple to use and very fast!
* Be agnostic. Your application may already be using its own JSON representation, and it shouldn’t be forced to use the built-in JSON library.
* Be inclusive. There’s a wide range of great, popular JSON libaries for the JVM, and we’ve supported many of them directly. That is, you can use types from the [Circe library](https://circe.github.io/circe/), and many others, when doing any operation. And if we’re missing support for your favourite, then please let us know on the [forums](http://forums.couchbase.com/).

> [!NOTE]
> The Scala 3 version of the SDK does not carry forward direct support for the external JSON libraries, though it remains easy to integrate with them. Please see [Migrating to Scala 3](../project-docs/migrating-to-scala-3.md) for guidance on these and other changes.

## [](#optional-dependencies)Optional Dependencies

Dependencies on third-party JSON libraries are performed with Maven’s `optional` scope. This means that if you have the Circe dependency in your _own_ project (be it SBT, Gradle or Maven based), then you will be able to use the Circe types with the Scala SDK. But the SDK will not pull in the dependency itself, to stay lean and mean.

## [](#getting-started)Getting Started

The examples below assume you’re familiar with connecting to a Couchbase cluster using the Scala SDK, and opening resources. Please check out [the Getting Started guide](#hello-world:start-using-sdk) for help with this.

In the examples below we’ll use the following case classes:

```scala
case class Address(address: String)
case class User(name: String, age: Int, addresses: Seq[Address])

val user = User("John Smith", 29, List(Address("123 Fake Street")))
```

Let’s dive into some practical examples of the many ways you can use JSON with the Couchbase Scala SDK.

## [](#circe)Circe

[Circe](https://circe.github.io/circe/) has the very useful property of being able to encode case classes directly to and from Circe data types, without having to write the 'codec' logic usually required for this.

Here’s an example of how to use Circe with Couchbase:

```scala
import io.circe.generic.auto._
import io.circe.syntax._

// Circe can encode case classes directly to its `Json` type, with no codec code required
val json: io.circe.Json = user.asJson

// Can provide Circe types for all mutation operations
val result1: Try[MutationResult] = collection.insert("id", json)

result1 match {
  case Success(_) =>
    val result2: Try[GetResult] = collection.get("id")

    result2 match {
      case Success(doc) =>
        // Can retrieve document content as Circe types
        val content: Try[io.circe.Json] = doc.contentAs[io.circe.Json]

      case Failure(err) => println(s"Error: ${err}")
    }

  case Failure(err) => println(s"Error: ${err}")
}
```

That works, but it’s very verbose to handle all those `Try` one-by-one. Here’s an example of how to do the same thing, but chaining all the `Try` together using `flatMap`:

```scala
import io.circe.generic.auto._
import io.circe.syntax._

val json: io.circe.Json = user.asJson

val result: Try[io.circe.Json] = collection.insert("id", json)
    .flatMap(_ => collection.get("id"))
    .flatMap(doc => doc.contentAs[io.circe.Json])
```

And finally the same thing again, but this time using a for-comprehension:

```scala
import io.circe.generic.auto._
import io.circe.syntax._

val json: io.circe.Json = user.asJson

val result: Try[io.circe.Json] = for {
  _       <- collection.insert("id", json)
  doc     <- collection.get("id")
  content <- doc.contentAs[io.circe.Json]
} yield content
```

If for-comprehensions are unfamiliar then they’re essentially syntactic sugar, with each of the `←` being a `flatMap` call.

Examples below will use the for-comprehension style, for brevity.

## [](#µpickle-µjson)µPickle / µJson

[µPickle](http://www.lihaoyi.com/upickle/) is a serialization library with its own JSON library, µJson.

Unlike the majority of JSON Scala libraries, µJson is mutable, with the [author’s rationale](http://www.lihaoyi.com/post/uJsonfastflexibleandintuitiveJSONforScala.html) an interesting read.

Here’s an example of how to use µJson with Couchbase:

```scala
val content = ujson.Obj("name" -> "John Smith",
  "age" -> 29,
  "addresses" -> ujson.Arr(
    ujson.Obj("address" -> "123 Fake Street")
  ))

val result: Try[ujson.Obj] = for {
  // Can provide upickle types for all mutation operations
  _       <- collection.insert("id", content)
  doc     <- collection.get("id")

  // Can retrieve document content as upickle types
  content <- doc.contentAs[ujson.Obj]
} yield content
```

## [](#jsonobject-and-jsonarray)JsonObject and JsonArray

The SDK includes a built-in JSON library, `JsonObject`. Its main goals are:

* Convenience. Not everyone wants to evaluate multiple JSON libraries before getting started. JsonObject is a decent default choice.
* Speed. Our internal benchmarking indicates `JsonObject` is up to 20 times faster than the nearest Scala JSON library on some important operations. It achieves this mostly by being built around simple, but very fast, mutable JVM data structures. Unlike the rest of the SDK, it also throws exceptions rather than incur the small cost on the good path of functional-style error handling (e.g. `Try`) — though there is an optional alternative [JsonObjectSafe](#error-handling-and-jsonobjectsafe) interface that does provide `Try`.
* Ease-of-use and mutability. We find ourselves in agreement with [the author of µJson](http://www.lihaoyi.com/post/uJsonfastflexibleandintuitiveJSONforScala.html), that though immutability is usually desirable, it’s actually not always the best choice for JSON. Dealing with deeply nested JSON requires functional tools such as lenses, which are rarely easy to read, not to mention incurring a performance penalty. And JSON is most often dealt with briefly and in a limited scope (e.g. getting and modifying a document), so rarely benefits from the safety of immutability. So `JsonObject` presents a simple mutable API.

Of course, if you’d rather have a JSON library with immutable data, lenses, cursors and other functional goodies, then one of the other options on this page may be a better choice.

### [](#creating)Creating

Using `JsonObject` here’s how to create some simple JSON:

```scala
val json = JsonObject("name" -> "Eric Wimp",
  "age" -> 9,
  "addresses" -> JsonArray(JsonObject("address" -> "29 Acacia Road")))

val str = json.toString()
// """{"name":"Eric Wimp","age":9,"addresses":[{"address","29 Acacia Road"}]}"""
```

As `JsonObject` and `JsonArray` are both mutable, they can also be created this way:

```scala
val obj = JsonObject.create.put("name", "Eric Wimp")
obj.put("age", 9)
val arr = JsonArray.create
arr.add(JsonObject("address" -> "29 Acacia Road"))
obj.put("addresses", arr)
```

### [](#retrieving-data)Retrieving Data

It’s easy to retrieve data:

```scala
json.str("name") // "Eric Wimp"
json.arr("addresses").obj(0).str("address") // "29 Acacia Road"
```

Or, using a feature of Scala called `Dynamic`, you can use an alternative syntax like this:

```scala
json.dyn.name.str // "Eric Wimp"
json.dyn.addresses(0).address.str // "29 Acacia Road"
```

### [](#using-with-key-value-operations)Using with Key-Value Operations

As with the other supported JSON libraries, `JsonObject` (and `JsonArray`) can easily be used directly with any SDK operation:

```scala
val json = JsonObject("name" -> "Eric Wimp",
  "age" -> 9,
  "addresses" -> JsonArray(JsonObject("address" -> "29 Acacia Road")))

val result: Try[JsonObject] = for {
  // Can provide JsonObject for all mutation operations
  _       <- collection.insert("id", json)
  doc     <- collection.get("id")

  // Can retrieve document content as JsonOject (and JsonObjectSafe)
  content <- doc.contentAs[JsonObject]
} yield content
```

### [](#error-handling-and-jsonobjectsafe)Error Handling and JsonObjectSafe

The majority of the Scala SDK will not throw exceptions. Methods on `JsonObject` are an exception to this general rule. If a requested field does not exist a `NoSuchElementException` will be thrown.

If you’d rather not deal with exceptions, `JsonObject` comes with a counterpart `JsonObjectSafe` that provides an alternative interface in which all methods return Scala `Try` rather than throwing:

```scala
val safe: JsonObjectSafe = json.safe

val r: Try[String] = safe.str("name")

r match {
  case Success(name) => println(s"Their name is $name")
  case Failure(err) => println(s"Could not find field 'name': $err")
}
```

A `JsonArraySafe` counterpart also exists.

If you’re walking through JSON it can be useful to use flatMap or for-comprehensions for readability:

```scala
val address: Try[String] = for {
  addresses <- safe.arr("addresses")
  address   <- addresses.obj(0)
  line      <- address.str("address")
} yield line
```

or use the support for `Dynamic` to combine brevity with safety:

```scala
val add: Try[String] = safe.dyn.addresses(0).address.str
```

Note that `JsonObjectSafe`, though presenting a more functional interface, is still mutable.

## [](#case-classes)Case Classes

It can be very useful to deal directly with Scala case classes, that is to send and retrieve them directly rather than via some interim type, and the Scala SDK includes built-in support for this.

> [!NOTE]
> The Scala 3 version of the SDK does not carry forward direct support for case classes, though it remains easy to use them directly via libraries such as `Jsoniter` and `Circe`. Please contact us if this is functionality that is useful to you.

It’s necessary to write a small amount of boilerplate code first. If you try and insert a case class directly, you’ll get an error. E.g. this won’t work:

```scala
    val user = User("Eric Wimp", 9, Seq(Address("29 Acacia Road")))

    // Will fail to compile
    collection.insert("eric-wimp", user) 
```

This is because the Scala SDK does not currently know how to convert a `User` into JSON that it can send to the server.

More technically, methods like `insert` that take content of type `T` also take an implicit `JsonSerializer[T]`, which defines how to turn `T` into JSON. If the Scala compiler cannot find a suitable `JsonSerializer[T]`, then it will report an error.

So, let’s provide an `JsonSerializer[User]`. It’s possible to create one manually, but the Scala SDK includes a convenient shortcut:

```scala
object User {
  implicit val codec: Codec[User] = Codec.codec[User]
}
```

(As this is a companion object for User, it needs to go in the same file as the `User` case class you added earlier.)

This short line of boilerplate uses Scala macros to, at compile time, provide a `JsonSerializer[User]`. Note that we don’t need one for `Address` too — only the top-level case classes you’re dealing with need a `Codec`.

Now we can pass a `User` directly to `insert`, and it will work fine. The Scala compiler will look for a `JsonSerializer[User]` in a number of places, and find it in the `User` companion object.

Since the encoding logic is generated at compile time it can also be extremely fast — no reflection is used.

The generated JSON will be as you expect, with "name" and "age" fields, and an "addresses" array.

The same `Codec` also generates a `JsonDeserializer[User]`, which can be used to pull data out as our case class, using `contentAs`:

```scala
    val r: Try[User] = for {
      doc <- collection.get("eric-wimp")
      user <- doc.contentAs[User]
    } yield user

    r match {
      case Success(user: User) => println(s"User: ${user}")
      case Failure(err)        => println("Error: " + err)
    }
```

> [!NOTE]
> There are other ways to handle case classes. Many of the supported JSON libraries have some method to encode and decode case classes into an interim type, as in the [Circe example](#circe).

## [](#json4s)Json4s

[Json4s](http://json4s.org/) aims to provide a single JSON representation that can be used by other JSON libraries.

Here’s an example of how to use `Json4s` with Couchbase:

```scala
import org.json4s.JsonAST._
import org.json4s.JsonDSL._

val json: JValue =
  ("name" -> "John Smith") ~
    ("age" -> 29) ~
    ("addresses" -> List(
      "address" -> "123 Fake Street")
      )

val result: Try[JValue] = for {
  // Can provide Json4s types for all mutation operations
  _ <- collection.insert("id", json)
  doc <- collection.get("id")

  // Can retrieve document content as Json4s types
  content <- doc.contentAs[JValue]
} yield content
```

## [](#jawn)Jawn

Here’s an example of how to use [Jawn](https://github.com/typelevel/jawn) with Couchbase:

```scala
import org.typelevel.jawn.ast._

val json = JObject.fromSeq(Seq("name" -> JString("John Smith"),
  "age" -> JNum(29),
  "address" -> JArray.fromSeq(Seq(JObject.fromSeq(Seq("address" -> JString("123 Fake Street")))))))

val result: Try[JValue] = for {
  // Can provide Jawn types for all mutation operations
  _       <- collection.insert("id", json)
  doc     <- collection.get("id")

  // Can retrieve document content as Jawn types
  content <- doc.contentAs[JValue]
} yield content
```

## [](#play-json)Play JSON

Here’s an example of how to use [Play Json](https://github.com/playframework/play-json) with Couchbase:

```scala
import play.api.libs.json.Json._
import play.api.libs.json._

val json = obj("name" -> "John Smith",
  "age" -> 29,
  "address" -> arr(obj("address" -> "123 Fake Street")))

val result: Try[JsValue] = for {
  // Can provide Play JSON types for all mutation operations
  _       <- collection.insert("id", json)
  doc     <- collection.get("id")

  // Can retrieve document content as Play JSON types
  content <- doc.contentAs[JsValue]
} yield content
```

## [](#strings)Strings

It’s possible to send and receive JVM `String` directly:

```scala
val json = """{"hello":"world"}"""

val result: Try[String] = for {
  // Can provide Play JSON types for all mutation operations
  _       <- collection.insert("id", json)
  doc     <- collection.get("id")

  // Can retrieve document content as String
  content <- doc.contentAs[String]
} yield content
```

## [](#arraybyte)Array\[Byte\]

And an `Array[Byte]` can be used directly:

```scala
val json: Array[Byte] = """{"hello":"world"}""".getBytes(StandardCharsets.UTF_8)

val result: Try[Array[Byte]] = for {
  // Can provide Play JSON types for all mutation operations
  _       <- collection.insert("id", json)
  doc     <- collection.get("id")

  // Can retrieve document content as String
  content <- doc.contentAs[Array[Byte]]
} yield content
```

With the support for `String` and `Array[Byte]`, the Scala SDK can be used with any JSON library that can import and export those formats.

## [](#adding-another-type)Adding Another Type

As alluded to above, when inserting a `T`, the Scala SDK looks for an `JsonSerializer[T]` in implicit scope. Similar for `contentAs` and `JsonDeserializer[T]`.

For advanced users it’s possible to support any type desired by simply writing an `JsonSerializer` and/or `JsonDeserializer` for that type. Please see the code of those interfaces for details.

## [](#choosing-a-library)Choosing a Library

We’ve looked at multiple options for working with JSON — but which one should you choose?

In truth, they all fulfill different needs, provide different tradeoffs, and any of them can be a good option in certain situations. You may want to evaluate and benchmark them with representative data to see which fits your situation best.

If you’re not already using a JSON library, then the built-in `JsonObject` library is very fast, very simple to use, and makes a good default choice.