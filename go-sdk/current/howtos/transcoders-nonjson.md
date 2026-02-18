---
title: Transcoders and Non-JSON Documents
description: The Go SDK supports common JSON document requirements out-of-the-box.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.11/modules/howtos/pages/transcoders-nonjson.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/go-sdk/current/howtos/transcoders-nonjson.html)

# Transcoders and Non-JSON Documents

> The Go SDK supports common JSON document requirements out-of-the-box. Custom transcoders and serializers provide support for applications needing to perform advanced operations, including supporting non-JSON data. 

The Go SDK uses the concept of transcoders, which are used whenever key-value data is sent to or retrieved from Couchbase Server.

> [!NOTE]
> Transcoders are only available to key value operations. Operations using search, analytics, query, or views will use the [json package](https://golang.org/doc/articles/json%5Fand%5Fgo.html) for serializing and deserializing data.

When sending data to Couchbase, the SDK passes the data being sent to a transcoder. The transcoder can either reject the data as being unsupported, or convert it into a `[]byte` and a Common Flag. The Common Flag specifies whether the data is JSON, a non-JSON string, or raw binary data.

On retrieving key-value data from Couchbase, the fetched `[]byte` and Common Flag are passed to a transcoder. The transcoder converts the bytes into a type (the application provides a pointer to a variable) if possible.

> [!NOTE]
> Many applications will not need to be aware of transcoders, as the defaults support most standard JSON use cases. The information in this page is only needed if the application has an advanced use-case, likely involving either non-JSON data, or a requirement for a particular JSON serialization library.

## [](#default-behaviour)Default Behaviour

The `ClusterOptions` specify a global transcoder, which by default is a `JSONTranscoder`.

`JSONTranscoder` uses the [json package](https://golang.org/doc/articles/json%5Fand%5Fgo.html) for serializing and deserializing data.

On sending data to Couchbase, `JSONTranscoder` will send the data to its serializer to convert into a `[]byte`. The serialized bytes are then sent to the Couchbase Server, along with a Common Flag of JSON.

`JSONTranscoder` will pass any data type to its serializer, apart from a `[]byte`. It will reject this with an error, as it is ambiguous how it should be handled.

On retrieving data from Couchbase, `JSONTranscoder` passes the fetched `[]byte` and Common Flag to its serializer to convert into a concrete value.

This table summarizes that information, and this more concise form will be used to describe the other transcoders included in the SDK.

| Item     | Result                | Common Flag |
| -------- | --------------------- | ----------- |
| string   | Results of serializer | JSON        |
| \[\]byte | error                 | \-          |
| Other    | Results of serializer | JSON        |

## [](#rawjsontranscoder)RawJSONTranscoder

The RawJSONTranscoder provides the ability for the application to explicitly specify that the data they are storing or retrieving is JSON. This transcoder does not use a serializer, and always performs straight pass through of the data to the server. This enables the application to avoid unnecessary parsing costs when they are certain they are using JSON data.

It only accepts Strings and `[]byte`.

| Item     | Result                   | Common Flag |
| -------- | ------------------------ | ----------- |
| string   | Passthrough              | JSON        |
| \[\]byte | Passthrough              | JSON        |
| Other    | InvalidArgumentException | \-          |

This transcoder is particularly useful when working with third-party JSON libraries. Here we want to use [ffjson](https://github.com/pquerna/ffjson) for serialization, instead of the default json package:

```golang
	user := User{Name: "John Smith", Age: 27}
	transcoder := gocb.NewRawJSONTranscoder()

	b, err := ffjson.Marshal(user)
	if err != nil {
		panic(err)
	}

	_, err = collection.Upsert("john-smith", b, &gocb.UpsertOptions{
		Transcoder: transcoder,
	})
	if err != nil {
		panic(err)
	}
```

Since ffjson has already done the serialization work, we don’t want to use the default `JSONTranscoder`, as this will run the provided string needlessly through `json.Marshal`. Instead, RawJSONTranscoder is used, which just passes through the serialized bytes, and stores them in Couchbase with the JSON Common Flag set.

Similarly, the same transcoder is used on reading the document, so the raw bytes can be retrieved in a string without going through `json.Unmarshal`. ffjson can then be used for the deserialization.

```golang
	getRes, err := collection.Get("john-smith", &gocb.GetOptions{
		Transcoder: transcoder,
	})
	if err != nil {
		panic(err)
	}

	var returned []byte
	err = getRes.Content(&returned)
	if err != nil {
		panic(err)
	}

	err = ffjson.Unmarshal(returned, &user)
	if err != nil {
		panic(err)
	}
```

## [](#non-json-transcoders)Non-JSON Transcoders

It is most common to store JSON with Couchbase. However, it is possible to store non-JSON documents, such as raw binary data, perhaps using an concise binary encoding like [MessagePack](https://msgpack.org) or [CBOR](https://cbor.io/), in the Key-Value store.

> [!NOTE]
> It’s important to note that the Couchbase Data Platform includes multiple components other than the Key-Value store — including [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) and its indexes, FTS (Search), analytics, and eventing — and these are optimized for JSON and will either ignore or provide limited functionality with non-JSON documents.

Also note that some simple data types can be stored directly as JSON, without recourse to non-JSON transcoding. A valid JSON document can be a simple integer (`42`), string (`"hello"`), array (`[1,2,3]`), boolean (`true`, `false`) and the JSON `null` value.

### [](#rawstringtranscoder)RawStringTranscoder

The RawStringTranscoder provides the ability for the user to explicitly store and retrieve raw string data with Couchbase. It can be used to avoid the overhead of storing the string as JSON, which requires two bytes for double quotes, plus potentially more for escaping characters.

Note that this transcoder does not accept a serializer, and always performs straight passthrough of the data to the server. It only accepts Strings.

| Item     | Result      | Common Flag |
| -------- | ----------- | ----------- |
| string   | Passthrough | String      |
| \[\]byte | error       | \-          |
| Other    | error       | \-          |

Here’s an example of using the `RawStringTranscoder`:

```golang
	input := "hello world"
	transcoder := gocb.NewRawStringTranscoder()

	_, err = collection.Upsert("key", input, &gocb.UpsertOptions{
		Transcoder: transcoder,
	})
	if err != nil {
		panic(err)
	}

	getRes, err := collection.Get("key", &gocb.GetOptions{
		Transcoder: transcoder,
	})
	if err != nil {
		panic(err)
	}

	var returned string
	err = getRes.Content(&returned)
	if err != nil {
		panic(err)
	}
```

### [](#rawbinarytranscoder)RawBinaryTranscoder

The RawBinaryTranscoder provides the ability for the user to explicitly store and retrieve raw byte data to Couchbase. The transcoder does not perform any form of real transcoding, and does not take a serializer, but rather passes the data through and assigns the appropriate binary Common Flag.

| Item     | Result      | Common Flag |
| -------- | ----------- | ----------- |
| string   | error       | \-          |
| \[\]byte | Passthrough | Binary      |
| Other    | error       | \-          |

Here’s an example of using the `RawBinaryTranscoder`:

```golang
	input := []byte("hello world")
	transcoder := gocb.NewRawBinaryTranscoder()

	_, err = collection.Upsert("key", input, &gocb.UpsertOptions{
		Transcoder: transcoder,
	})
	if err != nil {
		panic(err)
	}

	getRes, err := collection.Get("key", &gocb.GetOptions{
		Transcoder: transcoder,
	})
	if err != nil {
		panic(err)
	}

	var returned []byte
	err = getRes.Content(&returned)
	if err != nil {
		panic(err)
	}
```

## [](#custom-transcoders)Custom Transcoders

More advanced transcoding needs can be accomplished if the application implements their own transcoders and serializers.

### [](#creating-a-custom-transcoder)Creating a Custom Transcoder

Let’s look at a more complex example: encoding the JSON alternative, [MessagePack](https://msgpack.org). MessagePack is a compact binary data representation which is custom to our needs, so it should be stored with our with own Common Flag. The Common Flag is chosen by the transcoder, and none of the existing transcoders matches our needs (`RawBinaryTranscoder` does set the binary flag, but it passes data through directly rather than using a serializer, which could also cause issues if you access data through different SDKs). So we need to write one.

We create a transcoder that uses the `msgp.Marshaler`/`msgp.Unmarshaler` interfaces, and sets the our own Common Flag when storing the data:

```golang
const customFlags = (0x02 << 24) | ('M' << 16) | ('P' << 8) | ('K' << 0)

type MsgPackTranscoder struct {
}

func (t *MsgPackTranscoder) Encode(value interface{}) ([]byte, uint32, error) {
	msgPckVal, ok := value.(msgp.Marshaler)
	if !ok {
		return nil, 0, errors.New("MsgPackTranscoder only supports types that satisfy msgp.Marshaler")
	}

	data, err := msgPckVal.MarshalMsg(nil)
	if err != nil {
		return nil, 0, err
	}

	return data, customFlags, nil
}

func (t *MsgPackTranscoder) Decode(bytes []byte, flags uint32, out interface{}) error {
	if flags != customFlags {
		return errors.New("unexpected expectedFlags value")
	}

	msgPckVal, ok := out.(msgp.Unmarshaler)
	if !ok {
		return errors.New("MsgPackTranscoder only supports types that satisfy msgp.Unmarshaler")
	}

	var err error
	out, err = msgPckVal.UnmarshalMsg(bytes)
	if err != nil {
		return err
	}

	return nil
}
```

Note the use of `customFlags`. We are setting the flags to our own value so that our data cannot be misread by any other SDK accessing the data. We’d have to implement our transcoder in those SDKs too. The `0x02 << 24` value actually corresponds to an internal sdk flag signifying that the datatype is private, we then encode our own MsgPacK flag into it.

Now we can use the new transcoder to seamlessly store MessagePack data in Couchbase Server:

```golang
	transcoder := &MsgPackTranscoder{}

	_, err := collection.Upsert("key", input, &gocb.UpsertOptions{
		Transcoder: transcoder,
	})
	if err != nil {
		panic(err)
	}

	getRes, err := collection.Get("key", &gocb.GetOptions{
		Transcoder: transcoder,
	})
	if err != nil {
		panic(err)
	}

	var returned []byte
	err = getRes.Content(&returned)
	if err != nil {
		panic(err)
	}
```

Note that `input` in this example must be a type that has been enhanced using the [msgpack tooling](https://github.com/tinylib/msgp/wiki/Getting-Started).

## [](#further-reading)Further reading

* For _Common flags_, setting the data format used, see the [Data Structures reference](../ref/data-structures.md#common-flags).
* _Format flags_ for ancient SDKs are still available for compatibility, if you are porting a long-lived legacy app. See the [Legacy formats reference](../ref/data-structures.md#legacy-formats).
* If you want to work with binary documents and our Search service, you might like to take a look at <https://github.com/khanium/couchbase-fts-binary>