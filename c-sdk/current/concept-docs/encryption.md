---
title: Field Level Encryption
description: Fields within a document can be securely encrypted by the SDK, to
  support FIPS-140-2 compliance.
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/concept-docs/pages/encryption.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:c-sdk:concept-docs:encryption.adoc[]
---

[View original HTML](/c-sdk/current/concept-docs/encryption.html)

# Field Level Encryption

> Fields within a document can be securely encrypted by the SDK, to support FIPS-140-2 compliance. 

Field Level Encryption is normally carried out at a higher level than _libcouchbase_ (LCB). It is available in the LCB 'wrapper' SDKs: Node.js and Python. It will be available in a later release of the other LCB 'wrapper' SDKs, PHP. It will not be available in LCB.