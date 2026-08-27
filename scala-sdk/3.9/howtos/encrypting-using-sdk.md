---
title: Field Level Encryption from the SDK
description: The Field Level Encryption library enables encryption and
  decryption of JSON fields, to support FIPS-140-2 compliance.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.9/modules/howtos/pages/encrypting-using-sdk.adoc
  xref: xref:3.9@scala-sdk:howtos:encrypting-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/3.9/howtos/encrypting-using-sdk.html)

# Field Level Encryption from the SDK

> The Field Level Encryption library enables encryption and decryption of JSON fields, to support FIPS-140-2 compliance. 

> [!TIP]
> Native Encryption at Rest
> 
> Server 8.x (and new Capella Operational clusters) offer [encryption at rest](../../../server/current/learn/security/native-encryption-at-rest-overview.md). It's a comprehensive way of encrypting all data in a non-ephemeral bucket, as well as logs, configuration data, and audit data. However, you may prefer the relative simplicity of key management in Field Level Encryption for use cases where there are a limited number of data to be encrypted.

Client-side implementation of Field Level Encryption has not historically been a feature of the Couchbase Scala SDK, but it is hoped to introduce it eventually.

Field Level Encryption _is_ available in most of the other SDKs, including the [Java SDK](../../../java-sdk/current/howtos/encrypting-using-sdk.md).