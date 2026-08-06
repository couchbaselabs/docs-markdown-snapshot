---
title: DELETE Statements
description: This topic describes how you use <code>DELETE</code> statements to
  delete objects from a standalone collection.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/5_dml_delete.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:sqlpp:5_dml_delete.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_dml_delete.html)

# DELETE Statements

> This topic describes how you use `DELETE` statements to delete objects from a standalone collection. 

## [](#syntax)Syntax

**Delete EBNF** 

```EBNF
Delete ::=  "DELETE" "FROM" QualifiedName
            ("AS" OutputAlias)?
            ("WHERE" Expr)?
```

**Delete Diagram** 

!["DELETE" "FROM" QualifiedName ("AS" OutputAlias)? ("WHERE" Expr)?  ("RETURNING" Expr)?](_images/Delete.png) 

The first `QualifiedName` must resolve to a standalone collection or synonym.

## Examples

This example deletes all orders placed before 2020-07-01 from a standalone collection named Orders:

```SQL++
  DELETE FROM database_name.scope_name.Orders
  WHERE order_date < "2020-07-01";
```

After you use `DELETE`, you can run `ANALYZE COLLECTION` on the collection to update the data sample used by cost-based optimization (CBO). See [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md).

**Show additional example** 

This example deletes orders made by a customer named `T. Cody`:

```SQL++
  DELETE FROM database_name.scope_name.Orders AS ord
  WHERE ord.custid = (
     SELECT VALUE cust.custid
     FROM Customers AS cust
     WHERE cust.name = "T. Cody"
  )[0];
```

## [](#arguments)Arguments

WHERE

The optional **`WHERE`** clause specifies a condition that the objects in the target collection must satisfy for the statement to delete them. It can include uncomplicated predicates as well as other subqueries referring to other existing collections. The default database for the `WHERE` expression is the target collection's database. There's one variable in scope for the `WHERE` expression. If specified, `OutputAlias` defines the variable's name. Otherwise, the variable's name is the target collection's name.

Errors encountered during `DELETE` cancels the action and leaves the target dataset in its pre-DELETE state.

## [](#see-also)See Also

* [CREATE a Standalone Collection](5%5Fddl%5Fstandalone.md)
* [Access and Organize Data in Enterprise Analytics](../sources/database-objects.md)
* [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md)