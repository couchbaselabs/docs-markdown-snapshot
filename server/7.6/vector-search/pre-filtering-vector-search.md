[View original HTML](/server/7.6/vector-search/pre-filtering-vector-search.html)

> You can specify filters as part of a Vector Search query object to restrict the documents searched in a Search index. 

## [](#about-pre-filtering)About Pre-filtering

The Search Service supports pre-filtering on Vector Search queries. Pre-filtering allows you to execute vector searches over a subset of the vector index, via the means of a filter request that qualifies the subset.

|  | You cannot use Vector Search on Windows platforms. You can use Vector Search on Linux from Couchbase Server version 7.6.0 and MacOS from version 7.6.2. You can still use other features of the [Search Service](../search/search.md). |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../../current/manage/manage-buckets/create-bucket.md).
* Your user account has the **Search Admin** or **Search Reader** role.
* You installed the Couchbase command-line tool (CLI).
* You have the hostname or IP address for the node in your cluster where you’re running the Search Service. For more information about where to find the IP address for your node, see [List Cluster Nodes](../../current/manage/manage-nodes/list-cluster-nodes.md).
* You have created a Vector Search index.  
For more information about how to create a Vector Search index, see [Create a Vector Search Index with the Server Web Console](create-vector-search-index-ui.md) or [Create a Vector Search Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md).

|  | You can download a sample dataset to use with the procedure or examples on this page: [Download color\_data\_2vectors.zip](https://cbc-remote-execution-examples-prod.s3.amazonaws.com/color%5Fdata%5F2vectors.zip) To get the best results with using the sample data with the examples in this documentation, [import the sample files](../guides/import.md) from the dataset into your database with the following settings: Use a bucket called vector-sample. Use a scope called color. Use a collection called rgb for rgb.json. To set your document keys, use the value of the id field from each JSON document. For the best results, consider using the sample Vector Search index from [Create a Vector Search Index with the Server Web Console](create-vector-search-index-ui.md#example) or [Create a Vector Search Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md#example). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#procedure)Procedure

To add pre-filtering to a Vector Search with the REST API:

1. In your command-line tool, enter a `curl` command with the `XPOST` verb.
2. Set your header content to include `"Content-Type: application/json"`.
3. Add your `username`, `password`, and the Search Service endpoint on port `8094`.
4. Add the `index name` you want to query to the endpoint.  
```console  
curl -XPOST -H "Content-Type: application/json" \
  -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/vector-sample/scope/color/index/{INDEX_NAME}/query \
-d \  
```
5. Enter a search query that includes a `filter` object with your `knn` object.  
For more information about the `filter` object, see [filter](../search/search-request-params.md#filter).

### [](#example-pre-filter-a-vector-search-query-for-the-color-navy)Example: Pre-Filter A Vector Search Query For The Color "Navy"

For example, the following Vector Search query tries to find matches to a color with an RGB value of `[176, 0, 176]` with a minimum brightness of `70` and a maximum of `80`. A pre-filter on the query will narrow the documents searched inside the Vector Search index to documents that have a `color` field value that closely matches `navy`:

```console
curl -XPOST -H "Content-Type: application/json" \
  -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/vector-sample/scope/color/index/color-index/query \
-d '{
      "fields": ["*"],
      "query": {
        "min": 70,
        "max": 80,
        "inclusive_min": false,
        "inclusive_max": true,
        "field": "brightness"
      },
      "knn": [
        {
          "k": 10,
          "field": "colorvect_l2",
          "vector": [ 176, 0, 176 ],
          "filter": {
            "field":  "color",
            "match": "navy"
          }
        }
      ]
    }'
```