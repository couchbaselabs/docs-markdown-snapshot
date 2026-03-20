---
title: Managing Sample Buckets
description: Couchbase Server offers several sample buckets you can install for
  development and testing.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-sample-buckets.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:rest-api:rest-sample-buckets.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/rest-api/rest-sample-buckets.html)

# Managing Sample Buckets

## [](#description)Description

Couchbase Server offers several sample buckets you can install for development and testing.

## [](#http-methods-and-uris)HTTP Methods and URIs

GET /sampleBuckets

POST /sampleBuckets/install

## [](#description-2)Description

Gets the list of sample buckets available in Couchbase Server and installs one or more sample buckets.

## [](#curl-syntax)Curl Syntax

```console
curl -X GET -u USERNAME:PASSWORD
  http://NODE_NAME_OR_IP:PORT/sampleBuckets

curl -X POST -u USERNAME:PASSWORD
  http://NODE_NAME_OR_IP:PORT/sampleBuckets/install
  -d '[ "SAMPLE_BUCKET_NAME", ... ]'
```

* **`NODENAME_OR_IP`**: a node in the cluster.
* **`"SAMPLE_BUCKET_NAME"`**: the name of a sample bucket, specified as a string. You can provide a comma separated list of sample buckets to install.

## [](#responses)Responses

If the GET succeeds, it returns `200 OK` and a JSON object describing available sample buckets.

If the POST succeeds, it returns `200 OK` and a JSON array containing information about the tasks Couchbase Server started to load the buckets.

For either endpoint, an incorrectly specified bucket-name or URI gives `404 Object Not Found`; and failure to authenticate gives `401 Unauthorized`.

Calling the POST endpoint to install one or more sample buckets that are already installed returns a list containing a message for each error; such as `["Sample bucket travel-sample is already loaded.","Sample bucket beer-sample is already loaded."]`.

## [](#examples)Examples

The following example retrieves a list of the currently available sample buckets. Note that the output is piped to the [jq](https://https://stedolan.github.io/jq/) program, to facilitate readability.

```console
curl -X GET -u Administrator:password \
http://10.143.194.101:8091/sampleBuckets | jq
```

If successful, the call returns output similar to the following:

```json
[
  {
    "name": "beer-sample",
    "installed": false,
    "quotaNeeded": 104857600
  },
  {
    "name": "gamesim-sample",
    "installed": false,
    "quotaNeeded": 104857600
  },
  {
    "name": "travel-sample",
    "installed": false,
    "quotaNeeded": 104857600
  }
]
```

The output lists the available sample buckets and whether it’s installed and the memory required to install the bucket.

> [!NOTE]
> the `quotaNeeded` value is the minimum that Couchbase Server must have available. The sample bucket might not consume this entire value when you install it.

The following example installs the `travel-sample` and `beer-sample` sample buckets:

```console
curl -X POST -u Administrator:password \
     http://localhost:8091/sampleBuckets/install \
     -d '["travel-sample", "beer-sample"]' | jq .
```

If successful, the call returns a JSON array containing the tasks that Couchbase Server started to load the buckets:

```json
{
  "tasks": [
    {
      "taskId": "439b29de-0018-46ba-83c3-d3f58be68b12",
      "sample": "beer-sample",
      "bucket": "beer-sample"
    },
    {
      "taskId": "ed6cd88e-d704-4f91-8dd3-543e03669024",
      "sample": "travel-sample",
      "bucket": "travel-sample"
    }
  ]
}
```

You can monitor the status of these tasks by calling the `/pools/default/tasks` REST API endpoint. See [Getting Cluster Tasks](rest-get-cluster-tasks.md) for more information.

## [](#see-also)See Also

* For an overview of sample buckets, see [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).
* [Deleting Buckets](rest-bucket-delete.md) explains deleting buckets using the REST-API.
* [Sample Buckets](../manage/manage-settings/install-sample-buckets.md) explains how to load sample buckets using the Couchbase Server Web Console.