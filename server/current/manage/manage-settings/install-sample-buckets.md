[View original HTML](/server/current/manage/manage-settings/install-sample-buckets.html)

> You can install buckets containing example scopes, collections, and documents that you can experiment with. 

## [](#configuring-sample-buckets)Sample Buckets

Full and Cluster administrators can install sample buckets using the [Couchbase Server Web Console](#install-sample-buckets-with-the-ui) and the [REST API](#install-sample-buckets-with-the-rest-api).

### [](#scopes-collection-and-sample-buckets)Scopes, Collections, and Sample Buckets

[Scopes and Collections](../../learn/data/scopes-and-collections.md) let you organize data within a bucket by type. The `beer-sample` and `gamesim-sample` sample buckets store all of their data in the default scope. The `travel-sample` bucket contains data in six scopes in addition to the `_default` scope. These additional scopes define several collections. The `inventory` scope has collections that organize travel data such as airlines and airports. The data within the `tenant_agent_00` through `tenant_agent_04` scopes let you experiment with multi-tenancy applications.

|  | The \_default scope of the travel\_sample bucket duplicates all of the data stored in the inventory and tenant\_agent\_00 through tenant\_agent\_04 scopes. This duplication makes the bucket compatible with scripts and applications written for versions of Couchbase Server earlier than 7.0 that did not support scopes and collections. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#install-sample-buckets-with-the-ui)Install Sample Buckets with the UI

From the **Settings** screen, select the **Sample Buckets** tab. The **Sample Buckets** screen now appears, as follows:

![settings samples](../_images/manage-settings/settings-samples.png) 

If one or more sample buckets are already loaded, they’re listed under the **Installed Samples** section of the page.

See [Manage Users and Roles](../manage-security/manage-users-and-roles.md) to learn how to assign roles to users to grant access to the sample buckets.

To install, select one or more sample buckets from the displayed list, using the checkboxes provided. For example, select the `travel-sample` bucket:

![select travel sample bucket](../_images/manage-settings/select-travel-sample-bucket.png) 

If there is insufficient memory available for the specified installation, a notification appears at the lower left of Couchbase Web Console:

![insufficientRamWarning](../_images/manage-settings/insufficientRamWarning.png) 

For information about configuring memory quotas, see [General](general-settings.md) settings. For information about managing (including deleting) buckets, see [Manage Buckets](../manage-buckets/bucket-management-overview.md).

If and when you have sufficient memory, click **Load Sample Data**.

![loadSampleDataButton](../_images/manage-settings/loadSampleDataButton.png) 

When installed, the sample bucket is listed under the **Installed Samples** section of the page. It also appears in the **Buckets** screen, where its definition can be edited. See [Manage Buckets](../manage-buckets/bucket-management-overview.md), for information.

## [](#install-sample-buckets-with-the-rest-api)Install Sample Buckets with the REST API

To install sample buckets with the REST API, use the `POST /sampleBuckets/install` HTTP method and URI. For example:

```console
curl -X POST -u Administrator:password \
     http://localhost:8091/sampleBuckets/install \
     -d '["travel-sample", "beer-sample"]' | jq .
```

If successful, the call returns a JSON dictionary that lists the tasks Couchbase Server started to load the buckets:

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

You can monitor the status of these tasks using the `/pools/default/tasks` REST API endpoint. Pass it the `taskId` value from the task list returned by the call to `sampleBuckets/install`:

```console
curl -s -u Administrator:password  -G http://localhost:8091/pools/default/tasks \
     -d taskId=439b29de-0018-46ba-83c3-d3f58be68b12 | jq '.'
```

The command returns the current status of the task:

```json
[
    {
      "task_id": "439b29de-0018-46ba-83c3-d3f58be68b12",
      "status": "running",
      "type": "loadingSampleBucket",
      "bucket": "beer-sample",
      "bucket_uuid": "not_present"
    }
]
```

For more information about using the REST API, including details of how to retrieve a list of available sample buckets, see [Managing Sample Buckets](../../rest-api/rest-sample-buckets.md). For information about deleting buckets (including sample buckets), see [Deleting Buckets](../../rest-api/rest-bucket-delete.md).