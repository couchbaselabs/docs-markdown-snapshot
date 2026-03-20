---
title: cbepctl
description: The <code>cbepctl</code> tool is used to control vBucket states,
  configuration, and memory and disk persistence behavior.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cli/pages/cbepctl-intro.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:cli:cbepctl-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/cli/cbepctl-intro.html)

# cbepctl

> The `cbepctl` tool is used to control vBucket states, configuration, and memory and disk persistence behavior. 

## [](#description)Description

This tool is a per-node, per-bucket operation. That means that the IP address of a node in the cluster and a named bucket must be specified. If a named bucket is not provided, the server applies the setting to any default bucket that exists at the specified node. To perform this operation for an entire cluster, perform the command for every node/bucket combination that exists for that cluster.

For example, when a bucket is shared by two nodes, issue this command twice and provide the different host names and ports for each node along with the bucket name. Similarly, when two data buckets are on the same node, issue the command twice for each bucket. If a bucket is not specified, the command applies to the default bucket or returns an error if a default bucket does not exist.

> [!IMPORTANT]
> Changes to the cluster configuration using `cbepctl` are not persisted over a cluster restart.

The tool is found in the following locations:

| Operating system | Location                                                                           |
| ---------------- | ---------------------------------------------------------------------------------- |
| Linux            | _/opt/couchbase/bin/cbepctl_                                                       |
| Windows          | _C:\\Program Files\\Couchbase\\Server\\bin\\cbepctl.exe_                           |
| Mac OS X         | _/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/cbepctl_ |

## [](#syntax)Syntax

Basic syntax for this command:

cbepctl [host]:11210 [command] [options]

For this command, `host` is the IP address for the Couchbase Server cluster or node in the cluster. The port is always the standard port used for cluster-wide stats and is at `11210`.

Use the following commands to manage persistence:

__Table 1\. cbepctl commands__
| Command                          | Description                                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------------- |
| stop                             | Stop persistence                                                                                   |
| start                            | Start persistence                                                                                  |
| drain                            | Wait until queues are drained                                                                      |
| set \[type\] \[param\] \[value\] | Set checkpoint\_param and flush\_param command types. This changes how or when persistence occurs. |

## [](#options)Options

The following are the command options:

| Option             | Description                                             |
| ------------------ | ------------------------------------------------------- |
| \-h, --help        | Shows the help message and exits.                       |
| \-a                | Iterates over all buckets.                              |
| \-b \[BUCKETNAME\] | The bucket to control. Default: default.                |
| \-u \[USERNAME\]   | The username to authenticate. Default: the bucket name. |
| \-p \[PASSWORD\]   | The password for the bucket, if one exists.             |
| \-S                | Reads the password from stdin.                          |