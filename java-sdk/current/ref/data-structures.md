---
title: Data Structures Reference
description: You can use complex data structures such as dictionaries and lists
  in Couchbase.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.11/modules/ref/pages/data-structures.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/java-sdk/current/ref/data-structures.html)

# Data Structures Reference

> You can use complex data structures such as dictionaries and lists in Couchbase. 

Data structures in Couchbase are similar in concept to data structures in the Java Collections Framework:

See our [Data Model pages](../concept-docs/data-model.md).

Here is a list of common operations:

__Table 1\. Data Structure Operations__
|                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mapAdd                                | Add a key to the map. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\]                                                                                                                                                                                                                                                                                                                                                                                   |
| mapRemove                             | Remove a key from a map. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\]                                                                                                                                                                                                                                                                                                                                                                                |
| mapGet                                | Get an item from a map. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\] If the key is not found, a PathNotFoundException is raised.                                                                                                                                                                                                                                                                                                                     |
| listAppend                            | Add an item to the _end_ of a list. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\]                                                                                                                                                                                                                                                                                                                                                                     |
| listPrepend                           | Add an item to the _beginning_ of a list. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\]                                                                                                                                                                                                                                                                                                                                                               |
| listRemove                            | Remove a value from a list. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\]                                                                                                                                                                                                                                                                                                                                                                             |
| listSet                               | Set an element at a specific index in the list. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\]                                                                                                                                                                                                                                                                                                                                                         |
| listGet                               | Get an item from a list by its index. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\] If the index is out of range, a PathNotFoundException will be thrown. Note that you can get the _last_ array element by specifying \-1 as the index.                                                                                                                                                                                                              |
| setAdd                                | Add an item to a set, if the item does not yet exist in the set. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\] Note that a _set_ is just a list. You can retrieve the entire set by simply using a full-document get operation: Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\] Currently, you can only store primitive values in sets, such as strings, ints, and booleans. |
| setContains                           | Check if a value exists in the set. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\]                                                                                                                                                                                                                                                                                                                                                                     |
| setRemove                             | Remove an item from a set, if it exists. An exception is not thrown if the item does not exist. You can determine if an item existed or not by the return value. If the item did not exist beforehand, null is returned. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\]                                                                                                                                                                                |
| queuePush                             | Add an item to the beginning of the queue. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\] Note that a queue is just a list. You can retrieve items from the middle of the queue by using listGet                                                                                                                                                                                                                                                       |
| queuePop                              | Remove an item from the end of the queue and return it. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\] If the queue is empty, then null is returned.                                                                                                                                                                                                                                                                                                   |
| mapSize, listSize, setSize, queueSize | These methods get the length of the data structure. For maps, this is the number of key-value pairs inside the map. For lists, queues, and sets, this is the number of elements in the structure. Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java\[\]                                                                                                                                                                                                       |

Note that there are only **two** basic types: map and list. Types such as _queue_ and _set_ are merely derivatives of _list_.

## [](#data-structures-and-key-value-apis)Data Structures and Key-Value APIs

Data structures can be accessed using key-value APIs as well. In fact, the data structure API is actually a client-side wrapper _around_ the key-value and sub-document API. Most of the data structure APIs wrap the sub-document API directly.

> [!NOTE]
> Because the data structure API is just a wrapper around the various key-value APIs, you are free to switch between them in your code.

## [](#jcf)Collections Framework Integration

In addition to the `Bucket` level methods for working with data structures, the Java SDK provides implementations of the `Map`, `List`, `Set`, and `Queue` interfaces from the Java Collections Framework. Instead of maintaining in-memory storage, these implementations are backed by JSON documents stored in Couchbase Server. The implementations are thread-safe and suitable for concurrent use. The `Map`, `List`, and `Queue` implementations may contain values of the following types:

* String
* Integer
* Long
* Double
* Boolean
* BigInteger
* BigDecimal
* JsonObject
* JsonArray

The `Set` implementation may contain values of all of the above types except `JsonObject` and `JsonArray`.

## [](#couchbasemap)CouchbaseMap

The CouchbaseMap<V> class implements Map<String, V>. It allows null values, but does not allow null keys.

Example usage:

```java
Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java[]
```

## [](#couchbasearraylist)CouchbaseArrayList

The CouchbaseArrayList<V> class implements List<V>. It allows null values.

Example usage:

```java
Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java[]
```

## [](#couchbasearrayset)CouchbaseArraySet

The CouchbaseArraySet<V> class implements Set<V>. It allows null values.

Example usage:

```java
Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java[]
```

## [](#couchbasequeue)CouchbaseQueue

The CouchbaseQueue<V> class implements Queue<V>. It does not allow null values.

Example usage:

```java
Unresolved include directive in modules/ref/pages/data-structures.adoc - include::example$DataStructuresExample.java[]
```