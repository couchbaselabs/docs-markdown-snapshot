---
title: Create a Custom Token Filter
description: Create a custom token filter with the Couchbase Server Web Console
  to change how the Search Service creates tokens from Search index content and
  Search queries.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/create-custom-token-filter.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:search:create-custom-token-filter.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/search/create-custom-token-filter.html)

# Create a Custom Token Filter

> Create a custom token filter with the Couchbase Server Web Console to change how the Search Service creates tokens from Search index content and Search queries. 

[Token filters](customize-index.md#token-filters) can improve your search results by removing characters from your Search index or Search queries that prevent matches.

## [](#prerequisites)Prerequisites

* You’ve created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You’ve logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To create a custom token filter with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the Search index where you want to create a custom token filter.
3. Click **Edit**.
4. Expand **Customize Index** **Custom Filters**.
5. Click **Add Token Filter**.
6. In the **Name** field, enter a name for the token filter.

You can create any of the following custom token filters:

* [dict\_compound](#dict-compound): Use a wordlist to find and create tokens from compound words in existing tokens.
* [edge\_ngram](#edge-ngram): Use a set character length to create tokens from the start or end of existing tokens.
* [elision](#elision): Use a wordlist to remove elisions from input tokens.
* [keyword\_marker](#keyword-marker): Use a wordlist of keywords to find and create new tokens.
* [length](#length): Use a set character length to filter out tokens that are too long or too short.
* [ngram](#ngram): Use a set character length to create new tokens.
* [normalize\_unicode](#normalize-unicode): Use Unicode Normalization to convert tokens.
* [shingle](#shingle): Use a set character length and separator to concatenate and create new tokens.
* [stop\_tokens](#stop-tokens): Use a wordlist to find and remove words from tokens.
* [truncate\_token](#truncate-token): Use a set character length to truncate existing tokens.

### [](#dict-compound)Create a Custom `dict_compound` Token Filter

A `dict_compound` token filter uses a wordlist to find subwords inside an input token. If the token filter finds a subword inside a compound word, it turns it into a separate token.

For example, if you had a wordlist that contained `play` and `jump`, the token filter converts `playful jumping` into two tokens: `play` and `jump`.

![dict](_images/dict-3bbc6a301122c6fca086b287e7ea7c7af2e758bb.svg) 

To create a new `dict_compound` token filter with the Couchbase Server Web Console:

1. In the **Type** field, select **dict\_compound**.
2. In the **Sub Words** list, select the wordlist to use to find subwords in input tokens.  
You can choose your own [custom wordlist](create-custom-wordlist.md) or a [default wordlist](default-wordlists-reference.md). Each subword match creates a new token.
3. Click **Save**.

### [](#edge-ngram)Create a Custom `edge_ngram` Token Filter

An `edge_ngram` token filter uses a specified range to create new tokens. You can also choose whether to create the new token from the start or backward from the end of the input token.

For example, if you had a miminum of four and a maximum of five with an input token of `breweries`, the token filter creates the tokens `brew` and `brewe`.

![edge](_images/edge-53b440c158199de38d7528e48e6b15a36426f3d9.svg) 

To create a new `edge_ngram` token filter with the Couchbase Server Web Console:

1. In the **Type** field, select **edge\_ngram**.
2. Do one of the following:

  1. To create new tokens starting from the end of input tokens, select **Back**.
  2. To create new tokens starting from the beginning of input tokens, clear **Back**.
3. In the **Min** field, enter the minimum character length for a new token.
4. In the **Max** field, enter the maximum character length for a new token.
5. Click **Save**.

### [](#elision)Create a Custom `elision` Token Filter

An `elision` token filter removes elisions from input tokens.

For example, if you had the `stop_fr` wordlist in an elision token filter, the token `je m’appelle John` becomes the tokens `je`, `appelle`, and `John`.

![elision](_images/elision-f3bfe6d06370309959606d5b1299ce61a2a9feef.svg) 

To create a new `elision` token filter with the Couchbase Server Web Console:

1. In the **Type** field, select **elision**.
2. In the **Articles** list, select a wordlist to use to find elisions in input tokens.  
You can choose your own [custom wordlist](create-custom-wordlist.md) or a [default wordlist](default-wordlists-reference.md).
3. Click **Save**.

### [](#keyword-marker)Create a Custom `keyword_marker` Token Filter

A `keyword_marker` token filter finds keywords in an input token and turns them into tokens.

For example, if you had a wordlist that contained the keyword `beer`, the token `beer and breweries` becomes the token `beer`.

![keyword](_images/keyword-bfcc125930301861a91933fe34a0f600db3f8eee.svg) 

To create a new `keyword_marker` token filter with the Couchbase Server Web Console:

1. In the **Type** field, select **keyword\_marker**.
2. In the **Keywords** list, select a wordlist to use to find keywords to create tokens.  
You can choose your own [custom wordlist](create-custom-wordlist.md) or a [default wordlist](default-wordlists-reference.md).
3. Click **Save**.

### [](#length)Create a Custom `length` Token Filter

A `length` token filter removes tokens that are shorter or longer than a set character length.

For example, if you had a range with a minimum of two and a maximum of four, the token `beer and breweries` becomes the tokens `beer` and `and`.

![length](_images/length-1b79deaad25f915c0885ca143a6685dad8939b92.svg) 

To create a new `length` token filter with the Couchbase Server Web Console:

1. In the **Type** field, select **length**.
2. In the **Min** field, enter the minimum character length for a new token.
3. In the **Max** field, enter the maximum character length for a new token.
4. Click **Save**.

### [](#ngram)Create a Custom `ngram` Token Filter

An `ngram` token filter uses a specified character length to split an input token into new tokens.

For example, if you had a range with a minimum of four and a maximum of five, the token `beers` becomes the tokens `beer`, `beers`, and `eers`.

![ngram](_images/ngram-2126d46f08f25dc72513faacb0ff70924f58021e.svg) 

To create a new `ngram` token filter with the Couchbase Server Web Console:

1. In the **Type** field, select **ngram**.
2. In the **Min** field, enter the minimum character length for a new token.
3. In the **Max** field, enter the maximum character length for a new token.
4. Click **Save**.

### [](#normalize-unicode)Create a Custom `normalize_unicode` Token Filter

A `normalize_unicode` token filter uses a specified Unicode Normalization form to create new tokens.

To create a new `normalize_unicode` token filter with the Couchbase Server Web Console:

1. In the **Type** field, select **normalize\_unicode**.
2. In the **Form** list, select the type of Unicode normalization to apply:

  * **nfc**: Use canonical decomposition and canonical composition to normalize characters. The token filter separates combined unicode characters, then merges them into a single character.
  * **nfd**: Use canonical decomposition to normalize characters. The token filter separates combined unicode characters.
  * **nfkc**: Use compatibility decomposition to normalize characters. The token filter converts unicode characters to remove variants.
  * **nfkd**: Use compatibility decomposition and canonical composition to normalize characters. The token filter removes variants, then separates combined unicode characters to merge them into a single character.
3. Click **Save**.

### [](#shingle)Create a Custom `shingle` Token Filter

A `shingle` token filter uses a specified character length and separator to create new tokens.

For example, if you use a [whitespace tokenizer](#guides:search/default-tokenizers-reference.adoc#whitespace), a range with a minimum of two and a maximum of three, and a space as a separator, the token `abc def` becomes `abc`, `def`, and `abc def`.

![shingle](_images/shingle-bc68693147c520ba6def14401d61d5ba22710a7d.svg) 

To create a new `shingle` token filter with the Couchbase Server Web Console:

1. In the **Type** field, select **shingle**.
2. In the **Min** field, enter the minimum character length for a new token before concatenation.
3. In the **Max** field, enter the maximum character length for a new token before concatenation.
4. Do one of the following:

  1. To include the original token as an output token, select **Include original token**.
  2. To remove the original token from output, clear **Include original token**.
5. (Optional) In the **Separator** field, enter a character or characters to add in between concatenated tokens.
6. (Optional) In the **Filler** field, enter a character or characters to replace tokens that are removed by another token filter.
7. Click **Save**.

### [](#stop-tokens)Create a Custom `stop_tokens` Token Filter

A `stop_tokens` token filter uses a wordlist to remove specific tokens from input.

For example, if you have a wordlist that contains the word `and`, the token `beers and breweries` becomes `beers` and `breweries`.

![stop](_images/stop-de565d1d82022c6d4d8d3d4f574c90b8c13b24e0.svg) 

To create a new `stop_tokens` token filter with the Couchbase Server Web Console:

1. In the **Type** field, select **stop\_tokens**.
2. In the **Stop Words** list, select a wordlist to use to remove tokens.  
You can choose your own [custom wordlist](create-custom-wordlist.md) or a [default wordlist](default-wordlists-reference.md).
3. Click **Save**.

### [](#truncate-token)Create a Custom `truncate_token` Token Filter

A `truncate_token` token filter uses a specified character length to shorten any input tokens that are too long.

For example, if you had a `length` of four, the token `beer and breweries` becomes `beer`, `and`, and `brewe`.

![truncate](_images/truncate-eb79f973d761c93658082540e5665474e15eebbe.svg) 

To create a new `truncate_token` token filter with the Couchbase Server Web Console:

1. In the **Type** field, select **truncate\_token**.
2. In the **Length** field, enter the maximum character length for an output token.
3. Click **Save**.

## [](#next-steps)Next Steps

After you create a custom token filter, you can use it with [a custom analyzer](create-custom-analyzer.md).

To continue customizing your Search index, you can also:

* [Set the Type Identifier for a Search Index](set-type-identifier.md)
* [Create a Type Mapping](create-type-mapping.md)
* [Create a Child Field](create-child-field.md)
* [Create a Child Mapping](create-child-mapping.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Wordlist](create-custom-wordlist.md)
* [Set Search Index Advanced Settings](set-advanced-settings.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).