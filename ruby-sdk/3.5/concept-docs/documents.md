---
title: Documents
description: Couchbase supports CRUD operations, various data structures, and
  binary documents.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.5/modules/concept-docs/pages/documents.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/ruby-sdk/3.5/concept-docs/documents.html)

# Documents

> Couchbase supports CRUD operations, various data structures, and binary documents. 

Although query and path-based (Sub-Document) services are available, the simplicity of the document-based kv interface is the fastest way to perform operations involving single documents.

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

## [](#primitive-key-value-operations)Primitive Key-Value Operations

```ruby
collection.upsert(docid, document)
collection.insert(docid, document)
collection.replace(docid, document)
collection.get(docid)
collection.remove(docid)
```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

> [!NOTE]
> If you wish to only modify certain parts of a document, you can use [sub-document](subdocument-operations.md) operations which operate on specific subsets of documents:
> 
> ```ruby
> collection.mutate_in('airline_10', [
>   MutateInSpec.upsert('msrp', 18)
> ])
> ```
> 
> or [N1QL UPDATE](#7.1@server:n1ql:n1ql-language-reference/update.adoc) to update documents based on specific query criteria:
> 
> ```sql
> UPDATE `travel-sample`.inventory.airline SET sale_price = msrp * 0.75 WHERE msrp < 19.95;
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

```ruby
users_collection = bucket.scope('tenant_agent_00').collection('users')
result = users_collection.lookup_in('1', [
  LookupInSpec.get('credit_cards[0].type'),
  LookupInSpec.get('credit_cards[0].expiration')
])

puts("Card Type: #{result.content(0)}")
puts("Expiry: #{result.content(1)}")
```

The same behaviour could be achieved by using get with projections:

```ruby
options = Collection::GetOptions.new
options.project(%w[credit_cards[0].type credit_cards[0].expiration])
res = users_collection.get('1', options)

puts("Result: #{res.content}")
```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

```ruby
counter_doc_id = 'counter-doc'
# Increment by 1, creating doc if needed.
# By using `initial: 1` we set the starting count(non-negative) to 1 if the document needs to be created.
# If it already exists, the count will increase by 1.
collection.binary.increment(counter_doc_id, Options::Increment(initial: 1))
# Decrement by 1
collection.binary.decrement(counter_doc_id, Options::Decrement())
# Decrement by 5
collection.binary.decrement(counter_doc_id, Options::Decrement(delta: 5))
```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

```ruby
result = collection.get('counter-doc')
value = result.content

increment_amnt = 5
opts = Collection::ReplaceOptions.new
opts.cas = result.cas

puts("Current value: #{value}")
collection.replace('counter-doc', value + increment_amnt, opts) if value.zero?
puts("RESULT: #{value + increment_amnt}")
```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

### [](#use-cases)Use Cases

The SDK provides a high-level abstraction over the simple `incr()`/`decr()` of Couchbase Server’s memcached binary protocol, using `collection.binary()`. This enables you to work with counters using `get()` and `replace()` operations — allowing, _inter alia_, the use of durability options with the operations. You will find several ways of working with counters [in the API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/BinaryCollection.html).

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]