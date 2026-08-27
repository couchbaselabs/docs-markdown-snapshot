---
title: cbexport
description: A utility for exporting data from a Couchbase cluster
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/backup/edit/morpheus/docs/modules/tools/pages/cbexport.adoc
  xref: xref:server:tools:cbexport.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/tools/cbexport.html)

# cbexport

A utility for exporting data from a Couchbase cluster

## [](#synopsis)SYNOPSIS

cbexport [--version] [--help] <command> [<args>]

## [](#description)DESCRIPTION

cbexport is used to export data from Couchbase in various different formats.

For more information on how specific commands work you can run "cbexport <command> --help".

> [!IMPORTANT]
> Ensure that the version of `cbexport` is the same or greater than the version of Couchbase server (e.g., if you are running Couchbase Server 7.2, then ensure `cbexport` is 7.2, 7.6, 8.0 etc).

## [](#options)OPTIONS

\--version

Prints the cbexport suite version that the cbexport program came from.

\--help

Prints the synopsis and a list of commands.

If a cbexport command is named, this option will bring up the manual page for that command.

## [](#cbexport-commands)CBEXPORT COMMANDS

[cbexport-json](cbexport-json.md)

Exports data from Couchbase into a JSON file.

## [](#collection-aware-exports)COLLECTION AWARE EXPORTS

The default behavior of export for the cluster versions which support collections is to export all available scopes/collections in a bucket.

## [](#discussion)DISCUSSION

The cbexport command is used to export data from Couchbase to various different formats. Each supported export format is a subcommand of the cbexport utility.

## [](#operations-during-major-cluster-configuration-changes)OPERATIONS DURING MAJOR CLUSTER CONFIGURATION CHANGES

Operations (commands or sub-commands) which connect to a cluster are not supported during major cluster configuration changes.

For example, performing an import/export, making a backup or performing a restore whilst changing the TLS configuration/security settings is unsupported.

These types of changes (e.g. changing the TLS mode to strict) are not expected to be time consuming so it's generally expected that operations should be started after completing the configuration change.

Please note that this does not include rebalances; operations may be performed during a rebalance. The reason for this distinction, is that major cluster configuration changes are generally quick, whilst rebalances for large data sets may be time consuming.

## [](#further-documentation)FURTHER DOCUMENTATION

A manual page is available for each of the supported sources listed above.

## [](#authors)AUTHORS

cbexport\[1\] is a Couchbase Source tool and was written by Couchbase.

## [](#reporting-bugs)REPORTING BUGS

Report urgent issues to the Couchbase Support Team at [support@couchbase.com](mailto:support@couchbase.com). Bugs can be reported to the Couchbase Jira Bug Tracker at <http://www.couchbase.com/issues>.

## [](#see-also)SEE ALSO

[cbexport-json](cbexport-json.md)

## [](#cbexport)CBEXPORT

Part of the [cbexport](cbexport.md) suite