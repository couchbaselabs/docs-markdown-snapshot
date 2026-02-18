---
title: Error Messages
description: The standardized error codes returned by the Couchbase PHP SDK,
  from cloud connection to sub-document.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/ref/pages/error-codes.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/php-sdk/4.2/ref/error-codes.html)

# Error Messages

> The standardized error codes returned by the Couchbase PHP SDK, from cloud connection to sub-document. 

Unresolved include directive in modules/ref/pages/error-codes.adoc - include::7.5@sdk:shared:partial$error-ref.adoc\[\]

## [](#shared-error-definitions)Shared Error Definitions

Unresolved include directive in modules/ref/pages/error-codes.adoc - include::7.5@sdk:shared:partial$error-ref.adoc\[\]

## [](#keyvalue-error-definitions)KeyValue Error Definitions

Unresolved include directive in modules/ref/pages/error-codes.adoc - include::7.5@sdk:shared:partial$error-ref.adoc\[\]

## [](#query-error-definitions)Query Error Definitions

Unresolved include directive in modules/ref/pages/error-codes.adoc - include::7.5@sdk:shared:partial$error-ref.adoc\[\]

## [](#analytics-error-definitions)Analytics Error Definitions

Unresolved include directive in modules/ref/pages/error-codes.adoc - include::7.5@sdk:shared:partial$error-ref.adoc\[\]

## [](#search-error-definition)Search Error Definition

Unresolved include directive in modules/ref/pages/error-codes.adoc - include::7.5@sdk:shared:partial$error-ref.adoc\[\]

## [](#view-error-definitions)View Error Definitions

Unresolved include directive in modules/ref/pages/error-codes.adoc - include::7.5@sdk:shared:partial$error-ref.adoc\[\]

## [](#management-api-error-definitions)Management API Error Definitions

Unresolved include directive in modules/ref/pages/error-codes.adoc - include::7.5@sdk:shared:partial$error-ref.adoc\[\]

## [](#field-level-encryption-error-definitions)Field-Level Encryption Error Definitions

Unresolved include directive in modules/ref/pages/error-codes.adoc - include::7.5@sdk:shared:partial$error-ref.adoc\[\]

## [](#connecting-to-cloud)Connecting to Cloud

Unresolved include directive in modules/ref/pages/error-codes.adoc - include::7.5@sdk:shared:partial$error-ref.adoc\[\]

Couldn’t look up

```terminal
[cb,EROR] (connection L:503 I:3705255243) <8676842d-4e8b-4c5b-a44f-e0886f8c0bc1.dp.cloud.couchbase.com:11207> (SOCK=762eb846eaa3268f) Couldn't look up 8676842d-4e8b-4c5b-a44f-e0886f8c0bc1.dp.cloud.couchbase.com (nodename nor servname provided, or not known) [EAI=8]
```

Failed to establish connection

```terminal
[cb,EROR] (connection L:164 I:3705255243) <8676842d-4e8b-4c5b-a44f-e0886f8c0bc1.dp.cloud.couchbase.com:11207> (SOCK=762eb846eaa3268f) Failed to establish connection: LCB_ERR_UNKNOWN_HOST (1049), os errno=0
```

Could not get configuration

```terminal
[cb,EROR] (cccp L:171 I:3705255243) <NOHOST:NOPORT> (CTX=0x0,) Could not get configuration: LCB_ERR_UNKNOWN_HOST (1049)
```

## [](#further-reading)Further Reading

* Our practical look at [error handling with the SDK](../howtos/error-handling.md).
* [Discussion document](../concept-docs/errors.md) on handling exceptions.
* Further reference material in the [API Guide](https://docs.couchbase.com/sdk-api/couchbase-php-client/namespaces/couchbase.html).