---
title: Get Backup Repository Information
description: The Backup Service REST API lets you list and get information about
  the active, imported, and archived backup repositories.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/backup-get-repository-info.adoc
  xref: xref:7.6@server:rest-api:backup-get-repository-info.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/rest-api/backup-get-repository-info.html)

# Get Backup Repository Information

## [](#description)Description

The Backup Service REST API lets you list and get information about the active, imported, and archived backup repositories.

## [](#http-methods-and-uris)HTTP Methods and URIs

List all backup repositories with a specific status:

GET /api/v1/cluster/self/repository/{REPO_STATUS}

Get overview information about a specific backup repository:

GET /api/v1/cluster/self/repository/{REPO_STATUS}/{REPO_NAME}

Get detailed information about a specific backup repository including backup names and dates, buckets, items, and mutations:

GET /api/v1/cluster/self/repository/{REPO_STATUS}/{REPO_NAME}/info

> [!NOTE]
> These URIs are only available from the Backup Service port (8097 by default) on nodes running the Backup Service.

__Table 1\. Path Parameters__
| Name         | Description                           | Schema                                         |
| ------------ | ------------------------------------- | ---------------------------------------------- |
| REPO\_STATUS | The current status of the repository. | One of the following: active imported archived |
| REPO\_NAME   | The name of the backup repository     | String                                         |

## [](#curl-syntax)Curl Syntax

curl -X GET $BACKUP_SERVICE_NODE:$BACKUP_SERVICE_PORT/cluster/self/\
repository/$REPO_STATUS
-u $USERNAME:$PASSWORD

curl -X GET <backup-node-ip-address-or-domain-name>:8097/cluster/self/\
repository/$REPO_STATUS/$REPO_NAME
-u $USERNAME:$PASSWORD

curl -X GET <backup-node-ip-address-or-domain-name>:8097/cluster/self/\
repository/$REPO_STATUS/$REPO_NAME/info
-u $USERNAME:$PASSWORD

## [](#required-permissions)Required Permissions

Full Admin, Backup Full Admin, or Read-Only Admin roles.

## [](#responses)Responses

| Value                                                                                       | Description                                                            |
| ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 200 OK and JSON array containing repository information depending on the specific endpoint. | Successful call.                                                       |
| 400                                                                                         | Invalid parameter.                                                     |
| 400 Object Not found                                                                        | The repository in the endpoint URI does not exist.                     |
| 401 Unauthorized                                                                            | Authorization failure due to incorrect username or password.           |
| 403 Forbidden, plus a JSON message explaining the minimum permissions.                      | The provided username has insufficient privileges to call this method. |
| 404 Object Not Found                                                                        | Error in the URI path.                                                 |
| 500 Could not retrieve the requested repository                                             | Error in Couchbase Server.                                             |

## [](#examples)Examples

