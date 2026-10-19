---
title: Environment and Identifier Functions
description: This topic describes the builtin SQL++ for Operational Insights
  Cloud environment and identifier functions.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Capella
    version: ""
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sqlpp/pages/8_builtin_env.adoc
  xref: xref:analytics:sqlpp:8_builtin_env.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights-cloud/sqlpp/8_builtin_env.html)

# Environment and Identifier Functions

> This topic describes the builtin SQL++ for Operational Insights Cloud environment and identifier functions. 

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