[View original HTML](/kotlin-sdk/1.3/howtos/distributed-acid-transactions-from-the-sdk.html)

> Distributed ACID Transactions with JVM SDKs 

Distributed ACID Transactions are implemented in the Java SDK, and simple to integrate into your Kotlin client code.

## [](#java-transactions-from-the-kotlin-sdk)Java Transactions from the Kotlin SDK

You will need to include the Couchbase Java SDK in your project.

Create a `com.couchbase.client.java.Cluster` in your Kotlin app with the [normal Java calls](../../../java-sdk/current/howtos/managing-connections.md) `(Cluster.connect(…​))`, and then do transactions on it as normal, e.g.:

```java
javaCluster.transactions().run(ctx => { /* your transaction logic here */ })
```

So in your app you have both a `com.couchbase.client.java.Cluster` and a `com.couchbase.client.kotlin.Cluster`, which are independent connections.

## [](#additional-information)Additional Information

For more information on Java transactions, read our guide in the Java documentation:

* [Distributed ACID Transactions from the Java SDK](../../../java-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)

  * [Single Query Transactions](../../../java-sdk/current/howtos/transactions-single-query.md)
  * [Tracing](../../../java-sdk/current/howtos/transactions-tracing.md)
* [Transaction Concepts](../../../java-sdk/current/concept-docs/transactions.md)

  * [Cleanup](../../../java-sdk/current/concept-docs/transactions-cleanup.md)
  * [Error Handling](../../../java-sdk/current/concept-docs/transactions-error-handling.md)