---
title: Fleece C API
description: Introducing the key concepts of the Fleece C API
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/c/pages/c_fleece.adoc
  xref: xref:4.0@couchbase-lite:c:c_fleece.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/4.0/c/c_fleece.html)

# Fleece C API

> Description — _Introducing the key concepts of the Fleece C API_  

## [](#introduction)Introduction

_Couchbase Lite_ for C makes extensive use of the Fleece C API for accessing document data. This content introduces some basic Fleece API concepts and examples.

Fleece is a binary encoding for semi-structured data. Its data model is a superset of JSON, adding support for binary data (blobs) to give seven data types: null, boolean, numbers, strings, data, arrays, and dictionaries. Arrays can contain any data types. Dictionary keys are strings, with values of any data type.

Fleece is designed to be:

* Very fast to read:  
No parsing is needed, and the data can be navigated and read without any heap allocation. Fleece objects are internal pointers into the raw data. Arrays and dictionaries can be random-accessed. Performance on real-world-scale data has been clocked at 20x that of JSON.
* Compact:  
Simple values will be about the same size as JSON. Complex ones may be much smaller, since repeated values, especially strings, only need to be stored once.
* Efficient to convert into native objects:  
Numbers are binary, strings are raw UTF-8 without quoting, binary data is not base64-encoded. Storing repeated values once means they only need to be converted into native objects once.
* Appendable:  
Fleece is what's known as a persistent data structure. A Fleece document can be mutated by appending data to it. The mutation is in effect a delta, so it's usually much smaller than the original document. And the original document is unchanged, which is great for concurrency as well as (simple) version control.  
For more information, see  
[Fleece on GitHub](https://github.com/couchbaselabs/fleece) | [Using Fleece](https://github.com/couchbaselabs/fleece/wiki/Using-Fleece) | [Fleece Header File](https://github.com/couchbaselabs/fleece/blob/master/API/fleece/Fleece.h)

## [](#values)Values

Fleece's data types are almost identical to those of JSON, with the notable addition of binary data types.

Basically Fleece provides seven data types: _null_, _boolean_, _numbers_, _strings_, _arrays_, _dictionaries_, and _data_. Arrays can contain any data type and dictionaries have strings as keys, with values of any data type.

The basic Fleece data type is **FLValue**, an opaque pointer reference to a value of any type.

Use the _FLValue\_GetType_ API to check the value's actual type and _FLValue\_As<Type Name>_ to get the actual value as shown in [Use FLValue](#ex-flvalue)

Use FLValue

```c
FLDict props = CBLDocument_Properties(doc);
FLValue value = FLDict_Get(props, FLSTR("name”));
FLValueType type = FLValue_GetType(value); (1)
if (type == kFLString) {
    FLString name = FLValue_AsString(value);
    doSomethingWith(name); (2)
}
```

| **1** | Find the values data type |
| ----- | ------------------------- |
| **2** | Cast to appropriate type  |

See: [Fleece Header File](https://github.com/couchbaselabs/fleece/blob/master/API/fleece/Fleece.h) for more details.

## [](#slices-and-strings)Slices and Strings

### [](#flslice)FLSlice

Another basic Fleece data type, _FLSlice_ a simple struct consisting of a pointer and a length. It points to a block of memory, without implying ownership of that memory. FLSlice is used to represent both binary data and strings.

### [](#flstring)FLString

_FLString_ is a typedef of FLSlice, which explicitly represents a string value. Use the _FLSTR("Some String")_ macro to create an FLString from a string literal — see: [Create an FLString](#ex-flstr)

Create an FLString

```c
CBLDatabase* db = CBLDatabase_Open( (FLSTR("my-database"), NULL, &err); (1)
```

| **1** | FLSTR("My-database") creates the FLString from the given string literal. |
| ----- | ------------------------------------------------------------------------ |

### [](#flsliceresultflstringresult)FLSliceResult/FLStringResult

FLSlice doesn't imply an ownership of memory. However, _FLSliceResult_/_FLStringResult_ is an FLSlice type which _does_ own memory and is reference-counted.  

In general, whenever an FLSliceResult/FLStringResult is returned from an API call, you are responsible for calling FLSliceResult\_Release when you are done using it.

For an example of `FLSliceResult` in use, see: [Using FLStringResult](#ex-flsliceresult).

Using FLStringResult

```c
FLStringResult path = CBLDatabase_Path(db);
doSomethingWith(path);
FLSliceResult_Release(path); (1)
```

| **1** | You are responsible for calling FLSliceResult\_Release when you are done using it. |
| ----- | ---------------------------------------------------------------------------------- |

FLSlice and FLSliceResult have utility functions such as:

* `FLSlice_Equal` — compares two slices for equality.
* `FLSlice_Compare` — a 3-way comparison, like strcmp().
* `FLSlice_Copy`
* `FLSliceResult_New`
* `FLSliceResults_Release`

### [](#null-slices)Null Slices

The null slice {NULL, 0} is represented by the constant `kFLSliceNull`.  
You test a slice for null by comparing its pointer (buf) with NULL — see: [Test for null slice](#ex-flnullslice)

Test for null slice

```c
FLValue value = FLDict_Get(props, FLSTR("name”));
FLString name = FLValue_AsString(value);
if (name.buf != NULL) {
    doSomethingWith(name);
}
```

See: [FLSlice.h](https://github.com/couchbaselabs/fleece/blob/master/API/fleece/FLSlice.h) for more details on data slices.

## [](#dictionaries)Dictionaries

### [](#immutable)Immutable

_FLDict_ represents an immutable dictionary type in Fleece.  
To access a value with a string key from a dictionary, use FLDict\_Get — as shown in: [Get dictionary value](#ex-flget).

Get dictionary value

```c
FLDict props = CBLDocument_Properties(doc);
FLValue value = FLDict_Get(props, FLSTR("name”));
doSomethingWith(value);
```

To iterate through each key-value pair in the dictionary, use _FLDictIterator_, as shown in: [Iterate key-value pairs in dictionary](#ex-fliterator)

Iterate key-value pairs in dictionary

```c
FLDictIterator iter;
FLDictIterator_Begin(myDict, &iter);
FLValue value;
while (NULL != (value = FLDictIterator_GetValue(&iter))) {
    FLString key = FLDictIterator_GetKeyString(&iter);
    doSomethingWith(key, value);
    FLDictIterator_Next(&iter);
}
```

### [](#mutable)Mutable

**FLMutableDictionary** is a mutable dictionary type that allows editing.

To create a new mutable dictionary, use FLMutableDict\_New() — see: [Set dictionary value](#ex-flmutabledict-new).

Set dictionary value

```c
FLMutableDict myDict = FLMutableDict_New()
FLMutableDict_SetString(myDict, FLSTR(“name”), FLSTR(“John Doe”));
doSomethingWith(myDict);
FLMutableDict_Release(myDict); (1)
```

| **1** | don't forget to release resources once you have finished with them |
| ----- | ------------------------------------------------------------------ |

## [](#lbl-fleece-arrays)Arrays

### [](#immutable-2)Immutable

_FLArray_ represents an immutable array type in Fleece.  
use _FLArray\_Count_ and _FLArray\_Get_ respectively, to get the numbers of values in an array and to get a value using with an index — as shown in [Use arrays](#ex-flarray-get).

Use arrays

```c
int count = FLArray_Count(myArray);
if (count > 0) {
    FLValue value = FLArray_Get(myArray, 0);
    doSomethingWith(value);
}
```

Use _FLArrayIterator_ to iterate through arrays, as shown in : [Array iteration](#ex-array-iteration).

Array iteration

```c
FLArrayIterator iter;
FLArrayIterator_Begin(myArray, &iter);
FLValue value;
while (NULL != (value = FLArrayIterator_GetValue(&iter))) {
    doSomethingWith(value);
    FLArrayIterator_Next(&iter);
}
```

### [](#mutable-2)Mutable

_FLMutableArray_ is a mutable array type that allows editing.  

To create a new mutable array, use _FLMutableArray\_New_.

To append a value into the array, use _FLMutableArray\_Append<Type Name>_.

Append values to array

```c
FLMutableArray myArray = FLMutableArray_New();
FLMutableArray_AppendString(myArray, FLSTR(“String 1”));
FLMutableArray_AppendString(myArray, FLSTR(“String 2”)); (1)
doSomethingWith(myArray);
FLMutableArray_Release(myArray)
```

| **1** | To set a value at a specific array index, use FLMutableArraySet<Type Name>. |
| ----- | --------------------------------------------------------------------------- |

## [](#json-support)JSON Support

Fleece provides a JSON utility that allows you to parse JSON string into Fleece or generate JSON from Fleece.

### [](#parsing-json)Parsing JSON

Use **FLDoc\_FromJSON** to convert JSON Dictionary or Array into Fleece Dictionary or Array.

Parse JSON data to Fleece

```c
FLError error;
FLDoc doc = FLDoc_FromJSON(jsonString, &error);
if (doc) {
    FLValue value = FLDoc_GetRoot(doc);
    FLDict dict = FLValue_AsDict(value);
    doSomethingWith(dict);
}
FLDoc_Release(doc);
```

### [](#generating-json)Generating JSON

Use FLValue\_ToJSON to convert FLValue into JSON string

Convert to JSON

```c
FLDict props = CBLDocument_Properties(doc);
FLStringResult jsonString = FLValue_ToJSON((FLValue) props);
doSomethingWith(jsonString);
FLSliceResult_Release(jsonString);
```

## [](#memory-management)Memory Management

In general, Mutable objects are _reference counted_: with MutableArray and Mutable Dictionary each having _retain_ and _release_ functions.  
The lifespan of Immutable objects is the same as that of the memory block from which they are parsed. They cannot be individually released or retained.

For more see:  
[Fleece Mememory Management](https://github.com/couchbaselabs/fleece/wiki/Using-Fleece#5-memory-management) | [Advanced Fleece Mememory Management](https://github.com/couchbaselabs/fleece/wiki/Advanced-Fleece#for-memory-management)

## [](#related-content)Related Content

### [](#)

How to . . .

* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.