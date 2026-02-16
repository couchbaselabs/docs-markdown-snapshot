[View original HTML](/operator/2.8/whats-new.html)

Autonomous Operator 2.8 introduces our new Cluster Migration functionality well as a number of other improvements and minor fixes.

## [](#cluster-migration)Cluster Migration

Cluster Migration allows you to transfer a currently-unmanaged Couchbase Server cluster over to being managed by the Operator, with zero downtime.

See [Couchbase Cluster Migration](concept-migration.md) for more details.

## [](#admission-controller-improvements)Admission Controller Improvements

The Dynamic Admission Controller (DAC) will now warn if any cluster settings don’t match our [Best Practices for Production Deployments](best-practices.md#production-deployments).

The DAC will now prevent changes to the `CouchbaseCluster` spec while a hibernation is taking place. If hibernation is enabled while a cluster is migrating, upgrading, scaling, or rebalancing, that process will conclude before the cluster enters hibernation. The DAC will warn when this is the case, and it will be visible in the operator logs.

To prevent any invalid resources failing to reconcile (i.e. if the DAC is not deployed in the current environment), the DAC Validation is now run at the beginning of the reconciliation loop. Any invalid resources will be skipped for reconciliation, marked as `NotValid`, and logged.

## [](#miscellaneous-improvements)Miscellaneous Improvements

* Pod Disruption Budgets can now be set per-Server Class by enabling [couchbaseclusters.spec.perServiceClassPDB](resource/couchbasecluster.md#couchbaseclusters-spec-perserviceclasspdb).
* Sample Buckets can now be loaded via the [CouchbaseBucket](resource/couchbasebucket.md) resource, by using the [cao.couchbase.com/sampleBucket](reference-annotations.md#cao-couchbase-comsamplebucket) annotation.
* Query-related RBAC roles (`query_use_sequential_scans`, `query_use_sequences`, and `query_manage_sequences`) have now been added to [couchbasegroups.spec.roles.name](resource/couchbasegroup.md#couchbasegroups-spec-roles-name).