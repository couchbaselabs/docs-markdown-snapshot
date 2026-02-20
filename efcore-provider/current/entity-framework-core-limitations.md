---
title: Couchbase EFCore Provider Limitations
description: The Couchbase EFCore Provider is still evolving and does not
  currently support all features of EF Core or Couchbase.
editUrl: https://github.com/couchbase/docs-efcore/edit/release/1.0/modules/ROOT/pages/entity-framework-core-limitations.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:efcore-provider::entity-framework-core-limitations.adoc[]
---

[View original HTML](/efcore-provider/current/entity-framework-core-limitations.html)

# Couchbase EFCore Provider Limitations

> The Couchbase EFCore Provider is still evolving and does not currently support all features of EF Core or Couchbase. We recommend reviewing the known limitations to avoid potential issues and ensure a smooth development experience. 

## [](#unsupported-ef-core-features)Unsupported EF Core Features

* [Eager loading/fetching](https://learn.microsoft.com/en-us/ef/core/querying/related-data/eager) — use the `Include` and/or `ThenInclude` methods to specify related data to be included in query results.
* [Value generation](https://learn.microsoft.com/en-us/ef/core/modeling/generated-properties?tabs=data-annotations) — auto-generated values for properties and or primary keys.
* [Migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/?tabs=dotnet-core-cli) — The migrations feature in EF Core provides a way to incrementally update the database schema to keep it in sync with the application’s data model while preserving existing data in the database.
* [Table splitting](https://learn.microsoft.com/en-us/ef/core/modeling/table-splitting) — EF Core allows to map two or more entities to a single row. This is called table splitting or table sharing.
* Any features not explicitly mentioned in this documentation

## [](#unsupported-couchbase-features)Unsupported Couchbase Features

* All queries use [NOT\_BOUNDED](../../dotnet-sdk/current/concept-docs/n1ql-query.md#index-consistency). This means that the query will not wait for the index to be updated before returning results. This is the default behavior for Couchbase queries.
* Only [default values](../../dotnet-sdk/current/howtos/n1ql-queries-with-sdk.md#query-options) are used for all queries generated and executed against Couchbase.
* Only [default values](../../dotnet-sdk/current/ref/client-settings.md) are used for K/V CRUD operations.
* [Transactions](../../dotnet-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md) are not currently supported.
* [Enhanced durability](../../dotnet-sdk/current/concept-docs/durability-replication-failure-considerations.md#durability) is not currently supported.
* [Compare and swap (CAS)](../../dotnet-sdk/current/howtos/concurrent-document-mutations.md) is not currently supported.
* [Pessimistic locking](../../dotnet-sdk/current/howtos/concurrent-document-mutations.md#pessimistic-locking) is not currently supported.
* [Field level encryption](../../dotnet-sdk/current/concept-docs/encryption.md) is not currently supported.
* [XATTR and Virtual XATTR](../../dotnet-sdk/current/concept-docs/xattr.md) are not currently supported.
* [Sub-Document](../../dotnet-sdk/current/concept-docs/subdocument-operations.md) operations are not currently supported.
* [Non-JSON Document types](../../dotnet-sdk/current/concept-docs/nonjson.md) are not currently supported.

## [](#only-async-queries-supported)Only Async Queries Supported

Limitations on the Couchbase SDK mean that only async queries are supported. If a sync query is attempted, a `NotImplementedException` will be thrown with the following message:

"Couchbase EF Core Database Provider does not support synchronous I/O.
Make sure to use and correctly await only async methods when using Entity Framework
Core to access Couchbase database. See Couchbase EF Core Database Provider
documentation for more information."

All async queries are expected to be awaited. Avoid using `Wait()` or `Result()` on async queries, as this is the [sync-over-async anti-pattern](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/synchronous-io/)and leads to deadlocks and thread pool starvation.

## [](#subdocument-denormalization-not-supported)Subdocument (Denormalization) Not Supported

The Couchbase EF Core Provider maps to Couchbase’s JSON document model, which is not a relational model. This means that some features of EF Core may not work as expected, and data may not be saved as expected. For example, if you have a one-to-many relationship and you delete the parent entity, the child entities may not be deleted as well. This is because Couchbase does not have the concept of foreign keys or cascading deletes.

It is important to understand the limitations of the Couchbase EF Core Provider and to use it accordingly.

Additionally, parent JSON and chlidren document are stored in their own [Collections](https://docs.couchbase.com/server/current/learn/data/scopes-and-collections.html). Consider the following JSON document; in this case we have a parent document that represents a person and a child document that represents a child of that person. If the child document does not have a primary key, it will be lost when the parent document is saved. This is because EF Core will not be able to find the child document and it will not be saved to the database. Additionally, two collections must exist in Couchbase: `parent` and `child`.

Now take this document for example:

```json
{
  "id": "1",
  "name": "John Doe",
  "children": [
    {
      "name": "Jane Doe"
    }
  ]
}
```

In this document, the child document does not have an id, so it will be lost when the parent document is saved even if both collections exist. To fix this, you need to ensure that the child document has an id, like so:

```json
{
  "id": "1",
  "name": "John Doe",
  "children": [
    {
      "id": "2",
      "name": "Jane Doe"
    }
  ]
}
```

This will be mapped to the following entities:

```csharp
public class Person
{
    public string Id { get; set; }
    public string Name { get; set; }
    public List<Child> Children { get; set; }
}

public class Child
{
    public string Id { get; set; }
    public string Name { get; set; }
}
```

In the a `DbContext.OnModelCreating` method, you would configure the entities like this:

```csharp
builder.Entity<Person>().ToCouchbaseCollection(this, "parent");
builder.Entity<Child>().ToCouchbaseCollection(this, "child");
```

## [](#avoid-dynamic-or-object-type-properties)Avoid Dynamic or Object Type Properties

The dynamic and/or the System.Object type can be used as a property type in EF Core. This is not recommended for Couchbase, as it will not be able to map the property to a JSON document. This is the actual type of the field can only be determined at runtime. It is recommended to use a specific type for the property, such as a string or a number.

## [](#unsupported-linq-queries)Unsupported LINQ Queries

LINQ queries can be a near unlimited variety of queries, and the EF Core Couchbase DB Provider does not support all of them. If a lambda expression cannot be translated into a SQL++ statement, then query will error out with a `InvalidOperationException` and a message similar to the following:

System.InvalidOperationException
The LINQ expression 'DbSet<Customer>()
    .Where(c => (int)DbSet<Order>()
        .Where(o => o.CustomerID == "John Doe")
        .Select(o => (int?)o.CustomerID.Length)
        .FirstOrDefault() == 0)' could not be translated. Either rewrite the query in a form that can be translated, or switch to client evaluation explicitly by inserting a call to 'AsEnumerable', 'AsAsyncEnumerable', 'ToList', or 'ToListAsync'. See https://go.microsoft.com/fwlink/?linkid=2101038 for more information.`

Note that while the error message indicates that the query cannot re-rewritten using `AsEnumerable` or `ToList`, this is not a supported feature of the EF Core Couchbase DB Provider as it is sync-over-async.