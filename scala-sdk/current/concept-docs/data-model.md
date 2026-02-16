[View original HTML](/scala-sdk/current/concept-docs/data-model.html)

> Couchbase’s use of JSON as a storage format allows powerful search and query over documents. Several data structures are supported by the SDK, including map, list, queue, and set. 

The power to search, query, and easily work with data in Couchbase, comes from the choice of JSON as a storage format. Non-JSON storage is supported — see the [Binary Storage Documentation](nonjson.md) — including UTF-8 strings, raw sequences of bytes, and language specific serializations, however, only JSON is supported by [Query](n1ql-query.md). In Couchbase, JSON’s key-value structure allows the storage of collection data structures such as lists, maps, sets and queues — _see [below](#data-structures)_. JSON’s tree-like structure allows operations against [specific paths in the Document](subdocument-operations.md), and efficient support for these data structures.

## [](#data-structures)Data Structures

Data structures in Couchbase are similar in concept to data structures in C# (.NET):

* **Map** is like .NET `Dictionary<TKey, TValue>`, and is a key-value structure, where a value is accessed by using a key string.
* **List** is like a .NET `List<TValue>` and is a sequential data structure. Values can be placed in the beginning or end of a list, and can be accessed using numeric indexes.
* **Queue** is like a `IQueue` implementation which offers First In First Out (FIFO) semantics, allowing it to be used as a lightweight job queue.
* **Set** is a wrapper over a `List<TValue>` which provides the ability to handle unique values.

These data structures are stored as JSON documents in Couchbase, and can therefore be accessed both using the Query Service and normal key-value operations. Data structures can also be manipulated using the traditional sub-document and full-document KV APIs.

Using the data structures API may help your application in two ways:

* **Simplicity**: Data structures provide high level operations by which you can deal with documents as if they were container data structures. Adding an item to a dictionary is expressed as `MapAdd`, rather than retrieving the entire document, modifying it locally, and then saving it back to the server.
* **Efficiency**: Data structure operations don’t transfer the entire document across the network. Only the relevant data is exchanged between client and server, allowing for less network overhead and shorter latency.

|  | Besides the IBucket level data structure methods, there is a new namespace called Couchbase.Collections which contains implementations of some of the core interfaces in System.Collection.Generics such as ISet<TValue>, IList<TValue>, IDictionary<Tkey, TValue> and a CouchbaseQueue class. See section [The Couchbase.Collections Namespace](#couchbase-collections) below for more details. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#data-and-good-schema-design)Data and Good Schema Design

Most operations are performed at the _collection_ or _scope_ level (although legacy bucket-level ops are often available), and keeping documents in the same collection can make for speedier indexing and queries — whether SQL++ or Search.

The Server enforces no schema, enabing evolutionary changes to your data model that reflect changes in the real world. The schema-on-read approach allows the client software that you write with the SDK to work with changes to an implicit schema, and allows heterogeneous data.

### [](#objects-relations-tables)Objects, Relations, Tables

In the Relational Database (RDBMS) world, a translaton layer is often used between the objects of your data model in your application, and the tables that you store the data in. JSON storage allows you to store complex types, like nested records and arrays, without decomposing them to a second table (known in the SQL world as [database normalization](https://en.wikipedia.org/wiki/Database%5Fnormalization)).

When the relational model was proposed, more than 50 years ago, limitations in available computer resources meant that removing data duplication in one-to-many and many-to-many relationships this way made a great deal of sense. There is still a case to be made for it for reducing inconsistencies — the difference with a document database is that you get to choose when to do this.

### [](#collections-and-scopes)Collections and Scopes

Couchbase’s atomic units of data are documents, stored as key-value pairs. The value can be anything, but storing in JSON format enables indexing, searching, and many useful ways of working with the data from the SDK.

Collections are arbitary groupings of the data documents. Ones that suit your object model. For example, one collection of students enrolled at the college and one collection of courses available for them to take. Notionally you may view them as equivalent to an RDBMS table — but it’s up to you.

Within a bucket, you can organize your collections into scopes — some methods are available at the bucket level, but Search and Query Services favour Scope-level indexing and querying for greater efficiency.