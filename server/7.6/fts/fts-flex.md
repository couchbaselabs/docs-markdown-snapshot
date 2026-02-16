[View original HTML](/server/7.6/fts/fts-flex.html)

FTS is capable of supporting multiple collections within a single index definition.

Pre Couchbase Server 7.0 index definitions will continue to be supported with 7.0 FTS.

If the user wants to set up an index definition to subscribe to just a few collections within a single scope, they will be able to do so by toggling the "doc\_config.mode" to either of \["scope.collection.type\_field", "scope.collection.docid\_prefix"\].

The type mappings will now take the form of either "scope\_name.collection\_name" (to index all documents within that scope.collection) or "scope\_name.collection\_name.type\_name" (to index only those documents within that scope.collection that match "type" = "type\_name") . We will refer to FTS index definitions in this mode as collection-aware FTS indexes.

|  | The type expression check within SQL++ queries becomes unnecessary with collection-aware FTS indexes. |
|  | ----------------------------------------------------------------------------------------------------- |

## [](#example)Example

When you set up an FTS index definition to stream from 2 collections: landmark, hotel such as:

{
  "type": "fulltext-index",
  "name": "travel",
  "sourceType": "gocbcore",
  "sourceName": "travel-sample",
  "params": {
    "doc_config": {
      "mode": "scope.collection.type_field",
      "type_field": "type"
    },
    "mapping": {
      "analysis": {},
      "default_analyzer": "standard",
      "default_mapping": {
        "dynamic": true,
        "enabled": false
      },
      "types": {
        "inventory.hotel": {
          "enabled": true,
          "properties": {
            "reviews": {
              "enabled": true,
              "properties": {
                "content": {
                  "enabled": true,
                  "fields": [
                    {
                      "analyzer": "keyword",
                      "index": true,
                      "name": "content",
                      "type": "text"
                    }
                  ]
                }
              }
            }
          }
        },
        "inventory.landmark": {
          "enabled": true,
          "properties": {
            "content": {
              "enabled": true,
              "fields": [
                {
                  "analyzer": "keyword",
                  "index": true,
                  "name": "content",
                  "type": "text"
                }
              ]
            }
          }
        }
      }
    }
  }
}

Below are some SQL++ queries targeting the above index definition.

SELECT META().id
FROM `travel-sample`.`inventory`.`landmark` t USE INDEX(USING FTS)
WHERE content LIKE "%travel%";

SELECT META().id
FROM `travel-sample`.`inventory`.`hotel` t USE INDEX(USING FTS)
WHERE reviews.content LIKE "%travel%";

SELECT META().id
FROM `travel-sample`.`inventory`.`hotel` t USE INDEX(USING FTS)
WHERE content LIKE "%travel%";