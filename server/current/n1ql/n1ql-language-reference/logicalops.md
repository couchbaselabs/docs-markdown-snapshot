---
title: Logical Operators
description: Logical terms let you combine other expressions using Boolean logic.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/logicalops.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:n1ql:n1ql-language-reference/logicalops.adoc[]
---

[View original HTML](/server/current/n1ql/n1ql-language-reference/logicalops.html)

# Logical Operators

Logical terms let you combine other expressions using [Boolean logic](booleanlogic.md). SQL++ provides the following logical operators:

* AND
* OR
* NOT

In SQL++, logical operators have their usual meaning; however, Boolean propositions can evaluate to NULL or MISSING as well as to TRUE and FALSE. The truth tables for these operators therefore use four-valued logic.

## [](#logical-op-and)AND

```ebnf
and ::= cond 'AND' cond
```

![Syntax diagram](../_images/n1ql-language-reference/and.png) 

AND evaluates to TRUE only if both conditions are TRUE.

__Table 1\. AND Truth Table__
|             | TRUE    | FALSE | NULL    | MISSING |
| ----------- | ------- | ----- | ------- | ------- |
| **TRUE**    | TRUE    | FALSE | NULL    | MISSING |
| **FALSE**   | FALSE   | FALSE | FALSE   | FALSE   |
| **NULL**    | NULL    | FALSE | NULL    | MISSING |
| **MISSING** | MISSING | FALSE | MISSING | MISSING |

## [](#or-operator)OR

```ebnf
or ::= cond 'OR' cond
```

![Syntax diagram](../_images/n1ql-language-reference/or.png) 

OR evaluates to TRUE if one of the conditions is TRUE.

__Table 2\. OR Truth Table__
|             | TRUE | FALSE   | NULL | MISSING |
| ----------- | ---- | ------- | ---- | ------- |
| **TRUE**    | TRUE | TRUE    | TRUE | TRUE    |
| **FALSE**   | TRUE | FALSE   | NULL | MISSING |
| **NULL**    | TRUE | NULL    | NULL | NULL    |
| **MISSING** | TRUE | MISSING | NULL | MISSING |

## [](#logical-op-not)NOT

```ebnf
not ::= 'NOT' cond
```

![Syntax diagram](../_images/n1ql-language-reference/not.png) 

NOT evaluates to TRUE if the condition is FALSE, and vice versa.

__Table 3\. NOT Truth Table__
|             | NOT     |
| ----------- | ------- |
| **TRUE**    | FALSE   |
| **FALSE**   | TRUE    |
| **NULL**    | NULL    |
| **MISSING** | MISSING |

## [](#related-links)Related Links

For further details, refer to [Boolean Logic](booleanlogic.md).