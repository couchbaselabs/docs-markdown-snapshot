---
title: Transcoders and Non-JSON Documents
description: The Ruby SDK supports common JSON document requirements out-of-the-box.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.6/modules/howtos/pages/transcoders-nonjson.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/ruby-sdk/3.6/howtos/transcoders-nonjson.html)

# Transcoders and Non-JSON Documents

> The Ruby SDK supports common JSON document requirements out-of-the-box. Custom transcoders and serializers provide support for applications needing to perform advanced operations, including supporting non-JSON data. 

The Ruby SDK uses the concepts of transcoders and serializers, which are used whenever data is sent to or retrieved from Couchbase Server.

When sending data to Couchbase, the SDK passes the Object being sent to a transcoder. The transcoder can either reject the Object as being unsupported, or convert it into a `byte[]` and a Common Flag. The Common Flag specifies whether the data is JSON, a non-JSON string, or raw binary data. It may, but does not have to, use a serializer to perform the byte conversion.

On retrieving data from Couchbase, the fetched `byte[]` and Common Flag are passed to a transcoder. The transcoder converts the bytes into a concrete class (the application specifies the required type) if possible. It may use a serializer for this.

> [!NOTE]
> Many applications will not need to be aware of transcoders and serializers, as the defaults support most standard JSON use cases. The information in this page is only needed if the application has an advanced use-case, likely involving either non-JSON data, or a requirement for a particular JSON serialization library.

Details of the behavior of the API can be found in the [API documentation](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/JsonTranscoder.html).

## [](#further-reading)Further reading

* If you want to work with binary documents and our Search service, you might like to take a look at <https://github.com/khanium/couchbase-fts-binary>