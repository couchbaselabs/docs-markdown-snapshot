---
title: Migrating to SDK 3 API
description: The SDK 3.x API used in Go SDK 2.x breaks the existing 2.x APIs
  (used in Go SDK 1.6) in order to provide a number of improvements.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.11/modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc
  xref: xref:2.11@go-sdk:project-docs:migrating-sdk-code-to-3.n.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.11/project-docs/migrating-sdk-code-to-3.n.html)

# Migrating to SDK 3 API

> The SDK 3.x API used in Go SDK 2.x breaks the existing 2.x APIs (used in Go SDK 1.6) in order to provide a number of improvements. Collections and Scopes are introduced. The Document class and structure has been completely removed from the API, and the returned values are now typically `Result` type objects. Retry behaviour is more proactive, and lazy bootstrapping moves all error handling to a single place. Individual behaviour changes across services are explained here. 

Go SDK 2.x implements the SDK 3.x API found in the _3.x_ versions of the C, .NET, Java, PHP, and Python SDKs.

## [](#fundamentals)Fundamentals

Before this guide dives into the language-specific technical component of the migration, it is important to understand the high level changes first. As a migration guide, this document assumes you are familiar with the previous generation of the SDK and does not re-introduce SDK API 2 concepts. We recommend familiarizing yourself with the new SDK first by reading at least the [getting started guide](../hello-world/start-using-sdk.md), and browsing through the other chapters a little.

### [](#terminology)Terminology

