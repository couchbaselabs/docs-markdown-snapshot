---
title: Field Level Encryption from the SDK
description: Fields within a document can be securely encrypted by the SDK, to
  support FIPS-140-2 compliance.
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/howtos/pages/encrypting-using-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:c-sdk:howtos:encrypting-using-sdk.adoc[]
---

[View original HTML](/c-sdk/current/howtos/encrypting-using-sdk.html)

# Field Level Encryption from the SDK

> Fields within a document can be securely encrypted by the SDK, to support FIPS-140-2 compliance. 

Field Level Encryption is normally carried out at a higher level than _libcouchbase_ (LCB). It is not available directly in LCB.

If this is a requirement, we suggest considering a migration to the [C++](../../../cxx-sdk/current/hello-world/overview.md) SDK, which includes [Field Level Encryption](../../../cxx-sdk/current/howtos/encrypting-using-sdk.md).

Alternately, take a look at Capella Operational and self-managed Couchbase Server’s [Native Encryption at Rest](../../../server/current/learn/security/native-encryption-at-rest-overview.md) feature.