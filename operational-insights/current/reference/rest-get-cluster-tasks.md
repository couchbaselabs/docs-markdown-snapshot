---
title: Getting Cluster Tasks
description: You can list tasks running on the cluster using the <code>GET
  /pools/default/tasks</code> HTTP method and URI.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-get-cluster-tasks.adoc
  xref: xref:enterprise-analytics:reference:rest-get-cluster-tasks.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-get-cluster-tasks.html)

# Getting Cluster Tasks

> You can list tasks running on the cluster using the `GET /pools/default/tasks` HTTP method and URI. In addition, a report on the last-completed rebalance can be returned with `GET /logs/rebalanceReport?reportID=REPORT_ID`. 

## [](#http-method-and-uri)HTTP Methods and URIs

GET /pools/default/tasks

GET /pools/default/tasks?taskId=TASK_ID

GET /logs/rebalanceReport?reportID=REPORT_ID

## [](#rest-get-cluster-tasks-description)Description

Calling `GET /pools/default/tasks` lists tasks running on the cluster. The list includes the task's ID, status, and other relevant informaatiom. You can return information about a specific task by supplying its `taskId` as a parameter: `GET /pools/default/tasks?taskID=TASK_ID`.

Calling `GET /logs/rebalanceReport?reportID=REPORT_ID`, a report can be returned, providing information about a completed _rebalance_. The required `report-id` is provided in the object returned by `GET /pools/default/tasks`.

## [](#curl-syntax)Curl Syntax

curl -s -u USER_NAME:PASSWORD -G \
     http://NODE_NAME_OR_ADDRESS:PORT/pools/default/tasks \
     -d "taskId=TASK_ID"


curl -s -u USER_NAME:PASSWORD -G
     http://NODE_NAME_OR_ADDRESS:PORT/logs/rebalanceReport
     -d "reportID=REPORT_ID"

The arguments shown in the syntax are:

* **`USER_NAME`**: the username to use when connecting to Operational Insights.
* **`PASSWORD`**: the password for the user.
* **`NODE_NAME_OR_ADDRESS`**: the name or IP address of a node in the cluster.
* **`TASK_ID`**: the optional ID of a task whose status you want to view. If you do not provide a task ID, the call returns all tasks on the cluster.
* **`REPORT_ID`**: the required rebalance report ID. You can find this ID from the rebalance task's `lastReportURI` field in the task list returned by calling `GET /pools/default/tasks` without parameters.

## [](#responses)Responses

A successful call to `GET /pools/default/tasks` returns the response code `200 OK` and an object containing details about a specific task when you supply a `taskId` argument. If you do not supply the `taskId` argument, it returns an object containing information about all tasks.

A successful call to `GET /logs/rebalanceReport?reportID=REPORT_ID` returns response code `200 OK` and an object containing a report on the rebalance whose `reportID` matches `REPORT_ID`. If you pass Operational Insights a `reportID` that it cannot find, it returns the response code `200 OK` and an object containing the following error:

{
  "error": "enoent"
}

Passing a `reportID` of incorrect length returns `400 Bad Request` and an object with the following error message:

{
  "errors": {
    "reportID": "Length must be in range from 32 to 32"
  }
}

For both endpoints, failure to authenticate returns the response `401 Unauthorized`.

## [](#examples)Examples: Retrieving Cluster Tasks

The following examples demonstrate using the `/pools/default/tasks` and `/logs/rebalanceReport` endpoints.

### [](#no-tasks-underway)No Tasks Running

When the cluster has no tasks running, calling the `/pools/default/tasks` method returns just the most recent rebalance task:

curl -u Administrator:password -v -X GET \
     http://10.143.194.101:8091/pools/default/tasks | jq '.'

