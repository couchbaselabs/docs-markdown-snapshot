---
title: Couchbase Server Processes
description: Couchbase Server spawns a number of different processes on each node.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/install/pages/server-processes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:install:server-processes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/install/server-processes.html)

# Couchbase Server Processes

> Couchbase Server spawns a number of different processes on each node. These processes vary in type and number depending on which Couchbase services are running on a particular node. 

Couchbase Server spawns processes from a set of binaries that get installed by the Couchbase installer. Some of these processes support the basic functions of Couchbase Server, and run on every node in the Couchbase cluster (Data). Other processes, however, support the various Couchbase services, and only run on the nodes that happen to run a particular Couchbase service (Data, Query, Index, Search, Analytics, and Eventing).

The tables on this page list out all of the Couchbase processes, along with the specific Couchbase services that will invoke them. If a particular Couchbase service is not running on a node, then the processes associated with that service will not run.

It's important that each of these processes is allowed to run and access files on the nodes that are enabled for the Couchbase services that they support. Otherwise, Couchbase Server will not function properly. Depending on your security environment, you may need to explicitly approve these processes and their binary directories in your security policy.

## [](#linux)Linux

The following table lists the Couchbase processes that run on Linux platforms.

__Table 1\. Couchbase Processes on Linux__
| Process                      | Description                                                                                                                                 | Service   | Path                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------- |
| cbft                         | Couchbase Full-Text Search (FTS) service                                                                                                    | Search    | _/opt/couchbase/bin/_                                       |
| cbq-engine                   | Couchbase Query service                                                                                                                     | Query     | _/opt/couchbase/bin/_                                       |
| goport (5 copies)            | Process that acts as a bridge between ns\_server (Erlang) and the other server components (cbq- engine, cbft, etc.) which are written in Go | Query     | _/opt/couchbase/bin/_                                       |
| gosecrets                    | Service that is used to encrypt the cluster configuration stored on disk                                                                    | Data      | _/opt/couchbase/bin/_                                       |
| goxdcr                       | Cross Data Center Replication (XDCR) - replicates data from one cluster to another                                                          | Data      | _/opt/couchbase/bin/_                                       |
| indexer                      | Index service                                                                                                                               | Index     | _/opt/couchbase/bin/_                                       |
| memcached                    | Data service responsible for storing user data                                                                                              | Data      | _/opt/couchbase/bin/_                                       |
| godu (2 copies)              | Utility in Go to get disk usage stats                                                                                                       | Data      | _/opt/couchbase/bin/priv/_                                  |
| projector                    | Extracts secondary key from documents                                                                                                       | Data      | _/opt/couchbase/bin/_                                       |
| saslauthd-port               | Erlang port process (wrapper) used to talk to the saslauthd daemon for authentication purposes                                              | Data      | _/opt/couchbase/bin/_                                       |
| beam.smp (3 copies)          | Couchbase cluster manager run as Erlang virtual machines - babysitter, ns\_server, and ns\_couchdb                                          | Data      | _/opt/couchbase/lib/erlang/erts-9.3.3.9/bin/_               |
| epmd                         | Erlang-specific process which acts as a name server for Erlang distribution                                                                 | Data      | _/opt/couchbase/bin/_                                       |
| cpu\_sup (2 copies)          | Erlang-specific process used to collect CPU: 1 for ns\_server VM and 1 for ns\_couchdb VM                                                   | Data      | _/opt/couchbase/lib/erlang/lib/os\_mon-2.2.14/priv/bin/_    |
| memsup (2 copies)            | Erlang-specific process used to collect memory usage: 1 for ns\_server VM and 1 for ns\_couchdb VM                                          | Data      | _/opt/couchbase/lib/erlang/lib/os\_mon-2.2.14/priv/bin/_    |
| inet\_gethost (2 copies)     | Built-in Erlang port process that is used to perform name service lookup                                                                    | Data      | _/opt/couchbase/lib/erlang/erts-5.10.4.0.0.1/bin/_          |
| portsigar                    | Open source tool sigar that is used to collect system information                                                                           | Data      | _/opt/couchbase/bin/_                                       |
| sh -s disksup (2 copies)     | Erlang-specific process that is used to supervise the available disk space: 1 for ns\_server VM and 1 for ns\_couchdb VM                    | Data      | _/opt/couchbase/lib/erlang/lib/os\_mon-2.2.14/ebin/_        |
| sh -s ns\_disksup            | Wrapper for disksup which also collects information about mounted drives                                                                    | Data      | _/opt/couchbase/lib/ns\_server/erlang/lib/ns\_server/ebin/_ |
| cbcollect\_info              | Utility used to collect Couchbase server logs (will be seen only during log collection)                                                     | Data      | _/opt/couchbase/bin/_                                       |
| eventing-producer (1 copy)   | Eventing supervisor service (one instance per node)                                                                                         | Eventing  | _/opt/couchbase/bin/_                                       |
| eventing-consumer (n copies) | Eventing worker (multiple instances per node). Instance count is configured in UI.                                                          | Eventing  | _/opt/couchbase/bin/_                                       |
| java (Analytics Driver)      | JVM running the Analytics NC and CC                                                                                                         | Analytics | _/opt/couchbase/lib/cbas/runtime/bin_                       |
| cbas                         | Go-wrapper that communicates with ns\_server and manages the lifecycle of the Analytics Driver                                              | Analytics | _/opt/couchbase/bin/_                                       |

