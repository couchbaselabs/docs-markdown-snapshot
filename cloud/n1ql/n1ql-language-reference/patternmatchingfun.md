---
title: Pattern-Matching Functions
description: Pattern-matching functions allow you to find regular expression
  patterns in strings or attributes.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/patternmatchingfun.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:n1ql:n1ql-language-reference/patternmatchingfun.adoc[]
---

[View original HTML](/cloud/n1ql/n1ql-language-reference/patternmatchingfun.html)

# Pattern-Matching Functions

Pattern-matching functions allow you to find regular expression patterns in strings or attributes. Regular expressions can formally represent various string search patterns using different special characters to indicate wildcards, positional characters, repetition, optional or mandatory sequences of letters, etc. SQL++ functions are available to find matching patterns, find position of matching pattern, or replace a pattern with a new string.

For more information on all supported REGEX patterns, see <https://golang.org/pkg/regexp/syntax>.

> [!NOTE]
> SQL++ supports regular expressions supported by The Go Programming Language version 1.8\.

## [](#section%5Fregex%5Fcontains)REGEXP\_CONTAINS(`expression`, `pattern`)

This function has an alias [REGEX\_CONTAINS()](#aliases).

### [](#arguments)Arguments

expression

String, or any SQL++ expression that evaluates to a string.

pattern

String representing a supported regular expression.

### [](#return-value)Return Value

Returns TRUE if the string value contains any sequence that matches the regular expression pattern.

### [](#example)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Query

```sqlpp
SELECT name
FROM landmark
WHERE REGEXP_CONTAINS(name, "In+.*")
LIMIT 5;
```

Results

```json
[
  {
    "name": "Beijing Inn"
  },
  {
    "name": "Sportsman Inn"
  },
  {
    "name": "In-N-Out Burger"
  },
  {
    "name": "Mel's Drive-In"
  },
  {
    "name": "Inverness Castle"
  }
]
```

## [](#section%5Fregex%5Flike)REGEXP\_LIKE(`expression`, `pattern`)

This function has an alias [REGEX\_LIKE()](#aliases).

### [](#arguments-2)Arguments

expression

String, or any SQL++ expression that evaluates to a string.

pattern

String representing a supported regular expression.

### [](#return-value-2)Return Value

Returns TRUE if the string value exactly matches the regular expression pattern.

### [](#example-2)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Query

```sqlpp
SELECT name
FROM landmark
WHERE REGEXP_LIKE(name, "In+.*")
LIMIT 5;
```

Results

```json
[
  {
    "name": "In-N-Out Burger"
  },
  {
    "name": "Inverness Castle"
  },
  {
    "name": "Inverness Museum & Art Gallery"
  },
  {
    "name": "Inverness Botanic Gardens"
  },
  {
    "name": "International Petroleum Exchange"
  }
]
```

## [](#section%5Fregex%5Fmatches)REGEXP\_MATCHES(`expression`, `pattern`)

### [](#arguments-3)Arguments

expression

String, or any SQL++ expression that evaluates to a string.

pattern

String representing a supported regular expression.

### [](#return-value-3)Return Value

Returns an array of all substrings matching the expression _pattern_ within the input string _expression_. Returns an empty array if no match is found.

### [](#examples)Examples

REGEXP\_MATCHES() Example 1

The following query finds all words beginning with upper or lower case B.

Query

```sqlpp
SELECT REGEXP_MATCHES("So, 'twas better Betty Botter bought a bit of better butter",
                      "\\b[Bb]\\w+"); (1)
```

| **1** | The backslash that introduces an escape sequence in the regular expression must itself be escaped by another backslash in the SQL++ query. So \\b (word boundary) must be entered as \\\\b and \\w (word character) must be entered as \\\\w. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Results

```json
[
  {
    "$1": [
      "better",
      "Betty",
      "Botter",
      "bought",
      "bit",
      "better",
      "butter"
    ]
  }
]
```

REGEXP\_MATCHES() Example 2

The following query finds sequences of two words beginning with upper or lower case B.

Query

```sqlpp
SELECT REGEXP_MATCHES("So, 'twas better Betty Botter bought a bit of better butter",
                      "\\b[Bb]\\w+ \\b[Bb]\\w+");
```

Results

```json
[
  {
    "$1": [
      "better Betty",
      "Botter bought", (1)
      "better butter"
    ]
  }
]
```

| **1** | Note that Betty Botter is not found in this example, because Betty has already been found by the first match. |
| ----- | ------------------------------------------------------------------------------------------------------------- |

## [](#section%5Fregex%5Fposition)REGEXP\_POSITION(`expression`, `pattern`)

This function has an alias [REGEX\_POSITION()](#aliases).

### [](#arguments-4)Arguments

expression

String, or any SQL++ expression that evaluates to a string.

pattern

String representing a supported regular expression.

### [](#return-value-4)Return Value

Returns first position of the occurrence of the regular expression _pattern_ within the input string _expression_. Returns -1 if no match is found. Position counting starts from zero.

### [](#example-3)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

The following query finds positions of first occurrence of vowels in each word of the _name_ attribute.

Query

```sqlpp
SELECT name, ARRAY REGEXP_POSITION(x, "[aeiou]") FOR x IN TOKENS(name) END
FROM hotel
LIMIT 2;
```

Results

```json
[
  {
    "$1": [
      1,
      1,
      1
    ],
    "name": "Medway Youth Hostel"
  },
  {
    "$1": [
      2,
      1,
      1
    ],
    "name": "The Balmoral Guesthouse"
  }
]
```

Note that the order of tokens in the second result may be different.

## [](#section%5Fregex%5Freplace)REGEXP\_REPLACE(`expression`, `pattern`, `repl` \[, `n`\])

This function has an alias [REGEX\_REPLACE()](#aliases).

### [](#arguments-5)Arguments

expression

String, or any SQL++ expression that evaluates to a string.

pattern

String representing a supported regular expression.

repl

String, or any SQL++ expression that evaluates to a string.

n

\[Optional\] The maximum number of times to find and replace the matching pattern.

### [](#return-value-5)Return Value

Returns new string with occurrences of pattern replaced with _repl_. If _n_ is given, at the most _n_ replacements are performed. If _n_ is not provided, all matching occurrences are replaced.

### [](#examples-2)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

REGEXP\_REPLACE() Example 1

Query

```sqlpp
SELECT REGEXP_REPLACE("Sql++ is sql for NoSql", "[sS][qQ][lL]", "SQL"),
       REGEXP_REPLACE("Winning innings Inn", "[Ii]n+", "Hotel", 6),
       REGEXP_REPLACE("Winning innings Inn", "[IiNn]+g", upper("inning"), 2);
```

Results

```json
[
  {
    "$1": "SQL++ is SQL for NoSQL",
    "$2": "WHotelHotelg HotelHotelgs Hotel",
    "$3": "WINNING INNINGs Inn"
  }
]
```

REGEXP\_REPLACE() Example 2

In this example, the query retrieves first 4 documents and replaces the pattern of repeating n with emphasized NNNN.

Query

```sqlpp
SELECT name, REGEXP_REPLACE(name, "n+", "NNNN") as new_name
FROM airline
LIMIT 4;
```

Results

```json
[
  {
    "name": "40-Mile Air",
    "new_name": "40-Mile Air"
  },
  {
    "name": "Texas Wings",
    "new_name": "Texas WiNNNNgs"
  },
  {
    "name": "Atifly",
    "new_name": "Atifly"
  },
  {
    "name": "Jc royal.britannica",
    "new_name": "Jc royal.britaNNNNica"
  }
]
```

## [](#section%5Fregex%5Fsplit)REGEXP\_SPLIT(`expression`, `pattern`)

### [](#arguments-6)Arguments

expression

String, or any SQL++ expression that evaluates to a string.

pattern

String representing a supported regular expression.

### [](#return-value-6)Return Value

Returns an array of all the substrings created by splitting the input string _expression_ at each occurrence of the expression _pattern_. Returns an empty array if no match is found.

### [](#example-4)Example

Query

```sqlpp
SELECT REGEXP_SPLIT("C:\\Program Files\\couchbase\\server\\bin", "[\\\\]") AS Windows, (1)
REGEXP_SPLIT("/opt/couchbase/bin", "/") AS Unix;
```

| **1** | The regular expression \[\\\\\\\\\] matches the escaped backslash \\\\. |
| ----- | ----------------------------------------------------------------------- |

Results

```json
[
  {
    "Unix": [
      "", (1)
      "opt",
      "couchbase",
      "bin"
    ],
    "Windows": [
      "C:",
      "Program Files",
      "couchbase",
      "server",
      "bin"
    ]
  }
]
```

| **1** | The REGEXP\_SPLIT function returns any zero-length matches that occur at the start of the _expression_ string, except when the split pattern is zero-length. Otherwise, it returns any zero-length matches immediately after a previous match. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#aliases)Aliases

Some pattern-matching functions have an alias whose name begins with `REGEX_`.

* `REGEX_CONTAINS()` is an alias for [REGEXP\_CONTAINS()](#section%5Fregex%5Fcontains).
* `REGEX_LIKE()` is an alias for [REGEXP\_LIKE()](#section%5Fregex%5Flike).
* `REGEX_POSITION()` is an alias for [REGEXP\_POSITION()](#section%5Fregex%5Fposition).
* `REGEX_REPLACE()` is an alias for [REGEXP\_REPLACE()](#section%5Fregex%5Freplace).