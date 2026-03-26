---
title: ALTER SEQUENCE
description: The ALTER SEQUENCE statement enables you to alter an existing
  sequence in a given scope.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/altersequence.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:n1ql:n1ql-language-reference/altersequence.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-language-reference/altersequence.html)

# ALTER SEQUENCE

> The ALTER SEQUENCE statement enables you to alter an existing sequence in a given scope. 

## [](#purpose)Purpose

A sequence is a construct that returns a sequence of integer values, one at a time, rather like a counter. Each time you request the next value for a sequence, an increment is added to the previous value, and the resulting value is returned. This is useful for generating values such as sequential ID numbers, where you need the Query service to keep track of the current value from one query to the next. You can define any of the following attributes when you create a sequence. You can alter an existing sequence in order to restart it, or to change any of the sequence attributes.

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

### [](#cache)Cache

Sequences operate most efficiently with an in-memory cache of values. You can specify the size of this cache when you alter the sequence. A block of values is reserved by a node, and requests for values are satisfied from this cache. When exhausted, a new block of values is reserved. Reserving a cached block offers a performance boost, as it enables the Query service to return values directly from memory.

Note however that if a Query node shuts down, or if you alter the sequence, the unused values in the cached block are lost: a new block is reserved when you restart the node, or request the next value. You should choose a cache size with this in mind, along with the expected usage patterns for the sequence.

### [](#storage)Storage

Sequences are stored in the bucket's hidden `_system` scope. When you back up a bucket, sequences are included automatically, in accordance with the backup filters. Similarly, when you restore a bucket, sequences are restored in accordance with the restore command — if you select to restore specific scopes, the sequences associated with those scopes are restored, and no others.

## [](#prerequisites)Prerequisites

RBAC Privileges

To execute the ALTER SEQUENCE statement, you must have the _Query Manage Sequences_ privilege granted on the scope. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
alter-sequence ::= 'ALTER' 'SEQUENCE' sequence
                   ( alter-sequence-options | sequence-with )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/alter-sequence.png) 

The ALTER SEQUENCE statement provides two possible syntaxes for specifying options for a sequence.

