---
title: DROP SEQUENCE
description: The DROP SEQUENCE statement enables you to drop a sequence in a given scope.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/dropsequence.adoc
  xref: xref:7.6@server:n1ql:n1ql-language-reference/dropsequence.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/dropsequence.html)

# DROP SEQUENCE

> The DROP SEQUENCE statement enables you to drop a sequence in a given scope. 

## [](#purpose)Purpose

A sequence is a construct that returns a sequence of integer values, one at a time, rather like a counter. Each time you request the next value for a sequence, an increment is added to the previous value, and the resulting value is returned. This is useful for generating values such as sequential ID numbers, where you need the Query service to keep track of the current value from one query to the next.

## [](#prerequisites)Prerequisites

RBAC Privileges

To execute the DROP SEQUENCE statement, you must have the _Query Manage Sequences_ privilege granted on the scope. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
drop-sequence ::= 'DROP' 'SEQUENCE' ( sequence ( 'IF' 'EXISTS' )? |
                  ( 'IF' 'EXISTS' )? sequence )
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/drop-sequence.png) 

| sequence | (Required) A name that identifies the sequence within a namespace, bucket, and scope. See [Sequence Name](#sequence) below. |
| -------- | --------------------------------------------------------------------------------------------------------------------------- |

### [](#sequence)Sequence Name

```ebnf
sequence ::= ( ( namespace ':' )? bucket '.' scope '.' )? identifier
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/sequence.png) 

The sequence name specifies the name of the sequence to drop.

Each sequence is associated with a given namespace, bucket, and scope. You must specify the namespace, bucket, and scope to refer to the sequence correctly.

| namespace  | (Optional) The [namespace](../n1ql-intro/queriesandresults.md#logical-hierarchy) of the bucket which contains the sequence you want to drop. |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| bucket     | (Optional) The bucket which contains the sequence you want to drop.                                                                          |
| scope      | (Optional) The scope which contains the sequence you want to drop.                                                                           |
| identifier | (Required) The name of the sequence. The sequence name is case-sensitive.                                                                    |

Currently, only the `default` namespace is available. If you omit the namespace, the default namespace in the current session is used.

If the [query context](../n1ql-intro/queriesandresults.md#query-context) is set, you can omit the bucket and scope from the statement. In this case, the bucket and scope for the sequence are taken from the query context.

The namespace, bucket, scope, and sequence name must follow the rules for [identifiers](identifiers.md). If the namespace, bucket, scope, or sequence name contain any special characters such as hyphens (-), you must wrap that part of the expression in backticks (\` \`).

### [](#if-exists-clause)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified sequence doesn't exist.

When the sequence does not exist within the specified context:

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

## [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Drop a sequence in a specified scope

This statement drops a sequence in the specified scope.

```sqlpp
DROP SEQUENCE `travel-sample`.inventory.seq1;
```

Example 2\. Drop a sequence in the current query context

This statement drops a sequence in the current query context, if a sequence of that name exists.

```sqlpp
DROP SEQUENCE seq2 IF EXISTS;
```

## [](#related-links)Related Links

* To create a sequence, see [CREATE SEQUENCE](createsequence.md).
* To alter a sequence, see [ALTER SEQUENCE](altersequence.md).
* To use a sequence in an expression, see [Sequence Operators](sequenceops.md).
* To monitor sequences, see [Monitor Sequences](../n1ql-intro/sysinfo.md#sys-sequences).