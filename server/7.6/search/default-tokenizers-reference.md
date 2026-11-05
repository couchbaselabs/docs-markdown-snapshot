---
title: Default Tokenizers
description: Tokenizers control how the Search Service splits input strings into
  individual tokens.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/default-tokenizers-reference.adoc
  xref: xref:7.6@server:search:default-tokenizers-reference.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/search/default-tokenizers-reference.html)

# Default Tokenizers

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> Tokenizers control how the Search Service splits input strings into individual tokens. 

You can use a [tokenizer](customize-index.md#tokenizers) when you [create a custom analyzer](create-custom-analyzer.md). Choose a default tokenizer or [create your own](create-custom-tokenizer.md).

The following default tokenizers are available:

| Tokenizer  | Description                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| hebrew     | Separates an input string into tokens that contain only Hebrew alphabet characters. Punctuation marks and numbers are excluded. |
| letter     | Separates an input string into tokens that contain only Latin alphabet characters. Punctuation marks and numbers are excluded.  |
| single     | Creates a single token from the input string. Special characters and whitespace are preserved.                                  |
| unicode    | Separates input strings into tokens based on [Unicode Word Boundaries](http://www.unicode.org/reports/tr29/#Word%5FBoundaries). |
| web        | Creates tokens from an input string that match email address, URL, Twitter username, and hashtag patterns.                      |
| whitespace | Separates an input string into tokens based on the location of whitespace characters.                                           |