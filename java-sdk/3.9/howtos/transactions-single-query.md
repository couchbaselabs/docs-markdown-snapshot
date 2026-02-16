[View original HTML](/java-sdk/3.9/howtos/transactions-single-query.html)

> Learn how to perform bulk-loading transactions with the SDK. 

Single query transactions can be useful if you need to do large, bulk-loading transactions.

The Query service maintains where required some in-memory state for each document in a transaction, that is freed on commit or rollback. For most use-cases this presents no issue, but there are some workloads, such as bulk loading many documents, where this could exceed the server resources allocated to the service. Solutions to this include breaking the workload up into smaller batches, and allocating additional memory to the Query service. Alternatively, single query transaction, described here, may be used.

Single query transactions have these characteristics:

* They have greatly reduced memory usage inside the Query service.
* As the name suggests, they consist of exactly one query, and no key-value operations.

You will see reference elsewhere in Couchbase documentation to the `tximplicit` query parameter. Single query transactions internally are setting this parameter. In addition, they provide automatic error and retry handling.

```java
try {
    var result = cluster.query(bulkLoadStatement, QueryOptions.queryOptions().asTransaction());
} catch (TransactionCommitAmbiguousException e) {
    throw logCommitAmbiguousError(e);
} catch (TransactionFailedException e) {
    throw logFailure(e);
} catch (CouchbaseException e) {
    // Any standard query errors can be raised here too, such as ParsingFailureException.  In these cases the
    // transaction definitely did not reach commit point.
    logger.warning("Transaction did not reach commit point");
    throw e;
}
```

You can also run a single query transaction against a particular `Scope` (these examples will exclude the full error handling for brevity):

```java
Bucket travelSample = cluster.bucket("travel-sample");
Scope inventory = travelSample.scope("inventory");

inventory.query(bulkLoadStatement, QueryOptions.queryOptions().asTransaction());
```

and configure it:

```java
cluster.query(bulkLoadStatement, QueryOptions.queryOptions()
        // Single query transactions will often want to increase the default timeout
        .timeout(Duration.ofSeconds(360))
        .asTransaction(singleQueryTransactionOptions()
                .durabilityLevel(DurabilityLevel.PERSIST_TO_MAJORITY)));
```