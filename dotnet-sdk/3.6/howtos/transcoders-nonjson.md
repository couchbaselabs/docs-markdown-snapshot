---
title: Transcoders and Non-JSON Documents
description: The .NET SDK supports common JSON document requirements out-of-the-box.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.6/modules/howtos/pages/transcoders-nonjson.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.6@dotnet-sdk:howtos:transcoders-nonjson.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.6/howtos/transcoders-nonjson.html)

# Transcoders and Non-JSON Documents

> The .NET SDK supports common JSON document requirements out-of-the-box. Custom transcoders and serializers provide support for applications needing to perform advanced operations, including supporting non-JSON data. 

The .NET SDK uses the concepts of transcoders and serializers, which are used whenever data is sent to or retrieved from Couchbase Server.

When sending data to Couchbase, the SDK passes the Object being sent to a transcoder. The transcoder can either reject the Object as being unsupported, or convert it into a `byte[]` and a Common Flag. The Common Flag specifies whether the data is JSON, a non-JSON string, or raw binary data. It may, but does not have to, use a serializer to perform the byte conversion.

On retrieving data from Couchbase, the fetched `byte[]` and Common Flag are passed to a transcoder. The transcoder converts the bytes into a concrete class (the application specifies the required type) if possible. It may use a serializer for this.

> [!NOTE]
> Many applications will not need to be aware of transcoders and serializers, as the defaults support most standard JSON use cases. The information in this page is only needed if the application has an advanced use-case, likely involving either non-JSON data, or a requirement for a particular JSON serialization library.

## [](#default-behaviour)Default Behaviour

The `ClusterOptions` contains a global transcoder and serializer, which by default are `JsonTranscoder` and `DefaultSerializer`.

