---
title: Kotlin
description: Couchbase Lite for Android -- Kotlin support
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/android/pages/kotlin.adoc
  xref: xref:3.3@couchbase-lite:android:kotlin.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.3/android/kotlin.html)

# Kotlin

> Description — _Couchbase Lite for Android — Kotlin support_  
> Related Content — [Databases](database.md) | [Documents](document.md) | [Indexing](indexing.md) |

## [](#introduction)Introduction

_Couchbase Lite_ _Android 3.3.0_ introduces full idiomatic support for Kotlin apps, out-of-the-box.

Kotlin developers can now build apps using [common Kotlin Patterns](https://developer.android.com/kotlin/common-patterns), that integrate seamlessly with Couchbase Lite for Android and have full feature parity with the Java API; including some convenient Kotlin Extensions to get you started.

Key features include:

* Nullability annotations
* Named parameters
* Kotlin Flows, for asynchronous event notifications

Java support and functionality continues for Android.

## [](#kotlin-extensions)Kotlin Extensions

In addition to having full co-compatible access to the existing Java API, Kotlin developers can also access a number of Kotlin Extensions.

The [Kotlin Extensions](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx)package includes:

* [Configuration Factories](#lbl-factories) for the configuration of important Couchbase Lite objects such as _Databases_, _Replicators_ and _Listeners_.
* Change Flows that monitor key Couchbase Lite objects fpr change using Kotlin features such as, Co-routines and [Flows](https://developer.android.com/kotlin/flow).

See: [Kotlin Extensions](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx) for extension API docs

## [](#lbl-factories)Configuration Factories

Couchbase Lite provides a set of [ConfigurationFactories](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx/com/couchbase/lite/ConfigurationFactoriesKt.html) and [CommonConfigurationFactories](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx/com/couchbase/lite/CommonConfigurationFactoriesKt.html), these allow use of named parameters to specify property settings.

This makes it simple to create variant configurations, by simply overriding named parameters:

Example of overriding configuration

```kotlin
//include::example$kotlin_snippets/app/src/main/kotlin/com/couchbase/codesnippets/ListenerExamples.kt[tag=override-config]
        val listener8080 = URLEndpointListenerConfigurationFactory.newConfig(
            networkInterface = "en0",
            port = 8080
        )
        val listener8081 = listener8080.newConfig(port = 8081)
```

### [](#database)Database

Use [DatabaseConfigurationFactory](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx/com/couchbase/lite/ConfigurationFactoriesKt.html#DatabaseConfigurationFactory)to create a `DatabaseConfiguration` object, overriding the receiver's values with the passed parameters.

* In Use
* Definition

```kotlin
database = Database("getting-started")
```

```kotlin
val DatabaseConfigurationFactory: DatabaseConfiguration? = null

fun DatabaseConfiguration?.create(
    databasePath: String? = null,
    encryptionKey: EncryptionKey? = null
)
```

### [](#replication)Replication

Use [ReplicatorConfigurationFactory](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx/com/couchbase/lite/ConfigurationFactoriesKt.html#ReplicatorConfigurationFactory)to create a `ReplicatorConfiguration` object, overriding the receiver's values with the passed parameters.

* In Use
* Definition

```kotlin
val replicator =
    Replicator(
        ReplicatorConfigurationFactory.newConfig(
            collections = mapOf(db.collections to null),
            target = URLEndpoint(URI("ws://localhost:4984/getting-started-db")),
            type = ReplicatorType.PUSH_AND_PULL,
            authenticator = BasicAuthenticator("sync-gateway", "password".toCharArray())
        )
    )
```

```kotlin
val ReplicatorConfigurationFactory: ReplicatorConfiguration? = null

fun ReplicatorConfiguration?.create(
    database: Database? = null,
    target: Endpoint? = null,
    type: ReplicatorType? = null,
    continuous: Boolean? = null,
    authenticator: Authenticator? = null,
    headers: Map<String, String>? = null,
    pinnedServerCertificate: ByteArray? = null,
    channels: List<String>? = null,
    documentIDs: List<String>? = null,
    pushFilter: ReplicationFilter? = null,
    pullFilter: ReplicationFilter? = null,
    conflictResolver: ConflictResolver? = null,
    maxAttempts: Int? = null,
    maxAttemptWaitTime: Int? = null,
    heartbeat: Int? = null,
    enableAutoPurge: Boolean? = null,
    acceptOnlySelfSignedServerCertificate: Boolean? = null
)

val MessageEndpointListenerConfigurationFactory: MessageEndpointListenerConfiguration? = null

fun MessageEndpointListenerConfiguration?.create(
    database: Database? = null,
    protocolType: ProtocolType? = null
)
```

### [](#full-text-search)Full Text Search

Use [FullTextIndexConfigurationFactory](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx/com/couchbase/lite/CommonConfigurationFactoriesKt.html#FullTextIndexConfigurationFactory)to create a `FullTextIndexConfiguration` object, overriding the receiver's values with the passed parameters.

* In Use
* Definition

```kotlin
collection.createIndex(
    "overviewFTSIndex",
    FullTextIndexConfigurationFactory.newConfig("overview")
)
```

```Kotlin
val FullTextIndexConfigurationFactory: FullTextIndexConfiguration? = null

fun FullTextIndexConfiguration?.create(expression: String? = null)
```

### [](#indexing)Indexing

Use [ValueIndexConfigurationFactory](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx/com/couchbase/lite/CommonConfigurationFactoriesKt.html#ValueIndexConfigurationFactory)to create a `ValueIndexConfiguration` object, overriding the receiver's values with the passed parameters.

* In Use
* Definition

```kotlin
collection.createIndex(
    "TypeNameIndex",
    ValueIndexConfigurationFactory.newConfig("type", "name")
)
```

```Kotlin
val ValueIndexConfigurationFactory: ValueIndexConfiguration? = null

fun ValueIndexConfiguration?.create(vararg expressions: String = emptyArray())
```

### [](#logs)Logs

Use [LogFileConfigurationFactory](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx/com/couchbase/lite/CommonConfigurationFactoriesKt.html#LogFileConfigurationFactory)to create a `LogFileConfiguration` object, overriding the receiver's values with the passed parameters.

* In Use
* Definition

```kotlin
        Database.log.file.let {
            it.config = LogFileConfigurationFactory.newConfig(
                context.cacheDir.absolutePath, (1)
                maxSize = 10240, (2)
                maxRotateCount = 5, (3)
                usePlainText = false
            ) (4)
            it.level = LogLevel.INFO (5)

        }
```

```Kotlin
val LogFileConfigurationFactory: LogFileConfiguration? = null

.LogFileConfiguration.create()

fun LogFileConfiguration?.create(
    directory: String? = null,
    maxSize: Long? = null,
    maxRotateCount: Int? = null,
    usePlainText: Boolean? = null
)
```

## [](#flows)Flows

These wrappers use _Flowables_ to monitor for changes.

### [](#database-change-flow)Database Change Flow

Use the [databaseChangeFlow(Database,Executor)](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx/com/couchbase/lite/CommonFlowsKt.html#databaseChangeFlow%28Database,Executor%29)to monitor database change events.

* In Use
* Definition

```kotlin
val updatedDocs = db.databaseChangeFlow()
    .map { it.documentIDs }
    .asLiveData()
```

```kotlin
@ExperimentalCoroutinesApi
fun Database.databaseChangeFlow(executor: Executor? = null)
```

### [](#document-change-flow)Document Change Flow

Use [documentChangeFlow(Database,String,Executor)](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx/com/couchbase/lite/CommonFlowsKt.html#documentChangeFlow%28Database,String,Executor%29)to monitor changes to a document.

* In Use
* Definition

```kotlin
val docModDate = db.documentChangeFlow("1001", null)
    .map { it.collection.getDocument(it.documentID)?.getString("lastModified") }
    .asLiveData()
```

```kotlin
@ExperimentalCoroutinesApi

fun Database.documentChangeFlow(documentId: String, executor: Executor? = null)
```

### [](#replicator-change-flow)Replicator Change Flow

Use [replicatorChangeFlow(Replicator,Executor)](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx/com/couchbase/lite/CommonFlowsKt.html#replicatorChangeFlow%28Replicator,Executor%29)to monitor replicator changes.

* In Use
* Definition

```kotlin
val replState = repl.replicatorChangesFlow()
    .map { it.status.activityLevel }
    .asLiveData()
```

```kotlin
@ExperimentalCoroutinesApi
fun Replicator.replicatorChangesFlow(executor: Executor? = null)
```

### [](#document-replicator-change-flow)Document Replicator Change Flow

Use [documentReplicationFlow(Replicator,Executor)](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx/com/couchbase/lite/CommonFlowsKt.html#documentReplicationFlow%28Replicator,Executor%29)to monitor document changes during replication.

* In Use
* Definition

```kotlin
val replicatedDocs = repl.documentReplicationFlow(testSerialExecutor)
    .map { update -> update.documents }
    .onEach { listView.setUpdated(it) }
    .collect()
```

```kotlin
@ExperimentalCoroutinesApi
fun Replicator.documentReplicationFlow(executor: Executor? = null)
```

### [](#query-change-flow)Query Change Flow

Use [queryChangeFlow(Query,Executor)](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android-ktx/com/couchbase/lite/CommonFlowsKt.html#queryChangeFlow%28Query,Executor%29)to monitor document changes during replication.

* In Use
* Definition

```kotlin
fun watchQuery(query: Query): LiveData<List<Result>> {
    return query.queryChangeFlow()
        .mapNotNull { change ->
            val err = change.error
            if (err != null) {
                throw err
            }
            change.results?.allResults()
        }
        .asLiveData()
}
```

```kotlin
@ExperimentalCoroutinesApi
fun Query.queryChangeFlow(executor: Executor? = null)
```

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
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