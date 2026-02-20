---
title: String Operators
description: SQL++ provides the concatenation string operator.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/stringops.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:n1ql:n1ql-language-reference/stringops.adoc[]
---

[View original HTML](/server/7.2/n1ql/n1ql-language-reference/stringops.html)

# String Operators

SQL++ provides the concatenation string operator.

## [](#concatenation)Concatenation

The concatenation operator joins two strings. The result of the concatenation operator is also a string.

### [](#syntax)Syntax

```ebnf
concatenation-term ::= expr '||' expr
```

![Syntax diagram](../_images/n1ql-language-reference/concatenation-term.png) 

### [](#example)Example

The following example shows concatenation of two strings.

Query

```sqlpp
WITH airline AS (
   [
      { "name": "Delta Airlines", "code": "DL" },
      { "name": "United Airlines", "code": "UA" }
   ]
)
SELECT name || " (" || code || ")" AS full_airline_name
FROM airline
```

Result

```json
[
  {
    "full_airline_name": "Delta Airlines (DL)"
  },
  {
    "full_airline_name": "United Airlines (UA)"
  }
]
```

## [](#related-links)Related Links

Refer to [Comparison Operators](comparisonops.md) for string comparisons.