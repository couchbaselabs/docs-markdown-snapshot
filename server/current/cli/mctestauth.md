---
title: mctestauth
description: The mctestauth tool allows you to troubleshoot authentication
  issues in data services.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/cli/pages/mctestauth.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:cli:mctestauth.adoc[]
---

[View original HTML](/server/current/cli/mctestauth.html)

# mctestauth

> The mctestauth tool allows you to troubleshoot authentication issues in data services. 

## [](#description)Description

The `mctestauth` tool allows you to troubleshoot the authentication issues in data services. Data services use the [Simple Authentication and Security Layer](https://en.wikipedia.org/wiki/Simple%5FAuthentication%5Fand%5FSecurity%5FLayer) (SASL) framework for authentication and provide you access to use the underlying mechanisms. For example, SCRAM-SHA512 or PLAIN.

The tool is located as follows:

| Platform | Location                                                                              |
| -------- | ------------------------------------------------------------------------------------- |
| Linux    | _/opt/couchbase/bin/mctestauth_                                                       |
| Windows  | _C:\\Program Files\\Couchbase\\Server\\bin\\mctestauth.exe_                           |
| Mac OS X | _/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/mctestauth_ |

## [](#syntax)Syntax

mctestauth [options]

The `options` are as follows:

| Options                                    | Description                                                                                                                 |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| \--host with parameter <hostname\[:port\]> | The name of the host (with an optional port) to connect to. For IPv6, use \[address\]:port if you need to specify the port. |
| \--user <username>                         | The username to be used in authentication.                                                                                  |
| \--password <password>                     | The password to be used in authentication.                                                                                  |
| \--tls                                     | Optionally, use TLS to authenticate.                                                                                        |
| \--ipv4                                    | Connect over IPv4.                                                                                                          |
| \--ipv6                                    | Connect over IPv6.                                                                                                          |
| \--version                                 | Find program version.                                                                                                       |
| \--no-color                                | Print output without any colors.                                                                                            |
| \--help                                    | Display help text.                                                                                                          |

## [](#example)Example

The following call tries to connect to the data server running on the host `192.168.86.101`. The call then tries the various authentication mechanisms supported by the server and prints out the result of each mechanism. The call succeeds only if you provide the correct credentials.

./mctestauth --host 192.168.86.101 --user jones --password password

If successful, the command returns output as follows:

    SCRAM-SHA512: OK
    SCRAM-SHA256: OK
    SCRAM-SHA1: OK
    PLAIN: OK

If `jones` was defined as an external user in LDAP, the output is as follows:

    SCRAM-SHA512: FAILED
    SCRAM-SHA256: FAILED
    SCRAM-SHA1: FAILED
    PLAIN: OK