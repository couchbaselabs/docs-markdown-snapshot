---
title: Transcoders and Non-JSON Documents
description: The Node SDK supports common JSON, string and binary document
  requirements out-of-the-box.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.4/modules/howtos/pages/transcoders-nonjson.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:4.4@nodejs-sdk:howtos:transcoders-nonjson.adoc[]
---

[View original HTML](/nodejs-sdk/4.4/howtos/transcoders-nonjson.html)

# Transcoders and Non-JSON Documents

> The Node SDK supports common JSON, string and binary document requirements out-of-the-box. Custom transcoders and serializers provide support for applications needing to perform advanced operations, including supporting non-JSON data. 

The Node SDK uses the concepts of transcoders and serializers, which are used whenever data is sent to or retrieved from Couchbase Server.

When sending data to Couchbase, the SDK passes the Object being sent to a transcoder. The transcoder can either reject the Object as being unsupported, or convert it into a `Buffer` and a Common Flag. The Common Flag specifies whether the data is JSON, a non-JSON string, or raw binary data. It may, but does not have to, use a serializer to perform the byte conversion.

On retrieving data from Couchbase, the fetched `Buffer` and Common Flag are passed to a transcoder. The transcoder converts the bytes into a concrete class (the application specifies the required type) if possible. It may use a serializer for this.

> [!NOTE]
> Many applications will not need to be aware of transcoders and serializers, as the defaults support most standard JSON use cases. The information in this page is only needed if the application has an advanced use-case, likely involving either non-JSON data, non-string data, non-binary data, or a requirement for a particular JSON serialization library.

## [](#default-behaviour)Default Behaviour

The `ClusterEnvironment` contains a global transcoder, which by default is `defaulttranscoder`.

On sending data to Couchbase, `defaulttranscoder` will send Buffer objects through untouched, string objects to Buffer.from(obj), and other objects through JSON.stringify(obj) and then Buffer.from(…​) JSON.stringify will reject any non JSON object with 'bad value passed'. The serialized bytes are then sent to the Couchbase Server, along with a Common Flag of JSON.

On retrieving data from Couchbase, `defaulttranscoder` passes the fetched `Buffer` and Common Flag to its serializer (`DefaultJsonSerializer` by default) to convert into a concrete class.

This table summarizes that information, and this more concise form will be used to describe the other transcoders included in the SDK.

| Item                   | Result          | Common Flag  |
| ---------------------- | --------------- | ------------ |
| String                 | String → Buffer | CF\_UTF8     |
| NF\_UTF8               | Buffer          | Buffer       |
| CF\_RAW                | NF\_RAW         | Other Object |
| JSON → String → Buffer | CF\_JSON        | NF\_JSON     |

## [](#non-json-transcoders)Non-JSON Transcoders

It is most common to store JSON with Couchbase. However, it is possible to store non-JSON documents, such as raw binary data.

> [!NOTE]
> It’s important to note that the Couchbase Data Platform includes multiple components other than the Key-Value store — including Query and its indexes, FTS, Analytics, and Eventing — and these are optimized for JSON and will either ignore or provide limited functionality with non-JSON documents.

Also note that some simple data types can be stored directly as JSON, without recourse to non-JSON transcoding. A valid JSON document can be a simple integer (`42`), string (`"hello"`), array (`[1,2,3]`), boolean (`true`, `false`) and the JSON `null` value.

The following examples of a RawStringTranscoder and a RawBinaryTranscoder are somewhat contrived, as the defaulttranscoder provices support for both string and binary (Buffer) objects.

### [](#rawstringtranscoder)RawStringTranscoder

The RawStringTranscoder provides the ability for the user to explicitly store and retrieve raw string data with Couchbase. It can be used to avoid the overhead of storing the string as JSON, which requires two bytes for double quotes, plus potentially more for escaping characters.

Note that this transcoder does not accept a serializer, and always performs straight passthrough of the data to the server. It only accepts strings.

