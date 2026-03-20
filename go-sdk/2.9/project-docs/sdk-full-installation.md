---
title: Full Installation
description: Installation instructions for the Couchbase Go Client.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.9/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.9@go-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.9/project-docs/sdk-full-installation.html)

# Full Installation

> Installation instructions for the Couchbase Go Client. 

The Couchbase Go SDK 2.x is a complete rewrite of the API, reducing the number of overloads to present a simplified surface area, and adding support for future Couchbase Server features like [Collections and Scopes](../concept-docs/collections.md)(available from Couchbase Server 7.0 onwards). The Go 2.x SDK also introduces improved error handling providing extra error information.

If you’re upgrading your application from Couchbase Go SDK 1.x, please read the [Migration Guide](migrating-sdk-code-to-3.n.md).

## [](#installing-the-sdk)Installing the SDK

Version 2 of the Go SDK has added support for [Go Modules](https://github.com/golang/go/wiki/Modules). You can use `go get` to download the SDK:

> [!IMPORTANT]
> `go get` only works if you have initialised a [Go module](https://go.dev/blog/using-go-modules), and have a `go.mod` file in your working directory.

```console
$ go get github.com/couchbase/gocb/v2@v2.7.0
```

> [!NOTE]
> In line with the [Golang project](https://golang.org/doc/devel/release.html#policy), Couchbase supports both the current, and the previous, versions of Go. Earlier versions may work, but are not supported.

Information about new features, fixes, and known issues — as well as information about how to install earlier release versions — is in the [release notes](sdk-release-notes.md).