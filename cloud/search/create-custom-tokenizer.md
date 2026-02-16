[View original HTML](/cloud/search/create-custom-tokenizer.html)

> Create a custom tokenizer with the Couchbase Capella UI to change how the Search Service creates tokens for matching Search index content to a Search query. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have logged in to the Couchbase Capella UI.
* You have started to create or already created an index in [Advanced Mode Editing](create-search-indexes.md#advanced-mode).
* You have already created or started to create a [custom analyzer](create-custom-analyzer.md) in your Search index.

## [](#procedure)Procedure

To create a new custom tokenizer with the Capella UI in Advanced Mode:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Search Service.
3. Go to **Data Tools** **Search**.
4. Do one of the following:

  1. To work with an existing Search index, click the name of the index where you want to create a custom analyzer.
  2. To create a new Search index, click **Create Search Index**.
5. Make sure to select **Enable Advanced Options**.
6. Expand **Global Index Settings**.
7. Do one of the following:

  1. To create a new custom analyzer with a new tokenizer, click **Add Custom Analyzer**.
  2. To add a new custom tokenizer to use with an existing analyzer, expand the **Default Analyzer** list, and next to your custom analyzer, click **Edit**.
8. Click **Add Custom Tokenizer**.
9. In the **Tokenizer Name** field, enter a name for the tokenizer.
10. In the **Type** list, select a tokenizer type.
11. Configure your tokenizer based on your chosen tokenizer type.

You can create 2 types of custom tokenizers:

| Tokenizer Type                | Description                                                                                                                                                                         |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Regular expression](#regexp) | The tokenizer uses any input that matches the regular expression to create new tokens.                                                                                              |
| [Exception](#excep)           | The tokenizer removes any input that matches the regular expression, and creates tokens from the remaining input. You can choose another tokenizer to apply to the remaining input. |

### [](#regexp)Create a Regular Expression Tokenizer

To create a regular expression tokenizer with the Capella UI:

1. In the **Type** list, select **regexp**.
2. In the **Regular Expression** field, enter the regular expression to use to split input into tokens.  
For example, the regular expression `\b\w+\b` would create tokens based on the word boundaries and word characters found in the input.
3. Click **Add Custom Tokenizer**.

### [](#excep)Create an Exception Custom Tokenizer

To create an exception custom tokenizer with the Capella UI in Advanced Mode:

1. In the **Type** list, select **exception**.
2. In the **Regular Expressions** field, enter 1 or more regular expression to use to remove content from your input. Separate multiple regular expression patterns by entering a comma (`,`).
3. In the **Tokenizer for Remaining Input** list, select a tokenizer to apply to your input after removing any content that matches your provided **Regular Expressions**.  
For more information about the available tokenizers, see [Default Tokenizers](default-tokenizers-reference.md).
4. Click **Add Custom Tokenizer**.

## [](#next-steps)Next Steps

After you create a custom tokenizer, you can use it with [a custom analyzer](create-custom-analyzer.md).

To continue customizing your Search index, you can also:

* [Set a Document Filter](set-type-identifier.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Add Synonyms to a Search Index](synonyms/synonyms-search.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Capella UI](simple-search-ui.md).