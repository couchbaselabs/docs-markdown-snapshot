[View original HTML](/server/7.2/search/create-search-index-rest-api.html)

> You can create a Search index with the Search Service API. 

You must create a Search index before you can [run a search](simple-search-rest-api.md) with the Search Service.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your database.
* You have a bucket with scopes and collections in your database.
* Your user account has the **Search Admin** role for the bucket where you want to create the index.
* You’ve installed the Couchbase command-line tool (CLI).
* You have the hostname or IP address for your database.

## [](#procedure)Procedure

To create a Search index with the REST API:

1. In your command-line tool, enter a `curl` command with the `XPUT` verb.
2. Set your header content to include `Content-Type: application/json`.
3. Enter your username, password, and the Search Service endpoint on port `8094` with the name of the index you want to create:  
```console  
curl -s -XPUT -H "Content-Type: application/json" \
    -u $CB_USERNAME:$CB_PASSWORD http://$CB_HOSTNAME:8094/api/index/landmark-content-index  
    -d \  
```
4. Enter the JSON payload for the settings you want in your index.  
Don’t include the [uuid](search-index-params.md#uuid) or [sourceUUID](search-index-params.md#sourceuuid) parameters.

|  | If you remove the [uuid](search-index-params.md#uuid) and [sourceUUID](search-index-params.md#sourceuuid) parameters, you can copy the Search index definition JSON payload from the Couchbase Server Web Console to use in your REST API call. For more information about how to create an index with the UI, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  
In the following example, the JSON payload creates a simple index named `landmark-content-index` on the `travel-sample` bucket. It creates a type mapping for the `inventory.landmark` collection, with a child field, `content`:  
```console  
curl -s -XPUT -H "Content-Type: application/json" \
  -u $CB_USERNAME:$CB_PASSWORD http://$CB_HOSTNAME:8094/api/index/landmark-content-index  
  -d \  
  '{  
      "type": "fulltext-index",  
      "name": "landmark-content-index",  
      "sourceType": "gocbcore",  
      "sourceName": "travel-sample",  
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
            "inventory.landmark": {  
              "dynamic": false,  
              "enabled": true,  
              "properties": {  
                "content": {  
                  "dynamic": false,  
                  "enabled": true,  
                  "fields": [  
                    {  
                      "docvalues": true,  
                      "include_in_all": true,  
                      "include_term_vectors": true,  
                      "index": true,  
                      "name": "content",  
                      "store": true,  
                      "type": "text"  
                    }  
                  ]  
                }  
              }  
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
For more information about the available JSON properties for a Search index, see [Search Index JSON Properties](search-index-params.md).

## [](#next-steps)Next Steps

After you create a Search index, you can [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md) to test your Search index.

If you want to edit your index with another REST API call, include the [uuid](search-index-params.md#uuid) parameter with the UUID the Search Service assigned to your Search index.

You can also [Run A Simple Search with the Web Console](simple-search-ui.md) or with one of the Couchbase SDKs:

[.NET](../../../dotnet-sdk/current/howtos/full-text-searching-with-sdk.md)| [Go](../../../go-sdk/current/howtos/full-text-searching-with-sdk.md)| [Java](../../../java-sdk/current/howtos/full-text-searching-with-sdk.md)| [Kotlin](../../../kotlin-sdk/current/howtos/full-text-search.md)| [Node.js](../../../nodejs-sdk/current/howtos/full-text-searching-with-sdk.md)| [PHP](../../../php-sdk/current/howtos/full-text-searching-with-sdk.md)| [Python](../../../python-sdk/current/howtos/full-text-searching-with-sdk.md)| [Ruby](../../../ruby-sdk/current/howtos/full-text-searching-with-sdk.md)| [Scala](../../../scala-sdk/current/howtos/full-text-searching-with-sdk.md)