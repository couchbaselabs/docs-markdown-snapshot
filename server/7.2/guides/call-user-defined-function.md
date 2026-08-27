---
title: Calling a User-Defined Function
description: How to call a user-defined function from SQL++ statements.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/call-user-defined-function.adoc
  xref: xref:7.2@server:guides:call-user-defined-function.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/guides/call-user-defined-function.html)

# Calling a User-Defined Function

> How to call a user-defined function from SQL++ statements.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

A User-Defined Function can be called like any other SQL++ function. The Javascript is not called directly; it is called through the SQL++ User-Defined Function.

## [](#calling-the-sql-user-defined-function)Calling the SQL++ User-Defined Function

An SQL++ User-Defined Function can be called from anywhere that a standard SQL++ function can be called.

* Query Workbench
* REST API
* SQL++

1. Access the Query Workbench UI from the Administration Console.  
![accessing the query tool](_images/javascript-udfs/select-query-tool-ui.png)
2. Set the context to match the namespace of the function you are calling.  
![switch context to travel sample](_images/javascript-udfs/switch-context-to-travel-sample.png)
3. Enter the SQL++ statement in the query editor to run your function:  
```sqlpp  
EXECUTE FUNCTION GetBusinessDays("02/14/2022", "04/16/2022");  
```

1. Open up a shell session.
2. Execute a `curl` command to run the function:  
```console  
curl -v http://localhost:8093/query/service \
  -u Administrator:password \
  -d 'statement=EXECUTE FUNCTION default:`travel-sample`.inventory.GetBusinessDays("03/10/2022", "05/10.2022")'  
```

Run the `EXECUTE FUNCTION` function in the CBQ Shell.

```sqlpp
EXECUTE FUNCTION default:`travel-sample`.`inventory`.GetBusinessDays("03/10/2022", "05/10.2022");
```

> [!NOTE]
> The SQL++ User-Defined Function can be used in any SQL++ statement in exactly the same way as a standard built-in function.
> 
> ```sqlpp
> SELECT CASE 
>   WHEN  GetBusinessDays('02/14/2022', '4/16/2022') > 44 THEN "true" 
>   ELSE "false" 
>   END 
>   AS response;
> ```

## [](#further-reading)Further Reading

* [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md)
* [User-Defined Functions](../n1ql/n1ql-language-reference/userfun.md)