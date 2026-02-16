[View original HTML](/go-sdk/2.10/concept-docs/buckets-and-clusters.html)

> The Couchbase Go SDK provides an API for managing a Couchbase cluster programmatically. 

The primary means for managing clusters is through the [Couchbase Web UI](#7.1@server:manage:manage-buckets/bucket-management-overview.adoc) which provides an easy to use interface for adding, removing, monitoring, and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The SDK also comes with some convenience functionality for common Couchbase management requests — see the [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md) guide.

Management operations in the Go SDK may be performed through several interfaces depending on the object:

## [](#creating-and-removing-buckets)Creating and Removing Buckets

To create or delete a bucket, call the bucket manager with the `Buckets()` call on the cluster:

```golang
bucketMgr := cluster.Buckets()
createBucketSettings := gocb.CreateBucketSettings{
	BucketSettings: gocb.BucketSettings{
		Name:                 "myBucket",
		RAMQuotaMB:           150,
		BucketType:           gocb.CouchbaseBucketType,
	},
}
if err := bucketMgr.CreateBucket(createBucketSettings, &gocb.CreateBucketOptions{}); err != nil {
	panic(err)
}
```

This class is also used to expose information about an existing bucket (`manager.GetBucket(string, *gocb.GetBucketOptions)`) or to update an existing bucket (`manager.UpdateBucket(gocb.BucketSettings, *gocb.UpdateBucketOptions)`).

The default Collection & Default Scope will be used automatically.