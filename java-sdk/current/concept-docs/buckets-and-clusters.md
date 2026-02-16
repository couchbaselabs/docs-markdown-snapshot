[View original HTML](/java-sdk/current/concept-docs/buckets-and-clusters.html)

> The Couchbase Java SDK provides an API for managing a Couchbase cluster programmatically. 

The primary means for managing clusters is through the [Couchbase Web UI](../../../server/current/manage/manage-buckets/bucket-management-overview.md) which provides an easy to use interface for adding, removing, monitoring, and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The SDK also comes with some convenience functionality for common Couchbase management requests — see the [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md) guide.

Management operations in the Java SDK may be performed through several interfaces depending on the object:

## [](#creating-and-removing-buckets)Creating and Removing Buckets

To create or delete a bucket, call the bucket manager with the `buckets()` call on the cluster:

```java
Unresolved include directive in modules/concept-docs/pages/buckets-and-clusters.adoc - include::example$BucketsAndClustersExample.java[]
```

This class is also used to expose information about an existing bucket (`manager.getBucket(string)`) or to update an existing bucket (`manager.updateBucket(bucketSettings)`).

The default Collection & Default Scope will be used automatically.