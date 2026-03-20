---
title: Identifiers
description: An identifier is a symbolic reference to a value in the current
  context of a query.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/identifiers.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:n1ql:n1ql-language-reference/identifiers.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/identifiers.html)

# Identifiers

> An identifier is a symbolic reference to a value in the current context of a query. Identifiers can include keyspace names, fields within documents, and aliases. SQL++ identifiers are case-sensitive. 

An identifier can either be escaped or unescaped.

```ebnf
identifier ::= unescaped-identifier | escaped-identifier
```

![Syntax diagram](../_images/n1ql-language-reference/identifier.png) 

For example, if the current context is the document `{"name": "n1ql"}`, then the identifier `name` would evaluate to the value `n1ql`.

## [](#unescaped-identifiers)Unescaped Identifiers

Unescaped identifiers cannot support the full range of identifiers allowed in a JSON document, but do support the most common ones with a simpler syntax.

```ebnf
unescaped-identifier ::= [a-zA-Z_] ( [0-9a-zA-Z_$] )*
```

![Syntax diagram](../_images/n1ql-language-reference/unescaped-identifier.png) 

## [](#escaped-identifiers)Escaped Identifiers

Escaped identifiers are surrounded by backticks `` ` `` and support all identifiers in JSON. You can use the backtick character within an escaped identifier by specifying two consecutive backtick characters. Keywords cannot be escaped; therefore, escaped identifiers can overlap with keywords.

```ebnf
escaped-identifier ::= '`' char+ '`'
```

![Syntax diagram](../_images/n1ql-language-reference/escaped-identifier.png) 

For example, if you have a hyphen in an attribute name, it can be referred to as `` `first-name` ``.

Identifiers can be expressed using the dot notation, where the left-most portion of a dotted identifier refers to the name of the data source. For example, in the query `` SELECT `beer-sample`.name FROM `beer-sample` ``, `` `beer-sample`.name `` is a more formal way of expressing the identifier name.

## [](#identifier-alias)Aliases

Aliases give a temporary name to identifiers.

When an alias collides with a keyspace or field name in the same scope, the identifier always refers to the alias. This enables consistent behavior in scenarios where an identifier only collides in some documents.

The following table describes some rules that apply when referring to the new names created by aliases:

| Aliases in ... Clause | Create New Names That May be Referred to ...       |
| --------------------- | -------------------------------------------------- |
| WITH                  | Anywhere within the scope of the given query block |
| FROM                  | Anywhere within the scope of the given query block |
| LET                   | Anywhere within the scope of the given query block |
| LETTING               | HAVING, SELECT, and ORDER BY clauses               |
| SELECT                | SELECT and ORDER BY clauses                        |
| FOR                   | The local collection expression                    |