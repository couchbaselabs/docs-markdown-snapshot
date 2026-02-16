[View original HTML](/server/7.6/tools/cbimport.html)

A utility for importing data into a Couchbase cluster

## [](#synopsis)SYNOPSIS

cbimport [--version] [--help] <command> [<args>]

## [](#description)DESCRIPTION

cbimport is used to import data from various sources into Couchbase.

For more information on how specific commands work, you can run "cbimport <command> --help".

## [](#options)OPTIONS

\--version

Prints the cbimport suite version that the cbimport program came from.

\-h,--help

Prints the synopsis and a list of commands. If a cbimport command is named, this option will bring up the manual page for that command.

## [](#cbimport-commands)CBIMPORT COMMANDS

[cbimport-csv](cbimport-csv.md)

Imports data into Couchbase from a CSV file.

[cbimport-json](cbimport-json.md)

Imports data into Couchbase from a JSON file.

## [](#discussion)DISCUSSION

The cbimport command is used to import data from various sources into a Couchbase cluster. Each supported format is a subcommand of the cbimport utility.

## [](#insertingoverwriting-documents)INSERTING/OVERWRITING DOCUMENTS

`cbimport` can import documents into buckets that contain existing records.

If `cbimport` encounters an existing record in the bucket that has a document id that matches a record from the input source then it will overwrite the existing record with the document from the input source.

New records (i.e., documents that do not have an existing `id` in the target bucket) are added as new documents.

## [](#operations-during-major-cluster-configuration-changes)OPERATIONS DURING MAJOR CLUSTER CONFIGURATION CHANGES

Operations (commands or sub-commands) which connect to a cluster are not supported during major cluster configuration changes.

For example, performing an import/export, making a backup or performing a restore whilst changing the TLS configuration/security settings is unsupported.

These types of changes (e.g. changing the TLS mode to strict) are not expected to be time consuming so it’s generally expected that operations should be started after completing the configuration change.

Please note that this does not include rebalances; operations may be performed during a rebalance. The reason for this distinction, is that major cluster configuration changes are generally quick, whilst rebalances for large data sets may be time consuming.

## [](#json-specification)JSON SPECIFICATION

The cbimport utility translates data read from disk into JSON documents before importing them into the provided cluster. The converted documents must conform to the JSON specification defined in `RFC 8259`.

This means cbimport will skip importing documents that either: 1) Are not valid JSON 2) Are not valid UTF-8 data, as defined in `RFC 8259` JSON transferred between systems MUST be encoded using UTF-8.

Documents that are skipped during an import will be logged, along with the line number/index from which they originated. This information can be used to single out/fix invalid documents prior to re-importing.

## [](#further-documentation)FURTHER DOCUMENTATION

A manual page is available for each of the supported sources listed above.

## [](#authors)AUTHORS

cbimport is a Couchbase Source tool and was written by Couchbase.

## [](#reporting-bugs)REPORTING BUGS

Report urgent issues to the Couchbase Support Team at [support@couchbase.com](mailto:support@couchbase.com). Bugs can be reported to the Couchbase Jira Bug Tracker at <http://www.couchbase.com/issues>.

## [](#see-also)SEE ALSO

[cbimport-csv](cbimport-csv.md), [cbimport-json](cbimport-json.md)

## [](#cbimport)CBIMPORT

Part of the [cbimport](cbimport.md) suite