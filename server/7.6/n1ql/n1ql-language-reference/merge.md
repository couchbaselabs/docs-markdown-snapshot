---
title: MERGE
description: A MERGE statement provides the ability to update, insert into, or
  delete from a keyspace based on the results of a join with another keyspace or
  subquery.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/merge.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:n1ql:n1ql-language-reference/merge.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/merge.html)

# MERGE

> A MERGE statement provides the ability to update, insert into, or delete from a keyspace based on the results of a join with another keyspace or subquery. It is possible to specify actions (insert, update, delete) on the keyspace based on a match or no match in the join. Multiple actions can be specified in the same query. 

Couchbase Server supports two types of merge clause, which are described in the sections below: [ANSI Merge](#ansi-merge) and [Lookup Merge](#lookup-merge).

> [!NOTE]
> The ANSI merge clause has much more flexible functionality than its earlier legacy equivalent. Since it is standard compliant and more flexible, we recommend you to use ANSI merge exclusively, where possible.

## [](#privileges)Privileges

User executing the MERGE statement must have the following privileges:

* _Query Select_ privileges on the source keyspace
* _Query Insert_, _Query Update_, or _Query Delete_ privileges on the target keyspace as per the MERGE actions
* _Query Select_ privileges on the keyspaces referred in the RETURNING clause

For more details about user roles, refer to [Authorization](../../learn/security/authorization-overview.md).

> [!NOTE]
> A user with the _Data Writer_ privilege may set documents to expire. When the document expires, the data service deletes the document, even though the user may not have the _Query Delete_ privilege.

## [](#syntax)Syntax

```ebnf
merge ::= 'MERGE' 'INTO' ( ansi-merge | lookup-merge ) limit-clause? returning-clause?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/merge.png) 

| ansi-merge       | [ANSI Merge](#ansi-merge)             |
| ---------------- | ------------------------------------- |
| lookup-merge     | [Lookup Merge](#lookup-merge)         |
| limit-clause     | [LIMIT Clause](#limit-clause)         |
| returning-clause | [RETURNING Clause](#returning-clause) |

## [](#ansi-merge)ANSI Merge

```ebnf
ansi-merge ::= target-keyspace use-index-clause 'USING' ansi-merge-source
               ansi-merge-predicate ansi-merge-actions
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/ansi-merge.png) 

