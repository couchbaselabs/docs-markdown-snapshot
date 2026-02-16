[View original HTML](/server/current/guides/deleting-data.html)

> How to delete documents with a command line tool or an SDK. 

## [](#introduction)Introduction

In situations where data is no longer needed, Couchbase Server provides a remove operation to delete a document from the database permanently.

Read the following for further information about the clients available:

* [Command Line Clients](../../../c-sdk/current/hello-world/cbc.md)
* [SDK Clients](#home::sdk.adoc)

|  | Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Sample Buckets](../manage/manage-settings/install-sample-buckets.md) for details. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#deleting-a-document)Deleting a Document

To delete a specific field within a document, perform a Sub-Document remove operation.

* cbc
* .NET
* Java
* Node.js
* Python

Use the `cbc rm` command to delete a document from the database.

---

The example below deletes document `airport_1254` from the database.

```shell
cbc rm -u Administrator -P password -U couchbase://localhost/travel-sample airport_1254
```

Result

```console
airport_1254          Deleted
```

For further details, refer to [cbc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5F2cbc.html).

Use the `RemoveAsync()` method to delete a document from the database.

---

The example below deletes document `hotel-123` from the database.

```csharp
await hotelCollection.RemoveAsync("hotel-123");
```

|  | If the document does not exist, the SDK will return a DocumentNotFoundException error. |
|  | -------------------------------------------------------------------------------------- |

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

Use the `remove()` method to delete a document from the database.

---

The example below deletes document `hotel-123` from the database.

```java
MutationResult removeResult = hotelCollection.remove("hotel-123");
System.out.println("CAS:" + removeResult.cas());
```

|  | If the document does not exist, the SDK will return a DocumentNotFoundException error. |
|  | -------------------------------------------------------------------------------------- |

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html).

Use the `remove()` function to delete a document from the database.

---

The example below deletes document `hotel-123` from the database.

```nodejs
const removeResult = await hotelCollection.remove('hotel-123')
console.log('CAS:', removeResult.cas)
```

|  | If the document does not exist, the SDK will return a DocumentNotFoundError error. |
|  | ---------------------------------------------------------------------------------- |

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

Use the `remove()` function to delete a document from the database.

---

The example below deletes document `hotel-123` from the database.

```python
remove_result = hotel_collection.remove("hotel-123")
print("CAS:", remove_result.cas)
```

|  | If the document does not exist, the SDK will return a DocumentNotFoundException error. |
|  | -------------------------------------------------------------------------------------- |

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#deleting-a-sub-document)Deleting a Sub-Document

To delete a specific field within a document you can perform a Sub-Document remove operation.

* cbc-subdoc
* .NET
* Java
* Node.js
* Python

1. Connect to the `cbc-subdoc` interactive shell.
2. Use the `remove` command to delete a field from a document.
3. Pass the field to remove with the `--path` argument.

---

The example below deletes the `url` field from document `hotel-123`.

```console
cbc-subdoc -u Administrator -P password -U couchbase://localhost/travel-sample
subdoc> remove hotel-123 --path url
```

Result

```console
hotel-123          CAS=0x16be2f11c6040000
0. Size=0, RC=LCB_SUCCESS (0)
```

|  | If the path cannot be found, cbc-subdoc will return a LCB\_ERR\_SUBDOC\_PATH\_NOT\_FOUND error. |
|  | ----------------------------------------------------------------------------------------------- |

For further details, refer to [cbc-subdoc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5Fcbc%5Fsubdoc.html).

1. Call the `MutateInAsync()` method, which takes a document ID and an IEnumerable containing `MutateInSpec` objects.
2. Use a `MutateInSpec` object to specify the sub-operation to be performed within the lookup.

A `MutateInResult` object is returned containing the result and metadata relevant to the Sub-Document remove operation.

---

The example below deletes the `url` field from document `hotel-123`.

```csharp
var mutateInResult = await hotelCollection.MutateInAsync("hotel-123",
	specs => specs.Remove("url")
);
Console.WriteLine($"Cas: {mutateInResult.Cas}");
```

|  | If the path does not exist, the SDK will return a PathNotFoundException error. |
|  | ------------------------------------------------------------------------------ |

