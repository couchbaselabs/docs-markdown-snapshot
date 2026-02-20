---
title: Create a Custom Tokenizer
description: Create a custom tokenizer with the Couchbase Server Web Console to
  change how the Search Service creates tokens for matching Search index content
  to a Search query.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/create-custom-tokenizer.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:search:create-custom-tokenizer.adoc[]
---

[View original HTML](/server/current/search/create-custom-tokenizer.html)

# Create a Custom Tokenizer

> Create a custom tokenizer with the Couchbase Server Web Console to change how the Search Service creates tokens for matching Search index content to a Search query. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

You can create 2 types of custom tokenizers:

| Tokenizer Type                | Description                                                                                                                                                                         |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Regular expression](#regexp) | The tokenizer uses any input that matches the regular expression to create new tokens.                                                                                              |
| [Exception](#excep)           | The tokenizer removes any input that matches the regular expression, and creates tokens from the remaining input. You can choose another tokenizer to apply to the remaining input. |

### [](#regexp)Create a Regular Expression Tokenizer

To create a regular expression tokenizer with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the Search index where you want to create a custom tokenizer.
3. Click **Edit**.
4. Expand **Customize Index** **Custom Filters**.
5. Click **Add Tokenizer**.
6. In the **Name** field, enter a name for the custom tokenizer.
7. In the **Type** field, select **regexp**.
8. In the **Regular Expression** field, enter the regular expression to use to split input into tokens.
9. Click **Save**.

### [](#excep)Create an Exception Custom Tokenizer

To create an exception custom tokenizer with the Couchbase Server Web Console:

1. Go to **Search**.
2. Do one of the following:
3. Click the Search index where you want to create a custom tokenizer.
4. Click **Edit**.
5. Expand **Customize Index** **Custom Filters**.
6. Click **Add Tokenizer**.
7. In the **Name** field, enter a name for the custom tokenizer.
8. In the **Type** field, select **exception**.
9. In the **Exception Patterns** field, enter a regular expression to use to remove content from input.
10. To add the regular expression to the list of exception patterns, click **Add**.
11. (Optional) To add additional regular expressions to the list of exception patterns, repeat the previous steps.
12. In the **Tokenizer for Remaining Input** field, select a tokenizer to apply to input after removing any content that matches the regular expression.  
For more information about the available tokenizers, see [Default Tokenizers](default-tokenizers-reference.md).
13. Click **Save**.

## [](#next-steps)Next Steps

After you create a custom tokenizer, you can use it with [a custom analyzer](create-custom-analyzer.md).

To continue customizing your Search index, you can also:

* [Set the Type Identifier for a Search Index](set-type-identifier.md)
* [Create a Type Mapping](create-type-mapping.md)
* [Create a Child Field](create-child-field.md)
* [Create a Child Mapping](create-child-mapping.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Wordlist](create-custom-wordlist.md)
* [Set Search Index Advanced Settings](set-advanced-settings.md)
* [Add Synonyms to a Search Index](synonyms/synonyms-search.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).