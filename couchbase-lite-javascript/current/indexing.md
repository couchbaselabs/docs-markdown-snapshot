---
title: Indexing
description: Couchbase Lite JavaScript -- Indexing for Query Performance
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/indexing.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite-javascript/current/indexing.html)

# Indexing

> Description — _Couchbase Lite JavaScript — Indexing for Query Performance_  
> Related Content — [SQL++ for Mobile](query-n1ql-mobile.md) | [Query Resultsets](query-resultsets.md) | [Live Queries](query-live.md)

## [](#overview)Overview

Indexes speed up queries by creating efficient lookup structures for your data. Without indexes, queries must scan every document in a collection, which becomes slow as your data grows.

Couchbase Lite JavaScript uses IndexedDB’s native indexing capabilities, which provides fast query performance but has some unique constraints compared to native Couchbase Lite platforms.

## [](#indexing-constraints)IndexedDB Indexing Constraints

> [!IMPORTANT]
> Due to IndexedDB requirements, indexes must be declared when opening the database. You cannot create or delete indexes while the database is open.

**Key Constraints:**

* **Declaration at Open Time** \- All indexes must be specified in the `DatabaseConfig` when calling `Database.open()`
* **Limited Data Types** \- Only numbers, strings, and arrays of these types can be indexed
* **No Dynamic Index Management** \- Cannot add or remove indexes without closing and reopening the database
* **Per-Collection Indexes** \- Each collection has its own set of indexes

## [](#declaring-indexes)Declaring Indexes

Indexes are declared in the collection configuration when opening the database:

Example 1\. Basic index declaration

```javascript
const config: DatabaseConfig = {
    name: 'myapp',
    version: 1,
    collections: {
        products: {
            indexes: ['name', 'price', 'category']
        }
    }
};

const db = await Database.open(config);
```

## [](#index-types)Index Types

### [](#property-indexes)Property Indexes

The most common type of index is a property index, which indexes a single document property:

Example 2\. Property indexes

```javascript
const productConfig: DatabaseConfig = {
    name: 'store',
    version: 1,
    collections: {
        products: {
            indexes: [
                'sku',        // Product SKU
                'price',      // Product price
                'inStock'     // Stock status
            ]
        }
    }
};
```

### [](#array-indexes)Array Indexes

You can index array properties to enable efficient queries on array contents:

Example 3\. Array indexes

```javascript
const articleConfig: DatabaseConfig = {
    name: 'blog',
    version: 1,
    collections: {
        articles: {
            indexes: [
                'tags',       // Array of tags
                'categories'  // Array of categories
            ]
        }
    }
};
```

### [](#nested-property-indexes)Nested Property Indexes

Index nested object properties using dot notation:

Example 4\. Nested property indexes

```javascript
const userConfig: DatabaseConfig = {
    name: 'app',
    version: 1,
    collections: {
        users: {
            indexes: [
                'profile.name',
                'profile.email',
                'address.city',
                'address.country'
            ]
        }
    }
};
```

### [](#compound-indexes)Compound Indexes

While IndexedDB doesn’t support true compound indexes, you can create multiple single-property indexes that work together:

Example 5\. Multiple indexes

```javascript
const orderConfig: DatabaseConfig = {
    name: 'orders',
    version: 1,
    collections: {
        orders: {
            indexes: [
                'customerId',     // Filter by customer
                'status',         // Filter by status
                'orderDate',      // Sort by date
                'totalAmount'     // Sort/filter by amount
            ]
        }
    }
};
```

## [](#typescript-indexes)TypeScript Schema with Indexes

When using TypeScript, declare both your document schema and indexes together:

Example 6\. Type-safe indexes

```typescript
interface Product {
    sku: string;
    name: string;
    price: number;
    category: string;
    tags: string[];
}

interface StoreSchema {
    products: Product;
}

// Configure with type-safe indexes
const storeConfig: DatabaseConfig<StoreSchema> = {
    name: 'store',
    version: 1,
    collections: {
        products: {
            indexes: ['sku', 'price', 'category', 'tags']
        }
    }
};

const storeDb = await Database.open(storeConfig);
```

## [](#modifying-indexes)Modifying Indexes

To add or remove indexes, you must close and reopen the database with the new configuration:

Example 7\. Modify indexes

```javascript
// Close database first
database.close();

// Reopen with new indexes
const updatedConfig: DatabaseConfig = {
    name: 'myapp',
    version: 2,  // Increment version
    collections: {
        products: {
            indexes: [
                'name',
                'price',
                'category',
                'manufacturer'  // New index added
            ]
        }
    }
};

const updatedDb = await Database.open(updatedConfig);
```

