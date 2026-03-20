---
title: Client Settings
description: The <code>ClusterOptions</code> struct enables you to configure
  Rust SDK options for bootstrapping, reliability, and performance.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/ref/pages/client-settings.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:rust-sdk:ref:client-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/ref/client-settings.html)

# Client Settings

> The `ClusterOptions` struct enables you to configure Rust SDK options for bootstrapping, reliability, and performance. 

Almost all configuration for the SDK can be specified through the `ClusterOptions` which are passed to the `Cluster::connect` call in the SDK. In addition to this, some of these options can also be specified through the connection string.

Most of the Cluster Options are grouped into categories. For example, TLS options are configured using an instance of the `TlsOptions` struct, accessed via the `ClusterOptions` instance’s `tls_options()` getter.

Configuring TLS options

```rust
ClusterOptions::new(Authenticator::PasswordAuthenticator(
    PasswordAuthenticator::new("username".to_string(), "password".to_string()),
))
.tls_options(TlsOptions::new());
```

All Client Settings can be found in the API ref at <https://docs.rs/couchbase/latest/couchbase/options/cluster%5Foptions/struct.ClusterOptions.html>