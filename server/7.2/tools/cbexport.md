---
title: cbexport
description: A utility for exporting data from a Couchbase cluster
editUrl: https://github.com/couchbase/backup/edit/neo/docs/modules/tools/pages/cbexport.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:tools:cbexport.adoc[]
---

[View original HTML](/server/7.2/tools/cbexport.html)

# cbexport

A utility for exporting data from a Couchbase cluster

## [](#synopsis)SYNOPSIS

cbexport [--version] [--help] <command> [<args>]

## [](#description)DESCRIPTION

cbexport is used to export data from Couchbase in various different formats.

For more information on how specific commands work you can run "cbexport <command> --help".

## [](#options)OPTIONS

\--version

Prints the cbexport suite version that the cbexport program came from.

\--help

Prints the synopsis and a list of commands.

If a cbexport command is named, this option will bring up the manual page for that command.

## [](#cbexport-commands)CBEXPORT COMMANDS

[cbexport-json](cbexport-json.md)

Exports data from Couchbase into a JSON file.

## [](#environment-and-configuration-variables)ENVIRONMENT AND CONFIGURATION VARIABLES

CB\_CLUSTER

Specifies the hostname of the Couchbase cluster to connect to. If the hostname is supplied as a command line argument then this value is overridden.

CB\_USERNAME

Specifies the username for authentication to a Couchbase cluster. If the username is supplied as a command line argument then this value is overridden.

CB\_PASSWORD

Specifies the password for authentication to a Couchbase cluster. If the password is supplied as a command line argument then this value is overridden.

CB\_CLIENT\_CERT

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `CB_CLIENT_KEY` as an alternative to the `CB_USERNAME` and `CB_PASSWORD` variables. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_CERT\_PASSWORD

The password for the certificate provided to the `CB_CLIENT_CERT` variable, when using this variable, the certificate/key pair is expected to be in the PKCS#12 format. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_KEY

The path to the client private key whose public key is contained in the certificate provided to the `CB_CLIENT_CERT` variable. May be supplied with `CB_CLIENT_CERT` as an alternative to the `CB_USERNAME` and `CB_PASSWORD`variables. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_KEY\_PASSWORD

The password for the key provided to the `CB_CLIENT_KEY` variable, when using this variable, the key is expected to be in the PKCS#8 format. See the CERTIFICATE AUTHENTICATION section for more information.

## [](#collection-aware-exports)COLLECTION AWARE EXPORTS

The default behavior of export for the cluster versions which support collections is to export all available scopes/collections in a bucket.

## [](#discussion)DISCUSSION

The cbexport command is used to export data from Couchbase to various different formats. Each supported export format is a subcommand of the cbexport utility.

## [](#operations-during-major-cluster-configuration-changes)OPERATIONS DURING MAJOR CLUSTER CONFIGURATION CHANGES

Operations (commands or sub-commands) which connect to a cluster are not supported during major cluster configuration changes.

For example, performing an import/export, making a backup or performing a restore whilst changing the TLS configuration/security settings is unsupported.

These types of changes (e.g. changing the TLS mode to strict) are not expected to be time consuming so it’s generally expected that operations should be started after completing the configuration change.

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