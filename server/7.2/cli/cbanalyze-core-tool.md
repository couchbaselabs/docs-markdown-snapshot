[View original HTML](/server/7.2/cli/cbanalyze-core-tool.html)

> The `cbanalyze-core` tool is used to parse and analyze core dump data. 

## [](#syntax)Syntax

The basic syntax is:

cbanalyze-core -r [root] -f [reportfile] [corefile]

## [](#description)Description

The command `cbanalyze-core` tool is a helper script to parse and analyze core dump from a Couchbase Server node.

|  | The cbanalyze-core tool cannot analyze minidump core files and should only be used when directed by Couchbase Support. |
|  | ---------------------------------------------------------------------------------------------------------------------- |

Depending upon your platform, this tool is at the following locations:

| Operating system | Location                                                                          |
| ---------------- | --------------------------------------------------------------------------------- |
| Linux            | _/opt/couchbase/bin/tools/_                                                       |
| Windows          | (Not available on this platform)                                                  |
| Mac OS X         | _/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/tools/_ |

## [](#options)Options

The following are the command options:

| Options            | Description                        |
| ------------------ | ---------------------------------- |
| \-r \[root\]       | Search for the binary in root.     |
| \-f \[reportfile\] | Use the specified file for output. |