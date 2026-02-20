---
title: Handling Data Conflicts
description: Couchbase Lite JavaScript -- Handling conflict between data changes
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/conflict.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:couchbase-lite-javascript::conflict.adoc[]
---

[View original HTML](/couchbase-lite-javascript/current/conflict.html)

# Handling Data Conflicts

> Description — _Couchbase Lite JavaScript — Handling conflict between data changes_  
> Related Content — [Remote Sync Gateway](replication.md) | [CORS Configuration](cors-configuration.md)

## [](#causes-of-conflicts)Causes of Conflicts

Document conflicts can occur if multiple changes are made to the same version of a document by multiple peers in a distributed system. For Couchbase Mobile, this can be a Couchbase Lite or Sync Gateway database instance.

Such conflicts can occur after either of the following events:

* **A replication saves a document change** — in which case the change with the _most-revisions wins_ (unless one change is a delete). See [Case 1: Conflicts when a replication is in progress](#lbl-conflicts-when-replicating)
* **An application saves a document change directly to a database instance** — in which case, _last write wins_, unless one change is a delete — see [Case 2: Conflicts when saving a document](#conflicts-when-saving)

> [!NOTE]
> **_Deletes_ always win.** So, in either of the above cases, if one of the changes was a _Delete_ then that change wins.

The following sections discuss each scenario in more detail.

> [!TIP]
> Dive deeper …​
> 
> Read more about [Document Conflicts and Automatic Conflict Resolution in Couchbase Mobile](https://blog.couchbase.com/document-conflicts-couchbase-mobile).

## [](#lbl-conflicts-when-replicating)Conflicts when Replicating

There’s no practical way to prevent a conflict when incompatible changes to a document are made in multiple instances of an app. The conflict is realized only when replication propagates the incompatible changes to each other.

Example 1\. A typical cause of replication conflicts:

1. Alice uses her device to create _DocumentA_.
2. Replication syncs _DocumentA_ to Bob’s device.
3. Alice uses her device to apply _ChangeX_ to _DocumentA_.
4. Bob uses his device to make a different change, _ChangeY_, to _DocumentA_.
5. Replication syncs _ChangeY_ to Alice’s device.  
This device already has _ChangeX_ putting the local document in conflict.
6. Replication syncs _ChangeX_ to Bob’s device.  
This device already has _ChangeY_ and now Bob’s local document is in conflict.

### [](#automatic-conflict-resolution)Automatic Conflict Resolution

> [!NOTE]
> The rules only apply to conflicts caused by replication. Conflict resolution takes place exclusively during pull replication, while push replication remains unaffected.

Couchbase Lite uses the following rules to handle conflicts such as those described in [Example 1](#typical-conflict-scenario):

* If one of the changes is a deletion:  
A deleted document (that is, a _tombstone_) always wins over a document update.
* If both changes are document changes:  
The change with the most revisions wins. If both have the same number of revisions, a deterministic algorithm is used to pick a winner.

The result is saved internally by the Couchbase Lite replicator. Those rules describe the internal behavior of the replicator. For additional control over the handling of conflicts, including when a replication is in progress, see [Custom Conflict Resolution](#custom-conflict-resolution).

### [](#custom-conflict-resolution)Custom Conflict Resolution

Application developers who want more control over how document conflicts are handled can use custom logic to select the winner between conflicting revisions of a document.

If a custom conflict resolver is not provided, the system will automatically resolve conflicts as discussed in [Automatic Conflict Resolution](#automatic-conflict-resolution).

> [!CAUTION]
> Custom conflict handlers should be optimized and fast. Time-consuming conflict resolution can slow down the replication process significantly.

To implement custom conflict resolution during replication, you create a conflict resolver function and configure it on the replicator.

#### [](#conflict-resolver)Conflict Resolver

Apps have the following strategies for resolving conflicts:

* **Local Wins:** The current revision in the database wins.
* **Remote Wins:** The revision pulled from the remote endpoint through replication wins.
* **Merge:** Merge the content of the conflicting revisions.

Example 2\. Conflict Resolution Strategies

* Local Wins
* Remote Wins
* Merge
* Delete

```javascript
const localWinsResolver: PullConflictResolver = async (local, remote) => {
    return local;
};
```

```javascript
const remoteWinsResolver: PullConflictResolver = async (local, remote) => {
    return remote;
};
```

```javascript
    const mergeResolver: PullConflictResolver = async (local, remote) => {
        if (local && remote) {
            return { ...local, ...remote } as CBLDocument;
        } else {
            return local ?? remote;
        }
    };

    const deleteResolver: PullConflictResolver = async (local, remote) => {
        return null;
    };

    // tag::conflict-resolver-config
    const config: ReplicatorConfig = {
        database: database as unknown as Database,
        url: 'wss://sync-gateway.example.com:4984/myapp',
        collections: {
            tasks: {
                pull: { conflictResolver: remoteWinsResolver, continuous: true },
                push: { continuous: true}
            }
        }
    };
    // end::conflict-resolver-config
}

{
    // Configure logging
    await logtape.configure({
        sinks: {
            console: logtape.getConsoleSink(),
        },
        loggers: [
            {
                category: LogCategory,
                lowestLevel: 'info',
                sinks: ['console'],
            }
        ],
    });
}

{
    // Configure logging for database operations
    await logtape.configure({
        sinks: {
            console: logtape.getConsoleSink(),
        },
        loggers: [
            {
                category: [LogCategory, 'DB'],
                lowestLevel: 'debug',
                sinks: ['console'],
            }
        ],
    });
}

{
    // Configure logging for queries
    await logtape.configure({
        sinks: {
            console: logtape.getConsoleSink(),
        },
        loggers: [
            {
                category: [LogCategory, 'Query'],
                lowestLevel: 'debug',
                sinks: ['console'],
            }
        ],
    });
}

{
    // Declare indexes when opening database
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
}

{
    // Index individual properties
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
}

{
    // Index array properties
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
}

{
    // Index nested object properties using dot notation
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
}

{
    // Create multiple indexes for complex queries
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
}

{
    // Define schema with TypeScript
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
}

{
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
}

{
    // Store dates as ISO strings or timestamps
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
}

{
    // High selectivity: many unique values
    const emailConfig: DatabaseConfig = {
        name: 'users',
        version: 1,
        collections: {
            users: {
                indexes: [
                    'email',      // Unique per user - excellent selectivity
                    'userId',     // Unique - excellent selectivity
                    'ssn'         // Unique - excellent selectivity
                ]
            }
        }
    };

    const db = await Database.open(emailConfig);
}

{
    // Low selectivity: few unique values
    const taskConfig: DatabaseConfig = {
        name: 'tasks',
        version: 1,
        collections: {
            tasks: {
                // Not recommended: boolean has only 2 possible values
                indexes: ['completed']  // Low selectivity
            }
        }
    };

    const db = await Database.open(taskConfig);

    // Better: combine with high-selectivity queries
    const query = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE completed = false AND assignedTo = $userId -- High selectivity filter
    `);
}

{
    // Check IndexedDB storage usage
    if (navigator.storage && navigator.storage.estimate) {
        const {quota = 0, usage = 0} = await navigator.storage.estimate();
        const quotaGB = (quota / (1024 ** 3)).toFixed(2);
        const usageGB = (usage / (1024 ** 3)).toFixed(2);
        const percentUsed = ((usage / quota) * 100).toFixed(1);

        console.log(`Storage: ${usageGB} GB / ${quotaGB} GB (${percentUsed}%)`);
    }
}

{
    // Query that uses indexes efficiently
    const indexedQuery = database.createQuery(`
        SELECT *
        FROM products
        WHERE category = 'electronics' -- Uses category index
        ORDER BY price -- Uses price index
        LIMIT 50
    `);

    const results = await indexedQuery.execute();
}

{
    // Query without index - scans entire collection
    const unindexedQuery = database.createQuery(`
        SELECT *
        FROM products
        WHERE description LIKE '%wireless%' -- No index on description
    `);

    // This will be slow on large datasets
    const slowResults = await unindexedQuery.execute();
}

{
    // Use LIMIT for pagination and performance
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
}

{
    // Email/username lookup pattern
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
}

{
    // Status filtering pattern
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
}

{
    // Date range query pattern
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
}

{
    // Category filtering pattern
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
}

{
    // Performance testing pattern
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
}

{
    // Migration strategy for adding indexes
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
}

{
    const query = database.createQuery('SELECT * FROM tasks');
    const results = await query.execute();

    const allQuery = database.createQuery('SELECT * FROM tasks');
    const allResults = await allQuery.execute();

    const propsQuery = database.createQuery(`
        SELECT title, completed, createdAt
        FROM tasks
    `);
    const propResults = await propsQuery.execute();

    // Simple WHERE clause
    const whereQuery = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE completed = false
    `);

    // Multiple conditions
    const multiWhereQuery = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE completed = false
          AND type = 'urgent'
    `);

    // Using AND
    const andQuery = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE completed = false
          AND priority = 'high'
    `);

    // Using OR
    const orQuery = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE priority = 'high'
           OR priority = 'critical'
    `);

    // Using NOT
    const notQuery = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE NOT completed
    `);

    // LIKE with wildcards
    const likeQuery = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE title LIKE 'Learn%'
    `);

    // Contains pattern
    const containsQuery = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE title LIKE '%Couchbase%'
    `);

    // Single character wildcard
    const singleQuery = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE title LIKE 'Task_'
    `);

    // Regular expression matching
    const regexQuery = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE REGEXP_LIKE(title, '^[A-Z].*')
    `);

    // Check if contains pattern
    const regexContainsQuery = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE REGEXP_CONTAINS(description, 'important|urgent')
    `);

    // Order ascending
    const ascQuery = database.createQuery(`
        SELECT *
        FROM tasks
        ORDER BY createdAt ASC
    `);

    // Order descending
    const descQuery = database.createQuery(`
        SELECT *
        FROM tasks
        ORDER BY createdAt DESC
    `);

    // Multiple order columns
    const multiOrderQuery = database.createQuery(`
        SELECT *
        FROM tasks
        ORDER BY priority DESC, createdAt ASC
    `);

    // Limit results
    const limitQuery = database.createQuery(`
        SELECT *
        FROM tasks LIMIT 10
    `);

    // Pagination with LIMIT and OFFSET
    const pageQuery = database.createQuery(`
        SELECT *
        FROM tasks
        ORDER BY createdAt DESC LIMIT 20
        OFFSET 40
    `);

    // LEFT OUTER JOIN
    const joinQuery = database.createQuery(`
        SELECT tasks.title, users.username
        FROM tasks
                 LEFT OUTER JOIN users ON tasks.assignedTo = users._id
        WHERE tasks.completed = false
    `);

    const joinResults = await joinQuery.execute();

    // GROUP BY with aggregate function
    const groupQuery = database.createQuery(`
        SELECT status, COUNT(*) AS count
        FROM tasks
        GROUP BY status
    `);

    // GROUP BY with HAVING clause
    const havingQuery = database.createQuery(`
        SELECT assignedTo, COUNT(*) AS taskCount
        FROM tasks
        GROUP BY assignedTo
        HAVING COUNT(*) > 5
    `);

    // Array functions
    const arrayQuery = database.createQuery(`
        SELECT title,
               ARRAY_LENGTH(tags)             AS tagCount,
               ARRAY_CONTAINS(tags, 'urgent') AS isUrgent
        FROM tasks
        WHERE ARRAY_LENGTH(tags) > 0
    `);

    // Array aggregation
    const arrayAggQuery = database.createQuery(`
        SELECT category,
               ARRAY_AGG(title) AS titles
        FROM tasks
        GROUP BY category
    `);

    // String manipulation
    const stringQuery = database.createQuery(`
        SELECT UPPER(title)  AS upperTitle,
               LOWER(title)  AS lowerTitle,
               LENGTH(title) AS titleLength,
               TRIM(title)   AS trimmedTitle
        FROM tasks
    `);

    // String concatenation
    const concatQuery = database.createQuery(`
        SELECT title || ' - ' || status AS fullTitle
        FROM tasks
    `);

    // Date functions
    const dateQuery = database.createQuery(`
        SELECT title,
               STR_TO_MILLIS(createdAt) AS timestamp,
        MILLIS_TO_STR(STR_TO_MILLIS(createdAt)) AS formattedDate
        FROM tasks
    `);

    // Date arithmetic
    const dateRangeQuery = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE STR_TO_MILLIS(createdAt) > STR_TO_MILLIS($startDate)
          AND STR_TO_MILLIS(createdAt) < STR_TO_MILLIS($endDate)
    `);

    // Mathematical functions
    const mathQuery = database.createQuery(`
        SELECT title,
               ROUND(progress * 100) AS percentage,
               ABS(budget - spent)   AS difference,
               CEIL(duration / 24)   AS days,
               FLOOR(duration / 24)  AS wholeDays
        FROM tasks
    `);

    // Using POWER and SQRT
    const advMathQuery = database.createQuery(`
        SELECT title,
               POWER(priority, 2)   AS prioritySquared,
               SQRT(estimatedHours) AS sqrtHours
        FROM tasks
    `);

    // Type checking
    const typeCheckQuery = database.createQuery(`
        SELECT title,
               TYPE(metadata)     AS metadataType,
               ISSTRING(title)    AS isTitleString,
               ISNUMBER(priority) AS isPriorityNumber,
               ISARRAY(tags)      AS isTagsArray
        FROM tasks
    `);

    // Type conversion
    const typeConvertQuery = database.createQuery(`
        SELECT TOSTRING(priority)       AS priorityString,
               TONUMBER(estimatedHours) AS hours,
               TOBOOLEAN(completed)     AS isDone
        FROM tasks
    `);

    // Handling NULL and MISSING
    const conditionalQuery = database.createQuery(`
        SELECT title,
               IFNULL(assignedTo, 'unassigned')              AS assigned,
               IFMISSING(dueDate, 'no due date')             AS due,
               IFMISSINGORNULL(completedAt, 'not completed') AS completion
        FROM tasks
    `);

    // NULLIF and MISSINGIF
    const nullifQuery = database.createQuery(`
        SELECT title,
               NULLIF(status, 'unknown') AS validStatus,
               MISSINGIF(progress, 0)    AS nonZeroProgress
        FROM tasks
    `);

    // Simple CASE expression
    const caseQuery = database.createQuery(`
        SELECT title,
               CASE priority
                   WHEN 1 THEN 'Low'
                   WHEN 2 THEN 'Medium'
                   WHEN 3 THEN 'High'
                   ELSE 'Unknown'
                   END AS priorityLabel
        FROM tasks
    `);

    // Searched CASE expression
    const searchedCaseQuery = database.createQuery(`
        SELECT title,
               CASE
                   WHEN completed THEN 'Done'
                   WHEN dueDate < $now THEN 'Overdue'
                   WHEN dueDate < $soon THEN 'Due Soon'
                   ELSE 'On Track'
                   END AS taskStatus
        FROM tasks
    `);

    // Access document metadata
    const metaQuery = database.createQuery(`
        SELECT META().id       AS docId,
               META().sequence AS seq,
               title,
               completed
        FROM tasks
    `);

    // Filter by document ID
    const idQuery = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE META().id = $docId
    `);
}

