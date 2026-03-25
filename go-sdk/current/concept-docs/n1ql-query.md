---
title: Query
description: Parallel data management for complex queries over many records,
  using a familiar SQL-like syntax.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/release/2.12/modules/concept-docs/pages/n1ql-query.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:go-sdk:concept-docs:n1ql-query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/current/concept-docs/n1ql-query.html)

# Query

> Parallel data management for complex queries over many records, using a familiar SQL-like syntax. 

The [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) Query Language provides a familiar, SQL-like experience for querying documents stored in Couchbase. You can [read up on the language in our reference guide](../../../server/current/n1ql/n1ql-language-reference/index.md), but you probably just want to [dive into a practical example](../howtos/sqlpp-queries-with-sdk.md).

Below, we fill in some of the gaps between reference and rolling-up-your-sleeves practicality, with discussion of a few areas of the Query Service where more background knowledge will help you to better program your application.

## [](#prepared-statements-for-query-optimization)Prepared Statements for Query Optimization

When a SQL++ query string is sent to the server, the server will inspect the string and parse it, planning which indexes to query. Once this is done, it generates a _query plan_ (see the [SQL++ reference](../../../server/current/n1ql/n1ql-language-reference/prepare.md), which gives more information on how to optimize queries using prepared statements). The computation for the plan adds some additional processing time and overhead for the query.

Often-used queries can be _prepared_ so that its _plan_ is generated only once. Subsequent queries using the same query string will use the pre-generated plan instead, saving on the overhead and processing of the plan each time. This is done for queries from the SDK by setting the `adhoc` query option to `false`.

For Couchbase Server 6.0 and earlier, the plan is cached by the SDK (up to a limit of 5000), as well as the Query Service. On Couchbase Server 6.5 and newer, the plan is stored by the Query Service — up to an adjustable limit of 16 384 plans per Query node.

For Couchbase Server 6.0 and earlier, the generated plan is not influenced by placeholders. Thus parameterized queries are considered the same query for caching and planning purposes, even if the supplied parameters are different. With Couchbase Server 6.5 and newer, if a statement has placeholders, _and_ a placeholder is supplied, the Query Service will generate specially optimized plans. Therefore, if you are supplying the placeholder each time, `adhoc = true` will actually return a better-optimized plan (at the price of generating a fresh plan for each query).

If your queries are highly dynamic, we recommend using parameterized queries if possible (epecially when prepared statements are not used). Parameterized queries are more cache efficient and will allow for better performance.

> [!NOTE]
> In the Go SDK the `adhoc` parameter is `Adhoc`. It is set to `false` by default — set to `true` for a plan _not_ to be prepared, or a prepared plan _not_ to be reused. The 5000 limit to the client-side cache also does not apply.

```golang
		query := "SELECT count(*) FROM `travel-sample`.inventory.airport where country = $1;"
		rows, err := cluster.Query(query, &gocb.QueryOptions{
			Adhoc:                false,
			PositionalParameters: []interface{}{"France"},
		})
		if err != nil {
			panic(err)

		}

		for rows.Next() {
			// do something
		}
		if err := rows.Err(); err != nil {
			panic(err)
		}
```

## [](#indexes)Indexes

The Couchbase query service makes use of [_indexes_](../../../server/current/learn/services-and-indexes/indexes/indexes.md) in order to do its work. Indexes replicate subsets of documents from data nodes over to index nodes, allowing specific data (for example, specific document properties) to be retrieved quickly, and to distribute load away from data nodes in [MDS](../../../server/current/learn/services-and-indexes/services/services.md) topologies.

> [!IMPORTANT]
> In order to make a bucket queryable, it must have at least one index defined.

You can define a _primary index_ on a bucket. When a _primary_ index is defined you can issue non-covered (see below) queries on the bucket as well. This includes using the `META` function in the queries.

```sqlpp
CREATE PRIMARY INDEX ON `travel-sample`
```

You can also define indexes over given document fields and then use those fields in the query:

```sqlpp
CREATE INDEX ix_name ON `travel-sample`(name);
CREATE INDEX ix_email ON `travel-sample`(email);
```

This would allow you to query the _travel-sample_ bucket regarding a document’s `name` or `email` properties, thus:

```sqlpp
SELECT name, email
FROM `travel-sample`
WHERE name="Glasgow Grand Central" OR email="grandcentralhotel@principal-hayley.com";
```

Indexes help improve the performance of a query. When an index includes the actual values of all the fields specified in the query, the index _covers_ the query, and eliminates the need to fetch the actual values from the Data Service. An index, in this case, is called a _covering index_, and the query is called a _covered_ query. For more information, see [Covering Indexes](../../../server/current/indexes/covering-indexes.md).

You can also create and define indexes in the SDK using:

```golang
		mgr := cluster.QueryIndexes()
		if err := mgr.CreatePrimaryIndex(bucketName, nil); err != nil {
			if errors.Is(err, gocb.ErrIndexExists) {
				fmt.Println("Index already exists")
			} else {
				panic(err)
			}
		}

		if err := mgr.CreateIndex(bucketName, "ix_name", []string{"name"}, nil); err != nil {
			if errors.Is(err, gocb.ErrIndexExists) {
				fmt.Println("Index already exists")
			} else {
				panic(err)
			}
		}

		if err := mgr.CreateIndex(bucketName, "ix_email", []string{"email"}, nil); err != nil {
			if errors.Is(err, gocb.ErrIndexExists) {
				fmt.Println("Index already exists")
			} else {
				panic(err)
			}
		}
```

