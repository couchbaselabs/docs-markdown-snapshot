---
title: Call a User-Defined Function
description: Call a user-defined JavaScript function from the Query Tab or cbq
  and use it with your Capella operational cluster.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/call-user-defined-function.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:guides:call-user-defined-function.adoc[]
---

[View original HTML](/cloud/guides/call-user-defined-function.html)

# Call a User-Defined Function

> Call a user-defined JavaScript function from the Query Tab or cbq and use it with your Capella operational cluster. 

A user-defined function can be called like any other SQL++ function.

## [](#prerequisites)Prerequisites

* If you want to use cbq to run your user-defined function, you must complete the prerequisites for using cbq. For more information, see [Prerequisites](../n1ql/n1ql-intro/cbq.md#prerequisites).
* You have created a user-defined function. For more information, see [Create a User-Defined Function](create-user-defined-function.md).

## [](#procedure)Procedure

You can run user-defined functions from the Query Tab or cbq.

* Query Tab
* cbq

To run a user-defined function from the Query Tab:

1. On the **Operational Clusters** page, select the operational cluster where you want to work with your user-defined function.
2. Go to **Data Tools** **Query**.
3. Enter a SQL++ statement in the query editor to run your function.  
If you created a scoped user-defined function, make sure your [query context](../n1ql/n1ql-intro/queriesandresults.md#query-context) is set to the same bucket and scope as the namespace for your function.  
For example, the following statement executes a function called `GetBusinessDays`, which takes 2 dates:  
```sqlpp  
EXECUTE FUNCTION GetBusinessDays("02/14/2025", "04/16/2025");  
```  
You can also use a user-defined function in any SQL++ statement, just like a standard built-in function. For example:  
```sqlpp  
SELECT CASE  
  WHEN  GetBusinessDays('02/14/2025', '4/16/2025') > 44 THEN "true"  
  ELSE "false"  
  END  
  AS response;  
```

To run a user-defined function using the command line tool, cbq:

1. Open a terminal window.
2. Navigate to the directory where you installed cbq.
3. Connect to your Capella operational cluster. For more information, see [Connecting to the Cluster](../n1ql/n1ql-intro/cbq.md#cbq-connect-to-cluster).
4. Run the `EXECUTE FUNCTION` command with your user-defined function.  
For example, the following command executes a function called `GetBusinessDays`, which takes 2 dates, on the `travel-sample`/`inventory` keyspace:  
```sqlpp  
EXECUTE FUNCTION default:`travel-sample`.`inventory`.GetBusinessDays("03/10/2025", "05/10/2025");  
```  
You can also use a user-defined function in any SQL++ statement, just like a standard built-in function. For example:  
```console  
cbq> SELECT CASE  
      WHEN  GetBusinessDays('02/14/2025', '4/16/2025') > 44 THEN "true"  
      ELSE "false"  
      END  
      AS response;  
```

## [](#see-also)See Also

* [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md)
* [User-Defined Functions](../n1ql/n1ql-language-reference/userfun.md)
* [EXECUTE FUNCTION](../n1ql/n1ql-language-reference/execfunction.md)
* [JavaScript Functions for Query Reference](../javascript-udfs/javascript-functions-with-couchbase.md)