---
title: cbqueryreportgen
description: The <code>cbqueryreportgen</code> tool returns the complete details
  of any Query service to generate reports.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/cli/pages/cbqueryreportgen.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/cli/cbqueryreportgen.html)

# cbqueryreportgen

> A query tool that returns the complete details of any Query Service to generate reports. 

## [](#syntax)Syntax

cbqueryreportgen [-<args>
                  [ -c, --cluster <cluster> ]
                  [ -u, --username <username> ]
                  [ -p, --password <password> ]
                  [ -k, <keyspace> ]
                  [ -t1, <start-time>,<end-time> ]
                  [ -t2, <start-time>,<end-time> ]
                  [ -o, --output <output> ]
                  [ -l, --limit <limit> ]
                  [ -v, --verbose ]
                  [ -h, --help ]
                 ]

## [](#description)Description

This tool is only available in Couchbase Server 8.0 and later.

The `cbqueryreportgen` command connects to a Couchbase cluster and generates performance reports based on the Query Service’s AWR statistics.

The tool allows you to specify a time range for the report. You can specify 2 different time periods, allowing a report to be generated that compares query statistics over the different time periods. You can also specify the output file where the report must be saved. The output of the command is a report in HTML format.

Depending upon your platform, this tool is at the following locations:

| Operating system | Location                                                                 |
| ---------------- | ------------------------------------------------------------------------ |
| Linux            | /opt/couchbase/bin/                                                      |
| Windows          | C:\\Program Files\\Couchbase\\Server\\bin\\                              |
| Mac OS X         | /Applications/CouchbaseServer.app/Contents/Resources/couchbase-core/bin/ |

## [](#options)Options

Required flags:

The following flags are required to run the `cbqueryreportgen` command.

The `-c, --cluster` flag specifies the hostname of the Couchbase cluster. Example: `couchbase://localhost`.

The `-u, --username` flag specifies the username of the Couchbase cluster. Example: `-u Administrator`.

The `-p, --password` flag specifies the password of the Couchbase cluster. Example: `-p password`.

The `-k` flag specifies the keyspace. The keyspace is the AWR repository in the `bucket.scope.collection` format. Example: `travel-sample._default.awr`.

The `-t1` flag specifies the start-time and end-time for the report, in the local timezone. Enter both start-time and end-time in the `YYYY-MM-DDTHH:MM:SS` format, separated by a comma. Example: `2025-09-01T00:00:00,2025-09-02T00:00:00`.

The `-o, --output` flag specifies the output file for the report. Example: `report.html`.

Optional flags:

The `-t2` flag specifies the start-time and end-time of the second time period, in the local timezone. Enter both start-time and end-time in the `YYYY-MM-DDTHH:MM:SS` format, separated by a comma. Example: `2025-09-02T00:00:00,2025-09-03T00:00:00`.

The `-l, --limit` flag specifies the maximum number of results to include for every query. The default is `1000`.

The `-v, --verbose` flag enables verbose logging for debugging purposes.

The `-h, --help` flag prints the help information.

For more information about how the specific command works, run `cbqueryreportgen --help`.

## [](#example)Example

This example creates a report showing all of the statistics for a single day. The AWR repository is `travel-sample._default.awr`. It’s assumed that you have already specified this as the AWR repository, and created an index on the document key in the configured AWR location.

```sh
cbqueryreportgen -c couchbase://localhost \
-u Administrator -p password \
-k travel-sample._default.awr \
-o report.html \
-t1 '2025-09-01T00:00:00,2025-09-01T23:59:59'
```

The output of the command is a report in HTML format, saved to the file `report.html`.

## [](#see-also)See Also

For detailed information, see [Automatic Workload Repository](../n1ql/n1ql-manage/query-awr.md).