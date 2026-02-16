[View original HTML](/server/7.2/search/set-advanced-settings.html)

> Configure advanced settings with the Couchbase Server Web Console for a Search index to improve an index’s search results and performance. 

## [](#prerequisites)Prerequisites

* You’ve deployed the Search Service on a node in your database.
* You have a bucket with scopes and collections in your database.
* Your user account has the **Search Admin** role for the bucket where you want to edit an index.
* You’ve created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You’ve logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To set advanced settings for a Search index with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the index that you want to edit.
3. Click **Edit**.
4. Expand **Customize Index** **Advanced**.
5. Configure any of the following advanced settings for your index:

| Option                       | Description                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Default Type                 | Change the default type assigned to documents in the index. The default value is \_default.                                                                                                                                                                                                                                                       |
| Default Analyzer             | Change the default analyzer assigned to type mappings in the index. For more information about the available default analyzers, see [Default Analyzers](default-analyzers-reference.md). For more information about how to create your own custom analyzer, see [Create a Custom Analyzer](create-custom-analyzer.md).                            |
| Default Date/Time Parser     | Change the default date/time parser used for date data.                                                                                                                                                                                                                                                                                           |
| Default Field                | When you [create a child field](create-child-field.md) in a type mapping, you can choose to include that field in an \_all field. You can add fields to the \_all field to search their contents without specifying their field name in your search query. Enter a value in the **Default Field** field to change the name of this default field. |
| Store Dynamic Fields         | Select **Store Dynamic Fields** to include field values in search results from a [dynamic type mapping](customize-index.md#type-mappings) in the index.                                                                                                                                                                                           |
| Index Dynamic Fields         | Select **Index Dynamic Fields** to include fields from a [dynamic type mapping](customize-index.md#type-mappings) in the index.                                                                                                                                                                                                                   |
| DocValues for Dynamic Fields | Select **DocValues for Dynamic Fields** to include the values of each field from a [dynamic type mapping](customize-index.md#type-mappings) in the index.                                                                                                                                                                                         |
| Index Replicas               | Set the number of replicas that the Search Service creates for the index. For more information about replication and the Search Service, see [High Availability for Search](../fts/fts-high-availability-for-search.md).                                                                                                                          |
| Index Type                   | This setting is included for compatibility only. For new indexes, this setting is always **Version 6.0 (Scorch)**.                                                                                                                                                                                                                                |
| Index Partitions             | Enter a number greater than one to divide the index into partitions across multiple nodes running the Search Service.                                                                                                                                                                                                                             |
6. Click **Update Index**.

## [](#next-steps)Next Steps

After you change the settings for your Search index, you can continue to customize your Search index:

* [Set the Type Identifier for a Search Index](set-type-identifier.md)
* [Create a Type Mapping](create-type-mapping.md)
* [Create a Child Field](create-child-field.md)
* [Create a Child Mapping](create-child-mapping.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Wordlist](create-custom-wordlist.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).