The concept of a `Cluster` and a `Bucket` remain the same, but a fundamental new layer is introduced into the API: `Collections` and their `Scopes`. Collections are logical data containers inside a Couchbase bucket that let you group similar data just like a _Table_ does in a relational database — although documents inside a collection do not need to have the same structure. Scopes allow the grouping of collections into a namespace, which is very usfeul when you have multilpe tenants acessing the same bucket. Couchbase Server includes support for collections as a [developer preview](#6.5@server:developer-preview:preview-mode.adoc) in version 6.5, and as a first class concept of the programming model from [version 7.0.](../../../server/current/learn/data/scopes-and-collections.md)

Note that the SDKs include the feature from SDK 3.0, to allow easier migration.

In the previous SDK generation, particularly with the `KeyValue` API, the focus has been on the codified concept of a `Document`. Documents were read and written and had a certain structure, including the `id`/`key`, content, expiry (`ttl`), and so forth. While the server still operates on the logical concept of documents, we found that this model in practice didn't work so well for client code in certain edge cases. As a result we have removed the `Document` class/structure completely from the API. The new API follows a clear scheme: each command takes required arguments explicitly, and an option block for all optional values. The returned value is always of type `Result`. This avoids method overloading bloat in certain languages, and has the added benefit of making it easy to grasp APIs evenly across services.

As an example here is a KeyValue document fetch:

```golang
getResult, err := collection.Get("key", &gocb.GetOptions{
	Timeout: 2 * time.Second,
})
```

Compare this to a [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) query:

```golang
queryResult, err := cluster.Query("select 1=1", &gocb.QueryOptions{
	Timeout: 3 * time.Second,
})
```

Since documents also fundamentally handled the serialization aspects of content, two new concepts are introduced: the `Serializer` and the `Transcoder`. Out of the box the SDKs ship with a JSON serializer which handles the encoding and decoding of JSON. You'll find the serializer exposes the options for methods like SQL++ queries and KeyValue subdocument operations,.

The KV API extends the concept of the serializer to the `Transcoder`. Since you can also store non-JSON data inside a document, the `Transcoder` allows the writing of binary data as well. It handles the object/entity encoding and decoding, and if it happens to deal with JSON makes uses of the configured `Serializer` internally. See the _Serialization and Transcoding_ section below for details.

### [](#what-to-look-out-for)What to look out for

The SDKs are more proactive in retrying with certain errors and in certain situations, within the timeout budget given by the user — as an example, temporary failures or locked documents are now being retried by default — making it even easier to program against certain error cases. This behavior is customizable in a `RetryStrategy`, which can be overridden on a per operation basis for maximum flexibility if you need it.

Note, most of the bootstrap sequence is now lazy (happening behind the scenes). For example, opening a bucket is not raising an error anymore, but it will only show up once you perform an actual operation. The reason behind this is to spare the application developer the work of having to do error handling in more places than needed. A bucket can go down 2ms after you opened it, so you have to handle request failures anyway. By delaying the error into the operation result itself, there is only one place to do the error handling. There will still be situations why you want to check if the resource you are accessing is available before continuing the bootstrap; for this, we have the diagnostics and ping commands at each level which allow you to perform those checks eagerly.

## [](#language-specifics)Language Specifics

Now that you are familiar with the general theme of the migration, the next sections dive deep into the specifics. First, installation and configuration are covered, then we talk about exception handling, and then each service (i.e. Key/Value, Query,…​) is covered separately.

### [](#installation-and-configuration)Installation and Configuration

The Go SDK 2.x is available for download using the go modules system. All releases are posted to the couchbase/gocb GitHub repository and can be used by simply importing `github.com/couchbase/gocb/v2` and invoking `go get`.

> [!IMPORTANT]
> Go SDK 2.x has a minimum required Go version of 1.19, although we recommend running the latest LTS version with the highest patch version available.

Almost all configuration for the SDK can be specified through the ConnectOptions which are passed to the `gocb.Connect` call in the SDK. In addition to this, as with SDK 2.0, the majority of these options can also be specified through the connection string. See the appropriate documentation for more information.

#### [](#authentication)Authentication

Since Go SDK 1.x supports Couchbase Server clusters older than 5.0, it had to support both Role-Based access control as well as bucket-level passwords. The minimum cluster version supported by SDK 2.x is Server 5.0, which means that only RBAC is supported. This is why you can set the username and password when directly connecting:

```golang
opts := gocb.ClusterOptions{
	Username: "Administrator",
	Password: "password",
}
cluster, err := gocb.Connect("10.112.193.101", opts)
if err != nil {
	panic(err)
}
```

This is just shorthand for:

```golang
opts := gocb.ClusterOptions{
	Authenticator: gocb.PasswordAuthenticator{
		Username: "Administrator",
		Password: "password",
	},
}
cluster, err := gocb.Connect("10.112.193.101", opts)
if err != nil {
	panic(err)
}
```

The reason why you can pass in a specific authenticator is that you can also use the same approach to configure certificate-based authentication:

```golang
cert, err := tls.LoadX509KeyPair("mycert.pem", "mykey.pem")
if err != nil {
	panic(err)
}

opts := gocb.ClusterOptions{
	Authenticator: gocb.CertificateAuthenticator{
		ClientCertificate: &cert,
	},
}
cluster, err := gocb.Connect("10.112.193.101", opts)
if err != nil {
	panic(err)
}
```

Please see the documentation on certificate-based authentication for detailed information on how to configure this properly.

### [](#connection-lifecycle)Connection Lifecycle

From a high-level perspective, bootstrapping and shutdown is very similar to Go 1.x. One notable difference is that the `Collection` is introduced and that the individual methods like `Bucket` immediately return, and cannot error. Compare SDK 2: the `OpenBucket` method would return an error if it could not open the bucket.

The reason behind this change is that even if a bucket can be opened, a millisecond later it may not be available any more. All this state has been moved into the actual operation so there is only a single place where the error handling needs to take place. This simplifies error handling and retry logic for an application.

In SDK 1, you connected, opened a bucket, performed a KV op, and disconnected like this:

```golang
cluster, _ := gocb.Connect("127.0.0.1")
cluster.Authenticate(PasswordAuthenticator{
    Username: "user",
    Password: "pass"
})

bucket, _ := cluster.OpenBucket("travel-sample")

getResult, _ := bucket.Get("airline_10", nil)

bucket.Close()
```

Here is the SDK 2 equivalent:

```golang
bucket := cluster.Bucket("travel-sample")
collection := bucket.Scope("inventory").Collection("airport")

getResult, err := collection.Get("key", &gocb.GetOptions{
	Timeout: 2 * time.Second,
})
```

`Collections` are generally available from Couchbase Server version 7.0, which the SDK is already compatible with. If you are using a Couchbase Server version which does not support `Collections`, always use the `DefaultCollection()` method to access the KV API; it will map to the full bucket.

> [!IMPORTANT]
> You'll notice that `Bucket(string)` returns immediately, even if the bucket resources are not completely opened. This means that the subsequent `Get` operation may be dispatched even before the socket is open in the background. The SDK will handle this case transparently, and reschedule the operation until the bucket is opened properly. This also means that if a bucket could not be opened (say, because no server was reachable) the operation will time out. Please check the logs to see the cause of the timeout (in this case, you'll see socket connect rejections).