## [](#index-building)Index Building

Creating indexes on buckets with many existing documents can take a long time. You can build indexes in the background, creating _deferred_ indexes. The deferred indexes can be built together, rather than having to re-scan the entire bucket for each index.

```sql
CREATE PRIMARY INDEX ON `travel-sample` WITH {"defer_build": true};
CREATE INDEX ix_name ON `travel-sample`(name) WITH {"defer_build": true};
CREATE INDEX ix_email ON `travel-sample`(email) WITH {"defer_build": true};
BUILD INDEX ON `travel-sample`(`#primary`, `ix_name`, `ix_email`);
```

The indexes are not built until the `BUILD INDEX` statement is executed. At this point, the server scans all of the documents in the `travel-sample` bucket, and indexes it for all of the applicable indexes (in this case, those that have a `name` or `email` field).

Building deferred indexes can also be done via the SDK:

```golang
		mgr := cluster.QueryIndexes()
		if err := mgr.CreatePrimaryIndex(bucketName,
			&gocb.CreatePrimaryQueryIndexOptions{Deferred: true},
		); err != nil {
			if errors.Is(err, gocb.ErrIndexExists) {
				fmt.Println("Index already exists")
			} else {
				panic(err)
			}
		}

		if err := mgr.CreateIndex(bucketName, "ix_name", []string{"name"},
			&gocb.CreateQueryIndexOptions{Deferred: true},
		); err != nil {
			if errors.Is(err, gocb.ErrIndexExists) {
				fmt.Println("Index already exists")
			} else {
				panic(err)
			}
		}

		if err = mgr.CreateIndex(bucketName, "ix_email", []string{"email"},
			&gocb.CreateQueryIndexOptions{Deferred: true},
		); err != nil {
			if errors.Is(err, gocb.ErrIndexExists) {
				fmt.Println("Index already exists")
			} else {
				panic(err)
			}
		}

		indexesToBuild, err := mgr.BuildDeferredIndexes(bucketName, nil)
		if err != nil {
			panic(err)
		}
		err = mgr.WatchIndexes(bucketName, indexesToBuild, time.Duration(2*time.Second), nil)
		if err != nil {
			panic(err)
		}
```

## [](#index-consistency)Index Consistency

Because indexes are by design outside the Data Service, they are _eventually consistent_ with respect to changes to documents and, depending on how you issue the query, may at times not contain the most up-to-date information. This may especially be the case when deployed in a write-heavy environment: changes may take some time to propagate over to the index nodes.

The asynchronous updating nature of [Global Secondary Indexes (GSIs)](../../../server/current/indexes/indexing-overview.md) means that they can be very quick to query and do not require the additional overhead of index recaclculations at the time documents are modified. SQL++ queries are forwarded to the relevant indexes, and the queries are done based on indexed information, rather than the documents as they exist in the data service.

With default query options, the query service will rely on the current index state: the most up-to-date document versions are not retrieved, and only the indexed versions are queried. This provides the best performance. Only updates occurring with a small time frame may not yet have been indexed. For cases where consistency is more important than performance, the `scan_consistency` property of a query may be set to `REQUEST_PLUS`. ensuring that indexes are synchronized with the data service before querying.

The following options are available:

* `not_bounded`: Executes the query immediately, without requiring any consistency for the query. If index maintenance is running behind, out-of-date results may be returned.
* `at_plus`: Executes the query, requiring indexes first to be updated to the timestamp of the last update. If index maintenance is running behind, the query waits for it to catch up.
* `request_plus`: Executes the query, requiring the indexes first to be updated to the timestamp of the current query request. If index maintenance is running behind, the query waits for it to catch up.
* `statement_plus`: Executes the query with strong consistency per statement. Before processing each statement, the service obtains a current vector timestamp and uses it as a lower bound for that statement.

For SQL++, the default consistency is `not_bounded`.

Consider the following snippet:

```golang
		random := rand.Intn(10000000)
		user := struct {
			Name   string `json:"name"`
			Email  string `json:"email"`
			Random int    `json:"random"`
		}{Name: "Brass Doorknob", Email: "brass.doorknob@juno.com", Random: random}

		_, err := collection.Upsert(fmt.Sprintf("user:%d", random), user, nil)
		if err != nil {
			panic(err)
		}

		_, err = cluster.Query(
			"SELECT name, email, random, META().id FROM `travel-sample`.inventory.airport WHERE $1 IN name",
			&gocb.QueryOptions{
				PositionalParameters: []interface{}{"Brass"},
			},
		)
		if err != nil {
			panic(err)
		}
```

The above query may not return the newly inserted document because it has not yet been indexed. The query is issued immediately after document creation, and in this case the query engine may process the query before the index has been updated.

If the above code is modified to use _RequestPlus_, query processing will wait until all updates have been processed and recalculated into the index from the point in time the query was received:

```golang
		_, err := cluster.Query(
			"SELECT name, email, random, META().id FROM `travel-sample`.inventory.airport WHERE $1 IN name",
			&gocb.QueryOptions{
				PositionalParameters: []interface{}{"Brass"},
				ScanConsistency:      gocb.QueryScanConsistencyRequestPlus,
			},
		)
		if err != nil {
			panic(err)
		}
```

This gives the application developer more control over the balance between performance (latency) and consistency, and allows optimization on a case-by-case basis.