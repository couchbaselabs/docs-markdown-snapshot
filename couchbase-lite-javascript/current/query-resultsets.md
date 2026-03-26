---
title: Query Resultsets
description: Couchbase Lite JavaScript -- Working with Query Results
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/query-resultsets.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:couchbase-lite-javascript::query-resultsets.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite-javascript/current/query-resultsets.html)

# Query Resultsets

> Description — _Couchbase Lite JavaScript — Working with Query Results_  
> Related Content — [SQL++ for Mobile](query-n1ql-mobile.md) | [Live Queries](query-live.md) | [Indexing](indexing.md)

## [](#overview)Overview

After executing a query, you work with the results through query resultsets. This page shows you how to iterate through results, access result values, and work with result data in different formats.

## [](#executing-queries)Executing Queries

Couchbase Lite JavaScript provides two ways to execute queries:

### [](#execute-with-array)Execute and Return Array

The `execute()` method without arguments returns an array of all results:

Example 1\. Execute and return array

```javascript
const query = database.createQuery('SELECT tasks.* FROM tasks WHERE completed = false');
const results = await query.execute<Task>();

console.log(`Found ${results.length} incomplete tasks`);

for (const row of results) {
    console.log(`Task: ${row.title}`);
}
```

### [](#execute-with-callback)Execute with Callback

The `execute(callback)` method calls your callback function for each result row, which is more memory-efficient for large result sets:

Example 2\. Execute with callback

```javascript
const query = database.createQuery('SELECT tasks.* FROM tasks WHERE completed = false');

let count = 0;
await query.execute<Task>(row => {
    console.log(`Task ${++count}: ${row.title}`);
    // Process each row without storing all in memory
});

console.log(`Processed ${count} tasks total`);
```

> [!TIP]
> Use the callback pattern when processing large result sets to avoid loading all results into memory at once.

## [](#result-structure)Result Structure

Each result row is a JavaScript object. The structure depends on your SELECT clause.

### [](#column-names)Getting Column Names

Use the `columnNames` property to get the names of result columns:

Example 3\. Access column names

```javascript
const query = database.createQuery(`
    SELECT title, completed, createdAt
    FROM tasks
`);

const columnNames = query.columnNames;
console.log('Columns:', columnNames);  // ['title', 'completed', 'createdAt']
```

### [](#select-all-results)SELECT \* Results

When you use `SELECT *`, results are nested under the collection name:

Example 4\. SELECT \* structure

```javascript
const starQuery = database.createQuery('SELECT * FROM tasks');
const starResults = await starQuery.execute();

for (const row of starResults) {
    // Results nested under collection name
    const task = row.tasks! as JSONObject;  // Access via collection name
    console.log(task.title, task.completed);
}
```

### [](#select-properties-results)SELECT Properties Results

When you select specific properties, they appear as top-level properties in the result:

Example 5\. SELECT properties structure

```javascript
const propsQuery = database.createQuery(`
    SELECT title, completed
    FROM tasks
`);
const propsResults = await propsQuery.execute();

for (const row of propsResults) {
    // Properties at top level
    console.log(row.title, row.completed);
}
```

## [](#accessing-values)Accessing Result Values

Result values are accessed as regular JavaScript object properties:

Example 6\. Accessing values

```javascript
const query = database.createQuery('SELECT title, completed, priority FROM tasks');
const results = await query.execute<Task>();

for (const row of results) {
    const title = row.title;
    const completed = row.completed;
    const priority = row.priority;
    console.log(`${title}: ${completed ? 'Done' : 'Pending'} (Priority: ${priority})`);
}
```

## [](#result-aliases)Using Result Aliases

Use the `AS` keyword to create aliases for result columns:

Example 7\. Result aliases

```javascript
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
```

## [](#nested-properties)Accessing Nested Properties

When querying nested objects, the result structure reflects the query:

Example 8\. Nested properties

```javascript
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
```

## [](#collecting-results)Collecting Results

The `execute()` method without arguments returns all results as an array:

Example 9\. Collect all results

```javascript
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
```

For memory efficiency with large result sets, use the callback pattern instead:

Example 10\. Process results with callback

```javascript
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
```

## [](#counting-results)Counting Results

To count results without collecting them all:

Example 11\. Count results

