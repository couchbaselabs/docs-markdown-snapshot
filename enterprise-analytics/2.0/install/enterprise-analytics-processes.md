[View original HTML](/enterprise-analytics/2.0/install/enterprise-analytics-processes.html)

> Enterprise Analytics creates a number of different processes on each node. Enterprise Analytics creates processes from a set of binaries that get installed by the product installer. 

The tables on this page list out all of the Enterprise Analytics processes. It’s important that you allow each of these processes to run and access files on the nodes. Otherwise, Enterprise Analytics does not function properly. Depending on your security environment, you may need to explicitly approve these processes and their binary directories in your security policy.

## [](#linux)Linux

The following table lists the Enterprise Analytics processes that run on Linux platforms.

__Table 1\. Enterprise Analytics Processes on Linux__
| Process                  | Description                                                                                                                          | Path                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| goport (2 copies)        | Process that acts as a bridge between ns\_server (Erlang) and the other server components (cbas, prometheus) which are written in Go | /opt/enterprise-analytics/bin/                                       |
| gosecrets                | Service that’s used to encrypt the cluster configuration stored on disk                                                              | /opt/enterprise-analytics/bin/                                       |
| memcached                | Data service providing cluster topology updates to legacy SDKs                                                                       | /opt/enterprise-analytics/bin/                                       |
| godu (2 copies)          | Utility in Go to get disk usage stats                                                                                                | /opt/enterprise-analytics/bin/priv/                                  |
| saslauthd-port           | Erlang port process (wrapper) used to talk to the saslauthd daemon for authentication purposes                                       | /opt/enterprise-analytics/bin/                                       |
| beam.smp (3 copies)      | Couchbase Cluster Manager run as Erlang virtual machines - babysitter, ns\_server, and ns\_couchdb                                   | /opt/enterprise-analytics/lib/erlang/erts-14.2/bin/                  |
| epmd                     | Erlang-specific process which acts as a name server for Erlang distribution                                                          | /opt/enterprise-analytics/lib/erlang/erts-14.2/bin/                  |
| cpu\_sup (2 copies)      | Erlang-specific process used to collect CPU: 1 for ns\_server VM and 1 for ns\_couchdb VM                                            | /opt/enterprise-analytics/lib/erlang/lib/os\_mon-2.9.1/priv/bin/     |
| memsup (2 copies)        | Erlang-specific process used to collect memory usage: 1 for ns\_server VM and 1 for ns\_couchdb VM                                   | /opt/enterprise-analytics/lib/erlang/lib/os\_mon-2.9.1/priv/bin/     |
| inet\_gethost (4 copies) | Built-in Erlang port process that’s used to perform name service lookup                                                              | /opt/enterprise-analytics/lib/erlang/erts-14.2/bin/                  |
| portsigar                | Open source tool sigar that’s used to collect system information                                                                     | /opt/enterprise-analytics/bin/                                       |
| sh -s disksup (2 copies) | Erlang-specific process that’s used to supervise the available disk space: 1 for ns\_server VM and 1 for ns\_couchdb VM              | /opt/enterprise-analytics/lib/erlang/lib/os\_mon-2.9.1/ebin/         |
| sh -s ns\_disksup        | Wrapper for disksup which also collects information about mounted drives                                                             | /opt/enterprise-analytics/lib/ns\_server/erlang/lib/ns\_server/ebin/ |
| cbcollect\_info          | Utility used to collect Enterprise Analytics logs. Is seen only during log collection.                                               | /opt/enterprise-analytics/bin/                                       |
| java (Analytics Driver)  | JVM running the Enterprise Analytics Service                                                                                         | /opt/enterprise-analytics/lib/cbas/runtime/bin                       |
| cbas                     | Go-wrapper that communicates with ns\_server and manages the lifecycle of the Analytics Driver                                       | /opt/enterprise-analytics/bin/                                       |