{
    // Execute and return array of all results
    const query = database.createQuery('SELECT tasks.* FROM tasks WHERE completed = false');
    const results = await query.execute<Task>();

    console.log(`Found ${results.length} incomplete tasks`);

    for (const row of results) {
        console.log(`Task: ${row.title}`);
    }
}

{
    // Execute with callback for memory efficiency
    const query = database.createQuery('SELECT tasks.* FROM tasks WHERE completed = false');

    let count = 0;
    await query.execute<Task>(row => {
        console.log(`Task ${++count}: ${row.title}`);
        // Process each row without storing all in memory
    });

    console.log(`Processed ${count} tasks total`);
}

{
    // Get column names from query
    const query = database.createQuery(`
        SELECT title, completed, createdAt
        FROM tasks
    `);

    const columnNames = query.columnNames;
    console.log('Columns:', columnNames);  // ['title', 'completed', 'createdAt']
}

{
    // SELECT * structure
    const starQuery = database.createQuery('SELECT * FROM tasks');
    const starResults = await starQuery.execute();

    for (const row of starResults) {
        // Results nested under collection name
        const task = row.tasks! as JSONObject;  // Access via collection name
        console.log(task.title, task.completed);
    }
}

{
    // SELECT properties structure
    const propsQuery = database.createQuery(`
        SELECT title, completed
        FROM tasks
    `);
    const propsResults = await propsQuery.execute();

    for (const row of propsResults) {
        // Properties at top level
        console.log(row.title, row.completed);
    }
}

