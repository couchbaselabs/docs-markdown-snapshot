---
title: JSON Functions
description: DECODE_JSON(expression)
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/jsonfun.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:n1ql:n1ql-language-reference/jsonfun.adoc[]
---

[View original HTML](/server/current/n1ql/n1ql-language-reference/jsonfun.html)

# JSON Functions

DECODE\_JSON(expression)

Unmarshals the JSON-encoded string into a SQL++ value. The empty string is MISSING.

ENCODE\_JSON(expression)

Marshals the SQL++ value into a JSON-encoded string. MISSING becomes the empty string.

ENCODED\_SIZE(expression)

Number of bytes in an uncompressed JSON encoding of the value. The exact size is implementation-dependent. Always returns an integer, and never MISSING or NULL. Returns 0 for MISSING.

POLY\_LENGTH(expression)

Returns length of the value after evaluating the expression. The exact meaning of length depends on the type of the value:

* MISSING: MISSING
* NULL: NULL
* String: The length of the string.
* Array: The number of elements in the array.
* Object: The number of name/value pairs in the object
* Any other value: NULL