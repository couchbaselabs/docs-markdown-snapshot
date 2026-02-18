---
title: UPSERT INTO Statements
description: This topic describes how you use <code>UPSERT INTO</code>
  statements to insert and update objects in a standalone collection.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_dml_upsert.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/current/sqlpp/5_dml_upsert.html)

# UPSERT INTO Statements

> This topic describes how you use `UPSERT INTO` statements to insert and update objects in a standalone collection. 

If any of the objects you’re adding has the same primary key as an object that’s already in the standalone collection, Enterprise Analytics replaces the existing object’s values with the new object’s values.

## [](#syntax)Syntax

**UpsertInto EBNF** 

```EBNF
UpsertInto ::= "UPSERT" "INTO" QualifiedName
           ("AS" OutputAlias)?
            query ("RETURNING" Expr)?
```

**UpsertInto Diagram** 

!["UPSERT" "INTO" QualifiedName ("AS" OutputAlias)? query ("RETURNING" expression)?](_images/UpsertInto.png) 

## [](#examples)Examples

The following example uses an `UPSERT INTO` statement to both insert a new order, 1010, into the `sampleAnalytics.Commerce.orders` collection and update existing order 1009 with more information.

Optionally, you can review the contents of the collection before and after you do the upsert to compare the results: `SELECT * from sampleAnalytics.Commerce.orders LIMIT 10;`

```SQL++
UPSERT INTO sampleAnalytics.Commerce.orders (
    {
      "orderno": 1010,
      "custid": "C51",
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
    },
  {
    "orderno": 1009,
    "custid": "C13",
    "order_date": "2020-10-13",
    "items": [
       {
           "itemno": 460,
           "qty": 240,
           "price": 99.98
        }
      ]
    }
  );
```

After you use `UPSERT INTO`, you can run `ANALYZE COLLECTION` on the collection to update the data sample used by cost-based optimization (CBO). See [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md).

**Show an additional example** 

This example begins with two statements that create an external collection for data stored on S3 and a standalone collection. In this example, the objects in the external collection have a primary key field named `my_pk` with a data type of string, which you then use as the standalone collection’s primary key.

They’re followed by an `UPSERT INTO` statement that copies all data from the external location—identified by the defined `PATH` clause—to the standalone collection as is.

```SQL++
  CREATE EXTERNAL COLLECTION my_external_dataset
    ON my_s3_bucket
    AT my_s3_link
    PATH "my/path";
  CREATE COLLECTION my_standalone_dataset
    PRIMARY KEY (my_pk:string);

  UPSERT INTO my_standalone_dataset
  SELECT VALUE d
  FROM my_external_dataset AS d;
```

## [](#arguments)Arguments

RETURNING

Adding an optional **`RETURNING`** clause causes the statement to return a result for each object upserted, identified by the `OutputAlias` or the collection name. The clause can contain subqueries, although they cannot refer to any collections in their FROM clauses, making them object-local in nature.

## [](#see-also)See Also

* [CREATE a Standalone Collection](5%5Fddl%5Fstandalone.md)
* [Access and Organize Data in Enterprise Analytics](../sources/database-objects.md)
* [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md)