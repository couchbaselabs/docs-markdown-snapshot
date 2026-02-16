[View original HTML](/cloud/search/create-type-mapping.html)

> Create a type mapping with the Couchbase Capella UI to control what documents are included or excluded from a Search index. 

You can create [static type mappings](about-mappings.md#static), which include only specific fields from your documents, or [dynamic type mappings](about-mappings.md#dynamic), which include all available fields. For more information about type mappings and mappings in the Search Service, see [About Mapping Collections, Objects and Fields](about-mappings.md).

Some mappings are only available in Advanced Mode.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have a bucket with scopes and collections in your operational cluster. For more information, see [Manage Buckets](../clusters/data-service/manage-buckets.md).
* You have created a basic Search index with the Capella UI. For more information, see [Create a Search Index with the Capella UI](create-search-index-ui.md).
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

To use the Capella UI to create a new type mapping or mapping on a Search index:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Search Service.
3. Go to **Data Tools** **Search**.
4. Click the name of the index where you want to create a new type mapping.
5. If you have not already, create at least 1 [collection type mapping](#collection).
6. Do one of the following:

  1. To index all documents from an additional collection, create a [collection type mapping](#collection).
  2. (Advanced Mode Only) To index Extended Attributes (XATTRs) data from your documents, create an [XATTRs mapping](#xattrs).
  3. To index an entire JSON object from your document schema, create a [JSON object mapping](#object).
  4. To index a single document field from your document schema, create a [field mapping](#field).
  5. (Advanced Mode Only) Index [a field or object that does not yet exist in your document schema](#future).
7. (Optional) To remove all documents that match a type mapping or mapping from your Search index, [turn off the mapping](#disable-mapping).
8. Click **Update Index**.

### [](#collection)Add a Collection Type Mapping

Add a [collection type mapping](about-mappings.md#collections) to index all documents from a specific collection in your chosen bucket and scope.

To add an entire collection as a new type mapping:

1. In the **Choose a Collection or Document Field** panel, click a collection name.
2. [Configure your type mapping options](type-mapping-options.md#collection).
3. Click **Add To Index**.

#### [](#filter-mapping)Add a Document Filter to a Collection Type Mapping

You can add a [document filter](customize-index.md#type-identifiers) to any collection type mapping on your Search index. A document filter adds or removes documents from a collection type mapping in your Search index.

To add a document filter to a mapping, see [Set a Document Filter](set-type-identifier.md).

### [](#xattrs)Add an XATTRs Mapping

|  | XATTRs mappings can only be created with **Advanced Mode**. |
|  | ----------------------------------------------------------- |

Add an [XATTRs mapping](about-mappings.md#xattrs) to index document metadata from a specific collection.

To add Extended Attributes (XATTRs) document metadata as a new mapping:

1. If you have not already, [create a collection type mapping](#collection) for the collection that has documents with XATTRs data.
2. Under your **Configured Type Mappings**, next to your collection type mapping, click **Add XATTRs**.
3. [Configure your mapping options](type-mapping-options.md#xattrs).
4. Click **Add To Index**.

### [](#object)Add a JSON Object Mapping

Add a [JSON object mapping](about-mappings.md#objects) to index a JSON object from your document schema. You can choose to index the fields inside the JSON object as [field mappings](#field), or keep your JSON object mapping as a [dynamic mapping](about-mappings.md#dynamic).

To add an entire JSON object from your documents as a new mapping:

1. In the **Choose a Collection or Document Field** panel, expand a collection.
2. Inside your displayed document schema, click the name of a JSON object in your documents.
3. [Configure your mapping options](type-mapping-options.md#object).
4. Click **Add To Index**.

### [](#field)Add a Child Field Mapping

Add a [child field mapping](about-mappings.md#fields) to index a single document field from your document schema. Adding document field mappings turns any parent mappings into [static type mappings](about-mappings.md#static).

To add only a single field from your documents as a new mapping:

1. In the **Choose a Collection or Document Field** panel, expand a collection.
2. Inside your displayed document schema, click the name of a document field.
3. [configure your type mapping options](type-mapping-options.md#field).
4. Click **Add To Index**.

### [](#future)Add a Mapping or Type Mapping for a Future Object or Field

|  | Mappings for objects that do not yet exist in your documents can only be created in **Advanced Mode**. |
|  | ------------------------------------------------------------------------------------------------------ |

You can choose to add a mapping or type mapping for a JSON object or field that does not yet exist in your document schema. If you know the name of the object or field, the Search Service can search these fields after they have been added to the documents in your Search index.

To add a mapping or type mapping for a future object or field:

1. Select **Enable Advanced Options**.
2. [Create a collection type mapping](#collection) for the collection that will hold the documents with your future field.
3. Under your **Configured Type Mappings**, next to your collection type mapping, do one of the following:

  1. To create a new JSON Object, click **Add Object**.
  2. To create a new field, click **Add Field**.
4. In the **Property Name** field, enter the name of the JSON object or field.
5. Configure your [object mapping](type-mapping-options.md#object) or [field type mapping](type-mapping-options.md#field) options.
6. Click **Add To Index**.

### [](#disable-mapping)Turn a Mapping On or Off

You can turn off a type mapping or mapping to remove any documents that match that type mapping from your Search index. These documents will not appear in search results when you run a query on the index. Turning off mappings is useful for troubleshooting Search index configurations, without losing configuration settings.

To turn off a mapping or type mapping in your Search index:

1. Under **Configured Type Mappings**, find the type mapping or mapping you want to turn off.
2. Clear the checkbox for the type mapping or mapping.

You can select a type mapping or mapping again at any time to add it back to your Search index and search results.

## [](#next-steps)Next Steps

Your Search index will contain any documents, objects, or fields that you specify in your type mappings and mappings.

You can keep adding additional features to your Search index to improve performance and search results. For more information, see [Search Index Features](customize-index.md).

For more information about how to run a search, see [Run A Simple Search with the Capella UI](simple-search-ui.md).