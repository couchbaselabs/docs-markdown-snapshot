---
title: Glossary
description: Sync Gateway Glossary of Terms
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/ROOT/pages/glossary.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:sync-gateway::glossary.adoc[]
---

[View original HTML](/sync-gateway/current/glossary.html)

# Glossary

> Sync Gateway Glossary of Terms  

## [](#index)Index

[A](#a) | [\[B\]](#B) | [C](#c) | [\[D\]](#D) | [\[E\]](#E) | [\[F\]](#F) | [G](#g) | [\[H\]](#H) | [I](#i) | [\[J\]](#J) | [\[K\]](#K) | [L](#l) | [\[M\]](#M) | [N](#n) | [O](#o) | [P](#p) | [\[Q\]](#Q) | [R](#r) | [S](#s) | [T](#t) | [\[U\]](#U) | [\[V\]](#V) | [\[W\]](#W) | [\[X\]](#X) | [\[Y\]](#Y) | [\[Z\]](#Z)

## [](#a)A

Active replicator

The term _active replicator_, refers to the Sync Gateway endpoint that initiates the replication connection. That is, it s the Sync Gateway where the replicators are configured and from which the changes are pushed.

* _Synonym(s)_: active sync gateway
* _SGW Component_: Replication
* _Related Term(s)_: [Passive replicator](#passive-replicator)
* _Read More_: [Inter Sync Gateway Sync - Overview](sync/sync-inter-syncgateway-overview.md)

Active Sync Gateway node

The term _active Sync Gateway node_, refers to Sync Gateway nodes with incoming writes; these may be from Couchbase Lite clients, the REST API, or through the Couchbase Server.

* _SGW Component_: Replication

Adhoc Replication

The term _adhoc replication_ refers to transient, one-shot, replications that run once and are removed when they stop. They are initialized using the Admin REST API. They do not survive Sync Gateway restarts.

Ad hoc replications are useful when it is necessary to do one off replication or for troubleshooting.

Other useful use cases include:

* Starting a replication on-demand, for instance a replication that needs to be scheduled to be run at midnight every Thursday.  
In this case, it is likely that there is an automation script that schedules the adhoc replication on a predefined schedule.
* Deploying an emergency one-time update that needs to be pushed out to all edge clusters from primary data clusters.

Context:

* _Synonym(s)_: transient replication
* _Related Term(s)_:

  * [Persistent replication](#persistent-replication)
  * [Continuous replication](#continuous-replication)
* _SGW Component_: Inter-Sync Gateway Replication
* _Read More_: [Inter Sync Gateway Sync - Overview](sync/sync-inter-syncgateway-overview.md)
* _Related Config Elements_: [adhoc](configuration/configuration-schema-database.md#database-replications-this%5Frep-adhoc) | [continuous](configuration/configuration-schema-database.md#database-replications-this%5Frep-continuous)

Automatic conflict resolution

The goal of automatic conflict resoluton is to return a winning revision based on the consistent application of the configured [conflict resolver policy![glossary icon](_images/icons/glossaryIconImage2.png)](#conflict-resolver-policies).

The default _conflict resolver policy_ is to always returns a winner determined by the [automatic conflict resolution policy![glossary icon](_images/icons/glossaryIconImage2.png)](#auto-conflict-resolution-policy).

Automatic conflict resolution policy

The automatic conflict resolution policy uses timestamp-based conflict resolution often referred to as `"last write wins"`, which uses a document timestamp from the most recent document revisions to compare and return the revision that was most recently updated.

The default [automatic conflict resolution![glossary icon](_images/icons/glossaryIconImage2.png)](#auto-conflict-resolution) policy always returns a winner determined by the following rules:

* The revision with the most recent timestamp wins.
* If replicating a document that was last updated/written pre-upgrade to SG 4.x, the default policy for versions < 4.x will be used. See [Automatic Conflict Resolution](../3.3/glossary.md#auto-conflict-resolution).

Back to [Index](#index)

## [](#c)C

Checkpoint

A _Checkpoint_, in _Couchbase Mobile_ terms, is a “save state” on a replicator, used to enable a restart at the last success-point in the event of a failure during a replication.

The checkpoint itself is a (meta)document that describes how far in the replication process a given replicator has progressed.

Note that two [checkpoints![glossary icon](_images/icons/glossaryIconImage2.png)](#checkpoint) are saved for every replication; one local and one remote.

The checkpoint documents are compared at the beginning of every replication. If they do not agree, then it indicates a severe error during the last run, and the replication is forced to restart from the beginning.

Conflict Resolver Policies

Inter-Sync Gateway replication provides several predefined conflict resolver policies, which you can choose to apply. These include: `` default; `localWins ``, `remoteWins`; and `custom`.

Each conflict resolver policy applies a different strategy:

Default

* Always applies Sync Gateway’s [Automatic conflict resolution policy](#auto-conflict-resolution-policy)
* Configured using: `"conflict_resolution_type": "default"`

Local Wins

* Always considers the local change the winner.
* Configured using: `"conflict_resolution_type": "localWins"`

Remote Wins

* Always considers the remote change the winner.
* Configured using: `"conflict_resolution_type": "remoteWins"`

Custom

> [!NOTE]
> [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) Only

Applies the policy defined in the function provided by the `custom_conflict_resolver` parameter.

See: [Custom conflict resolver](#custom-conflict-resolver)

Custom conflict resolver

The custom\_conflict\_resolver property specifies a Javascript function used to resolve conflicting changes.

This is an [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) only feature and is configured like this:

"conflict_resolution_type": "custom",
"custom_conflict_resolver":`
  function(conflict) {
    // Always resolve in favor of remote
    console.log("full remoteDoc doc: "+JSON.stringify(conflict.RemoteDocument));
    return conflict.RemoteDocument;
  }`

Configuration property: [custom\_conflict\_resolver](configuration/configuration-schema-database.md#database-replications-this%5Frep-custom%5Fconflict%5Fresolver)

Continuous replication mode

A _continuous_ replication will sit in running state awaiting document changes to process in accordance to its _replication definition_.

Cloud-to-Edge Sync

The term _cloud-to-edge_ refers to the multi-cloud deployment mode commonly know as _ship-to-shore_ or _hub-and-spoke_. These typically involve a large number of edge clusters (mobiles,, tablets IoT) connected to one or more cloud data centers.

Each edge can operate autonomously without network connectivity to the cloud data centers. The _edge_ could be, for example a group of retail stores, ships at sea or distribution hubs. The number of edges can range from a few hundred to several thousand.

* _Synonym(s)_: ship-to-shore sync, hub-and-spoke sync
* _SGW Component_: Inter-Sync Gateway Replication
* _Related Term(s)_:
* _Read More_: [Inter Sync Gateway Sync - Overview](sync/sync-inter-syncgateway-overview.md)

Cloud-to-Edge synchronization

The term _cloud-to-edge synchronization_ refers to scenarios typically involving a hierarchy of couchbase mobile clusters, within which a large number of edge clusters must synchronize data changes with each other and with one or more clusters in cloud data centers.

Each edge can operate autonomously without network connectivity to the cloud data centers. The _edge_ could be, for example a group of retail stores, ships at sea or distribution hubs. The number of edges can range from a few hundred to several thousand.

* _Synonym(s)_: ship-to-shore sync, hub-and-spoke sync
* _SGW Component_: Inter-Syn Gateway Replication
* _Related Term(s)_:
* _Read More_: [Inter Sync Gateway Sync - Overview](sync/sync-inter-syncgateway-overview.md)

Back to [Index](#index)

## [](#g)G

Grafana

Grafana is an open source data visualization and alerting platform. It supports Prometheus as a data source and can be used to build comprehensive dashboards.

Back to [Index](#index)

## [](#i)I

Inter-Sync Gateway Replication

The term _inter-Sync Gateway replication_ refers to replication between two Sync Gateway clusters and-or between active mobile clusters.

From 2.8+ inter-Sync Gateway replication within Sync Gateway is delivered by a completely redesigned and re-engineered websocket-base protocol, which enables a Sync Gateway replicator to act as the _[active replicator![glossary icon](images/icons/glossaryIconImage2.png)](#active-replicator)_, pulling changes from a data source and pushing them to a target. Pre-2.8 inter-Sync Gateway replication used the SG Replicate protocol over https.

Back to [Index](#index)

## [](#l)L

Leaf revision

A Leaf revision is the last Document Revision in a series of changes. Documents may have multiple Leaf Revisions (aka Conflict Revisions) due to concurrent updates.

Back to [Index](#index)

## [](#n)N

No conflicts mode

No conflicts mode is the process by which write operations that would result in a conflict are rejected by the system. It is an optional feature \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] — see: [allow\_conflicts](configuration/configuration-schema-database.md#database-allow%5Fconflicts).

Example 1\. Couchbase Lite Conflict Resolution Links

* [Swift](../../couchbase-lite/current/swift/conflict.md)
* [Java](../../couchbase-lite/current/java/conflict.md)
* [Java (Android)](../../couchbase-lite/current/android/conflict.md)
* [C#](../../couchbase-lite/current/csharp/conflict.md)
* [Objective-C](../../couchbase-lite/current/objc/conflict.md)

No op updates

The term _no-op update_ refers to a change made to the document body that does not impact application logic but does trigger a replication by the Sync Gateway.

For example, you may include an otherwise redundant _counter_ property, that you increment in response to conflict resolver errors.

Back to [Index](#index)

## [](#o)O

One-shot replication mode

A _one-shot_ replication will start, process all existing document changes in accordance to its _replication definition_ and then stop.

Once finished, persistent _one-shot_ replications return to a 'stopped' state, but _adhoc_ _one-shot_ replications are removed.

Back to [Index](#index)

## [](#p)P

Passive replicator

The term _passive replicator_, refers to the Sync Gateway endpoint that receives an incoming replication connection.

Context

* _Synonym(s)_: passive sync gateway
* _Related Term(s)_: [Active replicator](#active-replicator)
* _SGW Component_: Inter-Sync Gateway Replication
* _Read More_: [Inter Sync Gateway Sync - Overview](sync/sync-inter-syncgateway-overview.md)

Persistent Exponential Backoff

The wait time between retry attempts is exponentially increased at each attempt, until it reaches a predetermined maximum limit. Subsequent retries may be made after the maximum limit time period has elapsed.

Persistent Replication

The term _Persistent replication_ refers to replications that survive Sync Gateway restarts. All replications are persisted by default unless explicitly flagged as not. Persistent replication is defined in the configuration file sync-gateway.json — see [Legacy Pre-3.0 Configuration](configuration/configuration-properties-legacy.md). It is started automatically and survives restarts. The recommended method of defining a persistent replication is by using the configuration file. With Inter-Sync Gateway replication you can configure all nodes with the replicators.

* _Synonym(s)_: continuous replication
* _Related Term(s)_:

  * [Transient replication](#transient-replication)
  * [Adhoc replication](#transient-replication)
* _SGW Component_: Inter-Sync Gateway Replication
* _Read More_: [Inter Sync Gateway Sync - Overview](sync/sync-inter-syncgateway-overview.md)

Prometheus

Prometheus is an open source systems monitoring and alerting platform and hosted by Cloud Native Computing Foundation. At the core of it is the Prometheus Server that is responsible for polling “Prometheus targets” for stats and storing it as time series data. Prometheus targets are statically configured or can be discovered by Prometheus.

Back to [Index](#index)

## [](#r)R

Replication definition

The term _Replication definition_ refers to that set of elements (parameters or properties) that define a replication, dictating what will be replicated and how the replication will be conducted.

Replication definitions are provided to Sync Gateway in 'JSON' format through either:

* The Sync Gateway configuration file (`sync-gateway-config.json`)
The Admin REST API’s _replication endpoint, using a utility such as `curl`, or an application such as \_Postman_. 

_Replication definitions_ comprise the same elements in both the JSON configuration file and the Admin REST API; except configured replications cannot use `adhoc` or `cancel`.

Revision pruning

Revision Pruning is the process that deletes the metadata and/or JSON bodies associated with old non-leaf revisions. Leaf revisions are not impacted.

Back to [Index](#index)

## [](#s)S

Synchronization

The term, _Synchronization_, refers to the process of replicating the changes made to documents on one database to the same documents in a second instance of that database.

* Synonyms: _replication_, _sync_
* _Related Term(s)_:

  * [Sync function](#sync-function)
  * [Persistent replication](#persistent-replication)
  * [Adhoc replication](#transient-replication)
* _SGW Component_: Inter-Sync Gateway Replication
* _Read More_: [Inter Sync Gateway Sync - Overview](sync/sync-inter-syncgateway-overview.md)

Sync Function

The Sync Function is a JavaScript function whose source code is provisioned using the Admin Rest API. It is in charge of data validation, and of authorizing both read and write access to documents.

[Sync Function](access-control/sync-function/sync-function.md)

Sync Gateway Database

The term _Sync Gateway database_ refers to what you may consider a namespace for documents. It provides Sync Gateway with access to documents that are stored in Couchbase Server.

## [](#t)T

Tombstone revision

A tombstone revision is essentially a marker indicating that a document has been deleted.

Each Tombstone Revision comprises: document ID, revision ID and a \_deleted flag (value=true). They are created to allow all devices to see that a document has been deleted - particularly in the case of devices that may not be online continuously and therefore not syncing regularly.

Every update — including deletes — creates a document revision. Deleted revisions are also known as _Tombstone_ revisions. They have the '“\_deleted”: true' property, are replicated, but are not returned if you do a query using, for example, Couchbase Lite.

+

```json
{
  "_deleted": true,
  "_id": "foobar",
  "_rev": "3-db962c6d93c3f1720cc7d3b6e50ac9df"
}
```

Mentioned in: \* [Managing Tombstones](manage/managing-tombstones.md)\* [Metadata Purge Interval](sync/sync-with-couchbase-server.md#metadata-purge-interval)\* [$dbname.enable\_shared\_bucket\_access](configuration/configuration-schema-database.md#database-enable%5Fshared%5Fbucket%5Faccess)\* [Server Tombstones](../../server/current/learn/buckets-memory-and-storage/storage-settings.md#tombstones)

Transient Replication

The term _transient replication_ refers to ad hoc replications — see: [Adhoc Replication](#adhoc-replication)

Back to [Index](#index)

---

[1](#%5Ffootnoteref%5F1). Post-2.0