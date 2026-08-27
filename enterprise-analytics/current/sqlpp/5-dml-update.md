---
title: UPDATE Statements
description: This topic describes how you use <code>UPDATE</code> statements to
  modify objects in a collection.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/5-dml-update.adoc
  xref: xref:enterprise-analytics:sqlpp:5-dml-update.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5-dml-update.html)

# UPDATE Statements

> This topic describes how you use `UPDATE` statements to modify objects in a collection. Use the `UPDATE` statement to target 1 or more objects, and add, delete, or update fields. 

The `UPDATE` statement enables modifications to both top-level (flat) and nested (non-flat) fields within a record. For nested fields, you can specify a subfield path to assign a new value or replace the entire object. To update specific elements within an array, you must use nested statements to iterate through the array. A record's primary key cannot be modified and must remain unchanged. Refer to the [Examples](#examples) section for detailed usage.

## [](#syntax)Syntax

**UpdateStatement EBNF** 

```EBNF
UpdateStatement ::=  "UPDATE" QualifiedName ( "AS" Variable)? (SetClause | ( "( " (InsertClause | DeleteClause |  NestedUpdateClause)  ") "))+ ('WHERE' Expr)? ('RETURNING' Expr)?
```

**UpdateStatement Diagram** 

!["UPDATE" QualifiedName ( "AS" Variable)? (SetClause | ( "( " (InsertClause | DeleteClause |  NestedUpdateClause)  ") "))+ (](_images/UpdateStatement.png) 

**NestedUpdateClause EBNF** 

```EBNF
NestedUpdateClause ::= "UPDATE" (((Identifier ("." Identifier)*) ("AS" Variable)?) ("AT" Variable)?) (SetClause | ("(" (InsertClause | DeleteClause | NestedUpdateClause) ")"))+ ("WHERE" Expr)?
```

**NestedUpdateClause Diagram** 

!["UPDATE" Identifier ( "AS" Variable)? (SetClause | ( "( " (InsertClause | DeleteClause |  NestedUpdateClause)  ") "))+ (](_images/NestedUpdateClause.png) 

**SetClause EBNF** 

```EBNF
SetClause ::=  "SET" Identifier  "'=" Expr ( "," Identifier  "=" Expr)*
```

**SetClause Diagram** 

!["SET" Identifier  "](_images/SetClause.png) 

**InsertClause EBNF** 

```EBNF
InsertClause ::=  "INSERT INTO " Identifier ( "AS" Variable)? ( "AT" Expr)?  "(" Expr  ")"
```

**InsertClause Diagram** 

!["INSERT INTO " Identifier ( "AS" Variable)? ( "AT" Expr)?  "(" Expr  ")"](_images/InsertClause.png) 

**DeleteClause EBNF** 

```EBNF
DeleteClause ::= "DELETE" "FROM" Identifier ( "AS" Variable )? ( "AT" Variable )?( "WHERE" Expr )?
```

**DeleteClause Diagram** 

!["DELETE" "FROM" Identifier ( "AS" Variable )? ( "AT" Variable )?( "WHERE" Expr )?](_images/DeleteClause.png) 

## Examples

The following example uses an `UPDATE` statement to modify the value of the field `ship_date` for the order with `orderno` equal to `1010` in the `sampleAnalytics.Commerce.orders` collection.

```SQL++
UPDATE sampleAnalytics.Commerce.orders
SET ship_date="2020-11-08"
WHERE orderno= 1010 ;
```

After you use the `UPDATE` statement, you can run `ANALYZE COLLECTION` on the collection to update the data sample used by cost-based optimization (CBO). For more information, see [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md).

**Show an additional example** 

The following examples modify different fields in the objects in the `sampleAnalytics.Commerce.orders` collection. For this example, use the following order in the collection:

```SQL++
{
      "orderno": 1010,
      "custid": "C51",
      "user_info": {
        "first_name": "John",
        "family_name": "Doe"
      },
      "order_date": "2020-11-04",
      "ship_date": "2020-11-08",
      "items": [
        {
          "itemno": 410,
          "qty": 120,
          "price": 88.16
        },
        {
          "itemno": 590,
          "qty": 6,
          "price": 217.75
        }
      ]
    }
```

Some of the possible updates are as follows:

```SQL++
UPDATE sampleAnalytics.Commerce.orders
SET user_info.first_name = "Jane"
WHERE orderno = 1010;
```

In the preceding example, the first name of the user is updated to `Jane`.

```SQL++
UPDATE sampleAnalytics.Commerce.orders
(UPDATE items AS i
SET i.price = 330, i.addiotionalInfo="fragile"
WHERE i.itemno= 410)
WHERE orderno= 1010 ;
```

In the preceding example, the price of the item with `itemno` 410 for the order with `orderno` 1010 is updated.

```SQL++
UPDATE sampleAnalytics.Commerce.orders
(INSERT INTO items AT 2([
       {
           "itemno": 460,
           "qty": 240,
           "price": 99.98
        }]))
WHERE orderno= 1010;
```

In the preceding example, a new item is added to the order's item list as the second item.

```SQL++
UPDATE sampleAnalytics.Commerce.orders as u
(DELETE from u.items at  number WHERE number IN [0,1])
 SET u.status="changed"
WHERE u.orderno= 1010;
```

In the preceding example, an item is deleted from the order's list of items.

## [](#arguments)Arguments

RETURNING

Adding an optional **`RETURNING`** clause causes the statement to return a result for each object updated, identified by the `OutputAlias` or the collection name. The clause can contain subqueries, although they cannot refer to any collections in their `FROM` clauses, making them object-local in nature.

## [](#see-also)See Also

* [CREATE a Standalone Collection](5%5Fddl%5Fstandalone.md)
* [Access and Organize Data in Enterprise Analytics](../sources/database-objects.md)
* [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md)