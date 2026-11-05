---
title: String Operators
description: SQL++ provides the concatenation string operator.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/stringops.adoc
  xref: xref:7.6@server:n1ql:n1ql-language-reference/stringops.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/stringops.html)

# String Operators

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

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