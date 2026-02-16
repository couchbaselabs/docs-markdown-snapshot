[View original HTML](/enterprise-analytics/2.0/sqlpp/8_builtin_env.html)

> This topic describes the builtin SQL++ for Enterprise Analytics environment and identifier functions. 

## [](#meta)meta

|  | The meta function applies only to remote Couchbase collections. |
|  | --------------------------------------------------------------- |

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