## [](#index-selection)How Queries Use Indexes

Couchbase Lite automatically selects appropriate indexes for your queries. The query optimizer:

1. Analyzes the WHERE clause
2. Identifies indexed properties used in the query
3. Selects the most efficient index
4. Falls back to collection scanning if no suitable index exists

## [](#indexable-types)Indexable Data Types

IndexedDB can only index certain data types:

**Indexable Types:**

* **Numbers** \- Integers and floating-point values
* **Strings** \- Text values
* **Arrays** \- Arrays containing numbers or strings

**Non-Indexable Types:**

* Objects (nested documents)
* Booleans
* Dates (must be converted to numbers or strings)
* null values
* Blobs

Example 8\. Handling dates in indexes

```javascript
interface Event {
    title: string;
    startDate: string;      // ISO date string: "2024-01-15T10:00:00Z"
    timestamp: number;      // Unix timestamp: 1705315200000
}

const eventConfig: DatabaseConfig = {
    name: 'events',
    version: 1,
    collections: {
        events: {
            indexes: [
                'startDate',    // Index ISO date string
                'timestamp'     // Index numeric timestamp
            ]
        }
    }
};

const db = await Database.open(eventConfig);
```

## [](#index-maintenance)Index Maintenance

**Automatic Updates:**

* Indexes update automatically when documents are saved
* No manual maintenance required
* Updates happen synchronously during document saves

**Performance Impact:**

* More indexes = slower write operations
* Each indexed property adds overhead to saves
* Balance query performance vs. write performance

## [](#query-optimization)Query Optimization Strategies

### [](#use-indexes-effectively)Use Indexes Effectively

Structure queries to take advantage of indexes:

Example 9\. Indexed query

```javascript
const indexedQuery = database.createQuery(`
    SELECT *
    FROM products
    WHERE category = 'electronics' -- Uses category index
    ORDER BY price -- Uses price index
    LIMIT 50
`);

const results = await indexedQuery.execute();
```

### [](#avoid-full-scans)Avoid Full Collection Scans

Queries without indexed properties scan the entire collection:

Example 10\. Unindexed query (slow)

```javascript
const unindexedQuery = database.createQuery(`
    SELECT *
    FROM products
    WHERE description LIKE '%wireless%' -- No index on description
`);

// This will be slow on large datasets
const slowResults = await unindexedQuery.execute();
```

### [](#limit-results)Use LIMIT for Large Result Sets

Even with indexes, limit results for better performance:

Example 11\. Limited query

```javascript
const limitedQuery = database.createQuery(`
    SELECT *
    FROM products
    WHERE category = $category
    ORDER BY price DESC LIMIT 20
    OFFSET $offset
`);

// Fetch first page
limitedQuery.parameters = {
    category: 'electronics',
    offset: 0
};
const page1 = await limitedQuery.execute();

// Fetch next page
limitedQuery.parameters = {
    category: 'electronics',
    offset: 20
};
const page2 = await limitedQuery.execute();
```

## [](#indexing-patterns)Common Indexing Patterns

### [](#email-username-pattern)Email/Username Lookups

Example 12\. Email lookup pattern

```javascript
const authConfig: DatabaseConfig = {
    name: 'auth',
    version: 1,
    collections: {
        users: {
            indexes: ['email', 'username']
        }
    }
};

// Fast lookup by email
const userQuery = database.createQuery(`
    SELECT *
    FROM users
    WHERE email = $email
`);

userQuery.parameters = {email: 'user@example.com'};
const user = await userQuery.execute();
```

### [](#status-filtering-pattern)Status Filtering

Example 13\. Status filter pattern

```javascript
const workflowConfig: DatabaseConfig = {
    name: 'workflow',
    version: 1,
    collections: {
        tasks: {
            indexes: ['status', 'priority', 'assignedTo']
        }
    }
};

// Query by status
const activeTasksQuery = database.createQuery(`
    SELECT *
    FROM tasks
    WHERE status IN ('pending', 'in-progress')
      AND assignedTo = $userId
    ORDER BY priority DESC
`);
```

### [](#date-range-pattern)Date Range Queries

Example 14\. Date range pattern

```javascript
const analyticsConfig: DatabaseConfig = {
    name: 'analytics',
    version: 1,
    collections: {
        events: {
            indexes: ['timestamp', 'eventType']
        }
    }
};

// Query date range
const dateRangeQuery = database.createQuery(`
    SELECT *
    FROM events
    WHERE timestamp >= $startDate
      AND timestamp <= $endDate
    ORDER BY timestamp DESC
