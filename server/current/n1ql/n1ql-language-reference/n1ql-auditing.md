---
title: SQL++ Auditing
description: SQL++-related activities can be audited, by Couchbase Server.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/n1ql-auditing.adoc
pubDate: 2026-04-23T05:28:56.075Z
link: xref:server:n1ql:n1ql-language-reference/n1ql-auditing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-language-reference/n1ql-auditing.html)

# SQL++ Auditing

> SQL++-related activities can be audited, by Couchbase Server. 

## [](#understanding-sql-auditing)Understanding SQL++ Auditing

This section provides specific information on Couchbase Server auditing as it relates to SQL++. For a general description of auditing with Couchbase Server, see [Auditing](../../learn/security/auditing.md).

Couchbase Server provides auditing for SQL++-related activities such as the following:

* Authenticating
* Starting and stopping the Query Service
* Editing Query Service settings
* Executing SQL++ statements
* Non-query API requests

SQL++-related activities are logged whether they are executed by a person or by an application running on behalf of a person. Auditing occurs at the level of _requests_, rather than of _operations_. Thus, when a request arrives with a SELECT query, only the SELECT query itself is logged: the associated subsidiary operations performed by the Data and Index Services are _not_ logged.

Auditing causes a reduction in SQL++ query-performance. This is in the range of 9% to 17% of queries performed per second: the exact reduction depends on query-size, and on the amount of auditing that has been enabled. Large queries and minimal auditing cause less performance-reduction.

Auditing can be configured by means of Couchbase Web Console: see the information provided in [Manage Auditing](../../manage/manage-security/manage-auditing.md). To capture SQL++-related events, use the **Query and Index Service** panel. Events available to be audited include ones issued through the SDK, the Query workbench, and the Query Shell.

## [](#audit-log-format)Audit Log Format

The audit records are written in JSON format to match the format used for Admin Auditing to allow easy integration with downstream auditing tools for audit log analysis. The syslog format will allow for integration with third party SIEM tools, such as QRadar.

