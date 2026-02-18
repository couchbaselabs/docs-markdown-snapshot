---
title: Live Queries
description: Couchbase Lite JavaScript -- Reactive Live Queries
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/query-live.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite-javascript/current/query-live.html)

# Live Queries

> Description — _Couchbase Lite JavaScript — Reactive Live Queries_  
> Related Content — [SQL++ for Mobile](query-n1ql-mobile.md) | [Query Resultsets](query-resultsets.md) | [Indexing](indexing.md)

## [](#overview)Overview

Live queries provide real-time updates when the results of a query change. This makes them perfect for building reactive user interfaces that automatically update when data changes.

When you create a live query, Couchbase Lite monitors the database and notifies you whenever documents that match the query are added, modified, or deleted.

## [](#creating-live-queries)Creating Live Queries

Create a live query by adding a change listener to your query:

Example 1\. Basic live query

```javascript
    interface TaskResult {
        title: string;
    }

    const query = database.createQuery(`
    SELECT title FROM tasks
    WHERE completed = false
    ORDER BY createdAt DESC
`);

    // Add change listener - receives array of results
    const token = query.addChangeListener<TaskResult>((results) => {
        console.log(`Query results updated: ${results.length} tasks`);

        // Update UI with new results
        results.forEach(row => {
            const task = row as TaskResult;
            console.log(`Task: ${task.title}`);
        });

        // Update your application UI
        updateTaskList(results);
    });

    // The listener is now active and will be called whenever results change
```

## [](#removing-listeners)Removing Listeners

Always remove listeners when they’re no longer needed:

Example 2\. Remove listener

```javascript
const query = database.createQuery('SELECT * FROM tasks WHERE completed = false');
const token = query.addChangeListener(_ => {
    console.log('Results updated');
});

// Later, remove the listener
token.remove();
console.log('Listener removed');
```

## [](#multiple-listeners)Multiple Listeners

You can add multiple listeners to the same query:

Example 3\. Multiple listeners

```javascript
const query = database.createQuery('SELECT * FROM tasks WHERE priority >= 3');

// Listener 1: Update UI
const uiToken = query.addChangeListener(results => {
    updateTaskList(results);
});

// Listener 2: Log changes
const logToken = query.addChangeListener(results => {
    console.log(`High priority tasks: ${results.length}`);
});

// Listener 3: Send analytics
const analyticsToken = query.addChangeListener(results => {
    trackMetric('high_priority_tasks', results.length);
});

// Each listener receives independent notifications
// Remove listeners individually when done
uiToken.remove();
logToken.remove();
analyticsToken.remove();
```

Each listener receives independent notifications.

## [](#typescript-live-queries)TypeScript Support

Type your live query results for type safety:

Example 4\. Typed live queries

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

    // Add typed listener
    const token = query.addChangeListener<TaskResult>((results) => {
        results.forEach(t => {
            const task = t as TaskResult;
            const title: string = task.title;  // Type-safe
            const priority: number = task.priority;

            console.log(`${title} - Priority: ${priority}`);
        });
    });
```

## [](#error-handling)Error Handling

Handle errors in live query listeners:

Example 5\. Error handling

```javascript
const query = database.createQuery('SELECT * FROM tasks');

query.addChangeListener(results => {
    try {
    // Process results
        updateUI(results);
    } catch (error) {
        console.error('Error updating UI:', error);
    // Handle error without crashing the listener
    }
});

// Wrap listener registration in try-catch for setup errors
try {
    query.addChangeListener(results => {
        processResults(results);
    });
} catch (error) {
    console.error('Failed to create live query listener:', error);
}
```

## [](#live-query-lifecycle)Live Query Lifecycle

Example 6\. Lifecycle stages

```javascript
class TaskManager {
    private query: Query | null = null;
    private database: Database | null = null;
    private listenerToken: ListenerToken | null = null;

    async start() {
        this.database = await Database.open({name: "mydb", version: 1, collections: { tasks: {} }});

        // Create query
        this.query = this.database.createQuery(`
        SELECT * FROM tasks
        WHERE assignedTo = $userId
        AND completed = false
    `);

        // Set parameters
        this.query.parameters = { userId: 'current-user' };

        // Start listening
        this.listenerToken = this.query.addChangeListener(results => {
            this.onResultsChanged(results);
        });

        console.log('Live query started');
    }

    onResultsChanged(results: QueryAliases[]) {
        console.log(`Tasks updated: ${results.length}`);
        this.updateUI(results);
    }

    updateParameters(userId: string) {
    // Changing parameters triggers listener with new results
        if (this.query) {
            this.query.parameters = { userId };
        }
    }

    stop() {
    // Clean up listener
        if (this.listenerToken) {
            this.listenerToken.remove();
            this.listenerToken = null;
            console.log('Live query stopped');
        }
    }

    private updateUI(_: QueryAliases[]) {
    // Update application UI
    }
}

// Usage
const manager = new TaskManager();
await manager.start();  // Start listening

// Later: change parameters (triggers update)
manager.updateParameters('different-user');

// Clean up when component unmounts
manager.stop();
```

## [](#limitations)Limitations

**Database Changes Only:**

* Live queries only respond to local database changes
* They don’t poll external data sources
* Replication changes trigger live query updates

**Query Constraints:**

* All SQL++ query limitations apply (see [query-n1ql-mobile.adoc#limitations](query-n1ql-mobile.md#limitations))
* Complex queries may have performance implications
* Index availability affects live query performance

**Browser Specific:**

* Live queries depend on browser staying active
* Background tabs may throttle updates
* Consider using Service Workers for background updates

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
* [Indexing](indexing.md)
* [Databases](database.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.