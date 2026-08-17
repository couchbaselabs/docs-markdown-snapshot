---
title: Sequence Operators
description: Sequence operators enable you to return a value from a sequence.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/sequenceops.adoc
  xref: xref:cloud:n1ql:n1ql-language-reference/sequenceops.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/sequenceops.html)

# Sequence Operators

> Sequence operators enable you to return a value from a sequence. 

## [](#sequences)Sequences

A sequence is a construct that returns a sequence of integer values, one at a time, rather like a counter. Each time you request the next value for a sequence, an increment is added to the previous value, and the resulting value is returned. This is useful for generating values such as sequential ID numbers, where you need the Query service to keep track of the current value from one query to the next.

You can define any of the following attributes when you create a sequence. You can alter an existing sequence in order to restart it, or to change any of the sequence attributes.

### [](#start-value-increment-and-direction)Start Value, Increment, and Direction

By default, a sequence starts at `0` and goes up by `1` at each step. You can specify the start value of the sequence, the incremental value for the sequence, and the direction of the sequence: ascending or descending.

### [](#maximum-and-minimum-value)Maximum and Minimum Value

The highest possible value for a sequence is the highest signed 64-bit integer, `263-1`. This is the default maximum value.

The lowest possible value for a sequence is the lowest signed 64-bit integer, `-263`. This is the default minimum value.

You can specify a different maximum or minimum value for a sequence.

### [](#cycling)Cycling

A sequence may permit cycling. In this case, the sequence behaves as follows:

* If the sequence is ascending, then when it reaches the maximum value, it continues from the minimum value — which may be different to the sequence's specified starting value.
* If the sequence is descending, then when it reaches the minimum value, it continues from the maximum value — which may be different to the sequence's specified starting value.

If a sequence does not permit cycling, then when it reaches the maximum or minimum value, it generates an error.

## [](#next-val-for)Next Value Operator

The next value operator increments a given sequence and returns the next value.

### [](#prerequisites)Prerequisites

RBAC Privileges

To use this operator, your client must have the _Query Use Sequences_ privilege granted on the scope. For more details about cluster access privileges, see [Manage Cluster Access Credentials](../../clusters/manage-database-users.md).

### [](#syntax)Syntax

```ebnf
next-val-expr ::= 'NEXT' 'VALUE' 'FOR' sequence |
                  'NEXTVAL' 'FOR' sequence
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/next-val-expr.png) 

Synonym: `NEXT VALUE FOR` and `NEXTVAL FOR` are synonyms.

| sequence | (Required) A name that identifies the sequence within a namespace, bucket, and scope. See [Sequence Name](#next-sequence) below. |
| -------- | -------------------------------------------------------------------------------------------------------------------------------- |

#### [](#next-sequence)Sequence Name

```ebnf
sequence ::= ( ( namespace ':' )? bucket '.' scope '.' )? identifier
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/sequence.png) 

Each sequence is associated with a given namespace, bucket, and scope. You must specify the namespace, bucket, and scope to refer to the sequence correctly.

