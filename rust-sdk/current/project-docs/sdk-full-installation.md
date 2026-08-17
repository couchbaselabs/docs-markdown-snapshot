---
title: Couchbase Rust SDK Installation
description: Installation instructions for the Couchbase Rust Client.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/project-docs/pages/sdk-full-installation.adoc
  xref: xref:rust-sdk:project-docs:sdk-full-installation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/project-docs/sdk-full-installation.html)

# Couchbase Rust SDK Installation

> Installation instructions for the Couchbase Rust Client. 

This page gives full installation instructions for the Rust SDK. In most cases, the [Quickstart Guide](../hello-world/start-using-sdk.md) should be enough to get you up and running if you're in a hurry.

## [](#prerequisites)Prerequisites

The Rust SDK is tested against LTS versions of Oracle JDK and OpenJDK — see our [compatibility docs](compatibility.md#jdk-compat).

The Couchbase Rust SDK 1.0 Client supports Rust 1.90+.

## [](#installing-the-sdk)Installing the SDK

The Couchbase Rust SDK is available on crates.io.

To include it in your project, add the following to your `Cargo.toml`:

```none
cargo add couchbase
```