Click the  View button to see this code in context.

For more information, see [CollectionExtensions](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.KeyValue.CollectionExtensions.html).

1. Call the `mutateIn()` method, which takes a document ID and an array of `MutateInSpec` objects.
2. Use a `MutateInSpec` object to specify the sub-operation to be performed within the lookup.

A `MutateInResult` object is returned, containing the result and metadata relevant to the Sub-Document remove operation.

---

The example below deletes the `url` field from document `hotel-123`.

```java
List<MutateInSpec> specs = Arrays.asList(MutateInSpec.remove("url"));

MutateInResult mutateInResult = hotelCollection.mutateIn("hotel-123", specs);
System.out.println("CAS:" + mutateInResult.cas());
```

|  | If the path does not exist, the SDK will return a PathNotFoundException error. |
|  | ------------------------------------------------------------------------------ |

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Collection.html).

1. Call the `mutateIn()` method, which takes a document ID and an array of `MutateInSpec` objects.
2. Use a `MutateInSpec` object to specify the sub-operation to be performed within the lookup.

A `MutateInResult` object is returned, containing the result and metadata relevant to the Sub-Document remove operation.

---

The example below deletes the `url` field from document `hotel-123`.

```nodejs
mutateInResult = await hotelCollection.mutateIn('hotel-123', [
  couchbase.MutateInSpec.remove('url'),
])
console.log('CAS:', mutateInResult.cas)
```

|  | If the path does not exist, the SDK will return a PathNotFoundError error. |
|  | -------------------------------------------------------------------------- |

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Collection.html).

1. Call the `lookup_in()` function, which takes a document ID and a list of `MutateInSpec` objects.
2. Use a `MutateInSpec` object to specify the sub-operation to be performed within the lookup.

A `MutateInResult` object is returned, containing the result and metadata relevant to the Sub-Document remove operation.

---

The example below deletes the `url` field from document `hotel-123`.

```python
mutate_in_result = hotel_collection.mutate_in(
    "hotel-123", [subdocument.remove("url")]
)
print("CAS:", mutate_in_result.cas)
```

|  | If the path does not exist, the SDK will return a PathNotFoundException error. |
|  | ------------------------------------------------------------------------------ |

Click the  View button to see this code in context.

For more information, see [Collection](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object).

## [](#related-links)Related Links

Key-Value Operations with SDKs:

* [C](../../../c-sdk/current/howtos/kv-operations.md)| [C++](../../../cxx-sdk/current/howtos/kv-operations.md)| [.NET](../../../dotnet-sdk/current/howtos/kv-operations.md)| [Go](../../../go-sdk/current/howtos/kv-operations.md)| [Java](../../../java-sdk/current/howtos/kv-operations.md)| [Kotlin](../../../kotlin-sdk/current/howtos/kv-operations.md)| [Node.js](../../../nodejs-sdk/current/howtos/kv-operations.md)| [PHP](../../../php-sdk/current/howtos/kv-operations.md)| [Python](../../../python-sdk/current/howtos/kv-operations.md)| [Ruby](../../../ruby-sdk/current/howtos/kv-operations.md)| [Rust](../../../rust-sdk/current/howtos/kv-operations.md)| [Scala](../../../scala-sdk/current/howtos/kv-operations.md)

Sub-Document operations with SDKs:

* [C](../../../c-sdk/current/howtos/subdocument-operations.md)| [C++](../../../cxx-sdk/current/howtos/subdocument-operations.md)| [.NET](../../../dotnet-sdk/current/howtos/subdocument-operations.md)| [Go](../../../go-sdk/current/howtos/subdocument-operations.md)| [Java](../../../java-sdk/current/howtos/subdocument-operations.md)| Kotlin | [Node.js](../../../nodejs-sdk/current/howtos/subdocument-operations.md)| [PHP](../../../php-sdk/current/howtos/subdocument-operations.md)| [Python](../../../python-sdk/current/howtos/subdocument-operations.md)| [Ruby](../../../ruby-sdk/current/howtos/subdocument-operations.md)| [Rust](../../../rust-sdk/current/howtos/subdocument-operations.md)| [Scala](../../../scala-sdk/current/howtos/subdocument-operations.md)