{
    // Accessing result values
    const query = database.createQuery('SELECT title, completed, priority FROM tasks');
    const results = await query.execute<Task>();

    for (const row of results) {
        const title = row.title;
        const completed = row.completed;
        const priority = row.priority;
        console.log(`${title}: ${completed ? 'Done' : 'Pending'} (Priority: ${priority})`);
    }
}

{
    // Using aliases
    interface AliasTask {
        taskName: string;
        isDone: boolean;
        created: string;
    };

    const aliasQuery = database.createQuery(`
        SELECT title     AS taskName,
               completed AS isDone,
               createdAt AS created
        FROM tasks
    `);

    const results = await aliasQuery.execute<AliasTask>();

    for (const row of results) {
        console.log(`${row.taskName} - Done: ${row.isDone}`);
    }
}

{
    // Accessing nested properties
    interface NestedTask {
        title: string;
        name: string;
        email: string;
        tags: string[];
    };

    const nestedQuery = database.createQuery(`
        SELECT title,
               assignee.name,
               assignee.email,
               metadata.tags
        FROM tasks
    `);

    const results = await nestedQuery.execute<NestedTask>();

    for (const row of results) {
        console.log(`Task: ${row.title}`);
        console.log(`Assigned to: ${row.name} (${row.email})`);
        console.log(`Tags: ${row.tags.join(', ')}`);
    }
}

