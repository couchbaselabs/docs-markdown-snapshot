---
title: Sub-Document Operations with the C SDK
description: <em>Sub-document</em> operations can be used to efficiently access
  <em>parts</em> of documents.
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/howtos/pages/subdocument-operations.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/c-sdk/current/howtos/subdocument-operations.html)

# Sub-Document Operations with the C SDK

> _Sub-document_ operations can be used to efficiently access _parts_ of documents. Sub-document operations may be quicker and more network-efficient than _full-document_ operations such as _upsert_, _replace_ and _get_ because they only transmit the accessed sections of the document over the network. Sub-document operations are also atomic, allowing safe modifications to documents with built-in concurrency control. 

## [](#sub-documents)Sub-documents

Starting with Couchbase Server 4.5 you can atomically and efficiently update and retrieve _parts_ of a document. These parts are called _sub-documents_.

While full-document retrievals retrieve the entire document and full document updates require sending the entire document, sub-document retrievals only retrieve relevant parts of a document and sub-document updates only require sending the updated portions of a document. You should use sub-document operations when you are modifying only portions of a document, and full-document operations when the contents of a document is to change significantly.

> [!IMPORTANT]
> The sub-document operations described on this page are for _Key-Value_ requests only: they are not related to sub-document SQL++ (formerly N1QL) queries. (Sub-document SQL++ queries are explained in the section [Querying with SQL++](../concept-docs/n1ql-query.md).)

Considering the document:

customer123.json

```json
{
  "name": "Douglas Reynholm",
  "email": "douglas@reynholmindustries.com",
  "addresses": {
    "billing": {
      "line1": "123 Any Street",
      "line2": "Anytown",
      "country": "United Kingdom"
    },
    "delivery": {
      "line1": "123 Any Street",
      "line2": "Anytown",
      "country": "United Kingdom"
    }
  },
  "purchases": {
    "complete": [
      339, 976, 442, 666
    ],
    "abandoned": [
      157, 42, 999
    ]
  }
}
```

The paths `name`, `addresses.billing.country` and `purchases.complete[0]` are all valid paths.

## [](#retrieving)Retrieving

The _lookup-in_ operations query the document for certain path(s); these path(s) are then returned. You have a choice of actually retrieving the document path using the _subdoc-get_ sub-document operation, or simply querying the existence of the path using the _subdoc-exists_ sub-document operation. The latter saves even more bandwidth by not retrieving the contents of the path if it is not needed.

Check existence of Subdocument path

```c
        check(lcb_subdocspecs_exists(specs, 2, 0, paths[2].c_str(), paths[2].size()),
                "create SUBDOC-EXISTS operation");
```

Retrieve Subdocument value

```c
        check(lcb_subdocspecs_get(specs, 1, 0, paths[1].c_str(), paths[1].size()),
                "create SUBDOC-GET operation");
```

See the [code sample](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/subdoc-retrieving.cc) for use in context.

## [](#choosing-an-api)Choosing an API

_libcouchbase_ is an asynchronous library which means that operations results are passed to callbacks you define rather than being returned to functions. Callbacks are passed a `cookie` parameter which is a user defined pointer (i.e your own pointer, which can be `NULL`) to associate a specific command with a specific callback invocation.

```c
        lcb_cmdstore_create(&scmd, LCB_STORE_UPSERT);
        lcb_cmdstore_key(scmd, key.data(), key.size());
        lcb_cmdstore_value(scmd, value.data(), value.size());

        err = lcb_store(instance, nullptr, scmd);
        lcb_cmdstore_destroy(scmd);
        if (err != LCB_SUCCESS) {
            die("Couldn't schedule storage operation", err);
        }
        lcb_wait(instance, LCB_WAIT_DEFAULT);
```

For simple synchronous use, you will need to call `lcb_wait()` after each set of scheduled operations. During `lcb_wait` the library will block for I/O, and invoke your callbacks as the results of the operations arrive.

```c
            // This snippet lives inside the callback, so it is not necessary to call lcb_wait here
            lcb_CMDSTORE *cmd;
            lcb_cmdstore_create(&cmd, LCB_STORE_INSERT);
            lcb_cmdstore_key(cmd, key, nkey);
            lcb_cmdstore_value(cmd, value, nvalue);

            lcb_STATUS err = lcb_store(instance, nullptr, cmd);
            lcb_cmdstore_destroy(cmd);
            if (err != LCB_SUCCESS) {
                die("Couldn't schedule storage operation", err);
            }
```

