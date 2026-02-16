[View original HTML](/server/7.2/fts/fts-creating-index-with-rest-api.html)

> The REST API can be used to instantly create indexes or query indexes from JSON payloads. 

## [](#prerequisites)Prerequisites

The user interface for Full Text Search is provided by the Couchbase Web Console.

* Ensure that Couchbase Server has the Search service appropriately enabled. The service must be enabled for a given node as part of that node’s initial configuration. Refer to Create a Cluster for information.
* You must have permission to log into the console, load sample data, create indexes, create search indexes, and perform searches. For information on Role-Based Access Control, see [Authorization](../learn/security/authorization-overview.md).
* The example(s) provided assume that you have can load or have loaded the `travel-sample` dataset. You will perform your Search operations on the data under this bucket. For instructions on how to load this sample dataset, see [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).
* The Couchbase Web Console by accessing `http://localhost:8091` or if remote `http://${CB_HOSTNAME}:8091` where **CB\_HOSTNAME** is an environment variable set to a FQDN or an IP address for a node on your Couchbase cluster.

## [](#quickstart-via-the-rest-api)Quickstart via the REST API

To quickly become familiarized with the Search service, try one of the step by step index creation (and query) examples against the `travel-sample` sample dataset:

* Collections

* Creating a **One Field Index** [via the REST API](fts-creating-index-from-REST-onefield.md) (or [via the UI](fts-creating-index-from-UI-classic-editor-onefield.md)), followed by a sample Search query.
* Creating a **Dynamic Index** [via the REST API](fts-creating-index-from-REST-dynamic.md) (or [via the UI](fts-creating-index-from-UI-classic-editor-dynamic.md)), followed by a sample Search query.
* Creating a **Geopoint Index** [via the REST API](fts-creating-index-from-REST-geopoint.md) (or [via the UI](fts-creating-index-from-UI-classic-editor-geopoint.md)), followed by a sample Search query.

Bucket Compatibility

Creating a **Legacy Index** [via the REST API](fts-creating-index-from-REST-legacy.md) (or [via the UI](fts-creating-index-from-UI-classic-editor-legacy.md)), followed by a sample Search query.

The above Legacy Index is used for compatibility after an upgrade from buckets to collections uses the old bucket style "**default \_mapping** which only works on the _default scope and \_default collection where buckets are upgraded into. The preferred method as of version 7.0 is shown in [Creating a Dynamic Index](fts-creating-index-from-UI-classic-editor-dynamic.md) above._ 

For a more detailed explanation of the available index creation, including index creation by means of the Couchbase REST API, refer to [Creating Search Indexes](fts-creating-indexes.md).

To install the `travel-sample` sample dataset, refer to [Install Sample Buckets with the UI](../manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).

## [](#rest-api-index-creation-details)REST API Index Creation Details

The REST API can be used to create indexes. Each call requires the following:

* An appropriate username and password.
* Use of the verb `PUT`.
* An endpoint referring to the Full Text Search service, on port `8094`; and including the appropriate endpoint for index creation as defined by the [Full Text Search REST API](../rest-api/rest-fts.md), including the name of the new index.
* Headers to specify settings for `cache-control` (`no-cache`) and `application-type` (`application/json`).
* A body containing the JSON document that defines the index to be created. This must include the name of the bucket on which the index is to be created.

The simplest way to create the appropriate JSON index-definition for the body is to create an index by means of the Couchbase Web Console, make a copy of the JSON index-definition produced (by accessing the [Using the Index Definition Preview](fts-creating-index-from-UI-classic-editor.md#using-the-index-definition-preview), explained above), modify the index-definition as appropriate, and finally, add the index-definition to the other, preceding elements required for the call.

Note, however, that this requires modification of the `uuid` field; since the re-specifying of an existing field-value is interpreted as an attempted _update_, to an existing index. Therefore, if the `uuid` field for an existing index appears in the Index Definition Preview as `"uuid": "3402702ff3c862c0"`, it should be edited to appear `"uuid": ""`. A new ID will be allocated to the new index, and this ID will appear in the Index Definition Preview for the new index.

Note also that a similar condition applies to the `sourceUUID` field, which refers to the targeted bucket: if a new index is being created for the same bucket that was referred to in the index-object copied from the UI, the field-value can remain the same. However, if a different bucket is now to be targeted, the field should be edited to appear `"sourceUUID": ""`

When specifying the endpoint for the index you are creating, make sure the path-element that concludes the endpoint is the same as that specified in the `name` field (which is the first field in the object).

The following `curl` example demonstrates the creation of an index named `demoIndex`, on the `inventory` scope and `airline` collection, within the `travel-sample` bucket. It assumes that Couchbase Server is running on `localhost`, and that the required username and password are `Administrator` and `password.`

**Example**

```bourne
curl -XPUT -H "Content-Type: application/json" \
-u <username>:<password> http://localhost:8094/api/index/demoIndex -d \
'{
  "type": "fulltext-index",
  "name": "demoIndex",
  "uuid": "4b70593a69cfcd79",
  "sourceType": "gocbcore",
  "sourceName": "travel-sample",
  "sourceUUID": "fc9b8eec20f8f7713ad14498064f50aa",
  "planParams": {
    "maxPartitionsPerPIndex": 1024,
    "indexPartitions": 1
  },
  "params": {
    "doc_config": {
      "docid_prefix_delim": "",
      "docid_regexp": "",
      "mode": "scope.collection.type_field",
      "type_field": "type"
    },
    "mapping": {
      "analysis": {},
      "default_analyzer": "standard",
      "default_datetime_parser": "dateTimeOptional",
      "default_field": "_all",
      "default_mapping": {
        "dynamic": true,
        "enabled": false
      },
      "default_type": "_default",
      "docvalues_dynamic": false,
      "index_dynamic": true,
      "store_dynamic": false,
      "type_field": "_type",
      "types": {
        "inventory.airline": {
          "dynamic": true,
          "enabled": true
        }
      }
    },
    "store": {
      "indexType": "scorch",
      "segmentVersion": 15
    }
  },
  "sourceParams": {}
}'
```

If the call is successful, the following object is returned:

```bourne
{"status":"ok"}
```

The newly created index can then be inspected in the Couchbase Web Console.

## [](#index-update-with-rest-api)Index Update with REST API

Specifying the "uuid" parameter in the index definition is required for the index creation to be treated as a valid update.

|  | This uuid in the JSON body of a valid index update request has to match that of the existing index definition. Upon successful creation/update of an index, the uuid will be re-initialized. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |