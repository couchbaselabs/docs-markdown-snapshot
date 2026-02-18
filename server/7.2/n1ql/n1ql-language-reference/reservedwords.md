---
title: Reserved Words
description: SQL++ defines an extensive list of keywords that are reserved
  words. You cannot use these keywords as identifiers unless you escape them.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/reservedwords.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/n1ql/n1ql-language-reference/reservedwords.html)

# Reserved Words

> SQL++ defines an extensive list of keywords that are reserved words. You cannot use these keywords as identifiers unless you escape them. All of the SQL++ keywords are case-insensitive. 

Some keywords are not currently implemented but are reserved for future use.

## [](#using-reserved-words-as-identifiers)Using Reserved Words as Identifiers

SQL++ allows escaped identifiers to overlap with keywords. To use a reserved word as an identifier, you must escape it by enclosing the reserved word inside backticks (\`\`). For example, if your JSON document contains a field named `index`, you can use it in your queries by escaping it like this:

```json
{
    "age": "42",
    "index": 27,
    "name": "Elvis"
}
```

```sqlpp
CREATE INDEX myindex ON default(`index`) USING GSI;
```

## [](#sql-reserved-words)SQL++ Reserved Words

The following keywords are reserved and cannot be used as unescaped identifiers:

### [](#a)A

[ADVISE](advise.md)  
[ALL](selectclause.md#all)  
ALTER  
ANALYZE  
[AND](logicalops.md#logical-op-and)  
[ANY](collectionops.md#collection-op-any)  
[ARRAY](collectionops.md#array)  
[AS](from.md#section%5Fax5%5F2nx%5F1db)  
ASC  
AT

### [](#b)B

BEGIN  
BETWEEN  
[BINARY](datatypes.md#datatype-binary)  
[BOOLEAN](datatypes.md#datatype-boolean)  
BREAK  
BUCKET  
BUILD  
BY

### [](#c)C

CALL  
CASE  
CAST  
CLUSTER  
COLLATE  
COLLECTION  
COMMIT  
[COMMITTED](set-transaction.md)  
CONNECT  
CONTINUE  
CORRELATED  
COVER  
[CREATE](createindex.md)  
[CURRENT](window.md#window-frame-extent)

### [](#d)D

DATABASE  
DATASET  
DATASTORE  
DECLARE  
DECREMENT  
[DELETE](delete.md)  
DERIVED  
DESC  
DESCRIBE  
[DISTINCT](selectclause.md#distinct)  
DO  
[DROP](dropindex.md)

### [](#e)E

EACH  
ELEMENT  
ELSE  
END  
[EVERY](collectionops.md#collection-op-every)  
[EXCEPT](union.md)  
EXCLUDE  
EXECUTE  
[EXISTS](collectionops.md#exists)  
[EXPLAIN](explain.md)

### [](#f)F

FALSE  
FETCH  
FILTER  
FIRST  
FLATTEN  
FLUSH  
[FOLLOWING](window.md#window-frame-extent)  
FOR  
FORCE  
[FROM](from.md)  
[FTS](hints.md#index-type)  
[FUNCTION](createfunction.md)

### [](#g)G

GOLANG  
GRANT  
[GROUP](groupby.md)  
[GROUPS](window.md#window-frame-clause)  
[GSI](hints.md#index-type)

### [](#h)H

[HASH](join.md#use-hash-hint)  
HAVING

### [](#i)I

IF  
[ISOLATION](set-transaction.md)  
IGNORE  
ILIKE  
[IN](collectionops.md#collection-op-in)  
INCLUDE  
INCREMENT  
INDEX  
INFER  
INLINE  
INNER  
[INSERT](insert.md)  
[INTERSECT](union.md)  
INTO  
IS

### [](#j)J

[JAVASCRIPT](createfunction.md)  
[JOIN](join.md)

### [](#k)K

KEY  
KEYS  
KEYSPACE  
KNOWN

### [](#l)L

[LANGUAGE](createfunction.md)  
LAST  
LEFT  
[LET](let.md)  
LETTING  
[LEVEL](set-transaction.md)  
LIKE  
[LIMIT](limit.md)  
LSM

### [](#m)M

MAP  
MAPPING  
MATCHED  
MATERIALIZED  
[MERGE](merge.md)  
MINUS  
[MISSING](comparisonops.md#null-and-missing)

### [](#n)N

NAMESPACE  
[NEST](nest.md)  
[NL](join.md#use-nl-hint)  
[NO](window.md#window-frame-exclusion)  
[NOT](logicalops.md#logical-op-not)  
[NTH\_VALUE](windowfun.md#fn-window-nth-value)  
[NULL](comparisonops.md#null-and-missing)  
[NULLS](window.md#nulls-treatment)  
NUMBER

### [](#o)O

OBJECT  
[OFFSET](offset.md)  
ON  
OPTION  
[OPTIONS](insert.md#insert-values)  
[OR](logicalops.md#or-operator)  
[ORDER](orderby.md)  
[OTHERS](window.md#window-frame-exclusion)  
OUTER  
[OVER](window.md)

### [](#p)P

PARSE  
PARTITION  
PASSWORD  
PATH  
POOL  
[PRECEDING](window.md#window-frame-extent)  
PREPARE  
PRIMARY  
PRIVATE  
PRIVILEGE  
[PROBE](join.md#use-hash-hint)  
PROCEDURE  
PUBLIC

### [](#r)R

[RANGE](window.md#window-frame-clause)  
RAW  
REALM  
REDUCE  
RENAME  
[RESPECT](window.md#nulls-treatment)  
RETURN  
RETURNING  
REVOKE  
RIGHT  
ROLE  
[ROLLBACK](rollback-transaction.md)  
[ROW](window.md#window-frame-extent)  
[ROWS](window.md#window-frame-clause)

### [](#s)S

SATISFIES  
[SAVEPOINT](savepoint.md)  
SCHEMA  
SCOPE  
[SELECT](selectclause.md)  
SELF  
SEMI  
SET  
SHOW  
SOME  
START  
STATISTICS  
STRING  
SYSTEM

### [](#t)T

THEN  
[TIES](window.md#window-frame-exclusion)  
TO  
[TRAN](begin-transaction.md)  
[TRANSACTION](begin-transaction.md)  
TRIGGER  
TRUE  
TRUNCATE

### [](#u)U

[UNBOUNDED](window.md#window-frame-extent)  
UNDER  
[UNION](union.md)  
UNIQUE  
UNKNOWN  
[UNNEST](unnest.md)  
UNSET  
[UPDATE](update.md)  
[UPSERT](upsert.md)  
[USE](hints.md)  
USER  
USING

### [](#v)V

VALIDATE  
VALUE  
VALUED  
VALUES  
VIA  
VIEW

### [](#w)W

WHEN  
[WHERE](where.md)  
WHILE  
WINDOW  
WITH  
[WITHIN](collectionops.md#collection-op-within)  
[WORK](begin-transaction.md)

### [](#x)X

XOR