| namespace  | (Optional) The [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the bucket which contains the sequence. |
| ---------- | --------------------------------------------------------------------------------------------------------------------------- |
| bucket     | (Optional) The bucket which contains the sequence.                                                                          |
| scope      | (Optional) The scope which contains the sequence.                                                                           |
| identifier | (Required) The name of the sequence. The sequence name is case-sensitive.                                                   |

Currently, only the `default` namespace is available. If you omit the namespace, the default namespace in the current session is used.

If the [query context](../n1ql-intro/queriesandresults.md#query-context) is set, you can omit the bucket and scope from the statement. In this case, the bucket and scope for the sequence are taken from the query context.

The namespace, bucket, scope, and sequence name must follow the rules for [identifiers](identifiers.md). If the namespace, bucket, scope, or sequence name contain any special characters such as hyphens (-), you must wrap that part of the expression in backticks (\` \`).

### [](#return-value)Return Value

For a new sequence, the next value operator returns the starting value in the sequence.

For a sequence that has been referenced already, the next value operator increments the sequence and returns the new value. However, the sequence is only incremented once per document.

Subqueries operate on independent documents from their containing queries, so subqueries increment the sequence independently.

> [!NOTE]
> A sequence is not guaranteed to generate unique values. For example, in the following circumstances, it may generate a value that it has generated before:
> 
> * If the sequence cycles.
> * If the sequence is restarted with a value that overlaps with previously-generated values.
> * If the sequence is restarted to change the direction of the increment: for example, descending instead of ascending.

### [](#restrictions)Restrictions

You cannot use this operator in a WHERE or ON clause. This generates a semantic error 3100.

### [](#examples)Examples

To try the examples in this section, set the query context to the `tenant_agent_00` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Start a sequence

This statement starts a sequence called `ordNum` for use in the following examples.

Query

```sqlpp
CREATE SEQUENCE ordNum START WITH 1000;
```

Example 2\. Insert a sequential value in a document body

The following statement uses the `ordNum` sequence to generate a booking number within the body of the document.

Query

```sqlpp
INSERT INTO bookings
  VALUES (UUID(),
    {"num": NEXT VALUE FOR ordNum, "user": 0})
  RETURNING *;
```

Results

```json
[
  {
    "bookings": {
      "num": 1000,
      "user": 0
    }
  }
]
```

Example 3\. Insert a sequential value in a document key and body

The following statement uses the `ordNum` sequence to generate the document key and a booking number within the body of the document.

Query

```sqlpp
INSERT INTO bookings
  VALUES (TO_STRING(NEXTVAL FOR ordNum),
    {"num": NEXTVAL FOR ordNum, "user": 1})
  RETURNING META().id, *;
```

This query gives different results, depending on the version of Couchbase Server.

---

Couchbase Server 7.6–7.6.3

Results

```json
[
  {
    "id": "1001",
    "bookings": {
      "num": 1002,
      "user": 1
    }
  }
]
```

In versions of Couchbase Server prior to 7.6.5, the key is not regarded as part of the document, so this query increments the sequence twice. This gives a different sequence number for the document key and the document value.

---

Couchbase Server 7.6.5

Results

```json
[
  {
    "id": "1001",
    "bookings": {
      "num": 1001,
      "user": 1
    }
  }
]
```

In Couchbase Server 7.6.5 and later, the entire VALUES clause (key, value, and options) is regarded as a single document, so the query only increments the sequence once. This gives the same sequence number in the document key and the document value.

Example 4\. Insert a sequential value with INSERT SELECT

The following statement uses an INSERT SELECT statement. With this query, the document key and document value are both generated within the same document.

Query

```sqlpp
INSERT INTO bookings (KEY k, VALUE v)
  SELECT TO_STRING(NEXTVAL FOR ordNum) k,
         {"num": NEXTVAL FOR ordNum, "user": 1} v
  RETURNING META().id, *;
```

Result

```json
[
  {
    "id": "1003",
    "bookings": {
      "num": 1003,
      "user": 1
    }
  }
]
```

The next value operator only increments a sequence once within the context of a document. This gives the same sequence number in the document key and the document value.

## [](#prev-val-for)Previous Value Operator

The previous value operator returns the current value in a sequence, without incrementing or decrementing the sequence. This is useful when you need to refer to the same value again without generating a new value.

### [](#prerequisites-2)Prerequisites

RBAC Privileges

To use this operator, your client must have the _Query Use Sequences_ privilege granted on the scope. For more details about cluster access privileges, see [Authorization](../../clusters/manage-database-users.md).

### [](#syntax-2)Syntax

```ebnf
prev-val-expr ::= 'PREVIOUS' 'VALUE' 'FOR' sequence |
                  'PREV' 'VALUE' 'FOR' sequence |
                  'PREVVAL' 'FOR' sequence
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/prev-val-expr.png) 

Synonym: `PREVIOUS VALUE FOR`, `PREV VALUE FOR`, and `PREVVAL FOR` are synonyms.

| sequence | (Required) A name that identifies the sequence within a namespace, bucket, and scope. See [Sequence Name](#prev-sequence) below. |
| -------- | -------------------------------------------------------------------------------------------------------------------------------- |

#### [](#prev-sequence)Sequence Name

```ebnf
sequence ::= ( ( namespace ':' )? bucket '.' scope '.' )? identifier
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/sequence.png) 

Each sequence is associated with a given namespace, bucket, and scope. You must specify the namespace, bucket, and scope to refer to the sequence correctly.

| namespace  | (Optional) The [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the bucket which contains the sequence. |
| ---------- | --------------------------------------------------------------------------------------------------------------------------- |
| bucket     | (Optional) The bucket which contains the sequence.                                                                          |
| scope      | (Optional) The scope which contains the sequence.                                                                           |
| identifier | (Required) The name of the sequence. The sequence name is case-sensitive.                                                   |

Currently, only the `default` namespace is available. If you omit the namespace, the default namespace in the current session is used.

If the [query context](../n1ql-intro/queriesandresults.md#query-context) is set, you can omit the bucket and scope from the statement. In this case, the bucket and scope for the sequence are taken from the query context.

The namespace, bucket, scope, and sequence name must follow the rules for [identifiers](identifiers.md). If the namespace, bucket, scope, or sequence name contain any special characters such as hyphens (-), you must wrap that part of the expression in backticks (\` \`).

### [](#return-value-2)Return Value

The previous value operator returns one of the following, in order of precedence:

1. If a value has been generated for the current document, the operator returns the current value generated for the document.
2. If in a transaction, and a value has been generated for the transaction, the operator returns the current value generated in the transaction.
3. Otherwise, the operator returns the current value generated for the sequence on the node.

The previous value operator does not increment or decrement the sequence.

If no value has been generated for the sequence, the previous value operator returns an error.

### [](#restrictions-2)Restrictions

You cannot use this operator in a WHERE or ON clause. This generates a semantic error 3100.

### [](#examples-2)Examples

To try the examples in this section, set the query context to the `tenant_agent_00` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 5\. Insert the same sequential value in multiple statements

This example assumes that you have created a sequence called `ordNum` as described in [Example 1](#ex-nextval-start).

Query

```sqlpp
BEGIN TRANSACTION;
INSERT INTO bookings VALUES(UUID(),
  {"num": NEXT VALUE FOR ordNum,
   "user": 0,
   "type": "order"});
INSERT INTO bookings VALUES(UUID(),
  {"order_num": PREVVAL FOR ordNum,
   "hotel": "hotel_17413",
   "type": "item"});
INSERT INTO bookings VALUES(UUID(),
  {"order_num": PREVVAL FOR ordNum,
   "hotel": "hotel_15912",
   "type": "item"});
COMMIT;
```

Example 6\. Check the result of [Example 5](#ex-prevval-multi)

Query

```sqlpp
SELECT o.num, o.user, ARRAY_AGG(i.hotel) items
FROM bookings o,
     bookings i
WHERE o.type = "order"
  AND i.type = "item"
  AND o.num = i.order_num
GROUP BY o.num, o.user;
```

Result

```json
[
  {
    "num": 1004,
    "user": 0,
    "items": [
      "hotel_15912",
      "hotel_17413"
    ]
  }
]
```

## [](#related-links)Related Links

* To create a sequence, see [CREATE SEQUENCE](createsequence.md).
* To alter a sequence, see [ALTER SEQUENCE](altersequence.md).
* To drop a sequence, see [DROP SEQUENCE](dropsequence.md).
* To monitor sequences, see [Monitor Sequences](../n1ql-intro/sysinfo.md#sys-sequences).