[View original HTML](/go-sdk/2.9/howtos/distributed-acid-transactions-from-the-sdk.html)

> A practical guide to using Couchbase’s distributed ACID transactions, via the Go SDK. 

This guide will show you examples of how to perform multi-document ACID (atomic, consistent, isolated, and durable) database transactions within your application, using the Couchbase Go SDK.

Refer to the [Transaction Concepts](../concept-docs/transactions.md) page for a high-level overview.

## [](#prerequisites)Prerequisites

* Couchbase Capella
* Couchbase Server

* Couchbase Capella account.
* You should know how to perform [key-value](kv-operations.md) or [query](n1ql-queries-with-sdk.md) operations with the SDK.
* Your application should have the relevant roles and permissions on the required buckets, scopes, and collections, to perform transactional operations. Refer to the [Organizations & Access](../../../cloud/organizations/organization-projects-overview.md) page for more details.
* If your application is using [extended attributes (XATTRs)](../concept-docs/xattr.md), you should avoid using the XATTR field `txn` — this is reserved for Couchbase use.

* Couchbase Server 7.0.0 or above.
* You should know how to perform [key-value](kv-operations.md) or [query](n1ql-queries-with-sdk.md) operations with the SDK.
* Your application should have the relevant roles and permissions on the required buckets, scopes, and collections, to perform transactional operations. Refer to the [Roles](../../../server/7.6/learn/security/roles.md) page for more details.
* If your application is using [extended attributes (XATTRs)](../concept-docs/xattr.md), you should avoid using the XATTR field `txn` — this is reserved for Couchbase use.
* NTP should be configured so nodes of the Couchbase cluster are in sync with time.

