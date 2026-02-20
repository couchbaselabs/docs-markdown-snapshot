---
title: Querying with the EF Core Couchbase DB Provider
description: Querying the database with SQL++.
editUrl: https://github.com/couchbase/docs-efcore/edit/release/1.0/modules/ROOT/pages/entity-framework-core-queries.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:efcore-provider::entity-framework-core-queries.adoc[]
---

[View original HTML](/efcore-provider/current/entity-framework-core-queries.html)

# Querying with the EF Core Couchbase DB Provider

> Querying the database with SQL++. 

## [](#querying-basics)Querying basics

[EF Core LINQ queries](https://learn.microsoft.com/en-us/ef/core/querying/) can be executed against EF Core Couchbase DB in the same way as for other database providers. For example:

```csharp
public class Session
{
    public Guid Id { get; set; }
    public string Category { get; set; }

    public string TenantId { get; set; } = null!;
    public Guid UserId { get; set; }
    public int SessionId { get; set; }
}

var stringResults = await context.Sessions
    .Where(
        e => e.Category.Length > 4
            && e.Category.Trim().ToLower() != "disabled"
            && e.Category.TrimStart().Substring(2, 2).Equals("xy", StringComparison.OrdinalIgnoreCase))
    .ToListAsync();
```

## [](#joins)Joins

The LINQ Join operator allows you to connect two data sources based on the key selector for each source, generating a tuple of values when the key matches. It naturally translates to `INNER JOIN` on relational databases. While the LINQ Join has outer and inner key selectors, the database requires a single join condition. So EF Core generates a join condition by comparing the outer key selector to the inner key selector for equality.

```csharp
var query = from photo in context.Set<PersonPhoto>()
    join person in context.Set<Person>()
        on photo.PersonPhotoId equals person.PhotoId
    select new { person, photo };
```

The SQL++ generated looks like this:

```csharp
SELECT `p0`.`PersonId`, `p0`.`Name`, `p0`.`PhotoId`, `p`.`PersonPhotoId`, `p`.`Caption`, `p`.`Photo`
FROM `Blogging`.`MyBlog`.`PersonPhoto` AS `p`
INNER JOIN `Blogging`.`MyBlog`.`Person` AS `p0` ON `p`.`PersonPhotoId` = `p0`.`PhotoId`
```

## [](#firstasync)FirstAsync

```csharp
var session = await context.Sessions.FirstAsync(x => x.SessionId == 2);
```

## [](#pagination)Pagination

Pagination refers to retrieving results in pages, rather than all at once; this is typically done for large resultsets, where a user interface is displayed, allowing users to navigate through pages of the results.

A common way to implement pagination with databases is to use the Skip and Take LINQ operators (OFFSET and LIMIT in SQL++). Given a page size of 10 results, the third page can be fetched with EF Core as follows:

```csharp
var position = 20;
var nextPage = await context.Sessions
    .OrderBy(s => s.Id)
    .Skip(position)
    .Take(10)
    .ToListAsync();
```

## [](#aggregation)Aggregation

Aggregation functions such as SUM can be combined with `GROUPBY`:

```csharp
var query = from s in _context.Students
    group s by s.EnrollmentDate
    into grp
    select new EnrollmentDateGroup { EnrollmentDate = grp.Key, StudentCount = grp.Count() };
```

## [](#first-async)First Async

[FindAsync](https://learn.microsoft.com/en-us/ef/core/change-tracking/entity-entries#find-and-findasync) is a useful API for getting an entity by its primary key, and avoiding a database roundtrip when the entity has already been loaded and is tracked by the context:

```csharp
public class Session
{
    public Guid Id { get; set; }
    ...
}

var mySession = await context.FindAsync(pkey);
```

> [!NOTE]
> Use `FindAsync` only when the entity might already be tracked by your context, and you want to avoid the database roundtrip. Otherwise, simply use `SingleAsync` — there is no performance difference between the two when the entity needs to be loaded from the database.

## [](#group-by)Group By

EF Core also translates queries where an aggregate operator on the grouping appears in a `WHERE` or `OrderBy` (or other ordering) LINQ operator. It uses `HAVING` clause in SQL for the `WHERE` clause. The part of the query before applying the `GroupBy` operator can be any complex query as long as it can be translated to server. Furthermore, once you apply aggregate operators on a grouping query to remove groupings from the resulting source, you can compose on top of it like any other query.

```csharp
var query = from s in _context.Students
    group s by s.EnrollmentDate
    into grp
    select new EnrollmentDateGroup { EnrollmentDate = grp.Key, StudentCount = grp.Count() };
```

Which is translated into the following SQL++ statement:

```csharp
SELECT `p`.`AuthorId` AS `Key`, COUNT(*) AS `Count`
FROM `Blogging`.`MyBlog`.`Posts` AS `p`
GROUP BY `p`.`AuthorId`
HAVING COUNT(*) > 0
ORDER BY `p`.`AuthorId`
```

## [](#supported-aggregate-operators)Supported Aggregate operators

The following aggregate operators are supported by the 1.0 release:

__Table 1\. Table Supported Aggregate operators__
| .NET                    | SQL++         |
| ----------------------- | ------------- |
| Average(x ⇒ x.Property) | AVG(Property) |
| Count()                 | COUNT(\*)     |
| LongCount()             | COUNT(\*)     |
| Max(x ⇒ x.Property)     | MAX(Property) |
| Min(x ⇒ x.Property)     | MIN(Property) |
| Sum(x ⇒ x.Property)     | SUM(Property) |

Other operators may or may not be supported in the 1.0 release.

## [](#sql-queries)SQL queries

### [](#sqlraw)SqlRaw

`DbContext.SqlRaw` is not implemented as of the EF Core Couchbase DB Provider 1.0 release because it depends on ADO.NET parameters which are minimally supported in the initial release.

> [!NOTE]
> `DbContext.FromSql` will throw a `NotImplementedException` in EF Core Couchbase DB Provider 1.0\.

### [](#fromsqlraw)FromSqlRaw

If you’ve decided you do want to dynamically construct your SQL, you’ll have to use `DbContext.FromSqlRaw`, which allows interpolating variable data directly into the SQL string, instead of using a database parameter:

```csharp
string query = "SELECT p.* FROM `Blogging`.`MyBlog`.`Person` as p WHERE PersonId={0}";
var person = await context.Set<Person>()
    .FromSqlRaw(query, 1)
    .FirstOrDefaultAsync();
```

### [](#meta-support)META Support

The [META function](../../server/current/n1ql/n1ql-language-reference/metafun.md#meta) is supported in the EF Core Couchbase DB Provider version 1.0\. Hhowever, lamda expression is not supported. This means you will need to use the `FromSqlRaw` method to execute the query.

```csharp
using (var context = new BloggingContext())
{
    await _couchbaseFixture.InitializeBloggingAsync();
    var statement = "SELECT `b`.* FROM `Content`.`Blogs`.`Blog` as `b` WHERE META().id = \"2\"";
    var blog = await context.Blogs.FromSqlRaw(statement).AsNoTracking().FirstOrDefaultAsync();

    Assert.NotNull(blog);
}
```

> [!TIP]
> In addition to META, other SQL++ functions not yet supported in the EF Core Couchbase DB Provider may be executed in a similar way.