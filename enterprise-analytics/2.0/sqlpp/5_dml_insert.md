---
title: INSERT INTO Statements
description: This topic describes how you use <code>INSERT INTO</code>
  statements to add objects to a standalone collection.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/5_dml_insert.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/2.0/sqlpp/5_dml_insert.html)

# INSERT INTO Statements

> This topic describes how you use `INSERT INTO` statements to add objects to a standalone collection. 

If any of the objects you’re adding have the same primary key value as an object that’s already in the collection, the request fails. The request also fails if the source data has duplicates. When such issues occur, Enterprise Analytics returns an error message and the standalone collection remains unchanged.

## [](#syntax)Syntax

**InsertInto EBNF** 

```EBNF
InsertInto ::= "INSERT" "INTO" QualifiedName
           ("AS" OutputAlias)?
            query ("RETURNING" Expr)?
```

**InsertInto Diagram** 

!["INSERT" "INTO" QualifiedName ("AS" OutputAlias)? query ("RETURNING" expression)?](_images/InsertInto.png) 

## [](#examples)Examples

This example copies all data, as is, from a remote Couchbase collection to a standalone collection, excluding existing meta-records. In this example, the objects in the external collection have an existing field named `my_pk`.

```SQL++
  CREATE COLLECTION my_shadow_dataset ON my_bucket;
  CREATE COLLECTION my_standalone_dataset PRIMARY KEY (my_pk:string);

  INSERT INTO my_standalone_dataset
  SELECT v FROM my_shadow_dataset AS v;
```

The next example creates a different standalone collection and then adds a JSON document with several objects to it.

```SQL++
  CREATE COLLECTION standaloneLocalData PRIMARY KEY (id:bigint);

  INSERT INTO standaloneLocalData  ([
    {"id": 317, "year": 2018, "quarter": null, "review": "good"},
    {"id": 455, "year": 2018, "quarter": null, "review": "bad"},
    {"id": 515, "year": 2018, "quarter": 1, "review": "good"},
    {"id": 832, "year": 2018, "quarter": 2, "review": "bad"},
    {"id": 1040, "year": 2019, "quarter": null, "review": "bad"}
]);
```

After you use `INSERT INTO`, you can run `ANALYZE COLLECTION` on the collection to update the data sample used by cost-based optimization (CBO). See [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md).

## [](#arguments)Arguments

RETURNING

Adding an optional **`RETURNING`** clause causes the statement to return a result for each object inserted, identified by the `OutputAlias` or the collection name. The clause can contain subqueries, although they cannot refer to any collections in their `FROM` clauses, making them object-local in nature.

## [](#see-also)See Also

* [CREATE a Standalone Collection](5%5Fddl%5Fstandalone.md)
* [Access and Organize Data in Enterprise Analytics](../sources/database-objects.md)
* [Cost-Based Optimizer for Enterprise Analytics Services](5b%5Fcbo.md)