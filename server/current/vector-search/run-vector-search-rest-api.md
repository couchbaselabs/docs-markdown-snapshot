[View original HTML](/server/current/vector-search/run-vector-search-rest-api.html)

> You can use the REST API and a curl command to run a search against a Search Vector Index and return similar vectors. 

For more information about how the Search Service scores documents in search results, see [Scoring for Search Queries](#run-searches.adoc#scoring).

|  | You cannot use Vector Search on Windows platforms. You can use Vector Search on Linux from Couchbase Server version 7.6.0 and MacOS from version 7.6.2. You can still use other features of the [Search Service](../search/search.md). |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
* Your user account has the **Search Admin** or **Search Reader** role.
* You installed the Couchbase command-line tool (CLI).
* You have the hostname or IP address for the node in your cluster where you’re running the Search Service. For more information about where to find the IP address for your node, see [List Cluster Nodes](../manage/manage-nodes/list-cluster-nodes.md).
* You have created a Search Vector Index.  
For more information about how to create a Search Vector Index, see [Create a Search Vector Index with the Server Web Console](create-vector-search-index-ui.md) or [Create a Search Vector Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md).

|  | You can download a sample dataset to use with the procedure or examples on this page: [Download color\_data\_2vectors.zip](https://cbc-remote-execution-examples-prod.s3.amazonaws.com/color%5Fdata%5F2vectors.zip) To get the best results with using the sample data with the examples in this documentation, [import the sample files](../guides/load.md) from the dataset into your database with the following settings: Use a bucket called vector-sample. Use a scope called color. Use a collection called rgb for rgb.json. To set your document keys, use the value of the id field from each JSON document. For the best results, consider using the sample Search Vector Index from [Create a Search Vector Index with the Server Web Console](create-vector-search-index-ui.md#example) or [Create a Search Vector Index with the REST API and curl/HTTP](create-vector-search-index-rest-api.md#example). |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#procedure)Procedure

To run a Vector search with the REST API:

1. In your command-line tool, enter a `curl` command with the `XPOST` verb.
2. Set your header content to include `"Content-Type: application/json"`.
3. Enter your username, password, and the Search Service endpoint on port `8094` with the name of the Search Vector Index you want to query:  
```console  
curl -s -XPUT -H "Content-Type: application/json" \
-u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/${BUCKET_NAME}/scope/${SCOPE_NAME}/index/${INDEX_NAME}/query -d \  
```  
To use SSL, use the `https` protocol in the Search Service endpoint URL and port `18094`.
4. Enter the JSON payload for your query.

|  | You can copy the JSON for a Query Request from the Couchbase Server Web Console to use in your REST API call. For more information about how to perform a search with the UI, see [Run A Simple Search with the Web Console](../search/simple-search-ui.md). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#example-hybrid-search-for-a-color-vector)Example: Hybrid Search for a Color Vector

In the following example, the JSON payload uses both a `query` and `knn` object to run both a Vector Search and traditional Search query on an index named `color-index`.

The query searches for a specified Euclidean distance color vector, but uses the `query` object to search for a color with a `brightness` value in the range of `70-80`:

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
          "k": 3, 
          "field": "colorvect_l2", 
          "vector": [ 176, 0, 176 ]
        }
      ]
    }'
