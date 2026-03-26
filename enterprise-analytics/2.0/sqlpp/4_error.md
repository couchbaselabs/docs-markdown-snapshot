---
title: Errors
description: This topic describes SQL++ for Enterprise Analytics errors.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/4_error.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.0@enterprise-analytics:sqlpp:4_error.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/sqlpp/4_error.html)

# Errors

> This topic describes SQL++ for Enterprise Analytics errors. 

A query can potentially result in one of the following types of errors:

* Syntax error
* Identifier resolution error
* Type error

If the query processor runs into an error, it terminates the ongoing processing of the query and returns an error or warning message to the client.

For example, the UI displays query status next to the query editor's **Run Query** button. When an exclamation mark appears next to the status, you can move your cursor over this symbol to show the message.

![Displaying a type mismatch warning message](_images/error_message.png) 

## [](#Syntax%5Ferrors)Syntax Errors

A valid query must satisfy the grammar rules of the query language. Otherwise, a syntax error occurs.

##### Example: Omitted Keyword

```SQL++
 customers AS c
 SELECT *;
```

Since the query has no `FROM` keyword before the collection `customers`, a syntax error results as follows:

"code": 24000,
"msg": "Syntax error: In line 1 >>customers AS c<< Encountered \"AS\" at column 11. "

##### Example: Undelimited Reserved Word

```SQL++
  FROM customers AS c
  WHERE type="advertiser"
  SELECT *;
```

Since `type` is a [reserved keyword](reserved%5Fkeywords.md), a syntax error results as follows:

"code": 24000,
"msg": "Syntax error: In line 2 >>  WHERE type=\"advertiser\"<< Encountered \"type\" at column 9. "

## [](#Identifier%5Fresolution%5Ferrors)Identifier Resolution Errors

Referring to an undefined identifier can cause an error if the query parser cannot resolve the identifier as valid.

##### Example: Collection Name Typo

```SQL++
  FROM customer AS c
  SELECT *;
```

If your query includes a typo, like `customer` instead of `customers`, an identifier resolution error results as follows:

"code": 24045,
"msg": "Cannot find analytics collection customer in analytics scope sampleAnalytics.Commerce nor an alias with name customer (in line 1, at column 6)"

##### Example: Unqualified Field Name

```SQL++
  FROM customers AS c JOIN orders AS o ON c.custid = o.custid
  SELECT orderno, name;
```

A query that defines multiple variables—in this case,`customers AS c` and `orders AS o`—but then leaves field names unqualified results in an identifier resolution error as follows:

"code": 24042,
"msg": "Cannot resolve ambiguous alias reference for identifier name (in line 2, at column 10)"

The message indicates only the first unqualified field name that it encounters, in this case, `orderno`.

An identifier resolution error can also occur if you do not properly qualify a field name in a `GROUP BY` expression.

SELECT o.custid, COUNT(o.orderno) AS `order count`
FROM orders AS o
GROUP BY custid;

Result:

"code": 24041,
"msg": "Cannot resolve alias reference for undefined identifier o (in line 1, at column 8)"

## [](#Type%5Ferrors)Type Errors

The query compiler does data type checks based on its available type information. Typically, a type mismatch results in NULL along with an warning message. The query runtime also reports type errors if a data model instance it processes does not satisfy the type requirement.

##### Example: Type Mismatch

```SQL++
 SELECT string_length(1);
```

Since function `string_length` can only act on strings, this statement has the following result:

[
 {
   "$1": null
 }
]

The following warning message appears:

"code": 24011,
"msg": "Type mismatch: function string_length expects its first input parameter to be of type string, but the actual input type is bigint (in line 1, at column 8)"

## [](#Error%5Fcodes)Error Codes

For a full list of error codes, see [Analytics Error Codes](https://docs.couchbase.com/server/current/analytics/error-codes.html).