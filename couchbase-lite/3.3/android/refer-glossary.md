---
title: Glossary
description: Couchbase Lite Glossary of Terms
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/android/pages/refer-glossary.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.3@couchbase-lite:android:refer-glossary.adoc[]
---

[View original HTML](/couchbase-lite/3.3/android/refer-glossary.html)

# Glossary

## [](#index)Index

[A](#a) | B | [C](#c) | [D](#d) | E | F | G | H | [I](#i) | J | K | [L](#l) | M | [N](#n) | O | [P](#p) | Q | [R](#r) | [S](#s) | [T](#t) | U | V | W | X | Y | Z

## [](#a)A

Active Peer

The term _active peer_, refers to the initiating peer in any peer-to-peer sync. The active peer initiates the communications. It is the peer that initializes and manages the connection and replication of database changes.

* _Synonym(s)_:
* _Couchbase Lite Component_: peer-to-peer sync
* _Related Term(s)_: [\[passive-peer\]](#passive-peer) [\[peer-to-peer-sync\]](#peer-to-peer-sync)
* _Read More_: [Peer-to-Peer Sync](#android:landing-p2psync.adoc)

## [](#c)C

Checkpoint

A _Checkpoint_, in _Couchbase Mobile_ terms, is a “save state” on a replicator, used to enable a restart at the last success-point in the event of a failure during a replication.

The checkpoint itself is a (meta)document that describes how far in the replication process a given replicator has progressed.

Note that two checkpoints are saved for every replication; one local and one remote.

The checkpoint documents are compared at the beginning of every replication. If they do not agree, then it indicates a severe error during the last run, and the replication is forced to restart from the beginning.

Back to [Index](#index)

## [](#d)D

Delta Sync

Delta Sync is the ability to replicate only parts of the Couchbase document that have changed.

This can result in significant savings in bandwidth consumption as well as throughput improvements, especially when network bandwidth is typically constrained.

* _Related Term(s)_: [Passive replicator](#passive-replicator)
* _Read More_: [Delta Sync](replication.md#delta-sync)

## [](#i)I

Back to [Index](#index)

## [](#l)L

Back to [Index](#index)

## [](#n)N

Back to [Index](#index)

## [](#p)P

Passive Peer

The term _Passive peer_, refers to the non-initiating peer in any peer-to-peer sync. The passive peer reacts to communications it receives but does not initiate any communication on its own.

* _Synonym(s)_:
* _Couchbase Lite Component_: peer-to-peer sync
* _Related Term(s)_: [\[active-peer\]](#active-peer), [\[peer-to-peer-sync\]](#peer-to-peer-sync)
* _Read More_: [Peer-to-Peer Sync](#android:landing-p2psync.adoc)

Peer-to-Peer Sync

The term _peer-to-peer sync_, in the Couchbase Mobile context refers to the synchronization of database changes between Couchbase Lite enabled clients without an intermediary server. Couchbase Lite provides out-of-the-box peer-to-peer sync, over websockets, between Couchbase Lite enabled clients in IP-based networks.

* _Synonym(s)_: p2p sync
* _Couchbase Lite Component_: Inter-cluster replication
* _Related Term(s)_: [\[active-peer\]](#active-peer) [\[passive-peer\]](#passive-peer)
* _Read More_: [Peer-to-Peer Sync](#android:landing-p2psync.adoc)

Back to [Index](#index)

## [](#r)R

Back to [Index](#index)

## [](#s)S

## [](#t)T

TLSIdentity

TLSIdentity represents the identity information (Key pair and Certificates) used for setting up TLS Communication.

The TLSIdentity API differs from platform-to-platform.

* _Synonym(s)_: n/a
* _Topic Group_: _Using Peer-to-Peer Synchronization (web sockets_
* _Related Term(s)_: [\[active-peer\]](#active-peer) [\[passive-peer\]](#passive-peer)
* _Read More_: [Peer-to-Peer](p2psync-websocket.md)

Back to [Index](#index)