---
title: SQL++ Queries
description: Couchbase Lite JavaScript -- SQL++ Query API
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/query-n1ql-mobile.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:couchbase-lite-javascript::query-n1ql-mobile.adoc[]
---

[View original HTML](/couchbase-lite-javascript/current/query-n1ql-mobile.html)

# SQL++ Queries

> Description — _Couchbase Lite JavaScript — SQL++ Query API_  
> Related Content — [Query Resultsets](query-resultsets.md) | [Live Queries](query-live.md) | [Indexing](indexing.md)

## [](#overview)Overview

Couchbase Lite JavaScript supports SQL++ (also known as N1QL), a powerful query language based on SQL, but designed for JSON documents.

SQL++ for Mobile brings SQL-like querying capabilities to the browser, allowing you to query documents stored locally in IndexedDB with the same familiar syntax used in Couchbase Server.

> [!NOTE]
> N1QL is Couchbase’s implementation of the developing SQL standard. As such, the terms N1QL and SQL are used interchangeably in Couchbase documentation unless explicitly stated otherwise.

## [](#query-format)Query Format

Queries in Couchbase Lite JavaScript are created using SQL++ query strings:

Example 1\. Basic query example

```javascript
const query = database.createQuery('SELECT * FROM tasks');
const results = await query.execute();
```

## [](#creating-queries)Creating Queries

You create queries using the database’s `createQuery()` method, which takes a SQL++ query string:

Example 2\. Create and execute query

```javascript
const query = database.createQuery(`
    SELECT tasks.*
    FROM tasks
    WHERE completed = false
    ORDER BY createdAt DESC
`);
```

## [](#query-parameters)Query Parameters

Use parameterized queries to make them reusable with different values. Parameters are prefixed with `$` in the query string:

Example 3\. Parameterized query

```javascript
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
```

## [](#select-statement)SELECT Statement

The SELECT statement is used to query documents. It supports various clauses for filtering, sorting, grouping, and limiting results.

### [](#basic-select)Basic SELECT

Example 4\. Select all documents

```javascript
const allQuery = database.createQuery('SELECT * FROM tasks');
const allResults = await allQuery.execute();
```

### [](#select-properties)Select Specific Properties

Example 5\. Select specific properties

```javascript
const propsQuery = database.createQuery(`
    SELECT title, completed, createdAt
    FROM tasks
`);
const propResults = await propsQuery.execute();
```

## [](#where-clause)WHERE Clause

The WHERE clause filters documents based on conditions:

Example 6\. WHERE clause examples

```javascript
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
```

### [](#comparison-operators)Comparison Operators

SQL++ supports standard comparison operators:

* `=` \- Equal to
* `!=` or `<>` \- Not equal to
* `<` \- Less than
* `⇐` \- Less than or equal to
* `>` \- Greater than
* `>=` \- Greater than or equal to
* `BETWEEN` \- Between two values
* `IN` \- Value in a list
* `LIKE` \- Pattern matching
* `IS NULL` \- Check for null values
* `IS NOT NULL` \- Check for non-null values

### [](#logical-operators)Logical Operators

Combine conditions with logical operators:

* `AND` \- Both conditions must be true
* `OR` \- Either condition must be true
* `NOT` \- Negates a condition

Example 7\. Logical operators

```javascript
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
```

### [](#pattern-matching)Pattern Matching with LIKE

Use `LIKE` for string pattern matching with wildcards:

* `%` \- Matches any sequence of characters
* `_` \- Matches any single character

Example 8\. Pattern matching

```javascript
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
```

### [](#regex-matching)Regular Expression Matching

Use regex functions for more complex pattern matching:

Example 9\. Regex matching

```javascript
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
```

## [](#order-by)ORDER BY Clause

Sort query results using the ORDER BY clause:

Example 10\. Sorting results

```javascript
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
```

## [](#limit-offset)LIMIT and OFFSET

Control the number of results returned:

Example 11\. Limiting results

```javascript
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
```

## [](#joins)JOIN Operations

SQL++ supports joining documents from multiple collections:

Example 12\. JOIN example

```javascript
const joinQuery = database.createQuery(`
    SELECT tasks.title, users.username
    FROM tasks
             LEFT OUTER JOIN users ON tasks.assignedTo = users._id
    WHERE tasks.completed = false
`);

const joinResults = await joinQuery.execute();
```

> [!NOTE]
> Only LEFT OUTER JOIN is supported in CBL-JS. RIGHT OUTER JOIN is not available.

## [](#grouping)GROUP BY and Aggregation

Group results and use aggregate functions:

Example 13\. Grouping and aggregation

```javascript
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
```

### [](#aggregate-functions)Aggregate Functions

Available aggregate functions:

* `COUNT()` \- Count of values
* `SUM()` \- Sum of numeric values
* `AVG()` \- Average of numeric values
* `MIN()` \- Minimum value
* `MAX()` \- Maximum value
* `ARRAY_AGG()` \- Collects values into an array

## [](#array-functions)Array Functions

SQL++ provides functions for working with arrays:

Example 14\. Array functions

```javascript
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
```

Available array functions:

* `ARRAY_LENGTH()` \- Length of array
* `ARRAY_CONTAINS()` \- Check if array contains value
* `ARRAY_COUNT()` \- Count non-null items
* `ARRAY_AVG()` \- Average of numeric array
* `ARRAY_MAX()` \- Maximum value in array
* `ARRAY_MIN()` \- Minimum value in array
* `ARRAY_SUM()` \- Sum of numeric array

