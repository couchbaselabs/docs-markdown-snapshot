---
title: Transcoders and Non-JSON Documents
description: The Python SDK supports common JSON document requirements out-of-the-box.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.5/modules/howtos/pages/transcoders-nonjson.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:python-sdk:howtos:transcoders-nonjson.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/howtos/transcoders-nonjson.html)

# Transcoders and Non-JSON Documents

> The Python SDK supports common JSON document requirements out-of-the-box. Custom transcoders and serializers provide support for applications needing to perform advanced operations, including supporting non-JSON data. 

The Python SDK uses the concepts of transcoders and serializers, which are used whenever data is sent to or retrieved from Couchbase Server.

> [!NOTE]
> Transcoders are only available for the Couchbase Python Client version `3.2.2` or later. Also, transcoders are only available to key value operations. Operations using search, analytics, query, or views will use the [Python Standard Libary json package](https://docs.python.org/3.8/library/json.html) for serializing and deserializing data.

When sending data to Couchbase, the SDK passes the Object being sent to a transcoder. The transcoder can either reject the Object as being unsupported, or convert it into a `bytes` object and a Common Flag. The Common Flag specifies whether the data is JSON, a non-JSON string, or raw binary data.

On retrieving data from Couchbase, the fetched `bytes` object and Common Flag are passed to a transcoder. The transcoder converts the bytes into an object (the application specifies the required object) if possible.

> [!NOTE]
> Many applications will not need to be aware of transcoders and serializers, as the defaults support most standard JSON use cases. The information in this page is only needed if the application has an advanced use-case, likely involving either non-JSON data, or a requirement for a particular JSON serialization library.

## [](#default-behaviour)Default Behaviour

The `ClusterOptions` contains a global transcoder, which by default is a `JSONTranscoder`.

`JSONTranscoder` uses the [Python Standard Libary json package](https://docs.python.org/3.8/library/json.html) for serializing and deserializing data.

On sending data to Couchbase, `JsonTranscoder` will send Objects to its serializer to convert into a `bytes` object. The serialized bytes are then sent to the Couchbase Server, along with a Common Flag of JSON.

`JSONTranscoder` will pass any object to its serializer, apart from a `bytes` or `bytearray` object. It will reject this with an `ValueFormatException`, as it is ambiguous how it should be handled.

On retrieving data from Couchbase, `JSONTranscoder` passes the fetched `bytes` object and Common Flag to its serializer to convert into a concrete object.

This table summarizes that information, and this more concise form will be used to describe the other transcoders included in the SDK.

| Item            | Result                | Common Flag |
| --------------- | --------------------- | ----------- |
| str             | Results of serializer | JSON        |
| bytes/bytearray | ValueFormatException  | \-          |
| other           | Results of serializer | JSON        |

## [](#rawjsontranscoder)RawJSONTranscoder

The `RawJSONTranscoder` provides the ability for the application to explicitly specify that the data they are storing or retrieving is JSON. This transcoder does not use a serializer, and always performs straight pass through of the data to the server. This enables the application to avoid unnecessary parsing costs when they are certain they are using JSON data.

It only accepts `str` and `bytes` or `bytearray` objects.

| Item            | Result               | Common Flag |
| --------------- | -------------------- | ----------- |
| str             | Passthrough          | JSON        |
| bytes/bytearray | Passthrough          | JSON        |
| Other           | ValueFormatException | \-          |

This transcoder is particularly useful when working with third-party JSON libraries. Here we want to use [orjson](https://pypi.org/project/orjson) for serialization, instead of the default json package:

```python
transcoder = RawJSONTranscoder()
user = {"name": "John Smith", "age": 27}

data = orjson.dumps(user)
try:
    _ = collection.upsert(
        "john-smith", data, UpsertOptions(transcoder=transcoder))
except (ValueFormatException, CouchbaseException) as ex:
    traceback.print_exc()
```

Since orjson has already done the serialization work, we don’t want to use the default `JSONTranscoder`, as this will run the provided string needlessly through `json.loads`. Instead, `RawJSONTranscoder` is used, which just passes through the serialized bytes, and stores them in Couchbase with the JSON Common Flag set.

Similarly, the same transcoder is used on reading the document, so the raw bytes can be retrieved in a string without going through `json.dumps`. orjson can then be used for the deserialization.

```python
try:
    get_result = collection.get("john-smith", GetOptions(transcoder=transcoder))
except (ValueFormatException, CouchbaseException) as ex:
    traceback.print_exc()

decoded = orjson.loads(get_result.value)
assert decoded == user
```

## [](#non-json-transcoders)Non-JSON Transcoders

It is most common to store JSON with Couchbase. However, it is possible to store non-JSON documents, such as raw binary data.

> [!NOTE]
> It’s important to note that the Couchbase Data Platform includes multiple components other than the Key-Value store — including Query and its indexes, FTS (Search), analytics, and eventing — and these are optimized for JSON and will either ignore or provide limited functionality with non-JSON documents.

Also note that some simple data types can be stored directly as JSON, without recourse to non-JSON transcoding. A valid JSON document can be a simple integer (`42`), string (`"hello"`), array (`[1,2,3]`), boolean (`true`, `false`) and the JSON `null` value.

### [](#rawstringtranscoder)RawStringTranscoder

The `RawStringTranscoder` provides the ability for the user to explicitly store and retrieve raw string data with Couchbase. It can be used to avoid the overhead of storing the string as JSON, which requires two bytes for double quotes, plus potentially more for escaping characters.

Note that this transcoder does not accept a serializer, and always performs straight passthrough of the data to the server. It only accepts str objects.

| Item            | Result               | Common Flag |
| --------------- | -------------------- | ----------- |
| str             | Passthrough          | String      |
| bytes/bytearray | ValueFormatException | \-          |
| other           | ValueFormatException | \-          |

Here’s an example of using the `RawStringTranscoder`:

```python
transcoder = RawStringTranscoder()
input_str = "Hello, World!"

try:
    _ = collection.upsert(
        "key", input_str, UpsertOptions(transcoder=transcoder))

    get_result = collection.get("key", GetOptions(transcoder=transcoder))
except (ValueFormatException, CouchbaseException) as ex:
    traceback.print_exc()

assert get_result.value == input_str
```

### [](#rawbinarytranscoder)RawBinaryTranscoder

The `RawBinaryTranscoder` provides the ability for the user to explicitly store and retrieve raw byte data to Couchbase. The transcoder does not perform any form of real transcoding, and does not take a serializer, but rather passes the data through and assigns the appropriate binary Common Flag.

| Item            | Result               | Common Flag |
| --------------- | -------------------- | ----------- |
| str             | ValueFormatException | \-          |
| bytes/bytearray | Passthrough          | Binary      |
| other           | ValueFormatException | \-          |

Here’s an example of using the `RawBinaryTranscoder`:

```python
transcoder = RawBinaryTranscoder()
input_bytes = bytes("Hello, World!", "utf-8")

try:
    _ = collection.upsert(
        "key", input_bytes, UpsertOptions(transcoder=transcoder))

    get_result = collection.get("key", GetOptions(transcoder=transcoder))
except (ValueFormatException, CouchbaseException) as ex:
    traceback.print_exc()

assert get_result.value == input_bytes
```

## [](#custom-transcoders)Custom Transcoders

More advanced transcoding needs can be accomplished if the application implements their own transcoders and serializers.

### [](#creating-a-custom-transcoder)Creating a Custom Transcoder

Let’s look at a more complex example: encoding the JSON alternative, [MessagePack](https://msgpack.org). MessagePack is a compact binary data representation which is custom to our needs, so it should be stored with our with own Common Flag. The Common Flag is chosen by the transcoder, and none of the existing transcoders matches our needs (`RawBinaryTranscoder` does set the binary flag, but it passes data through directly rather than using a serializer, which could also cause issues if you access data through different SDKs). So we need to write one.

We create a transcoder that uses the `msgpack.packb`/`msgpack.unpackb` methods, and sets the our own Common Flag when storing the data:

```python
class MessagePackTranscoder(Transcoder):
    _CUSTOM_FLAGS = (1 << 24) | (ord("M") << 16) | (ord("P") << 8) | (ord("K") << 0)

    def encode_value(self,  # type: "MessagePackTranscoder"
                     value  # type: Any
                     ) -> Tuple[bytes, int]:

        try:
            packed = msgpack.packb(value)
            return packed, self._CUSTOM_FLAGS
        except Exception as ex:
            # Implement custom exception handling
            print("Exception: {}".format(ex))
            raise

    def decode_value(self,  # type: "MessagePackTranscoder"
                     value,  # type: bytes
                     flags  # type: int
                     ) -> bytes:

        if flags != self._CUSTOM_FLAGS:
            raise ValueError("Unexpected flags value.")

        try:
            return msgpack.unpackb(value)
        except Exception as ex:
            # Implement custom exception handling
            print("Exception: {}".format(ex))
            raise
```

Note the use of a private property `_CUSTOM_FLAGS`. We are setting the flags to our own value so that our data cannot be misread by any other SDK accessing the data. We’d have to implement our transcoder in those SDKs too. The `(1 << 24)` value actually corresponds to an internal SDK flag signifying that the datatype is private, we then encode our own `MPK` flag into it.

Now we can use the new transcoder to seamlessly store MessagePack data in Couchbase Server:

```python
transcoder = MessagePackTranscoder()
user = {"name": "John Smith", "age": 27}

try:
    _ = collection.upsert(
        "mpk_key", user, UpsertOptions(transcoder=transcoder))

    get_result = collection.get("mpk_key", GetOptions(transcoder=transcoder))
except (ValueFormatException, CouchbaseException) as ex:
    traceback.print_exc()

assert get_result.value == user
```

See the [msgpack-python docs](https://github.com/msgpack/msgpack-python) for further details on what the package can do.

## [](#further-reading)Further reading

* If you want to work with binary documents and our Search service, you might like to take a look at <https://github.com/khanium/couchbase-fts-binary>