Also note, you will now find Query, Search, and Analytics at the `Cluster` level. This is where they logically belong. If you are using Couchbase Server 6.5 or later, you will be able to perform cluster-level queries even if no bucket is open. If you are using an earlier version of the cluster you must open at least one bucket, otherwise cluster-level queries will fail.

### [](#serialization-and-transcoding)Serialization and Transcoding

In SDK 2 the main method to control transcoding was through specfying unique Transcoder instances at the top-level. This concept has been extended to enable developers to specify per-operation Transcoder instances.

Additionally, the default transcoder has been modified to no longer transcoder byte-arrays as a precaution against accidentally encoding strings as JSON or JSON as strings. A new LegacyTranscoder has been implemented which mirrors Go SDK 1.x's behaviour.

### [](#encryption)Encryption

Field Level Encryption is a separate library requiring, for Go SDK 2.x, SDK 2.2.0 or more recent. Differences between the 1.x and 2.x implementations, and an upgrade path, are discussed in the [Field-Level Encryption documentation](../howtos/encrypting-using-sdk.md#migration-from-sdk1).

### [](#error-handling)Error Handling

How to handle errors has remained relatively unchanged from Go SDK 1.x and continues to follow the idiomatic Go ideology of returning errors via a parameter.

However in Go SDK 2.x, we have updated our code to follow the latest Go error handling best practices and provide an improved error interface using the `errors.As` and `errors.Is` methods.

In version 1.x of the SDK, you may receive an error and compare it directly to one of the `gocb.ErrSomething` errors:

```golang
res, err := bucket.Get("airline_10", nil)
if err == gocb.ErrKeyNotFound {
  // handle the error
}
```

In version 2.x of the SDK, you should instead now check using the `errors.Is` method:

```golang
if errors.Is(err, gocb.ErrDocumentNotFound) {
	// handle your error
}
```

In addition, 2.x of the SDK provides the ability to gather additional contextual information about why your operation failed through the various error types:

```golang
	if errors.Is(err, gocb.ErrDocumentNotFound) {
		var kverr gocb.KeyValueError
		if errors.As(err, &kverr) {
			log.Printf("Error Context: %+v\n", kverr)
		}
	}
	log.Printf("Get Result: %+v\n", getResult)

	queryResult, err := cluster.Query("select 1=1", &gocb.QueryOptions{
		Timeout: 3 * time.Second,
	})
	log.Printf("Query Result: %+v\n", queryResult)

	cluster.Close(&gocb.ClusterCloseOptions{})
}

func passauthenticator() {
	opts := gocb.ClusterOptions{
		Authenticator: gocb.PasswordAuthenticator{
			Username: "Administrator",
			Password: "password",
		},
	}
	cluster, err := gocb.Connect("10.112.193.101", opts)
	if err != nil {
		panic(err)
	}

	cluster.Close(&gocb.ClusterCloseOptions{})
}

func certauthenticator() {
	cert, err := tls.LoadX509KeyPair("mycert.pem", "mykey.pem")
	if err != nil {
		panic(err)
	}

	opts := gocb.ClusterOptions{
		Authenticator: gocb.CertificateAuthenticator{
			ClientCertificate: &cert,
		},
	}
	cluster, err := gocb.Connect("10.112.193.101", opts)
	if err != nil {
		panic(err)
	}

	cluster.Close(&gocb.ClusterCloseOptions{})
}

func main() {
	basic()
	passauthenticator()
	certauthenticator()
}
```

## [](#comparing-older-documentation)Comparing Older Documentation

You may want to visit documentation for older versions of the SDK, to help to understand application code that you are migrating. Versions that have reached end of life can be found in the [archive](https://docs-archive.couchbase.com/home/index.html). In the release notes pages of these older docs, you will also find links to the API reference for each no-longer-supported release.