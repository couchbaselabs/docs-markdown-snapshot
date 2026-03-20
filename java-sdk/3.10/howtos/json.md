---
title: JSON Modelling
description: The Java SDK supports multiple options for working with JSON.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.10/modules/howtos/pages/json.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.10@java-sdk:howtos:json.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.10/howtos/json.html)

# JSON Modelling

## [](#philosophy)Philosophy

The Couchbase Server is a key-value store that’s agnostic to what’s stored, but it’s very common to store JSON.

The Java SDK has these main objectives for JSON:

* Be usable 'out-of-the-box'. A simple JSON library is included, so you can get started right away. Bonus: it’s simple to use and very fast!
* Be agnostic. Your application may already be using its own JSON representation, and it shouldn’t be forced to use the built-in JSON library. We use [Jackson](https://github.com/FasterXML/jackson) internally, so if you’re already using that popular ecosystem’s annotations you’re set to go. But you’re never locked into it, and you can use other libraries like [Gson](https://github.com/google/gson/) easily.

## [](#getting-started)Getting Started

The examples below assume you’re familiar with connecting to a Couchbase cluster using the Java SDK, and opening resources. Please check out [the Getting Started guide](#hello-world:start-using-sdk) for help with this.

### [](#inserting-a-simple-object)Inserting a simple object

Let’s assume we have a very simple JSON structure we want to insert:

```json
{ 
  name: "Arthur",
  number: 42
}
```

Once we’ve connected to a Couchbase server and the bucket, scope, and collection that we want to write to, we know that inserting is as simple as:

```java
collection.upsert("arthur", json);
```

But how do we model that JSON object?

We mentioned the simple JSON library that we ship with the SDK, and let’s look at this first:

```java
import com.couchbase.client.java.json.*;
```

```java
JsonObject json = JsonObject.create()
  .put("name", "Arthur")
  .put("number", 42);
```

### [](#retrieving)Retrieving

Couchbase’s `Collection.get()` method returns a `GetResult` object, which can then be converted back into a `JsonObject`. In this example, we print the JSON back, and access one of the fields:

```java
JsonObject jsonResult = collection.get("arthur")
  .contentAsObject();

System.out.println(jsonResult);
System.out.println(jsonResult.getString("name"));
```

### [](#using-javas-map-data-structure)Using Java’s `Map` data structure

The `JsonObject` is modelled on the classic Java `Map` data structure, and in fact is backed by one. So we can easily create an object from an existing Map:

```java
Map<String, Object> map = Map.of( // Java 9+ syntax
  "name", "Arthur",
  "number", 42);

JsonObject json = JsonObject.from(map);
```

The resulting `JsonObject` can be inserted as normal. But most JSON serializers can handle simple objects like a Map already, and ours (backed by Jackson) is no different. So you can simply:

```java
collection.upsert("arthur", map);
```

Once the data is in Couchbase, it is stored in exactly the same way, that is to say, as the JSON representation we started this example with!

So whether we inserted a Map or a JsonObject, we could retrieve it as a JsonObject…​ or indeed a Map:

```java
Map<String, Object> result = collection.get("arthur")
  .contentAs(Map.class);
```

While you are free to use Map, this is capable of storing any valid Java value, including ones that can’t be represented as JSON. JsonObject offers validation to make sure that only the relevant [datatypes](#datatypes) are stored, which will give you greater diagnostics and robustness.

### [](#inserting-a-json-string-or-json-file)Inserting a JSON string or `.json` file

If we read the contents of a file to get a JSON string, we can also inflate a JsonObject from that string:

```java
import java.nio.file.Paths;
import java.nio.file.Files;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
```

```java
String content  = new String(
  Files.readAllBytes(
    Paths.get(pathToArthurJson)),
  StandardCharsets.UTF_8);
// String content  = Files.readString(Paths.get(pathToArthurJson), StandardCharsets.UTF_8); // Java 11+

JsonObject json = JsonObject.fromJson(content);
```

This might seem a little clumsy though: We’re reading a string, inflating it into a JsonObject, passing it to a serializer which will…​ turn it back into a string again to send over the network to the Couchbase server!

We could instead simply pass it through with the Raw JSON Transcoder:

```java
import com.couchbase.client.java.codec.RawJsonTranscoder;
```

```java
collection.upsert("arthur", content,
  UpsertOptions.upsertOptions().transcoder(RawJsonTranscoder.INSTANCE));
```

This approach could also be used to handle JSON created by other libraries such as Gson. See the [Transcoder documentation](transcoders-nonjson.md#rawjsontranscoder) for more details.

### [](#serializing-objects)Serializing objects

It’s common to want to serialize your own objects, rather than creating Json programmatically or textually. Luckily our built-in JSON serializer makes light work of this task. Using this simple class:

```java
public class Person {
  public String name;
  
  public int number;
  
  public Person() {} // default constructor needed to deserialize
  
  public Person(String name, int number) {
    this.name = name;
    this.number = number;
  }
}
```

We could insert the exact same JSON as before with:

```java
collection.upsert("arthur", new Person("Arthur", 42));
```

It’s now trivial to return the data either as a JsonObject, exactly as we’ve done before, or indeed as a Person object:

```java
Person person = collection.get("arthur")
  .contentAs(Person.class);
```

### [](#ObjectMapper)More complex Object to JSON mapping

Because the SDK’s serializer is backed by an industry standard library (Jackson), it is easy to model all kinds of Object to JSON mappings. Though the SDK automatically uses your version of Jackson when it finds the library on the CLASSPATH, you may wish to be explicit, or use an already configured ObjectMapper, as in this example:

```java
import com.couchbase.client.java.env.ClusterEnvironment;
import com.couchbase.client.java.codec.JacksonJsonSerializer;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.annotation.JsonProperty;
```

```java
ObjectMapper mapper = new ObjectMapper();
mapper.registerModule(new JsonValueModule()); // for JsonObject

ClusterEnvironment env = 
  ClusterEnvironment.builder()
    .jsonSerializer(JacksonJsonSerializer.create(mapper))
    .build();

Cluster cluster = Cluster.connect(
  connectionString,
  ClusterOptions
    .clusterOptions(username, password)
    .environment(env));
```

With this setup, we can then configure our classes as we wish. Here, we’ve just renamed the Java class and its fields in Spanish. But the generated JSON will have the same fields as before, for easy interoperability:

```java
public class Persona {
  @JsonProperty("name")
  public String nombre;
  
  @JsonProperty("number")
  public int numero;
  
  // ...
}
```

## [](#datatypes)Modelling JSON datatypes in Java

We’ve only looked at a few datatypes so far, JSON objects `{}`, strings, and integers. But the full range of JSON types can be expressed, with the obvious mappings to Java.

* string `"hello"`
* integer `123`
* float `123.456`
* boolean: `true`, `false`
* object: `JavaObject`, `Map`
* array: `JavaArray`, `List`
* null

In general, these values can be inserted as top-level values, or nested within an object or array. Let’s look at a few examples:

### [](#nested-object)Nested object

This example shows a variety of data types, including a nested array ("possessions") and object ("address"):

```java
JsonObject arthur = JsonObject.create()
  .put("name", "Arthur")
  .put("number", 42)
  .put("float", 42.0)
  .put("address", JsonObject.create()
    .put("street", "Country Lane")
    .put("number", 155)
    .put("town", "Cottington"))
  .put("harmless", true)
  .put("tea", JsonNull.INSTANCE) // or e.g. (String) null
  .put("possessions",
        JsonArray.from(
          "dressing gown",
          "pyjamas"));
```

### [](#top-level-values-other-than-jsonobject)Top level values other than JsonObject

Although it’s common to use a JsonObject, or a JsonArray as the inserted value to couchbase, other values are supported.

For example, to insert a string value, we could simply:

```java
collection.upsert("some-string", "string-value");
```

We can retrieve this value as usual, with the appropriate `.contentAs()`:

```java
System.out.println(
  collection.get("some-string")
    .contentAs(String.class));
```

### [](#dates)Dates

JSON has no built-in representation of dates, so commonly they are represented as one of:

* a string-formatted [ISO-8601](https://www.w3.org/TR/NOTE-datetime) date
* an offset in seconds or milliseconds from the Unix epoch 1 January 1970 UTC

While it doesn’t matter which you choose (as long as you serialize and deserialize your Date object consistently!) it may make sense to store the dates in Couchbase in a format that can be easily manipulated using the [date functions in SQL++](../../../server/current/n1ql/n1ql-language-reference/datefun.md).

Handily, as we can see on the same page, the [supported date formats](#server:n1ql:n1ql-language-reference$datefun.adoc#date-formats) are the usual convention in JSON.

Let’s look at a brief example of how we might implement this, to serialize a new Event class:

```java
public  class Event {
  public String name;
  
  @JsonFormat(shape=JsonFormat.Shape.STRING, pattern="yyyy-MM-dd'T'HH:mm:ss")
  public LocalDateTime date;
  
  // ...
}
```

We’ll need a few extra imports:

```java
import java.time.*;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.annotation.JsonFormat;
```

As we are controlling the serialization carefully, we’ll also want to register our own [ObjectMapper](#ObjectMapper) as above, and additionally configure some of the date handling properties:

```java
mapper.registerModule(new JavaTimeModule());
mapper.disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS);
```

Now all this is set up we can simply serialize and deserialize our Event objects exactly as we’ve done before:

```java
Event towelday = new Event("Towel Day",
  LocalDateTime.of(2021, Month.MAY, 25, 9, 30));

collection.upsert("towel-day", towelday);

Event event = collection.get("towel-day").contentAs(Event.class);
System.out.println(event.date);
```

## [](#subdocuments)Subdocuments

The JsonObjects work equally well with the [Sub-Document](subdocument-operations.md) API. So taking our original "Arthur" object above, we can insert a simple value:

```java
String string = "value";
collection.mutateIn("arthur",
  Arrays.asList(MutateInSpec.upsert("key", string)));
```

```json
{ "name": "Arthur",
  "number": 42,
  "key": "value" }
```

Or we could insert another nested object:

```java
JsonObject object  = JsonObject.create().put("subkey", "subvalue");
collection.mutateIn("arthur",
  Arrays.asList(MutateInSpec.upsert("key", object)));
```

```json
{ "name": "Arthur",
  "number": 42,
  "key": {
    "subkey":"subvalue"
  }
}
```

> [!NOTE]
> Currently, paths cannot exceed 1024 characters, and cannot be more than 32 levels deep. DJSON documents with more than 32 nested layers cannot be parsed, atttempting to do so will result in a `DocumentTooDeepException` exception.

## [](#identifying-the-type-of-arbitrary-json)Identifying the type of arbitrary JSON

Though you will often be mapping objects to JSON according to a defined schema, sometimes you may wish to handle values with unknown types.

As we want to interrogate a specific Java object with well-defined semantics, we again want to specify the [ObjectMapper](#ObjectMapper) used.

We can now convert the result to Jackson’s `JsonNode`, and use its rich set of methods to identify and handle arbitrary values:

```java
import com.fasterxml.jackson.databind.JsonNode;
```

```java
GetResult result = collection.get("mystery");

JsonNode node = result.contentAs(JsonNode.class);
if (node.isBoolean()) {
  System.out.println("It's a boolean!");
  if (node.booleanValue()) {
    System.out.println("SUCCESS!");
  }
}
else {
  System.out.println(node.getNodeType());
  // STRING
}
```

## [](#additional-resources)Additional Resources

* Read more about the [Couchbase Data Model](../../../server/current/learn/data/data.md).