`);

dateRangeQuery.parameters = {
    startDate: Date.now() - (7 * 24 * 60 * 60 * 1000),  // 7 days ago
    endDate: Date.now()
};
const recentEvents = await dateRangeQuery.execute();
```

### [](#category-filtering-pattern)Category Filtering

Example 15\. Category filter pattern

```javascript
const catalogConfig: DatabaseConfig = {
    name: 'catalog',
    version: 1,
    collections: {
        products: {
            indexes: ['category', 'subcategory', 'brand']
        }
    }
};

// Hierarchical category query
const categoryQuery = database.createQuery(`
    SELECT *
    FROM products
    WHERE category = $category
      AND subcategory = $subcategory
    ORDER BY name
`);

categoryQuery.parameters = {
    category: 'electronics',
    subcategory: 'laptops'
};
const laptops = await categoryQuery.execute();
```

## [](#limitations)Indexing Limitations

**Missing Features:**

* **No Full-Text Search Indexes** \- FTS with `MATCH()` not available
* **No Vector Indexes** \- Vector search without indexes is very slow
* **No Partial Indexes** \- Cannot index subset of documents
* **No Expression Indexes** \- Only property values can be indexed
* **No Multi-Property Compound Indexes** \- Each index is single-property

**Workarounds:**

* For FTS: Consider using a JavaScript FTS library and storing results
* For vector search: Use `EUCLIDEAN_DISTANCE()` on small datasets only
* For partial indexes: Filter in WHERE clause instead
* For expression indexes: Store computed values as properties

## [](#performance-testing)Performance Testing

Always test index effectiveness with realistic data:

Example 16\. Performance testing pattern

```javascript
async function testQueryPerformance() {
    // Test without index
    const startUnindexed = performance.now();
    const unindexedResults = await database.createQuery(`
        SELECT *
        FROM products
        WHERE description LIKE '%test%'
    `).execute();
    const timeUnindexed = performance.now() - startUnindexed;

    console.log(`Unindexed query: ${timeUnindexed.toFixed(2)}ms`);
    console.log(`Results: ${unindexedResults.length}`);

    // Test with index
    const startIndexed = performance.now();
    const indexedResults = await database.createQuery(`
        SELECT *
        FROM products
        WHERE category = 'electronics'
    `).execute();
    const timeIndexed = performance.now() - startIndexed;

    console.log(`Indexed query: ${timeIndexed.toFixed(2)}ms`);
    console.log(`Results: ${indexedResults.length}`);
    console.log(`Speedup: ${(timeUnindexed / timeIndexed).toFixed(1)}x`);
}
```

## [](#debugging-indexes)Debugging Index Issues

**Query Not Using Index:**

1. Verify property name matches index exactly
2. Ensure indexed property is used in WHERE clause
3. Check that query condition is compatible with indexing

**Slow Queries Despite Indexes:**

1. Check index selectivity (too many duplicate values?)
2. Verify result set size (use LIMIT if appropriate)
3. Monitor IndexedDB performance in browser DevTools
4. Consider simplifying complex queries

**Index Declaration Errors:**

1. Verify indexes declared in DatabaseConfig
2. Check property names for typos
3. Ensure database version increments when changing indexes
4. Verify database successfully reopened with new config

## [](#migration-strategy)Index Migration Strategy

When adding indexes to existing databases:

Example 17\. Index migration

```javascript
async function migrateIndexes() {
    // Step 1: Check current version
    const currentDb = await Database.open({
        name: 'myapp',
        version: 1,
        collections: {
            products: {
                indexes: ['name']
            }
        }
    });

    console.log('Current version:', currentDb.config.version);

    // Step 2: Close database
    currentDb.close();

    // Step 3: Reopen with new indexes and incremented version
    const migratedDb = await Database.open({
        name: 'myapp',
        version: 2,
        collections: {
            products: {
                indexes: [
                    'name',
                    'price',      // New index
                    'category'    // New index
                ]
            }
        }
    });

    console.log('Migrated to version:', migratedDb.config.version);

    return migratedDb;
}

await migrateIndexes();
```

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)

.

### [](#-2)

Learn more . . .

* [SQL++ for Mobile](query-n1ql-mobile.md)
* [Query Resultsets](query-resultsets.md)
* [Live Queries](query-live.md)
* [Databases](database.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.