`DefaultSerializer` uses the flexible JSON library [JSON.NET](https://github.com/JamesNK/Newtonsoft.Json) for serializing and deserializing byte arrays to and from concrete objects.

`SystemTextJsonSerializer` uses the more modern, high-performance, but also more strict `System.Text.Json` serializer instead.

On sending data to Couchbase, `JsonTranscoder` will send Objects to its serializer (`DefaultSerializer` by default) to convert into a `byte[]`. The serialized bytes are then sent to the Couchbase Server, along with a Common Flag of JSON.

`JsonTranscoder` will pass any Object to its serializer, apart from a `byte[]`. It will reject this with an InvalidArgumentException, as it is ambiguous how it should be handled.

On retrieving data from Couchbase, `JsonTranscoder` passes the fetched `byte[]` and Common Flag to its serializer (`DefaultSerializer` by default) to convert into a concrete class.

This table summarizes that information, and this more concise form will be used to describe the other transcoders included in the SDK.

| Item         | Result                   | Common Flag |
| ------------ | ------------------------ | ----------- |
| String       | Results of serializer    | JSON        |
| byte\[\]     | InvalidArgumentException | \-          |
| Other Object | Results of serializer    | JSON        |

## [](#rawjsontranscoder)RawJsonTranscoder

The RawJsonTranscoder provides the ability for the application to explicitly specify that the data they are storing or retrieving is JSON. This transcoder does not accept a serializer, and always performs straight pass through of the data to the server. This enables the application to avoid unnecessary parsing costs when they are certain they are using JSON data.

It only accepts Strings and `byte[]`.

| Item         | Result                   | Common Flag |
| ------------ | ------------------------ | ----------- |
| String       | Passthrough              | JSON        |
| byte\[\]     | Passthrough              | JSON        |
| Other Object | InvalidArgumentException | \-          |

This transcoder is particularly useful when working with third-party JSON libraries. Here we want to use [System.Text.Json](https://docs.microsoft.com/en-us/dotnet/api/system.text.json?view=netcore-3.1) for serialization, instead of the default JSON.NET:

```csharp
var userBytes = JsonSerializer.SerializeToUtf8Bytes(new User
{
    Name = "John Smith",
    Age = 27
}, typeof(User));

await collection.UpsertAsync("john-smith", userBytes, options => options.Transcoder(new RawJsonTranscoder()));
```

Since System.Text.Json has already done the serialization work, we don't want to use the default `JsonTranscoder`, as this will run the provided String needlessly through `DefaultSerializer` (JSON.NET). Instead, RawJsonTranscoder is used, which just passes through the serialized bytes, and stores them in Couchbase with the JSON Common Flag set.

Similarly, the same transcoder is used on reading the document, so the raw bytes can be retrieved in a String without going through `DefaultSerializer` (JSON.NET). System.Text.Json can then be used for the deserialization.

```csharp
using var rawJsonDecodeResult =
    await collection.GetAsync("john-smith", options => options.Transcoder(new RawJsonTranscoder()));

var returnedJson = rawJsonDecodeResult.ContentAs<byte[]>();
var decodedUser = JsonSerializer.Deserialize(returnedJson, typeof(User));
```

## [](#non-json-transcoders)Non-JSON Transcoders

It is most common to store JSON with Couchbase. However, it is possible to store non-JSON documents, such as raw binary data, perhaps using an concise binary encoding like [MessagePack](https://msgpack.org) or [CBOR](https://cbor.io/), in the Key-Value store.

> [!NOTE]
> It's important to note that the Couchbase Data Platform includes multiple components other than the Key-Value store — including Query and its indexes, FTS, Analytics, and Eventing — and these are optimized for JSON and will either ignore or provide limited functionality with non-JSON documents.

Also note that some simple data types can be stored directly as JSON, without recourse to non-JSON transcoding. A valid JSON document can be a simple integer (`42`), string (`"hello"`), array (`[1,2,3]`), boolean (`true`, `false`) and the JSON `null` value.

### [](#rawstringtranscoder)RawStringTranscoder

The RawStringTranscoder provides the ability for the user to explicitly store and retrieve raw string data with Couchbase. It can be used to avoid the overhead of storing the string as JSON, which requires two bytes for double quotes, plus potentially more for escaping characters.

Note that this transcoder does not accept a serializer, and always performs straight passthrough of the data to the server. It only accepts Strings.

| Item         | Result                   | Common Flag |
| ------------ | ------------------------ | ----------- |
| String       | Passthrough              | String      |
| byte\[\]     | InvalidArgumentException | \-          |
| Other Object | InvalidArgumentException | \-          |

Here's an example of using the `RawStringTranscoder`:

```csharp
var docId = "doc";

await collection.UpsertAsync<string>(docId, "hello world",
    options =>
    {
        options.Transcoder(new RawStringTranscoder());
        options.Timeout(TimeSpan.FromMinutes(1000));
    });


using var stringResult = await collection.GetAsync(docId, options => options.Transcoder(new RawStringTranscoder()));

var returnedString = stringResult.ContentAs<string>();
```

### [](#rawbinarytranscoder)RawBinaryTranscoder

The RawBinaryTranscoder provides the ability for the user to explicitly store and retrieve raw byte data to Couchbase. The transcoder does not perform any form of real transcoding, and does not take a serializer, but rather passes the data through and assigns the appropriate `Binary` Common Flag (except in the case of an exception).

| Item                 | Encoding Result          | Decoding Result          |
| -------------------- | ------------------------ | ------------------------ |
| String               | InvalidArgumentException | InvalidArgumentException |
| byte\[\]             | Passthrough              | Passthrough              |
| Memory<byte>         | Passthrough(from 3.2.6)  | InvalidArgumentException |
| ReadOnlyMemory<byte> | Passthrough(from 3.2.6)  | InvalidArgumentException |
| IMemoryOwner<byte>   | InvalidArgumentException | Passthrough(from 3.2.6)  |
| Other Object         | InvalidArgumentException | InvalidArgumentException |

Here's an example of using the `RawBinaryTranscoder`:

```csharp

var strBytes = System.Text.Encoding.UTF8.GetBytes("hello world");

await collection.UpsertAsync(docId, strBytes, options => options.Transcoder(new RawBinaryTranscoder()));

using var binaryResult = await collection.GetAsync(docId, options => options.Transcoder(new RawBinaryTranscoder()));

var returnedBinary = binaryResult.ContentAs<byte[]>();
```

From version 3.2.6, the `RawBinaryTranscoder` will accept `Memory<byte>` and `ReadOnlyMemory<byte>` inputs and can return `IMemoryOwner<byte>` outputs. Using these types may improve performance by not allocating large, temporary `byte[]` arrays on the heap.

```csharp

 using var buffer = MemoryPool<byte>.Shared.Rent(16);
 var byteCount = System.Text.Encoding.UTF8.GetBytes("hello world", buffer.Memory.Span);
 Memory<byte> bytes = buffer.Memory.Slice(0, byteCount);

 await collection.UpsertAsync(docId, bytes, options => options.Transcoder(new RawBinaryTranscoder()));

using var binaryMemoryResult = await collection.GetAsync(docId, options => options.Transcoder(new RawBinaryTranscoder()));

 // Be sure to dispose of the IMemoryOwner<byte> when done, typically via a using statement
 using var binary = binaryMemoryResult.ContentAs<IMemoryOwner<byte>>();
```

## [](#custom-transcoders-and-serializers)Custom Transcoders and Serializers

More advanced transcoding needs can be accomplished if the application implements their own transcoders and serializers.

### [](#creating-a-custom-serializer)Creating a Custom Serializer

We saw above one example of using System.Text.Json with the `RawJsonTranscoder`, but it requires the application to explicitly serialize and deserialize objects each time. By creating a custom JSON serializer, we can avoid this.

It's easy to create a serializer. Simply implement the `ITypeSerializer` interface's three methods:

```csharp
public class DotnetJsonSerializer : ITypeSerializer
{
    public T Deserialize<T>(ReadOnlyMemory<byte> buffer)
    {
        return JsonSerializer.Deserialize<T>(buffer.Span);
    }

    public T Deserialize<T>(Stream stream)
    {
        using var ms = new MemoryStream();
        stream.CopyTo(ms);
        var span = new ReadOnlySpan<byte>(ms.GetBuffer()).Slice(0, (int)ms.Length);
        return JsonSerializer.Deserialize<T>(span);
    }

    public ValueTask<T> DeserializeAsync<T>(Stream stream, CancellationToken cancellationToken = default)
    {
        return JsonSerializer.DeserializeAsync<T>(stream, null, cancellationToken);
    }

    public void Serialize(Stream stream, object obj)
    {
        using var jsonUtf8Writer = new Utf8JsonWriter(stream);
        JsonSerializer.Serialize(jsonUtf8Writer, obj);
    }

    public ValueTask SerializeAsync(Stream stream, object obj, CancellationToken cancellationToken = default)
    {
        return new ValueTask(JsonSerializer.SerializeAsync(stream, obj, null, cancellationToken));
    }
}
```

In this case, there is no need to provide a custom transcoder. The [table for JsonTranscoder](#default-behaviour) shows that it already does what we need: for any Object (that's not a `byte[]`), it sends it to its serializer, and then stores the result in Couchbase with the JSON Common Flag set. All we need to do is change the serializer, as so:

```csharp
var serializer = new DotnetJsonSerializer();
var transcoder = new JsonTranscoder(serializer);

var user = new User
{
    Name = "John Smith",
    Age = 27
};

await collection.UpsertAsync("john-smith", user, options => options.Transcoder(transcoder));
```

And for decoding:

```csharp

using var customDecodeResult = await collection.GetAsync("john-smith", options => options.Transcoder(transcoder));
var returnedUser = customDecodeResult.ContentAs<User>();
```

Currently its not suggested that a custom JSON serializer be used globally in the Couchbase .NET SDK for anything other than K/V. This is because of streaming optimizations used in Query, FTS and Search that use JSON.NET features. These internals are gradually being migrated to the `SystemTextJsonSerializer` for improved performance.

```csharp
var newClusterOptions = new ClusterOptions().WithSerializer(new DotnetJsonSerializer());
var newCluster = await Cluster.ConnectAsync("couchbase://your-ip", newClusterOptions);


var globalResults = await newCluster.QueryAsync<dynamic>("SELECT * FROM `default`");
await foreach (var result in globalResults)
{
    Console.WriteLine(result);
}
```

### [](#creating-a-custom-transcoder)Creating a Custom Transcoder

Let's look at a more complex example: encoding the JSON alternative, [MessagePack](https://msgpack.org). MessagePack is a compact binary data representation, so it should be stored with the binary Common Flag. The Common Flag is chosen by the transcoder, and none of the existing transcoders matches our needs (`RawBinaryTranscoder` does set the binary flag, but it passes data through directly rather than using a serializer). So we need to write one.

Start by creating a new serializer for MessagePack. This is similar to the custom JSON Serializer example above:

```csharp
public class MsgPackSerializer : ITypeSerializer
{
    public T Deserialize<T>(ReadOnlyMemory<byte> buffer)
    {
        return MessagePackSerializer.Deserialize<T>(buffer);
    }

    public T Deserialize<T>(Stream stream)
    {
        return MessagePackSerializer.Deserialize<T>(stream);
    }

    public ValueTask<T> DeserializeAsync<T>(Stream stream, CancellationToken cancellationToken = default)
    {
        return MessagePackSerializer.DeserializeAsync<T>(stream, null, cancellationToken);
    }

    public void Serialize(Stream stream, object obj)
    {
        MessagePackSerializer.Serialize(stream, obj);
    }

    public ValueTask SerializeAsync(Stream stream, object obj, CancellationToken cancellationToken = default)
    {
        return new ValueTask(MessagePackSerializer.SerializeAsync(stream, obj, null, cancellationToken));
    }
}
```

And now create a transcoder that uses the `MsgPackSerializer`, and sets the binary Common Flag when storing the data:

```csharp
public class MsgPackTranscoder : BaseTranscoder
{
    public MsgPackTranscoder() : this(new MsgPackSerializer())
    {
    }

    internal MsgPackTranscoder(MsgPackSerializer serializer)
    {
        Serializer = serializer;
    }

    public override Flags GetFormat<T>(T value)
    {
        var typeCode = Type.GetTypeCode(typeof(T));
        var dataFormat = DataFormat.Binary;
        return new Flags { Compression = Compression.None, DataFormat = dataFormat, TypeCode = typeCode };
    }

    public override void Encode<T>(Stream stream, T value, Flags flags, OpCode opcode)
    {
        Serializer.Serialize(stream, value);
    }

    public override T Decode<T>(ReadOnlyMemory<byte> buffer, Flags flags, OpCode opcode)
    {
        return Serializer.Deserialize<T>(buffer);
    }
}
```

Note the use of `DataFormat.Binary`. The other Common Flags that can be used are `DataFormat.Json` and `DataFormat.String`.

Create a POCO properly adjorned with the MessagePack attributes:

```csharp

```

Now we can use the new transcoder to seamlessly store MessagePack data in Couchbase Server:

```csharp
var msgpackSerializer = new MsgPackSerializer();
var msgpackTranscoder = new MsgPackTranscoder(msgpackSerializer);

var user2 = new User2
{
    Name = "John Smith",
    Age = 27
};

await collection.UpsertAsync("john-smith", user2, options => options.Transcoder(msgpackTranscoder));
```

## [](#further-reading)Further reading

* For _Common flags_, setting the data format used, see the [Data Structures reference](../ref/data-structures.md#common-flags).
* _Format flags_ for ancient SDKs are still available for compatibility, if you are porting a long-lived legacy app. See the [Legacy formats reference](../ref/data-structures.md#legacy-formats).
* If you want to work with binary documents and our Search service, you might like to take a look at <https://github.com/khanium/couchbase-fts-binary>