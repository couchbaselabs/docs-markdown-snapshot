---
title: XDCR Regular Expressions
description: XDCR Regular Expressions can be used to specify character-matches,
  and thereby determine which documents should be included in filtered XDCR
  replications.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/xdcr-reference/pages/xdcr-regular-expressions.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:xdcr-reference:xdcr-regular-expressions.adoc[]
---

[View original HTML](/server/7.2/xdcr-reference/xdcr-regular-expressions.html)

# XDCR Regular Expressions

> XDCR Regular Expressions can be used to specify character-matches, and thereby determine which documents should be included in filtered XDCR replications. 

## [](#xdcr-regular-expressions)XDCR Regular Expressions

The following JavaScript regular expressions (RegExes) can be used for XDCR Advanced Filtering. Note that regular expressions are case-sensitive: a lowercase '`a`' is distinct from an uppercase '`A`'. You can enclose a range of characters in square brackets, to match against all of those characters.

See [Regular Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular%5FExpressions) and [Regular-Expressions.info](https://www.regular-expressions.info/), for further information.

| Expression    | Description                                                                                                                                                                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[tT\]here    | Matches against 'There' and 'there'                                                                                                                                                                                                                         |
| \[ \]         | Can be used on a range of characters separated by a \- character.                                                                                                                                                                                           |
| \[0-9\]       | Matches any digit.                                                                                                                                                                                                                                          |
| \[A-Z\]       | Matches any uppercase alpha character.                                                                                                                                                                                                                      |
| \[A-Za-z0-9\] | Matches any alphanumeric character.                                                                                                                                                                                                                         |
| ^             | Matches the beginning of input. For example, ^a matches abb and ab; but does _not_ match ba, bab, or bba. Used within square brackets, as the first character, ^ implies _negation_: therefore, \[^0-9\] matches against any character that is not a digit. |
| $             | Matches the end of input. For example, a$ matches ba and bba; but does _not_ match abb, bab, or ab.                                                                                                                                                         |

Ranges can be used to specify a group of characters. The following shortcuts are also available:

| Expression | Description                                                                            |
| ---------- | -------------------------------------------------------------------------------------- |
| .          | Matches against any character.                                                         |
| \\d        | Matches against a digit \[0-9\].                                                       |
| \\D        | Matches against a non-digit \[^0-9\].                                                  |
| \\s        | Matches against a whitespace character (such as a tab, space, or line-feed character). |
| \\S        | Matches against a non-whitespace character.                                            |
| \\w        | Matches against an alphanumeric character \[a-zA-Z\_0-9\].                             |
| \\W        | Matches against a non-alphanumeric character.                                          |
| \\xhh      | Matches against a control character (for the hexadecimal character hh).                |
| \\uhhhh    | Matches against a Unicode character (for the hexadecimal character hhhh).              |

Note that since the backslash character is used to denote a specific search expression, a double backslash (`\\`) must be entered when the backslash is the search target.

To match against occurrences of a character or expression, you can use the following.

| Expression | Description                                                                       |
| ---------- | --------------------------------------------------------------------------------- |
| \*         | Matches against zero or more occurrences of the previous character or expression. |
| +          | Matches against one or more occurrences of the previous character or expression.  |
| ?          | Matches zero or one occurrence of the previous character or expression.           |
| {n}        | Matches n occurrences of the previous character or expression.                    |
| {n,m}      | Matches from n to m occurrences of the previous character or expression.          |
| {n,}       | Matches at least n occurrences of the previous character or expression.           |