[View original HTML](/java-sdk/3.10/howtos/transcoders-nonjson.html)

> The Java SDK supports common JSON document requirements out-of-the-box. Custom transcoders and serializers provide support for applications needing to perform advanced operations, including supporting non-JSON data. 

The Java SDK uses the concepts of transcoders and serializers, which are used whenever data is sent to or retrieved from Couchbase Server.

When sending data to Couchbase, the SDK passes the Object being sent to a transcoder. The transcoder can either reject the Object as being unsupported, or convert it into a `byte[]` and a Common Flag. The Common Flag specifies whether the data is JSON, a non-JSON string, or raw binary data. It may, but does not have to, use a serializer to perform the byte conversion.

On retrieving data from Couchbase, the fetched `byte[]` and Common Flag are passed to a transcoder. The transcoder converts the bytes into a concrete class (the application specifies the required type) if possible. It may use a serializer for this.

|  | Many applications will not need to be aware of transcoders and serializers, as the defaults support most standard JSON use cases. The information in this page is only needed if the application has an advanced use-case, likely involving either non-JSON data, or a requirement for a particular JSON serialization library. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#default-behaviour)Default Behaviour

The `ClusterEnvironment` contains a global transcoder and serializer, which by default are `JsonTranscoder` and `DefaultJsonSerializer`.

