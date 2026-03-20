---
title: Transcoders &amp; Non-JSON Documents
description: The Scala SDK supports common JSON document requirements out-of-the-box.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.11/modules/howtos/pages/transcoders-nonjson.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:scala-sdk:howtos:transcoders-nonjson.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/current/howtos/transcoders-nonjson.html)

# Transcoders &amp; Non-JSON Documents

> The Scala SDK supports common JSON document requirements out-of-the-box. Custom transcoders and serializers provide support for applications needing to perform advanced operations, including supporting non-JSON data. 

The Scala SDK uses the concepts of transcoders and serializers, which are used whenever data is sent to or retrieved from Couchbase Server.

When sending data to Couchbase, the SDK passes the object being sent to a transcoder. The transcoder can either reject the object as being unsupported, or convert it into a `byte[]` and a Common Flag. The Common Flag specifies whether the data is JSON, a non-JSON string, or raw binary data. It may, but does not have to, use a serializer to perform the byte conversion.

Serializers are discovered at compile-time: if the application is sending type `T`, the compiler will look for a `JsonSerializer[T]`. Similarly when the application is receiving data to a desired type `T`, the compiler will look for a `JsonDeserializer[T]`. There are JsonSerializer and JsonDeserializer implementations provided for many types, including several popular third-party JSON libraries, and it is easy to add more.

On retrieving data from Couchbase, the fetched `byte[]` and Common Flag are passed to a transcoder. The transcoder converts the bytes into a concrete class (the application specifies the required type) if possible. It may use a serializer (the `JsonDeserializer[T]`) for this.

So, while a JsonSerializer\[T\] and JsonDeserializer\[T\] will always be found - the code will not compile if not - they are not necessarily used. It is down to the transcoder to make this choice.

> [!NOTE]
> Many applications will not need to be aware of transcoders and serializers, as the defaults support most standard JSON use cases. The information in this page is only needed if the application has an advanced use-case, likely involving either non-JSON data, or a requirement for a particular JSON serialization library. For examples of many common JSON use cases see [JSON Libraries](json.md).

## [](#default-behaviour)Default Behaviour

The `ClusterEnvironment` contains a global transcoder, which by default is `JsonTranscoder`.

On sending data of type `T` to Couchbase, a `JsonSerializer[T]` will be found by the compiler. If it cannot be found, the program will not be compiled. `JsonTranscoder` will send objects to that serializer to convert into a `byte[]`. The serialized bytes are then sent to the Couchbase Server, along with a Common Flag of JSON.

`JsonTranscoder` will pass any `T` to its serializer, apart from a `byte[]`. It will reject this with a `Failure(IllegalArgumentException)`, as it is ambiguous how it should be handled.

On retrieving data from Couchbase into a desired type `T`, a `JsonDeserializer[T]` will be found by the compiler. `JsonTranscoder` passes the fetched `byte[]` and Common Flag to that serializer to convert into a `T`.

This table summarizes that information, and this more concise form will be used to describe the other transcoders included in the SDK.

| Item     | Result                            | Common Flag |
| -------- | --------------------------------- | ----------- |
| String   | Results of serializer             | JSON        |
| byte\[\] | Failure(IllegalArgumentException) | \-          |
| Other T  | Results of serializer             | JSON        |

The default `JsonSerializer` and `JsonDeserializer` provided handle objects of type `T` as follows:

