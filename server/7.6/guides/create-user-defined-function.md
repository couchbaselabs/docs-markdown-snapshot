[View original HTML](/server/7.6/guides/create-user-defined-function.html)

> How to create a user-defined function to call external JavaScript code. 

## [](#introduction)Introduction

You cannot call external JavaScript code directly from a SQL++ query. You must create a SQL++ user-defined function to reference the external JavaScript code.

If you have created a JavaScript function in an external library (see [Creating a JavaScript Library](create-javascript-library.md)), you must create a SQL++ user-defined function to reference it.

You can also create a SQL++ user-defined function and the external JavaScript code in a single operation. In this case, the JavaScript code is not stored in an external library.

## [](#creating-the-n1ql-udf-function)Creating a SQL++ User-Defined Function to Reference an External Library

To create a SQL++ user-defined function to reference an external library, do one of the following:

* Use the [UDF UI](../tools/udfs-ui.md) in the Query Workbench.
* Use the SQL++ [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md) statement, and reference the external library and JavaScript function.

* Query Workbench
* SQL++

1. Access the **UDF** screen from the administration console.  
![navigate to udf query](_images/javascript-udfs/navigate-to-udf-query.png)
2. Click on the **\+ add function** link.  
![library list](_images/javascript-udfs/my-library-list-add-function-button.png)  
The **Add Function** dialog is displayed.  
![add function dialog](_images/javascript-udfs/add-function-dialog.png)
3. Use the **Namespace** drop-down lists to select the bucket and scope where your JavaScript function resides.
4. Fill in the **Function Name** of your SQL++ user-defined function.
5. Specify **Parameters** for the function.

|  | The …​ in the parameters box denotes a variable length list of parameters. |
|  | -------------------------------------------------------------------------- |
6. Select **JavaScript** for the function type. A field appears in the dialog with a list of available libraries in the namespace you selected.  
![add function dialog switch to javascript](_images/javascript-udfs/add-function-dialog-switch-to-javascript.png)  
From this list select the library containing your function.
7. Enter the name of the JavaScript function in the `Library Function Name` field.

Execute the `CREATE FUNCTION` in the CBQ Shell to create the SQL++ user-defined function:

```sqlpp
CREATE FUNCTION default:`travel-sample`.`inventory`.GetBusinessDays(...) LANGUAGE JAVASCRIPT as "getBusinessDays" AT "travel-sample/inventory/my-library";
```

|  | The SQL++ user-defined function will take the same scope as the JavaScript UDF it is referencing. |
|  | ------------------------------------------------------------------------------------------------- |

## [](#related-links)Related Links

* To create a SQL++ user-defined function and the external JavaScript code in a single operation, see [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md).