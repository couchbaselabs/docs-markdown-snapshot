---
title: Logging Client-Side Errors
description: Client-side errors can be written to a log file.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/reference/pages/rest-client-logs.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/2.0/reference/rest-client-logs.html)

# Logging Client-Side Errors

> Client-side errors can be written to a log file. 

## [](#http-method-and-uri)HTTP method and URI

POST /logClientError

## [](#description)Description

If a client experiences an error, a corresponding entry can be written to the `info.log` log file, which is maintained by Enterprise Analytics in the standard, platform-specific location — see [Log-File Locations](rest-manage-log-collection.md#log-file-locations).

This method and URI can be used by any Enterprise Analytics role.

## [](#curl-syntax)Curl Syntax

curl -X POST http://<ip-address-or-domain-name>:8091/logClientError
  -u <username>:<password>

## [](#responses)Responses

Success returns `200 OK`. Failure to authenticate returns `401 Unauthorized`. An incorrectly specified URI returns `404 Object Not Found`.

## [](#example)Example

The following call logs a client error:

curl -X POST http://localhost:8091/logClientError -u Administrator:password

Following successful execution, the log file `info.log` can be checked as follows:

$ grep "client" info.log
[menelaus:warn,2023-06-06T16:43:11.136Z,ns_1@10.144.231.101:<0.19779.51>:menelaus_web:log_client_error:1115]Client-side error-report for user "<ud>Administrator</ud>" on node 'ns_1@10.144.231.101':

## [](#see-also)See Also

Logging, redaction, and file upload are described at [Manage Logging](../manage/manage-logging/manage-logging.md). This also provides a list of log-files, and a description of how to use logging with Couchbase Web Console. It also provides an introduction to managing logging with the CLI.