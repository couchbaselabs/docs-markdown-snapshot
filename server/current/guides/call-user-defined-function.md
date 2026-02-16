[View original HTML](/server/current/guides/call-user-defined-function.html)

> How to call a user-defined function from SQL++ statements. 

## [](#introduction)Introduction

A user-defined function can be called like any other SQL++ function.

## [](#calling-the-sql-user-defined-function)Calling the SQL++ User-Defined Function

An SQL++ user-defined function can be called from anywhere that a standard SQL++ function can be called.

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

|  | The SQL++ user-defined function can be used in any SQL++ statement in exactly the same way as a standard built-in function. SELECT CASE    WHEN  GetBusinessDays('02/14/2022', '4/16/2022') > 44 THEN "true"    ELSE "false"    END    AS response; |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#related-links)Related Links

* [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md)
* [User-Defined Functions](../n1ql/n1ql-language-reference/userfun.md)