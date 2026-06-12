---
title: Couchbase Go SDK Installation
description: Installation instructions for the Couchbase Go Client.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/release/2.12/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:go-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/current/project-docs/sdk-full-installation.html)

# Couchbase Go SDK Installation

> Installation instructions for the Couchbase Go Client. 

This page gives full installation instructions for the Go SDK. In most cases, the [Quickstart Guide](../hello-world/start-using-sdk.md) should be enough to get you up and running if you're in a hurry.

## [](#prerequisites)Prerequisites

In line with the [Golang project](https://golang.org/doc/devel/release.html#policy), Couchbase supports both the current, and the previous, versions of Go. Earlier versions may work, but are not supported.

## [](#installing-the-sdk)Installing the SDK

Version 2 of the Go SDK has added support for [Go Modules](https://github.com/golang/go/wiki/Modules). You can use `go get` to download the SDK:

> [!IMPORTANT]
> `go get` only works if you have initialised a [Go module](https://go.dev/blog/using-go-modules), and have a `go.mod` file in your working directory.

Install the latest version of the Couchbase 2.12 Go SDK

```console
$ go get github.com/couchbase/gocb/v2@v2.12.3
```

## [](#further-information)Further Information

Information about new features, fixes, and known issues — as well as information about how to install earlier release versions — is in the [release notes](sdk-release-notes.md).