__Table 1\. Required auditing fields for executed statements__
| Field        | Description                                                                                                                                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                                                                                                                                     |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| timestamp    | Exact date and time of the access event in UTC format.                                                                                                                                                                                                                                                                                                          | 2018-02-09T14:52:35.163-08:00                                                                                                                                                                                                                                                                                                                               |
| real\_userid | Source/User from basic authentication fields of request.                                                                                                                                                                                                                                                                                                        | "source":"local", "user":"Administrator"                                                                                                                                                                                                                                                                                                                    |
| requestId    | UUID of request, generated by the SQL++ server.                                                                                                                                                                                                                                                                                                                 | aee53bf0-d009-4015-8a1d-efec74f2cd74                                                                                                                                                                                                                                                                                                                        |
| statement    | The actual SQL++ query that was executed.                                                                                                                                                                                                                                                                                                                       | SELECT \* FROM \`travel-sample\`                                                                                                                                                                                                                                                                                                                            |
| isAdHoc      | TRUE for statements made directly. FALSE for prepared statements.                                                                                                                                                                                                                                                                                               | TRUE                                                                                                                                                                                                                                                                                                                                                        |
| userAgent    | To identify the type of user by a combination of the User-Agent and CB-User-Agent headers in one of the following formats: Query Workbench CURL request CBQ shell SDK                                                                                                                                                                                           | Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_10\_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 (Couchbase Query Workbench (5.1.0-1434-enterprise)) curl/7.43.0 Go-http-client/1.1 (CBQ/2.0) couchbase-java-client/2.5.2 (git: 2.5.2, core: 1.5.2) (Mac OS X/10.11.6 x86\_64; Java HotSpot(TM) 64-Bit Server VM 1.8.0\_101-b13) |
| node         | Assigned name (IP address) of the server where the request ran. local for unclustered nodes.                                                                                                                                                                                                                                                                    | local                                                                                                                                                                                                                                                                                                                                                       |
| status       | Status of the request, as success or failed or stopped.                                                                                                                                                                                                                                                                                                         | success                                                                                                                                                                                                                                                                                                                                                     |
| metrics      | The elapsed time, execution time, result count, and result size (MB). The elapsed time and execution time use a duration string format, which includes a numeric value and a unit suffix. The unit varies depending on the duration of the query. Valid units are: ms \- milliseconds µs \- microseconds ns \- nanoseconds s \- seconds m \- minutes h \- hours | "elapsedTime":"7.599684ms", "executionTime":"7.507755ms", "resultCount":0, "resultSize":0                                                                                                                                                                                                                                                                   |
| id           | Number for the [audit event type](#section%5Fnyb%5Fjsh%5Fwcb).                                                                                                                                                                                                                                                                                                  | 28672                                                                                                                                                                                                                                                                                                                                                       |
| name         | The SQL++ command or REST API request type.                                                                                                                                                                                                                                                                                                                     | SELECT                                                                                                                                                                                                                                                                                                                                                      |
| description  | Description of the event type.                                                                                                                                                                                                                                                                                                                                  | A SQL++ SELECT statement was executed                                                                                                                                                                                                                                                                                                                       |

__Table 2\. Optional auditing fields for statements__
| Field           | Description                                                                                                                                                                                                                                    | Example        |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| namedArgs       | Names and values of name arguments.                                                                                                                                                                                                            | $val and $user |
| positionalArgs  | Array of values of positional arguments.                                                                                                                                                                                                       | $1 and ?       |
| clientContextId | Captured from the client\_context\_id parameter of the SQL++ query. May be used to distinguish between user-generated queries and UI-generated queries from the Query WorkBench. UI-generated queries have the prefix INTERNAL- in this field. |                |

> [!NOTE]
> The client context ID has no security guarantees. The parameter can be set by any user in any request and is not verified in the server, so it should not be relied upon for security purposes.

__Table 3\. Required auditing fields for API requests__
| Field          | Description                                                       | Example                                                                    |
| -------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------- |
| timestamp      | Exact date and time of the access event in UTC format.            | 2018-02-09T14:52:35.163-08:00                                              |
| real\_userid   | Source/User from basic authentication fields of request.          | "source":"local","user":"Administrator"                                    |
| httpMethod     | The API method call, either GET, PUT, DELETE, POST                | GET                                                                        |
| httpResultCode | The number representing the API result.                           | 200                                                                        |
| errorMessage   | If an error occurred, this will contain information on the error. | User does not have credentials to run queries accessing the system tables. |
| id             | Number for the [API auditing code](#section%5Fcmd%5Flyh%5Fwcb).   | 28689                                                                      |
| name           | The API request location.                                         | /admin/ping                                                                |
| description    | Description of the event type.                                    | An HTTP request was made to the API at /admin/ping.                        |

## [](#examples)Examples

To reduce disk usage and improve performance, the log files are as compact as possible.

To make the log entry easier-to-read, use a formatting utility such as [jq](https://stedolan.github.io/jq/).

Example 1\. 

Execute `SELECT * FROM orders` via a CURL statement.

```json
{
  "timestamp": "2018-02-09T14:52:35.163-08:00",
  "real_userid": {
    "source": "local",
    "user": "Administrator"
  },
  "requestId": "aee53bf0-d009-4015-8a1d-efec74f2cd74",
  "statement": "SELECT * FROM orders",
  "isAdHoc": true,
  "userAgent": "curl/7.43.0",
  "node": "local_node",
  "status": "success",
  "metrics": {
    "elapsedTime": "7.599684ms",
    "executionTime": "7.507755ms",
    "resultCount": 0,
    "resultSize": 0
  },
  "id": 28672,
  "name": "SELECT statement",
  "description": "A N1QL SELECT statement was executed"
}
```

Example 2\. 

Execute `DELETE FROM orders WHERE priority = 6` via a CURL statement.

```json
{
  "timestamp": "2018-02-09T14:52:55.786-08:00",
  "real_userid": {
    "source": "local",
    "user": "Administrator"
  },
  "requestId": "ded68ae3-d964-4d87-b1c2-70cf72041c6b",
  "statement": "DELETE FROM orders WHERE priority = 6",
  "isAdHoc": true,
  "userAgent": "curl/7.43.0",
  "node": "local_node",
  "status": "success",
  "metrics": {
    "elapsedTime": "8.884558ms",
    "executionTime": "8.853976ms",
    "resultCount": 0,
    "resultSize": 0
  },
  "id": 28678,
  "name": "DELETE statement",
  "description": "A N1QL DELETE statement was executed"
}
```

Example 3\. 

Make an HTTP `GET` method from an `/admin/ping` API request.

```json
{
  "timestamp": "2018-02-09T14:53:10.856-08:00",
  "real_userid": {
    "source": "internal",
    "user": "unknown"
  },
  "httpMethod": "GET",
  "httpResultCode": 200,
  "errorMessage": "",
  "id": 28697,
  "name": "/admin/ping API request",
  "description": "An HTTP request was made to the API at /admin/ping."
}
```

## [](#audit-rotation)Audit Rotation

The auditing Rotation parameters can be only one of the following:

| Audit Log Rotation Type | Examples                           |
| ----------------------- | ---------------------------------- |
| Time-based (days)       | 7 (for weekly); 30 (for monthly).  |
| Size-based (MB)         | 10 (for 10 MB); 10000 (for 10 GB). |

## [](#audit-failure-semantics)Audit Failure Semantics

When the audit target fails, the auditing system can be set to one of the following:

| Failure Response Type | Description                                                                                                                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ignore                | Continue the action without firing an audit record.                                                                                                                                           |
| Block                 | Cancel the operation.                                                                                                                                                                         |
| Log Reuse             | This option is for out-of-space failures: **Time-Based**: Limit audit logs to the specified number of recent days. **Size-Based**: Limit audit log size to the specified number of megabytes. |

If an audit record attempt fails in the query engine, an error message will be printed to the `query.log` file.

## [](#audit-trail-protection)Audit Trail Protection

To prevent unauthorized modification of the audit service configuration, the auditing system restricts access to configuring only to Full and Local User Security Administrators.

Audit records are immutable since the auditing system prevents changes of audit event records once written.

Once archived, audit data is deleted from Couchbase, and the file space is recovered.

The [cbcollect\_info](../../cli/cbcollect-info-tool.md) utility does not collect audit logs.

## [](#section%5Fnyb%5Fjsh%5Fwcb)Audit Event Types

Below is the list of all events that are captured in the audit logs.

1. System clock modifications, as captured in the operating system audit log
2. Disabling auditing
3. Enabling auditing, with audit settings written
4. Login, both success and failure
5. Logout, both success and failure
6. Data access operations — see [Query and Index Service Events](../../audit-event-reference/audit-event-reference.md#query-service-event-list-table)
7. Audit archive
8. System backup
9. Data service:

  1. Read
  2. Write
  3. DCP-Read
  4. DCP-Write
10. Search service:

  1. FTS-Read
11. Analytics audit events

Items that will not be captured in the audit logs:

* API calls that are not statements
* API requests sent to URLs the query engine does not service
* API requests which are handled by the autonomic functionality of the HTTP server

## [](#section%5Fcmd%5Flyh%5Fwcb)API Auditing Codes

Audit records will be issued by the query engine for requests to its secondary APIs. This does not include the main URL used for queries (/query/service) but does include all other URLs the query engine listens to.

There will be a separate audit record code for each registered URL. The mapping from URLs to audit record codes is given below. Some URLs require extra fields, as noted.

| Audit Code | API                                                                                                              | Remarks                                                                                                                                                                                                                                    |
| ---------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 28689      | /admin/stats /admin/stats/{stat}                                                                                 | Field "stat": optional, string, for input parameter {stat} if present.                                                                                                                                                                     |
| 28690      | /admin/vitals                                                                                                    |                                                                                                                                                                                                                                            |
| 28691      | /admin/prepareds /admin/prepareds/{name}                                                                         | Field "name": optional, string, for input parameter {name} if present. Do not audit POST requests.                                                                                                                                         |
| 28692      | /admin/active\_requests /admin/active\_requests/{request}                                                        | Field "request": optional, string, for input parameter {request} if present. Do not audit POST requests.                                                                                                                                   |
| 28693      | /admin/indexes/prepareds                                                                                         |                                                                                                                                                                                                                                            |
| 28694      | /admin/indexes/active\_requests                                                                                  |                                                                                                                                                                                                                                            |
| 28695      | /admin/indexes/completed\_requests                                                                               |                                                                                                                                                                                                                                            |
| 28696      | /debug/vars                                                                                                      |                                                                                                                                                                                                                                            |
| 28697      | /admin/ping                                                                                                      |                                                                                                                                                                                                                                            |
| 28698      | /admin/config                                                                                                    |                                                                                                                                                                                                                                            |
| 28699      | /admin/ssl\_cert                                                                                                 |                                                                                                                                                                                                                                            |
| 28700      | /admin/settings                                                                                                  |                                                                                                                                                                                                                                            |
| 28701      | /admin/clusters /admin/clusters/{cluster} /admin/clusters/{cluster}/nodes /admin/clusters/{cluster}/nodes/{node} | Field "cluster": optional, string, for input parameter {cluster} if present. Field "node": optional, string, for input parameter {node} if present. Field "body": PUT/POST only, JSON representation of cluster or node from request body. |
| 28702      | /admin/completed\_requests /admin/completed\_requests/{request}                                                  | Field "request": optional, string, for input parameter {request} if present. Do not audit POST requests.                                                                                                                                   |