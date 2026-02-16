[View original HTML](/server/7.2/guides/create-user-defined-function.html)

> How to create a user-defined function to call your JavaScript function.  
> This guide is for Couchbase Server.

## [](#creating-the-n1ql-udf-function)Creating the SQL++ User-Defined Function

Before you can run the JavaScript function you have created (see [Creating a JavaScript Library](create-javascript-library.md)), you will need to create a SQL++ User-Defined Function to reference it. You can create a SQL++ User-Defined Function by using:

* the [UDF UI](../tools/udfs-ui.md) in the Query Workbench.
* the [standard SQL++ CREATE FUNCTION DDL](../n1ql/n1ql-language-reference/createfunction.md), using the _External Functions_ option to reference the Javascript function.
* the REST-API to execute a [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md) call.

For more information on SQL++ User Defined Functions in general, read [User-Defined Functions](../n1ql/n1ql-language-reference/userfun.md).

* Query Workbench
* REST API
* SQL++

1. Access the `UDF` screen from the administration console.  
![navigate to udf query](_images/javascript-udfs/navigate-to-udf-query.png)
2. Click on the `+ add function` link from the `UDFs` screen.  
![library list](_images/javascript-udfs/my-library-list-add-function-button.png)  
which will display the `Add Function` screen.  
![add function dialog](_images/javascript-udfs/add-function-dialog.png)
3. Use the `Namespace` drop-down lists to select the bucket and scope where your Javascript function resides.
4. Fill in the `Function Name` of your SQL++ User-Defined Function.
5. Leave the `Parameters` as they are.

|  | The …​ in the parameters box denotes a variable length list of parameters. This is why you don’t have to fill in this field. |
|  | ---------------------------------------------------------------------------------------------------------------------------- |
6. Select `Javascript` for the function type. A field will appear in the dialog with a list of available libraries in the namespace you selected.  
![add function dialog switch to javascript](_images/javascript-udfs/add-function-dialog-switch-to-javascript.png)  
From this list select the library containing your function.
7. Enter the name of the JavaScript function in the `Library Function Name` field.

Run a `curl` command from the shell to add a SQL++ User-Defined Function that calls your Javascript function.

```console
curl -v http://localhost:8093/query/service \
  -u Administrator:password \
  -d 'statement=CREATE FUNCTION default:`travel-sample`.inventory.GetBusinessDays(...)
  LANGUAGE JAVASCRIPT as "getBusinessDays" AT "travel-sample/inventory/my-library"'
```

Execute the `CREATE FUNCTION` in the CBQ Shell to create the SQL++ User-Defined Function:

```sqlpp
CREATE FUNCTION default:`travel-sample`.`inventory`.GetBusinessDays(...) LANGUAGE JAVASCRIPT as "getBusinessDays" AT "travel-sample/inventory/my-library";
```

|  | The SQL++ User-Defined Function will take the same scope as the JavaScript UDF it is referencing. |
|  | ------------------------------------------------------------------------------------------------- |

Having created your SQL++ User-Defined Function, the [next step](call-user-defined-function.md) is to use a SQL++ statement to call the function.