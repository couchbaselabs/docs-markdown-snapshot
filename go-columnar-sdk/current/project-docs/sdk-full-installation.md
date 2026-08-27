---
title: Full Installation
description: Installation instructions for the Couchbase Go Client.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-columnar-sdk-go/edit/release/1.0/modules/project-docs/pages/sdk-full-installation.adoc
  xref: xref:go-columnar-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-columnar-sdk/current/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions for the Couchbase Go Client. 

Columnar SDKs are developed from the ground-up and while they maintain some syntactic similarities with the [operational SDKs](../../../home/sdk.md), they are purpose built for Columnar's analytical use cases. They support streaming APIs to handle large datasets, as well as the common features expected to be present in any modern database SDK — such as connection management and robust error handling.

## [](#installing-the-sdk)Installing the SDK

The Go Columnar SDK has added support for [Go Modules](https://github.com/golang/go/wiki/Modules). You can use `go get` to download the SDK:

> [!IMPORTANT]
> `go get` only works if you have initialised a [Go module](https://go.dev/blog/using-go-modules), and have a `go.mod` file in your working directory.

```console
$ go get github.com/couchbase/gocbcolumnar@v1.0.0
```

> [!NOTE]
> In line with the [Golang project](https://golang.org/doc/devel/release.html#policy), Couchbase supports both the current, and the previous, versions of Go. Earlier versions may work, but are not supported.

Information about new features, fixes, and known issues — as well as information about how to install earlier release versions — is in the [release notes](columnar-sdk-release-notes.md).