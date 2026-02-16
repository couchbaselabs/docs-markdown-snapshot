[View original HTML](/server/7.6/search/create-search-index-alias-rest-api.html)

> Use the REST API to create a Search index alias. Use a Search index alias to run a Search query across multiple buckets, scopes, or Search indexes. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* You have created at least one Search index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md) or [Create a Search Index with the REST API and curl/HTTP](create-search-index-rest-api.md).
* Your user account has the **Search Admin** role for the bucket where you want to create the alias.
* You have installed the Couchbase command-line tool (CLI).
* You have the hostname or IP address for the node in your cluster where you’re running the Search Service. For more information about where to find the IP address for your node, see [List Cluster Nodes](../../current/manage/manage-nodes/list-cluster-nodes.md).

## [](#procedure)Procedure

To create a Search index alias with the REST API:

1. In your command-line tool, enter a `curl` command with the `XPUT` verb.
2. Set your header content to include `"Content-Type: application/json"`.
3. Enter your username, password, and the Search Service endpoint on port `8094` with the name of the index you want to create.  
If your alias’s target Search indexes are all in the same bucket and scope, use the scoped index creation endpoint:  
Scoped Index Creation Endpoint  
```console  
curl -s -XPUT -H "Content-Type: application/json" \
    -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/${BUCKET_NAME}/scope/${SCOPE_NAME}/index/${INDEX_NAME}
    -d \  
```  
If your target Search indexes are in different buckets or scopes, use the global index creation endpoint:  
Global Index Creation Endpoint  
```console  
curl -s -XPUT -H "Content-Type: application/json" \
    -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/index/${INDEX_NAME}  
    -d \  
```  
To use SSL, use the `https` protocol in the Search Service endpoint URL and port `18094`.

|  | Your alias name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_). For Couchbase Server version 7.6 and later, if you’re using the scoped endpoint, your alias name must be unique inside your selected bucket and scope. You cannot have 2 aliases with the same name globally or inside the same bucket and scope. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
4. Enter the JSON payload for your Search index alias. Your Search index alias only requires the properties from [the start of a Search index JSON payload](search-index-params.md#initial), except where otherwise noted.

## [](#example-create-an-alias-with-targets-in-the-same-bucket-and-scope)Example: Create an Alias With Targets in the Same Bucket and Scope

In the following example, the JSON payload creates an index alias named `travel-sample-alias`, which contains the `landmark-content`, `hotel-reviews`, and `routes` Search indexes:

```console
curl -s -XPUT -H "Content-Type: application/json" \
  -u ${CB_USERNAME}:${CB_PASSWORD} http://localhost:8094/api/bucket/travel-sample/scope/inventory/index/travel-sample-alias
  -d \
  '{
    "name": "travel-sample-alias",
    "type": "fulltext-alias",
    "params": {
      "targets": {
        "travel-sample.inventory.landmark-content": {},
        "travel-sample.inventory.hotel-reviews": {},
        "travel-sample.inventory.routes": {}
      }
    },
    "sourceType": "nil",
    "sourceName": "",
    "sourceUUID": "",
    "sourceParams": null,
    "planParams": {},
    "uuid": ""
  }'
```

All the Search indexes in the `targets` object are in the same bucket and scope, so the REST API call uses the scoped endpoint to create a scoped alias.

If the REST API call is successful, the Search Service returns a `200 OK` and the following JSON response:

```json
{
    "status": "ok",
    "name": "travel-sample.inventory.travel-sample-alias",
    "uuid": "7e569bdb5d3a2a83"
}
```

The `"uuid"` is randomly generated for each Search index alias you create. Your own UUID might not match the value shown in the example.

## [](#example-create-an-alias-with-targets-in-different-buckets)Example: Create an Alias With Targets in Different Buckets

In the following example, the JSON payload creates an index alias named `travel-color-alias`, which contains the `landmark-content` and `color-index` Search indexes, which are in different buckets on the cluster:

```console
curl -s -XPUT -H "Content-Type: application/json" \
  -u ${CB_USERNAME}:${CB_PASSWORD} http://localhost:8094/api/index/travel-color-alias
  -d \
  '{
    "name": "travel-sample-alias",
    "type": "fulltext-alias",
    "params": {
      "targets": {
        "travel-sample.inventory.landmark-content": {},
        "vector-sample.color.color-index": {}
      }
    },
    "sourceType": "nil",
    "sourceName": "",
    "sourceUUID": "",
    "sourceParams": null,
    "planParams": {},
    "uuid": ""
  }'
```

The REST API call uses the global endpoint to create a global alias.

If the REST API call is successful, the Search Service returns a `200 OK` and the following JSON response:

```json
{
    "status": "ok",
    "name": "travel-color-alias",
    "uuid": "d630f5570437ff92"
}
```

The `"uuid"` is randomly generated for each Search index alias you create. Your own UUID might not match the value shown in the example.

## [](#next-steps)Next Steps

After you create a Search index alias, you can [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md) to test your alias and Search indexes.

If you want to edit your alias with another REST API call, include the [uuid](search-index-params.md#uuid) parameter with your alias UUID.

You can get the UUID from the response to your first call. You can also view the UUID from the Couchbase Server Web Console by selecting the alias, and clicking **Edit Index**. The UUID displays in the Index Definition Preview on the Edit Index page.

You can also use the [Index Definition](../fts-rest-indexing/index.md) endpoints provided by the Search REST API.