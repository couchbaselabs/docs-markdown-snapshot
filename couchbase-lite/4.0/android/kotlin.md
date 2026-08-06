---
title: Kotlin
description: Couchbase Lite for Android -- Kotlin support
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/android/pages/kotlin.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.0@couchbase-lite:android:kotlin.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/4.0/android/kotlin.html)

# Kotlin

> Description — _Couchbase Lite for Android — Kotlin support_  
> Related Content — [Databases](database.md) | [Documents](document.md) | [Indexing](indexing.md) |

## [](#introduction)Introduction

_Couchbase Lite_ _Android 4.0.3_ introduces full idiomatic support for Kotlin apps, out-of-the-box.

Kotlin developers can now build apps using [common Kotlin Patterns](https://developer.android.com/kotlin/common-patterns), that integrate seamlessly with Couchbase Lite for Android and have full feature parity with the Java API; including some convenient Kotlin Extensions to get you started.

Key features include:

* Nullability annotations
* Named parameters
* Kotlin Flows, for asynchronous event notifications

Java support and functionality continues for Android.

## [](#kotlin-extensions)Kotlin Extensions

In addition to having full co-compatible access to the existing Java API, Kotlin developers can also access a number of Kotlin Extensions.

The [Kotlin Extensions](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android-ktx)package includes:

* [Configuration Factories](#lbl-factories) for the configuration of important Couchbase Lite objects such as _Databases_, _Replicators_ and _Listeners_.
* Change Flows that monitor key Couchbase Lite objects fpr change using Kotlin features such as, Co-routines and [Flows](https://developer.android.com/kotlin/flow).

See: [Kotlin Extensions](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android-ktx) for extension API docs

## [](#lbl-factories)Configuration Factories

Couchbase Lite provides a set of [ConfigurationFactories](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android-ktx/com/couchbase/lite/ConfigurationFactoriesKt.html) and [CommonConfigurationFactories](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android-ktx/com/couchbase/lite/CommonConfigurationFactoriesKt.html), these allow use of named parameters to specify property settings.

This makes it simple to create variant configurations, by simply overriding named parameters:

Example of overriding configuration

```kotlin
val listener8080 = URLEndpointListenerConfigurationFactory.newConfig(
    networkInterface = "en0",
    port = 8080
)
val listener8081 = listener8080.newConfig(port = 8081)
```

### [](#database)Database

Use [DatabaseConfigurationFactory](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android-ktx/com/couchbase/lite/ConfigurationFactoriesKt.html#DatabaseConfigurationFactory)to create a `DatabaseConfiguration` object, overriding the receiver's values with the passed parameters.

* In Use
* Definition

```kotlin
database = Database("getting-started")
```

```kotlin
val DatabaseConfigurationFactory: DatabaseConfiguration? = null

fun DatabaseConfiguration?.newConfig(
    databasePath: String? = null,
    encryptionKey: EncryptionKey? = null,
    fullSync: Boolean? = null,
)
```

### [](#replication)Replication

Use [ReplicatorConfigurationFactory](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android-ktx/com/couchbase/lite/ConfigurationFactoriesKt.html#ReplicatorConfigurationFactory)to create a `ReplicatorConfiguration` object, overriding the receiver's values with the passed parameters.

* In Use
* Definition

```kotlin
val replicator =
    Replicator(
        ReplicatorConfigurationFactory.newConfig(
            collections = CollectionConfiguration.fromCollections(db.collections),
            target = URLEndpoint(URI("ws://localhost:4984/getting-started-db")),
            type = ReplicatorType.PUSH_AND_PULL,
            authenticator = BasicAuthenticator("sync-gateway", "password".toCharArray())
        )
    )
```

```kotlin
val ReplicatorConfigurationFactory: ReplicatorConfiguration? = null

fun ReplicatorConfiguration.newConfig(
    collections: Set<CollectionConfiguration>,
    target: Endpoint,
    type: ReplicatorType? = null,
    continuous: Boolean? = null,
    authenticator: Authenticator? = null,
    headers: Map<String, String>? = null,
    pinnedServerCertificate: X509Certificate? = null,
    maxAttempts: Int? = null,
    maxAttemptWaitTime: Int? = null,
    heartbeat: Int? = null,
    enableAutoPurge: Boolean? = null,
    acceptOnlySelfSignedServerCertificate: Boolean? = null,
    acceptParentDomainCookies: Boolean? = null
)

val MessageEndpointListenerConfigurationFactory: MessageEndpointListenerConfiguration? = null

fun MessageEndpointListenerConfiguration?.create(
    database: Database? = null,
    protocolType: ProtocolType? = null
)
```

### [](#full-text-search)Full Text Search

Use [FullTextIndexConfigurationFactory](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android-ktx/com/couchbase/lite/CommonConfigurationFactoriesKt.html#FullTextIndexConfigurationFactory)to create a `FullTextIndexConfiguration` object, overriding the receiver's values with the passed parameters.

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

Use [ValueIndexConfigurationFactory](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android-ktx/com/couchbase/lite/CommonConfigurationFactoriesKt.html#ValueIndexConfigurationFactory)to create a `ValueIndexConfiguration` object, overriding the receiver's values with the passed parameters.

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

Use [FileLogSinkFactory](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android-ktx/com/couchbase/lite/CommonConfigurationFactoriesKt.html#FileLogSinkFactory)to create a `FileLogSink` object, overriding the receiver's values with the passed parameters.

* In Use
* Definition

```kotlin
FileLogSinkFactory.install(
    directory = context.cacheDir.absolutePath, (1)
    level = LogLevel.INFO, (2)
    maxFileSize = 10240L, (3)
    maxKeptFiles = 5, (4)
    isPlainText = false (5)
)
```

```Kotlin
val FileLogSinkFactory: FileLogSink? = null

fun FileLogSinkFactory?.install(
    directory: String? = null,
    level: LogLevel? = null,
    maxFileSize: Long? = null,
    maxKeptFiles: Int? = null,
    isPlainText: Boolean? = null
)
```

## [](#flows)Flows

These wrappers use _Flowables_ to monitor for changes.

### [](#replicator-change-flow)Replicator Change Flow

Use [replicatorChangeFlow(Replicator,Executor)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android-ktx/com/couchbase/lite/CommonFlowsKt.html#replicatorChangeFlow%28Replicator,Executor%29)to monitor replicator changes.

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

Use [documentReplicationFlow(Replicator,Executor)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android-ktx/com/couchbase/lite/CommonFlowsKt.html#documentReplicationFlow%28Replicator,Executor%29)to monitor document changes during replication.

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

Use [queryChangeFlow(Query,Executor)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android-ktx/com/couchbase/lite/CommonFlowsKt.html#queryChangeFlow%28Query,Executor%29)to monitor document changes during replication.

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