|  | Single Node Cluster When using a single node cluster (for example, during development), the default number of replicas for a newly created bucket is **1**. If left at this default, all key-value writes performed with durability will fail with a ErrDurabilityImpossible. In turn, this will cause all transactions (which perform all key-value writes durably) to fail. This setting can be changed via: [Capella UI](../../../cloud/clusters/data-service/manage-buckets.md#add-bucket) [Couchbase Server UI](../../../server/7.6/manage/manage-buckets/create-bucket.md#couchbase-bucket-settings) [Command Line](../../../server/7.6/cli/cbcli/couchbase-cli-bucket-create.md#options) If the bucket already exists, then the server needs to be rebalanced for the setting to take effect. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#creating-a-transaction)Creating a Transaction

To create a transaction, an application must supply its logic inside a `function literal`, including any conditional logic required. Once the function literal has successfully run to conclusion, the transaction will be automatically committed. If at any point an error occurs, the transaction will rollback and the function literal may run again.

```go
scope := cluster.Bucket("travel-sample").Scope("inventory")

_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	// Inserting a doc:
	_, err := ctx.Insert(collection, "doc-a", map[string]interface{}{})
	if err != nil {
		return err
	}

	// Getting documents:
	_, err = ctx.Get(collection, "doc-a")
	// Use err != nil && !errors.Is(err, gocb.ErrDocumentNotFound) if the document may or may not exist
	if err != nil {
		return err
	}

	// Replacing a doc:
	docB, err := ctx.Get(collection, "doc-b")
	if err != nil {
		return err
	}

	var content map[string]interface{}
	err = docB.Content(&content)
	if err != nil {
		return err
	}
	content["transactions"] = "are awesome"
	_, err = ctx.Replace(docB, content)
	if err != nil {
		return err
	}

	// Removing a doc:
	docC, err := ctx.Get(collection, "doc-c")
	if err != nil {
		return err
	}

	err = ctx.Remove(docC)
	if err != nil {
		return err
	}

	// Performing a SELECT N1QL query against a scope:
	qr, err := ctx.Query("SELECT * FROM hotel WHERE country = $1", &gocb.TransactionQueryOptions{
		PositionalParameters: []interface{}{"United Kingdom"},
		Scope:                scope,
	})
	if err != nil {
		return err
	}

	type hotel struct {
		Name string `json:"name"`
	}

	var hotels []hotel
	for qr.Next() {
		var h hotel
		err = qr.Row(&h)
		if err != nil {
			return err
		}

		hotels = append(hotels, h)
	}

	// Performing an UPDATE N1QL query on multiple documents, in the `inventory` scope:
	_, err = ctx.Query("UPDATE route SET airlineid = $1 WHERE airline = $2", &gocb.TransactionQueryOptions{
		PositionalParameters: []interface{}{"airline_137", "AF"},
		Scope:                scope,
	})
	if err != nil {
		return err
	}

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
var ambigErr gocb.TransactionCommitAmbiguousError
if errors.As(err, &ambigErr) {
	log.Println("Transaction possibly committed")

	log.Printf("%+v", ambigErr)
	return
}
var failedErr gocb.TransactionFailedError
if errors.As(err, &failedErr) {
	log.Println("Transaction did not reach commit point")

	log.Printf("%+v", failedErr)
	return
}
if err != nil {
	panic(err)
}
```

The transaction function literal gets passed a `TransactionAttemptContext` object — generally referred to as `ctx` in these examples. Since the function literal could be rerun multiple times, it is important that it does not contain any side effects. In particular, you should never perform regular operations on a `Collection`, such as `collection.Insert()`, inside the function literal. Such operations may be performed multiple times, and will not be performed transactionally. Instead, you should perform these operations through the `ctx` object, e.g. `ctx.Insert()`.

The result of a transaction is represented by a `TransactionResult` object, which can be used to expose debugging and logging information to help track what happened during a transaction.

In the event that a transaction fails, your application could run into the following errors:

* `TransactionCommitAmbiguousError`
* `TransactionFailedError`

Refer to [Error Handling](../concept-docs/transactions-error-handling.md#transaction%5Ferrors) for more details on these.

### [](#logging)Logging

To aid troubleshooting, raise the log level on the SDK.

Please see the [Go SDK logging documentation](collecting-information-and-logging.md) for details.

## [](#key-value-operations)Key-Value Operations

You can perform transactional database operations using familiar key-value CRUD methods:

* **C**reate - `Insert()`
* **R**ead - `Get()`
* **U**pdate - `Replace()`
* **D**elete - `Remove()`

|  | As mentioned [previously](#lambda-ops), make sure your application uses the transactional key-value operations inside the function literal — such as ctx.Insert(), rather than collection.Insert(). |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#insert)Insert

To insert a document within a transaction function literal, simply call `ctx.Insert()`.

```go
_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	_, err := ctx.Insert(collection, "insert-doc", map[string]interface{}{})
	if err != nil {
		return err
	}

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
if err != nil {
	panic(err)
}
```

### [](#get)Get

To retrieve a document from the database you can call `ctx.Get()`.

```go
_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	doc, err := ctx.Get(collection, "get-doc")
	if err != nil {
		return err
	}

	var content interface{}
	err = doc.Content(&content)
	if err != nil {
		return err
	}

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
if err != nil {
	panic(err)
}
```

`ctx.Get()` will return a `TransactionGetResult` object, which is very similar to the `GetResult` you are used to.

Getting a document could potentially return an `ErrDocumentNotFound` which can be ignored, if you are unsure whether the document exists or not, or if it not existing does not matter:

```go
_, err = cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	doc, err := ctx.Get(collection, "get-doc")
	if err != nil && !errors.Is(err, gocb.ErrDocumentNotFound) {
		return err
	}

	fmt.Println(doc != nil)

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
if err != nil {
	panic(err)
}
```

If the `ErrDocumentNotFound` is not ignored then `Get` will cause the transaction to fail with `TransactionFailedError` (after rolling back any changes, of course). `ErrDocumentNotFound` is one of very few errors that the SDK will allow you to ignore, as the SDK internally tracks the state of the transaction and will not allow illegal operations to continue.

Gets will "Read Your Own Writes", e.g. this will succeed:

```go
_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	_, err := ctx.Insert(collection, "ownwritesdoc", map[string]interface{}{})
	if err != nil {
		return err
	}

	doc, err := ctx.Get(collection, "ownwritesdoc")
	if err != nil {
		return err
	}

	var content interface{}
	err = doc.Content(&content)
	if err != nil {
		return err
	}

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
if err != nil {
	panic(err)
}
```

### [](#replace)Replace

Replacing a document requires a `ctx.Get()` call first. This is necessary so the SDK can check that the document is not involved in another transaction, and take appropriate action if so.

```go
_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	doc, err := ctx.Get(collection, "replace-doc")
	if err != nil {
		return err
	}

	var content map[string]interface{}
	err = doc.Content(&content)
	if err != nil {
		return err
	}
	content["transactions"] = "are awesome"

	_, err = ctx.Replace(doc, content)
	if err != nil {
		return err
	}

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
if err != nil {
	panic(err)
}
```

### [](#remove)Remove

As with replaces, removing a document requires a `ctx.Get()` call first.

```go
_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	doc, err := ctx.Get(collection, "remove-doc")
	if err != nil {
		return err
	}

	err = ctx.Remove(doc)
	if err != nil {
		return err
	}

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
if err != nil {
	panic(err)
}
```

## [](#sql-queries)SQL++ Queries

If you already use [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql), then its use in transactions is very similar. A query returns a `TransactionQueryResult` that is very similar to the `QueryResult` you are used to, and takes most of the same options.

The main difference between `TransactionsQueryResult` and `QueryResult` is that `TransactionsQueryResult` does not stream results. This means that there are no `Err` or `Close` functions and that result sets are buffered in memory - allowing the SDK to read and handle any errors that occur on the stream before returning a result/error.

|  | As mentioned [previously](#lambda-ops), make sure your application uses the transactional query operations inside the function literal — such as ctx.Query(), rather than cluster.Query() or scope.Query(). |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Here is an example of selecting some rows from the `travel-sample` bucket:

```go
bucket := cluster.Bucket("travel-sample")
scope := bucket.Scope("inventory")
_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	qr, err := ctx.Query("SELECT * FROM hotel WHERE country = $1", &gocb.TransactionQueryOptions{
		PositionalParameters: []interface{}{"United Kingdom"},
		Scope:                scope,
	})
	if err != nil {
		return err
	}

	type hotel struct {
		Name string `json:"name"`
	}

	var hotels []hotel
	for qr.Next() {
		var h hotel
		err = qr.Row(&h)
		if err != nil {
			return err
		}

		hotels = append(hotels, h)
	}

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
if err != nil {
	panic(err)
}
```

An example using a `Scope` for an UPDATE operation:

```go
bucket := cluster.Bucket("travel-sample")
scope := bucket.Scope("inventory")
_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	qr, err := ctx.Query("UPDATE hotel SET price = $1 WHERE url LIKE $2 AND country = $3", &gocb.TransactionQueryOptions{
		PositionalParameters: []interface{}{99.99, "http://marriot%", "United Kingdom"},
		Scope:                scope,
	})
	if err != nil {
		return err
	}

	meta, err := qr.MetaData()
	if err != nil {
		return err
	}

	if meta.Metrics.MutationCount != 1 {
		panic("Should have received 1 mutation")
	}

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
if err != nil {
	panic(err)
}
```

And an example combining `SELECT` and `UPDATE`.

```go
bucket := cluster.Bucket("travel-sample")
scope := bucket.Scope("inventory")
_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	// Find all hotels of the chain
	qr, err := ctx.Query("SELECT reviews FROM hotel WHERE url LIKE $1 AND country = $2", &gocb.TransactionQueryOptions{
		PositionalParameters: []interface{}{"http://marriot%", "United Kingdom"},
		Scope:                scope,
	})
	if err != nil {
		return err
	}

	// This function (not provided here) will use a trained machine learning model to provide a
	// suitable price based on recent customer reviews
	updatedPrice := priceFromRecentReviews(qr)

	_, err = ctx.Query("UPDATE hotel SET price = $1 WHERE url LIKE $2 AND country = $3", &gocb.TransactionQueryOptions{
		PositionalParameters: []interface{}{updatedPrice, "http://marriot%", "United Kingdom"},
		Scope:                scope,
	})
	if err != nil {
		return err
	}

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
if err != nil {
	panic(err)
}
```

As you can see from the snippet above, it is possible to call regular Go methods from the function literal, permitting complex logic to be performed. Just remember that since the function literal may be called multiple times, so may the method.

Like key-value operations, queries support "Read Your Own Writes". This example shows inserting a document and then selecting it again:

```go
_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	_, err := ctx.Query("INSERT INTO `default` VALUES ('doc', {'hello':'world'})", nil) (1)
	if err != nil {
		return err
	}

	st := "SELECT `default`.* FROM `default` WHERE META().id = 'doc'" (2)
	qr, err := ctx.Query(st, nil)
	if err != nil {
		return err
	}

	meta, err := qr.MetaData()
	if err != nil {
		return err
	}

	if meta.Metrics.ResultCount != 1 {
		panic("Should have received 1 result")
	}

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
if err != nil {
	panic(err)
}
```

| **1** | The inserted document is only staged at this point, as the transaction has not yet committed.Other transactions, and other non-transactional actors, will not be able to see this staged insert yet. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can, as we are reading a mutation staged inside the same transaction.                                                                                                                 |

### [](#query-options)Query Options

Query options can be provided via `TransactionQueryOptions`, which provides a subset of the options in the Go SDK’s `QueryOptions`.

```go
_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	_, err := ctx.Query("INSERT INTO `default` VALUES ('queryOpts', {'hello':'world'})",
		&gocb.TransactionQueryOptions{Profile: gocb.QueryProfileModeTimings},
	)
	if err != nil {
		return err
	}

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
if err != nil {
	panic(err)
}
```

__Table 1\. Supported Transaction Query Options__
| Name                                      | Description                                                                      |
| ----------------------------------------- | -------------------------------------------------------------------------------- |
| PositionalParameters(\[\]interface{})     | Allows to set positional arguments for a parameterized query.                    |
| NamedParameters(map\[string\]interface{}) | Allows you to set named arguments for a parameterized query.                     |
| ScanConsistency(QueryScanConsistency)     | Sets a different scan consistency for this query.                                |
| FlexIndex(bool)                           | Tells the query engine to use a flex index (utilizing the search service).       |
| ClientContextID(string)                   | Sets a context ID returned by the service for debugging purposes.                |
| ScanWait(time.Duration)                   | Allows to specify a maximum scan wait time.                                      |
| ScanCap(uint32)                           | Specifies a maximum cap on the query scan size.                                  |
| PipelineBatch(uint32)                     | Sets the batch size for the query pipeline.                                      |
| PipelineCap(uint32)                       | Sets the cap for the query pipeline.                                             |
| Profile(QueryProfileMode)                 | Allows you to enable additional query profiling as part of the response.         |
| Readonly(bool)                            | Tells the client and server that this query is readonly.                         |
| Prepared(bool)                            | If set to false will prepare the query and later execute the prepared statement. |
| Raw(map\[str\]interface{})                | Escape hatch to add arguments that are not covered by these options.             |

## [](#mixing-key-value-and-sql)Mixing Key-Value and SQL++

Key-Value operations and queries can be freely intermixed, and will interact with each other as you would expect. In this example we insert a document with a key-value operation, and read it with a `SELECT` query.

```go
_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	_, err := ctx.Insert(collection, "queryRyow", map[string]interface{}{"hello": "world"}) (1)
	if err != nil {
		return err
	}

	st := "SELECT `default`.* FROM `default` WHERE META().id = 'queryRyow'" (2)
	qr, err := ctx.Query(st, nil)
	if err != nil {
		return err
	}

	meta, err := qr.MetaData()
	if err != nil {
		return err
	}

	if meta.Metrics.ResultCount != 1 {
		panic("Should have received 1 result")
	}

	// There is no commit call, by not returning an error the transaction will automatically commit
	return nil
}, nil)
if err != nil {
	panic(err)
}
```

| **1** | The key-value insert operation is only staged, and so it is not visible to other transactions or non-transactional actors. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can view it, as the insert was in the same transaction.                                                     |

|  | Query Mode When a transaction executes a query statement, the transaction enters **query mode**, which means that the query is executed with the user’s query permissions. Any **key-value** operations which are executed by the transaction _after_ the query statement are _also_ executed with the user’s query permissions. These may or may not be different to the user’s data permissions; if they are different, you may get unexpected results. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#concurrent-operations)Concurrent Operations

The API allows operations to be performed concurrently inside a transaction, which can assist performance. There are two rules the application needs to follow:

* The first mutation must be performed alone, in serial. This is because the first mutation also triggers the creation of metadata for the transaction.
* All concurrent operations must be allowed to complete fully, so the transaction can track which operations need to be rolled back in the event of failure. This means the application must 'swallow' the error, but record that an error occurred, and then at the end of the concurrent operations, if an error occurred, throw an error to cause the transaction to retry.

|  | Query ConcurrencyOnly one query statement will be performed by the Query service at a time. Non-blocking mechanisms can be used to perform multiple concurrent query statements, but this may result internally in some added network traffic due to retries, and is unlikely to provide any increased performance. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#non-transactional-writes)Non-Transactional Writes

To ensure key-value performance is not compromised, and to avoid conflicting writes, applications should **never** perform non-transactional _writes_ concurrently with transactional ones, on the same document.

See [Concurrency with Non-Transactional Writes](../concept-docs/transactions.md#concurrency-with-non-transactional-writes) to learn more.

## [](#configuration)Configuration

The default configuration should be appropriate for most use-cases. Transactions can optionally be globally configured at the point of creating the `Cluster` object. For example, if you want to change the level of durability which must be attained, this can be configured as part of the connect options:

```go
opts := gocb.ClusterOptions{
	Authenticator: gocb.PasswordAuthenticator{
		Username: "Administrator",
		Password: "password",
	},
	TransactionsConfig: gocb.TransactionsConfig{
		DurabilityLevel: gocb.DurabilityLevelPersistToMajority,
	},
}
```

The default configuration will perform all writes with the durability setting `Majority`, ensuring that each write is available in-memory on the majority of replicas before the transaction continues. There are two higher durability settings available that will additionally wait for all mutations to be written to physical storage on either the active or the majority of replicas, before continuing. This further increases safety, at a cost of additional latency.

|  | A level of None is present but its use is discouraged and unsupported. If durability is set to None, then ACID semantics are not guaranteed. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#additional-resources)Additional Resources

* Learn more about [Distributed ACID Transactions](../concept-docs/transactions.md).
* Check out the SDK [API Reference](https://pkg.go.dev/github.com/couchbase/gocb/v2).