Output is piped through the [jq](https://jqlang.org/) tool to enhance readability and appears as the following:

[
  {
    "statusId": "28452d665fce646c98385fb590a30adc",
    "type": "rebalance",
    "status": "notRunning",
    "statusIsStale": false,
    "masterRequestTimedOut": false,
    "lastReportURI": "/logs/rebalanceReport?reportID=0c41dba637a8971b1aa921a89e851d83"
  }
]

The default output indicates that no rebalance is underway. A `statusId` and task `type` are provided. The `lastReportURI` specifies the location of the report of the last rebalance to have been performed. See the [Rebalance Reference](rebalance-reference.md), for further information.

For an example of the task that is listed while logs are being collected, see [Collecting Logs](rest-manage-log-collection.md#examples).

### [](#rebalance-following-node-addition)Rebalance Following Node-Addition

When rebalance is used to eject node `10.143.194.103` from a cluster of three nodes, which has included `10.143.194.101` and `10.143.194.102` in addition to itself, the progress of the task can be retrieved as follows:

curl -u Administrator:password -v -X GET \
http://10.143.194.101:8091/pools/default/tasks | jq '.'

Depending on at what point in the rebalance the method is run, the output might be as follows (abbreviated):

[
  {
    "statusId": "1a51786a937213ac456d2f066f65c08a",
    "type": "rebalance",
    "subtype": "rebalance",
    "recommendedRefreshPeriod": 0.25,
    "status": "running",
    "progress": 1.531444089632196,
    "perNode": {
      "ns_1@10.143.194.101": {
        "progress": 0.9765625
      },
      "ns_1@10.143.194.102": {
        "progress": 0.9784735812133072
      },
      "ns_1@10.143.194.103": {
        "progress": 2.639296187683282
      }
    },
    "rebalanceId": "b9a087fb3533d6ada22a1c43d8d09e24",
    "nodesInfo": {
      "active_nodes": [
        "ns_1@10.143.194.101",
        "ns_1@10.143.194.102",
        "ns_1@10.143.194.103"
      ],
      "keep_nodes": [
        "ns_1@10.143.194.101",
        "ns_1@10.143.194.102"
      ],
      "eject_nodes": [
        "ns_1@10.143.194.103"
      ],
      "delta_nodes": [],
      "failed_nodes": []
    },
    "masterNode": "ns_1@10.143.194.102"
  }
]

Note that the contents of the object differ significantly, once rebalance is in progress.

The response object provides a `statusId` that now corresponds to the ongoing `rebalance` operation. The value of `progress` is the value as it was at the time of running the method. A progress value is also given `perNode`: each value is a percentage — note that these percentages are displayed by the Operational Insights Web Console, when it is itself used to monitor rebalance. All progress values are represented as floating-point numbers with fourteen places.

The full object also contains a `stageInfo` object, which provides information about the stages of the rebalance. A complete description of the fields is provided in the [Rebalance Reference](rebalance-reference.md).

Note that a `recommendedRefreshPeriod` of `0.25` seconds is given. If the same method is entered subsequently, output indicates that progress has continued:

[
  {
    "statusId": "1a51786a937213ac456d2f066f65c08a",
    "type": "rebalance",
    "subtype": "rebalance",
    "recommendedRefreshPeriod": 0.25,
    "status": "running",
    "progress": 60.58881772169409,
    "perNode": {
      "ns_1@10.143.194.101": {
        "progress": 58.69140625
      },
      "ns_1@10.143.194.102": {
        "progress": 55.77299412915851
      },
      "ns_1@10.143.194.103": {
        "progress": 67.30205278592376
      }
    },
    "rebalanceId": "b9a087fb3533d6ada22a1c43d8d09e24",
    "nodesInfo": {
      "active_nodes": [
        "ns_1@10.143.194.101",
        "ns_1@10.143.194.102",
        "ns_1@10.143.194.103"
      ],
      "keep_nodes": [
        "ns_1@10.143.194.101",
        "ns_1@10.143.194.102"
      ],
      "eject_nodes": [
        "ns_1@10.143.194.103"
      ],
      "delta_nodes": [],
      "failed_nodes": []
    },
    "masterNode": "ns_1@10.143.194.102"
  }
]

The `lastReportURI` corresponding to the rebalance that has been performed must be retrieved by means of a subsequent call, once rebalance has concluded. This is described immediately below.

## [](#getting-a-rebalance-report)Example: Getting a Rebalance Report

A rebalance report can be retrieved by means of the URI specified as the value of `lastReportURI`. For example:

curl -u Administrator:password -v -X \
GET http://10.143.194.102:8091/logs/rebalanceReport?reportID=f95697f13542aaffb9058cb1920b13c7 | jq

If successful, the content of the report is returned, and printed to standard output. The initial section might appear as follows:

{
  "stageInfo": {
    "data": {
      "totalProgress": 100,
      "perNodeProgress": {
        "ns_1@10.143.194.101": 1,
        "ns_1@10.143.194.102": 1,
        "ns_1@10.143.194.103": 1
      },
      "startTime": "2020-03-16T04:49:22.624-07:00",
      "completedTime": "2020-03-16T04:52:13.380-07:00",
      "timeTaken": 170757,
          .
          .
          .

A complete description of the fields in the `stageInfo` object is provided the in [Rebalance Reference](rebalance-reference.md).

### [](#rebalance-failure)Rebalance Failure

If rebalance fails, the method can be used to retrieve the following confirmation of failure:

[
  {
    "statusId": "1f05321a7b359e1743ffc8b7ee69a8b9",
    "type": "rebalance",
    "status": "notRunning",
    "errorMessage": "Rebalance failed. See logs for detailed reason. You can try rebalance again."
  }
]

## [](#see-also)See Also

Examples of adding a node and rebalancing by means of the UI, CLI, and REST API are provided in [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md). The REST method and URI for rebalance is explained in [Rebalancing the Cluster](rest-cluster-rebalance.md).

For additional information about retrieving the progress of the rebalance operation, see [Getting Rebalance Progress](rest-get-rebalance-progress.md). See the [Rebalance Reference](rebalance-reference.md), for detailed information about downloading and reading rebalance reports.