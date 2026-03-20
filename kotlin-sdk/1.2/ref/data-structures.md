---
title: Data Structures Reference
description: You can use complex data structures such as dictionaries and lists
  in Couchbase.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/release/1.2/modules/ref/pages/data-structures.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:1.2@kotlin-sdk:ref:data-structures.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/1.2/ref/data-structures.html)

# Data Structures Reference

> You can use complex data structures such as dictionaries and lists in Couchbase. 

Data structures in Couchbase are similar in concept to data structures in the Java Collections Framework:

See our [Data Model pages](../concept-docs/data-model.md).

Here is a list of common operations:

__Table 1\. Data Structure Operations__
|                                       |                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mapAdd                                | Add a key to the map. map.put("some\_key", "value");                                                                                                                                                                                                                                                                            |
| mapRemove                             | Remove a key from a map. map.remove("some\_key");                                                                                                                                                                                                                                                                               |
| mapGet                                | Get an item from a map. map.get("some\_key"); //=> value If the key is not found, a PathNotFoundException is raised.                                                                                                                                                                                                            |
| listAppend                            | Add an item to the _end_ of a list. arrayList.add(1234);                                                                                                                                                                                                                                                                        |
| listPrepend                           | Add an item to the _beginning_ of a list. arrayList.add(0, "hello world");                                                                                                                                                                                                                                                      |
| listRemove                            | Remove a value from a list. arrayList.remove(1);                                                                                                                                                                                                                                                                                |
| listSet                               | Set an element at a specific index in the list. arrayList.set(0, "first value");                                                                                                                                                                                                                                                |
| listGet                               | Get an item from a list by its index. arrayList.get(0); If the index is out of range, a PathNotFoundException will be thrown. Note that you can get the _last_ array element by specifying \-1 as the index.                                                                                                                    |
| setAdd                                | Add an item to a set, if the item does not yet exist in the set. arraySet.add("some\_value"); Note that a _set_ is just a list. You can retrieve the entire set by simply using a full-document get operation: Set set = arraySet; Currently, you can only store primitive values in sets, such as strings, ints, and booleans. |
| setContains                           | Check if a value exists in the set. arraySet.contains("value");                                                                                                                                                                                                                                                                 |
| setRemove                             | Remove an item from a set, if it exists. An exception is not thrown if the item does not exist. You can determine if an item existed or not by the return value. If the item did not exist beforehand, null is returned. arraySet.remove("some\_value");                                                                        |
| queuePush                             | Add an item to the beginning of the queue. queue.add("job123"); Note that a queue is just a list. You can retrieve items from the middle of the queue by using listGet                                                                                                                                                          |
| queuePop                              | Remove an item from the end of the queue and return it. Object item = queue.poll(); //=> "job123" If the queue is empty, then null is returned.                                                                                                                                                                                 |
| mapSize, listSize, setSize, queueSize | These methods get the length of the data structure. For maps, this is the number of key-value pairs inside the map. For lists, queues, and sets, this is the number of elements in the structure. int len = arrayList.size(); //=> 42                                                                                           |

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
Map<String, String> favorites = new CouchbaseMap<String>("mapDocId", collection, String.class, MapOptions.mapOptions());
favorites.put("color", "Blue");
favorites.put("flavor", "Chocolate");

System.out.println(favorites); //=> {flavor=Chocolate, color=Blue}

// What does the JSON document look like?
System.out.println(collection.get("mapDocId").contentAsObject());
//=> {"flavor":"Chocolate","color":"Blue"}
```

## [](#couchbasearraylist)CouchbaseArrayList

The CouchbaseArrayList<V> class implements List<V>. It allows null values.

Example usage:

```java
List<String> names = new CouchbaseArrayList<String>("listDocId", collection, String.class, ArrayListOptions.arrayListOptions());
names.add("Alice");
names.add("Bob");
names.add("Alice");

System.out.println(names); //=> [Alice, Bob, Alice]

// What does the JSON document look like?
System.out.println(collection.get("listDocId").contentAsArray());
//=> ["Alice","Bob","Alice"]
```

## [](#couchbasearrayset)CouchbaseArraySet

The CouchbaseArraySet<V> class implements Set<V>. It allows null values.

Example usage:

```java
Set<String> uniqueNames = new CouchbaseArraySet<String>("setDocId", collection, String.class, ArraySetOptions.arraySetOptions());
uniqueNames.add("Alice");
uniqueNames.add("Bob");
uniqueNames.add("Alice");

System.out.println(uniqueNames); //=> [Alice, Bob]

// What does the JSON document look like?
System.out.println(collection.get("setDocId").contentAsArray());
//=> ["Alice","Bob"]
```

## [](#couchbasequeue)CouchbaseQueue

The CouchbaseQueue<V> class implements Queue<V>. It does not allow null values.

Example usage:

```java
Queue<String> shoppingList = new CouchbaseQueue<String>("queueDocId", collection, String.class, QueueOptions.queueOptions());
shoppingList.add("loaf of bread");
shoppingList.add("container of milk");
shoppingList.add("stick of butter");

// What does the JSON document look like?
System.out.println(collection.get("queueDocId").contentAsArray());
//=> ["stick of butter","container of milk","loaf of bread"]

String item;
while ((item = shoppingList.poll()) != null) {
  System.out.println(item);
  // => loaf of bread
  // => container of milk
  // => stick of butter
}

// What does the JSON document look like after draining the queue?
System.out.println(collection.get("queueDocId").contentAsArray());
//=> []
```