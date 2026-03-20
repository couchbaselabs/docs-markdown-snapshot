---
title: Field Level Encryption from the SDK
description: The Field Level Encryption library enables encryption and
  decryption of JSON fields, to support FIPS-140-2 compliance.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.4/modules/howtos/pages/encrypting-using-sdk.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:php-sdk:howtos:encrypting-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/current/howtos/encrypting-using-sdk.html)

# Field Level Encryption from the SDK

> The Field Level Encryption library enables encryption and decryption of JSON fields, to support FIPS-140-2 compliance. 

Client-side implementation of Field Level Encryption is available in the previous version of the SDK. It will be enabled in a future release of the third generation SDK.

> [!TIP]
> Native Encryption at Rest
> 
> Server 8.x (and new Capella Operational clusters) offer [encryption at rest](../../../server/current/learn/security/native-encryption-at-rest-overview.md). It’s a comprehensive way of encrypting all data in a non-ephemeral bucket, as well as logs, configuration data, and audit data.