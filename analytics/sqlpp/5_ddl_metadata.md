---
title: Querying Metadata
description: You can review information about your Capella Analytics entities by
  querying the collections in the <code>System.Metadata</code> scope.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sqlpp/pages/5_ddl_metadata.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:analytics:sqlpp:5_ddl_metadata.adoc[]
---

[View original HTML](/analytics/sqlpp/5_ddl_metadata.html)

# Querying Metadata

> You can review information about your Capella Analytics entities by querying the collections in the `System.Metadata` scope. 

For metadata introspection, the `System.Metadata` scope contains the following collections:

* Database
* Dataverse, for scope metadata
* Dataset, for collection metadata
* Function
* Index
* Link
* Synonym

Each collection contains the queryable metadata for that entity type.

Each of these collection identifiers is a [reserved word](reserved%5Fkeywords.md). As a result, you must escape these names with backticks (``` `` ```), as shown in the examples that follow.

For more information about metadata storage, see [Metadata Storage](1a%5Fentities.md#metadata).

## [](#examples)Examples

This example returns the metadata for a single link object so that you can identify the field names for further querying:

```SQL++
  SELECT * FROM System.Metadata.`Link` LIMIT 1;
```

Returns:

```SQL++
  {
    "Link": {
      "Name": "capellaLink",
      "Type": "COUCHBASE",
      "IsActive": true
    }
  }
```

To get additional information about a link, you can use a [DESCRIBE LINK](5%5Fdml%5Fdescribe.md) statement.

The next example returns the metadata for a specific collection. In its results, you can then verify the values for its Amazon S3 bucket—or `ON` clause—and path by inspecting the container and definition properties respectively.

```SQL++
  SELECT * from System.Metadata.`Dataset`
    WHERE DatasetName = "rockSongs";
```

Returns:

[
  {
    "Dataset": {
    "DatabaseName": "music",
    "DataverseName": "myPlaylist",
    "DatasetName": "rockSongs",
    "DatatypeDataverseName": "Metadata",
    "DatatypeName": "AnyObject",
    "DatasetType": "EXTERNAL",
    "GroupName": "music.myPlaylist.rockSongs",
    "CompactionPolicy": "",
    "CompactionPolicyProperties": [],
    "ExternalDetails": {
      "DatasourceAdapter": "LINK",
      "Properties": [
        {
          "Name": "container",
          "Value": "music"
        },
        {
          "Name": "name",
          "Value": "musicLink"
        },
        {
          "Name": "format",
          "Value": "json"
        },
        {
          "Name": "database",
          "Value": "music"
        },
        {
          "Name": "definition",
          "Value": "music/myPlaylist/rockSongs"
        },
        {
          "Name": "dataverse",
          "Value": "myPlaylist"
        }
      ],
      "LastRefreshTime": "2024-02-02T15:23:08.508",
      "TransactionState": 0
    },
    "Hints": [],
    "Timestamp": "Fri Feb 02 15:23:08 GMT 2024",
    "DatasetId": 117,
    "PendingOp": 0,
    "DatatypeDatabaseName": "System",
    "DatasetFormat": {
      "Format": "ROW"
      }
    }
  }
]

The next example returns the qualified names of all collections that are not themselves in the `System.Metadata` scope.

```SQL++
  SELECT VALUE d.DatabaseName || '.' || d.DataverseName || '.' || d.DatasetName
  FROM System.Metadata.`Dataset` d
  WHERE d.DataverseName <> "Metadata";
```

Returns:

[
  "sampleAnalytics.Commerce.customers",
  "sampleAnalytics.Commerce.orders",
  "music.myPlaylist.rockSongs",
  "music.myPlaylist.countrySongs"
]

## [](#see-also)See Also

* [Metadata Storage](1a%5Fentities.md#metadata)
* [Access and Organize Data in Capella Analytics Services](../sources/database-objects.md)