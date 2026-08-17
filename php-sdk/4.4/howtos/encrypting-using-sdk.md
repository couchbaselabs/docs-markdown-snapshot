---
title: Field Level Encryption from the SDK
description: The Field Level Encryption library enables encryption and
  decryption of JSON fields, to support FIPS-140-2 compliance.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.4/modules/howtos/pages/encrypting-using-sdk.adoc
  xref: xref:4.4@php-sdk:howtos:encrypting-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/4.4/howtos/encrypting-using-sdk.html)

# Field Level Encryption from the SDK

> The Field Level Encryption library enables encryption and decryption of JSON fields, to support FIPS-140-2 compliance. 

Client-side implementation of Field Level Encryption is available in the previous version of the SDK. It will be enabled in a future release of the third generation SDK.

> [!TIP]
> Native Encryption at Rest
> 
> Server 8.x (and new Capella Operational clusters) offer [encryption at rest](../../../server/current/learn/security/native-encryption-at-rest-overview.md). It's a comprehensive way of encrypting all data in a non-ephemeral bucket, as well as logs, configuration data, and audit data.