| Item     | Result          | Common Flag             |
| -------- | --------------- | ----------------------- |
| String   | String → Buffer | CF\_UTF8                |
| NF\_UTF8 | anything else   | Error: bad value passed |

Here’s an example of using the `RawStringTranscoder`:

```javascript
try {
    await collection.upsert('string_123', 'my string',
        { transcoder: new RawStringTranscoder() },
    ).catch((e) => { console.log("caught exception from upsert: "); console.log(e); console.log(e.cause) });
} catch (e) {
    console.log("try/catch: ");
    console.log(e);
    return h.response(e.toString());
}

try {
    const result = await collection.get(key,
        { transcoder: new RawStringTranscoder() }
    ).catch((e) => { console.log("caught exception from get: "); console.log(e); console.log(e.cause) });
    var output = result.value;
    console.log('output : type=' + (typeof output) + ' value=' + output);
    return h.response(output);
} catch (e) {
    console.log("get try/catch: ");
    console.log(e);
    return h.response(e.toString());
}
```

### [](#rawbinarytranscoder)RawBinaryTranscoder

The RawBinaryTranscoder provides the ability for the user to explicitly store and retrieve raw byte data to Couchbase. The transcoder does not perform any form of real transcoding, and does not take a serializer, but rather passes the data through and assigns the appropriate binary Common Flag.

| Item    | Result        | Common Flag             |
| ------- | ------------- | ----------------------- |
| Buffer  | Buffer        | CF\_RAW                 |
| NF\_RAW | anything else | Error: bad value passed |

Here’s an example of using the `RawBinaryTranscoder`:

```jvascript
try {
    await collection.upsert('binary_123', Buffer.from('my binary'),
        { transcoder: new RawBinaryTranscoder() },
    ).catch((e) => console.log(e));
} catch (e) {
    console.log(e);
    return h.response(e.toString());
}

try {
    const result = await collection.get(key,
        { transcoder: new RawBinaryTranscoder() },
    )
    var output = result.value;
    return h.response(output);
} catch (e) {
    console.log(e);
    return h.response(e.toString());
}
```

## [](#custom-transcoders-and-serializers)Custom Transcoders and Serializers

More advanced transcoding needs can be accomplished if the application implements their own transcoders and serializers.

### [](#creating-a-custom-transcoder)Creating a Custom Transcoder

We saw above two examples of custom transcoders with `RawStringTranscoder` and `RawBinaryTranscoder`

It’s easy to create a transcoders. Simply implement the Transcoder interface’s two methods:

```javascript
/**
 * Transcoder provides an interface for performing custom transcoding
 * of document contents being retrieved and stored to the cluster.
 *
 * @interface
 */
class Transcoder {
  /**
   * @param {*} value
   *
   * @returns {Pair.<Buffer, number>}
   */
  encode(value) {
    throw new Error('not implemented');
  }

  /**
   * @param {Buffer} bytes
   * @param {number} flags
   *
   * @returns {*}
   */
  decode(bytes, flags) {
    throw new Error('not implemented');
  }
}
```

```javascript
encode(value) {
  // If its a string, encode it as a UTF8 string.
  if (typeof value === 'string') {
    return [
      Buffer.from(value),
      CF_UTF8 | NF_UTF8
    ];
  }
  const myErr = new Error('encode - InvalidArgumentException');
  console.log("encode is going to throw");
  console.log(myErr);
  throw myErr;
}
```

And for decoding:

```javascript
decode(bytes, flags) {
  var format = flags & NF_MASK;
  var cfformat = flags & CF_MASK;

  if (cfformat === CF_UTF8) {
    format = NF_UTF8;
    return bytes.toString('utf8');
  } 
  const myErr = new Error('decode - InvalidArgumentException');
  console.log("decode is going to throw");
  console.log(myErr);
  throw myErr;
}
```

## [](#further-reading)Further reading

See the [Legacy formats reference](../ref/data-structures.md#legacy-formats). \* If you want to work with binary documents and our Search service, you might like to take a look at <https://github.com/khanium/couchbase-fts-binary>