---
title: Language Constructs
description: Language constructs are the fundamental units of a language.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/eventing/pages/eventing-language-constructs.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:eventing:eventing-language-constructs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/eventing/eventing-language-constructs.html)

# Language Constructs

> Language constructs are the fundamental units of a language. 

This page describes which JavaScript constructs Eventing Functions do and do not support.

> [!NOTE]
> Couchbase functions inherit support for most ECMAScript constructs by using Google v8 as the execution container. Certain capabilities have been removed and are not supported in order to handle the automatic sharding and scaling of functions.

## [](#supported-lang-features)Supported Language Features

Eventing Functions support the following features:

* [Basic Keyspace Accessors](#basic%5Fbucket%5Faccessors)
* [Advanced Keyspace Accessors](#advanced%5Fbucket%5Faccessors)
* [Logging](#logging)
* [SQL++ Statements](#n1ql%5Fstatements)

### [](#basic%5Fbucket%5Faccessors)Basic Keyspace Accessors

Buckets that are bound to an Eventing Function appear as a global JavaScript map. Map operations like GET, SET, and DELETE are exposed to the GET, SET, and DELETE Data Service provider operations.

If the bucket binding has a wildcard `*` for its scope or collection, you cannot use a Basic Keyspace Accessor to access the Data Service. Instead, you must use an [Advanced Keyspace Accessor](#advanced%5Fbucket%5Faccessors).

| Operation | Description                                                                                                                                                                                                                                                                                                                                                                               |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GET       | operator\[\] is applied on a bucket binding and used as a value expression. Fetches the object from the KV bucket that the variable is bound to. Returns the parsed JSON value as a JavaScript object. Fetching a non-existent object from a bucket returns an undefined value. This operation throws an exception if the underlying bucket GET operation fails with an unexpected error. |
| SET       | operator\[\] appears to the left of the \= assignment statement. Sets the provided JavaScript value into the KV bucket that the variable is bound to. Replaces any existing value with the specified key. This operation throws an exception if the underlying bucket SET operation fails with an unexpected error.                                                                       |
| DELETE    | operator\[\] appears after the JavaScript delete keyword. Deletes the provided key from the KV bucket that the variable is bound to. Returns a no-op if the object does not exist. This operation throws an exception if the underlying bucket DELETE operation fails with an unexpected error.                                                                                           |

```javascript
function OnUpdate(doc, meta) {
  // Assuming 'dest' is a bucket alias or binding to a keyspace
  var val = dest[meta.id];         // this is a bucket GET operation
  dest[meta.id] = {"status":3};    // this is a bucket SET operation
  delete dest[meta.id];            // this is a bucket DEL operation
}
```

### [](#advanced%5Fbucket%5Faccessors)Advanced Keyspace Accessors

Advanced Keyspace Accessors expose a larger set of options and operators than [Basic Keyspace Accessors](#basic%5Fbucket%5Faccessors). They have non-trivial argument sets and return values.

See [Advanced Keyspace Accessors](eventing-advanced-keyspace-accessors.md) for more details.

### [](#logging)Logging

The `log()` function allows Eventing Functions to log user-defined messages. `log()` statements are logged in each Eventing Function’s log file.

`log()` does not throw exceptions.

```javascript
function OnUpdate(doc, meta) {
  log("Now processing: " + meta.id);
}
```

The Eventing Service also creates a system log file named `eventing.log`. This file exists in all Eventing Functions and captures management and lifecycle information. The end-user cannot write to this file.

### [](#n1ql%5Fstatements)SQL++ Statements

You can use top-level SQL++ keywords like SELECT, UPDATE, INSERT, and DELETE as inline words in Eventing Functions. These operations are accessible through the returned iterable handle.

SQL++ Query results, through the SELECT operation, are streamed in batches to the iterable handle as the iteration progresses through the result set.

> [!NOTE]
> To avoid recursion, an Eventing Function can listen for mutations in a bucket. SQL++ DML statements cannot manipulate documents in that same bucket. To work around this, you can use the exposed data service KV map in your Eventing Function.

The following Function has a feed boundary of **Everything**, which means the same SQL++ statement is executed 7,303 times. To execute only one query, you can configure your feed boundary to be **From now** and to mutate only one document in the keyspace `beer-sample`.`_default`.`_default`.

You can also use an optimal index, which makes your query performance 24 times faster.

```javascript
function OnUpdate(doc, meta) {
    var strong = 70;
    var results =
        SELECT *                               /* SQL++ queries are embedded directly */
        FROM `beer-sample`._default._default   /* Token escaping is standard SQL++ style */
        WHERE abv > $strong;                   // Local variable reference using $ syntax
    for (var beer of results) {                // Stream results using 'for' iterator
        log(beer);
        break;
    }
    results.close();                           // End the query and free resources held
}
```

The embedded SQL++ call starts the query and returns a JavaScript iterable object that represents the result set of the query. You can iterate the returned handle using standard JavaScript mechanisms like `for…​of` loops.

The iterator is an input iterator, meaning the elements are read-only. The variables created inside the iterator are local to it. You cannot use the keyword `this` in the body of the iterator.

You must close each result set with the `close()` method, which stops the underlying SQL++ query and releases associated resources. In some cases like nested SQL++ lookups, failing to explicitly call `close()` can use too many SQL++ resources and lead to poor performance.

#### [](#valid-and-invalid-statements)Valid and Invalid Statements

SQL++ is not syntactically part of the JavaScript language. Eventing transpiles the Eventing Function code to identify SQL++ statements and convert them to a standard JavaScript function call. This call then returns an iterable object with a `close()` method.

To use a JavaScript variable in a query statement, you must use `$<variable>`. This parameter is substituted in the query by the corresponding JavaScript variable’s runtime value.

You cannot use the `meta.id` expression in the query statement. Instead, you must use `var id = meta.id`.

The following is a valid statement:

```sqlpp
var id = meta.id;
DELETE FROM mybucket.myscope.transactions WHERE username = $id;
```

The following is an invalid statement:

```sqlpp
DELETE FROM mybucket.myscope.transactions WHERE username = $meta.id;
```

#### [](#escaped-identifiers)Escaped Identifiers

When you use a SQL++ query inside an Eventing Function, you must also use an escaped identifier for keyspaces with special characters. To escape an identifier, enclose it in back ticks (\`\`).

If the bucket name is `beer-sample` and the scope and collection are both `_default`, you only need to escape the bucket in the SQL++ query:

```sqlpp
SELECT * FROM `beer-sample`._default._default WHERE type ...
```

If the bucket name is `beersample`, you do not need to escape the keyspace of the SQL++ query:

```sqlpp
SELECT * FROM beersample._default._default WHERE type ...
```

#### [](#end-of-line-comments)End of Line Comments

In multiline SQL++ statements, you cannot use single line `// end of line comments` before the semicolon at the end of the statement. This causes syntax errors in the transformation and compilation of the SQL++ statement.

To include comments in multiline statements, use `/* this format */` instead.

## [](#unsupported-lang-features)Unsupported Language Features

The following features are not supported by Eventing Functions:

* [Global State](#global-state)
* [Asynchrony](#asynchrony)
* [Browser and Other Extensions](#browser%5Fextensions)
* [Library Imports](#library%5Fimports)

### [](#global-state)Global State

Eventing Functions do not support global variables. This restriction makes sure that the logic of Eventing Functions remains agnostic of rebalance operations.

Instead of using global variables, you must save and retrieve all states from persistence providers like the Data Service. You can use bindings to make all global states contained in Data Service buckets available to Eventing Functions.

```javascript
var count = 0;                         // Not allowed - global variable.
function OnUpdate(doc, meta) {
  count++;
}
```

You can use Constant alias bindings in your Function’s settings to access global constants within a Function’s JavaScript. For example, a Constant alias of `debug` with a value of `true` or `false` behaves in the same way as the statement `const debug = true`.

### [](#asynchrony)Asynchrony

Eventing Functions do not support asynchronous flows.

Asynchrony creates a node-specific, long-running state that prevents persistence providers from capturing the entire state. This limits Eventing Functions to executing short-running, straight-line code without sleep and wake-ups.

You can use Timers to add limited asynchrony back into your Function. Timers are designed specifically to prevent a state from being node-specific.

```javascript
function OnUpdate(doc, meta) {
  setTimeout(function(){}, 300);     // Not allowed - asynchronous flow.
}
```

### [](#browser%5Fextensions)Browser and Other Extensions

Eventing Functions do not support browser extensions, like window methods and DOM events.

You can use Timers instead of `setTimeout` and curl calls instead of `XMLHttpRequests`.

```javascript
function OnUpdate(doc, meta) {
  var rpc = window.XMLHttpRequest();  // Not allowed - browser extension.
}
```

### [](#library%5Fimports)Library Imports

The Eventing Service does not support importing libraries into Eventing Functions.

## [](#build-in-functions)Built-in Functions

Eventing Functions support the following built-in functions:

* [N1QL()](#n1ql%5Fcall)
* [couchbase.​analyticsQuery(⁠)](#analytics%5Fcall)
* [crc64()](#crc64%5Fcall)
* [crc\_64\_go\_iso()](#crc%5F64%5Fgo%5Fiso%5Fcall)
* [base64()](#base64%5Fcall)
* [createTimer() and cancelTimer()](#timers%5Fgeneral)
* [curl()](#curl%5Fcall)

### [](#n1ql%5Fcall)`N1QL()`

You cannot use the `N1QL()` function call directly because it bypasses the semantic and syntactic checks of the transpiler.

> [!NOTE]
> The `N1QL()` function has replaced the deprecated `N1qlQuery()`.

The `N1QL()` function contains the following parameters:

| Parameter             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| statement             | The identified SQL++ statement. This is passed to SQL++ through SDK to run as a prepared statement. All the JavaScript variables referenced in the statement using the $<variable> notation are treated as named parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| params                | Can be a JavaScript array or a JavaScript map object. params is a JavaScript array when the SQL++ statement executes positional parameters. This array corresponds to the values bound to the positional parameters. params is a JavaScript map object when the SQL++ statement executes named parameters. This map object provides the name-value pairs that correspond to the variables used by the SQL++ statement. You cannot mix positional and named parameters. Example of an iterator using a positional params array:     // Using \`travel-sample\`.\_default.\_default to demonstrate params.     // a) Positional param 1 is field 'iata' from the input doc     // b) Positional param 2 from an Eventing Function variable: max\_dist     // c) Will also prepare the statement for better performance     if (doc.type !== "airline") return; // only process airline docs     var max\_dist = 120;     var results = N1QL(         "SELECT COUNT(\*) AS cnt " +         "FROM \`travel-sample\`.\_default.\_default " +         "WHERE type = \\"route\\" " +         "AND airline = $1 AND distance <= $2",         \[doc.iata,max\_dist\],         { 'isPrepared': true }     ); Example of an iterator using a named params map object:     // Using \`travel-sample\`.\_default.\_default to demonstrate named params.     // a) Named param 1 '$mytype' is a hardcode     // b) Named param 2 '$myairline' is field 'iata' from the input doc     // c) Named param 3 '$mydistance' if from an Eventing Function variable max\_dist     // d) Set the consistency in the options to none     if (doc.type !== "airline") return; // only process airline docs     var max\_dist = 120;     var results = N1QL("SELECT COUNT(\*) AS cnt " +         "FROM \`travel-sample\`.\_default.\_default " +         "WHERE type = $mytype " +         "AND airline = $myairline AND distance <= $mydistance",         { '$mytype': 'route', '$mydistance': max\_dist, '$myairline': doc.iata },         { 'consistency': 'none' }     ); |
| options               | A JSON object that has various query runtime options as keys. The following settings are available: isPrepared determines if the statement is prepared. This setting defaults to false, but you can change it to true to increase the performance of any SQL++ query. consistency determines the consistency level for the statement. This setting defaults to the consistency level specified in your Eventing Function settings, but you can change it on any individual statement. Valid values are none and request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| return value (handle) | Returns a JavaScript iterable object that represents the result set of the query. You can iterate the returned handle using standard JavaScript mechanisms like for…​of loops. You can use the close() method on the handle object to release the resources held by the SQL++ query. This method also cancels queries that are in the process of streaming results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Exceptions thrown     | The N1QL() function throws an exception if the underlying SQL++ query fails to parse or does not start to execute. The returned iterable handle throws an exception if the underlying SQL++ query fails after it has started. The close() method on the iterable handle can throw an exception if the underlying SQL++ query cancellation finds an unexpected error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### [](#analytics%5Fcall)`couchbase.​analyticsQuery(⁠)`

Couchbase Server 7.6

The `couchbase.analyticsQuery()` function provides integration with SQL++ Analytics directly from the Eventing Service.

Integrating Eventing with Analytics:

* Allows Eventing to benefit from the high availability and load balancing of Analytics, where requests can take turns being submitted across nodes
* Simplifies Eventing code logic and improves code readability
* Eliminates security and network latency issues with the `curl()` function

The following example assumes that the Analytics collection (dataset) called `default` already exists.

```javascript
function OnUpdate(doc, meta) {
    var count = 0;
    const limit = 4;

    let query = couchbase.analyticsQuery('SELECT * FROM default LIMIT $limit;', {
        "limit": limit
    });
    for (let row of query) {
        ++count;
    }

    if (count === limit) {
        dst_bucket[meta.id] = 'yes';
    }
}
```

For more information about SQL++ Analytics, see [SQL++ for Analytics Reference](../../server/current/analytics/1%5Fintro.md).

### [](#crc64%5Fcall)`crc64()`

The `crc64()` function:

* Calculates the CRC64 hash of an object using the ISO polynomial
* Suppresses double mutations

The `crc64()` function takes the object to checksum as its only parameter. The parameter can be any JavaScript object that can be encoded to JSON.

The function returns the hash as a string. The hash is sensitive to the order of the parameters in the case of map objects.

If multiple Eventing Functions share the same `crc64` checksum documents as the Sync Gateway, real mutations can be suppressed and missed. To prevent this from happening, you can make the checksum documents unique to each Eventing Function.

```javascript
function OnUpdate(doc, meta) {
    var crc_str = crc64(doc);
    /// Code goes here
}
```

You can also use the `crc64` function to suppress a double mutation. A double mutation can happen when the Sync Gateway and the Eventing Function leverage the same bucket.

The Sync Gateway updates the metadata of the document inside the bucket and generates an event for the Eventing Function to process. The Eventing Function cannot differentiate between events from the Sync Gateway and events from SDKs, SQL++, and other sources.

```javascript
function OnUpdate(doc, meta) {
    // Ignore documents created by Sync Gateway
    if(meta.id.startsWith("_sync") == true) return;

    // Ignore documents whose body has not changed since we last saw it
    var prev_crc = checksum_bucket[meta.id];
    var curr_crc = crc64(doc);
    if (prev_crc === curr_crc) return;
    checksum_bucket[meta.id] = curr_crc;

   // Business logic goes in here
}
```

> [!NOTE]
> Translating strings
> 
> Bear in mind that using `crc64()` to convert strings will include any quotation marks as part of the conversion. If you want to translate the string without including the enclosing quotes, then use the [crc\_64\_go\_iso()](#crc%5F64%5Fgo%5Fiso%5Fcall) instead.
> 
> This does not apply to any other data type (e.g., numeric data or JSON data types).

### [](#crc%5F64%5Fgo%5Fiso%5Fcall)`crc_64_go_iso()`

Couchbase Server 7.6

`crc_64_go_iso()` performs the same function as [crc64()](#crc64%5Fcall), but does not include the enclosing quotation marks from the parameter in the translation if its parameter type is `string`.

Other datatypes work the same as the `crc64()` call.

```javascript
function OnUpdate(doc, meta) {
    var crc_iso_str = couchbase.crc_64_go_iso(doc);
    /// Code goes here
}
```

### [](#base64%5Fcall)`base64()`

Couchbase Server 7.6

The `base64()` functions let you pack large-dimensional arrays of floats as base64 encoded strings when you use the Eventing Service to generate vector embeddings. This encoding process stores and transmits arrays as text, ensuring data integrity and compatibility with text-based systems.

The following `base64()` functions are available:

* `base64Encode()`, which takes a JSON argument and returns a base64 string.  
```javascript  
function OnUpdate(doc, meta) {  
    var base_str = couchbase.base64Encode(doc);  
    /// Code goes here  
}  
```
* `base64Decode()`, which takes a base64 encoded string and returns a value string.  
```javascript  
function OnUpdate(doc, meta) {  
    var base_str = couchbase.base64Decode(doc);  
    /// Code goes here  
}  
```
* `couchbase.base64Float32ArrayEncode()`, which takes a float32 number array and returns a base64 string.
* `couchbase.base64Float32ArrayDecode()`, which takes a base64 encoded string and returns a float32 number array.
* `couchbase.base64Float64ArrayEncode()`, which takes a float64 number array and returns a base64 string.
* `couchbase.base64Float64ArrayDecode()`, which takes a base64 encoded string and returns a float64 number array.

### [](#timers%5Fgeneral)`createTimer()` and `cancelTimer()`

Timers are asynchronously computed. They allow Eventing Functions to execute in reference to wall-clock events.

To create a Timer, call the `createTimer()` function using `createTimer(callback, date, reference, context)`. This function executes at or close to a specified date.

The reference is an identifier for the Timer that is scoped to an Eventing Function and callback. The context must be serializable data that is available to the callback when the Timer is fired.

To cancel a Timer, you can do one of the following:

* Call the `createTimer()` function again using a reference from the existing Timer you want to cancel.
* Call the `cancelTimer()` function using `cancelTimer(callback, reference)`.

For more information about Timers, see [Timers](eventing-timers.md).

### [](#curl%5Fcall)`curl()`

The `curl()` function lets you interact with external entities through a REST endpoint from Eventing Functions, using either HTTP or HTTPS.

For more information about the `curl()` function, see [cURL](eventing-curl-spec.md).

## [](#handler-signatures)Handler Signatures

The Eventing Service calls the following JavaScript functions on events like mutations and fired Timers:

* [OnUpdate Handler](#onupdate%5Fhandler)
* [OnDelete Handler](#ondelete%5Fhandler)
* [OnDeploy Handler](#ondeploy%5Fhandler)
* [Timer Callback Handler](#timer%5Fcallback%5Fhandler)

### [](#onupdate%5Fhandler)OnUpdate Handler

The `OnUpdate` handler is called when you create or modify a document. The entry point `OnUpdate(doc, meta)` listens to mutations in the associated source bucket.

The `OnUpdate` handler has the following limitations:

* If a document is modified several times in a short period of time, the handler calls can merge into a single event due to deduplication.
* You cannot distinguish between a Create and an Update operation.

```javascript
function OnUpdate(doc, meta) {
  if (doc.type === 'order' && doc.value > 5000) {
    // ‘phoneverify’ is a bucket alias or binding to a keyspace
    phoneverify[meta.id] = doc.customer;
  }
}
```

### [](#ondelete%5Fhandler)OnDelete Handler

The `OnDelete` handler is called when a document is deleted or removed due to expiration. The entry point `OnDelete(meta, options)` listens to mutations like deletions and expirations in the associated source bucket.

To make sure that a document has been deleted or has expired, you can inspect the optional argument `options`. The `options` argument is a JavaScript map object that contains the boolean property `expired`.

You cannot get the value of a deleted or expired document.

```javascript
function OnDelete(meta,options) {
    if (options.expired) {
        log("Document expired", meta.id);
    } else {
        log("Document deleted", meta.id);
    }
    var addr = meta.id;
    var res = SELECT id from mybucket.myscope.orders WHERE shipaddr = $addr;
    for (var id of res) {
        log("Address invalidated for pending order: " + id);
    }
}
```

In versions of Couchbase Server before version 6.6.0, the optional argument `options` is not present and the entry point for the handler is `OnDelete(meta)`. The entry point is still supported, but using it means you’re unable to differentiate deletion from expiration.

```javascript
function OnDelete(meta) {
    log("Document deleted or expired", meta.id);
}
```

### [](#ondeploy%5Fhandler)OnDeploy Handler

Couchbase Server 8.0

The `OnDeploy` handler is invoked once when an Eventing function is deployed or resumed, before any mutations are processed. The entry point `OnDeploy(action)` is used for one-time setup tasks like resource initialization, creation of timers, and so on.

The `OnDeploy` handler has a limitation. Avoid any long-running operations within the `OnDeploy` as they can delay function deployment.

The timeout for OnDeploy execution is configurable separately in the [Eventing Function Settings](eventing-Terminologies.md#function-settings).

function OnDeploy(action) {
    log("OnDeploy triggered. Reason:", action.reason, "Delay (ms):", action.delay);

    if (action.reason === "deploy") {
        // Perform operations for fresh deployment (like timer creation, resource initialisation)
        log("Deploy: perform first time setup for function");
    }
    else if (action.reason === "resume") {
        // Function was paused and resumed: refresh any cached information
        log("Resume: perform operations before function resumption");
    }
}

### [](#timer%5Fcallback%5Fhandler)Timer Callback Handler

Timer callbacks are user-defined JavaScript functions passed as the callback argument in the built-in `createTimer(callback, date, reference, context)` function call.

The Timer callback handler is an entry point for the event when a timer, created by the specific Eventing Function, matures and fires.

```javascript
// Timer Callback Handler (user-defined entry point)
function DocTimerCallback(context) {
	log("Timer fired running callback 'DocTimerCallback' with context: " + context);
}

// Insert/Update Handler or entry point
function OnUpdate(doc, meta) {
	// filter out docs of no interest
	if (meta.id != 'make_timer:1') return;
	// Create a Date value 60 seconds from now
	var oneMinuteFromNow = new Date(); // Get current time & add 60 sec. to it
	oneMinuteFromNow.setSeconds(oneMinuteFromNow.getSeconds() + 60);
	// Create a doc to hold context to pass state to the callback function
	var context = { docId: meta.id, random_text: "arbitrary text" };
	// Create a timer that will fire an event in the future
	log("createTimer with callback 'DocTimerCallback'");
	createTimer(DocTimerCallback, oneMinuteFromNow, meta.id, context);
}
```

For more information about Timers, see [Timers](eventing-timers.md).

## [](#reserved-words)Reserved Words

You cannot use reserved words as variable names, function names, or JavaScript code properties in Eventing Functions. If you use a reserved word, the Eventing Function returns a deployment error.

The following reserved words are used by the transpiler to integrate SQL++ with Eventing:

| SQL++ Reserved Words |        |        |        |        |         |
| -------------------- | ------ | ------ | ------ | ------ | ------- |
| ALTER                | BUILD  | CREATE | DELETE | DROP   | EXECUTE |
| EXPLAIN              | GRANT  | INFER  | INSERT | MERGE  | PREPARE |
| RENAME               | REVOKE | SELECT | UPDATE | UPSERT |         |