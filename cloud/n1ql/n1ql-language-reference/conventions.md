---
title: Conventions
description: The SQL++ syntax descriptions in the documentation use some
  notational conventions that you need to be familiar with.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/conventions.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:n1ql:n1ql-language-reference/conventions.adoc[]
---

[View original HTML](/cloud/n1ql/n1ql-language-reference/conventions.html)

# Conventions

> The SQL++ syntax descriptions in the documentation use some notational conventions that you need to be familiar with. 

The syntax descriptions are written using a [W3C dialect of EBNF](https://www.w3.org/TR/REC-xml/#sec-notation) (Extended Backus-Naur Format).

__Table 1\. Notational conventions for SQL++ syntax descriptions__
| Convention              | Notation | Example                    | Description                                                                                                                                                                     |
| ----------------------- | -------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Upper case              |          | 'SELECT'                   | Indicates keywords in the syntax description. Delimited by quotes, to show that the keyword is required in the syntax. Note that you can enter keywords in upper or lower case. |
| Single or double quotes | '' or "" | '(' ')' ','                | Indicate that the text between the quotes is required in the syntax.                                                                                                            |
| Pipe                    | \|       | 'AND' \| 'OR'              | Separates alternatives.                                                                                                                                                         |
| Parentheses             | ( )      | 'USING' ( 'GSI' \| 'FTS' ) | Delimit alternatives, or group optional and repeated elements, where necessary.                                                                                                 |
| Question mark           | ?        | element? (',' element)?    | Indicates that the element or group preceding the question mark is optional.                                                                                                    |
| Plus sign               | +        | element+ (',' element)+    | Indicates that the element or group preceding the plus sign may appear one or many times.                                                                                       |
| Asterisk                | \*       | element\* (',' element)\*  | Indicates that the element or group preceding the asterisk may appear zero, one, or many times.                                                                                 |

Syntax diagrams generated using [Railroad Diagram Generator](https://www.bottlecaps.de/rr/ui).