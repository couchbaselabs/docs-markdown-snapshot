---
title: Escaping
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-query-string-syntax-escaping.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-query-string-syntax-escaping.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-query-string-syntax-escaping.html)

# Escaping

The following quoted-string enumerates the characters which may be escaped:

"+-=&|><!(){}[]^\"~*?:\\/ "

> [!NOTE]
> This list contains the space character.

In order to escape these characters, they are prefixed with the `\` (backslash) character. In all cases, using the escaped version produces the character itself and is not interpreted by the lexer.

For example:

* `my\ name` is interpreted as a single argument to a match query with the value "my name".
* `"contains a\" character"` is interpreted as a single argument to a phrase query with the value `contains a " character`.