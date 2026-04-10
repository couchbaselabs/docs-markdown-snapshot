---
title: Transcoders &amp; Non-JSON Documents
description: The Rust SDK supports common JSON document requirements out-of-the-box.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/transcoders-nonjson.adoc
pubDate: 2026-04-10T05:25:10.333Z
link: xref:rust-sdk:howtos:transcoders-nonjson.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/howtos/transcoders-nonjson.html)

# Transcoders &amp; Non-JSON Documents

> The Rust SDK supports common JSON document requirements out-of-the-box. Custom transcoders and serializers provide support for applications needing to perform advanced operations, including supporting non-JSON data. 

The Rust SDK uses the concepts of transcoders, which are used whenever data is sent to or retrieved from Couchbase Server.

When sending data to Couchbase, the SDK passes the object being sent to a transcoder. The transcoder can either reject the object as being unsupported, or convert it into a `byte[]` and a Common Flag. The Common Flag specifies whether the data is JSON, a non-JSON string, or raw binary data.

Transcoders in the Rust SDK work a little differently to other SDKs. The SDK exposes a number of `{operation-name}_raw` functions for supporting types that do not implement `Serialize` and/or should not be serialized to JSON using `serde_json`. Transcoding with these functions occurs outside the function, to be idiomatic to the Rust ecosystem. Owing to a lack of reflection in Rust, the transcoders implemented in the SDK do not work in the same way as other SDKs. We'll explore how this works in the examples below.

On retrieving data from Couchbase, the fetched `byte[]` and Common Flag are passed to a transcoder. The transcoder converts the bytes into a concrete type (the application specifies the required type) if possible.

> [!NOTE]
> Many applications will not need to be aware of transcoders, as the defaults support most standard JSON use cases. The information in this page is only needed if the application has an advanced use-case, likely involving either non-JSON data, or a requirement for a particular JSON serialization library.

## [](#default-behaviour)Default Behaviour

By default, the SDK will use `couchbase::transcoding::json` for serialization and deserialization, which leverages `serde_json`.

## [](#rawjsontranscoder)RawJsonTranscoder

The RawJsonTranscoder provides the ability for the application to explicitly specify that the data they are storing or retrieving is JSON. This transcoder always performs straight pass through of the data to the server. This enables the application to avoid unnecessary parsing costs when they are certain they are using JSON data.

```rust
let value = r#"{"type":"raw_json","name":"Raw JSON Example"}"#;

// This effectively does nothing more than convert &str to &[u8] and set the flags to indicate JSON.
let (encoded, flags) = raw_json::encode(&value)?;

collection
    .upsert_raw("doc-id", encoded, flags, None)
    .await?;

let doc = collection.get("doc-id", None).await?;
let (content_raw, flags) = doc.content_as_raw();

// value will be of type &[u8]
let value = raw_json::decode(content_raw, flags)?;
```

## [](#non-json-transcoders)Non-JSON Transcoders

It is most common to store JSON with Couchbase. However, it is possible to store non-JSON documents, such as raw binary data, perhaps using an concise binary encoding like [MessagePack](https://msgpack.org) or [CBOR](https://cbor.io/), in the Key-Value store.

> [!NOTE]
> It's important to note that the Couchbase Data Platform includes multiple components other than the Key-Value store — including Query and its indexes, Search Service, Analytics, and Eventing — and these are optimized for JSON and will either ignore or provide limited functionality with non-JSON documents.

Also note that some simple data types can be stored directly as JSON, without recourse to non-JSON transcoding. A valid JSON document can be a simple integer (`42`), string (`"hello"`), array (`[1,2,3]`), boolean (`true`, `false`) and the JSON `null` value.

### [](#rawstringtranscoder)RawStringTranscoder

The RawStringTranscoder provides the ability for the user to explicitly store and retrieve raw string data with Couchbase. It can be used to avoid the overhead of storing the string as JSON, which requires two bytes for double quotes, plus potentially more for escaping characters.

```rust
let value = "This is a raw string";

// This effectively does nothing more than convert &str to &[u8] and set the flags to indicate a raw string.
let (encoded, flags) = raw_string::encode(&value)?;

collection
    .upsert_raw("doc-id", encoded, flags, None)
    .await?;

let doc = collection.get("doc-id", None).await?;
let (content_raw, flags) = doc.content_as_raw();

// value will be of type &str
let value = raw_string::decode(content_raw, flags)?;
```

### [](#rawbinarytranscoder)RawBinaryTranscoder

The RawBinaryTranscoder provides the ability for the user to explicitly store and retrieve raw byte data to Couchbase. The transcoder does not perform any form of real transcoding, and does not take a serializer, but rather passes the data through and assigns the appropriate binary Common Flag.

```rust
let value: &[u8] = b"This is raw binary";

// This effectively does nothing more than take &[u8] and set the flags to indicate binary data.
let (encoded, flags) = raw_binary::encode(&value)?;

collection
    .upsert_raw("doc-id", encoded, flags, None)
    .await?;

let doc = collection.get("doc-id", None).await?;
let (content_raw, _flags) = doc.content_as_raw();

// value will be of type &[u8]
let value = raw_binary::decode(content_raw, flags)?;
```

## [](#custom-transcoders)Custom Transcoders

More advanced transcoding needs can be accomplished if the application implements their own transcoders.

### [](#creating-a-custom-transcoder)Creating a Custom Transcoder

Let's look at a more complex example: encoding the JSON alternative, [MessagePack](https://msgpack.org). MessagePack is a compact binary data representation, so it should be stored with the binary Common Flag. The Common Flag is chosen by the transcoder, and none of the existing transcoders matches our needs (`raw_binary` does set the binary flag, but it passes data through directly rather than using a serializer). So we need to write one.

Create a transcoder that uses the `rmp_serde` crate to serialize/deserialize and sets the binary Common Flag when storing the data:

```rust
pub fn encode_msg_pack<T>(value: T) -> Result<(Vec<u8>, u32), rmp_serde::encode::Error>
where
    T: serde::Serialize,
{
    let encoded = rmp_serde::to_vec(&value)?;
    Ok((
        encoded,
        couchbase::transcoding::encode_common_flags(couchbase::transcoding::DataType::Binary),
    ))
}

pub fn decode_msg_pack<T>(encoded: &[u8], _flags: u32) -> Result<T, rmp_serde::decode::Error>
where
    T: DeserializeOwned,
{
    rmp_serde::from_slice(encoded)
}
```

Note this transcoder is completely independent to MessagePack. All it does is pass data to and from a serializer, and set a Binary Common Flag.

Now we can use the new transcoder to seamlessly store MessagePack data in Couchbase Server:

```rust
#[derive(serde::Serialize, serde::Deserialize, PartialEq, Debug)]
struct User {
    field1: String,
    field2: i32,
}

let user = User {
    field1: "value1".to_string(),
    field2: 42,
};

// Unwrap for simplicity in this example; production code should handle the error.
let (encoded, flags) = encode_msg_pack(&user).unwrap();

collection
    .upsert_raw("john-smith", &encoded, flags, None)
    .await?;

let doc = collection.get("doc-id", None).await?;
let (content_raw, flags) = doc.content_as_raw();

// Unwrap for simplicity in this example; production code should handle the error.
let decoded: User = decode_msg_pack(content_raw, flags).unwrap();

assert_eq!(user, decoded);
```

## [](#further-reading)Further reading

* If you want to work with binary documents and our Search Service, you might like to take a look at <https://github.com/khanium/couchbase-fts-binary>