{
    // Collect all results as array
    const query = database.createQuery('SELECT * FROM tasks');
    const allResults = await query.execute();

    // Now you have an array of all results
    console.log(`Total tasks: ${allResults.length}`);

    // Can use array methods
    const completedTasks = allResults.filter(row => {
        const task = row.tasks! as JSONObject;
        return task.completed;
    });
    console.log(`Completed: ${completedTasks.length}`);
}

{
    // Process with callback for memory efficiency
    const query = database.createQuery('SELECT * FROM tasks');

    const completed = [];
    await query.execute(row => {
        const task = row.tasks! as JSONObject;
        if (task.completed) {
            completed.push(task);
        }
        // Row is processed and can be garbage collected
    });

    console.log(`Found ${completed.length} completed tasks`);
}

{
    // Count results efficiently
    const query = database.createQuery('SELECT COUNT(*) AS count FROM tasks WHERE completed = false');
    const results = await query.execute();

    const count = results[0].count as number;
    console.log(`Incomplete tasks: ${count}`);
}

{
    // Aggregate functions
    interface TaskStats {
        total: number;
        totalHours: number;
        avgPriority: number;
        earliest: string;
        latest: string;
    }

    const aggQuery = database.createQuery(`
        SELECT COUNT(*)            AS total,
               SUM(estimatedHours) AS totalHours,
               AVG(priority)       AS avgPriority,
               MIN(createdAt)      AS earliest,
               MAX(createdAt)      AS latest
        FROM tasks
    `);

    const results = await aggQuery.execute<TaskStats>();
    const stats = results[0];

    console.log(`Total: ${stats.total}`);
    console.log(`Total Hours: ${stats.totalHours}`);
    console.log(`Avg Priority: ${stats.avgPriority}`);
}

