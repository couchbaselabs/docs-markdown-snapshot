---
title: cbft-bleve
description: The <code>cbft-bleve</code> tool returns information on
  <em>Moss</em> and <em>Scorch</em> index partitions, and on <em>Zap</em> files.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cli/pages/cbft-bleve.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/cli/cbft-bleve.html)

# cbft-bleve

> The `cbft-bleve` tool returns information on _Moss_ and _Scorch_ index partitions, and on _Zap_ files. 

## [](#syntax)Syntax

cbft-bleve [command] [path] [argument] [--help]

The `command` specified as the principal argument to `cbft-bleve` can be any one of the following.

| Command    | Description                                                                                                                                                                                                                                                                                              |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| check      | Checks the contents of a specified index partition. Can be used on a _Moss_ index partition. Can be used on a _Scorch_ index partition, but only on platforms other than _CentOS_ and _Ubuntu_ Linux. Cannot be used on a _Zap_ file.                                                                    |
| count      | Counts the number of documents referenced by a specified index partition. Can be used on a _Moss_ index partition. Can be used on a _Scorch_ index partition, but only on platforms other than _CentOS_ and _Ubuntu_ Linux. Cannot be used on a _Zap_ file.                                              |
| dictionary | Prints to standard output the _term dictionary_ for a specified field in a specified index partition. Can be used on a _Moss_ index partition. Can be used on a _Scorch_ index partition, but only on platforms other than _CentOS_ and _Ubuntu_ Linux. Cannot be used on a _Zap_ file.                  |
| dump       | Dumps the contents of a specified _Moss_ index partition. Can be used on a _Moss_ index partition. Cannot be used on a _Scorch_ index partition. Cannot be used on a _Zap_ file.                                                                                                                         |
| fields     | Lists the fields in a specified index partition. Can be used on a _Moss_ index partition. Can be used on a _Scorch_ index partition, but only on platforms other than _CentOS_ and _Ubuntu_ Linux. Cannot be used on a _Zap_ file.                                                                       |
| mapping    | Prints to standard output the _mapping_ used for a specified index partition. Can be used on a _Moss_ index partition. Can also be used on a _Scorch_ index partition, but only on platforms other than _CentOS_ and _Ubuntu_ Linux. Cannot be used on a _Zap_ file.                                     |
| query      | Executes a specified query against a specified index partition. Can be used on a _Moss_ index partition. Can also be used on a _Scorch_ index partition, but only on platforms other than _CentOS_ and _Ubuntu_ Linux. Cannot be used on a _Zap_ file.                                                   |
| registry   | Prints to standard output the _analyzers_, _tokenizers_ and other components used by a specified index partition. Can be used on a _Moss_ index partition. Can also be used on a _Scorch_ index partition, but only on platforms other than _CentOS_ and _Ubuntu_ Linux. Cannot be used on a _Zap_ file. |
| scorch     | Establishes that the index partition on which information is to be returned is a _Scorch_ index partition. Can be used on a _Scorch_ index partition, on any Couchbase-Server supported platform. Cannot be used on either a _Moss_ index partition or a _Zap_ file.                                     |
| zap        | Estabishes that the specified path is that of a Zap file, on which information is to be returned. Can be used on a _Zap_ file, on any Couchbase-Server supported platform. Cannot be used on either a _Moss_ or a _Scorch_ index partition.                                                              |

When a value for `command` is _not_ specified, `--help` prints help text to standard output, describing the acceptable values of `command`. When a value for `command` _is_ specified, `--help` prints help text describing additional syntax entailed by the specified value (see [Per Command Syntax](#per-command-syntax), below).

The `path` is the filesystem path of an index partition or a Zap file: see [Specifying Index Partitions](#specifying-index-partitions), immediately below.

The `arguments` vary, according to the value specified for `command`. See the syntax and examples provided in [cbft-bleve for Moss Indexes](cbft-bleve-moss.md) and [cbft-bleve for Scorch Indexes](cbft-bleve-scorch.md).

## [](#specifying-index-partitions)Specifying Index Partitions

The _Search_ Service divides each _Full Text Index_ into _partitions_. The default number of partitions per index is six. For information, see [Index Partitions](../fts/fts-creating-indexes.md#index-partitions).

Many of the commands that can be used with `cbft-bleve` take as their principal argument the filesystem path of an index partition. Index partitions are themselves _directories_. The name of each (whether it is a _Moss_ or a _Scorch_ index) is formed from the _user-defined index-name_, the _uuid_ of the user-defined index, and the _partition id_: these are connected with underscores, and given the `.pindex` suffix. For example, `myIndex_690ef363c7557832_13aa53f3.pindex`.

Index partitions can be found in the following locations, on each node running the Search Service:

| OS        | Location                                                                             |
| --------- | ------------------------------------------------------------------------------------ |
| _Linux_   | /opt/couchbase/var/lib/couchbase/data/@fts/                                          |
| _Windows_ | C:\\Program Files\\couchbase\\server\\var\\lib\\couchbase\\data\\@fts\\              |
| _MacOS_   | /Users/<username>/Library/Application Support/Couchbase/var/lib/couchbase/data/@fts/ |

To specify a _Moss_ index partition, the pathname of the `.pindex` directory (located in one of the `@fts` directories listed above) should be given. To specify a _Scorch_ index partition with any of the command-values listed above _except_ `scorch`, the pathname of the `.pindex` directory (located in one of the `@fts` directories listed above) should be given. To specify a _Scorch_ index partition by means of the `scorch` command-value, the pathname of the `store` subdirectory (located in the `.pindex` directory) should be given.

Some commands provide information on the Zap file provided with each Scorch-index partition. To specify a Zap file, the pathname of the `.zap` file itself (located in the `store` subdirectory, under the `.pindex` directory) should be given.

Note that on Linux and MacOS, supervisor permission may be required, to view and access index partitions: therefore, the `sudo` command should be used as appropriate.

## [](#per-command-syntax)Per-Command Syntax

Each of the top-level commands that can be specified as a value to `cbft-bleve` entails its own syntax. The `scorch` and `zap` values refer to a specified Scorch index and to its associated Zap file, respectively.

Syntax and command-line examples for `cbft-bleve` when applied to:

* _Moss_ indexes, are provided at [cbft-bleve for Moss Indexes](cbft-bleve-moss.md).
* _Scorch_ indexes, are provided at [cbft-bleve for Scorch Indexes](cbft-bleve-scorch.md).
* _Zap_ files, are provided at [cbft-bleve for Zap Files](cbft-bleve-zap.md).