| sequence               | (Required) A name that identifies the sequence within a namespace, bucket, and scope. See [Sequence Name](#sequence) below.    |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| alter-sequence-options | (Optional) One possible syntax for specifying options for the sequence. See [Sequence Options](#alter-sequence-options) below. |
| sequence-with          | (Optional) The other possible syntax for specifying options for the sequence. See [WITH Clause](#sequence-with) below.         |

### [](#sequence)Sequence Name

```ebnf
sequence ::= ( ( namespace ':' )? bucket '.' scope '.' )? identifier
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/sequence.png) 

The sequence name specifies the name of the sequence to alter.

Each sequence is associated with a given namespace, bucket, and scope. You must specify the namespace, bucket, and scope to refer to the sequence correctly.

| namespace  | (Optional) The [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the bucket which contains the sequence you want to alter. |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket     | (Optional) The bucket which contains the sequence you want to alter.                                                                          |
| scope      | (Optional) The scope which contains the sequence you want to alter.                                                                           |
| identifier | (Required) The name of the sequence. The sequence name is case-sensitive.                                                                     |

Currently, only the `default` namespace is available. If you omit the namespace, the default namespace in the current session is used.

If the [query context](../n1ql-intro/queriesandresults.md#query-context) is set, you can omit the bucket and scope from the statement. In this case, the bucket and scope for the sequence are taken from the query context.

The namespace, bucket, scope, and sequence name must follow the rules for [identifiers](identifiers.md). If the namespace, bucket, scope, or sequence name contain any special characters such as hyphens (-), you must wrap that part of the expression in backticks (\` \`).

### [](#alter-sequence-options)Sequence Options

```ebnf
alter-sequence-options ::= ( restart-with
                           | increment-by
                           | maxvalue
                           | minvalue
                           | cycle
                           | cache )*
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/alter-sequence-options.png) 

You can use the following optional clauses to specify individual attributes for the sequence. These clauses can occur in any order, but none of them can occur more than once in the statement.

| restart-with | [RESTART WITH Clause](#restart-with) |
| ------------ | ------------------------------------ |
| increment-by | [INCREMENT BY Clause](#increment-by) |
| maxvalue     | [MAXVALUE Clause](#maxvalue)         |
| minvalue     | [MINVALUE Clause](#minvalue)         |
| cycle        | [CYCLE Clause](#cycle)               |
| cache        | [Cache](#cache)                      |

#### [](#restart-with)RESTART WITH Clause

```ebnf
restart-with ::= 'RESTART' ( 'WITH' integer )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/restart-with.png) 

Use the RESTART keyword by itself to restart the sequence from its original starting value.

Use the RESTART WITH clause to restart the sequence from a new value.

If this clause is omitted, the sequence does not restart.

| integer | (Optional) The restart value for the sequence. |
| ------- | ---------------------------------------------- |

#### [](#increment-by)INCREMENT BY Clause

```ebnf
increment-by ::= 'INCREMENT' 'BY' integer
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/increment-by.png) 

Use the INCREMENT BY clause to specify the increment value of each step in the sequence.

If this clause is omitted, the increment value is not altered.

| integer | (Required) The step size for the sequence. Use a negative value for a descending sequence. |
| ------- | ------------------------------------------------------------------------------------------ |

#### [](#maxvalue)MAXVALUE Clause

```ebnf
maxvalue ::= 'MAXVALUE' integer | 'NO' 'MAXVALUE'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/maxvalue.png) 

Use the MAXVALUE clause to specify the maximum value for the sequence.

Use NO MAXVALUE to specify that the maximum value is the highest signed 64-bit integer, `263-1`.

If this clause is omitted, the maximum value is not altered.

| integer | (Optional) The maximum value for the sequence. |
| ------- | ---------------------------------------------- |

#### [](#minvalue)MINVALUE Clause

```ebnf
minvalue ::= 'MINVALUE' integer | 'NO' 'MINVALUE'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/minvalue.png) 

Use the MINVALUE clause to specify the minimum value for the sequence.

Use NO MINVALUE to specify that the minimum value is the lowest signed 64-bit integer, `-263`.

If this clause is omitted, the minimum value is not altered.

| integer | (Optional) The minimum value for the sequence. |
| ------- | ---------------------------------------------- |

#### [](#cycle)CYCLE Clause

```ebnf
cycle ::= 'CYCLE' | 'NO' 'CYCLE'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/cycle.png) 

Use the CYCLE clause to specify the whether the sequence should loop when it reaches the maximum or minimum value.

Use NO CYCLE to specify that the sequence should stop when it reaches the maximum or minimum value.

If this clause is omitted, the sequence behavior is not altered.

#### [](#cache)CACHE Clause

```ebnf
cache ::= 'CACHE' integer | 'NO' 'CACHE'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/cache.png) 

Use the CACHE clause to specify the cache size for the sequence.

Use NO CACHE to specify a cache size of `1`.

If this clause is omitted, the cache size is not altered.

| integer | (Optional) The cache size for the sequence. The value must be greater than 0. |
| ------- | ----------------------------------------------------------------------------- |

### [](#sequence-with)WITH Clause

```ebnf
index-with ::= 'WITH' expr
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/index-with.png) 

You can use the WITH clause to specify options for the sequence using a JSON object.

| expr | (Required) An object with the following properties. |
| ---- | --------------------------------------------------- |

| Name                     | Description                                                                                        | Schema          |
| ------------------------ | -------------------------------------------------------------------------------------------------- | --------------- |
| **restart** _optional_   | The restart value for the sequence. If unspecified, the sequence does not restart.                 | Integer         |
| **increment** _optional_ | The step size for the sequence. Use a negative value for a descending sequence.                    | Integer         |
| **max** _optional_       | The maximum value for the sequence.                                                                | Integer (int64) |
| **min** _optional_       | The minimum value for the sequence.                                                                | Integer (int64) |
| **cycle** _optional_     | Whether the sequence should continue when it reaches the specified maximum value or minimum value. | Boolean         |
| **cache** _optional_     | The cache size for the sequence. The value must be greater than 0.                                 | Integer         |

## [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Restart a sequence

This example assumes that you have created a sequence as follows.

```sqlpp
CREATE SEQUENCE seq3 IF NOT EXISTS START WITH 5 INCREMENT BY 5 MAXVALUE 1000 MINVALUE 0 CYCLE;
```

The following statement restarts the sequence at the original starting value.

```sqlpp
ALTER SEQUENCE seq3 RESTART;
```

The following query tests the sequence.

```sqlpp
SELECT NEXT VALUE FOR seq3;
```

The query returns the specified starting value, 5.

```json
[
  {
    "$1": 5
  }
]
```

Example 2\. Restart a sequence from a new starting value

This example assumes that you have created a sequence as follows.

```sqlpp
CREATE SEQUENCE seq3 IF NOT EXISTS START WITH 5 INCREMENT BY 5 MAXVALUE 1000 MINVALUE 0 CYCLE;
```

The following statement restarts the sequence at a new starting value.

```sqlpp
ALTER SEQUENCE seq3 RESTART WITH 25;
```

The following query tests the sequence.

```sqlpp
SELECT NEXT VALUE FOR seq3;
```

The query returns the specified starting value, 25.

```json
[
  {
    "$1": 25
  }
]
```

Example 3\. Alter the increment and maximum value of a sequence

This example assumes that you have created a sequence as follows.

```sqlpp
CREATE SEQUENCE seq3 IF NOT EXISTS START WITH 5 INCREMENT BY 5 MAXVALUE 1000 MINVALUE 0 CYCLE;
```

The following statement alters the increment and maximum value of the sequence.

```sqlpp
ALTER SEQUENCE seq3 INCREMENT BY 1 MAXVALUE 250;
```

Example 4\. Alter the cycling of a sequence

This example assumes that you have created a descending sequence as follows.

```sqlpp
CREATE SEQUENCE seq4 IF NOT EXISTS WITH {"start": 10, "increment": -1, "min": 0};
```

The following statement specifies that the sequence should count down from 10 again when it reaches 0.

```sqlpp
ALTER SEQUENCE seq4 WITH {"max": 10, "cycle": true};
```

Note that you must specify the maximum value to be `10`, even though the starting value is already set. If you didn't do this, the sequence would cycle to the highest possible value, `263-1`.

## [](#related-links)Related Links

* To create a sequence, see [CREATE SEQUENCE](createsequence.md).
* To drop a sequence, see [DROP SEQUENCE](dropsequence.md).
* To use a sequence in an expression, see [Sequence Operators](sequenceops.md).
* To monitor sequences, see [Monitor Sequences](../n1ql-intro/sysinfo.md#sys-sequences).