```javascript
const query = database.createQuery('SELECT COUNT(*) AS count FROM tasks WHERE completed = false');
const results = await query.execute();

const count = results[0].count as number;
console.log(`Incomplete tasks: ${count}`);
```

## [](#aggregate-results)Working with Aggregate Results

When using aggregate functions, results contain the aggregated values:

Example 12\. Aggregate results

```javascript
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
```

## [](#group-by-results)GROUP BY Results

GROUP BY queries return one result per group:

Example 13\. GROUP BY results

```javascript
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
```

## [](#join-results)JOIN Results

JOIN queries combine data from multiple collections:

Example 14\. JOIN results

```javascript
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
```

## [](#null-missing-values)Handling NULL and MISSING Values

SQL++ distinguishes between NULL and MISSING values:

* **NULL** \- Explicitly set to null
* **MISSING** \- Property doesn't exist

Example 15\. NULL and MISSING handling

```javascript
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
```

## [](#json-results)Converting Results to JSON

You can convert result objects to JSON strings:

Example 16\. JSON conversion

```javascript
const query = database.createQuery('SELECT * FROM tasks LIMIT 10');
const results = await query.execute();

// Convert to JSON string
const jsonString = JSON.stringify(results, null, 2);
console.log(jsonString);

// Or save to file/localStorage
localStorage.setItem('taskResults', jsonString);
```

## [](#typescript-results)TypeScript Result Types

When using TypeScript, specify the result type using generics for type safety:

Example 17\. Typed results

```typescript
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
```

The Query class is generic: `Query<Schema>` where Schema is inherited from its Database. You can also specify the result type when calling `execute<T>()`:

Example 18\. Specify result type

```typescript
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
```

> [!NOTE]
> TypeScript result types are not runtime-checked. It's your responsibility to ensure the type matches the actual query results.

## [](#processing-patterns)Result Processing Patterns

### [](#streaming-processing)Streaming Processing

Process results as they arrive without storing them all in memory:

Example 19\. Streaming pattern

```javascript
const query = database.createQuery('SELECT * FROM tasks');

let processedCount = 0;
await query.execute(row => {
    // Process each row immediately
    processRow(row.tasks);
    processedCount++;

    // Row is not stored, can be garbage collected
});

console.log(`Streamed ${processedCount} results`);
```

### [](#filtering-results)Filtering Results

Filter results in your callback:

Example 20\. Filtering pattern

```javascript
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
```

### [](#transforming-results)Transforming Results

Transform result data during iteration:

Example 21\. Transformation pattern

```javascript
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
```

## [](#async-processing)Asynchronous Processing

The `execute()` method itself is asynchronous. If you use the callback pattern, your callback can also be asynchronous:

Example 22\. Async callback processing

```javascript
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
```

> [!NOTE]
> With async callbacks, the `execute()` method waits for each callback to complete before processing the next result.

## [](#error-handling)Error Handling

Handle errors during query execution:

Example 23\. Error handling

```javascript
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
```

## [](#performance-tips)Performance Tips

**Process Results Efficiently:**

* Use the callback pattern to process results one at a time
* Avoid collecting all results if you only need to process them
* Use `LIMIT` to restrict result count when appropriate

**Memory Management:**

* Don't store large result sets in memory unnecessarily
* Process and release results as you go
* Consider pagination for large datasets

**Query Optimization:**

* Select only the properties you need
* Use indexes to speed up queries (see [Indexing](indexing.md))
* Check query explanations to verify index usage

## [](#result-iteration-control)Controlling Result Iteration

When using the callback pattern, `execute()` returns a boolean indicating whether the query completed:

* `true` \- Query completed normally
* `false` \- Query was interrupted (see [Interrupting Queries](#interrupting-queries))

Example 24\. Check if query completed

```javascript
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
```

### [](#interrupting-queries)Interrupting Queries

You can stop a running query using the `interrupt()` method:

Example 25\. Interrupt a query

```javascript
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
```

When interrupted, `execute()` throws an `InterruptedQueryError`.

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)

.

### [](#-2)

Learn more . . .

* [SQL++ for Mobile](query-n1ql-mobile.md)
* [Live Queries](query-live.md)
* [Indexing](indexing.md)
* [Databases](database.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.