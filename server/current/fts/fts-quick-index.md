[View original HTML](/server/current/fts/fts-quick-index.html)

To create a quick index, left-click on the **QUICK INDEX** button, towards the right-hand side:

The QUICK INDEX screen appears:

![fts quick index screen](_images/fts-quick-index-screen.png) 

To define a basic index on which Full Text Search can be performed, begin by entering a unique name for the index into the Index Name field, at the upper-left: for example, travel-sample-index. (Note that only alphanumeric characters, hyphens, and underscores are allowed for index names. Note also that the first character of the name must be an alphabetic character.) Then, use the pull-down menu provided for the Keyspace field, at the upper-right, to specify as follows:

bucket: `travel-sample`

scope: `inventory`

collection: `hotel`

![fts quick index name and bucket](_images/fts-quick-index-name-and-bucket.png) 

The user can continue to randomly pick documents until they find a document of their intended type/schema. It is also possible to have multi-schema documents within a collection.

![fts quick index json](_images/fts-quick-index-json.png) 

Select the required field from the document, which is needed to be mapped to this index. Once the field is selected, the configuration panel is displayed at the right.

![fts quick index json configuration](_images/fts-quick-index-json-configuration.png) 

Select the related type of the field from the **Type** dropdown.

Select **Index this field as an identifier** to index the identifier values precisely without any transformation; for this case, language selection is disabled.

After that, select the required language for the chosen field.

Additionally, select from the following configuration options corresponding to the selected language:

* **Include in search results**: Select this option to include the field in the search result.
* **Support highlighting**: Select this option to highlight the matched field. For this option, you must select the **Include in search result** option.
* **Support phrase matching**: Select this option to match the phrases in the index.
* **Support sorting and faceting**: Select this option to allow sorting and faceting the index.

|  | Selecting configuration options requires additional storage and makes the index size larger. |
|  | -------------------------------------------------------------------------------------------- |

## [](#document-refreshreselection-option)Document Refresh/Reselection option

The 'Refresh' option will randomly select a document from the given Keyspace (bucket.scope.collection).

![fts quick index refresh](_images/fts-quick-index-refresh.png) 

Include In search results, Support phrase matching, and Support sorting and faceting. Searchable As field allows you to modify searchable input for the selected field.

![fts quick index searchable input](_images/fts-quick-index-searchable-input.png) 

Once the configuration is completed for the selected fields, click Add. Mapped fields will display the updated columns.

![fts quick index json mapping](_images/fts-quick-index-json-mapping.png) 

This is all you need to specify in order to create a basic index for test and development. No further configuration is required.

Note, however, that such default indexing is not recommended for production environments since it creates indexes that may be unnecessarily large, and therefore insufficiently performant. To review the wide range of available options for creating indexes appropriate for production environments, see Creating Indexes.

To save your index,

Left-click on the **Create Index** button near the bottom of the screen:

At this point, you are returned to the Full Text Search screen. A row now appears, in the Full Text Indexes panel, for the quick index you have created. When left-clicked on, the row opens as follows:

![fts new quick index progress](_images/fts-new-quick-index-progress.png) 

|  | The percentage figure: this appears under the indexing progress column, and is incremented in correspondence with the build-progress of the index. When 100% is reached, the index build is said to be complete. Search queries will, however, be allowed as soon as the index is created, meaning partial results can be expected until the index build is complete. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Once the new index has been built, it supports Full Text Searches performed by all available means: the Console UI, the Couchbase REST API, and the Couchbase SDK.

In the event where one or more of the nodes in the cluster running data service go down and/or are failed over, indexing progress may show a value > 100%.