## [](#windows)Windows

The following table lists the Couchbase processes that run on the Windows platforms.

__Table 2\. Couchbase Processes on Windows__
| Process                     | Description                                                                                                                 | Service   | Path                                                      |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------- |
| backup.exe                  | Backup application for Couchbase data                                                                                       | Backup    | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| cbas.exe                    | Go-wrapper that communicates with ns\_server and manages the lifecycle of the Analytics Driver                              | Analytics | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| cbcollect\_info.exe         | Utility used to collect Couchbase server logs (will be seen only during log collection)                                     | Data      | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| cbft.exe                    | Couchbase Full-Text Search (FTS) service                                                                                    | Search    | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| cbq-engine.exe              | Couchbase Query service                                                                                                     | Query     | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| epmd.exe                    | Erlang-specific process which acts as a name server for Erlang distribution                                                 | Data      | _C:\\Program Files\\Couchbase\\Server\\erts-x.x.x.x\\bin_ |
| erl.exe                     | Erlang process used by the name server.                                                                                     | Data      | _C:\\Program Files\\Couchbase\\Server\\erts-x.x.x.x\\bin_ |
| erlsrv.exe                  | Used to start the Erlang emulator as a Windows process.                                                                     | Data      | _C:\\Program Files\\Couchbase\\Server\\erts-x.x.x.x\\bin_ |
| eventing-consumer.exe       | Eventing worker (multiple instances per node). Instance count is configured in UI.                                          | Eventing  | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| eventing-producer.exe       | Eventing supervisor service (one instance per node)                                                                         | Eventing  | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| goport.exe                  | Process that acts as a bridge between ns\_server (Erlang) and the other server components (cbq- engine.exe, cbft.exe, etc.) | Query     | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| gosecrets.exe               | Service that is used to encrypt the cluster configuration stored on disk                                                    | Data      | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| goxdcr.exe                  | Cross Data Center Replication (XDCR) - replicates data from one cluster to another                                          | Data      | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| indexer.exe                 | Index service                                                                                                               | Index     | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| godu.exe                    | Utility in Go to get disk usage stats                                                                                       | Data      | _C:\\Program Files\\Couchbase\\Server\\bin\\priv_         |
| inet\_gethost.exe           | Built-in Erlang port process that is used to perform name service lookup                                                    | Data      | _C:\\Program Files\\Couchbase\\Server\\erts-x.x.x.x\\bin_ |
| java.exe (Analytics Driver) | JVM running the Analytics NC and CC                                                                                         | Analytics | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| memcached.exe               | Data service responsible for storing user data                                                                              | Data      | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| projector.exe               | Extracts secondary key from documents                                                                                       | Data      | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| prometheus.exe              | Engine used Couchbase for creating metrics.                                                                                 | Data      | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| saslauthd-port.exe          | Erlang port process (wrapper) used to talk to the saslauthd daemon for authentication purposes                              | Data      | _C:\\Program Files\\Couchbase\\Server\\bin_               |
| sigar\_port.exe             | Open source tool sigar that is used to collect system information                                                           | Data      | _C:\\Program Files\\Couchbase\\Server\\bin_               |