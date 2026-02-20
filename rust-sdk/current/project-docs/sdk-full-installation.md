---
title: Couchbase Rust SDK Installation
description: Installation instructions for the Couchbase Rust Client.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/project-docs/pages/sdk-full-installation.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:rust-sdk:project-docs:sdk-full-installation.adoc[]
---

[View original HTML](/rust-sdk/current/project-docs/sdk-full-installation.html)

# Couchbase Rust SDK Installation

> Installation instructions for the Couchbase Rust Client. 

This page gives full installation instructions for the Rust SDK. In most cases, the [Quickstart Guide](../hello-world/start-using-sdk.md) should be enough to get you up and running if you’re in a hurry.

## [](#prerequisites)Prerequisites

The Rust SDK is tested against LTS versions of Oracle JDK and OpenJDK — see our [compatibility docs](compatibility.md#jdk-compat).

The Couchbase Rust SDK 1.0 Client supports Rust 1.90+.

## [](#installing-the-sdk)Installing the SDK

The Couchbase Rust SDK is available on crates.io.

To include it in your project, add the following to your `Cargo.toml`:

```none
cargo add couchbase
```