See the [code sample](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/example%5F2minimal%5F2minimal%5F8c-example.html#a5) for use in context.

## [](#mutating)Mutating

Mutation operations modify one or more paths in the document. The simplest of these operations is _subdoc-upsert_, which, similar to the fulldoc-level _upsert_, will either modify the value of an existing path or create it if it does not exist.

```c
        lcb_CMDSTORE *cmd = nullptr;
        check(lcb_cmdstore_create(&cmd, LCB_STORE_UPSERT), "create UPSERT command");
        check(lcb_cmdstore_key(cmd, key.c_str(), key.size()), "assign ID for UPSERT command");
        check(lcb_cmdstore_value(cmd, value.c_str(), value.size()),
                "assign value for UPSERT command");
        check(lcb_store(instance, nullptr, cmd), "schedule UPSERT command");
        check(lcb_cmdstore_destroy(cmd), "destroy UPSERT command");
        lcb_wait(instance, LCB_WAIT_DEFAULT);
```

See the [code sample](https://github.com/couchbase/docs-sdk-c/blob/release/3.3/modules/devguide/examples/c/subdoc-retrieving.cc) for use in context.

> [!NOTE]
> `mutateIn` is an _atomic_ operation. If any single `ops` fails, then the entire document is left unchanged.

## [](#array-insertion)Array insertion

New elements can also be _inserted_ into an array. While _append_ will place a new item at the _end_ of an array and _prepend_ will place it at the beginning, _insert_ allows an element to be inserted at a specific _position_. The position is indicated by the last path component, which should be an array index. For example, to insert `"42"` as the last element in the array `[1,2,3,4]`, the code would look like:

```c
std::string value_to_add{ "42" };
check(lcb_subdocspecs_array_add_last(specs, 0, 0, paths[0].c_str(), paths[0].size(), value_to_add.c_str(), value_to_add.size()),"create ARRAY_ADD_LAST operation");
```

Note that the array must already exist and that the index must be valid (i.e. it must not point to an element which is out of bounds).

## [](#executing-multiple-operations)Executing multiple operations

Multiple sub-document operations can be executed at once on the same document, allowing you to retrieve or modify several sub-documents at once. When multiple operations are submitted within the context of a single _lookup-in_ or _mutate-in_ command, the server will execute all the operations with the same version of the document.

> [!NOTE]
> Unlike _batched operations_ which is simply a way of sending multiple individual operations efficiently on the network, multiple subdoc operations are formed into a single command packet, which is then executed atomically on the server. You can submit up to 16 operations at a time.

When submitting multiple _mutation_ operations within a single _mutate-in_ command, those operations are considered to be part of a single transaction: if any of the mutation operations fail, the server will logically roll-back any other mutation operations performed within the _mutate-in_, even if those commands would have been successful had another command not failed.

When submitting multiple _retrieval_ operations within a single _lookup-in_ command, the status of each command does not affect any other command. This means that it is possible for some retrieval operations to succeed and others to fail. While their statuses are independent of each other, you should note that operations submitted within a single _lookup-in_ are all executed against the same _version_ of the document.

## [](#subdoc-create-parents)Creating parents

Sub-document mutation operations such as _subdoc-upsert_ or _subdoc-insert_ will fail if the _immediate parent_ is not present in the document. Consider:

```json
{
    "level_0": {
        "level_1": {
            "level_2": {
                "level_3": {
                    "some_field": "some_value"
                }
            }
        }
    }
}
```

Looking at the `some_field` field (which is really `level_0.level_1.level_2.level_3.some_field`), its _immediate_ parent is `level_3`. If we were to attempt to insert another field, `level_0.level_1.level_2.level_3.another_field`, it would succeed because the immediate parent is present. However if we were to attempt to _subdoc-insert_ to `level_1.level_2.foo.bar` it would fail, because `level_1.level_2.foo` (which would be the immediate parent) does not exist. Attempting to perform such an operation would result in a Path Not Found error.

By default the automatic creation of parents is disabled, as a simple typo in application code can result in a rather confusing document structure.

## [](#error-handling)Error handling

Subdoc operations have their own set of errors. When programming with subdoc, be prepared for any of the full-document errors (such as _Document Not Found_) as well as special sub-document errors which are received when certain constraints are not satisfied. Some of the errors include:

* **Path does not exist**: When retrieving a path, this means the path does not exist in the document. When inserting or upserting a path, this means the _immediate parent_ does not exist.
* **Path already exists**: In the context of an _insert_, it means the given path already exists. In the context of _array-add-unique_, it means the given value already exists.
* **Path mismatch**: This means the path may exist in the document, but that there is a type conflict between the path in the document and the path in the command. Consider the document:  
```json  
{ "tags": ["reno", "nevada", "west", "sierra"] }  
```  
The path `tags.sierra` is a mismatch, since `tags` is actually an array, while the path assumes it is a JSON object (dictionary).
* **Document not JSON**: This means you are attempting to modify a binary document using sub-document operations.
* **Invalid path**: This means the path is invalid for the command. Certain commands such as _subdoc-array-insert_ expect array elements as their final component, while others such as _subdoc-upsert_ and _subdoc-insert_ expect dictionary (object) keys.

If a Sub-Document command fails a top-level error is reported (_Multi Command Failure_), rather than an individual error code (e.g. _Path Not Found_). When receiving a top-level error code, you should traverse the results of the command to see which individual code failed.

## [](#path-syntax)Path syntax

Path syntax largely follows SQL++ conventions: A path is divided into components, with each component referencing a specific _level_ in a document hierarchy. Components are separated by dots (`.`) in the case where the element left of the dot is a dictionary, or by brackets (`[n]`) where the element left of the bracket is an array and `n` is the index within the array.

As a special extension, you can indicate the _last element_ of an array by using an index of `-1`, for example to get the last element of the array in the document

```json
{"some":{"array":[1,2,3,4,5,6,7,8,9,0]}}
```

Use `some.array[-1]` as the path, which will return the element `0`.

Each path component must conform as a JSON string, as if it were surrounded by quotes, and any character in the path which may invalidate it as a JSON string must be escaped by a backslash (`\`). In other words, the path component must match exactly the path inside the document itself. For example:

```json
{"literal\"quote": {"array": []}}
```

must be referenced as `literal\"quote.array`.

If the path also has special path characters (i.e. a dot or brackets) it may be escaped using SQL++ escapes. Considering the document

```json
{"literal[]bracket": {"literal.dot": true}}
```

A path such as \`literal\[\]bracket\`.\`literal.dot\`. You can use double-backticks (\`\`) to reference a literal backtick.

If you need to combine both JSON _and_ path-syntax literals you can do so by escaping the component from any JSON string characters (e.g. a quote or backslash) and then encapsulating it in backticks (`` `path` ``).

> [!NOTE]
> Currently, paths cannot exceed 1024 characters, and cannot be more than 32 levels deep.

Unresolved include directive in modules/howtos/pages/subdocument-operations.adoc - include::6.6@sdk:shared:partial$sdk-xattr-overview.adoc\[\]