{
    // GROUP BY results
    interface GroupedResult {
        status: string;
        count: number;
        avgPriority: number;
    };

    const groupQuery = database.createQuery(`
        SELECT status,
               COUNT(*) AS count,
        AVG(priority) AS avgPriority
        FROM tasks
        GROUP BY status
    `);

    const results = await groupQuery.execute<GroupedResult>();

    for (const row of results) {
        console.log(`${row.status}: ${row.count} tasks (Avg Priority: ${row.avgPriority})`);
    }
}

{
    // JOIN results
    interface JoinResult {
        title: string;
        status: string;
        username: string;
        email: string;
    };

    const joinQuery = database.createQuery(`
        SELECT tasks.title,
               tasks.status,
               users.username,
               users.email
        FROM tasks
                 LEFT OUTER JOIN users ON tasks.assignedTo = users._id
    `);

    const results = await joinQuery.execute<JoinResult>();

    for (const row of results) {
        console.log(`Task: ${row.title}`);
        if (row.username) {
            console.log(`Assigned to: ${row.username} (${row.email})`);
        } else {
            console.log('Unassigned');
        }
    }
}

{
    // Handling NULL and MISSING
    const query = database.createQuery(`
        SELECT title,
               assignedTo,
               dueDate,
               IFNULL(assignedTo, 'unassigned')  AS assigned,
               IFMISSING(dueDate, 'no due date') AS due
        FROM tasks
    `);

    const results = await query.execute();

    for (const row of results) {
        // NULL values appear as null
        if (row.assignedTo === null) {
            console.log('Task not assigned');
        }

        // MISSING values don't exist in the object
        if (!('dueDate' in row)) {
            console.log('No due date set');
        }
    }
}

