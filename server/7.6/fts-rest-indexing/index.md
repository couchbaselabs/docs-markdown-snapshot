---
title: Couchbase Search Index Management and Monitoring API
description: The Search Indexing REST API is provided by the Search Service.
  This API enables you to manage and monitor your Search indexes.
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/7.6/docs/modules/fts-rest-indexing/pages/index.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:fts-rest-indexing:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts-rest-indexing/index.html)

# Couchbase Search Index Management and Monitoring API

## [](#overview)Overview

The Search Indexing REST API is provided by the Search service. This API enables you to manage and monitor your Search indexes.

### Version information

**Version:** 7.6

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                              |
| ---------- | ---------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                     |
| **host**   | The host name or IP address of a node running the Search Service. **Example:** localhost |
| **port**   | The Search Service REST port. Use 18094 for secure access. **Values:** 8094, 18094       |

## [](#resources)Resources

This section describes the operations available with this REST API. The operations are grouped in the following categories.

[Definitions](#tag-Definitions)  
[Management](#tag-Management)  
[Monitoring](#tag-Monitoring)  
[Querying](#tag-Querying)

### [](#tag-Definitions)Definitions

Use the following APIs to retrieve Search index definitions, create new Search indexes, or delete an existing Search index.

[Delete Index Definition](#d-api-index-name)  
[Delete Index Definition (Scoped)](#d-api-scoped-index-name)  
[Get All Search Index Definitions](#g-api-index)  
[Get Index Definition](#g-api-index-name)  
[Get All Search Index Definitions (Scoped)](#g-api-scoped-index)  
[Get Index Definition (Scoped)](#g-api-scoped-index-name)  
[Create or Update an Index Definition](#p-api-index-name)  
[Create or Update an Index Definition (Scoped)](#p-api-scoped-index-name)

#### [](#d-api-index-name)Delete Index Definition

DELETE /api/index/{INDEX_NAME}

##### [](#d-api-index-name-description)Description

Deletes the Search index definition specified in the endpoint URL.

> [!NOTE]
> This endpoint is for legacy Search indexes and may be deprecated in a future release. Use [Delete Index Definition (Scoped)](#d-api-scoped-index-name) instead.

Produces

* application/json

##### [](#d-api-index-name-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                                                                                                       | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **INDEX\_NAME**required | The name of the Search index definition. You must use the fully qualified name for the index, which includes the bucket and scope. To view the full, scoped name for an index for use with this endpoint: Go to the **Search** tab in the Couchbase Server Web Console. Point to the **Index Name** for an index. | String |

##### [](#d-api-index-name-responses)Responses

| HTTP Code | Description                                                                | Schema                                  |
| --------- | -------------------------------------------------------------------------- | --------------------------------------- |
| 200       | The Search Service returns a response that includes the status ok.         | [Delete Response](#DeleteIndexResponse) |
| Default   | The Search Service returns a non-200 HTTP error code when a request fails. | Object                                  |

##### [](#d-api-index-name-security)Security

| Type         | Name                     |
| ------------ | ------------------------ |
| http (basic) | [Write](#security-Write) |

##### [](#d-api-index-name-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok",
  "uuid" : "123294e5a4efbe39"
}
```

Default Response

```json
{
  "error" : "rest_auth: preparePerms, err: index not found",
  "request" : "",
  "status" : "fail"
}
```

#### [](#d-api-scoped-index-name)Delete Index Definition (Scoped)

DELETE /api/bucket/{BUCKET_NAME}/scope/{SCOPE_NAME}/index/{INDEX_NAME}

##### [](#d-api-scoped-index-name-description)Description

Delete the Search index definition from the bucket and scope specified in the endpoint URL. This endpoint is scoped and does not require a fully qualified `{INDEX_NAME}` value.

Produces

* application/json

##### [](#d-api-scoped-index-name-parameters)Parameters

Path Parameters

| Name                     | Description                                                                              | Schema |
| ------------------------ | ---------------------------------------------------------------------------------------- | ------ |
| **BUCKET\_NAME**required | The name of the bucket containing the Search index definition.                           | String |
| **SCOPE\_NAME**required  | The name of the scope containing the Search index definition.                            | String |
| **INDEX\_NAME**required  | The name of the Search index definition. **Pattern:** /^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$/ | String |

##### [](#d-api-scoped-index-name-responses)Responses

| HTTP Code | Description                                                                | Schema                                  |
| --------- | -------------------------------------------------------------------------- | --------------------------------------- |
| 200       | A JSON object indicating the status of the operation.                      | [Delete Response](#DeleteIndexResponse) |
| Default   | The Search Service returns a non-200 HTTP error code when a request fails. | Object                                  |

##### [](#d-api-scoped-index-name-security)Security

| Type         | Name                     |
| ------------ | ------------------------ |
| http (basic) | [Write](#security-Write) |

##### [](#d-api-scoped-index-name-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok",
  "uuid" : "687be6a2ad647c34"
}
```

Default Response

```json
{
  "error" : "rest_auth: preparePerms, err: index not found",
  "request" : "",
  "status" : "fail"
}
```

#### [](#g-api-index)Get All Search Index Definitions

GET /api/index

##### [](#g-api-index-description)Description

Returns all Search index definitions from the bucket where you have read permissions, as a JSON object.

> [!NOTE]
> This endpoint is for legacy Search indexes and may be deprecated in a future release. Use [Get All Search Index Definitions (Scoped)](#g-api-scoped-index) instead.

Produces

* application/json

##### [](#g-api-index-responses)Responses

| HTTP Code | Description                                            | Schema                                  |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 200       | A JSON object containing all Search index definitions. | [Indexes Response](#GetIndexesResponse) |

##### [](#g-api-index-security)Security

| Type         | Name                   |
| ------------ | ---------------------- |
| http (basic) | [Read](#security-Read) |

##### [](#g-api-index-ex-response)Example HTTP Response

Response 200

```json
{
  "indexDefs" : {
    "implVersion" : "4.0.0",
    "indexDefs" : {
      "myFirstIndex" : {
        "name" : "myFirstIndex",
        "params" : "",
        "planParams" : {
          "hierarchyRules" : null,
          "maxPartitionsPerPIndex" : 0,
          "nodePlanParams" : null,
          "numReplicas" : 0,
          "planFrozen" : false
        },
        "sourceName" : "",
        "sourceParams" : "",
        "sourceType" : "nil",
        "sourceUUID" : "",
        "type" : "fulltext-index",
        "uuid" : "6cc599ab7a85bf3b"
      }
    },
    "uuid" : "6cc599ab7a85bf3b"
  },
  "status" : "ok"
}
```

#### [](#g-api-index-name)Get Index Definition

GET /api/index/{INDEX_NAME}

##### [](#g-api-index-name-description)Description

Returns the definition of the Search index specified in the endpoint URL as a JSON object.

> [!NOTE]
> This endpoint is for legacy Search indexes and may be deprecated in a future release. Use [Get Index Definition (Scoped)](#g-api-scoped-index-name) instead.

Produces

* application/json

##### [](#g-api-index-name-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                                                                                                       | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **INDEX\_NAME**required | The name of the Search index definition. You must use the fully qualified name for the index, which includes the bucket and scope. To view the full, scoped name for an index for use with this endpoint: Go to the **Search** tab in the Couchbase Server Web Console. Point to the **Index Name** for an index. | String |

##### [](#g-api-index-name-responses)Responses

| HTTP Code | Description                                           | Schema                              |
| --------- | ----------------------------------------------------- | ----------------------------------- |
| 200       | A JSON object containing the Search index definition. | [Index Response](#GetIndexResponse) |

##### [](#g-api-index-name-security)Security

| Type         | Name                   |
| ------------ | ---------------------- |
| http (basic) | [Read](#security-Read) |

##### [](#g-api-index-name-ex-response)Example HTTP Response

Response 200

```json
{
  "indexDef" : {
    "name" : "myFirstIndex",
    "params" : "",
    "planParams" : {
      "hierarchyRules" : null,
      "maxPartitionsPerPIndex" : 0,
      "nodePlanParams" : null,
      "numReplicas" : 0,
      "planFrozen" : false
    },
    "sourceName" : "",
    "sourceParams" : "",
    "source" : "nil",
    "sourceUUID" : "",
    "type" : "fulltext-index",
    "uuid" : "6cc599ab7a85bf3b"
  },
  "planPIndexes" : [ {
    "indexName" : "myFirstIndex",
    "indexParams" : "",
    "indexType" : "bleve",
    "indexUUID" : "6cc599ab7a85bf3b",
    "name" : "myFirstIndex_6cc599ab7a85bf3b_0",
    "nodes" : {
      "78fc2ffac2fd9401" : {
        "canRead" : true,
        "canWrite" : true,
        "priority" : 0
      }
    },
    "sourceName" : "",
    "sourceParams" : "",
    "sourcePartitions" : "",
    "sourceType" : "nil",
    "sourceUUID" : "",
    "uuid" : "64bed6e2edf354c3"
  } ],
  "status" : "ok",
  "warnings" : [ ]
}
```

#### [](#g-api-scoped-index)Get All Search Index Definitions (Scoped)

GET /api/bucket/{BUCKET_NAME}/scope/{SCOPE_NAME}/index

##### [](#g-api-scoped-index-description)Description

Returns all Search index definitions inside the bucket and scope specified in the endpoint URL as a JSON object.

Produces

* application/json

##### [](#g-api-scoped-index-parameters)Parameters

Path Parameters

| Name                     | Description                                                    | Schema |
| ------------------------ | -------------------------------------------------------------- | ------ |
| **BUCKET\_NAME**required | The name of the bucket containing the Search index definition. | String |
| **SCOPE\_NAME**required  | The name of the scope containing the Search index definition.  | String |

##### [](#g-api-scoped-index-responses)Responses

| HTTP Code | Description                                            | Schema                                  |
| --------- | ------------------------------------------------------ | --------------------------------------- |
| 200       | A JSON object containing all Search index definitions. | [Indexes Response](#GetIndexesResponse) |

##### [](#g-api-scoped-index-security)Security

| Type         | Name                   |
| ------------ | ---------------------- |
| http (basic) | [Read](#security-Read) |

##### [](#g-api-scoped-index-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok",
  "indexDefs" : {
    "uuid" : "23cf9530131858b8",
    "indexDefs" : {
      "travel-sample.inventory.travel-hotel" : {
        "type" : "fulltext-index",
        "name" : "travel-hotel",
        "uuid" : "a04a16f178846bc4",
        "sourceType" : "gocbcore",
        "sourceName" : "travel-sample",
        "sourceUUID" : "8f866261438f8b0d415a437552f3ae99",
        "planParams" : {
          "maxPartitionsPerPIndex" : 1024,
          "indexPartitions" : 1
        },
        "params" : {
          "doc_config" : {
            "docid_prefix_delim" : "",
            "docid_regexp" : "",
            "mode" : "scope.collection.type_field",
            "type_field" : "type"
          },
          "mapping" : {
            "analysis" : { },
            "default_analyzer" : "standard",
            "default_datetime_parser" : "dateTimeOptional",
            "default_field" : "_all",
            "default_mapping" : {
              "dynamic" : true,
              "enabled" : false
            },
            "default_type" : "_default",
            "docvalues_dynamic" : false,
            "index_dynamic" : true,
            "store_dynamic" : false,
            "type_field" : "_type",
            "types" : {
              "inventory.hotel" : {
                "dynamic" : false,
                "enabled" : true,
                "properties" : {
                  "reviews" : {
                    "dynamic" : false,
                    "enabled" : true,
                    "properties" : {
                      "content" : {
                        "dynamic" : false,
                        "enabled" : true,
                        "fields" : [ {
                          "docvalues" : true,
                          "include_in_all" : true,
                          "include_term_vectors" : true,
                          "index" : true,
                          "name" : "content",
                          "store" : true,
                          "type" : "text"
                        } ]
                      }
                    }
                  }
                }
              }
            }
          },
          "store" : {
            "indexType" : "scorch",
            "segmentVersion" : 15
          }
        },
        "sourceParams" : { }
      },
      "travel-sample.inventory.travel-test" : {
        "type" : "fulltext-index",
        "name" : "travel-test",
        "uuid" : "766ddce5d41a3b41",
        "sourceType" : "gocbcore",
        "sourceName" : "travel-sample",
        "sourceUUID" : "8f866261438f8b0d415a437552f3ae99",
        "planParams" : {
          "maxPartitionsPerPIndex" : 1024,
          "indexPartitions" : 1
        },
        "params" : {
          "doc_config" : {
            "docid_prefix_delim" : "",
            "docid_regexp" : "",
            "mode" : "scope.collection.type_field",
            "type_field" : "type"
          },
          "mapping" : {
            "analysis" : { },
            "default_analyzer" : "standard",
            "default_datetime_parser" : "dateTimeOptional",
            "default_field" : "_all",
            "default_mapping" : {
              "dynamic" : true,
              "enabled" : true
            },
            "default_type" : "_default",
            "docvalues_dynamic" : false,
            "index_dynamic" : true,
            "store_dynamic" : false,
            "type_field" : "_type"
          },
          "store" : {
            "indexType" : "scorch",
            "segmentVersion" : 15
          }
        },
        "sourceParams" : { }
      }
    },
    "implVersion" : "5.7.0"
  }
}
```

#### [](#g-api-scoped-index-name)Get Index Definition (Scoped)

GET /api/bucket/{BUCKET_NAME}/scope/{SCOPE_NAME}/index/{INDEX_NAME}

##### [](#g-api-scoped-index-name-description)Description

Returns the Search index definition for the Search index specified in the endpoint URL as a JSON object. This endpoint is scoped and does not require a fully qualified `{INDEX_NAME}` value.

Produces

* application/json

##### [](#g-api-scoped-index-name-parameters)Parameters

Path Parameters

| Name                     | Description                                                                              | Schema |
| ------------------------ | ---------------------------------------------------------------------------------------- | ------ |
| **BUCKET\_NAME**required | The name of the bucket containing the Search index definition.                           | String |
| **SCOPE\_NAME**required  | The name of the scope containing the Search index definition.                            | String |
| **INDEX\_NAME**required  | The name of the Search index definition. **Pattern:** /^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$/ | String |

##### [](#g-api-scoped-index-name-responses)Responses

| HTTP Code | Description                                           | Schema                              |
| --------- | ----------------------------------------------------- | ----------------------------------- |
| 200       | A JSON object containing the Search index definition. | [Index Response](#GetIndexResponse) |

##### [](#g-api-scoped-index-name-security)Security

| Type         | Name                   |
| ------------ | ---------------------- |
| http (basic) | [Read](#security-Read) |

##### [](#g-api-scoped-index-name-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok",
  "indexDef" : {
    "type" : "fulltext-index",
    "name" : "color-test",
    "uuid" : "6ea521a918bd3837",
    "sourceType" : "gocbcore",
    "sourceName" : "vector-sample",
    "sourceUUID" : "614177a67bdfbd2823c5f9c3e62f5991",
    "planParams" : {
      "maxPartitionsPerPIndex" : 1024,
      "indexPartitions" : 1
    },
    "params" : {
      "doc_config" : {
        "docid_prefix_delim" : "",
        "docid_regexp" : "",
        "mode" : "scope.collection.type_field",
        "type_field" : "type"
      },
      "mapping" : {
        "analysis" : { },
        "default_analyzer" : "standard",
        "default_datetime_parser" : "dateTimeOptional",
        "default_field" : "_all",
        "default_mapping" : {
          "dynamic" : false,
          "enabled" : false
        },
        "default_type" : "_default",
        "docvalues_dynamic" : false,
        "index_dynamic" : false,
        "store_dynamic" : false,
        "type_field" : "_type",
        "types" : {
          "color.rgb" : {
            "dynamic" : false,
            "enabled" : true,
            "properties" : {
              "color" : {
                "dynamic" : false,
                "enabled" : true,
                "fields" : [ {
                  "analyzer" : "en",
                  "docvalues" : true,
                  "include_in_all" : true,
                  "include_term_vectors" : true,
                  "index" : true,
                  "name" : "color",
                  "store" : true,
                  "type" : "text"
                } ]
              },
              "colorvect_dot" : {
                "dynamic" : false,
                "enabled" : true,
                "fields" : [ {
                  "dims" : 3,
                  "index" : true,
                  "name" : "colorvect_dot",
                  "similarity" : "dot_product",
                  "type" : "vector",
                  "vector_index_optimized_for" : "recall"
                } ]
              }
            }
          }
        }
      },
      "store" : {
        "indexType" : "scorch",
        "segmentVersion" : 16
      }
    },
    "sourceParams" : { }
  },
  "planPIndexes" : [ {
    "name" : "vector-sample.color.color-test_6ea521a918bd3837_4c1c5584",
    "uuid" : "1543820346544e08",
    "indexType" : "fulltext-index",
    "indexName" : "vector-sample.color.color-test",
    "indexUUID" : "6ea521a918bd3837",
    "sourceType" : "gocbcore",
    "sourceName" : "vector-sample",
    "sourceUUID" : "614177a67bdfbd2823c5f9c3e62f5991",
    "sourcePartitions" : "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999,1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023",
    "nodes" : {
      "b7d460b7d4145482ac132dfa23727c5c" : {
        "canRead" : true,
        "canWrite" : true,
        "priority" : 0
      }
    },
    "indexParams" : {
      "doc_config" : {
        "docid_prefix_delim" : "",
        "docid_regexp" : "",
        "mode" : "scope.collection.type_field",
        "type_field" : "type"
      },
      "mapping" : {
        "analysis" : { },
        "default_analyzer" : "standard",
        "default_datetime_parser" : "dateTimeOptional",
        "default_field" : "_all",
        "default_mapping" : {
          "dynamic" : false,
          "enabled" : false
        },
        "default_type" : "_default",
        "docvalues_dynamic" : false,
        "index_dynamic" : false,
        "store_dynamic" : false,
        "type_field" : "_type",
        "types" : {
          "color.rgb" : {
            "dynamic" : false,
            "enabled" : true,
            "properties" : {
              "color" : {
                "dynamic" : false,
                "enabled" : true,
                "fields" : [ {
                  "analyzer" : "en",
                  "docvalues" : true,
                  "include_in_all" : true,
                  "include_term_vectors" : true,
                  "index" : true,
                  "name" : "color",
                  "store" : true,
                  "type" : "text"
                } ]
              },
              "colorvect_dot" : {
                "dynamic" : false,
                "enabled" : true,
                "fields" : [ {
                  "dims" : 3,
                  "index" : true,
                  "name" : "colorvect_dot",
                  "similarity" : "dot_product",
                  "type" : "vector",
                  "vector_index_optimized_for" : "recall"
                } ]
              }
            }
          }
        }
      },
      "store" : {
        "indexType" : "scorch",
        "segmentVersion" : 16
      }
    }
  } ],
  "warnings" : [ ]
}
```

#### [](#p-api-index-name)Create or Update an Index Definition

PUT /api/index/{INDEX_NAME}

##### [](#p-api-index-name-description)Description

If the Search index in the endpoint URL does not exist, this endpoint uses a JSON object in the request body to create a new index. If the Search index already exists, this endpoint updates the Search index definition.

> [!NOTE]
> This endpoint is for legacy Search indexes and may be deprecated in a future release. Use [Create or Update an Index Definition (Scoped)](#p-api-scoped-index-name) instead.

Consumes

* application/json

Produces

* application/json

##### [](#p-api-index-name-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                                                                                                       | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **INDEX\_NAME**required | The name of the Search index definition. You must use the fully qualified name for the index, which includes the bucket and scope. To view the full, scoped name for an index for use with this endpoint: Go to the **Search** tab in the Couchbase Server Web Console. Point to the **Index Name** for an index. | String |

Body Parameter

| Name             | Description                                                                                                                                                           | Schema                               |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **Body**required | The full Search index definition. For a detailed list of all parameters for the request body, see [Search Index JSON Properties](../search/search-index-params.html). | [Index Definition](#IndexDefinition) |

##### [](#p-api-index-name-responses)Responses

| HTTP Code | Description                                                                | Schema                                         |
| --------- | -------------------------------------------------------------------------- | ---------------------------------------------- |
| 200       | A JSON object indicating the status of the operation.                      | [Create or Update Response](#PutIndexResponse) |
| Default   | The Search Service returns a non-200 HTTP error code when a request fails. | Object                                         |

##### [](#p-api-index-name-security)Security

| Type         | Name                     |
| ------------ | ------------------------ |
| http (basic) | [Write](#security-Write) |

##### [](#p-api-index-name-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok",
  "name" : "travel-test",
  "uuid" : "565ca041af3baf9d"
}
```

Default Response

```json
{
  "error" : "rest_create_index: index type is required, indexName: travel-test",
  "request" : "",
  "status" : "fail"
}
```

#### [](#p-api-scoped-index-name)Create or Update an Index Definition (Scoped)

PUT /api/bucket/{BUCKET_NAME}/scope/{SCOPE_NAME}/index/{INDEX_NAME}

##### [](#p-api-scoped-index-name-description)Description

If the Search index in the endpoint URL does not exist, this endpoint uses a JSON object in the request body to create a new index. If the Search index already exists, this endpoint updates the Search index definition. This endpoint is scoped and does not require a fully qualified `{INDEX_NAME}` value.

Consumes

* application/json

Produces

* application/json

##### [](#p-api-scoped-index-name-parameters)Parameters

Path Parameters

| Name                     | Description                                                                              | Schema |
| ------------------------ | ---------------------------------------------------------------------------------------- | ------ |
| **BUCKET\_NAME**required | The name of the bucket containing the Search index definition.                           | String |
| **SCOPE\_NAME**required  | The name of the scope containing the Search index definition.                            | String |
| **INDEX\_NAME**required  | The name of the Search index definition. **Pattern:** /^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$/ | String |

Body Parameter

| Name             | Description                                                                                                                                                           | Schema                               |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **Body**required | The full Search index definition. For a detailed list of all parameters for the request body, see [Search Index JSON Properties](../search/search-index-params.html). | [Index Definition](#IndexDefinition) |

##### [](#p-api-scoped-index-name-responses)Responses

| HTTP Code | Description                                                                | Schema                                         |
| --------- | -------------------------------------------------------------------------- | ---------------------------------------------- |
| 200       | A JSON object indicating the status of the operation.                      | [Create or Update Response](#PutIndexResponse) |
| Default   | The Search Service returns a non-200 HTTP error code when a request fails. | Object                                         |

##### [](#p-api-scoped-index-name-security)Security

| Type         | Name                     |
| ------------ | ------------------------ |
| http (basic) | [Write](#security-Write) |

##### [](#p-api-scoped-index-name-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok",
  "name" : "travel-sample.inventory.travel-test",
  "uuid" : "654cb62baebf2d26"
}
```

Default Response

```json
{
  "error" : "rest_create_index: index type is required, indexName: travel-test",
  "request" : { },
  "status" : "fail"
}
```

### [](#tag-Management)Management

Use the following endpoints to manage index controls, such as document ingestion, partition assignment, and queries.

[Set Index Ingestion Control](#p-api-idx-name-ingestcontrol)  
[Freeze Index Partition Assignment](#p-api-idx-name-planfreezecontrol)  
[Stop Queries on an Index](#p-api-idx-name-querycontrol)  
[Set Index Ingestion Control (Scoped)](#p-api-scoped-ingestcontrol)  
[Freeze Index Partition Assignment (Scoped)](#p-api-scoped-planfreezecontrol)  
[Stop Queries on an Index (Scoped)](#p-api-scoped-querycontrol)

#### [](#p-api-idx-name-ingestcontrol)Set Index Ingestion Control

POST /api/index/{INDEX_NAME}/ingestControl/{OP}

##### [](#p-api-idx-name-ingestcontrol-description)Description

For the Search index specified in the endpoint URL, pause or resume index updates and maintenance. While paused, the Search index does not load any new document mutations.

> [!NOTE]
> This endpoint is for legacy Search indexes and may be deprecated in a future release. Use [Set Index Ingestion Control (Scoped)](#p-api-scoped-ingestcontrol) instead.

Produces

* application/json

##### [](#p-api-idx-name-ingestcontrol-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                                                                                                       | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **INDEX\_NAME**required | The name of the Search index definition. You must use the fully qualified name for the index, which includes the bucket and scope. To view the full, scoped name for an index for use with this endpoint: Go to the **Search** tab in the Couchbase Server Web Console. Point to the **Index Name** for an index. | String |
| **OP**required          | To pause ingestion and maintenance, set {OP} to pause. To resume ingestion and maintenance on a paused index, set {OP} to resume. **Values:** "pause", "resume"                                                                                                                                                   | String |

##### [](#p-api-idx-name-ingestcontrol-responses)Responses

| HTTP Code | Description                                                        | Schema                               |
| --------- | ------------------------------------------------------------------ | ------------------------------------ |
| 200       | The Search Service returns a response that includes the status ok. | [Management Response](#MgmtResponse) |

##### [](#p-api-idx-name-ingestcontrol-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Manage](#security-Manage) |

##### [](#p-api-idx-name-ingestcontrol-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok"
}
```

#### [](#p-api-idx-name-planfreezecontrol)Freeze Index Partition Assignment

POST /api/index/{INDEX_NAME}/planFreezeControl/{OP}

##### [](#p-api-idx-name-planfreezecontrol-description)Description

For the Search index specified in the endpoint URL, freeze or unfreeze the assignment of index partitions to nodes. While frozen, the Search index stops assigning partitions during index rebalancing and index definition updates.

> [!NOTE]
> This endpoint is for legacy Search indexes and may be deprecated in a future release. Use [Freeze Index Partition Assignment (Scoped)](#p-api-scoped-planfreezecontrol) instead.

Produces

* application/json

##### [](#p-api-idx-name-planfreezecontrol-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                                                                                                       | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **INDEX\_NAME**required | The name of the Search index definition. You must use the fully qualified name for the index, which includes the bucket and scope. To view the full, scoped name for an index for use with this endpoint: Go to the **Search** tab in the Couchbase Server Web Console. Point to the **Index Name** for an index. | String |
| **OP**required          | To freeze partition assignment, set {OP} to freeze. To unfreeze partition assignment on a frozen index, set {OP} to unfreeze. **Values:** "freeze", "unfreeze"                                                                                                                                                    | String |

##### [](#p-api-idx-name-planfreezecontrol-responses)Responses

| HTTP Code | Description                                                        | Schema                               |
| --------- | ------------------------------------------------------------------ | ------------------------------------ |
| 200       | The Search Service returns a response that includes the status ok. | [Management Response](#MgmtResponse) |

##### [](#p-api-idx-name-planfreezecontrol-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Manage](#security-Manage) |

##### [](#p-api-idx-name-planfreezecontrol-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok"
}
```

#### [](#p-api-idx-name-querycontrol)Stop Queries on an Index

POST /api/index/{INDEX_NAME}/queryControl/{OP}

##### [](#p-api-idx-name-querycontrol-description)Description

For the Search index specified in the endpoint URL, disallow or allow queries. While queries are disallowed, users see an error that the Search index's partitions could not be reached.

> [!NOTE]
> This endpoint is for legacy Search indexes and may be deprecated in a future release. Use [Stop Queries on an Index (Scoped)](#p-api-scoped-querycontrol) instead.

Produces

* application/json

##### [](#p-api-idx-name-querycontrol-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                                                                                                       | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **INDEX\_NAME**required | The name of the Search index definition. You must use the fully qualified name for the index, which includes the bucket and scope. To view the full, scoped name for an index for use with this endpoint: Go to the **Search** tab in the Couchbase Server Web Console. Point to the **Index Name** for an index. | String |
| **OP**required          | To allow queries against a Search index, set {OP} to allow. To block queries against a Search index, set {OP} to disallow. **Values:** "allow", "disallow"                                                                                                                                                        | String |

##### [](#p-api-idx-name-querycontrol-responses)Responses

| HTTP Code | Description                                                        | Schema                               |
| --------- | ------------------------------------------------------------------ | ------------------------------------ |
| 200       | The Search Service returns a response that includes the status ok. | [Management Response](#MgmtResponse) |

##### [](#p-api-idx-name-querycontrol-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Manage](#security-Manage) |

##### [](#p-api-idx-name-querycontrol-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok"
}
```

#### [](#p-api-scoped-ingestcontrol)Set Index Ingestion Control (Scoped)

POST /api/bucket/{BUCKET_NAME}/scope/{SCOPE_NAME}/index/{INDEX_NAME}/ingestControl/{OP}

##### [](#p-api-scoped-ingestcontrol-description)Description

For the Search index specified in the endpoint URL, pause or resume index updates and maintenance. While paused, the Search index does not load any new document mutations. This endpoint is scoped and does not require a fully qualified `{INDEX_NAME}` value.

Produces

* application/json

##### [](#p-api-scoped-ingestcontrol-parameters)Parameters

Path Parameters

| Name                     | Description                                                                                                                                                     | Schema |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **BUCKET\_NAME**required | The name of the bucket containing the Search index definition.                                                                                                  | String |
| **SCOPE\_NAME**required  | The name of the scope containing the Search index definition.                                                                                                   | String |
| **INDEX\_NAME**required  | The name of the Search index definition. **Pattern:** /^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$/                                                                        | String |
| **OP**required           | To pause ingestion and maintenance, set {OP} to pause. To resume ingestion and maintenance on a paused index, set {OP} to resume. **Values:** "pause", "resume" | String |

##### [](#p-api-scoped-ingestcontrol-responses)Responses

| HTTP Code | Description                                                        | Schema                               |
| --------- | ------------------------------------------------------------------ | ------------------------------------ |
| 200       | The Search Service returns a response that includes the status ok. | [Management Response](#MgmtResponse) |

##### [](#p-api-scoped-ingestcontrol-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Manage](#security-Manage) |

##### [](#p-api-scoped-ingestcontrol-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok"
}
```

#### [](#p-api-scoped-planfreezecontrol)Freeze Index Partition Assignment (Scoped)

POST /api/bucket/{BUCKET_NAME}/scope/{SCOPE_NAME}/index/{INDEX_NAME}/planFreezeControl/{OP}

##### [](#p-api-scoped-planfreezecontrol-description)Description

For the Search index specified in the endpoint URL, freeze or unfreeze the assignment of index partitions to nodes. While frozen, the Search index stops assigning partitions during index rebalancing and index definition updates. This endpoint is scoped and does not require a fully qualified `{INDEX_NAME}` value.

Produces

* application/json

##### [](#p-api-scoped-planfreezecontrol-parameters)Parameters

Path Parameters

| Name                     | Description                                                                                                                                                    | Schema |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **BUCKET\_NAME**required | The name of the bucket containing the Search index definition.                                                                                                 | String |
| **SCOPE\_NAME**required  | The name of the scope containing the Search index definition.                                                                                                  | String |
| **INDEX\_NAME**required  | The name of the Search index definition. **Pattern:** /^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$/                                                                       | String |
| **OP**required           | To freeze partition assignment, set {OP} to freeze. To unfreeze partition assignment on a frozen index, set {OP} to unfreeze. **Values:** "freeze", "unfreeze" | String |

##### [](#p-api-scoped-planfreezecontrol-responses)Responses

| HTTP Code | Description                                                        | Schema                               |
| --------- | ------------------------------------------------------------------ | ------------------------------------ |
| 200       | The Search Service returns a response that includes the status ok. | [Management Response](#MgmtResponse) |

##### [](#p-api-scoped-planfreezecontrol-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Manage](#security-Manage) |

##### [](#p-api-scoped-planfreezecontrol-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok"
}
```

#### [](#p-api-scoped-querycontrol)Stop Queries on an Index (Scoped)

POST /api/bucket/{BUCKET_NAME}/scope/{SCOPE_NAME}/index/{INDEX_NAME}/queryControl/{OP}

##### [](#p-api-scoped-querycontrol-description)Description

For the Search index specified in the endpoint URL, disallow or allow queries. While queries are disallowed, users see an error that the Search index's partitions could not be reached. This endpoint is scoped and does not require a fully qualified `{INDEX_NAME}` value.

Produces

* application/json

##### [](#p-api-scoped-querycontrol-parameters)Parameters

Path Parameters

| Name                     | Description                                                                                                                                                | Schema |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **BUCKET\_NAME**required | The name of the bucket containing the Search index definition.                                                                                             | String |
| **SCOPE\_NAME**required  | The name of the scope containing the Search index definition.                                                                                              | String |
| **INDEX\_NAME**required  | The name of the Search index definition. **Pattern:** /^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$/                                                                   | String |
| **OP**required           | To allow queries against a Search index, set {OP} to allow. To block queries against a Search index, set {OP} to disallow. **Values:** "allow", "disallow" | String |

##### [](#p-api-scoped-querycontrol-responses)Responses

| HTTP Code | Description                                                        | Schema                               |
| --------- | ------------------------------------------------------------------ | ------------------------------------ |
| 200       | The Search Service returns a response that includes the status ok. | [Management Response](#MgmtResponse) |

##### [](#p-api-scoped-querycontrol-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Manage](#security-Manage) |

##### [](#p-api-scoped-querycontrol-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok"
}
```

### [](#tag-Monitoring)Monitoring

Use the following endpoints to get statistics about Search indexes for monitoring and debugging.

[Get Index Status (Scoped)](#g-api-scoped-status)  
[Get Indexing and Data Metrics for All Indexes](#g-api-stats)  
[Get Indexing and Data Metrics for an Index](#g-api-stats-index-name)  
[Analyze Document](#g-api-stats-index-name-analyzeDoc)

#### [](#g-api-scoped-status)Get Index Status (Scoped)

GET /api/bucket/{BUCKET_NAME}/scope/{SCOPE_NAME}/index/{INDEX_NAME}/status

##### [](#g-api-scoped-status-description)Description

Returns the status of the Search index specified in the endpoint URL, including whether all index partitions are created and ready to use.

Produces

* application/json

##### [](#g-api-scoped-status-parameters)Parameters

Path Parameters

| Name                     | Description                                                                              | Schema |
| ------------------------ | ---------------------------------------------------------------------------------------- | ------ |
| **BUCKET\_NAME**required | The name of the bucket containing the Search index definition.                           | String |
| **SCOPE\_NAME**required  | The name of the scope containing the Search index definition.                            | String |
| **INDEX\_NAME**required  | The name of the Search index definition. **Pattern:** /^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$/ | String |

##### [](#g-api-scoped-status-responses)Responses

| HTTP Code | Description                                                        | Schema                             |
| --------- | ------------------------------------------------------------------ | ---------------------------------- |
| 200       | The Search Service returns a response that includes the status ok. | [Status Response](#StatusResponse) |

##### [](#g-api-scoped-status-security)Security

| Type         | Name                   |
| ------------ | ---------------------- |
| http (basic) | [Read](#security-Read) |

##### [](#g-api-scoped-status-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok",
  "indexStatus" : "Ready"
}
```

#### [](#g-api-stats)Get Indexing and Data Metrics for All Indexes

GET /api/stats

##### [](#g-api-stats-description)Description

Returns indexing and data-related metrics, timings, counters, and detailed partition information for all Search indexes, from the node running the Search Service.

This endpoint returns statistics provided by the Search service. For additional statistics, see [Get Query, Mutation, and Partition Statistics for the Search Service](../fts-rest-stats/index.html#g-api-nsstats).

Produces

* application/json

##### [](#g-api-stats-responses)Responses

| HTTP Code | Description                                         | Schema                                |
| --------- | --------------------------------------------------- | ------------------------------------- |
| 200       | A JSON object containing indexing and data metrics. | [Node Statistics](#StatsNodeResponse) |

##### [](#g-api-stats-security)Security

| Type         | Name                               |
| ------------ | ---------------------------------- |
| http (basic) | [Statistics](#security-Statistics) |

##### [](#g-api-stats-ex-response)Example HTTP Response

Response 200

```json
{
  "feeds" : {
    "myFirstIndex_6cc599ab7a85bf3b" : { }
  },
  "manager" : {
    "TotCreateIndex" : 1,
    "TotCreateIndexOk" : 1,
    "TotDeleteIndex" : 0,
    "TotDeleteIndexOk" : 0,
    "TotIndexControl" : 0,
    "TotIndexControlOk" : 0,
    "TotJanitorClosePIndex" : 0,
    "TotJanitorKick" : 2,
    "TotJanitorKickErr" : 0,
    "TotJanitorKickOk" : 2,
    "TotJanitorKickStart" : 2,
    "TotJanitorNOOP" : 0,
    "TotJanitorNOOPOk" : 0,
    "TotJanitorRemovePIndex" : 0,
    "TotJanitorSubscriptionEvent" : 0,
    "TotJanitorUnknownErr" : 0,
    "TotKick" : 0,
    "TotPlannerKick" : 2,
    "TotPlannerKickChanged" : 1,
    "TotPlannerKickErr" : 0,
    "TotPlannerKickOk" : 2,
    "TotPlannerKickStart" : 2,
    "TotPlannerNOOP" : 0,
    "TotPlannerNOOPOk" : 0,
    "TotPlannerSubscriptionEvent" : 0,
    "TotPlannerUnknownErr" : 0,
    "TotSaveNodeDef" : 2,
    "TotSaveNodeDefGetErr" : 0,
    "TotSaveNodeDefOk" : 2,
    "TotSaveNodeDefSame" : 0,
    "TotSaveNodeDefSetErr" : 0
  },
  "pindexes" : {
    "myFirstIndex_6cc599ab7a85bf3b_0" : null
  }
}
```

#### [](#g-api-stats-index-name)Get Indexing and Data Metrics for an Index

GET /api/stats/index/{INDEX_NAME}

##### [](#g-api-stats-index-name-description)Description

Returns indexing and data-related metrics, timings, counters, and detailed partition information for the Search index specified in the endpoint URL.

This endpoint returns statistics provided by the Search service. For additional statistics, see [Get Query, Mutation, and Partition Statistics for an Index](../fts-rest-stats/index.html#g-api-nsstats-index-name).

Produces

* application/json

##### [](#g-api-stats-index-name-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                                                                                                       | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **INDEX\_NAME**required | The name of the Search index definition. You must use the fully qualified name for the index, which includes the bucket and scope. To view the full, scoped name for an index for use with this endpoint: Go to the **Search** tab in the Couchbase Server Web Console. Point to the **Index Name** for an index. | String |

##### [](#g-api-stats-index-name-responses)Responses

| HTTP Code | Description                                                         | Schema                                  |
| --------- | ------------------------------------------------------------------- | --------------------------------------- |
| 200       | A JSON object containing statistics for the specified Search index. | [Index Statistics](#StatsIndexResponse) |

##### [](#g-api-stats-index-name-security)Security

| Type         | Name                               |
| ------------ | ---------------------------------- |
| http (basic) | [Statistics](#security-Statistics) |

##### [](#g-api-stats-index-name-ex-response)Example HTTP Response

Response 200

```json
{
  "feeds" : { },
  "pindexes" : {
    "travel-sample.inventory.travel-test_3858c70e4d4d8df9_4c1c5584" : {
      "pindexStoreStats" : {
        "TimerBatchStore" : {
          "count" : 0,
          "min" : 0,
          "max" : 0,
          "mean" : 0,
          "stddev" : 0,
          "percentiles" : {
            "99%" : 0,
            "99.9%" : 0,
            "median" : 0,
            "75%" : 0,
            "95%" : 0
          },
          "rates" : {
            "mean" : 0,
            "1-min" : 0,
            "5-min" : 0,
            "15-min" : 0
          }
        },
        "Errors" : [ ]
      },
      "bleveIndexStats" : {
        "index" : {
          "CurFilesIneligibleForRemoval" : 0,
          "CurOnDiskBytes" : 34007668,
          "CurOnDiskFiles" : 4,
          "CurRootEpoch" : 0,
          "LastMergedEpoch" : 44,
          "LastPersistedEpoch" : 44,
          "MaxBatchIntroTime" : 0,
          "MaxFileMergeZapIntroductionTime" : 0,
          "MaxFileMergeZapTime" : 0,
          "MaxMemMergeZapTime" : 0,
          "TotAnalysisTime" : 0,
          "TotBatchIntroTime" : 0,
          "TotBatches" : 0,
          "TotBatchesEmpty" : 0,
          "TotBytesReadAtQueryTime" : 294892,
          "TotBytesWrittenAtIndexTime" : 0,
          "TotDeletes" : 0,
          "TotEventTriggerCompleted" : 2,
          "TotEventTriggerStarted" : 2,
          "TotFileMergeForceOpsCompleted" : 0,
          "TotFileMergeForceOpsStarted" : 0,
          "TotFileMergeIntroductions" : 0,
          "TotFileMergeIntroductionsDone" : 0,
          "TotFileMergeIntroductionsObsoleted" : 0,
          "TotFileMergeIntroductionsSkipped" : 0,
          "TotFileMergeLoopBeg" : 2,
          "TotFileMergeLoopEnd" : 1,
          "TotFileMergeLoopErr" : 0,
          "TotFileMergePlan" : 1,
          "TotFileMergePlanErr" : 0,
          "TotFileMergePlanNone" : 1,
          "TotFileMergePlanOk" : 0,
          "TotFileMergePlanTasks" : 0,
          "TotFileMergePlanTasksDone" : 0,
          "TotFileMergePlanTasksErr" : 0,
          "TotFileMergePlanTasksSegments" : 0,
          "TotFileMergePlanTasksSegmentsEmpty" : 0,
          "TotFileMergeSegments" : 0,
          "TotFileMergeSegmentsEmpty" : 0,
          "TotFileMergeWrittenBytes" : 0,
          "TotFileMergeZapBeg" : 0,
          "TotFileMergeZapEnd" : 0,
          "TotFileMergeZapIntroductionTime" : 0,
          "TotFileMergeZapTime" : 0,
          "TotFileSegmentsAtRoot" : 1,
          "TotIndexTime" : 0,
          "TotIndexedPlainTextBytes" : 0,
          "TotIntroduceLoop" : 3,
          "TotIntroduceMergeBeg" : 0,
          "TotIntroduceMergeEnd" : 0,
          "TotIntroducePersistBeg" : 0,
          "TotIntroducePersistEnd" : 0,
          "TotIntroduceRevertBeg" : 0,
          "TotIntroduceRevertEnd" : 0,
          "TotIntroduceSegmentBeg" : 0,
          "TotIntroduceSegmentEnd" : 0,
          "TotIntroducedItems" : 0,
          "TotIntroducedSegmentsBatch" : 0,
          "TotIntroducedSegmentsMerge" : 0,
          "TotItemsToPersist" : 0,
          "TotMemMergeBeg" : 0,
          "TotMemMergeDone" : 0,
          "TotMemMergeErr" : 0,
          "TotMemMergeSegments" : 0,
          "TotMemMergeZapBeg" : 0,
          "TotMemMergeZapEnd" : 0,
          "TotMemMergeZapTime" : 0,
          "TotMemorySegmentsAtRoot" : 0,
          "TotOnErrors" : 0,
          "TotPersistLoopBeg" : 2,
          "TotPersistLoopEnd" : 1,
          "TotPersistLoopErr" : 0,
          "TotPersistLoopProgress" : 0,
          "TotPersistLoopWait" : 2,
          "TotPersistLoopWaitNotified" : 0,
          "TotPersistedItems" : 0,
          "TotPersistedSegments" : 0,
          "TotPersisterMergerNapBreak" : 1,
          "TotPersisterNapPauseCompleted" : 1,
          "TotPersisterSlowMergerPause" : 0,
          "TotPersisterSlowMergerResume" : 0,
          "TotSnapshotsRemovedFromMetaStore" : 0,
          "TotTermSearchersFinished" : 13,
          "TotTermSearchersStarted" : 13,
          "TotUpdates" : 0,
          "analysis_time" : 0,
          "batches" : 0,
          "deletes" : 0,
          "errors" : 0,
          "index_time" : 0,
          "num_bytes_read_at_query_time" : 294892,
          "num_bytes_used_disk" : 34007668,
          "num_bytes_used_disk_by_root" : 15644303,
          "num_bytes_used_disk_by_root_reclaimable" : 0,
          "num_bytes_written_at_index_time" : 0,
          "num_files_on_disk" : 4,
          "num_items_introduced" : 0,
          "num_items_persisted" : 0,
          "num_persister_nap_merger_break" : 1,
          "num_persister_nap_pause_completed" : 1,
          "num_plain_text_bytes_indexed" : 0,
          "num_recs_to_persist" : 0,
          "num_root_filesegments" : 1,
          "num_root_memorysegments" : 0,
          "term_searchers_finished" : 13,
          "term_searchers_started" : 13,
          "total_compaction_written_bytes" : 0,
          "updates" : 0
        },
        "search_time" : 40353204,
        "searches" : 1
      },
      "basic" : {
        "DocCount" : 917
      },
      "partitions" : { },
      "copyPartitionStats" : {
        "TotCopyPartitionStart" : 0,
        "TotCopyPartitionFinished" : 0,
        "TotCopyPartitionTimeInMs" : 0,
        "TotCopyPartitionFailed" : 0,
        "TotCopyPartitionRetries" : 0,
        "TotCopyPartitionErrors" : 0,
        "TotCopyPartitionSkipped" : 0,
        "TotCopyPartitionCancelled" : 0,
        "TotCopyPartitionOnHttp2" : 0
      }
    }
  }
}
```

#### [](#g-api-stats-index-name-analyzeDoc)Analyze Document

POST /api/index/{INDEX_NAME}/analyzeDoc

##### [](#g-api-stats-index-name-analyzeDoc-description)Description

Use the Search index specified in the endpoint URL to analyze a document from the request body.

Consumes

* application/json

Produces

* application/json

##### [](#g-api-stats-index-name-analyzeDoc-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                                                                                                       | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **INDEX\_NAME**required | The name of the Search index definition. You must use the fully qualified name for the index, which includes the bucket and scope. To view the full, scoped name for an index for use with this endpoint: Go to the **Search** tab in the Couchbase Server Web Console. Point to the **Index Name** for an index. | String |

Body Parameter

| Name             | Description                                      | Schema                |
| ---------------- | ------------------------------------------------ | --------------------- |
| **Body**required | Add any valid JSON document to the request body. | [\[Object\]](#Object) |

##### [](#g-api-stats-index-name-analyzeDoc-responses)Responses

| HTTP Code | Description                                                     | Schema                                 |
| --------- | --------------------------------------------------------------- | -------------------------------------- |
| 200       | A JSON object containing the analysis of the provided document. | [Document Analysis](#DocumentAnalysis) |

##### [](#g-api-stats-index-name-analyzeDoc-security)Security

| Type         | Name                   |
| ------------ | ---------------------- |
| http (basic) | [Read](#security-Read) |

##### [](#g-api-stats-index-name-analyzeDoc-ex-request)Example Request Body

```json
{
  "name" : "hello world",
  "title" : "couchbase blr"
}
```

##### [](#g-api-stats-index-name-analyzeDoc-ex-response)Example HTTP Response

[Response 200](#g-api-stats-index-name-analyzeDoc-ex-response-200) shows the result of analyzing the document from the [Example Request Body](#g-api-stats-index-name-analyzeDoc-ex-request) using a Search index with the following settings:

* A `keyword` analyzer for the `title` field.
* An `ngram` token filter with a `min` of 2 and a `max` of 5 for the `name` field.

Response 200

```json
{
  "status" : "ok",
  "analyzed" : [ {
    "couchbase blr" : {
      "Term" : "Y291Y2hiYXNlIGJscg==",
      "Locations" : [ {
        "Field" : "title",
        "ArrayPositions" : [ ],
        "Start" : 0,
        "End" : 13,
        "Position" : 1
      } ]
    }
  }, {
    "he" : {
      "Term" : "aGU=",
      "Locations" : [ {
        "Field" : "name",
        "ArrayPositions" : [ ],
        "Start" : 0,
        "End" : 5,
        "Position" : 1
      } ]
    },
    "hel" : {
      "Term" : "aGVs",
      "Locations" : [ {
        "Field" : "name",
        "ArrayPositions" : [ ],
        "Start" : 0,
        "End" : 5,
        "Position" : 1
      } ]
    },
    "hell" : {
      "Term" : "aGVsbA==",
      "Locations" : [ {
        "Field" : "name",
        "ArrayPositions" : [ ],
        "Start" : 0,
        "End" : 5,
        "Position" : 1
      } ]
    },
    "hello" : {
      "Term" : "aGVsbG8=",
      "Locations" : [ {
        "Field" : "name",
        "ArrayPositions" : [ ],
        "Start" : 0,
        "End" : 5,
        "Position" : 1
      } ]
    },
    "wo" : {
      "Term" : "d28=",
      "Locations" : [ {
        "Field" : "name",
        "ArrayPositions" : [ ],
        "Start" : 6,
        "End" : 11,
        "Position" : 2
      } ]
    },
    "wor" : {
      "Term" : "d29y",
      "Locations" : [ {
        "Field" : "name",
        "ArrayPositions" : [ ],
        "Start" : 6,
        "End" : 11,
        "Position" : 2
      } ]
    },
    "worl" : {
      "Term" : "d29ybA==",
      "Locations" : [ {
        "Field" : "name",
        "ArrayPositions" : [ ],
        "Start" : 6,
        "End" : 11,
        "Position" : 2
      } ]
    },
    "world" : {
      "Term" : "d29ybGQ=",
      "Locations" : [ {
        "Field" : "name",
        "ArrayPositions" : [ ],
        "Start" : 6,
        "End" : 11,
        "Position" : 2
      } ]
    }
  }, null ]
}
```

### [](#tag-Querying)Querying

Use the following endpoints to query the contents of a Search index.

[Get Document Count for an Index](#g-api-index-name-count)  
[Query a Search Index](#p-api-index-name-query)  
[Look Up the Index Partition for a Document (Scoped)](#p-api-pindex-lookup)  
[Query a Search Index (Scoped)](#p-api-scoped-query)

#### [](#g-api-index-name-count)Get Document Count for an Index

GET /api/index/{INDEX_NAME}/count

##### [](#g-api-index-name-count-description)Description

Returns the number of documents indexed in the specified Search index.

Produces

* application/json

##### [](#g-api-index-name-count-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                                                                                                       | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **INDEX\_NAME**required | The name of the Search index definition. You must use the fully qualified name for the index, which includes the bucket and scope. To view the full, scoped name for an index for use with this endpoint: Go to the **Search** tab in the Couchbase Server Web Console. Point to the **Index Name** for an index. | String |

##### [](#g-api-index-name-count-responses)Responses

| HTTP Code | Description                                                        | Schema                           |
| --------- | ------------------------------------------------------------------ | -------------------------------- |
| 200       | The Search Service returns a response that includes the status ok. | [Document Count](#DocumentCount) |

##### [](#g-api-index-name-count-security)Security

| Type         | Name                               |
| ------------ | ---------------------------------- |
| http (basic) | [Statistics](#security-Statistics) |

##### [](#g-api-index-name-count-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok",
  "count" : 285
}
```

#### [](#p-api-index-name-query)Query a Search Index

POST /api/index/{INDEX_NAME}/query

##### [](#p-api-index-name-query-description)Description

Run a query formatted as a JSON object against the Search index definition specified in the endpoint URL. The endpoint returns a JSON object as a response.

> [!NOTE]
> This endpoint is for legacy Search indexes and may be deprecated in a future release. Use [Query a Search Index (Scoped)](#p-api-scoped-query) instead.

Consumes

* application/json

Produces

* application/json

##### [](#p-api-index-name-query-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                                                                                                       | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **INDEX\_NAME**required | The name of the Search index definition. You must use the fully qualified name for the index, which includes the bucket and scope. To view the full, scoped name for an index for use with this endpoint: Go to the **Search** tab in the Couchbase Server Web Console. Point to the **Index Name** for an index. | String |

Body Parameter

| Name             | Description                                                                                                                                                                                                  | Schema                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| **Body**required | A JSON object to define the settings for your Search query. For more information about how to create a Search query JSON object, see [Search Request JSON Properties](../search/search-request-params.html). | [Query Request](#QueryRequest) |

##### [](#p-api-index-name-query-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                                       | Schema                           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| 200       | The response object has a status section that must be checked for every request. Under nearly all circumstances, the query response will be HTTP 200 even though individual index shards (partitions) may encounter a timeout or return an error. | [Query Response](#QueryResponse) |

##### [](#consistency-and-timeouts)Consistency and Timeouts

A query can specify a timeout value, a consistency requirement, or both. This section explains how this affects the query behavior and how to handle the resulting query return values.

* Logical first phase consistency wait — if timeout in this period, get 416 error with message saying request could not be satisfied.
* If consistency wait times out with 416, return value to client will indicate the sequence number range processed so the client will have an idea how far the processing got and has the option of retrying more intelligently.
* In phase 2, you have the normal pindex timeout. This will start whenever the first phase completes. At this point, request will return 200 HTTP response code unless there is an internal server error.
* The client must check response status, which returns any errors or timeouts for each pindex. If the response includes the number of errors, and the client can determine whether they need the complete results or can continue as long as enough pindexes return to give a reasonable user experience. The query return status is 200 even if all pindexes return errors, so it’s critical to check the response status and code accordingly.
* If the client sets timeout low, for example 1 ms, you may receive a 200 error with all timeouts instead of a consistency wait timeout.

##### [](#p-api-index-name-query-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Manage](#security-Manage) |

##### [](#p-api-index-name-query-ex-request)Example Request Body

The [Regular Query](#p-api-index-name-query-ex-request-0) request searches for the text `a sample query` in the documents included in the Search index.

The [Query with Options](#p-api-index-name-query-ex-request-1) request uses from/size for results paging, with `ctl` for a timeout and the `"at_plus"` consistency level. On consistency, the index must have incorporated at least mutation sequence-number 123 for partition (vbucket) 0 and mutation sequence-number 234 for partition (vbucket) 1, where vbucket 1 should have a `vbucketUUID` of `a0b1c2`.

The [Hybrid Query](#p-api-index-name-query-ex-request-2) request searches for a specified normalized color vector in `colorvect_dot`, but uses regular query parameters to limit the `brightness` value of the returned color to the range of `70-80`.

For more information about vector searches, see [Use Vector Search for AI Applications](../vector-search/vector-search.md).

Regular Query

```json
{
  "query" : {
    "query" : "a sample query",
    "boost" : 1
  },
  "size" : 10,
  "from" : 0,
  "highlight" : null,
  "fields" : null,
  "facets" : null,
  "explain" : false
}
```

Query with Options

```json
{
  "ctl" : {
    "timeout" : 10000,
    "consistency" : {
      "level" : "at_plus",
      "vectors" : {
        "customerIndex" : {
          "0" : 123,
          "1/a0b1c2" : 234
        }
      }
    }
  },
  "query" : {
    "query" : "alice smith",
    "boost" : 1
  },
  "size" : 10,
  "from" : 20,
  "highlight" : {
    "style" : null,
    "fields" : null
  },
  "fields" : [ "*" ],
  "facets" : null,
  "explain" : true
}
```

Hybrid Query

```json
{
  "fields" : [ "*" ],
  "query" : {
    "min" : 70,
    "max" : 80,
    "inclusive_min" : false,
    "inclusive_max" : true,
    "field" : "brightness"
  },
  "knn" : [ {
    "k" : 10,
    "field" : "colorvect_dot",
    "vector" : [ 0.707106781186548, 0, 0.707106781186548 ]
  } ],
  "size" : 10
}
```

#### [](#p-api-pindex-lookup)Look Up the Index Partition for a Document (Scoped)

POST /api/bucket/{BUCKET_NAME}/scope/{SCOPE_NAME}/index/{INDEX_NAME}/pindexLookup

##### [](#p-api-pindex-lookup-description)Description

Send a document ID in the request body and return the Search index partition ID where the document is stored. The endpoint returns a JSON object as a response.

Consumes

* application/json

Produces

* application/json

##### [](#p-api-pindex-lookup-parameters)Parameters

Path Parameters

| Name                     | Description                                                                              | Schema |
| ------------------------ | ---------------------------------------------------------------------------------------- | ------ |
| **BUCKET\_NAME**required | The name of the bucket containing the Search index definition.                           | String |
| **SCOPE\_NAME**required  | The name of the scope containing the Search index definition.                            | String |
| **INDEX\_NAME**required  | The name of the Search index definition. **Pattern:** /^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$/ | String |

Body Parameter

| Name             | Description                                                                                                                         | Schema                           |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **Body**required | A valid JSON object that contains the docID property, with a value that matches the document ID for a document in the Search index. | [Lookup Request](#LookupRequest) |

##### [](#p-api-pindex-lookup-responses)Responses

| HTTP Code | Description                                                        | Schema                             |
| --------- | ------------------------------------------------------------------ | ---------------------------------- |
| 200       | The Search Service returns a response that includes the status ok. | [Lookup Response](#LookupResponse) |

##### [](#p-api-pindex-lookup-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Manage](#security-Manage) |

##### [](#p-api-pindex-lookup-ex-request)Example Request Body

```json
{
  "docID" : "hotel_5848"
}
```

##### [](#p-api-pindex-lookup-ex-response)Example HTTP Response

Response 200

```json
{
  "status" : "ok",
  "pindexes" : {
    "travel-sample.inventory.travel-test" : {
      "id" : "travel-sample.inventory.travel-test_123294e5a4efbe39_4c1c5584"
    }
  }
}
```

#### [](#p-api-scoped-query)Query a Search Index (Scoped)

POST /api/bucket/{BUCKET_NAME}/scope/{SCOPE_NAME}/index/{INDEX_NAME}/query

##### [](#p-api-scoped-query-description)Description

Run a query formatted as a JSON object against the Search index definition specified in the endpoint URL. The endpoint returns a JSON object as a response. This endpoint is scoped and does not require a fully qualified `{INDEX_NAME}` value.

Consumes

* application/json

Produces

* application/json

##### [](#p-api-scoped-query-parameters)Parameters

Path Parameters

| Name                     | Description                                                                              | Schema |
| ------------------------ | ---------------------------------------------------------------------------------------- | ------ |
| **BUCKET\_NAME**required | The name of the bucket containing the Search index definition.                           | String |
| **SCOPE\_NAME**required  | The name of the scope containing the Search index definition.                            | String |
| **INDEX\_NAME**required  | The name of the Search index definition. **Pattern:** /^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$/ | String |

Body Parameter

| Name             | Description                                                                                                                                                                                                  | Schema                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| **Body**required | A JSON object to define the settings for your Search query. For more information about how to create a Search query JSON object, see [Search Request JSON Properties](../search/search-request-params.html). | [Query Request](#QueryRequest) |

##### [](#p-api-scoped-query-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                                       | Schema                           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| 200       | The response object has a status section that must be checked for every request. Under nearly all circumstances, the query response will be HTTP 200 even though individual index shards (partitions) may encounter a timeout or return an error. | [Query Response](#QueryResponse) |
| Default   | The Search Service returns a non-200 HTTP error code when a request fails.                                                                                                                                                                        |                                  |

##### [](#p-api-scoped-query-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Manage](#security-Manage) |

##### [](#p-api-scoped-query-ex-response)Example HTTP Response

Response 200

Success Response for a Regular Query

```json
{
  "status" : {
    "total" : 1,
    "failed" : 0,
    "successful" : 1
  },
  "request" : {
    "query" : {
      "conjuncts" : [ {
        "match" : "location",
        "field" : "reviews.content",
        "prefix_length" : 0,
        "fuzziness" : 0,
        "operator" : "or"
      }, {
        "match_phrase" : "nice view",
        "field" : "reviews.content"
      } ]
    },
    "size" : 10,
    "from" : 0,
    "highlight" : {
      "style" : "html",
      "fields" : [ "reviews.content" ]
    },
    "fields" : null,
    "facets" : null,
    "explain" : true,
    "sort" : [ "reviews.Ratings.Cleanliness", {
      "by" : "field",
      "field" : "reviews.Ratings.Cleanliness",
      "type" : "number"
    }, "-_score", "-_id" ],
    "includeLocations" : false,
    "score" : "none",
    "search_after" : null,
    "search_before" : null
  },
  "hits" : [ {
    "index" : "travel-sample.inventory.travel-test_53373d2948c55e82_4c1c5584",
    "id" : "hotel_7388",
    "score" : 0,
    "explanation" : {
      "value" : 0,
      "message" : "sum of:",
      "children" : [ {
        "value" : 0,
        "message" : "product of:",
        "children" : [ {
          "value" : 0,
          "message" : "sum of:",
          "children" : [ {
            "value" : 0,
            "message" : "weight(reviews.content:location^1.000000 in \u0000\u0000\u0000\u0000\u0000\u0000\u0003\n), product of:",
            "children" : [ {
              "value" : 0.5320504947307548,
              "message" : "queryWeight(reviews.content:location^1.000000), product of:",
              "children" : [ {
                "value" : 1,
                "message" : "boost"
              }, {
                "value" : 1.4291903588638628,
                "message" : "idf(docFreq=596, maxDocs=917)"
              }, {
                "value" : 0.3722740581273647,
                "message" : "queryNorm"
              } ]
            }, {
              "value" : 0,
              "message" : "fieldWeight(reviews.content:location in \u0000\u0000\u0000\u0000\u0000\u0000\u0003\n), product of:",
              "children" : [ {
                "value" : 0,
                "message" : "tf(termFreq(reviews.content:location)=0"
              }, {
                "value" : 0,
                "message" : "fieldNorm(field=reviews.content, doc=\u0000\u0000\u0000\u0000\u0000\u0000\u0003\n)"
              }, {
                "value" : 1.4291903588638628,
                "message" : "idf(docFreq=596, maxDocs=917)"
              } ]
            } ]
          } ]
        }, {
          "value" : 1,
          "message" : "coord(1/1)"
        } ]
      }, {
        "value" : 0,
        "message" : "sum of:",
        "children" : [ {
          "value" : 0,
          "message" : "weight(reviews.content:view^1.000000 in \u0000\u0000\u0000\u0000\u0000\u0000\u0003\n), product of:",
          "children" : [ {
            "value" : 0.6867550119496617,
            "message" : "queryWeight(reviews.content:view^1.000000), product of:",
            "children" : [ {
              "value" : 1,
              "message" : "boost"
            }, {
              "value" : 1.8447565629585312,
              "message" : "idf(docFreq=393, maxDocs=917)"
            }, {
              "value" : 0.3722740581273647,
              "message" : "queryNorm"
            } ]
          }, {
            "value" : 0,
            "message" : "fieldWeight(reviews.content:view in \u0000\u0000\u0000\u0000\u0000\u0000\u0003\n), product of:",
            "children" : [ {
              "value" : 0,
              "message" : "tf(termFreq(reviews.content:view)=0"
            }, {
              "value" : 0,
              "message" : "fieldNorm(field=reviews.content, doc=\u0000\u0000\u0000\u0000\u0000\u0000\u0003\n)"
            }, {
              "value" : 1.8447565629585312,
              "message" : "idf(docFreq=393, maxDocs=917)"
            } ]
          } ]
        }, {
          "value" : 0,
          "message" : "weight(reviews.content:nice^1.000000 in \u0000\u0000\u0000\u0000\u0000\u0000\u0003\n), product of:",
          "children" : [ {
            "value" : 0.4952674273751292,
            "message" : "queryWeight(reviews.content:nice^1.000000), product of:",
            "children" : [ {
              "value" : 1,
              "message" : "boost"
            }, {
              "value" : 1.3303839377539577,
              "message" : "idf(docFreq=658, maxDocs=917)"
            }, {
              "value" : 0.3722740581273647,
              "message" : "queryNorm"
            } ]
          }, {
            "value" : 0,
            "message" : "fieldWeight(reviews.content:nice in \u0000\u0000\u0000\u0000\u0000\u0000\u0003\n), product of:",
            "children" : [ {
              "value" : 0,
              "message" : "tf(termFreq(reviews.content:nice)=0"
            }, {
              "value" : 0,
              "message" : "fieldNorm(field=reviews.content, doc=\u0000\u0000\u0000\u0000\u0000\u0000\u0003\n)"
            }, {
              "value" : 1.3303839377539577,
              "message" : "idf(docFreq=658, maxDocs=917)"
            } ]
          } ]
        } ]
      } ]
    },
    "locations" : {
      "reviews.content" : {
        "location" : [ {
          "pos" : 312,
          "start" : 1641,
          "end" : 1649,
          "array_positions" : [ 4 ]
        } ],
        "nice" : [ {
          "pos" : 165,
          "start" : 840,
          "end" : 844,
          "array_positions" : [ 2 ]
        } ],
        "view" : [ {
          "pos" : 166,
          "start" : 845,
          "end" : 849,
          "array_positions" : [ 2 ]
        } ]
      }
    },
    "fragments" : {
      "reviews.content" : [ "…at&#39;s her name checked us in, very friendly and knowlegeable of the area. I would stay here again get area and right at the street car stop. nice resturants in walking distance. <mark>nice</mark> <mark>view</mark> of the city o…" ]
    },
    "sort" : [ "􏿿􏿿􏿿", "􏿿􏿿􏿿", "_score", "hotel_7388" ]
  }, "..." ],
  "total_hits" : 27,
  "cost" : 108906,
  "max_score" : 0,
  "took" : 14964461,
  "facets" : null
}
```

Success Response for a Hybrid Query

```json
{
  "status" : {
    "total" : 1,
    "failed" : 0,
    "successful" : 1
  },
  "request" : {
    "fields" : [ "*" ],
    "query" : {
      "match_none" : ""
    },
    "knn" : [ {
      "k" : 2,
      "field" : "colorvect_dot",
      "vector" : [ 0.707106781186548, 0, 0.707106781186548 ]
    } ]
  },
  "hits" : [ {
    "index" : "vector-sample.color.color-test_4d6a4a2f00f48fa2_4c1c5584",
    "id" : "#FF00FF",
    "score" : 0.9999999403953552,
    "sort" : [ "_score" ],
    "fields" : {
      "color" : "magenta / fuchsia"
    }
  }, {
    "index" : "vector-sample.color.color-test_4d6a4a2f00f48fa2_4c1c5584",
    "id" : "#B000B0",
    "score" : 0.9999999403953552,
    "sort" : [ "_score" ],
    "fields" : {
      "color" : "dark lavender"
    }
  } ],
  "total_hits" : 2,
  "cost" : 0,
  "max_score" : 0.9999999403953552,
  "took" : 4608572,
  "facets" : null
}
```

Default Response

```json
{
  "error" : "rest_index: Query, indexName: travel-sample.inventory.travel-test, err: bleve: QueryBleve parsing searchRequest, err: unknown query type",
  "request" : {
    "collections" : [ "hotel" ],
    "ctl" : {
      "consistency" : {
        "level" : "at_plus",
        "results" : "complete",
        "vectors" : {
          "searchIndexName" : {
            "607/205096593892159" : 2,
            "640/298739127912798" : 4
          }
        }
      },
      "timeout" : 10000
    },
    "explain" : true,
    "from" : 0,
    "highlight" : {
      "fields" : [ "reviews.content" ],
      "style" : "html"
    },
    "includeLocations" : false,
    "limit" : 10,
    "offset" : 0,
    "query" : { },
    "score" : "none",
    "size" : 10,
    "sort" : [ "reviews.Ratings.Cleanliness", {
      "by" : "field",
      "desc" : false,
      "field" : "reviews.Ratings.Cleanliness",
      "missing" : "last",
      "mode" : "default",
      "type" : "number"
    }, "-_score", "-_id" ]
  },
  "status" : "fail"
}
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Delete Response](#DeleteIndexResponse)  
[Document Analysis](#DocumentAnalysis)  
[Analysis Item](#DocumentAnalysisItem)  
[Analysis Token](#DocumentAnalysisItemToken)  
[Analysis Token Location](#DocumentAnalysisItemTokenLocation)  
[Document Count](#DocumentCount)  
[Index Response](#GetIndexResponse)  
[Plan Partition](#GetIndexResponsePIndex)  
[Partition Nodes Wrapper](#GetIndexResponsePIndexNodesWrapper)  
[Partition Node](#GetIndexResponsePIndexNodesWrapperNode)  
[Indexes Response](#GetIndexesResponse)  
[Index Definitions](#GetIndexesResponseIndexes)  
[Index Definitions Wrapper](#GetIndexesResponseIndexesWrapper)  
[Index Definition](#IndexDefinition)  
[Plan Parameters](#IndexDefinitionPlanParams)  
[Lookup Request](#LookupRequest)  
[Lookup Response](#LookupResponse)  
[Lookup Partition Wrapper](#LookupResponsePartitions)  
[Lookup Partition](#LookupResponsePartitionsID)  
[Management Response](#MgmtResponse)  
[Create or Update Response](#PutIndexResponse)  
[Query Request](#QueryRequest)  
[Query Response](#QueryResponse)  
[Index Statistics](#StatsIndexResponse)  
[Node Statistics](#StatsNodeResponse)  
[Manager Statistics](#StatsNodeResponseMgr)  
[Status Response](#StatusResponse)

### [](#DeleteIndexResponse)Delete Response

 Object

| Property           |                                                                                                                         | Schema |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------- | ------ |
| **status**optional | The status of the operation.                                                                                            | String |
| **uuid**optional   | The UUID of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial). | String |

### [](#DocumentAnalysis)Document Analysis

 Object

| Property             |                                                              | Schema                                       |
| -------------------- | ------------------------------------------------------------ | -------------------------------------------- |
| **status**optional   | The status of the operation.                                 | String                                       |
| **analyzed**optional | An array of objects containing the analysis of the document. | [Analysis Item](#DocumentAnalysisItem) array |

#### Analysis Item

 Object

| Property           |                                                                                                                                                      | Schema                                       |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| additionalproperty | An object containing the analysis of a single search term or token from the analyzed document. The name of the property is the search term or token. | [Analysis Token](#DocumentAnalysisItemToken) |

#### Analysis Token

 Object

| Property              |                                                                                           | Schema                                                              |
| --------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Term**optional      |                                                                                           | String                                                              |
| **Locations**optional | An array of objects describing the locations of the search term or token in the document. | [Analysis Token Location](#DocumentAnalysisItemTokenLocation) array |

#### Analysis Token Location

 Object

| Property                   |                                                      | Schema         |
| -------------------------- | ---------------------------------------------------- | -------------- |
| **Field**optional          | The field in the document where the token was found. | String         |
| **ArrayPositions**optional |                                                      | Any Type array |
| **Start**optional          | The starting point of the token in the field.        | Integer        |
| **End**optional            | The ending point of the token in the field.          | Integer        |
| **Position**optional       | The position of the token in the field.              | Integer        |

### [](#DocumentCount)Document Count

 Object

| Property           |                                             | Schema  |
| ------------------ | ------------------------------------------- | ------- |
| **status**optional | The status of the operation.                | String  |
| **count**optional  | The document count for the specified index. | Integer |

### [](#GetIndexResponse)Index Response

 Object

| Property                 |                                                                                                                                                  | Schema                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| **indexDef**optional     | The full Search index definition. For a detailed list of all parameters, see [Search Index JSON Properties](../search/search-index-params.html). | [Index Definition](#IndexDefinition)            |
| **planPIndexes**optional | An array of objects, each containing information about a single Search index partition.                                                          | [Plan Partition](#GetIndexResponsePIndex) array |
| **status**optional       | The status of the operation.                                                                                                                     | String                                          |
| **warnings**optional     | An array of warnings.                                                                                                                            | String array                                    |

#### Plan Partition

 Object

| Property                     |                                                                                                                                                         | Schema                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **indexName**optional        | The name of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                 | String                                                         |
| **indexParams**optional      | The Search index's type identifier, type mappings, and analyzers. For more information, see [Params Object](../search/search-index-params.html#params). | Object                                                         |
| **indexType**optional        | The type of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                 | String                                                         |
| **indexUUID**optional        | The UUID of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                 | String                                                         |
| **name**optional             | The name of the Search index partition.                                                                                                                 | String                                                         |
| **nodes**optional            | An object containing information about 1 or more Search index partition nodes.                                                                          | [Partition Nodes Wrapper](#GetIndexResponsePIndexNodesWrapper) |
| **sourceName**optional       | The name of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).      | String                                                         |
| **sourceParams**optional     | Advanced settings for Search index behavior. For more information, see [Initial Settings](../search/search-index-params.html#initial).                  | Object                                                         |
| **sourcePartitions**optional |                                                                                                                                                         | String                                                         |
| **sourceType**optional       | The type of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).      | String                                                         |
| **sourceUUID**optional       | The UUID of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).      | String                                                         |
| **uuid**optional             | The UUID of the Search index partition.                                                                                                                 | String                                                         |

#### Partition Nodes Wrapper

 Object

| Property           |                                                                                                                         | Schema                                                    |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| additionalproperty | An object containing information about a single Search index partition node. The name of the property is the node UUID. | [Partition Node](#GetIndexResponsePIndexNodesWrapperNode) |

#### Partition Node

 Object

| Property             |  | Schema  |
| -------------------- |  | ------- |
| **canRead**optional  |  | Boolean |
| **canWrite**optional |  | Boolean |
| **priority**optional |  | Integer |

### [](#GetIndexesResponse)Indexes Response

 Object

| Property              |                                                                        | Schema                                          |
| --------------------- | ---------------------------------------------------------------------- | ----------------------------------------------- |
| **indexDefs**optional | An object containing Search index definitions and related information. | [Index Definitions](#GetIndexesResponseIndexes) |
| **status**optional    | The status of the operation.                                           | String                                          |

#### Index Definitions

 Object

| Property                |                                                          | Schema                                                         |
| ----------------------- | -------------------------------------------------------- | -------------------------------------------------------------- |
| **implVersion**optional |                                                          | String                                                         |
| **indexDefs**optional   | An object containing 1 or more Search index definitions. | [Index Definitions Wrapper](#GetIndexesResponseIndexesWrapper) |
| **uuid**optional        |                                                          | String                                                         |

#### Index Definitions Wrapper

 Object

| Property           |                                                                                                                                                  | Schema                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| additionalproperty | The full Search index definition. For a detailed list of all parameters, see [Search Index JSON Properties](../search/search-index-params.html). | [Index Definition](#IndexDefinition) |

### [](#IndexDefinition)Index Definition

 Object

| Property                  |                                                                                                                                                                  | Schema                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **name**required          | The name of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                          | String                                        |
| **type**required          | The type of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                          | String                                        |
| **sourceName**required    | The name of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).               | String                                        |
| **sourceUUID**optional    | The UUID of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).               | String                                        |
| **sourceParams**optional  | Advanced settings for Search index behavior. For more information, see [Initial Settings](../search/search-index-params.html#initial).                           | Object                                        |
| **sourceType**required    | The type of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).               | String                                        |
| **params**required        | The Search index's type identifier, type mappings, and analyzers. For more information, see [Params Object](../search/search-index-params.html#params).          | Object                                        |
| **planParams**required    | The Search index's partitioning and replication settings. For more information, see [Plan Params Object](../search/search-index-params.html#planParams).         | [Plan Parameters](#IndexDefinitionPlanParams) |
| **prevIndexUUID**optional | The UUID of the previous index. Intended for clients that want to check that they are not overwriting the Search index definition updates of concurrent clients. | String                                        |
| **uuid**optional          | The UUID of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                          | String                                        |

#### Plan Parameters

 Object

| Property                           |                                                                                                                                                | Schema  |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **hierarchyRules**optional         | **Nullable:** yes                                                                                                                              | String  |
| **maxPartitionsPerPIndex**optional | This setting is deprecated. Use indexPartitions instead.                                                                                       | Integer |
| **indexPartitions**optional        | The number of partitions to split the Search index into, across the nodes you have available in your database with the Search Service enabled. | Integer |
| **nodePlanParams**optional         | **Nullable:** yes                                                                                                                              | String  |
| **numReplicas**optional            | The number of replicas the Search Service creates for the Search index to ensure high availability.                                            | Integer |
| **planFrozen**optional             |                                                                                                                                                | Boolean |

### [](#LookupRequest)Lookup Request

 Object

| Property          |                                                 | Schema |
| ----------------- | ----------------------------------------------- | ------ |
| **docID**optional | The document ID to look up in the Search index. | String |

### [](#LookupResponse)Lookup Response

 Object

| Property             |                                                                           | Schema                                                |
| -------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------- |
| **status**optional   | The status of the operation.                                              | String                                                |
| **pindexes**optional | An object containing information about 1 or more Search index partitions. | [Lookup Partition Wrapper](#LookupResponsePartitions) |

#### Lookup Partition Wrapper

 Object

| Property           |                                                                                                                                      | Schema                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| additionalproperty | An object containing information about a single Search index partition. The name of the property is the Search index partition name. | [Lookup Partition](#LookupResponsePartitionsID) |

#### Lookup Partition

 Object

| Property       |                                | Schema |
| -------------- | ------------------------------ | ------ |
| **id**optional | The Search index partition ID. | String |

### [](#MgmtResponse)Management Response

 Object

| Property           |                              | Schema |
| ------------------ | ---------------------------- | ------ |
| **status**optional | The status of the operation. | String |

### [](#PutIndexResponse)Create or Update Response

 Object

| Property           |                                                                                                                         | Schema |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------- | ------ |
| **status**optional | The status of the operation.                                                                                            | String |
| **name**optional   | The name of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial). | String |
| **uuid**optional   | The UUID of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial). | String |

### [](#QueryRequest)Query Request

 Object

| Property                     |                                                                                                                                                                                  | Schema         |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **query**optional            | An object that contains the properties for one of the supported query types. For more information, see [Query Object](../search/search-request-params.html#query-object).        | Object         |
| **knn**optional              | An array that contains objects that describe a Vector Search query. For more information, see [Knn Objects](../search/search-request-params.html#knn-object).                    | Object array   |
| **ctl**optional              | An object that contains properties for query consistency. For more information, see [Ctl Object](../search/search-request-params.html#ctl).                                      | Object         |
| **size**optional             | Set the total number of results to return for a single page of search results.                                                                                                   | Integer        |
| **from**optional             | Set an offset value to change where pagination starts for search results.                                                                                                        | Integer        |
| **highlight**optional        | Contains properties to control search result highlighting. For more information, see [Highlight Objects](../search/search-request-params.html#highlight).                        | Object         |
| **fields**optional           | An array of strings to specify each indexed field you want to return in search results.                                                                                          | String array   |
| **facets**optional           | Contains nested objects to define each facet you want to return with search results. For more information, see [Facet Objects](../search/search-request-params.html#facet-name). | Object         |
| **explain**optional          | Whether to create an explanation for a search result's score in search results.                                                                                                  | Boolean        |
| **sort**optional             | Contains an array of strings or JSON objects to set how to sort search results. For more information, see [Sort Object](../search/search-request-params.html#sort).              | Any Type array |
| **includeLocations**optional | Whether to return the position of each occurrence of a search term inside a document.                                                                                            | Boolean        |
| **score**optional            | Whether to include document relevancy scoring in search results.                                                                                                                 | String         |
| **search\_after**optional    | Use to control pagination in search results.                                                                                                                                     | String array   |
| **search\_before**optional   | Use to control pagination in search results.                                                                                                                                     | String array   |
| **collections**optional      | An array of strings that specify the collections where you want to run the query.                                                                                                | String array   |

### [](#QueryResponse)Query Response

 Object

| Property            |                                  | Schema       |
| ------------------- | -------------------------------- | ------------ |
| **status**optional  | The status of the operation.     | String       |
| **results**optional | The results of the Search query. | Object array |

### [](#StatsIndexResponse)Index Statistics

 Object

| Property             |  | Schema |
| -------------------- |  | ------ |
| **feeds**optional    |  | Object |
| **pindexes**optional |  | Object |

### [](#StatsNodeResponse)Node Statistics

 Object

| Property             |  | Schema                                      |
| -------------------- |  | ------------------------------------------- |
| **feeds**optional    |  | Object                                      |
| **manager**optional  |  | [Manager Statistics](#StatsNodeResponseMgr) |
| **pindexes**optional |  | Object                                      |

#### Manager Statistics

 Object

| Property                           |  | Schema  |
| ---------------------------------- |  | ------- |
| **TotCreateIndex**optional         |  | Integer |
| **TotDeleteIndex**optional         |  | Integer |
| **TotUpdateIndex**optional         |  | Integer |
| **TotBatchIntro**optional          |  | Integer |
| **TotBatchIntroFail**optional      |  | Integer |
| **TotBatchUpdate**optional         |  | Integer |
| **TotBatchUpdateFail**optional     |  | Integer |
| **TotBatchDelete**optional         |  | Integer |
| **TotBatchDeleteFail**optional     |  | Integer |
| **TotBatchGet**optional            |  | Integer |
| **TotBleveDestStart**optional      |  | Integer |
| **TotBleveDestStop**optional       |  | Integer |
| **TotBleveDestRemove**optional     |  | Integer |
| **TotBleveDestUpdate**optional     |  | Integer |
| **TotBleveDestUpdateFail**optional |  | Integer |
| **TotBleveDestIntro**optional      |  | Integer |
| **TotBleveDestIntroFail**optional  |  | Integer |
| **TotBleveDestBatch**optional      |  | Integer |
| **TotBleveDestBatchFail**optional  |  | Integer |
| **TotBleveDestDelete**optional     |  | Integer |
| **TotBleveDestDeleteFail**optional |  | Integer |
| **TotBleveDestClose**optional      |  | Integer |
| **TotBleveDestCloseFail**optional  |  | Integer |
| **TotQuery**optional               |  | Integer |
| **TotQueryFail**optional           |  | Integer |

### [](#StatusResponse)Status Response

 Object

| Property                |                                 | Schema |
| ----------------------- | ------------------------------- | ------ |
| **status**optional      | The status of the operation.    | String |
| **indexStatus**optional | The status of the Search index. | String |

## [](#security)Security

The Search REST APIs support HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-Manage)Manage

You must have the **Search Admin** role, with `cluster.bucket[$BUCKET_NAME].fts!manage` permissions on the required bucket.

**Type:** http

### [](#security-Statistics)Statistics

You must have the **Search Admin** role, with `cluster.bucket[$BUCKET_NAME].stats!read` permissions on the required bucket.

**Type:** http

### [](#security-Read)Read

You must have the **Search Reader** or **Search Admin** role, with `cluster.bucket[$BUCKET_NAME].fts!read` permissions on the required bucket.

**Type:** http

### [](#security-Write)Write

You must have the **Search Admin** role, with `cluster.bucket[$BUCKET_NAME].fts!write` permissions on the required bucket.

**Type:** http

For more information, see [Roles](../learn/security/roles.md).