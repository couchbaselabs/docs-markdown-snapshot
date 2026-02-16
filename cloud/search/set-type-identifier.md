[View original HTML](/cloud/search/set-type-identifier.html)

> Use a document filter with a type mapping to add an extra filter to the documents you want to include in a Search index. 

For example, if you added a filter to your type mapping that checked if the value of a field was `true`, only documents with the value `true` for that field would be included in your Search index under that type mapping. Based on your settings, [child fields](create-type-mapping.md#field) or [child mappings](create-type-mapping.md#object) that you define for documents that pass the filter on this type mapping will be returned in search results.

You can filter based on the value of a field, or part of the value of your document IDs.

As of Couchbase Server version 8.0, you can filter documents with custom filters based on the value of:

* [A boolean field](search-index-params.md#boolean%5Ffilter).
* [A date field, within a specific range](search-index-params.md#date%5Frange%5Ffilter).
* [A numeric field, within a specific range](search-index-params.md#numeric%5Frange%5Ffilter).
* [A term in a text field](search-index-params.md#term%5Ffilter).
* A [conjunct](search-index-params.md#conjunct%5Ffilter) or [disjunct](search-index-params.md#disjunct%5Ffilter) object that combines 2 or more of the available filters. You can add up to a maximum of 100 custom document filters on a single Search index.

For more information about document filters and type mappings, see [Search Index Features](customize-index.md#type-identifiers).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have a bucket with scopes and collections in your operational cluster. For more information, see [Manage Buckets](../clusters/data-service/manage-buckets.md).
* You have started to create or already created an index in [Advanced Mode Editing](create-search-indexes.md#advanced-mode).
* You have created at least 1 type mapping in your Search index. For more information, see [Create a New Mapping or Type Mapping](create-type-mapping.md).
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

To set a document filter for a Search index with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Search Service.
3. Go to **Data Tools** **Search**.
4. Do 1 of the following:

  1. To work with an existing Search index, click the name of the index where you want to create a document filter.
  2. To create a new Search index, click **Create Search Index**.
5. Make sure to select **Enable Advanced Options**.
6. Expand **Global Index Settings**.
7. Do 1 of the following:

  1. [Create a JSON Type Field Document Filter](#json-type)
  2. [Create a Doc ID Up To Separator Document Filter](#doc-id-sep)
  3. [Create a Doc ID with Regex Document Filter](#doc-id-regex)
  4. [Create a Custom Document Filter](#custom)

|  | You cannot use custom document filters with another type of type identifier on your Search index. If you select an option other than **Custom** after you have defined custom document filters, you’ll lose any defined custom filters on your Search index. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#json-type)Create a JSON Type Field Document Filter

To only add documents to your Search index that contain a specific field with a specified string value:

1. Under **Choose Document Filter**, click **JSON Type Field**
2. In the **JSON Type Field** field, enter the name of the field in your documents that you want to use to filter documents in your Search index.  
For example, if your documents include a `type` field, you could enter `type` in the **JSON Type Field** field.

|  | You cannot use a field as a document filter if the field name contains a period (.). |
|  | ------------------------------------------------------------------------------------ |
3. Under **Type Mappings**, next to the type mapping where you want to add the document filter, click **Edit**.
4. In the **Enter Document Filter** field, enter the exact string from the document field that you want to use as a filter.  
For example, if you wanted your type mapping to only include documents that had a value of `hotel` in the `type` field, you could enter `hotel` in the filter field.
5. Click **Submit**.
6. Click **Update Index**.

### [](#doc-id-sep)Create a Doc ID Up To Separator Document Filter

To only add documents to your Search index that have IDs that match a specified prefix:

1. Under **Choose Document Filter**, click **Doc ID up to Separator**.
2. In the **Doc ID up to Separator** field, enter the separator character from the ID prefix in your document ID values.  
For example, if you know all of your document ID values are prefixed by a string and an underscore (\_), enter `_`.
3. Under **Type Mappings**, next to the type mapping where you want to add the document filter, click **Edit**.
4. In the **Enter Document Filter** field, enter the exact prefix from the document’s ID value that you want to use as a filter.  
For example, if you wanted your type mapping to only include documents that have an prefix of `landmark_` in their ID values, you could enter `landmark` in the filter field.
5. Click **Submit**.
6. Click **Update Index**.

### [](#doc-id-regex)Create a Doc ID with Regex Document Filter

To only add documents to your Search index that have IDs that match a specified [RE2](https://github.com/google/re2/wiki/Syntax) regular expression:

1. Under **Choose Document Filter**, click **Doc ID with Regex**.
2. In the **Doc ID with Regex** field, enter the regular expression that you want to use to filter documents in your Search index.  
For example, if you wanted documents with ID values that contained `_40`, you could enter `_[3-5]0` as your regular expression.
3. Under **Type Mappings**, next to the type mapping where you want to add the document filter, click **Edit**.
4. In the **Enter Document Filter** field, enter a match for the regular expression from the document’s ID value that you want to use as a filter.  
For example, if you wanted your type mapping to only include documents with ID values that contained `_40`, you could enter `_40` in the filter field.
5. Click **Submit**.
6. Click **Update Index**.

### [](#custom)Create a Custom Document Filter

Couchbase Server 8.0

To create a new custom document filter on a Search index with the Couchbase Capella UI:

1. Under **Choose Document Filter**, click **Custom**.
2. Click **Add Document Filter**.
3. In the **Label** field, enter a name for your new document filter.
4. In the **Filter** code editor, enter a JSON object to define your document filter.  
For more information about the properties for each document filter type, see:

  * [Boolean Document Filters](search-index-params.md#boolean%5Ffilter)
  * [Date Range Document Filters](search-index-params.md#date%5Frange%5Ffilter)
  * [Numeric Range Document Filters](search-index-params.md#numeric%5Frange%5Ffilter)
  * [Term Document Filters](search-index-params.md#term%5Ffilter)
  * [Conjunct Document Filters](search-index-params.md#conjunct%5Ffilter)
  * [Disjunct Document Filters](search-index-params.md#disjunct%5Ffilter)

|  | Do not add the name of your document filter to your filter definition when defining a custom document filter through the Capella UI. Define the document filter as an unnamed object with the specific properties you need for your document filter type. You can also click a **Preset Example** to automatically add the necessary fields for each filter type to your editor. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
5. Click **Save**.
6. Under **Type Mappings**, next to the type mapping where you want to add the document filter, click **Edit**.
7. In the **Select Document Filter** list, select the name of the custom document filter that you want to use to filter documents on this type mapping.
8. Click **Submit**.
9. Click **Update Index**.

## [](#next-steps)Next Steps

After you set the document filter for your Search index, you can continue to customize your Search index:

* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Add Synonyms to a Search Index](synonyms/synonyms-search.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Capella UI](simple-search-ui.md).