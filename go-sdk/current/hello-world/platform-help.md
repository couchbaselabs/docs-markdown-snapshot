---
title: Setting Up Couchbase Go SDK
description: Discover how to get up and running developing applications with the
  Couchbase Go SDK.
pubDate: 2026-09-03T05:31:47.619Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-go/edit/release/2.12/modules/hello-world/pages/platform-help.adoc
  xref: xref:go-sdk:hello-world:platform-help.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/current/hello-world/platform-help.html)

# Setting Up Couchbase Go SDK

> Discover how to get up and running developing applications with the Couchbase Go SDK. 

A simple Go orientation intro for _non-_Go folk who are evaluating the Couchbase Go SDK.

> [!IMPORTANT]
> Is This Page for You?
> 
> This page is to help evaluate the Couchbase Go SDK, if Go is not where you spend the majority of your working day. It is aimed at Software Architects, QE folk, managers, and anyone else who needs to run through using the Go SDK without necessarily being comfortable with installing and developing with Go. If this is not you, head back to the [rest of the Couchbase Go SDK documentation](overview.md).

* The [Go Getting Started Guide](https://go.dev/doc/tutorial/getting-started) is an excellent introduction to installing and using the Go platform.
* Be aware that the Go SDK supports [Go Modules](https://github.com/golang/go/wiki/Modules). You can use `go get` to download the SDK:  
> [!TIP]  
> `go get` only works if you have initialised a [Go module](https://go.dev/blog/using-go-modules), and have a `go.mod` file in your working directory.  
Install the latest version of the Couchbase 2.12 Go SDK  
```console  
$ go get github.com/couchbase/gocb/v2@v2.12.5  
```