| target-keyspace      | [ANSI Merge Target](#ansi-merge-target)       |
| -------------------- | --------------------------------------------- |
| use-index-clause     | [ANSI Merge Target Hint](#target-hint)        |
| ansi-merge-source    | [ANSI Merge Source](#ansi-merge-source)       |
| ansi-merge-predicate | [ANSI Merge Predicate](#ansi-merge-predicate) |
| ansi-merge-actions   | [ANSI Merge Actions](#ansi-merge-actions)     |

### [](#ansi-merge-target)ANSI Merge Target

```ebnf
target-keyspace ::= keyspace-ref ( 'AS'? alias )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/target-keyspace.png) 

The merge target is the keyspace which you want to update, insert into, or delete from.

| keyspace-ref | [Keyspace Reference](#ansi-target-ref) |
| ------------ | -------------------------------------- |
| alias        | [AS Alias](#ansi-target-alias)         |

#### [](#ansi-target-ref)Keyspace Reference

```ebnf
keyspace-ref ::= keyspace-path | keyspace-partial
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-ref.png) 

```ebnf
keyspace-path ::= ( namespace ':' )? bucket ( '.' scope '.' collection )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-path.png) 

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

Keyspace reference for the merge target. For more details, refer to [Keyspace Reference](from.md#from-keyspace-ref).

#### [](#ansi-target-alias)AS Alias

Assigns another name to the keyspace reference. For details, refer to [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

Assigning an alias to the keyspace reference is optional. If you assign an alias to the keyspace reference, the `AS` keyword may be omitted.

### [](#target-hint)ANSI Merge Target Hint

You can use a `USE INDEX` hint on the merge target to specify that the merge should use a particular index. For details, refer to [USE INDEX Clause](hints.md#use-index-clause).

> [!NOTE]
> The `USE INDEX` hint is the only hint allowed on the target. You cannot specify a `USE KEYS` hint or a join hint (`USE NL` or `USE HASH`) on the target of a merge statement.

### [](#ansi-merge-source)ANSI Merge Source

```ebnf
ansi-merge-source ::= ( merge-source-keyspace | merge-source-subquery | merge-source-expr )
                      ansi-join-hints?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/ansi-merge-source.png) 

The merge source is the recordset that you want to merge with the merge target. It can be a keyspace reference, a subquery, or a generic expression.

| merge-source-keyspace | [ANSI Merge Keyspace](#ansi-merge-source-keyspace)  |
| --------------------- | --------------------------------------------------- |
| merge-source-subquery | [ANSI Merge Subquery](#ansi-merge-source-subquery)  |
| merge-source-expr     | [ANSI Merge Expression](#ansi-merge-source-expr)    |
| ansi-join-hints       | [ANSI Merge Source Hints](#ansi-merge-source-hints) |

#### [](#ansi-merge-source-keyspace)ANSI Merge Keyspace

```ebnf
merge-source-keyspace ::= keyspace-ref ( 'AS'? alias )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/merge-source-keyspace.png) 

| keyspace-ref | [Keyspace Reference](#ansi-keyspace-ref) |
| ------------ | ---------------------------------------- |
| alias        | [AS Alias](#ansi-keyspace-alias)         |

##### [](#ansi-keyspace-ref)Keyspace Reference

```ebnf
keyspace-ref ::= keyspace-path | keyspace-partial
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-ref.png) 

```ebnf
keyspace-path ::= ( namespace ':' )? bucket ( '.' scope '.' collection )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-path.png) 

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

Keyspace reference for the merge source. For details, refer to [Keyspace Reference](from.md#from-keyspace-ref).

##### [](#ansi-keyspace-alias)AS Alias

Assigns another name to the keyspace reference. For details, refer to [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

Assigning an alias to the keyspace reference is optional. If you assign an alias to the keyspace reference, the `AS` keyword may be omitted.

#### [](#ansi-merge-source-subquery)ANSI Merge Subquery

```ebnf
merge-source-subquery ::= subquery-expr 'AS'? alias
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/merge-source-subquery.png) 

| subquery-expr | [Subquery Expression](#ansi-subquery-expr) |
| ------------- | ------------------------------------------ |
| alias         | [AS Alias](#ansi-subquery-alias)           |

##### [](#ansi-subquery-expr)Subquery Expression

```ebnf
subquery-expr ::= '(' select ')'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/subquery-expr.png) 

Use parentheses to specify a subquery for the merge source. For details, refer to [Subqueries](subqueries.md).

##### [](#ansi-subquery-alias)AS Alias

Assigns another name to the subquery. For details, refer to [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

You must assign an alias to a subquery on the merge source. However, when you assign an alias to the subquery, the `AS` keyword may be omitted.

#### [](#ansi-merge-source-expr)ANSI Merge Expression

```ebnf
merge-source-expr ::= expr ( 'AS'? alias )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/merge-source-expr.png) 

| expr  | A SQL++ [expression](index.md) generating JSON documents or objects for the merge source. |
| ----- | ----------------------------------------------------------------------------------------- |
| alias | [AS Alias](#ansi-generic-alias)                                                           |

##### [](#ansi-generic-alias)AS Alias

Assigns another name to the generic expression. For details, refer to [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

Assigning an alias to the generic expression is optional. If you assign an alias to the generic expression, the `AS` keyword may be omitted.

#### [](#ansi-merge-source-hints)ANSI Merge Source Hints

You can specify ANSI join hints (`USE HASH` or `USE NL`) on the source of an ANSI merge. For details, refer to [ANSI JOIN Hints](join.md#ansi-join-hints).

> [!NOTE]
> If the merge source is a keyspace, you can also specify a `USE KEYS` or `USE INDEX` hint on the merge source. For details, refer to [Multiple Hints](join.md#multiple-hints).
> 
> If the merge action is [update](#ansi-merge-update) or [delete](#ansi-merge-delete), you can specify any of the join methods: `USE HASH(BUILD)`, `USE HASH(PROBE)`, or `USE NL`.
> 
> If the merge action is [insert](#ansi-merge-insert), the only join methods you can specify are `USE HASH(PROBE)` or `USE NL`. In this case, if you specify `USE HASH(BUILD)`, the join method will default to `USE NL`.
> 
> The ANSI join hint is optional. If omitted, the default hint is `USE NL`.
> 
> If you are using a nested-loop join, i.e. `USE NL` is specified or no join hint is specified, the target keyspace reference must have an appropriate secondary index defined for the join to work. If such an index cannot be found an error will be returned.

### [](#ansi-merge-predicate)ANSI Merge Predicate

```ebnf
ansi-merge-predicate ::= 'ON' expr
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/ansi-merge-predicate.png) 

The merge predicate enables you to specify an ANSI join between the [merge source](#ansi-merge-source) and the [merge target](#ansi-merge-target).

| expr | Boolean expression representing the join condition. This expression may contain fields, constant expressions, or any complex SQL++ expression. |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#ansi-merge-actions)ANSI Merge Actions

```ebnf
ansi-merge-actions ::= merge-update? merge-delete? ansi-merge-insert?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/ansi-merge-actions.png) 

The merge actions enable you to specify insert, update, and delete actions on the target keyspace, based on a match or no match in the join.

| merge-update      | [ANSI Merge Update](#ansi-merge-update) |
| ----------------- | --------------------------------------- |
| merge-delete      | [ANSI Merge Delete](#ansi-merge-delete) |
| ansi-merge-insert | [ANSI Merge Insert](#ansi-merge-insert) |

#### [](#ansi-merge-update)ANSI Merge Update

```ebnf
merge-update ::= 'WHEN' 'MATCHED' 'THEN' 'UPDATE' set-clause? unset-clause? where-clause?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/merge-update.png) 

Updates a document that already exists with updated values.

| set-clause   | [SET Clause](#ansi-set-clause)     |
| ------------ | ---------------------------------- |
| unset-clause | [UNSET Clause](#ansi-unset-clause) |
| where-clause | [WHERE Clause](#ansi-update-where) |

##### [](#ansi-set-clause)SET Clause

```ebnf
set-clause ::= 'SET' ( meta '=' expiration | path '=' expr update-for? )
               ( ',' ( meta '=' expiration | path '=' expr update-for? ) )*
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/set-clause.png) 

Specifies the value for an attribute to be changed. Also enables you to set the expiration of the document. For more details, refer to [SET Clause](update.md#set-clause).

| update-for | [FOR Clause](#ansi-update-for) |
| ---------- | ------------------------------ |

##### [](#ansi-unset-clause)UNSET Clause

```ebnf
unset-clause ::= 'UNSET' path update-for? (',' path update-for?)*
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/unset-clause.png) 

Removes a specified attribute from the document. For more details, refer to [UNSET Clause](update.md#unset-clause).

| update-for | [FOR Clause](#ansi-update-for) |
| ---------- | ------------------------------ |

##### [](#ansi-update-for)FOR Clause

```ebnf
update-for ::= ('FOR' (name-var ':')? var ('IN' | 'WITHIN') path
               (','   (name-var ':')? var ('IN' | 'WITHIN') path)* )+
               ('WHEN' cond)? 'END'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/update-for.png) 

```ebnf
path ::= identifier ( '[' expr ']' )* ( '.' identifier ( '[' expr ']' )* )*
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/path.png) 

Iterates over a nested array to SET or UNSET the given attribute for every matching element in the array. For more details, refer to [FOR Clause](update.md#update-for).

##### [](#ansi-update-where)WHERE Clause

```ebnf
where-clause ::= 'WHERE' cond
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/where-clause.png) 

Optionally specifies a condition that must be met for data to be updated. For more details, refer to [WHERE Clause](update.md#where-clause).

#### [](#ansi-merge-delete)ANSI Merge Delete

```ebnf
merge-delete ::= 'WHEN' 'MATCHED' 'THEN' 'DELETE' where-clause?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/merge-delete.png) 

Removes the specified document from the keyspace.

| where-clause | [WHERE Clause](#ansi-delete-where) |
| ------------ | ---------------------------------- |

##### [](#ansi-delete-where)WHERE Clause

```ebnf
where-clause ::= 'WHERE' cond
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/where-clause.png) 

Optionally specifies a condition that must be met for data to be deleted. For more details, refer to [WHERE Clause](update.md#where-clause).

#### [](#ansi-merge-insert)ANSI Merge Insert

```ebnf
ansi-merge-insert ::= 'WHEN' 'NOT' 'MATCHED' 'THEN' 'INSERT' '(' 'KEY'? key
                      ( ',' 'VALUE'? value )? ( ',' 'OPTIONS'? options )? ')' where-clause?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/ansi-merge-insert.png) 

Inserts a new document into the keyspace. Use parentheses to specify the key and value for the inserted document, separated by a comma.

> [!TIP]
> Use the [UUID()](metafun.md#uuid) function to generate a random, unique document key.

| key          | An expression specifying the key for the inserted document. The KEY keyword may be omitted. If it is omitted, the VALUE keyword must be omitted also.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| value        | \[Optional\] An expression specifying the value for the inserted document. If the value is omitted, an empty document is inserted. The VALUE keyword may be omitted. If it is omitted, the KEY keyword must be omitted also.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| options      | \[Optional\] An object representing the metadata to be set for the inserted document. Only the expiration attribute has any effect; any other attributes are ignored. expiration An integer, or an expression resolving to an integer, representing the [document expiration](../../../../java-sdk/current/howtos/kv-operations.md#document-expiration) in seconds. If the document expiration is not specified, it defaults to 0, meaning the document expiration is the same as the [bucket or collection expiration](../../learn/data/expiration.md). The OPTIONS keyword may be omitted. If it is omitted, the KEY and VALUE keywords must be omitted also. |
| where-clause | [WHERE Clause](#ansi-insert-where)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

##### [](#ansi-insert-where)WHERE Clause

```ebnf
where-clause ::= 'WHERE' cond
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/where-clause.png) 

Optionally specifies a condition that must be met for data to be inserted. For more details, refer to [WHERE clause](update.md#where-clause).

## [](#lookup-merge)Lookup Merge

```ebnf
lookup-merge ::= target-keyspace 'USING' lookup-merge-source lookup-merge-predicate
                 lookup-merge-actions
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/lookup-merge.png) 

| target-keyspace        | [Lookup Merge Target](#lookup-merge-target)       |
| ---------------------- | ------------------------------------------------- |
| lookup-merge-source    | [Lookup Merge Source](#lookup-merge-source)       |
| lookup-merge-predicate | [Lookup Merge Predicate](#lookup-merge-predicate) |
| lookup-merge-actions   | [Lookup Merge Actions](#lookup-merge-actions)     |

### [](#lookup-merge-target)Lookup Merge Target

Keyspace reference for the merge target. The syntax is the same as for an ANSI merge. Refer to [ANSI Merge Target](#ansi-merge-target).

### [](#lookup-merge-source)Lookup Merge Source

```ebnf
lookup-merge-source ::= merge-source-keyspace use-clause? |
                        merge-source-subquery |
                        merge-source-expr
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/lookup-merge-source.png) 

The merge source is the recordset that you want to merge with the merge target. It can be a keyspace reference, a subquery, or a generic expression.

| merge-source-keyspace   | [Lookup Merge Keyspace](#lookup-merge-source-keyspace) |
| ----------------------- | ------------------------------------------------------ |
| use-clause              | [Lookup Merge Source Hint](#lookup-merge-source-hints) |
| merge-source-subquery   | [Lookup Merge Subquery](#lookup-merge-source-subquery) |
| merge-source-expression | [Lookup Merge Expression](#lookup-merge-source-expr)   |

#### [](#lookup-merge-source-keyspace)Lookup Merge Keyspace

Keyspace reference for the merge source. The syntax is the same as for an ANSI merge. Refer to [ANSI Merge Keyspace](#ansi-merge-source-keyspace).

#### [](#lookup-merge-source-hints)Lookup Merge Source Hint

If the merge source is a keyspace, you can specify a USE KEYS or USE INDEX hint on the merge source. For details, refer to [USE clause](hints.md).

#### [](#lookup-merge-source-subquery)Lookup Merge Subquery

Specifies a subquery for the merge source. The syntax is the same as for an ANSI merge. Refer to [ANSI Merge Subquery](#ansi-merge-source-subquery).

#### [](#lookup-merge-source-expr)Lookup Merge Expression

Specifies a generic expression for the merge source. The syntax is the same as for an ANSI merge. Refer to [ANSI Merge Expression](#ansi-merge-source-expr).

### [](#lookup-merge-predicate)Lookup Merge Predicate

```ebnf
lookup-merge-predicate ::= 'ON' 'PRIMARY'? 'KEY' expr
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/lookup-merge-predicate.png) 

The merge predicate produces a document key for the target of the lookup merge.

| expr | \[Required\] String or expression representing the primary key of the documents for the target keyspace. |
| ---- | -------------------------------------------------------------------------------------------------------- |

### [](#lookup-merge-actions)Lookup Merge Actions

```ebnf
lookup-merge-actions ::= merge-update? merge-delete? lookup-merge-insert?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/lookup-merge-actions.png) 

The merge actions enable you to specify insert, update, and delete actions on the target keyspace, based on a match or no match in the join.

| merge-update        | [Lookup Merge Update](#lookup-merge-update) |
| ------------------- | ------------------------------------------- |
| merge-delete        | [Lookup Merge Delete](#lookup-merge-delete) |
| lookup-merge-insert | [Lookup Merge Insert](#lookup-merge-insert) |

#### [](#lookup-merge-update)Lookup Merge Update

Updates a document that already exists with updated values. The syntax is the same as for an ANSI merge. Refer to [ANSI Merge Update](#ansi-merge-update).

#### [](#lookup-merge-delete)Lookup Merge Delete

Removes the specified document from the keyspace. The syntax is the same as for an ANSI merge. Refer to [ANSI Merge Delete](#ansi-merge-delete) for details.

#### [](#lookup-merge-insert)Lookup Merge Insert

```ebnf
lookup-merge-insert ::= 'WHEN' 'NOT' 'MATCHED' 'THEN' 'INSERT' expr where-clause?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/lookup-merge-insert.png) 

Inserts a new document into the keyspace. The key specified in the [Lookup Merge Predicate](#lookup-merge-predicate) is used as the key for the newly inserted document.

| expr         | An expression specifying the value for the inserted document. |
| ------------ | ------------------------------------------------------------- |
| where-clause | [WHERE Clause](#lookup-merge-insert-where)                    |

> [!NOTE]
> The Lookup Merge Insert syntax does not enable you to specify the document expiration. If you need to specify the document expiration, rewrite the query using the ANSI Merge Insert syntax.

##### [](#lookup-merge-insert-where)WHERE Clause

```ebnf
where-clause ::= 'WHERE' cond
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/where-clause.png) 

Optionally specifies a condition that must be met for data to be inserted. For more details, refer to [WHERE clause](update.md#where-clause).

## [](#common-clauses)Common Clauses

The following clauses are common to both ANSI Merge and Lookup Merge.

### [](#limit-clause)LIMIT Clause

```ebnf
limit-clause ::= 'LIMIT' expr
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/limit-clause.png) 

Specifies the _minimum_ number of records to be processed. For more details, refer to [LIMIT Clause](insert.md#limit-clause).

### [](#returning-clause)RETURNING Clause

```ebnf
returning-clause ::= 'RETURNING' (result-expr (',' result-expr)* |
                    ('RAW' | 'ELEMENT' | 'VALUE') expr)
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/returning-clause.png) 

Specifies the information to be returned by the operation as a query result. For more details, refer to [RETURNING Clause](insert.md#returning-clause).

## [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

> [!WARNING]
> Please note that the examples below will alter the data in your sample buckets. To restore your sample data, remove and reinstall the `travel-sample` bucket. Refer to [Sample Buckets](../../manage/manage-settings/install-sample-buckets.md) for details.

Example 1\. ANSI merge with expression source

This example updates the vacancy field based on the source expression.

```sqlpp
MERGE INTO hotel t
USING [
  {"id":"21728", "vacancy": true},
  {"id":"21730", "vacancy": true}
] source
ON meta(t).id = "hotel_" || source.id
WHEN MATCHED THEN
  UPDATE SET t.old_vacancy = t.vacancy,
             t.vacancy = source.vacancy
RETURNING meta(t).id, t.old_vacancy, t.vacancy;
```

Example 2\. ANSI merge with keyspace source

This example finds all BA routes whose source airport is in France. If any flights are using equipment 319, they are updated to use 797\. If any flights are using equipment 757, they are deleted.

```sqlpp
MERGE INTO route
USING airport
ON route.sourceairport = airport.faa
WHEN MATCHED THEN UPDATE
  SET route.old_equipment = route.equipment,
      route.equipment = "797",
      route.updated = true
  WHERE airport.country = "France"
    AND route.airline = "BA"
    AND CONTAINS(route.equipment, "319")
WHEN MATCHED THEN DELETE
  WHERE airport.country = "France"
    AND route.airline = "BA"
    AND CONTAINS(route.equipment, "757")
RETURNING route.old_equipment, route.equipment, airport.faa;
```

Example 3\. ANSI merge with updates and inserts

This example compares a source set of airport data with the `airport` keyspace data. If the airport already exists in the `airport` keyspace, the record is updated. If the airport does not exist in the `airport` keyspace, a new record is created.

```sqlpp
MERGE INTO airport AS target
USING [
  {"iata":"DSA", "name": "Doncaster Sheffield Airport"},
  {"iata":"VLY", "name": "Anglesey Airport / Maes Awyr Môn"}
] AS source
ON target.faa = source.iata
WHEN MATCHED THEN
  UPDATE SET target.old_name = target.airportname,
             target.airportname = source.name,
             target.updated = true
WHEN NOT MATCHED THEN
  INSERT (KEY UUID(),
          VALUE {"faa": source.iata,
                 "airportname": source.name,
                 "type": "airport",
                 "inserted": true} )
RETURNING *;
```

Example 4\. ANSI merge with expiration

This example compares a source set of airport data with the `airport` keyspace data. If the airport already exists in the `airport` keyspace, the record is updated, and the existing document expiration is preserved. If the airport does not exist in the `airport` keyspace, a new record is created with an expiration of one week.

```sqlpp
MERGE INTO airport AS target
USING [
  {"iata":"DSA", "name": "Doncaster Sheffield Airport"},
  {"iata":"VLY", "name": "Anglesey Airport / Maes Awyr Môn"}
] AS source
ON target.faa = source.iata
WHEN MATCHED THEN
  UPDATE SET target.old_name = target.airportname,
             target.airportname = source.name,
             target.updated = true,
             meta(target).expiration = meta(target).expiration
WHEN NOT MATCHED THEN
  INSERT (KEY UUID(),
          VALUE {"faa": source.iata,
                 "airportname": source.name,
                 "type": "airport",
                 "inserted": true},
          OPTIONS {"expiration": 7*24*60*60} );
```

Note that it is possible to preserve the document expiration using the request-level [preserve\_expiry](../n1ql-manage/query-settings.md#preserve%5Fexpiry) parameter.

Example 5\. Lookup merge with expression source

Lookup merge version of [Example 1](#example-1).

```sqlpp
MERGE INTO hotel t
USING [
  {"id":"21728", "vacancy": true},
  {"id":"21730", "vacancy": true}
] source
ON KEY "hotel_"|| source.id
WHEN MATCHED THEN
  UPDATE SET t.old_vacancy = t.vacancy, t.vacancy = source.vacancy
RETURNING meta(t).id, t.old_vacancy, t.vacancy;
```

Example 6\. Lookup merge with keyspace source

The following statement updates product based on orders.

```sqlpp
MERGE INTO product p USING orders o ON KEY o.productId
WHEN MATCHED THEN
  UPDATE SET p.lastSaleDate = o.orderDate
WHEN MATCHED THEN
  DELETE WHERE p.inventoryCount  <= 0;
```

Example 7\. Lookup merge with updates and inserts

The following statement merges two datasets containing employee information. It then updates `all_empts` on match with `emps_deptb` and inserts when there is no match.

```sqlpp
MERGE INTO all_empts a USING emps_deptb b ON KEY b.empId
WHEN MATCHED THEN
  UPDATE SET a.depts = a.depts + 1
  a.title = b.title || ", " || b.title
WHEN NOT MATCHED THEN
  INSERT { "name": b.name,
           "title": b.title,
           "depts": b.depts,
           "empId": b.empId,
           "dob": b.dob };
```