```

The Search Service combines the Vector search results from the `knn` object with the traditional `query` object by using an `OR` function. If the same documents match the `knn` and `query` objects, the Search Service ranks those documents higher in search results.

|  | For a more complex query, you can copy the query object from the example under [Example: Running a Semantic Search Query with a Large Embedding Vector](run-vector-search-ui.md#large) to use in your REST API call. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

For more information about the available properties for a Search query JSON payload, see [Search Request JSON Properties](../search/search-request-params.md).

If the REST API call is successful, the Search Service returns a `200 OK` and the following JSON response:

```json
{
    "status": {
        "total": 1,
        "failed": 0,
        "successful": 1
    },
    "hits": [
        {
            "index": "vector-sample.color.color-index_629266a5f4e09384_4c1c5584",
            "id": "#B000B0",
            "score": 3.4028234663852886e+38,
            "sort": [
                "_score"
            ],
            "fields": {
                "brightness": 72.688,
                "color": "dark lavender",
                "description": "Dark lavender is a deep, rich color that exudes a sense of mystery and calmness. It envelopes the viewer in its alluring hue, drawing them in with its soothing presence. This color is perfect for creating a sense of depth and intrigue in any space."
            },
            "partial_match": true
        },
        {
            "index": "vector-sample.color.color-index_629266a5f4e09384_4c1c5584",
            "id": "#008000",
            "score": 0.42046520427629075,
            "sort": [
                "_score"
            ],
            "fields": {
                "brightness": 75.136,
                "color": "green",
                "description": "Green is a color that evokes feelings of freshness and vitality. It is often associated with nature and growth, as it is the color of many plants and trees. The color green can also represent balance and harmony, as it is a combination of the calming blue and energizing yellow. It is a versatile color that can range from a soft pastel to a bold and vibrant hue. Whether it's the lush green of a forest or the crisp green of a freshly cut lawn, this color has a way of invigorating and rejuvenating the senses."
            },
            "partial_match": true
        },
        {
            "index": "vector-sample.color.color-index_629266a5f4e09384_4c1c5584",
            "id": "#483D8B",
            "score": 0.42046520427629075,
            "sort": [
                "_score"
            ],
            "fields": {
                "brightness": 73.181,
                "color": "dark slate blue",
                "description": "Dark slate blue is a rich and deep color that evokes a sense of mystery and calmness. It envelopes the viewer in its deep hue, creating a soothing and tranquil atmosphere. This color is perfect for creating a sense of depth and intrigue in any space."
            },
            "partial_match": true
        },
        {
            "index": "vector-sample.color.color-index_629266a5f4e09384_4c1c5584",
            "id": "#C000C0",
            "score": 0.3829836951163303,
            "sort": [
                "_score"
            ],
            "fields": {
                "brightness": 79.296,
                "color": "magenta",
                "description": "Magenta is a vibrant and bold color that is often described as a deep purplish-red. It is a highly saturated color that is eye-catching and demands attention. Magenta is often associated with creativity, passion, and energy. It is a color that exudes confidence and can add a pop of excitement to any design or outfit."
            },
            "partial_match": true
        },
        {
            "index": "vector-sample.color.color-index_629266a5f4e09384_4c1c5584",
            "id": "#FF0000",
            "score": 0.3810305701163303,
            "sort": [
                "_score"
            ],
            "fields": {
                "brightness": 76.245,
                "color": "red",
                "description": "Red is a vibrant color that evokes feelings of passion and intensity. It is a bold and attention-grabbing color that symbolizes love, energy, and power. Red is often associated with strong emotions and can also represent danger or warning. It is a color that demands attention and can make a statement in any setting."
            },
            "partial_match": true
        },
        {
            "index": "vector-sample.color.color-index_629266a5f4e09384_4c1c5584",
            "id": "#A52A2A",
            "score": 0.3810305701163303,
            "sort": [
                "_score"
            ],
            "fields": {
                "brightness": 78.777,
                "color": "brown",
                "description": "Brown is a warm and earthy color that often evokes feelings of comfort and stability. It is a rich color that can range from light tan to dark chocolate. Brown is often associated with nature and can be found in the colors of trees, soil, and animals. It is a versatile color that can be used in both casual and formal settings, making it a popular choice in fashion and interior design. Overall, brown is a comforting and grounding color that adds a sense of warmth and coziness to any environment."
            },
            "partial_match": true
        },
        {
            "index": "vector-sample.color.color-index_629266a5f4e09384_4c1c5584",
            "id": "#B22222",
            "score": 0.3810305701163303,
            "sort": [
                "_score"
            ],
            "fields": {
                "brightness": 77.056,
                "color": "firebrick",
                "description": "Firebrick is a deep, rich red color that evokes images of a blazing fire. It is a warm and intense hue, reminiscent of the glowing embers of a fire. The color is bold and eye-catching, yet also has a sense of warmth and comfort. Firebrick is a powerful and passionate color that demands attention and exudes energy and vitality."
            },
            "partial_match": true
        },
        {
            "index": "vector-sample.color.color-index_629266a5f4e09384_4c1c5584",
            "id": "#9400D3",
            "score": 0.0004977600796416127,
            "sort": [
                "_score"
            ],
            "fields": {
                "brightness": 68.306,
                "color": "dark violet",
                "description": "Dark violet is a rich and deep color that can be described as enveloping, mysterious, and intense. It is a shade of purple that is darker and more intense than traditional violet. It exudes a sense of mystery and depth, making it a popular choice for creating a dramatic and moody atmosphere. The color is often associated with luxury, royalty, and spirituality. Its deep and intense hue can evoke a sense of power and sophistication. Dark violet is a versatile color that can be used to add depth and drama to any space or design."
            }
        }
    ],
    "total_hits": 8,
    "cost": 2621,
    "max_score": 3.4028234663852886e+38,
    "took": 6628491,
    "facets": null
}
```

### [](#example-use-global%5Fscoring-with-a-bm25-search-index)Example: Use global\_scoring With a bm25 Search Index

In the following example, the JSON payload uses both a `query` and `knn` object to run both a Vector Search and traditional Search query on an index named `products-index`.

The query searches for a specific embedding vector generated from an ecommerce website’s product description. The Search vector is generated from the phrase `long battery life wireless earbuds`. The `query` object specifically searches for documents that have `Electronics` as their category, with a price between `100.00` and `300.00`. The query returns the `description`, `price`, and `product_name` fields in results. Since the query is on a large, partitioned index and uses the `bm25` scoring algorithm, the query also uses `global_scoring` to keep document scores consistent across the Search index’s partitions:

```console
curl -XPOST -H "Content-Type: application/json" \
  -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/e-commerce/scope/products/index/products-index/query \
-d '{
      "fields": ["description", "price", "product_name"],
      "query": {
        "conjuncts": [
          {
            "term": "Electronics",
            "field": "category"
          },
          {
            "field": "price",
            "min": 100.00,
            "max": 300.00,
            "inclusive_max": true
          }
        ]
      },
      "knn": [
        {
          "k": 5,
          "field": "embedding",
          "vector": [0.23, -0.75, 0.61, ...]
        }
      ],
      "ctl": {
        "global_scoring": true
      }
    }'
```

|  | The vector embedding has been truncated for this example. The vector embedding in your Search query must match the configured dimension and similarity metric for your Search index. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

If the REST API call is successful, the Search Service returns a `200 OK`.

For more information about the `bm25` scoring algorithm, see [Scoring for Search Queries](../search/run-searches.md#scoring).

## [](#next-steps)Next Steps

If you do not get the search results you were expecting, you can change the JSON definition [for your Search index](../search/search-index-params.md) or change the parameters [for your Search query](../search/search-request-params.md).

You can also [Customize a Search Index with the Web Console](../search/customize-index.md).