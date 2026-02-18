---
title: Document
description: Couchbase supports CRUD operations, various data structures, and
  binary documents.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/1.3/modules/concept-docs/pages/documents.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/kotlin-sdk/1.3/concept-docs/documents.html)

# Document

> Couchbase supports CRUD operations, various data structures, and binary documents. 

Although query and path-based (Sub-Document) services are available, the simplicity of the document-based key-value (kv) interface is the fastest way to perform operations involving single documents.

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

## [](#primitive-key-value-operations)Primitive Key-Value Operations

```java
upsert(String docid, Object document)
insert(String docid, Object document)
replace(String docid, Object document)
get(String docid)
remove(String docid)
```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

> [!NOTE]
> If you wish to only modify certain parts of a document, you can use [sub-document](subdocument-operations.md) operations which operate on specific subsets of documents:
> 
> ```java
> List<MutateInSpec> spec = Collections.singletonList(
>         MutateInSpec.upsert("msrp", 18.00)
> );
> collection.mutateIn("airline_10", spec);
> ```
> 
> or [N1QL UPDATE](#7.1@server:n1ql:n1ql-language-reference/update.adoc) to update documents based on specific query criteria:
> 
> ```sql
> update `travel-sample`.inventory.airline SET sale_price = msrp * 0.75 WHERE msrp < 19.95;
> ```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

```sql
SELECT * FROM `travel-sample`.inventory.airport USE KEYS ["airport_1254"];
```

or

```sql
SELECT * FROM `travel-sample`.inventory.airport WHERE META().id = "airport_1254";
```

You can also retrieve _parts_ of documents using [sub-document operations](subdocument-operations.md), by specifying one or more sections of the document to be retrieved

```java
Collection usersCollection = bucket.scope("tenant_agent_00").collection("users");
List<LookupInSpec> spec = Arrays.asList(
        LookupInSpec.get("credit_cards[0].type"),
        LookupInSpec.get("credit_cards[0].expiration")
);
usersCollection.lookupIn("1", spec);
```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

```java
String counterDocId = "counter-doc";
// Increment by 1, creating doc if needed.
// By using `.incrementOptions().initial(1)` we set the starting count(non-negative) to 1 if the document needs to be created.
// If it already exists, the count will increase by 1.
collection.binary().increment(counterDocId, IncrementOptions.incrementOptions().initial(1));
// Decrement by 1
collection.binary().decrement(counterDocId);
// Decrement by 5
collection.binary().decrement(counterDocId, DecrementOptions.decrementOptions().delta(5));
```

You can simplify by importing `decrementOptions()` statically:

```java
collection.binary().decrement(counterDocId, decrementOptions().delta(5));
```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

```java
            GetResult getResult = collection.get("counter-doc");
            int value = getResult.contentAs(Integer.class);
            int incrementAmnt = 5;

            if (shouldIncrementAmnt(value)) {
                collection.replace(
                        "counter-doc",
                        value + incrementAmnt,
                        ReplaceOptions.replaceOptions().cas(getResult.cas())
                );
            }
```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

### [](#use-cases)Use Cases

The SDK provides a high-level abstraction over the simple `incr()`/`decr()` of Couchbase Server’s memcached binary protocol, using `collections.binary()`. This enables you to work with counters using `get()` and `upsert()` operations — allowing, _inter alia_, the use of durability options with the operations. You will find several ways of working with counters [in the API docs](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/kv/CounterAccessor.html#increment%28com.couchbase.client.core.Core,com.couchbase.client.core.msg.kv.IncrementRequest,java.lang.String,com.couchbase.client.java.kv.PersistTo,com.couchbase.client.java.kv.ReplicateTo%29%28java.lang.String,long%29).

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]