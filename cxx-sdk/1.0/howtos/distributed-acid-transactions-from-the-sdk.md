---
title: Using Couchbase Transactions
description: A practical guide on using Couchbase Distributed ACID transactions,
  via the C&#43;&#43; SDK.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.0/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:1.0@cxx-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc[]
---

[View original HTML](/cxx-sdk/1.0/howtos/distributed-acid-transactions-from-the-sdk.html)

# Using Couchbase Transactions

> A practical guide on using Couchbase Distributed ACID transactions, via the C++ SDK. 

This guide will show you examples of how to perform multi-document ACID (atomic, consistent, isolated, and durable) database transactions within your application, using the Couchbase Scala SDK.

Refer to the [Transaction Concepts](../concept-docs/transactions.md) page for a high-level overview.

## [](#prerequisites)Prerequisites

* Couchbase Capella
* Couchbase Server

* Couchbase Capella account.
* You should know how to perform [key-value](kv-operations.md) or [query](sqlpp-queries-with-sdk.md) operations with the SDK.
* Your application should have the relevant roles and permissions on the required buckets, scopes, and collections, to perform transactional operations. Refer to the [Organizations & Access](../../../cloud/organizations/organization-projects-overview.md) page for more details.
* If your application is using [extended attributes (XATTRs)](../concept-docs/xattr.md), you should avoid using the XATTR field `txn` — this is reserved for Couchbase use.

* Couchbase Server (6.6.1 or above).
* You should know how to perform [key-value](kv-operations.md) or [query](sqlpp-queries-with-sdk.md) operations with the SDK.
* Your application should have the relevant roles and permissions on the required buckets, scopes, and collections, to perform transactional operations. Refer to the [Roles](../../../server/7.6/learn/security/roles.md) page for more details.
* If your application is using [extended attributes (XATTRs)](../concept-docs/xattr.md), you should avoid using the XATTR field `txn` — this is reserved for Couchbase use.
* NTP should be configured so nodes of the Couchbase cluster are in sync with time.

