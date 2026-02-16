[View original HTML](/kotlin-sdk/1.3/howtos/json.html)

> The SDK makes it easy to turn Kotlin objects into JSON, and JSON into Kotlin objects. 

## [](#prerequisites)Before You Start

You should know [how to do basic Key Value operations](kv-operations.md).

You should know about [JSON](https://simple.wikipedia.org/wiki/JSON).

## [](#data-binding-intro)Introduction to Data Binding

It’s good to store documents in JSON format, because some Couchbase services only work with JSON documents.

When we talk about "data binding" in the Couchbase SDK, we mean converting Kotlin objects into JSON, and converting JSON into Kotlin objects. Data binding happens automatically, so you don’t need to write a lot of code.

## [](#data-binding-with-map)Data binding with Map

The simplest data binding uses a Kotlin `Map` object to represent document content. Here is an example:

Using a Kotlin `Map` to represent document content

```kotlin
collection.upsert(
    id = "alice",
    content = mapOf("favoriteColor" to "blue"),
)

val result: GetResult = collection.get("alice")

println("Content in Couchbase: " + String(result.content.bytes))
println("Content as Map: " + result.contentAs<Map<String, Any?>>())
```

The example prints:

```none
Content in Couchbase: {"favoriteColor":"blue"} (1)
Content as Map: {favoriteColor=blue} (2)
```

| **1** | The SDK converted the Map to JSON, then saved the JSON in Couchbase. |
| ----- | -------------------------------------------------------------------- |
| **2** | The contentAs method converted the JSON into a Kotlin Map.           |

## [](#data-binding-with-your-own-classes)Data binding with your own classes

It’s often good to make Kotlin classes that represent the structure of your data. Then you can work your own classes instead of maps.

When you write a document, the `content` argument can be an instance of your own class. The SDK uses data binding to convert your object to JSON.

When you read a document, you can ask the SDK to convert the content to an instance of your own class.

Here is an example:

Data binding with a user-defined class

```kotlin
data class MyClass(
    val favoriteColor: String,
)

collection.upsert(
    id = "alice",
    content = MyClass(favoriteColor = "blue"),
)

val result: GetResult = collection.get("alice")

println("Content in Couchbase: " + String(result.content.bytes))
println("Content as MyClass: " + result.contentAs<MyClass>())
```

The example prints:

```none
Content in Couchbase: {"favoriteColor":"blue"}
Content as MyClass: MyClass(favoriteColor=blue)
```

In this example, `MyClass` is very simple — it has only one property. Data binding works with complicated classes, too. Your classes can have properties that are maps or lists of other complicated objects. Experiment and have fun!

## [](#skip-data-binding)Writing content already in JSON format

If the data you want to save in Couchbase is already in JSON format, you must tell the SDK to skip data binding.

There are two ways to skip data binding. This example shows both ways:

Writing a JSON document without data binding

```kotlin
val jsonContent = """{"favoriteColor":"blue"}"""

// Option A
collection.upsert(
    id = "alice",
    content = jsonContent,
    transcoder = RawJsonTranscoder, (1)
)

// Option B
collection.upsert(
    id = "alice",
    content = Content.json(jsonContent), (1)
)
```

| **1** | We will talk more about RawJsonTranscoder and Content in the [transcoders section](#transcoders). |
| ----- | ------------------------------------------------------------------------------------------------- |

|  | If you use a String for the content when changing a document, and don’t skip data binding, the SDK assumes you want the document content to be a JSON String. For example, if you write: // Don't do this! collection.upsert(     id = "alice",     content = """{"favoriteColor":"blue"}""" ) The document content in Couchbase is: "{\\"favoriteColor\\":\\"blue\\"}" instead of what you probably want: {"favoriteColor":"blue"} To fix this problem, [skip data binding](#skip-data-binding), |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#reading-json-content-without-data-binding)Reading JSON content without data binding

Sometimes it’s useful to get the content of a JSON document as a byte array. This examples shows how to get the unprocessed bytes of a document:

Reading a JSON document as a byte array

```kotlin
val result: GetResult = collection.get(id = "alice")
val jsonBytes: ByteArray = result.content.bytes (1)
```

| **1** | The byte array contains the unprocessed document content. You can parse the JSON yourself, or do something else with the bytes. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------- |

## [](#json-serializer)JsonSerializer

The part of the SDK that does data binding is called a `JsonSerializer`. The SDK includes serializers for some popular JSON libraries. You can add support for other libraries, too.

### [](#jackson)Jackson

The Kotlin SDK uses the [Jackson data binding library](https://github.com/FasterXML/jackson-databind). Jackson is a fast and popular library for working with JSON.

|  | The Kotlin SDK includes a repackaged version of Jackson for its own internal use. Your code should not use that version of Jackson. Always import Jackson classes from the com.fasterxml.jackson package. Never import Jackson classes from the com.couchbase.client.core.deps.com.fasterxml.jackson package. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

When you use your own classes for data binding, you can put special Jackson annotations on your classes to change how the data binding works. You can use annotations to change the JSON field names, or ignore some properties of your classes. Jackson is a powerful tool with many features.

To learn more about Jackson, please read the [Jackson documentation](https://github.com/FasterXML/jackson-docs).

|  | Jackson Tree Model Jackson can represent a JSON document as a tree of JsonNode objects. You can use data binding with JsonNode. This is useful if you don’t know the structure of the document. For example: val json = collection.get(id = "alice").contentAs<JsonNode>() when {     json is ArrayNode -> println("Content is a JSON Array")     json is ObjectNode -> println("Content is a JSON Object")     else -> println("Content is a JSON primitive") } Sometimes it’s easier to do data binding with a JsonNode than a Map. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### [](#customize-jackson-mapper)Customizing the Jackson mapper

By default, `JacksonJsonSerializer` uses a `JsonMapper` with default settings, and the Kotlin and JDK 8 modules.

You can use your own Jackson mapper instead. This example creates a `JacksonJsonSerializer` with a different mapper, and configures the SDK to use it by default:

Overriding the default Jackson JsonMapper

```kotlin
val jsonMapper: JsonMapper = getMyCustomJsonMapper()

val cluster = Cluster.connect(connectionString, username, password) {
    jsonSerializer = JacksonJsonSerializer(jsonMapper)
}
```

### [](#moshi)Moshi

[Moshi](https://github.com/square/moshi) is another popular library for working with JSON. If you like Moshi more than Jackson, you can tell the SDK to use Moshi instead.

First, add Moshi as a dependency of your project:

* Gradle (Kotlin)
* Gradle (Groovy)
* Maven

```kotlin
implementation("com.squareup.moshi:moshi-kotlin:1.13.0")
```

```groovy
implementation "com.squareup.moshi:moshi-kotlin:1.13.0"
```

```xml
<dependency>
    <groupId>com.squareup.moshi</groupId>
    <artifactId>moshi-kotlin</artifactId>
    <version>1.13.0</version>
</dependency>
```

When you connect to the cluster, tell the SDK to use Moshi as the default JSON serializer:

```kotlin
val moshi = Moshi.Builder()
    .add(KotlinJsonAdapterFactory())
    .build()

val cluster = Cluster.connect(connectionString, username, password) {
    jsonSerializer = MoshiJsonSerializer(moshi) (1)
}
```

| **1** | Please read the [MoshiJsonSerializer API reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client/kotlin-client/com.couchbase.client.kotlin.codec/-moshi-json-serializer/) to see more options. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#custom-jsonserializer)Custom JsonSerializer

If there is a JSON library you like more than Jackson or Moshi, you can make your own serializer by implementing the `JsonSerializer` interface. The [Moshi](#moshi) section shows how to tell the SDK which serializer to use.

Alternatively, you can [skip data binding](#skip-data-binding) and use your preferred JSON library to read and write JSON without using the SDK.