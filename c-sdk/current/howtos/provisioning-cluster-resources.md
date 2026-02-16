[View original HTML](/c-sdk/current/howtos/provisioning-cluster-resources.html)

> Provisioning cluster resources is managed at the collection or bucket level, depending upon the service affected. Common use cases are outlined here, less common use cases are covered in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/). 

|  | Managing Capella Clusters This part of the SDK API predates the Capella Management API, and is only intended to work with self-managed Couchbase Server clusters. Management of your Capella Operational cluster is available away from the Web UI with the [Capella Management API](../../../cloud/management-api-guide/management-api-intro.md). |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The primary means for managing clusters is through the Couchbase Web UI which provides an easy to use interface for adding, removing, monitoring and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The C SDK also comes with some convenience functionality for common Couchbase management requests.

|  | When using a Couchbase version earlier than 6.5, you must create a valid Bucket connection before you can use cluster level managers. |
|  | ------------------------------------------------------------------------------------------------------------------------------------- |

## [](#creating-and-removing-buckets)Creating and Removing Buckets

The `ClusterManager` interface may be used to create and delete buckets from the Couchbase cluster. It is instantiated through the `lcb_create()` method — see the bucket creation example [here](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/management-bucket-create.cc).

And the [dropping bucket example](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/management-bucket-drop.cc).

|  | Note that any property that is not explicitly set when building the bucket settings will use the default value. In the case of the update, this is not necessarily the currently configured value, so you should be careful to set all properties to their correct expected values when updating an existing bucket configuration. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#flushing-buckets)Flushing Buckets

When a bucket is flushed, all content is removed. Because this operation is potentially dangerous it is disabled by default for each bucket. Bucket flushing may be useful in test environments where it becomes a simpler alternative to removing and creating a test bucket. You may enable bucket flushing on a per-bucket basis using the Couchbase Web Console or when creating a bucket.

You can flush a bucket in the SDK by using the [lcb\_cbflush3() method](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/group%5F%5Flcb-flush.html).

The `lcb_cbflush3()` operation may fail if the bucket does not have flush enabled, in that case it will return an `ErrBucketNotFlushable`.

See the example [here](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/management-bucket-flush.cc).