{
    // Convert results to JSON
    const query = database.createQuery('SELECT * FROM tasks LIMIT 10');
    const results = await query.execute();

    // Convert to JSON string
    const jsonString = JSON.stringify(results, null, 2);
    console.log(jsonString);

    // Or save to file/localStorage
    localStorage.setItem('taskResults', jsonString);
}

{
    // Type-safe query results with TypeScript
    interface TaskResult {
        title: string;
        completed: boolean;
        priority: number;
        createdAt: string;
    }

    const query = database.createQuery(`
        SELECT title, completed, priority, createdAt
        FROM tasks
        WHERE completed = false
    `);

    const results = await query.execute<TaskResult>();

    // TypeScript knows the result type
    for (const row of results) {
        const title: string = row.title;  // Type-safe access
        const priority: number = row.priority;
    }
}

{
    // Specify result type on execute
    interface TaskSummary {
        taskName: string;
        isDone: boolean;
    }

    const query = database.createQuery(`
        SELECT title     AS taskName,
               completed AS isDone
        FROM tasks
    `);

    const results = await query.execute<TaskSummary>();

    // Results are typed as TaskSummary[]
    results.forEach(task => {
        console.log(`${task.taskName}: ${task.isDone ? 'Done' : 'Pending'}`);
    });
}

{
    // Process results as stream without storing all
    const query = database.createQuery('SELECT * FROM tasks');

    let processedCount = 0;
    await query.execute(row => {
        // Process each row immediately
        processRow(row.tasks);
        processedCount++;

        // Row is not stored, can be garbage collected
    });

    console.log(`Streamed ${processedCount} results`);
}

{
    // Filter results in callback
    const query = database.createQuery('SELECT * FROM tasks');

    const urgentTasks = [];
    await query.execute(row => {
        const task = row.tasks as JSONObject;

        // Only keep urgent tasks
        if (task.priority === 'high' && !task.completed) {
            urgentTasks.push(task);
        }
    });

    console.log(`Found ${urgentTasks.length} urgent tasks`);
}

{
    // Transform results during iteration
    const query = database.createQuery(
        'SELECT * FROM tasks'
    );

    const taskSummaries = [];
    await query.execute(row => {
        const task = row.tasks as JSONObject;

        // Transform to summary format
        taskSummaries.push({
            id: task._id,
            title: task.title,
            status: task.completed ? 'Done' : 'Pending',
            daysOld: calculateDaysOld(task.createdAt as string)
        });
    });
}

{
    // Async callback for processing
    const query = database.createQuery(
        'SELECT tasks.* FROM tasks'
    );

    let asyncTasks: Promise<void>[] = [];
    await query.execute((row) => {
        asyncTasks.push(saveToCache(row));
        asyncTasks.push(updateUI(row));
    });

    await Promise.all(asyncTasks);
    console.log('All results processed asynchronously');
}

{
    // Error handling for queries
    try {
        const query = database.createQuery(
            'SELECT * FROM tasks WHERE priority > $minPriority'
        );
        query.parameters = { minPriority: 5 };
        const results = await query.execute();

        console.log(`Found ${results.length} high priority tasks`);
    } catch (error) {
        if (error instanceof N1QLParseError) {
            console.error('Invalid query syntax:', error.message);
        } else if (error instanceof InterruptedQueryError) {
            console.error('Query was interrupted');
        } else {
            console.error('Query failed:', error);
        }
    }
}

