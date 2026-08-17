---
title: Encrypting Your Data
description: The Field Level Encryption library enables encryption and
  decryption of JSON fields, to support FIPS-140-2 compliance.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.7/modules/howtos/pages/encrypting-using-sdk.adoc
  xref: xref:3.7@ruby-sdk:howtos:encrypting-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.7/howtos/encrypting-using-sdk.html)

# Encrypting Your Data

> The Field Level Encryption library enables encryption and decryption of JSON fields, to support FIPS-140-2 compliance. 

Client-side implementation of Field Level Encryption is available in the previous versions of some of the other SDKs. It will be enabled in a future release of the third generation SDK.

> [!TIP]
> Native Encryption at Rest
> 
> Server 8.x (and new Capella Operational clusters) offer [encryption at rest](../../../server/current/learn/security/native-encryption-at-rest-overview.md). It's a comprehensive way of encrypting all data in a non-ephemeral bucket, as well as logs, configuration data, and audit data. However, you may prefer the relative simplicity of key management in Field Level Encryption for use cases where there are a limited number of data to be encrypted.