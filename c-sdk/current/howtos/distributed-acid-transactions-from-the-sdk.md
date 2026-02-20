---
title: Distributed Transactions from the C SDK
description: C&#43;&#43; Transactions built upon the C SDK have been replaced
  with native C&#43;&#43; SDK ACID transactions.
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:c-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc[]
---

[View original HTML](/c-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.html)

# Distributed Transactions from the C SDK

> C++ Transactions built upon the C SDK have been replaced with native C++ SDK ACID transactions. 

Transactions are not available directly via the C SDK.

Previously a version of C++ Distributed ACID Transactions was built upon the C SDK, although not exposing any C symbols explicitly. This has now been deprecated, and customers are recommended to explore [native C++ SDK ACID transactions](../../../cxx-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md).