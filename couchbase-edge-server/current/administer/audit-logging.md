---
title: Audit Logging
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.0/modules/administer/pages/audit-logging.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-edge-server/current/administer/audit-logging.html)

# Audit Logging

Audit logging is a separate optional log file that allows you to track events associated with administrative, management, and end-user operations made in Couchbase Edge Server. These logs are presented as a [JSON-lines formatted series of events](https://jsonlines.org/).

Audit logs typically include:

* A timestamp for each event.
* The nature of each event, such as a login attempt.
* The outcome of each event, such as success or failure.
* The user or system component that initiated the event.

Logs are immutable and cannot be altered once recorded.

You can configure the following options for your audit log file as show in the configuration options table.

For more information, see [Edge Server Configuration Schema](../configuration/edge-server-configuration.md#json-schema).

__Table 1\. Audit Log Configuration Options__
| Key                     | Type          | Value                                                       |
| ----------------------- | ------------- | ----------------------------------------------------------- |
| audit.file              | String        | Filename of audit log.                                      |
| audit.omit\_description | Boolean       | If true, audit events omit their description.               |
| audit.enable            | Array or "\*" | Array of audit events to enable, "\*" enables all events.   |
| audit.disable           | Array or "\*" | Array of audit events to disable, "\*" disables all events. |

> [!NOTE]
> If `audit.omit_description` is `true` in the audit configuration, the `description` field is not included.

Audit Events have four core components:

__Table 2\. Audit Log Event Breakdown__
| Key         | Type    | Value                                                  |
| ----------- | ------- | ------------------------------------------------------ |
| id          | Integer | Identifies the audit event type.                       |
| timestamp   | String  | An ISO-8601 timestamp.                                 |
| name        | String  | Name of the Audit Event, based on its id.              |
| description | String  | A longer, more detailed description of the event type. |

The following table lists all Audit Log Events that can be captured in the Couchbase Edge Server audit log file.

> [!IMPORTANT]
> If `Enabled` is `true`, the audit events are logged in the audit log file unless it’s within the `audit.disabled` array.

__Table 3\. Audit Log Events__
| Audit Event ID | Description                        | Enabled? |
| -------------- | ---------------------------------- | -------- |
| 57344          | Server Started.                    | true     |
| 57345          | Server Stopped.                    | true     |
| 57346          | Public HTTP request.               | false    |
| 57347          | User authenticated.                | true     |
| 57348          | User auth failed.                  | true     |
| 57349          | Read database.                     | false    |
| 57350          | Read all databases.                | true     |
| 57351          | Changes feed started.              | true     |
| 57352          | Changes feed ended.                | true     |
| 57353          | Replication client connect.        | true     |
| 57354          | Replication client disconnect.     | true     |
| 57355          | Inter-server replication start.    | true     |
| 57356          | Inter-server replication stop.     | true     |
| 57357          | Inter-server replication conflict. | true     |
| 57358          | Create document.                   | false    |
| 57359          | Read document.                     | false    |
| 57360          | Update document.                   | false    |
| 57361          | Delete document.                   | false    |
| 57362          | Read document metadata.            | false    |
| 57363          | Query                              | true     |

## [](#see-also)See Also

* [Administer](administer-landing.md)
* [Operational Logging](operational-logging.md)