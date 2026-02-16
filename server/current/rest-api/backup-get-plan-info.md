[View original HTML](/server/current/rest-api/backup-get-plan-info.html)

> The Backup Service REST API lets you get information about backup plans. 

## [](#http-methods-and-uris)HTTP Methods and URIs

Get a list of all defined backup plans:

GET /plan

Get detailed information about a specific backup plan:

GET /plan/{PLAN_NAME}

__Table 1\. Path Parameters__
| Name       | Description                | Schema |
| ---------- | -------------------------- | ------ |
| PLAN\_NAME | The name of a backup plan. | String |

## [](#curl-syntax)Curl Syntax

curl -X GET http://$BACKUP_SERVICE_NODE:$BACKUP_SERVICE_PORT/plan
  -u $USERNAME:$PASSWORD

curl -X GET http://$BACKUP_SERVICE_NODE:$BACKUP_SERVICE_PORT:8097/plan/$PLAN_NAME
  -u $USERNAME:$PASSWORD

## [](#required-permissions)Required Permissions

Full Admin, Backup Full Admin, or Read-Only Admin roles.

## [](#responses)Responses

| Value                                                                                 | Description                                                            |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 200 OK and JSON array containing plan information depending on the specific endpoint. | Successful call.                                                       |
| 400                                                                                   | Invalid parameter.                                                     |
| 401 Unauthorized                                                                      | Authorization failure due to incorrect username or password.           |
| 403 Forbidden, plus a JSON message explaining the minimum permissions.                | The provided username has insufficient privileges to call this method. |
| 404 Object Not found and the message {"status":404,"msg":"requested plan not found"}  | The plan in the endpoint URI does not exist.                           |
| 500 Could not retrieve the requested repository                                       | Error in Couchbase Server.                                             |

## [](#examples)Examples

The following call returns an array each of whose members is an object containing information for a plan currently defined for the cluster. The command pipes the output to the [jq](https://stedolan.github.io/jq) command to improve readability:

```console
curl -v -X GET http://127.0.0.1:8097/api/v1/api/v1/plan \
-u Administrator:password | jq '.'
```

If the call is successful, `200 OK` is returned, with an array the initial part of which may appear as follows:

```json
[
  {
    {
      "name": "HourlyBackupPlan",
      "description": "Backups occur every hour, with merge every four hours.",
      "services": [
        "data",
        "gsi"
      ],
      "tasks": [
        {
          "name": "HourlyBackupTask",
          "task_type": "BACKUP",
          "schedule": {
            "job_type": "BACKUP",
            "frequency": 1,
            "period": "HOURS",
            "time": "14:00"
          },
          "full_backup": false
        },
        {
          "name": "FourthHourMergeTask",
          "task_type": "MERGE",
          "schedule": {
            "job_type": "MERGE",
            "frequency": 4,
            "period": "HOURS",
            "time": "15:00"
          },
          "merge_options": {
            "offset_start": 0,
            "offset_end": 1
          },
          "full_backup": false
        }
      ]
    },
    {
      "name": "DailyPruningTask",
      "task_type": "PRUNE",
      "schedule": {
        "job_type": "PRUNE",
        "frequency": 1,
        "period": "DAYS",
        "time": "22:00"
      },
      "full_backup": false
    }
  }
  {...
  }
]
```

Each object in the array contains information on the specified plan. The information includes confirmation of the services for which data is backed up by the plan; and the tasks that are performed for the plan. Each task is listed with an account of its type and schedule.

The following call returns information specifically on the plan `PlanBackupMergePrune`:

```console
curl -v -X GET http://127.0.0.1:8091/_p/backup/api/v1/plan/PlanBackupMergePrune \
-u Administrator:password | jq '.'
```

If the call is successful, `200 OK` is returned, with the following object:

```json
{
  "name": "PlanBackupMergePrune",
  "services": [
    "data",
    "gsi"
  ],
  "tasks": [
    {
      "name": "TaskForBackup",
      "task_type": "BACKUP",
      "schedule": {
        "job_type": "BACKUP",
        "frequency": 1,
        "period": "HOURS",
        "time": "14:00"
      },
      "full_backup": true
    },
    {
      "name": "TaskForMerge",
      "task_type": "MERGE",
      "schedule": {
        "job_type": "MERGE",
        "frequency": 1,
        "period": "HOURS",
        "time": "14:30"
      },
      "merge_options": {
        "offset_start": 0,
        "offset_end": 3
      },
      "full_backup": false
    },
    {
      "name": "TaskForPrune",
      "task_type": "PRUNE",
      "schedule": {
        "job_type": "PRUNE",
        "frequency": 1,
        "period": "DAYS",
        "time": "22:00"
      },
      "full_backup": false
    }
  ]
}
```

The object contains information about the specified plan. The information includes confirmation of the services for which data is backed up by the plan; and the tasks that are performed for the plan. Each task is listed with an account of its type and schedule.

## [](#see-also)See Also

* For an overview of the Backup Service, see [Backup Service](../learn/services-and-indexes/services/backup-service.md).
* For a step-by-step guide to using Couchbase Server Web Console to configure and use the Backup Service, see [Manage Backup and Restore](../manage/manage-backup-and-restore/manage-backup-and-restore.md).
* For Information about using the Backup Service REST API to create a plan, see [Create and Edit Plans](backup-create-and-edit-plans.md).
* For information about deleting plans, see [Delete a Plan](backup-delete-plan.md).