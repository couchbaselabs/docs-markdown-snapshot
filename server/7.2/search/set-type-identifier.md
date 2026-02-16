[View original HTML](/server/7.2/search/set-type-identifier.html)

> Use a type identifier with a type mapping to add an extra filter to the documents you want to include in a Search index. 

For more information about type identifiers and type mappings, see [Customize a Search Index with the Web Console](customize-index.md#type-identifiers).

## [](#prerequisites)Prerequisites

* You’ve created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You’ve created at least one type mapping in your Search index. For more information, see [Create a Type Mapping](create-type-mapping.md).
* You’ve logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To set a type identifier for a Search index with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the index where you want to set a type identifier.
3. Click **Edit**.
4. Do one of the following:

  1. [Create a JSON Type Field Type Identifier](#json-type)
  2. [Create a Doc ID Up To Separator Type Identifier](#doc-id-sep)
  3. [Create a Doc ID with Regex Type Identifier](#doc-id-regex)

### [](#json-type)Create a JSON Type Field Type Identifier

To only add documents to your Search index that contain a specific field with a specified string value:

1. Select **JSON type field**.
2. In the **JSON Type Field** field, enter the name of the field in your documents that you want to use to filter documents in your Search index.  
For example, if your documents include a `type` field, you could enter `type` in the **JSON Type Field** field.

|  | You can’t use a field as a type identifier if the field name contains a period (.). |
|  | ----------------------------------------------------------------------------------- |
3. Under **Type Mappings**, next to the type mapping where you want to add the type identifier, click **Edit**.
4. In the **#** field, add a period (.) to the end of the current type mapping name.
5. After the period, add the exact string from the document field that you want to use as a filter.  
For example, if you wanted your Search index to only return documents that had a `type` value of `hotel`, you could enter `scope.collection.hotel` in the type mapping **#** field.
6. Click **OK**.
7. Click **Update Index**.

### [](#doc-id-sep)Create a Doc ID Up To Separator Type Identifier

To only add documents to your Search index that have IDs that match a specified prefix:

1. Select **Doc ID up to Separator**.
2. In the **Doc ID up to Separator** field, enter the ID prefix, up to the separator character, that you want to use to filter documents in your Search index.  
For example, if you know all of your document ID values are prefixed by a string and an underscore, enter `_`.
3. Under **Type Mappings**, next to the type mapping where you want to add the type identifier, click **Edit**.
4. In the **#** field, add a period (.) to the end of the current type mapping name.
5. After the period, add the exact prefix from the document’s ID value that you want to use as a filter.  
For example, if you wanted your Search index to only return documents that have an prefix of `landmark_`, you could enter `scope.collection.landmark` in the type mapping **#** field.
6. Click **OK**.
7. Click **Update Index**.

### [](#doc-id-regex)Create a Doc ID with Regex Type Identifier

To only add documents to your Search index that have IDs that match a specified [RE2](https://github.com/google/re2/wiki/Syntax) regular expression:

* Select **Doc ID with Regex**.

In the **Doc ID with Regex** field, enter the regular expression that you want to use to filter documents in your Search index.

For example, if you wanted only documents with ID values that contained 40, you could enter `[3-5]0` as your regular expression. 
* Under **Type Mappings**, next to the type mapping where you want to add the type identifier, click **Edit**.
* In the **#** field, add a period (.) to the end of the current type mapping name.
* After the period, add a match for the regular expression from the document’s ID value that you want to use as a filter.  
For example, if you wanted your Search index to only return documents with ID values that contained `_40`, you could enter `scope.collection._40` in the type mapping **#** field.
* Click **OK**.
* Click **Update Index**.

## [](#next-steps)Next Steps

After you set the type identifier for your Search index, you can continue to customize your Search index:

* [Create a Type Mapping](create-type-mapping.md)
* [Create a Child Field](create-child-field.md)
* [Create a Child Mapping](create-child-mapping.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Wordlist](create-custom-wordlist.md)
* [Set Search Index Advanced Settings](set-advanced-settings.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).