---
title: Manage Backup Configuration
description: This method lets you get and set the rotation size for Backup Service history.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/backup-manage-config.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:rest-api:backup-manage-config.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/rest-api/backup-manage-config.html)

# Manage Backup Configuration

> This method lets you get and set the rotation size for Backup Service history. 

## [](#http-methods-and-uris)HTTP Methods and URIs

Get the current rotation configuration:

GET /api/v1/config

Apply a new configuration:

POST /api/v1/config

__Table 1\. POST Parameter__
| Name                    | Description                                                                                                 | Schema                          |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------- |
| history\_rotation\_size | The maximum size of the backup history can grow to before the Backup Service starts removing older history. | Integer value between 5 and 200 |

## [](#curl-syntax)Curl Syntax

curl -X GET http://$BACKUP_SERVICE_NODE:$BACKUP_SERVICE_PORT/api/v1/config
  -u $USERNAME:$PASSWORD

curl -X POST http://$BACKUP_SERVICE_NODE:$BACKUP_SERVICE_PORT/api/v1/config
  -u $USERNAME:$PASSWORD
  -d '{"history_rotation_size":$HISTORY_ROTATION_SIZE}'

## [](#required-permissions)Required Permissions

To call this method via GET: Full Amin, Backup Admin, or Read-Only Admin.

To call this method via POST: Full Admin or Backup Admin.

## [](#responses)Responses

| Value                                                                                                      | Description                                                            |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 200 OK and when calling via GET, a JSON object containing the current settings.                            | Successful call.                                                       |
| 400 Bad Request plus the JSON message { "status": 400, "msg": "Rotation size has to be between 5 and 200"} | Returned when trying to set the rotation size to an invalid value.     |
| 401 Unauthorized                                                                                           | Authorization failure due to incorrect username or password.           |
| 403 Forbidden, plus a JSON message explaining the minimum permissions.                                     | The provided username has insufficient privileges to call this method. |

## [](#examples)Examples

The following call returns the current configuration limits:

curl -v -X GET http://127.0.0.1:8097/api/v1/config \
-u Administrator:password

If successful, the call returns `200 OK`, and the following object:

{"history_rotation_size":50}

The following call modifies the rotation size:

curl -v -X POST http://127.0.0.1:8097/api/v1/config -u Administrator:password \
-d '{"history_rotation_size":51}'

Success returns `200 OK`.

## [](#see-also)See Also

* For an overview of the Backup Service, see [Backup Service](../learn/services-and-indexes/services/backup-service.md).
* For a step-by-step guide to using Couchbase Server Web Console to configure and use the Backup Service, see [Manage Backup and Restore](../manage/manage-backup-and-restore/manage-backup-and-restore.md).