---
title: Field Level Encryption
description: Fields within a document can be securely encrypted by the SDK, to
  support FIPS-140-2 compliance.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: PHP SDK
    version: "4.6"
  edition: Enterprise Edition
antora:
  editUrl: https://github.com/couchbase/docs-sdk-php/edit/release/4.6/modules/concept-docs/pages/encryption.adoc
  xref: xref:php-sdk:concept-docs:encryption.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/current/concept-docs/encryption.html)

# Field Level Encryption

> Fields within a document can be securely encrypted by the SDK, to support FIPS-140-2 compliance. 

Client-side implementation of Field Level Encryption is available in the [C++](../../../cxx-sdk/current/howtos/encrypting-using-sdk.md), [.NET](../../../dotnet-sdk/current/howtos/encrypting-using-sdk.md), [Go](../../../go-sdk/current/howtos/encrypting-using-sdk.md), [Java](../../../java-sdk/current/howtos/encrypting-using-sdk.md), [Node.js](../../../nodejs-sdk/current/howtos/encrypting-using-sdk.md), [Python](../../../python-sdk/current/howtos/encrypting-using-sdk.md), and [Scala](../../../scala-sdk/current/howtos/encrypting-using-sdk.md) SDKs.

> [!TIP]
> Native Encryption at Rest
> 
> Server 8.x (and new Capella Operational clusters) offer [encryption at rest](../../../server/current/learn/security/native-encryption-at-rest-overview.md). It's a comprehensive way of encrypting all data in a non-ephemeral bucket, as well as logs, configuration data, and audit data.