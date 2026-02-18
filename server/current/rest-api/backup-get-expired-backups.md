---
title: Get Expired Backup Information
description: The Backup Service REST API lets you retrieve information about the
  expired backups in a repository.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/backup-get-expired-backups.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/rest-api/backup-get-expired-backups.html)

# Get Expired Backup Information

## [](#description)Description

> This HTTP method and URI return an array containing the expiry information of the backups in a repository specified by the `REPO_NAME` path-parameter. 

## [](#http-methods-and-uris)HTTP Methods and URI

GET /api/v1/cluster/self/repository/{REPO_STATUS}/{REPO_NAME}/expiredBackups

> [!NOTE]
> These URIs are only available from the Backup Service port (8097 by default) on nodes running the Backup Service.

__Table 1\. Path Parameters__
| Name         | Description                          | Schema                                   |
| ------------ | ------------------------------------ | ---------------------------------------- |
| REPO\_STATUS | The status of the backup repository. | Must be one of: active imported archived |
| REPO\_NAME   | The name of the repository           | String                                   |

## [](#curl-syntax)Curl Syntax

curl -X GET http://$BACKUP_SERVICE_NODE:$BACKUP_SERVICE_PORT/cluster/self\
     /repository/$REPO_STATUS/$REPOSITORY_NAME/expiredBackups \
     -u $USERNAME:$PASSWORD

## [](#required-permissions)Required Permissions

Full Admin, Backup Full Admin, or Read-Only Admin roles.

## [](#responses)Responses

| Value                                                                   | Description                                                            |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 200 OK and JSON array containing the expired backups and their details. | Successful call.                                                       |
| 400                                                                     | Invalid parameter.                                                     |
| 400 Object Not found                                                    | The repository in the endpoint URI does not exist.                     |
| 401 Unauthorized                                                        | Authorization failure due to incorrect username or password.           |
| 403 Forbidden, plus a JSON message explaining the minimum permissions.  | The provided username has insufficient privileges to call this method. |
| 404 Object Not Found                                                    | Error in the URI path.                                                 |
| 500 Internal Server Error                                               | Error in Couchbase Server.                                             |

## [](#example)Examples

> [!NOTE]
> The following examples assume you’re running the curl command from a node that is running the Backup Service.

The following call returns the details of expired backups for the active repository `repoNewForPrune`:

```console
curl -v -X GET http://127.0.0.1:8097/api/v1/cluster/self/\
     repository/active/repoNewForPrune/expiredBackups \
     -u Administrator:password
```

If the call is successful, the output may appear as follows:

```json
[
  {
  "expired_backups": [
    "2025-07-27T10_01_47.657575+05_30"
  ],
  "expired_backups_with_non_expired_dependents": [
    "2025-07-27T10_01_48.657595+05_30"
  ]
  }
]
```

## [](#see-also)See Also

* For a an overview of the Backup Service, see [Backup Service](../learn/services-and-indexes/services/backup-service.md).
* For a step-by-step guide to configure and use the Backup Service using the Couchbase Server Web Console, see [Manage Backup and Restore](../manage/manage-backup-and-restore/manage-backup-and-restore.md).