{
    // Check if query completed
    const query = database.createQuery(
        'SELECT * FROM tasks'
    );

    let count = 0;
    const completed = await query.execute(row => {
        count++;
        // Process row
    });

    if (completed) {
        console.log(`Query completed successfully, processed ${count} rows`);
    } else {
        console.log('Query was interrupted');
    }
}

{
    // Interrupt a running query
    const query = database.createQuery(
        'SELECT * FROM tasks'
    );

    // Start query execution
    const executePromise = query.execute(row => {
        // Long-running processing
        processRow(row);
    });

    // Interrupt after timeout
    setTimeout(() => {
        query.interrupt();
        console.log('Query interrupted');
    }, 5000);

    try {
        await executePromise;
    } catch (error) {
        if (error instanceof InterruptedQueryError) {
            console.log('Query was interrupted as expected');
        }
    }
}

// Working with blobs in results
// This is not supported yet.
/*
const query = database.createQuery(`
    SELECT title, attachment
    FROM documents
    WHERE attachment IS NOT NULL
`);

const results = await query.execute();

for (const row of results) {
    if (row.attachment) {
        // Get blob data
        const blob = row.attachment;
        const url = blob.getURL();  // Get URL for display
        const data = await blob.getArrayBuffer();  // Get binary data

        console.log(`Document: ${row.title}`);
        console.log(`Attachment size: ${blob.length} bytes`);
    }
}
*/

{
    // Type-safe query with TypeScript
    interface TaskResult {
        title: string;
        completed: boolean;
        priority: number;
    }

    // Create parameterized query
    let query = database.createQuery(`
        SELECT *
        FROM tasks
        WHERE completed = $completed
          AND priority >= $minPriority
        ORDER BY createdAt DESC
    `);

    // Set parameters using the parameters property
    query.parameters = {
        completed: false,
        minPriority: 3
    };

    // Execute with parameters
    const results = await query.execute();
    console.log(`Found ${results.length} high priority incomplete tasks`);

    const taskResults = await query.execute<TaskResult>();

    // TypeScript provides full type checking
    taskResults.forEach((task: TaskResult) => {
        console.log(`${task.title} - Priority: ${task.priority}`);
    });
}

function processRow(task: JSONValue) {
    // Process task
}

function calculateDaysOld(date: string): number {
    const created = new Date(date);
    const now = new Date();
    return Math.floor((now.getTime() - created.getTime()) / (1000 * 60 * 60 * 24));
}

async function saveToCache(task: JSONValue) {
    // Save to cache
}

async function updateUI(task: JSONValue) {
    // Update UI
}

{
    // Working with blobs
    // Create the blob from a File object
    const fileInput = document.getElementById('avatarFile') as HTMLInputElement;
    if (!fileInput?.files || fileInput.files.length === 0) {
        throw new Error('Please choose an image file first.');
    }
    const file = fileInput.files[0];
    const buffer = new Uint8Array(await file.arrayBuffer());
    const blob = new NewBlob(buffer, 'image/jpeg'); (1)

    // Add the blob to a document
    const user: CBLDictionary = {
        type: 'user',
        username: 'jane',
        email: 'jane@email.com',
        role: 'engineer',
        avatar: blob
    };

    // Create a document and save
    const users = database.getCollection('users');
    const doc = users.createDocument(DocID("profile1"), user);
    const saved = await users.save(doc);
}

{
    // Create blob from file input
    const fileInput = document.getElementById('avatarFile') as HTMLInputElement;
    if (!fileInput?.files || fileInput.files.length === 0) {
        throw new Error('Please choose an image file first.');
    }
    const file = fileInput.files[0];
    const buffer = new Uint8Array(await file.arrayBuffer());
    const blob = new NewBlob(buffer, 'image/jpeg');
}

