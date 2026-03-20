---
title: Documents
description: Couchbase supports CRUD operations, various data structures, and
  binary documents.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/concept-docs/pages/documents.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:4.2@php-sdk:concept-docs:documents.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/4.2/concept-docs/documents.html)

# Documents

> Couchbase supports CRUD operations, various data structures, and binary documents. 

Although query and path-based (Sub-Document) services are available, the simplicity of the document-based kv interface is the fastest way to perform operations involving single documents.

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

## [](#primitive-key-value-operations)Primitive Key-Value Operations

```php
upsert(string $id, mixed $value[, UpsertOptions $options = null ]) : MutationResult
insert(string $id, mixed $value[, InsertOptions $options = null ]) : MutationResult
replace(string $id, mixed $value[, ReplaceOptions $options = null ]) : MutationResult
get(string $id[, GetOptions $options = null ]) : GetResult
remove(string $id[, RemoveOptions $options = null ]) : MutationResult
```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

> [!NOTE]
> If you wish to only modify certain parts of a document, you can use [sub-document](subdocument-operations.md) operations which operate on specific subsets of documents:
> 
> ```php
> $result = $collection->mutateIn('airline_10', [
>     new MutateUpsertSpec('msrp', 18.00)
> ]);
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

```php
$usersCollection = $bucket->scope('tenant_agent_00')->collection('users');
$usersCollection->lookupIn('1', [
    new LookupGetSpec('credit_cards[0].type'),
    new LookupGetSpec('credit_cards[0].expiration')
]);
```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

```php
$counterDocId = 'counter-doc';
$decrementOpts = new DecrementOptions();
$incrementOpts = new IncrementOptions();
// Increment by 1, creating doc if needed.
// By using `initial(1)` we set the starting count(non-negative) to 1 if the document needs to be created.
// If it already exists, the count will increase by 1.
$collection->binary()->increment($counterDocId, $incrementOpts->initial(1));
// Decrement by 1
$collection->binary()->decrement($counterDocId);
// Decrement by 5
$collection->binary()->decrement($counterDocId, $decrementOpts->delta(5));
```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

```php
$result = $collection->get('counter-doc');
$value = $result->content();
$incrementAmnt = 5;

if (shouldIncrementValue($value)) {
    $opts = new ReplaceOptions();
    $opts->cas($result->cas());
    $collection->replace('counter-doc', $value + $incrementAmnt, $opts);
}
```

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]

### [](#use-cases)Use Cases

The SDK provides a high-level abstraction over the simple `incr()`/`decr()` of Couchbase Server’s memcached binary protocol, using `Collection→binary()`. This enables you to work with counters using `get()` and `upsert()` operations — allowing, _inter alia_, the use of durability options with the operations. You will find several ways of working with counters [in the API docs](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-BinaryCollection.html).

Unresolved include directive in modules/concept-docs/pages/documents.adoc - include::7.5@sdk:shared:partial$documents.adoc\[\]