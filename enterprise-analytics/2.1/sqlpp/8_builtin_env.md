---
title: Environment and Identifier Functions
description: This topic describes the builtin SQL++ for Enterprise Analytics
  environment and identifier functions.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/8_builtin_env.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:sqlpp:8_builtin_env.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/sqlpp/8_builtin_env.html)

# Environment and Identifier Functions

> This topic describes the builtin SQL++ for Enterprise Analytics environment and identifier functions. 

## [](#meta)meta

> [!NOTE]
> The `meta` function applies only to remote Couchbase collections.

* Syntax:  
meta(expr)  
meta()
* Return a metadata object for a stored document.
* Arguments:

  * `expr` : an expression returning a stored document
  * none, if the stored document can be determined from the context
* Return Value:

  * a metadata object containing fields `id`, `vbid`, `seq`, `cas`, and `flags`.

## [](#uuid)uuid

* Syntax:  
uuid()
* Generates a `uuid`.
* Arguments:

  * none
* Return Value:

  * a generated, random `uuid`.