`DefaultJsonSerializer` uses the high-performance JSON library [Jackson](https://github.com/FasterXML/jackson) for serializing and deserializing byte arrays to and from concrete objects.

On sending data to Couchbase, `JsonTranscoder` will send Objects to its serializer (`DefaultJsonSerializer` by default) to convert into a `byte[]`. The serialized bytes are then sent to the Couchbase Server, along with a Common Flag of JSON.

`JsonTranscoder` will pass any Object to its serializer, apart from a `byte[]`. It will reject this with an InvalidArgumentException, as it is ambiguous how it should be handled.

On retrieving data from Couchbase, `JsonTranscoder` passes the fetched `byte[]` and Common Flag to its serializer (`DefaultJsonSerializer` by default) to convert into a concrete class.

This table summarizes that information, and this more concise form will be used to describe the other transcoders included in the SDK.

| Item         | Result                   | Common Flag |
| ------------ | ------------------------ | ----------- |
| String       | Results of serializer    | JSON        |
| byte\[\]     | InvalidArgumentException | \-          |
| Other Object | Results of serializer    | JSON        |

## [](#using-custom-jackson)Using Custom Jackson

As described above, the default serializer (`DefaultJsonSerializer`) uses Jackson for serializing objects. (This Jackson dependency is shaded into a different namespace, so that it does not clash with any Jackson used by your application.)

If Jackson is on the application’s classpath, the SDK will instead automatically default to using this. It does this during `ClusterEnvironment` creation: if no serializer has been specified, and if Jackson is detected on the classpath, then a `JacksonJsonSerializer` is used as the global default serializer instead of `DefaultJsonSerializer`. This will create and use a Jackson `ObjectMapper` from the standard `com.fasterxml.jackson.databind` package.

Using a custom JsonMapper

```java
JsonMapper customMapper = JsonMapper.builder()
  // add modules or customize other settings
  .build();

Cluster cluster = Cluster.connect(
  connectionString,
  ClusterOptions.clusterOptions(username, password)
    .environment(env -> env
      .jsonSerializer(JacksonJsonSerializer.create(customMapper))
    )
);
```

## [](#rawjsontranscoder)RawJsonTranscoder

The RawJsonTranscoder provides the ability for the application to explicitly specify that the data they are storing or retrieving is JSON. This transcoder does not accept a serializer, and always performs straight pass through of the data to the server. This enables the application to avoid unnecessary parsing costs when they are certain they are using JSON data.

It only accepts Strings and `byte[]`.

| Item         | Result                   | Common Flag |
| ------------ | ------------------------ | ----------- |
| String       | Passthrough              | JSON        |
| byte\[\]     | Passthrough              | JSON        |
| Other Object | InvalidArgumentException | \-          |

This transcoder is particularly useful when working with third-party JSON libraries. Here we want to use [Google Gson](https://github.com/google/gson) for serialization, instead of the default Jackson:

```java
// User is a simple POJO
User user = new User("John Smith", 27);

Gson gson = new Gson();
String json = gson.toJson(user);

collection.upsert("john-smith", json, UpsertOptions.upsertOptions().transcoder(RawJsonTranscoder.INSTANCE));
```

Since Gson has already done the serialization work, we don’t want to use the default `JsonTranscoder`, as this will run the provided String needlessly through `DefaultJsonSerializer` (Jackson). Instead, RawJsonTranscoder is used, which just passes through the serialized bytes, and stores them in Couchbase with the JSON Common Flag set.

Similarly, the same transcoder is used on reading the document, so the raw bytes can be retrieved in a String without going through `DefaultJsonSerializer` (Jackson). Gson can then be used for the deserialization.

```java
GetResult result = collection.get("john-smith", GetOptions.getOptions().transcoder(RawJsonTranscoder.INSTANCE));

String returnedJson = result.contentAs(String.class);
User returnedUser = gson.fromJson(returnedJson, User.class);
```

## [](#non-json-transcoders)Non-JSON Transcoders

It is most common to store JSON with Couchbase. However, it is possible to store non-JSON documents, such as raw binary data, perhaps using an concise binary encoding like [MessagePack](https://msgpack.org) or [CBOR](https://cbor.io/), in the Key-Value store.

|  | It’s important to note that the Couchbase Data Platform includes multiple components other than the Key-Value store — including [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) and its indexes, FTS, analytics, and eventing — and these are optimized for JSON and will either ignore or provide limited functionality with non-JSON documents. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

Also note that some simple data types can be stored directly as JSON, without recourse to non-JSON transcoding. A valid JSON document can be a simple integer (`42`), string (`"hello"`), array (`[1,2,3]`), boolean (`true`, `false`) and the JSON `null` value.

### [](#rawstringtranscoder)RawStringTranscoder

The RawStringTranscoder provides the ability for the user to explicitly store and retrieve raw string data with Couchbase. It can be used to avoid the overhead of storing the string as JSON, which requires two bytes for double quotes, plus potentially more for escaping characters.

Note that this transcoder does not accept a serializer, and always performs straight passthrough of the data to the server. It only accepts Strings.

| Item         | Result                   | Common Flag |
| ------------ | ------------------------ | ----------- |
| String       | Passthrough              | String      |
| byte\[\]     | InvalidArgumentException | \-          |
| Other Object | InvalidArgumentException | \-          |

Here’s an example of using the `RawStringTranscoder`:

```java
collection.upsert(docId, "hello world", UpsertOptions.upsertOptions().transcoder(RawStringTranscoder.INSTANCE));

GetResult result = collection.get(docId, GetOptions.getOptions().transcoder(RawStringTranscoder.INSTANCE));

String returned = result.contentAs(String.class);
```

### [](#rawbinarytranscoder)RawBinaryTranscoder

The RawBinaryTranscoder provides the ability for the user to explicitly store and retrieve raw byte data to Couchbase. The transcoder does not perform any form of real transcoding, and does not take a serializer, but rather passes the data through and assigns the appropriate binary Common Flag.

| Item         | Result                   | Common Flag |
| ------------ | ------------------------ | ----------- |
| String       | InvalidArgumentException | \-          |
| byte\[\]     | Passthrough              | Binary      |
| Other Object | InvalidArgumentException | \-          |

Here’s an example of using the `RawBinaryTranscoder`:

```java
String input = "hello world";
byte[] bytes = input.getBytes(StandardCharsets.UTF_8);

collection.upsert(docId, bytes, UpsertOptions.upsertOptions().transcoder(RawBinaryTranscoder.INSTANCE));

GetResult result = collection.get(docId, GetOptions.getOptions().transcoder(RawBinaryTranscoder.INSTANCE));

byte[] returned = result.contentAs(byte[].class);
```

## [](#custom-transcoders-and-serializers)Custom Transcoders and Serializers

More advanced transcoding needs can be accomplished if the application implements their own transcoders and serializers.

### [](#creating-a-custom-serializer)Creating a Custom Serializer

We saw above one example of using Google Gson with the `RawJsonTranscoder`, but it requires the application to explicitly serialize and deserialize objects each time. By creating a custom Gson serializer, we can avoid this.

It’s easy to create a serializer. Simply implement the `JsonSerializer` interface’s three methods:

```java
class GsonSerializer implements JsonSerializer {
    private final Gson gson = new Gson();

    @Override
    public byte[] serialize(Object input) {
        String json = gson.toJson(input);
        return json.getBytes(StandardCharsets.UTF_8);
    }

    @Override
    public <T> T deserialize(Class<T> target, byte[] input) {
        String str = new String(input, StandardCharsets.UTF_8);
        return gson.fromJson(str, target);
    }

    @Override
    public <T> T deserialize(TypeRef<T> target, byte[] input) {
        String str = new String(input, StandardCharsets.UTF_8);
        return gson.fromJson(str, target.type());
    }
}
```

|  | The TypeRef overload is optional, and is only used if the application explicitly uses it with for example result.contentAs(new TypeRef<String> {}), which is an uncommon requirement. It is fine to throw an exception from this method rather than implementing it, if it is not needed. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

In this case, there is no need to provide a custom transcoder. The [table for JsonTranscoder](#default-behaviour) shows that it already does what we need: for any Object (that’s not a `byte[]`), it sends it to its serializer, and then stores the result in Couchbase with the JSON Common Flag set. All we need to do is change the serializer, as so:

```java
GsonSerializer serializer = new GsonSerializer();
JsonTranscoder transcoder = JsonTranscoder.create(serializer);

User user = new User("John Smith", 27);

collection.upsert("john-smith", user, UpsertOptions.upsertOptions().transcoder(transcoder));
```

And for decoding:

```java
GetResult result = collection.get("john-smith", GetOptions.getOptions().transcoder(transcoder));

User returnedUser = result.contentAs(User.class);

assertEquals(user, returnedUser);
```

If you want to use Gson for all JSON serialization, you can register it as the global JSON serializer when creating a `ClusterEnvironment`:

```java
GsonSerializer serializer = new GsonSerializer();

ClusterEnvironment env = ClusterEnvironment.builder().jsonSerializer(serializer).build();
```

The default global `JsonTranscoder` will be initialized with this serializer. Now our GsonSerializer will be automatically used by all operations, without needing to provide a transcoder each time.

### [](#creating-a-custom-transcoder)Creating a Custom Transcoder

Let’s look at a more complex example: encoding the JSON alternative, [MessagePack](https://msgpack.org).

MessagePack is a compact binary data representation, so it should be stored with the binary Common Flag. The Common Flag is chosen by the transcoder, and none of the existing transcoders matches our needs (`RawBinaryTranscoder` does set the binary flag, but it passes data through directly rather than using a serializer). So we need to write one.

Start by creating a new serializer for MessagePack. This is similar to the GsonSerializer example above:

```java
class MsgPackSerializer implements JsonSerializer {
    private final MessagePack msgpack = new MessagePack();

    @Override
    public byte[] serialize(Object input) {
        try {
            return msgpack.write(input);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public <T> T deserialize(Class<T> target, byte[] input) {
        try {
            return msgpack.read(input, target);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public <T> T deserialize(TypeRef<T> target, byte[] input) {
        throw new DecodingFailureException("Does not support decoding via TypeRef.");
    }
}
```

And now create a transcoder that uses the `MsgPackSerializer`, and sets the binary Common Flag when storing the data:

```java
class MsgPackTranscoder implements Transcoder {
    private final MsgPackSerializer serializer = new MsgPackSerializer();

    @Override
    public EncodedValue encode(Object input) {
        byte[] serialized = serializer.serialize(input);
        return new EncodedValue(serialized, CodecFlags.BINARY_COMPAT_FLAGS);
    }

    @Override
    public <T> T decode(Class<T> target, byte[] input, int flags) {
        return serializer.deserialize(target, input);
    }
}
```

Note the use of `BINARY_COMPAT_FLAGS`. The other Common Flags that can be used are `JSON_COMPAT_FLAGS` and `STRING_COMPAT_FLAGS`. Any other flags in `CodecFlags` are for legacy purposes and internal SDK usage, and should not be used.

Now we can use the new transcoder to seamlessly store MessagePack data in Couchbase Server:

```java
MsgPackTranscoder transcoder = new MsgPackTranscoder();

String input = "hello world!";

collection.upsert("msgpack-doc", input, UpsertOptions.upsertOptions().transcoder(transcoder));

GetResult result = collection.get("msgpack-doc", GetOptions.getOptions().transcoder(transcoder));

String output = result.contentAs(String.class);
```

## [](#further-reading)Further reading

* If you want to work with binary documents and our Search service, you might like to take a look at <https://github.com/khanium/couchbase-fts-binary>