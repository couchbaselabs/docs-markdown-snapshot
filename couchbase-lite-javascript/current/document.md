---
title: Documents
description: Couchbase Lite concepts -- Data model -- Documents
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/document.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:couchbase-lite-javascript::document.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite-javascript/current/document.html)

# Documents

> Description — _Couchbase Lite concepts — Data model — Documents_  
> Related Content — [Databases](database.md) | [Blobs](blob.md) | [Indexing](indexing.md) |

## [](#overview)Overview

### [](#document-structure)Document Structure

In _Couchbase Lite_ the term 'document' refers to an entry in the database. You can compare it to a record, or a row in a table.

Each document has an ID or unique identifier. This ID is similar to a primary key in other databases.

You can specify the ID programmatically. If you omit it, it will be automatically generated as a UUID.

> [!NOTE]
> Couchbase documents are assigned to a [Collection](database.md#database-concepts). The ID of a document must be unique within the Collection it is written to. You cannot change it after you have written the document.

The document also has a value which contains the actual application data. This value is stored as a dictionary of key-value (k-v) pairs. The values can be made up of several different [Data Types](#data-types) such as numbers, strings, arrays, and nested objects.

### [](#data-encoding)Data Encoding

The document body is stored in an internal, efficient, binary form called [Fleece](https://github.com/couchbaselabs/fleece#readme). This internal form can be easily converted into a manageable native object format for manipulation in applications.

Fleece data is stored in the smallest format that will hold the value whilst maintaining the integrity of the value.

### [](#data-types)Data Types

Couchbase Lite JavaScript works with standard JavaScript data types:

* Boolean
* Number (integer and floating-point)
* String
* Date (stored as ISO-8601 strings)
* Object (dictionary/map)
* Array
* null

When using TypeScript, you can define interfaces for your document types to ensure type safety throughout your application.

In addition to these basic data types, Couchbase Lite provides:

CBLDictionary

represents a key-value pair collection

CBLDocument

represents a document with metadata

Blob

represents an arbitrary piece of binary data

### [](#json)JSON

Couchbase Lite JavaScript natively works with JSON data. Documents are JavaScript objects that can be easily serialized to and from JSON using standard `JSON.stringify()` and `JSON.parse()` methods.

## [](#constructing-a-document)Constructing a Document

An individual document often represents a single instance of an object in application code.

You can consider a document as the equivalent of a 'row' in a relational table, with each of the document's attributes being equivalent to a 'column'.

Documents can contain nested structures. This allows developers to express many-to-many relationships without requiring a reference or join table, and is naturally expressive of hierarchical data.

Most apps will work with one or more documents, persisting them to a local database and optionally syncing them, either centrally or to the cloud.

In this section we provide an example of how you might create a `hotel` document, which provides basic contact details and price data.

Data Model

```javascript
hotel: {
  type: string (value = `hotel`)
  name: string
  address: object {
    street: string
    city: string
    state: string
    country: string
    code: string
  }
  phones: array
  rate: number
}
```

### [](#ex-usage)Working with Collections

Couchbase documents are assigned to a [Collection](database.md#database-concepts). All the CRUD examples in this document operate on a `collection` object (here, from the Default Collection).

See [Databases](database.md) for information on opening databases and accessing collections.

### [](#create-and-save-document)Create and Save a Document in a Collection

All of these sections can be merged into a Create and Save a Document in a Collection section, with the following example:

```javascript
// 2. Get the collection
const coll = database.collection.hotels;

// 3. Create a typed hotel object
const hotel: Hotel = {
  type: "hotel",
  name: "The Grand Plaza",
  address: {
    street: "123 Main Street",
    city: "New York",
    state: "NY",
    country: "USA",
    code: "10001"
  },
  phones: ["+1-555-123-4567"],
  rate: 189.99
};

// 4. Create a document using the typed object
const doc = coll.createDocument(hotel);

// 5. Save the document
await coll.save(doc);
```

Learn more about [Using Dictionaries](#using-dictionaries) and [Using Arrays](#using-arrays).

> [!NOTE]
> Couchbase recommend using a `type` attribute to define each logical document type.

> [!NOTE]
> For information on closing databases, see [Close Database](database.md#close-database).

## [](#working-with-data)Working with Data

### [](#checking-a-documents-properties)Checking a Document's Properties

To check whether a given property exists in the document, use standard JavaScript property access or the `hasOwnProperty()` method.

```javascript
const coll = database.collection.hotels;

// Fetch a document
const doc = await coll.get("hotel_123");

// Access a known property
console.log("Name:", doc.name);

// Check if a property exists
if (doc.hasOwnProperty("rate")) {
  console.log("Rate:", doc.rate);
}
```

If you try to access a property which doesn't exist in the document, JavaScript will return `undefined`.

### [](#date-accessors)Date Handling

Dates in Couchbase Lite JavaScript are stored as ISO-8601 formatted strings. You can easily convert between JavaScript Date objects and these string representations.

> [!CAUTION]
> Date precision
> 
> JavaScript Date objects provide millisecond precision. If you require greater precision, consider storing timestamps as numbers representing microseconds or nanoseconds.

Example 1\. Date Handling

This example demonstrates storing and retrieving dates.

```javascript
const coll = database.collection("events");

const event = {
  type: "event",
  name: "Conference",
  createdAt: new Date().toISOString(), // store ISO date string
};

const doc = coll.createDocument(event);
await coll.save(doc);
```

### [](#using-dictionaries)Using Dictionaries

In JavaScript, dictionaries are represented as standard JavaScript objects. You can work with nested objects naturally.

Example 2\. Working with Objects

```javascript
interface TasksSchema {
    title: string;
    details: {
        location: string;
        duration: number;
        attendees: string[];
    };
    metadata: {
        createdBy: string;
        department: string;
        tags: string[];
    };
};

interface DBSchema {
    tasks: TasksSchema;
}

const config: DatabaseConfig<DBSchema> = {
    name: "mydb",
    version: 1,
    collections: {
        tasks: {}
    }
};

const database = await Database.open(config);
const tasks = database.collections.tasks;

// Create document with nested objects
const doc = tasks.createDocument(null, {
    title: "Project Meeting",
    details: {
        location: "Conference Room A",
        duration: 60,
        attendees: ["Alice", "Bob", "Charlie"]
    },
    metadata: {
        createdBy: "admin",
        department: "Engineering",
        tags: ["important", "recurring"]
    }
});

await tasks.save(doc);

// Access nested properties (note in TypeScript you should use a schema instead)
const meeting = await tasks.getDocument(meta(doc).id);
if (meeting) {
    console.log(`Location: ${meeting.details.location}`);
    console.log(`Duration: ${meeting.details.duration} minutes`);
    console.log(`Created by: ${meeting.metadata.createdBy}`);

    // Modify nested objects
    meeting.details.location = "Conference Room B";
    meeting.metadata.tags.push("urgent");
    await tasks.save(meeting);
}
```

### [](#using-arrays)Using Arrays

Arrays in Couchbase Lite JavaScript are standard JavaScript arrays.

Example 3\. Working with Arrays

```javascript
// Working with arrays

    interface ProjectsSchema {
        name: string;
        team: string[];
        milestones: string[];
        tags: string[];
    };

    interface DBSchema {
        projects: ProjectsSchema;
    }

    const config: DatabaseConfig<DBSchema> = {
        name: "mydb",
        version: 1,
        collections: {
            projects: {}
        }
    };

    const database = await Database.open(config);
    const projects = database.collections.projects;

    // Create document with arrays
    const project = projects.createDocument(null, {
        name: "Mobile App Development",
        team: ["Alice", "Bob", "Charlie"],
        milestones: [
            "Requirements gathering",
            "Design phase",
            "Development",
            "Testing",
            "Deployment"
        ],
        tags: ["mobile", "javascript", "react"]
    });

    await projects.save(project);

    // Access array elements
    const savedProject = await projects.getDocument(meta(project).id);
    if (savedProject) {
        console.log(`First team member: ${savedProject.team[0]}`);
        console.log(`Total milestones: ${savedProject.milestones.length}`);

        // Modify arrays
        savedProject.team.push("Diana");  // Add team member
        savedProject.milestones[2] = "Development (In Progress)";  // Update milestone
        savedProject.tags = savedProject.tags.filter((tag: string) => tag !== "mobile");  // Remove tag

        await projects.save(savedProject);
    }
```

### [](#using-blobs)Using Blobs

For more on working with blobs, see [Blobs](blob.md)

## [](#document-retrieval)Retrieving Documents

You can retrieve documents by their ID using the collection's `document()` method.

Example 4\. Retrieve a document

```javascript
const docId = DocID('task-001');
const doc = await tasks.getDocument(docId);
if (doc) {
    console.log('Task:', doc.title);
} else {
    console.log('Document not found');
}
```

## [](#document-update)Updating Documents

To update a document, retrieve it, modify its properties, and save it back to the collection.

Example 5\. Update a document

```javascript
const docId = DocID('task-001');
const docToUpdate = await tasks.getDocument(docId);
if (docToUpdate) {
    docToUpdate.completed = true;
    await tasks.save(docToUpdate);
    console.log('Document updated');
}
```

> [!NOTE]
> Any user change to the value of reserved keys (`_id`, `_rev` or `_deleted`) will be detected when a document is saved and will result in an error — see also [Document Constraints](#lbl-doc-constraints).

## [](#document-delete)Deleting Documents

You can delete a document using the collection's `deleteDocument()` method.

Example 6\. Delete a document

```javascript
const docId = DocID('task-001');
const deleteDoc = await tasks.getDocument(docId);
if (deleteDoc) {
    await tasks.delete(deleteDoc);
    console.log('Document deleted');
}
```

## [](#batch-operations)Batch operations

If you're making multiple changes to a database at once, it's faster to group them together. The following example persists multiple documents in a batch.

Example 7\. Batch operations

```javascript
const coll = database.collection.tasks;

async function bulkUpdate() {
  // Fetch two docs to update
  const taskA = await coll.get("taskA");
  const taskB = await coll.get("taskB");

  // Modify them locally
  taskA.status = "done";
  taskB.status = "in-progress";

  // Prepare doc to delete
  const obsolete = await coll.get("old_task");

  await coll.updateMultiple({
    bestEffort: true, // Perform updates even if one fails
    save: [taskA, taskB],    // Documents to save
    delete: [obsolete],       // Documents to delete

    onConflict: (conflict) => {
      // conflict.localDoc  - our version
      // conflict.remoteDoc - version from the database
      // conflict.documentID - id of the conflicting doc

      console.warn("Conflict detected for:",
        conflict.documentID);

      // Choose to keep the remote version (remote wins)
      return conflict.remoteDoc;

      // OR return conflict.localDoc for local-wins
      // OR return null to delete doc
    }
  });

  console.log("Bulk update complete.");
}
```

At the **local** level this operation is still transactional: no other `Database` instances, including ones managed by the replicator can make changes during the execution of the batch operation, and other instances will not see partial changes. But Couchbase Mobile is a distributed system, and due to the way replication works, there's no guarantee that Sync Gateway or other devices will receive your changes all at once.

## [](#document-change-events)Document change events

You can register for document changes. The following example registers for changes to a specific document and logs the changes when detected.

Example 8\. Document change events

```javascript
// Register for document change events
const tasks = database.getCollection("tasks");
const docId = DocID("task-001");

// Add document change listener
const token = tasks.addDocumentChangeListener(docId, (change) => {
    console.log(`Document ${change.id} changed`);
    console.log(`Revision: ${change.rev}`);
    console.log(`Sequence: ${change.sequence}`);

    if (change.deleted) {
        console.log('Document was deleted');
    } else {
        console.log('Document was updated');
    }
});

// Make changes to trigger the listener
const doc = await tasks.getDocument(docId);
if (doc) {
    doc.status = "completed";
    await tasks.save(doc);  // Listener will be called
}

// Remove listener when done
token.remove();
```

## [](#document-expiration)Document Expiration

Document expiration allows users to set the expiration date for a document. When the document expires, it is purged from the database. The purge is not replicated to Sync Gateway.

Example 9\. Set document expiration

This example sets the TTL for a document to 1 day from the current time.

```javascript
// Set document expiration
const tasks = database.getCollection("tasks");
const doc = await tasks.getDocument(DocID("task-001"));

if (doc) {
// Set expiration to 1 day from now (using milliseconds)
    const oneDayFromNow = 24 * 60 * 60 * 1000;  // 24 hours in milliseconds
    await tasks.setDocumentExpiration(doc, oneDayFromNow);

    console.log('Document will expire in 24 hours');

    // Or set expiration using Date object
    const expirationDate = new Date();
    expirationDate.setDate(expirationDate.getDate() + 1);  // 1 day from now
    await tasks.setDocumentExpiration(doc, expirationDate);

    // Get document expiration
    const expiration = await tasks.getDocumentExpiration(doc);
    if (expiration) {
        console.log(`Document expires on: ${expiration.toISOString()}`);
    }

    // Clear expiration
    await tasks.setDocumentExpiration(doc, undefined);
    console.log('Document expiration cleared');
}
```

You can also set expiration for a whole Collection.

## [](#lbl-doc-constraints)Document Constraints

Couchbase Lite APIs do not explicitly disallow the use of attributes with the underscore prefix at the top level of document. This is to facilitate the creation of documents for use either in _local only_ mode where documents are not synced, or when used exclusively in peer-to-peer sync.

> [!NOTE]
> "\_id", "\_rev" and "\_sequence" are reserved keywords and must not be used as top-level attributes — see [Example 10](#res-keys).

Users are cautioned that any attempt to sync such documents to Sync Gateway will result in an error. To be future proof, you are advised to avoid creating such documents. Use of these attributes for user-level data may result in undefined system behavior.

For more guidance — see: [Sync Gateway - data modeling guidelines](../../sync-gateway/current/data-modeling.md)

Example 10\. Reserved Keys List

* \_attachments
* \_deleted
* \_id
* \_removed
* \_rev
* \_sequence

## [](#lbl-json-data)Working with JSON Data

### [](#lbl-document)Documents as JSON

Since JavaScript natively works with JSON, converting documents is straightforward using standard `JSON.stringify()` and `JSON.parse()` methods.

Example 11\. Documents as JSON strings

```javascript
// Get a document from the collection
const users = database.getCollection("users");
const doc = await users.getDocument(DocID("user-123"));

if (doc) {
// Convert document to JSON string
    const jsonString = JSON.stringify(doc);
    console.log('Document as JSON:', jsonString);

    // Parse JSON string back to object
    const parsedDoc = JSON.parse(jsonString) as CBLDocument;
    console.log('Parsed document:', parsedDoc);

    // You can also stringify with formatting
    const prettyJson = JSON.stringify(doc, null, 2);
    console.log('Pretty JSON:\n', prettyJson);
}
```

### [](#lbl-result)Query Results as JSON

Query results can be easily converted to JSON for serialization or use in your application.

Example 12\. Using JSON Results

```javascript
// Execute a query
const query = database.createQuery(`
    SELECT users.* FROM users
    WHERE role = 'admin'
`);

const results = await query.execute();

// Convert results to JSON string
const jsonResults = JSON.stringify(results, null, 2);
console.log('Query results as JSON:', jsonResults);

// Parse JSON back to object
const parsedResults = JSON.parse(jsonResults) as JSONObject[];

// Save query results as documents in Couchbase Lite
const exports = database.getCollection("exports");

for (const row of parsedResults) {
    const userData = row.users;  // Extract user data

    // Create and save as new document
    const exportDoc = exports.createDocument(null, {
        type: 'user_export',
        exportedAt: new Date().toISOString(),
        userData: userData
    });

    await exports.save(exportDoc);
}

console.log('Query results saved as documents');
```

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)

.

### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](#)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.