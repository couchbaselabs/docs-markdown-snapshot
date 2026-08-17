---
title: DELETE Statements
description: This topic describes how you use <code>DELETE</code> statements to
  delete objects from a standalone collection.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sqlpp/pages/5_dml_delete.adoc
  xref: xref:analytics:sqlpp:5_dml_delete.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sqlpp/5_dml_delete.html)

# DELETE Statements

> This topic describes how you use `DELETE` statements to delete objects from a standalone collection. 

## [](#syntax)Syntax

**Delete EBNF** 

```EBNF
Delete ::=  "DELETE" "FROM" QualifiedName
            ("AS" OutputAlias)?
            ("WHERE" Expr)?
            ("RETURNING" Expr)?
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

After you use `DELETE`, you can run `ANALYZE COLLECTION` on the collection to update the data sample used by cost-based optimization (CBO). See [Cost-Based Optimizer for Capella Analytics Services](5b%5Fcbo.md).

**Show additional example** 

This example deletes orders made by a customer named `T. Cody` and returns the values of the `orderno` field for those deleted orders:

```SQL++
  DELETE FROM database_name.scope_name.Orders AS ord
  WHERE ord.custid = (
     SELECT VALUE cust.custid
     FROM Customers AS cust
     WHERE cust.name = "T. Cody"
  )[0]
  RETURNING VALUE ord.orderno;
```

The output of the RETURNING clause is:

1002
1007
1008
1009

## [](#arguments)Arguments

WHERE

The optional **`WHERE`** clause specifies a condition that the objects in the target collection must satisfy for the statement to delete them. It can include uncomplicated predicates as well as other subqueries referring to other existing collections. The default database for the `WHERE` expression is the target collection's database. There's one variable in scope for the `WHERE` expression. If specified, `OutputAlias` defines the variable's name. Otherwise, the variable's name is the target collection's name.

RETURNING

Adding an optional **`RETURNING`** clause causes the statement to return a result for each object deleted, identified by the `OutputAlias` or the collection name. The clause can contain subqueries, although they cannot refer to any collections in their FROM clauses, making them object-local in nature.

Errors encountered during `DELETE` cancels the action and leaves the target dataset in its pre-DELETE state.

## [](#see-also)See Also

* [CREATE a Standalone Collection](5%5Fddl%5Fstandalone.md)
* [Access and Organize Data in Capella Analytics Services](../sources/database-objects.md)
* [Cost-Based Optimizer for Capella Analytics Services](5b%5Fcbo.md)