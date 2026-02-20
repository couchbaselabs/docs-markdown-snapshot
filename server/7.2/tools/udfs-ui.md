---
title: User-Defined Functions UI
description: The Couchbase Server admin console provides a UI for adding user
  defined functions.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/tools/pages/udfs-ui.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:tools:udfs-ui.adoc[]
---

[View original HTML](/server/7.2/tools/udfs-ui.html)

# User-Defined Functions UI

> The Couchbase Server admin console provides a UI for adding user defined functions. 

Starting from Couchbase Server 7.1, the Couchbase Administration console provides an interface to create, update, or delete user-defined functions written in SQL++ or JavaScript.

Start at the administration console and select **Query** **UDFs** from the menus to access the **UDF** screen.

![screen for adding user-defined functions](_images/udf-screen.png) 

## [](#javascript-function-libraries)Javascript Function Libraries

Click on the `+ add function library` link to create a library of JavaScript functions.

![add javascript library screen](_images/udf-add-library.png) 

When you create a new library, an example function (`add`) is supplied as an example. You can delete it when you add your own function, or leave it to serve as a basic example.

You can set a **Namespace** for your library which will restrict its access to users that have permissions to access the bucket and scope specified by the namespace.

Before you leave the screen, you must set a **Library Name**.

Click **Save** to save the library and return to the main UDF screen, or **Cancel** to cancel without saving the library.

![udf screen with library added](_images/udf-screen-with-library.png) 

You can **edit** the library again to add and/or delete functions contained inside it.

You can also delete the whole library by clicking on the **drop** link.

## [](#user-defined-functions)User-Defined Functions

You can add your own user-defined functions in the lower **User-Defined Functions** list. These functions can be one of two types:

To add a user-defined function, click on **\+ add function** below the **User-Defined Functions** list.

![Add function screen](_images/udf-add-function-inline.png) 

The **Namespace** can be set to define the scope that function resides in (`travel-sample.inventory` for example).

Users will need permissions to access this namespace to run the function.

The **Function Name** is the name that will be used in SQL++ statements (`EXECUTE FUNCTION` for example) to reference your function. The name must be unique and is case-insensitive.

You can define a list of fixed parameters for your function, or you can use the `…​` symbol which indicates a variable length function list defined as `args[]`.

The **Function Type** can be either `inline` or `Javascript`:

| **Inline**     | This is a function written in SQL++ which can be used as part of another SQL++ statement, such as [SELECT](../n1ql/n1ql-language-reference/selectintro.md) and [EXECUTE FUNCTION](../n1ql/n1ql-language-reference/execfunction.md). |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **JavaScript** | You can create SQL++ functions that call the Javascript functions defined in your library.                                                                                                                                          |

If you are defining an `inline` function then you can fill in any valid SQL++ expression which can then be used as part of another SQL++ statement. This is the default when creating a function.

If you switch **Function Type** to `Javascript` then the dialog will change to configure a JavaScript function call.

![add Javascript function](_images/udf-add-function-js.png) 

Then you select the `Javascript Library` where you created your Javascript function, and the name of your function. (There is no need to include the parameters.)

Once the details have been filled, you can click the **Save Function** to save the function and exit the dialog, or click on **Cancel** to exit the dialog without saving the details.