{
    // Fetch remote binary data
    const response = await fetch('https://couchbase-example.com/images/avatar.jpg');
    if (!response.ok) {
        throw new Error(`Failed to fetch image: ${response.status}`);
    }

    // Convert the response into binary data
    const data = await response.arrayBuffer();

    // Create a blob from the downloaded data
    const buffer = new Uint8Array(await response.arrayBuffer());
    const blob = new NewBlob(buffer, 'image/jpeg');
}

{
    const users = database.getCollection('users');
    const doc = await users.getDocument(DocID("profile1"));
    if (doc) {
        // Note: Import as { Blob as CBLBlob } from â€˜@couchbase/lite-jsâ€™ to
        // avoid conflict with the standard Blob type.
        const blob = doc.avatar as CBLBlob;
        if (blob instanceof CBLBlob) {
            const contentType = blob.content_type ?? "None";
            const length = blob.length ?? 0;
            const digest = blob.digest;
            console.log(`Blob info:
                Content-Type: ${contentType}
                Length: ${length} bytes
                Digest: ${digest}`
            );
            const content = await blob.getContents();
            // Use content as needed
        }
    } else {
        console.log('User not found');
    }
}

{
    // Note: Import as { Blob as CBLBlob } from '@couchbase/lite-js'
    // to avoid conflict with the standard Blob type.
    interface UserSchema {
        type: 'user';
        username: string;
        email: string;
        role: string;
        avatar: CBLBlob | null;
    }

    const users = database.collections.users;
    const doc = await users.getDocument(DocID("profile1"));
    if (doc) {
        const blob = doc.avatar;
        if (blob) {
            const content = await blob.getContents();
            // Use content as needed
        }
    }
}
```

```javascript
const deleteResolver: PullConflictResolver = async (local, remote) => {
    return null;
};
```

When `null` is returned by the resolver, the conflict is resolved as a document deletion.

## [](#conflicts-when-saving)Conflicts when Saving

When updating a document, you need to consider the possibility of update conflicts. Update conflicts can occur when you try to update a document that’s been updated since you read it.

Example 3\. How Updating May Cause Conflicts

Here’s a typical sequence of events that would create an update conflict:

1. Your code reads the document’s current properties, and constructs a modified copy to save.
2. Another thread (perhaps the replicator) updates the document, creating a new revision with different properties.
3. Your code updates the document with its modified properties using the save operation.

### [](#automatic-conflict-resolution-2)Automatic Conflict Resolution

In Couchbase Lite, by default, the conflict is automatically resolved and only one document update is stored in the database. The Last-Write-Win (LWW) algorithm is used to pick the winning update. So in effect, the changes from step 2 would be overwritten and lost.

If the probability of update conflicts is high in your app and you wish to avoid the possibility of overwritten data, you can use a custom save handler with concurrency control.

### [](#save-with-conflict-handler)Save with Conflict Handler

Implement a conflict handler when saving documents to handle conflicts during save operations:

Example 4\. Save with Conflict Handler

```javascript
// Use my changes
await tasks.save(doc, (_mine, _theirs /* conflicting */) => {
    return 'replace';
});

// Discard my change
await tasks.save(doc, (_mine, _theirs /* conflicting */) => {
    return 'revert';
});

// Abort with an error
await tasks.save(doc, (_mine, _theirs /* conflicting */) => {
    return 'fail';
});
```

The conflict handler receives:

* `document` \- The document being saved
* `conflicting` \- The current document in the database (that conflicts)

The handler should return:

* The resolved document to save
* `null` to cancel the save operation

#### [](#custom-merge-on-save)Custom Merge on Save

Implement property-level merging when saving:

Example 5\. Custom merge on save

```javascript
// Use my changes
await tasks.save(doc, (mine, theirs /* conflicting */) => {
    // Delete always wins
    if (!theirs) return 'revert';

    // Custom merge
    mine.title = `${mine.title} and ${theirs.title}`;
    mine.completed = !!(mine.completed && theirs.completed);
    mine.priority = Math.min(mine.priority, theirs.priority);
    mine.createdAt = new Date().toISOString();
    return 'replace';
});
```

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)

.

### [](#-2)

Learn more . . .

* [Remote Sync Gateway](replication.md)
* [CORS Configuration](cors-configuration.md)
* [Databases](database.md)
* [Documents](document.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.