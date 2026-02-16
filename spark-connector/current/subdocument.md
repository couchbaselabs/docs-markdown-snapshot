[View original HTML](/spark-connector/current/subdocument.html)

> Use sub-document KV writes with Spark DataFrames to update parts of JSON documents efficiently. 

Couchbase supports sub-document writes that update only specific parts of the document, and users writing large documents may find this provides a performance optimization, or allows concurrent actors to modify different parts of the same documents. The Spark Connector exposes the sub-document writes via both [RDDs](working-with-rdds.md) and DataFrames.

The connector will ultimately perform sub-document KV mutateIn calls, one for each row/document in the DataFrame.

For a mutateIn call, up to 16 sub-document 'specs' can be provided. A spec has three elements:

* A spec operation. All sub-document spec operations are supported by the connector: upsert, insert, replace, remove, arrayAppend, arrayPrepend, arrayInsert, arrayAddUnique, increment and decrement.
* A path where the operation acts, such as `user.name` (the `name` field of the `user` object), or `user.addresses[1]`.
* A value, which can be any valid JSON value. This is written to the path.

For Spark, the core idea is that the DataFrame be setup by the application so that:

* As usual with KV DataFrame writes, each row represents a single document, which will be written with a single mutateIn KV call by the Spark connector.
* Each column represents a sub-document spec to be performed by every mutateIn call. The column title combines the operation type and the path it acts on with format "operation:path" e.g. "upsert:user.name". The "upsert:" prefix is optional as it’s the default.
* Each cell represents the value that will be written by that sub-document spec to that document.

An example will help make this clear. Here we take an incoming DataFrame, manipulate it to specify the sub-document specs we want, and then write it to Couchbase:

```scala
// Get a read Spark DataFrame from Couchbase (but could come from anywhere):
val queryData = spark.read.format("couchbase.query").load()

// Transform the data and prepare for subdoc operations
val transformedData = queryData
  .select(
    // This will be used as the document id, as usual
    queryData("__META_ID"),
    // The values in these columns will be used as the sub-document spec values
    queryData("employee_name"),
    queryData("employee_age"),
  )
  // Rename the columns to reflect the sub-document specs we wish to perform:
  // Spec 1: Upsert the contents of the "name" column into the "user.name" field
  // We could also write "upsert:user.name", but upsert is the default.
  .withColumnRenamed("name", "user.name")
  // Spec 2: Upsert the contents of the "age" column into the "user.age" field
  .withColumnRenamed("age", "user.age")
```

Our DataFrame now looks something like:

```none
__META_ID    | user.name          | user.age
-----------------------------------------
"docId1"     | "John Richardson"  | 29
"docId2"     | "Jane Doe"         | 34
```

Now write the transformed data back to KV using WriteModeSubdocUpsert, which activates sub-document mode.

As we have two rows in the DataFrame this will result in two sub-document KV mutateIn calls from the connector, and each will upsert two fields "user.name" and "user.age" into the target documents.

```scala
transformedData.write
  .format("couchbase.kv")
  .option(KeyValueOptions.Bucket, "aBucket")
  .option(KeyValueOptions.Scope, "aScope")
  .option(KeyValueOptions.Collection, "aCollection")
  // SubdocUpsert is used which will create the docs if they don't exist, otherwise overwrite them
  .option(KeyValueOptions.WriteMode, KeyValueOptions.WriteModeSubdocUpsert)
  .save()
```

And we will end up with "docId1" containing JSON:

```none
{
  "user": {
    "name": "John Richardson",
    "age": 29
  }
  // .. and the rest of the document, which will not have been modified
}
```

This is a very simple example of what is possible with sub-document. We can also perform operations that manipulate arrays, as shown below:

```scala
val queryData = spark.read.format("couchbase.query").load()

val transformedData = queryData
  .select(
    queryData("__META_ID"),
    queryData("employee_phone_number")
  )
  .withColumnRenamed("employee_phone_number", "arrayAppend:user.phoneNumbers")

transformedData.write
  .format("couchbase.kv")
  .option(KeyValueOptions.Bucket, "aBucket")
  .option(KeyValueOptions.Scope, "aScope")
  .option(KeyValueOptions.Collection, "aCollection")
  .option(KeyValueOptions.WriteMode, KeyValueOptions.WriteModeSubdocUpsert)
  .save()
```

To illustrate how some of the other operations work, we’ll use this sample existing document:

```json
{
  "user": {
    "age": 28,
    "phoneNumbers": ["+1 8267485570"]
  }
}
```

__Table 1\. Sub-document operation examples__
| Operation and Path                   | Value                  | Result                                                                               |
| ------------------------------------ | ---------------------- | ------------------------------------------------------------------------------------ |
| "increment:user.age"                 | 1                      | {   "user": {     "age": 29,     ...   } }                                           |
| "arrayAppend:user.phoneNumbers"      | "+1 9833848745"        | {   "user": {     ...     "phoneNumbers": \["+1 8267485570", "+1 9833848745"\]   } } |
| "arrayInsert:user.phoneNumbers\[1\]" | "+1 9833848745"        | {   "user": {     ...     "phoneNumbers": \["+1 8267485570", "+1 9833848745"\]   } } |
| "remove:user.phoneNumbers"           | <anything except null> | {   "user": {     ... phoneNumbers removed   } }                                     |

See the [Scala SDK documentation on sub-document operations](https://docs.couchbase.com/scala-sdk/current/howtos/subdocument-operations.html) for full details.

N.b. `remove` sub-document spec operations are a special case as they will ignore the provided value. Hence any value can be used, except null, as Spark will automatically remove null columns before it passes the DataFrame to the connector.

## [](#sub-document-error-handling)Sub-document error handling

The same [Failure handling during persistence](spark-sql.md#failure-handling-during-persistence) error handling detailed elsewhere can be used with sub-document operations, so the failures of individual sub-document KV calls do not have to fail the entire Spark job.

```scala
dataFrame.write
  .format("couchbase.kv")
  .option(KeyValueOptions.Bucket, "aBucket")
  .option(KeyValueOptions.Scope, "aScope")
  .option(KeyValueOptions.Collection, "aCollection")
  // Specify a Couchbase collection to write errors to
  .option(KeyValueOptions.ErrorBucket, "errorBucket")
  .option(KeyValueOptions.ErrorScope, "errorScope")
  .option(KeyValueOptions.ErrorCollection, "errorCollection")
  .save()
```

Bear in mind that the specified sub-document specs will be applied to all documents in the DataFrame, so the specs should be chosen to be compatible. For instance, "insert" and "replace" operations will fail if the field exists or does not respectively, while "upsert" will succeed regardless, and so will often be a better choice.

Similarly, we generally recommend using `WriteModeSubdocUpsert` rather than `WriteModeSubdocInsert` (which fails if any document already exists) or `WriteModeSubdocReplace` (which fails if any document does not), to be maximally compatible with all documents in the DataFrame.