The following `curl` command returns information about all active repositories. The command pipes the output to the [jq](https://stedolan.github.io/jq/) command for readability.

```console
curl -v -X GET \
http://127.0.0.1:8097/api/v1/cluster/self/repository/active \
-u Administrator:password  | jq
```

Successful execution returns a JSON array, each of whose members is an object containing information on an active repository. Information includes repository names, file or cluster paths, and plan details. The initial part of the potentially extensive output might appear as follows:

```json
[
  {
    "id": "bestRepo",
    "plan_name": "BackupAndMergePlan",
    "state": "active",
    "archive": "/Users/user/Documents/archives/bestRepo",
    "repo": "40aa565c-6049-4ea9-9837-516a2dcdf53b",
    "scheduled": {
      "BackupEveryTuesdayForOneYear": {
        "name": "BackupEveryTuesdayForOneYear",
        "task_type": "BACKUP",
        "next_run": "2021-09-28T21:00:00+01:00"
      },
      "testTask3": {
        "name": "testTask3",
        "task_type": "MERGE",
        "next_run": "2020-10-29T22:00:00Z"
      }
    },
    "version": 1,
    "health": {
      "healthy": true
    },
    "creation_time": "2020-10-01T13:28:56.207976+01:00",
    "update_time": "2020-10-01T13:28:56.207976+01:00"
  },
  {
    "id": "testRepo",
    "plan_name": "_hourly_backups",
    "bucket": {
      "name": "travel-sample",
      "uuid": "15b15c78439db91ba73f27ac4d6ba116"
    },
      .
      .
      .
  }
]
```

Each object thus contains the `id` (name), `plan_name`, `state`, `repo` (unique identifier), and scheduled tasks for the repository. It also contains an account of the repository's health, its creation time, and the time of its latest update.

The following call returns information on a specific, named, active repository:

```console
curl -v -X GET \
http://127.0.0.1:8091/_p/backup/api/v1/cluster/self/repository/active/restRepo \
-u Administrator:password  | jq
```

If successful, the call returns the following object:

```json
{
  "id": "restRepo",
  "plan_name": "_hourly_backups",
  "bucket": {
    "name": "travel-sample",
    "uuid": "15b15c78439db91ba73f27ac4d6ba116"
  },
  "state": "active",
  "archive": "/Users/user/Documents/archives/restRepo",
  "repo": "8b623987-9353-48f0-9773-55b124ce9146",
  "scheduled": {
    "backup_hourly": {
      "name": "backup_hourly",
      "task_type": "BACKUP",
      "next_run": "2020-10-02T09:00:41+01:00"
    },
    "merge_every_6_hours": {
      "name": "merge_every_6_hours",
      "task_type": "MERGE",
      "next_run": "2020-10-02T12:30:48+01:00"
    },
    "merge_week": {
      "name": "merge_week",
      "task_type": "MERGE",
      "next_run": "2020-10-04T23:40:00+01:00"
    }
  },
  "version": 1,
  "health": {
    "healthy": true
  },
  "creation_time": "2020-09-29T10:48:52.232386+01:00",
  "update_time": "2020-09-29T10:48:52.232386+01:00"
}
```

The object thus contains information on the specified repository.

The following call returns information including backup names and dates, buckets, items, and mutations; on an imported repository named `mergedRepo`:

```console
curl -v -X GET http://127.0.0.1:8097/api/v1/cluster/self/repository/imported/mergedRepo/info \
-u Administrator:password  | jq
```

If successful, the initial part of the potentially extensive output is as follows:

```json
{
  "name": "7509894b-7138-40fe-917e-9581d298482c",
  "size": 23859762,
  "count": 4,
  "backups": [
    {
      "date": "2020-09-16T09_00_29.113465+01_00",
      "type": "MERGE - FULL",
      "source": "Merge",
      "range": [
        "2020-09-16T08_00_25.672063+01_00",
        "2020-09-16T08_15_26.560952+01_00",
        "2020-09-16T08_30_27.458006+01_00",
        "2020-09-16T08_45_28.32018+01_00",
        "2020-09-16T09_00_29.113465+01_00"
      ],
      "events": 0,
      "fts_alias": 0,
      "size": 23806455,
      "buckets": [
        {
          "name": "travel-sample",
          "size": 23806449,
          "items": 31592,
          "mutations": 31592,
          "tombstones": 0,
          "views_count": 0,
          "fts_count": 0,
          "index_count": 10,
          "analytics_count": 0,
          "scopes": {
            "0": {
              "uid": 0,
              "name": "_default",
              "mutations": 31592,
              "tombstones": 0,
              "collections": {
                "0": {
                  "id": 0,
                  "name": "_default",
                  "mutations": 31592,
                  "tombstones": 0
                }
              }
            },
            "8": {
              "uid": 8,
              "name": "MyScope",
              "mutations": 0,
              "tombstones": 0,
              "collections": {
                "8": {
                  "id": 8,
                  "name": "MyCollection",
                  "mutations": 0,
                  "tombstones": 0
                }
              }
            }
          }
        }
      ],
      "complete": true,
      "source_cluster_uuid": "a7ec688d232620b2a9ea8c28ca68fd9a"
    },
    {
      "date": "2020-09-16T09_15_29.826312+01_00",
      "type": "INCR",
      "source": "http://127.0.0.1:8091",
      "events": 0,
      "fts_alias": 0,
      "size": 17769,
        .
        .
        .
    }
  ]
}
```

## [](#see-also)See Also

* For an overview of the Backup Service, see [Backup Service](../learn/services-and-indexes/services/backup-service.md).
* For a step-by-step guide to using Couchbase Server Web Console to configure and use the Backup Service, see [Manage Backup and Restore](../manage/manage-backup-and-restore/manage-backup-and-restore.md).
* For Information about using the Backup Service REST API to create a plan, see [Create and Edit Plans](backup-create-and-edit-plans.md).
* For information about using the Backup Service REST API to create a repository, see [Create a Repository](backup-create-repository.md).