---
title: JSON Functions
description: This topic describes the builtin SQL++ for Operational Insights JSON functions.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "2.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/8_builtin_json.adoc
  xref: xref:2.1@enterprise-analytics:sqlpp:8_builtin_json.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/2.1/sqlpp/8_builtin_json.html)

# JSON Functions

> This topic describes the builtin SQL++ for Operational Insights JSON functions. 

## [](#decode%5Fjson)decode\_json

* Syntax:  
decode_json(expr)
* Unmarshals the JSON-encoded string into a SQL++ for Operational Insights value.
* Arguments:

  * `expr`: a JSON-encoded string.
* Return Value:

  * A SQL++ value.
  * If `expr` is NULL or an empty string then NULL is returned.
  * If `expr` is MISSING then MISSING is returned.
* Example:  
decode_json("{\"abc\":1,\"def\":2}");
* The expected result is:  
{  
  "abc": 1,  
  "def": 2  
}

## [](#encode%5Fjson)encode\_json

* Syntax:  
encode_json(expr)
* Marshals the SQL++ for Operational Insights value into a JSON-encoded string.
* Arguments:

  * `expr`: a SQL++ value.
* Return Value:

  * A JSON-encoded string.
  * If `expr` is NULL then NULL is returned.
  * If `expr` is MISSING then MISSING is returned.
* Example:  
encode_json({"abc":1,"def":2});
* The expected result is:  
"{ \"abc\": 1, \"def\": 2 }"

## [](#encoded%5Fsize)encoded\_size

* Syntax:  
encoded_size(expr)
* Returns the number of bytes in an uncompressed JSON encoding of the value. The exact size is implementation-dependent.
* Arguments:

  * `expr`: a SQL++ value.
* Return Value:

  * An integer. Never MISSING or NULL. Returns 0 for MISSING.
* Example:  
encoded_size({"abc":1,"def":2});
* The expected result is:  
22