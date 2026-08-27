---
title: Concurrent Document Mutations
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.4/modules/howtos/pages/concurrent-document-mutations.adoc
  xref: xref:4.4@php-sdk:howtos:concurrent-document-mutations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/4.4/howtos/concurrent-document-mutations.html)

# Concurrent Document Mutations

> You can use the CAS value to control how concurrent document modifications are handled. It helps avoid and control potential race conditions in which some mutations may be inadvertently lost or overridden by mutations made by other clients. 

The _CAS_ is a value representing the current state of an item. Each time the item is modified, its CAS changes.

The CAS value itself is returned as part of a document's metadata whenever a document is accessed. In the SDK, this is presented as the `cas` field in the result object from any operation which executes successfully.

CAS is an acronym for _Compare And Swap_, and is known as a form of optimistic locking. The CAS can be supplied as parameters to the _replace_ and _remove_ operations. When applications provide the CAS, server will check the application-provided version of CAS against the CAS of the document on the server:

* If the two CAS values match (they compare successfully), then the mutation operation succeeds.
* If the two CAS values differ, then the mutation operation fails.

CAS, on the server-side might be implemented along these lines (pseudocode):

```c
uint Replace(string docid, object newvalue, uint oldCas=0) {
    object existing = this.kvStore.get(docid);
    if (!existing) {
        throw DocumentDoesNotExist();
    } else if (oldCas != 0 && oldCas != existing.cas) {
        throw CasMismatch();
    }
    uint newCas = ++existing.cas;
    existing.value = newValue;
    return newCas;
}
```

## [](#demonstration)Demonstration

The following demonstrates how the server handles CAS. A use case for employing the CAS is when adding a new field to an existing document. At the application level, this requires the following steps:

1. Read entire document.
2. Perform modification locally.
3. Store new document to server.

Assume the following two blocks of code are executing concurrently in different application instances:

__Table 1\. CAS flow__
| Thread #1                                                                                                                            | Thread #2                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| \>>> result = cb1.get('docid') \>>> new\_doc = result.value \>>> new\_doc\['field1'\] = 'value1' \>>> cb1.replace('docid', new\_doc) | \>>> result = cb2.get('docid') \>>> new\_doc = result.value \>>> new\_doc\['field2'\] = 'value2' \>>> cb2.replace('docid', new\_doc) |

Retrieving the document again yields:

```python
>>> cb1.get('docid').value
{u'field2': u'value2', u'a_field': u'a_value'}
```

Note that `field1` is not present, even though the application inserted it into the document. The reason is because the replace on Thread #2 happened to run after the replace on Thread #1, however Thread #1's replace was executed after Thread #2's get: Since the local version of the document on Thread #2 did not contain field1 (because Thread #1's update was not stored on the server yet), by executing the replace, it essentially overrode the replace performed by Thread #1.