## [](#string-functions)String Functions

Functions for string manipulation:

Example 15\. String functions

```javascript
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
```

Available string functions:

* `UPPER()` / `LOWER()` \- Convert case
* `LENGTH()` \- String length
* `CONTAINS()` \- Check if string contains substring
* `CONCAT()` \- Concatenate strings
* `TRIM()` / `LTRIM()` / `RTRIM()` \- Remove whitespace

## [](#date-functions)Date and Time Functions

Work with dates and timestamps:

Example 16\. Date functions

```javascript
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
```

Available date functions:

* `MILLIS_TO_STR()` \- Convert timestamp to ISO-8601 string
* `MILLIS_TO_UTC()` \- Convert timestamp to UTC string
* `STR_TO_MILLIS()` \- Parse ISO-8601 string to timestamp
* `STR_TO_UTC()` \- Normalize ISO-8601 string to UTC

## [](#math-functions)Mathematical Functions

Perform mathematical operations:

Example 17\. Math functions

```javascript
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
```

Available math functions:

* Trigonometric: `SIN()`, `COS()`, `TAN()`, `ASIN()`, `ACOS()`, `ATAN()`, `ATAN2()`
* Rounding: `ROUND()`, `CEIL()`, `FLOOR()`, `TRUNC()`
* Other: `ABS()`, `SQRT()`, `POWER()`, `EXP()`, `LN()`, `LOG()`
* Division: `DIV()` (float division), `IDIV()` (integer division)
* Constants: `E()`, `PI()`

## [](#type-functions)Type Checking and Conversion

Check and convert data types:

Example 18\. Type functions

```javascript
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
```

Type checking functions:

* `ISARRAY()`, `ISOBJECT()`, `ISSTRING()`, `ISNUMBER()`, `ISBOOLEAN()`
* `TYPE()` \- Returns type name as string

Type conversion functions:

* `TOARRAY()`, `TOOBJECT()`, `TOSTRING()`, `TONUMBER()`, `TOBOOLEAN()`

## [](#conditional-functions)Conditional Functions

Handle null and missing values:

Example 19\. Conditional functions

```javascript
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
```

Available conditional functions:

* `IFNULL()` \- Returns first non-null value
* `IFMISSING()` \- Returns first non-missing value
* `IFMISSINGORNULL()` \- Returns first value that is neither missing nor null
* `NULLIF()` \- Returns null if two values are equal
* `MISSINGIF()` \- Returns missing if two values are equal

## [](#case-expression)CASE Expression

Use CASE for conditional logic:

Example 20\. CASE expression

```javascript
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
```

## [](#metadata-access)Accessing Document Metadata

Access document metadata using the `META()` function:

Example 21\. Document metadata

```javascript
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
```

Available metadata properties:

* `META().id` \- Document ID
* `META().sequence` \- Sequence number

## [](#query-explanation)Query Explanations

Use the `explanation` property to understand how a query is executed:

Example 22\. Query explanation

```javascript
const explanation = query.explanation;
console.log('Query plan:', explanation);
```

The explanation shows:

* Whether indexes are being used
* The order of operations
* Which collections are being scanned
* Join strategies

This is helpful for optimizing query performance.

## [](#typescript-queries)TypeScript Support

When using TypeScript, you can type your query results:

Example 23\. Type-safe queries

```typescript
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
```

## [](#limitations)Couchbase Lite JavaScript Query Limitations

Couchbase Lite JavaScript supports most SQL++ features, but has some limitations compared to other Couchbase Lite platforms and Couchbase Server:

### [](#missing-features)Missing Features

The following features are not currently supported:

* **Advanced search indexes** \- Full-text search using `MATCH()` and vector search with indexes are not available (though `EUCLIDEAN_DISTANCE()` and `COSINE_DISTANCE()` functions work without indexes)
* **Operators** \- `COLLATE` (string collation is by UTF-16 code points), `EXISTS`
* **Set operations** \- `UNION`, `INTERSECT`, `EXCEPT`
* **JOIN operations** \- `RIGHT OUTER JOIN` (only `LEFT OUTER JOIN` is available), `NEST`/`UNNEST`
* **Format string arguments** \- For date functions like `MILLIS_TO_STR()`, `STR_TO_MILLIS()`
* **Multiple GROUP BY conditions** \- Only single GROUP BY expressions supported

### [](#boolean-logic)Boolean Logic Rules

Couchbase Lite JavaScript follows Couchbase Server’s boolean logic rules:

* `TRUE` is TRUE, `FALSE` is FALSE
* Numbers: 0 or 0.0 are FALSE
* Arrays and objects are FALSE
* Strings and Blobs are TRUE if cast as non-zero, FALSE if cast as 0 or 0.0
* `NULL` is FALSE
* `MISSING` is MISSING

### [](#comparison-differences)Comparison Operators

Couchbase Lite JavaScript correctly supports comparison operators (`=`, `<`, etc.) on array and object values, which differs from some other CBL platforms.

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)

.

### [](#-2)

Learn more . . .

* [Query Resultsets](query-resultsets.md)
* [Live Queries](query-live.md)
* [Indexing](indexing.md)
* [Databases](database.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.