> [!CAUTION]
> Single Node Cluster
> 
> When using a single node cluster (for example, during development), the default number of replicas for a newly created bucket is **1**. If left at this default, all key-value writes performed with durability will fail with a `errc::key_value::durability_impossible`. In turn, this will cause all transactions (which perform all key-value writes durably) to fail. This setting can be changed via:
> 
> * [Capella UI](../../../cloud/clusters/data-service/manage-buckets.md#add-bucket)
> * [Couchbase Server UI](../../../server/7.6/manage/manage-buckets/create-bucket.md#couchbase-bucket-settings)
> * [Command Line](../../../server/7.6/cli/cbcli/couchbase-cli-bucket-create.md#options)
> 
> If the bucket already exists, then the server needs to be rebalanced for the setting to take effect.

## [](#creating-a-transaction)Creating a Transaction

To create a transaction, an application must supply its logic inside a `lambda`, including any conditional logic required. Once the lambda has successfully run to conclusion, the transaction will be automatically committed. If at any point an error occurs, the transaction will rollback and the lambda may run again.

You can create transactions either _synchronously_ or _asynchronously_ using a callback-based API.

* Synchronous API
* Asynchronous API

The synchronous mode is the easiest to write and understand.

Transactions are accessed via the `cluster` object. By invoking `cluster.transactions()`, we can access the `transactions` object and `run` a transaction.

```c++
auto inventory = cluster.bucket("travel-sample").scope("inventory");

auto [err, result] = cluster.transactions()->run(
  [&collection, &inventory](std::shared_ptr<couchbase::transactions::attempt_context> ctx
  ) -> couchbase::error {
      // Inserting a document
      ctx->insert(collection, "doc-a", tao::json::value{ { "foo", "bar" } });

      // Getting the document
      auto [err_a, doc_a] = ctx->get(collection, "doc-a");
      if (err_a.ec() == couchbase::errc::key_value::document_not_found) {
          // This will not fail the transaction
          fmt::println("Could not find document with key: doc-a");
      } else if (err_a) {
          // Any other error will fail the transaction
          fmt::println("Error getting doc-a: {}", err_a);
      }

      // Replacing a document
      auto [err_b, doc_b] = ctx->get(collection, "doc-b");
      if (err_b) {
          fmt::println("Error getting doc-b: {}", err_b);
          return err_b; // Abort the transaction
      }
      auto content = doc_b.content_as<tao::json::value>();
      content["transactions"] = "are awesome";
      ctx->replace(doc_b, content);

      // Removing a document
      auto [err_c, doc_c] = ctx->get(collection, "doc-c");
      ctx->remove(doc_c);

      // Performing a SELECT SQL++ query against a scope
      auto [query_err, query_res] = ctx->query(
        inventory,
        "SELECT * FROM hotel WHERE country = $1",
        couchbase::transactions::transaction_query_options().positional_parameters(
          "United Kingdom"
        )
      );
      if (!query_err) {
          auto rows = query_res.rows_as_json();
          fmt::println("Query returned {} rows", rows.size());
      }

      // Performing an UPDATE SQL++ query on multiple documents in a scope
      ctx->query(
        inventory,
        "UPDATE route SET airlineid = $1 WHERE airline = $2",
        couchbase::transactions::transaction_query_options().positional_parameters(
          "airline_137", "AF"
        )
      );

      return {};
  }
);

if (err) {
    fmt::println("Transaction finished with error: {}", err);
} else {
    fmt::println("Transaction finished successfully");
}
```

The asynchronous mode allows you to build your application in a reactive style, which can help you scale with excellent efficiency.

Transactions are accessed via the `ReactiveCluster` object. By invoking `Cluster.reactive().transactions()`, we can access the `ReactiveTransactions` object and `run` the lambda.

```c++
auto inventory = cluster.bucket("travel-sample").scope("inventory");

auto barrier = std::make_shared<
  std::promise<std::pair<couchbase::error, couchbase::transactions::transaction_result>>>();
auto fut = barrier->get_future();

cluster.transactions()->run(
  [&collection,
   &inventory](std::shared_ptr<couchbase::transactions::async_attempt_context> ctx
  ) -> couchbase::error {
      auto err_barrier = std::make_shared<std::promise<couchbase::error>>();
      auto err_fut = err_barrier->get_future();

      // Inserting a document
      ctx->insert(
        collection,
        "doc-a",
        tao::json::value{ { "foo", "bar" } },
        [ctx, err_barrier, &collection, &inventory](auto err, auto doc_a) {
            // Getting the document
            ctx->get(
              collection,
              "doc-a",
              [ctx, err_barrier, &collection, &inventory](auto err, auto doc_a) {
                  if (err.ec() == couchbase::errc::key_value::document_not_found) {
                      // This will not fail the transaction
                      fmt::println("Could not find document with key: doc-a");
                  } else if (err) {
                      // Any other error will fail the transaction
                      fmt::println("Error getting doc-a: {}", err);
                  }

                  // Replacing a document
                  ctx->get(
                    collection,
                    "doc-b",
                    [ctx, err_barrier, &collection, &inventory](auto err, auto doc_b) {
                        if (err) {
                            fmt::println("Error getting doc-b: {}", err);
                            err_barrier->set_value(err); // Abort the transaction
                            return;
                        }
                        auto content = doc_b.template content_as<tao::json::value>();
                        content["transactions"] = "are awesome";
                        ctx->replace(
                          doc_b,
                          content,
                          [ctx, err_barrier, &collection, &inventory](
                            auto err, auto doc_b
                          ) {
                              // Removing a document
                              ctx->get(
                                collection,
                                "doc-c",
                                [ctx, err_barrier, &collection, &inventory](
                                  auto err, auto doc_c
                                ) {
                                    ctx->remove(
                                      doc_c,
                                      [ctx, err_barrier, &inventory](auto err) {
                                          // Performing a SELECT SQL++ query against a scope
                                          ctx->query(
                                            inventory,
                                            "SELECT * FROM hotel WHERE country = $1",
                                            couchbase::transactions::
                                              transaction_query_options()
                                                .positional_parameters("United Kingdom"),
                                            [ctx,
                                             err_barrier,
                                             &inventory](auto err, auto res) {
                                                if (!err) {
                                                    auto rows = res.rows_as_json();
                                                    fmt::println(
                                                      "Query returned {} rows", rows.size()
                                                    );
                                                }

                                                // Performing an UPDATE SQL++ query on
                                                // multiple documents in a scope
                                                ctx->query(
                                                  inventory,
                                                  "UPDATE route SET airlineid = $1 WHERE "
                                                  "airline = $2",
                                                  couchbase::transactions::
                                                    transaction_query_options()
                                                      .positional_parameters(
                                                        "airline_137", "AF"
                                                      ),
                                                  [err_barrier](auto err, auto res) {
                                                      err_barrier->set_value({});
                                                  }
                                                );
                                            }
                                          );
                                      }
                                    );
                                }
                              );
                          }
                        );
                    }
                  );
              }
            );
        }
      );

      return err_fut.get();
  },
  [barrier](auto err, auto result) { barrier->set_value({ err, result }); }
);

auto [err, result] = fut.get();
if (err) {
    fmt::println("Transaction finished with error: {}", err);
} else {
    fmt::println("Transaction finished successfully");
}
```

The transaction lambda gets passed a `transaction_attempt_context` object — generally referred to as `ctx` in these examples. Since the lambda could be rerun multiple times, it is important that it does not contain any side effects. In particular, you should never perform regular operations on a `Collection`, such as `collection.insert()`, inside the lambda. Such operations may be performed multiple times, and will not be performed transactionally. Instead, you should perform these operations through the `ctx` object, e.g. `ctx->insert()`.

The result of a transaction is represented by a `TransactionResult` object, which can be used to expose debugging and logging information to help track what happened during a transaction.

In the event that a transaction fails, your application could run into the following errors:

* `errc::transaction::ambiguous`
* `errc::transaction::failed`

Refer to [Error Handling](../concept-docs/transactions-error-handling.md#transaction%5Ferrors) for more details on these.

## [](#key-value-operations)Key-Value Operations

You can perform transactional database operations using familiar key-value CRUD methods:

* **C**reate - `ctx→insert()`
* **R**ead - `ctx→get()`
* **U**pdate - `ctx→replace()`
* **D**elete - `ctx→remove()`

> [!IMPORTANT]
> As mentioned [previously](#lambda-ops), make sure your application uses the transactional key-value operations inside the lambda — such as `ctx→insert()`, rather than `collection.insert()`.

### [](#insert)Insert

To insert a document within a transaction lambda, simply call `ctx→insert()`.

* Synchronous API
* Asynchronous API

```c++
auto [err, result] = cluster.transactions()->run([&](auto ctx) -> couchbase::error {
    ctx->insert(collection, "doc_id", tao::json::value{ { "foo", "bar" } });
    return {};
});
```

```c++
cluster.transactions()->run(
  [&](auto ctx) -> couchbase::error {
      ctx->insert(
        collection,
        "doc_id",
        tao::json::value{ { "foo", "bar" } },
        [](auto err, auto doc) {
            // Handle operation result/err
        }
      );
      return {};
  },
  std::move(complete_handler)
);
```

### [](#get)Get

To retrieve a document from the database you can call `ctx→get()`.

```c++
auto [err, result] = cluster.transactions()->run([&](auto ctx) -> couchbase::error {
    auto [err, doc] = ctx->get(collection, "doc_id");
    return {};
});
```

`ctx→get()` will return a `transaction_get_result` object, which is very similar to the `get_result` you are used to.

If the application needs to ignore or take action on a document not existing, it can handle the failure:

```c++
auto [err, result] = cluster.transactions()->run([&](auto ctx) -> couchbase::error {
    auto [err, doc] = ctx->get(collection, "doc_id");
    if (err.ec() == couchbase::errc::key_value::document_not_found) {
        // By propagating this failure, the application will cause the transaction to be
        // rolled back.
        return err;
    }
    return {};
});
```

Gets will "Read Your Own Writes", e.g. this will succeed:

```c++
auto [err, result] = cluster.transactions()->run([&](auto ctx) -> couchbase::error {
    ctx->insert(collection, "doc_id2", tao::json::value{ { "foo", "bar" } });
    auto [err, doc] = ctx->get(collection, "doc_id2");
    auto content = doc.template content_as<tao::json::value>();
    fmt::println("Got document: {}", tao::json::to_string(content));
    return {};
});
```

Of course, no other transaction will be able to read that inserted document, until this transaction reaches the commit point.

### [](#replace)Replace

Replacing a document requires a `ctx→get()` call first. This is necessary so the SDK can check that the document is not involved in another transaction, and take appropriate action if so.

* Synchronous API
* Asynchronous API

```c++
auto [err, result] = cluster.transactions()->run([&](auto ctx) -> couchbase::error {
    auto [err, doc] = ctx->get(collection, "doc_id");
    if (err) {
        return {};
    }
    auto content = doc.template content_as<tao::json::value>();
    content["transactions"] = "are awesome";
    ctx->replace(doc, content);
    return {};
});
```

```c++
cluster.transactions()->run(
  [&](auto ctx) -> couchbase::error {
      ctx->get(collection, "doc_id", [ctx](auto err, auto doc) {
          if (err) {
              return;
          }
          auto content = doc.template content_as<tao::json::value>();
          content["transactions"] = "are awesome";
          ctx->replace(doc, content, [](auto err, auto doc) {});
      });
      return {};
  },
  std::move(complete_handler)
);
```

### [](#remove)Remove

As with replaces, removing a document requires a `ctx→get()` call first.

* Synchronous API
* Asynchronous API

```c++
auto [err, result] = cluster.transactions()->run([&](auto ctx) -> couchbase::error {
    auto [err, doc] = ctx->get(collection, "doc_id");
    if (err) {
        return {};
    }
    ctx->remove(doc);
    return {};
});
```

```c++
cluster.transactions()->run(
  [&](auto ctx) -> couchbase::error {
      ctx->get(collection, "doc_id", [ctx](auto err, auto doc) {
          if (err) {
              return;
          }
          ctx->remove(doc, [](auto err) {});
      });
      return {};
  },
  std::move(complete_handler)
);
```

## [](#sql-queries)SQL++ Queries

If you already use [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql), then its use in transactions is very similar. A query returns a `transaction_query_result` that is very similar to the `query_result` you are used to, and takes most of the same options.

> [!IMPORTANT]
> As mentioned [previously](#lambda-ops), make sure your application uses the transactional query operations inside the lambda — such as `ctx→query()`, rather than `cluster.query()` or `scope.query()`.

Here is an example of selecting some rows from the `travel-sample` bucket:

```c++
auto travel_sample = cluster.bucket("travel-sample");
auto inventory = travel_sample.scope("inventory");

cluster.transactions()->run([&](auto ctx) -> couchbase::error {
    std::string statement{ "SELECT * FROM hotel WHERE country = $1" };
    auto [err, result] = ctx->query(
      inventory,
      statement,
      couchbase::transactions::transaction_query_options().positional_parameters(
        "United States"
      )
    );
    auto rows = result.rows_as_json();
    return {};
});
```

An example using a `scope` for an `UPDATE`:

```c++
std::string hotel_chain{ "http://marriot%" };
std::string country{ "United States" };

cluster.transactions()->run([&](auto ctx) -> couchbase::error {
    std::string statement{
        "UPDATE hotel SET price = $1 WHERE url LIKE $2 AND country = $3"
    };
    auto options =
      couchbase::transactions::transaction_query_options().positional_parameters(
        99, 99, hotel_chain, country
      );
    auto [err, result] = ctx->query(inventory, statement, options);
    fmt::println(
      "Mutation Count = {}", result.meta_data().metrics().value().mutation_count()
    );
    return {};
});
```

And an example combining `SELECT` and `UPDATE`.

```c++
cluster.transactions()->run([&](auto ctx) -> couchbase::error {
    // Find all hotels of the chain
    auto [err, result] = ctx->query(
      inventory,
      "SELECT reviews FROM hotel WHERE url LIKE $1 AND country = $2",
      couchbase::transactions::transaction_query_options().positional_parameters(
        hotel_chain, country
      )
    );

    // This function (not provided here) will use a trained machine learning model to
    // provide a suitable price based on recent customer reviews.
    auto updated_price = price_from_recent_reviews(result);

    // Set the price of al hotels in the chain
    ctx->query(
      inventory,
      "UPDATE hotel SET price = $1 WHERE url LIKE $2 AND country = $3",
      couchbase::transactions::transaction_query_options().positional_parameters(
        updated_price, hotel_chain, country
      )
    );

    return {};
});
```

As you can see from the snippet above, it is possible to call regular C++ functions from the lambda, permitting complex logic to be performed. Just remember that since the lambda may be called multiple times, so may the method.

Like key-value operations, queries support "Read Your Own Writes". This example shows inserting a document and then selecting it again:

```c++
cluster.transactions()->run([&](auto ctx) -> couchbase::error {
    ctx->query("INSERT INTO `default` VALUES ('doc', {'hello':'world'})"); (1)

    // Performing a 'Read Your Own Write'
    auto [err, result] =
      ctx->query("SELECT `default`.* FROM `default` WHERE META().id = 'doc'"); (2)
    fmt::println("Result Count = {}", result.meta_data().metrics().value().result_count());

    return {};
});
```

| **1** | The inserted document is only staged at this point, as the transaction has not yet committed.Other transactions, and other non-transactional actors, will not be able to see this staged insert yet. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can, as we are reading a mutation staged inside the same transaction.                                                                                                                 |

## [](#mixing-key-value-and-sql)Mixing Key-Value and SQL++

Key-Value and SQL++ query operations can be freely intermixed, and will interact with each other as you would expect. In this example we insert a document with a key-value operation, and read it with a `SELECT` query.

```c++
cluster.transactions()->run([&](auto ctx) -> couchbase::error {
    ctx->insert(collection, "doc", tao::json::value{ { "hello", "world" } }); (1)

    // Performing a 'Read Your Own Write'
    auto [err, result] =
      ctx->query("SELECT `default`.* FROM `default` WHERE META().id = 'doc'"); (2)
    fmt::println("Result Count = {}", result.meta_data().metrics().value().result_count());

    return {};
});
```

| **1** | The key-value insert operation is only staged, and so it is not visible to other transactions or non-transactional actors. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can view it, as the insert was in the same transaction.                                                     |

> [!IMPORTANT]
> Query Mode
> 
> When a transaction executes a query statement, the transaction enters **query mode**, which means that the query is executed with the user’s query permissions. Any **key-value** operations which are executed by the transaction _after_ the query statement are _also_ executed with the user’s query permissions. These may or may not be different to the user’s data permissions; if they are different, you may get unexpected results.

## [](#concurrent-operations)Concurrent Operations

The async API allows operations to be performed concurrently inside a transaction, which can assist performance.

An example of performing parallel operations using the async API:

```c++
std::vector<std::string> doc_ids = { "doc1", "doc2", "doc3", "doc4", "doc5" };

cluster.transactions()->run(
  [&](auto ctx) -> couchbase::error {
      for (auto doc_id : doc_ids) {
          ctx->get(collection, doc_id, [ctx](auto err, auto doc) {
              if (err) {
                  return;
              }
              auto content = doc.template content_as<tao::json::value>();
              content["value"] = "updated";
              ctx->replace(doc, content, [](auto err, auto doc) {
                  if (err) {
                      fmt::println("Error: {}", err);
                  } else {
                      fmt::println("Replaced document successfully");
                  }
              });
          });
      }

      return {};
  },
  std::move(complete_handler)
);
```

> [!NOTE]
> Query Concurrency
> 
> Only one query statement will be performed by the Query service at a time. Non-blocking mechanisms can be used to perform multiple concurrent query statements, but this may result internally in some added network traffic due to retries, and is unlikely to provide any increased performance.

### [](#non-transactional-writes)Non-Transactional Writes

To ensure key-value performance is not compromised, and to avoid conflicting writes, applications should **never** perform non-transactional _writes_ concurrently with transactional ones, on the same document.

The event contains the key of the document involved, to aid the application with debugging.

See [Concurrency with Non-Transactional Writes](../concept-docs/transactions.md#concurrency-with-non-transactional-writes) to learn more.

## [](#configuration)Configuration

The default configuration should be appropriate for most use-cases. If needed, transactions can be globally configured at the point of creating the `cluster`:

```c++
auto opts =
  couchbase::cluster_options(username, password)
    .transactions()
    .durability_level(couchbase::durability_level::persist_to_majority)
    .cleanup_config(couchbase::transactions::transactions_cleanup_config().cleanup_window(
      std::chrono::seconds(30)
    ));
```

The default configuration will perform all writes with the durability setting `Majority`, ensuring that each write is available in-memory on the majority of replicas before the transaction continues. There are two higher durability settings available that will additionally wait for all mutations to be written to physical storage on either the active or the majority of replicas, before continuing. This further increases safety, at a cost of additional latency.

> [!CAUTION]
> A level of `None` is present but its use is discouraged and unsupported. If durability is set to `None`, then ACID semantics are not guaranteed.

## [](#additional-resources)Additional Resources

* Learn more about [Distributed ACID Transactions](../concept-docs/transactions.md).
* Check out the SDK [API Reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/namespacecouchbase%5F1%5F1transactions.html).