| 1 | (#2): new\_doc = get("docid").value   |
| - | ------------------------------------- |
| 2 | (#1): new\_doc = get("docid").value   |
| 3 | (#1): new\_doc\["field1"\] = "value1" |
| 4 | (#2): new\_doc\["field2"\] = "value2" |
| 5 | (#1): cb.replace("docid", new\_doc)   |
| 6 | (#2): cb.replace("docid", new\_doc)   |

## [](#using-cas-example)Using CAS - Example

In the prior example, we saw that concurrent updates to the same document may result in some updates being lost. This is not because Couchbase itself has lost the updates, but because the application was unaware of newer changes made to the document and inadvertently overwrote them.

__Table 2\. CAS flow__
|                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \>>> result = cb1.get('docid') \>>> new\_doc = result.value \>>> print new\_doc {u'a\_field': u'a\_value'} \>>> cur\_cas = result.cas \>>> print cur\_cas 272002471883283 \>>> new\_doc\['field1'\] = 'value1' \>>> new\_result = cb1.replace(        'docid',        new\_doc,        cas=cur\_cas) Server's CAS matches cur\_cas. New CAS assigned \>>> print new\_result.cas 195896137937427 | \>>> result = cb2.get('docid') \>>> new\_doc = result.value \>>> print new\_doc {u'a\_field': u'a\_value'} \>>> cur\_cas = result.cas \>>> print cur\_cas 272002471883283 \>>> new\_doc\['field2'\] = 'value2' \>>> new\_result = cb2.replace(        'docid',        new\_doc,        cas=cur\_cas) CAS on server differs: 195896137937427 vs 272002471883283! |

## [](#handling-cas-errors)Handling CAS errors

If the item's CAS has changed since the last operation performed by the current client (i.e. the document has been changed by another client), the CAS used by the application is considered _stale_. If a _stale_ CAS is sent to the server (via one of the mutation commands, as above), the server will reply with an error, and the Couchbase SDK will accordingly return this error to the application (either via return code or exception, depending on the language).

How to handle this error depends on the application logic. If the application wishes to simply insert a new property within the document (which is not dependent on other properties within the document), then it may simply retry the read-update cycle by retrieving the item (and thus getting the new CAS), performing the local modification and then uploading the change to the server. For example, if a document represents a user, and the application is simply updating a user's information (like an email field), the method to update this information may look like this:

```php
function incrementVisitCount(Collection $collection, string $userId) {
    $maxRetries = 10;
    for ($i = 0; $i < $maxRetries; $i++) {
        // Get the current document contents
        $res = $collection->get($userId);

        // Increment the visit count
        $user = $res->content();
        $user["visit_count"]++;

        try {
            // Attempt to replace the document using CAS
            $opts = new ReplaceOptions();
            $opts->cas($res->cas());
            $collection->replace($userId, $user, $opts);
        } catch (CasMismatchError $ex) {
            continue;
        }

        // If no errors occured during the replace, we can exit our retry loop
        return;
    }
    printf("Replace failed after %d attempts\n", $maxRetries);
}
```

Sometimes more logic is needed when performing updates, for example, if a property is mutually exclusive with another property; only one or the other can exist, but not both.

## [](#performance-considerations)Performance considerations

CAS operations incur no additional overhead. CAS values are always returned from the server for each operation. Comparing CAS at the server involves a simple integer comparison which incurs no overhead.

## [](#cas-value-format)CAS value format

The CAS value should be treated as an opaque object at the application level. No assumptions should be made with respect to how the value is changed (for example, it is wrong to assume that it is a simple counter value). In the SDK, the CAS is represented as a 64 bit integer for efficient copying but should otherwise be treated as an opaque 8 byte buffer.

## [](#pessimistic-locking)Pessimistic locking

While CAS is the recommended way to perform locking and concurrency control, Couchbase also offers explicit _locking_. When a document is locked, attempts to mutate it without supplying the correct CAS will fail.

Documents can be locked using the _get-and-lock_ operation and unlocked either explicitly using the _unlock_ operation or implicitly by mutating the document with a valid CAS. While a document is locked, it may be retrieved but not modified without using the correct CAS value. When a locked document is retrieved, the server will return an invalid CAS value, preventing mutations of that document.

This handy table shows various behaviors while an item is locked:

__Table 3\. Behavior of various operations on a locked item__
| Operation                           | Result                                                                                                              |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| _get-and-lock_                      | Locked error.                                                                                                       |
| _get_                               | Always succeeds, but with an invalid CAS value returned (so it cannot be used as an input to subsequent mutations). |
| _unlock_ with bad/missing CAS value | Locked error.                                                                                                       |
| _unlock_ with correct CAS           | Item is unlocked. It can now be locked again and/or accessed as usual.                                              |
| Mutate with bad/missing CAS value   | CasMismatch error.                                                                                                  |
| Mutate with correct CAS value       | Mutation is performed and item is unlocked. It can now be locked again and/or accessed as usual.                    |

A document can be locked for a maximum of 30 seconds, after which the server will unlock it. This is to prevent misbehaving applications from blocking access to documents inadvertently. You can modify the time the lock is held for (though it can be no longer than 30 seconds).

> [!CAUTION]
> Setting a lock greater than 30 seconds will cause Couchbase Server to set the lock duration at the Server's _default_ value, which is 15 seconds.

Be sure to keep note of the _cas_ value when locking a document. You will need it when unlocking or mutating the document. The following blocks show how to use `lock` and `unlock` operations.

```php
    $res = $collection->getAndLock($userId, 2 /* seconds */);
    $lockedCas = $res->cas();

    /* // an example of simply unlocking the document:
     * $collection->unlock($userId, $lockedCas);
     */

    // Increment the visit count
    $user = $res->content();
    $user["visit_count"]++;

    $opts = new ReplaceOptions();
    $opts->cas($lockedCas);
    $collection->replace($userId, $user, $opts);
```

The handler will unlock the item either via an explicit unlock operation (`unlock`) or implicitly via modifying the item with the correct CAS.

If the item has already been locked, the server will respond with CasMismatch which means that the operation could not be executed temporarily, but may succeed later on.