| Type of T                                                                               | Serialized                                                                                            |
| --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| String                                                                                  | Into/from JSON with the high-performance JSON library [Jackson](https://github.com/FasterXML/jackson) |
| byte\[\]                                                                                | Passed through (no serialization)                                                                     |
| JsonObject, JsonArray, JsonObjectSafe, JsonArraySafe                                    | Into/from JSON using Jackson                                                                          |
| Boolean                                                                                 | Into/from a JSON representation directly ('true' or 'false')                                          |
| Other primitives (Int, Double, Long, Short)                                             | Into/from a JSON representation directly                                                              |
| ujson.Value from [µPickle](http://www.lihaoyi.com/upickle/)                             | Into/from JSON using the µPickle library                                                              |
| io.circe.Json from [Circe](https://circe.github.io/circe/)                              | Into/from JSON using the Circe library                                                                |
| play.api.libs.json.JsValue from [Play JSON](https://github.com/playframework/play-json) | Into/from JSON using the Play JSON library                                                            |
| org.json4s.JsonAST.JValue from [Json4s](http://json4s.org/)                             | Into/from JSON using the Json4s library                                                               |
| org.typelevel.jawn.ast.JValue from [Jawn](https://github.com/typelevel/jawn)            | Into/from JSON using the Jawn library                                                                 |
| Scala case classes                                                                      | Into/from JSON with a small amount of boilerplate to automatically generate a JsonSerializer          |

There are concrete examples of using these on the [JSON Libraries](json.md) page. Note that the Scala SDK only has an optional dependency on Circe, Json4s, et al, so those libraries not be pulled into your application.

## [](#rawjsontranscoder)RawJsonTranscoder

The RawJsonTranscoder provides the ability for the application to explicitly specify that the data they are storing or retrieving is JSON. This transcoder does not accept a serializer, and always performs straight pass through of the data to the server. This enables the application to avoid unnecessary parsing costs when they are certain they are using JSON data.

It only accepts Strings and `byte[]`.

| Item     | Result                            | Common Flag |
| -------- | --------------------------------- | ----------- |
| String   | Passthrough                       | JSON        |
| byte\[\] | Passthrough                       | JSON        |
| Other T  | Failure(IllegalArgumentException) | \-          |

Say we want to serialize and deserialize some data with the JSON library uPickle\[<https://github.com/lihaoyi/upickle>\], and have the Scala SDK just passthrough the serialized data to and from Couchbase. We will look at better ways of doing this later, but here is one approach using `RawJsonTranscoder`.

Since uPickle has already done the serialization work, we don’t want to use the default `JsonTranscoder`, as this will run the provided bytes needlessly through `DefaultJsonSerializer` (Jackson). Instead, RawJsonTranscoder is used, which just passes through the serialized bytes, and stores them in Couchbase with the JSON Common Flag set. Similarly, the same transcoder is used on reading the document, so the raw bytes can be retrieved in a String without going through `DefaultJsonSerializer` (Jackson).

```scala

val json = ujson.Obj("name" -> "John Smith", "age" -> 27)
val bytes: Array[Byte] = ujson.transform(json, ujson.BytesRenderer()).toByteArray

collection.upsert(
  "doc-id",
  bytes,
  UpsertOptions().transcoder(RawJsonTranscoder.Instance)
) match {
  case Success(_) =>
    collection
      .get(
        "doc-id",
        GetOptions().transcoder(RawJsonTranscoder.Instance)
      )
      .flatMap(result => result.contentAs[Array[Byte]]) match {
      case Success(fetched) =>
        val jsonFetched = upickle.default.read[ujson.Value](fetched)
        assert(jsonFetched("name").str == "John Smith")
        assert(jsonFetched("age").num == 27)

      case Failure(err) => fail(s"Failed to get or convert doc: $err")
    }

  case Failure(err) => fail(s"Failed to upsert doc: $err")
}
```

## [](#non-json-transcoders)Non-JSON Transcoders

It is most common to store JSON with Couchbase. However, it is possible to store non-JSON documents, such as raw binary data, perhaps using an concise binary encoding like [MessagePack](https://msgpack.org) or [CBOR](https://cbor.io/), in the Key-Value store.

> [!NOTE]
> It’s important to note that the Couchbase Data Platform includes multiple components other than the Key-Value store — including Query and its indexes, FTS, Analytics, and Eventing — and these are optimized for JSON and will either ignore or provide limited functionality with non-JSON documents.

Also note that some simple data types can be stored directly as JSON, without recourse to non-JSON transcoding. A valid JSON document can be a simple integer (`42`), string (`"hello"`), array (`[1,2,3]`), boolean (`true`, `false`) and the JSON `null` value.

### [](#rawstringtranscoder)RawStringTranscoder

The RawStringTranscoder provides the ability for the user to explicitly store and retrieve raw string data with Couchbase. It can be used to avoid the overhead of storing the string as JSON, which requires two bytes for double quotes, plus potentially more for escaping characters.

Note that this transcoder does not accept a serializer, and always performs straight passthrough of the data to the server. It only accepts Strings.

| Item     | Result                            | Common Flag |
| -------- | --------------------------------- | ----------- |
| String   | Passthrough                       | String      |
| byte\[\] | Failure(IllegalArgumentException) | \-          |
| Other T  | Failure(IllegalArgumentException) | \-          |

Here’s an example of using the `RawStringTranscoder`:

```scala
collection.upsert(
  "doc-id",
  "hello world",
  UpsertOptions().transcoder(RawStringTranscoder.Instance)
) match {

  case Success(_) =>
    collection
      .get(
        "doc-id",
        GetOptions().transcoder(RawStringTranscoder.Instance)
      )
      .flatMap(result => result.contentAs[String]) match {

      case Success(fetched) =>
        assert(fetched == "hello world")

      case Failure(err) => fail(s"Failed to get or convert doc: $err")
    }

  case Failure(err) => fail(s"Failed to upsert doc: $err")
}
```

### [](#rawbinarytranscoder)RawBinaryTranscoder

The RawBinaryTranscoder provides the ability for the user to explicitly store and retrieve raw byte data to Couchbase. The transcoder does not perform any form of real transcoding, and does not take a serializer, but rather passes the data through and assigns the appropriate binary Common Flag.

| Item     | Result                            | Common Flag |
| -------- | --------------------------------- | ----------- |
| String   | Failure(IllegalArgumentException) | \-          |
| byte\[\] | Passthrough                       | Binary      |
| Other T  | Failure(IllegalArgumentException) | \-          |

Here’s an example of using the `RawBinaryTranscoder`:

```scala
val content: Array[Byte] = "hello world".getBytes(StandardCharsets.UTF_8)

  collection.upsert(
    "doc-id",
    content,
    UpsertOptions().transcoder(RawBinaryTranscoder.Instance)
  ) match {
    case Success(_) =>
      collection
        .get(
          "doc-id",
          GetOptions().transcoder(RawBinaryTranscoder.Instance)
        )
        .flatMap(result => result.contentAs[Array[Byte]]) match {
        case Success(fetched) =>
          assert(fetched(0) == 'h')
          assert(fetched(1) == 'e')
          assert(fetched(2) == 'l')
          // ...

        case Failure(err) => fail(s"Failed to get or convert doc: $err")
      }

    case Failure(err) => fail(s"Failed to upsert doc: $err")
  }
```

## [](#custom-transcoders-and-serializers)Custom Transcoders and Serializers

More advanced transcoding needs can be accomplished if the application implements their own transcoders and serializers.

### [](#creating-a-custom-serializer)Creating a Custom Serializer

Say we have a Scala case class, `MyUser`, that we want to easily convert to & from JSON to store in Couchbase. The Scala SDK already provides support for this (see [JSON Libraries](json.md)), but perhaps for some reason we want to use the JSON library [uPickle](https://github.com/lihaoyi/upickle) for this instead. First we need a `JsonSerializer[User]` and `JsonDeserializer[User]`, which are simple to write:

```scala
case class MyUser(name: String, age: Int)

object MyUser {
  implicit object UserSerializer extends JsonSerializer[MyUser] {
    override def serialize(content: MyUser): Try[Array[Byte]] = {
      // It's also possible for uPickle to serialize and deserialize
      // case classes directly to/from JSON, but for the purposes of
      // demonstration we will generate the JSON manually.
      val json = ujson.Obj("name" -> content.name, "age" -> content.age)
      Success(ujson.transform(json, ujson.BytesRenderer()).toByteArray)
    }
  }

  implicit object UserDeserializer extends JsonDeserializer[MyUser] {
    override def deserialize(bytes: Array[Byte]): Try[MyUser] = {
      Try({
        val json = upickle.default.read[ujson.Value](bytes)
        MyUser(json("name").str, json("age").num.toInt)
      })
    }
  }
}
```

Both of these are marked `implicit object` and inside `object MyUser` so the compiler can find them. They will now be picked up by the compiler and used automatically:

```scala
val user = MyUser("John Smith", 27)

// The compiler will find our UserSerializer for this
collection.upsert("john-smith", user) match {

  case Success(_) =>
    collection
      .get("john-smith")

      // ... and our UserDeserializer for this
      .flatMap(fetched => fetched.contentAs[MyUser]) match {

      case Success(fetchedUser) =>
        assert(fetchedUser == user)

      case Failure(err) => fail(s"Failed to get doc: $err")
    }

  case Failure(err) => fail(s"Failed to upsert doc: $err")
}
```

Note we don’t need to change the transcoder for this example. The [table for JsonTranscoder](#default-behaviour) shows that it already does what we need: on serialization (in the `upsert`), it passes the `MyUser` object to the compiler-found serializer (`UserSerializer`) and stores the result in Couchbase with the JSON common flag. And on deserialization (in the `contentAs`), the raw bytes are passed to `UserDeserializer`, and resulting `MyUser` passed back to the application.

### [](#selecting-a-serializer)Selecting a Serializer

What if there are multiple serializers that could be used for an object, and the application needs to select one?

The serializer is an implicit argument to any operation that requires one, and the compiler-chosen selection can be overwritten by the application like this:

```scala
case class MyUser2(name: String, age: Int)

object MyUser2 {
  // First serializer uses uPickle
  implicit object UserSerializer1 extends JsonSerializer[MyUser2] {
    override def serialize(content: MyUser2): Try[Array[Byte]] = {
      val json = ujson.Obj("name" -> content.name, "age" -> content.age)
      Success(ujson.transform(json, ujson.BytesRenderer()).toByteArray)
    }
  }

  // Second serializer writes the JSON manually
  implicit object UserSerializer2 extends JsonSerializer[MyUser2] {
    override def serialize(content: MyUser2): Try[Array[Byte]] = {
      val sb = new StringBuilder
      sb.append("""{"name":""")
      sb.append(content.name)
      sb.append("""","age":""")
      sb.append(content.age)
      sb.append("}")
      Success(sb.toString.getBytes(StandardCharsets.UTF_8))
    }
  }
}
```

```scala
val user = MyUser2("John Smith", 27)

// This import will cause the compiler to prefer UserSerializer2
import MyUser2.UserSerializer2
collection.upsert("john-smith", user).get

// But the application can override this
collection.upsert("john-smith", user)(MyUser2.UserSerializer1).get
```

### [](#creating-a-custom-transcoder)Creating a Custom Transcoder

Let’s look at a more complex example: encoding the JSON alternative, [MessagePack](https://msgpack.org). MessagePack is a compact binary data representation, so it should be stored with the binary Common Flag. The Common Flag is chosen by the transcoder, and none of the existing transcoders matches our needs (`RawBinaryTranscoder` does set the binary flag, but it passes data through directly rather than using a serializer). So we need to write one.

Start by creating a new serializer and deserializer for our case class, that uses MessagePack:

```scala
object MsgPack {
  implicit object MsgPackSerializer extends JsonSerializer[MyUser] {
    override def serialize(content: MyUser): Try[Array[Byte]] = {
      Try({
        // MessagePack can automatically generate equivalent code,
        // but for demonstration purposes we will do it manually
        val packer = MessagePack.newDefaultBufferPacker()
        packer.packString(content.name)
        packer.packInt(content.age)
        packer.close()
        packer.toByteArray
      })
    }
  }

  implicit object MsgPackDeserializer extends JsonDeserializer[MyUser] {
    override def deserialize(bytes: Array[Byte]): Try[MyUser] = {
      Try({
        val unpacker = MessagePack.newDefaultUnpacker(bytes)
        MyUser(unpacker.unpackString(), unpacker.unpackInt())
      })
    }
  }
}
```

And now create a transcoder that sets the binary Common Flag when storing the data:

```scala
class BinaryTranscoder extends TranscoderWithSerializer {
  def encode[A](value: A, serializer: JsonSerializer[A]): Try[EncodedValue] = {
    serializer
      .serialize(value)
      .map(bytes => EncodedValue(bytes, DocumentFlags.Binary))
  }

  def decode[A](
    value: Array[Byte],
    flags: Int,
    serializer: JsonDeserializer[A]
  )(implicit tag: ClassTag[A]): Try[A] = {
    serializer.deserialize(value)
  }
}
```

Note this transcoder is completely independent to MessagePack. All it does is pass data to and from a serializer, and set a Binary Common Flag.

Now we can use the new transcoder and serializer to seamlessly store MessagePack data in Couchbase Server:

```scala
val user = MyUser("John Smith", 27)

// Make sure the MessagePack serializers are used
import MsgPack._

val transcoder = new BinaryTranscoder

// The compiler will find and use our MsgPackSerializer here
collection.upsert(
  "john-smith",
  user,
  UpsertOptions().transcoder(transcoder)
) match {
  case Success(_) =>

    collection
      .get("john-smith", GetOptions().transcoder(transcoder))

      // ... and our MsgPackDeserializer here
      .flatMap(result => result.contentAs[MyUser]) match {

      case Success(fetched) =>
        assert(fetched == user)

      case Failure(err) => fail(s"Failed to get or convert doc: $err")
    }

  case Failure(err) => fail(s"Failed to upsert doc: $err")
}
```

## [](#further-reading)Further reading

* For _Common flags_, setting the data format used, see the [Data Structures reference](../ref/data-structures.md#common-flags).
* _Format flags_ for ancient SDKs are still available for compatibility, if you are porting a long-lived legacy app. See the [Legacy formats reference](../ref/data-structures.md#legacy-formats).
* If you want to work with binary documents and our Search service, you might like to take a look at <https://github.com/khanium/couchbase-fts-binary>