---
title: Annotation Documentation
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.5/modules/ROOT/pages/reference-annotations.adoc
  xref: xref:2.5@operator::reference-annotations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/reference-annotations.html)

# Annotation Documentation

> Couchbase Operator uses special annotations to configure specific resources. 

## [](#history-retention)History Retention

### [](#bucket)Bucket

```yaml
apiVersion: v2
kind: CouchbaseBucket
metadata:
  name: "my-bucket"
  annotations:
    cao.couchbase.com/historyRetention.seconds: "1000"
    cao.couchbase.com/historyRetention.bytes: "2147483648"
    cao.couchbase.com/historyRetention.collectionHistoryDefault: "true"
spec:
  storageBackend: magma
  memoryQuota: 1024Mi
  evictionPolicy: valueOnly
```

#### [](#cao-couchbase-comhistoryretention-seconds)`cao.couchbase.com/historyRetention.seconds`

Used for configuring history retention time for a bucket. This parameter is parsed into an integer and defines how many seconds of history an individual vbucket should aim to retain on disk. Defaults to `0`, and can be altered after bucket creation. This annotation is only supported on buckets with `couchbasebuckets.spec.storageBackend=magma`.

#### [](#cao-couchbase-comhistoryretention-bytes)`cao.couchbase.com/historyRetention.bytes`

Used for configuring history retention size for a bucket. This parameter is parsed into an integer and defines how many bytes of history an individual vbucket should aim to retain on disk. Defaults to `0` and has a minimum working value of `2147483648`. Can be altered after bucket creation. Only supported on buckets with `couchbasebuckets.spec.storageBackend=magma`. This annotation is only supported on buckets with `couchbasebuckets.spec.storageBackend=magma`.

#### [](#cao-couchbase-comhistoryretention-collectionhistorydefault)`cao.couchbase.com/historyRetention.collectionHistoryDefault`

Used for configuring whether history retention is enabled for a collection by default. This parameter sets whether history retention is enabled by default on newly created collections. Defaults to `true`, and accepts `true` or `false`. This field can be altered after bucket creation. This annotation is only supported on buckets with `couchbasebuckets.spec.storageBackend=magma`.

### [](#collection)Collection

```yaml
apiVersion: v2
kind: CouchbaseCollection
metadata:
  name: "my-collection"
  annotations:
    cao.couchbase.com/history: "true"
```

#### [](#cao-couchbase-comhistory)`cao.couchbase.com/history`

Used for enabling/disabling history retention at collection creation time. This parameter is used to enable/disable history retention when a new collection is being created. Any changes to this field once the collection has been created will be ignored. Accepts a either `true` or `false` and defaults to the bucket level `collectionHistoryDefault`.