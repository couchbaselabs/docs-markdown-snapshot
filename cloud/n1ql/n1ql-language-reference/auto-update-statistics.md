---
title: Auto Update Statistics
description: Auto Update Statistics (AUS) automatically refreshes optimizer
  statistics, ensuring accurate and cost-effective query plans.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/auto-update-statistics.adoc
  xref: xref:cloud:n1ql:n1ql-language-reference/auto-update-statistics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/auto-update-statistics.html)

# Auto Update Statistics

> Auto Update Statistics (AUS) automatically refreshes optimizer statistics, ensuring accurate and cost-effective query plans. 

## [](#overview)Overview

Auto Update Statistics (AUS) is a feature that keeps the optimizer statistics up to date by automatically identifying and refreshing outdated statistics.

Optimizer statistics are crucial as they help the [Cost Based Optimizer](cost-based-optimizer.md) generate optimal query plans. These statistics are initially created when you run the [UPDATE STATISTICS](updatestatistics.md) statement or build an index (available from 7.6.0 onward). However, as data changes over time, the statistics can become stale, leading to sub-optimal query plans and reduced query performance.

To handle this, AUS executes a scheduled task on each query node in the cluster. This task evaluates statistics based on expiration policies to identify outdated ones and then refreshes them by running the [UPDATE STATISTICS](updatestatistics.md) statement. AUS can also optionally generate statistics for indexed expressions that do not already have them.

> [!NOTE]
> AUS maintains statistics only for expressions on index keys, and only for those indexed using the Plasma storage engine. It does not support Memory-Optimized indexes. For more information about these index storage types, see [Index Storage Settings](../../indexes/storage-modes.md).

## [](#availability)Availability

AUS is available only in clusters running Couchbase Server version 8.0 or later.

* You can enable AUS in a cluster that has been fully migrated to 8.0, or in a cluster that includes both 7.6.x and 8.0 query nodes. In such mixed clusters, the 7.6.x query nodes will not perform any AUS tasks.
* For clusters migrating from pre-7.6.x versions (to a configuration described above), the AUS task can only be enabled once the automatic migration of optimizer statistics to the `_query` collection in the `_system` scope of the buckets has been completed.

## [](#how-aus-works)How AUS Works

AUS is an opt-in feature that you must explicitly enable and schedule. Once it's enabled and a schedule is set, all query nodes in the cluster participate in AUS, according to the same schedule.

### [](#aus-task-execution)AUS Task Execution

Each node receives its own AUS task, which performs the following actions during its scheduled window:

* The query node first selects specific collections for AUS processing, ensuring that no other query node updates the same collection during this period.
* Each selected collection then goes through two phases: [Evaluation](#evaluation%5Fphase) and [Update](#update%5Fphase). These phases process statistics gathered from expressions based on fields within that collection.
* After AUS completes processing all statistics in all buckets, the query node schedules the next AUS run.
* If the scheduled window ends before the AUS task finishes, the task is aborted and the next AUS run is scheduled.

![AUS process flow showing the evaluation and update phases](../_images/aus-process-47a555a3e50d0b5917f28d716cc4efe783f36994.svg) 

Figure 1\. AUS process flow showing the evaluation and update phases

### [](#evaluation-phase)Evaluation Phase

In this phase, AUS evaluates whether existing statistics are stale based on the [expiration policy](#expiration%5Fpolicy). For each index, AUS assess how much data has changed since the last update of the optimizer statistics for the index's key expressions. If the percentage of change exceeds the defined threshold in the [expiration policy](#expiration%5Fpolicy), the statistics are marked as stale.

Additionally, if configured to do so, this phase also identifies any indexed expressions that currently lack statistics and flags them for creation. You can control this setting using the `create_missing_statistics` attribute in the [system:aus](#system%5Faus) catalog.

### [](#update-phase)Update Phase

After the evaluation, AUS executes [UPDATE STATISTICS](updatestatistics.md) statements to refresh the statistics identified as stale. When updating the existing statistics, AUS ensures that the refreshed statistics maintain the original [resolution](cost-based-optimizer.md#resolution) at which they were collected.

Also, if the `create_missing_statistics` option is set to `true`, AUS creates new optimizer statistics for indexed expressions that were flagged as missing during the evaluation phase. The new statistics are created with the default [resolution](cost-based-optimizer.md#resolution).

> [!IMPORTANT]
> When AUS is first enabled, the initial task run might update all existing optimizer statistics, regardless of the expiration policy evaluation. This is because the index change information might not have been recorded prior to this first run.

### [](#expiration%5Fpolicy)Expiration Policy

AUS uses expiration policies to determine when statistics are outdated and require an update. The policy is based on the percentage of changes to data within an index. You can configure this value using the `change_percentage` attribute in the [system:aus](#system%5Faus) or [system:aus\_settings](#system%5Faus%5Fsettings) catalogs. It defines how much data in an index must change before the statistics are considered outdated.

If the percentage of changed data since the last statistics collection exceeds the defined threshold, AUS flags the statistics as stale. The subsequent AUS operation then updates these statistics.

## [](#enable-and-schedule-aus)Enable and Schedule AUS

To start using AUS for your cluster, you need to enable it and configure a schedule. You can configure AUS to run during off-peak hours or at specific times that align with your workload patterns.

AUS maintains its global configurations in the [system:aus](#system%5Faus) catalog. You can enable AUS and set its schedule by modifying the relevant configurations within this catalog.

If you need more granular control, use the [system:aus\_settings](#system%5Faus%5Fsettings) catalog to customize certain AUS configurations at the bucket, scope, and collection levels.

For a historical record of recent AUS tasks across all query nodes, use the [system:tasks\_cache](../n1ql-intro/sysinfo.md#sys-tasks-cache) catalog. For more information, see [Monitor AUS Tasks](#monitor%5Faus%5Ftasks).

### [](#system%5Faus)system:aus

The `system:aus` catalog contains a single document that holds all the global configurations of AUS. You can update this document to modify the settings.

> [!NOTE]
> * Only SELECT and UPDATE DMLs are allowed on this keyspace.
> * To execute SELECT on `system:aus`, you need the `query_system_catalog` role.
> * To execute UPDATE on `system:aus`, you need the `query_manage_system_catalog` role.

Each attribute in the document represents a particular global configuration. The following are the attribute names and the configurations they represent:

| Name                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                      | Schema                             |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **enable** _required_                      | Indicates whether AUS is enabled for the cluster or not. To enable AUS, set this attribute to true.If set to true, then the schedule attribute must also be set. **Default:** false                                                                                                                                                                                                                                              | Boolean                            |
| **schedule** _optional_                    | Defines the schedule for AUS operations. This attribute is required only if enable is set to true.                                                                                                                                                                                                                                                                                                                               | [Schedule](#aus%5Fschedule) object |
| **change\_percentage** _required_          | The percentage of change to items within an index that must be exceeded for the statistics to be refreshed. This is the threshold for determining whether the statistics are stale or not. The value must be an integer between 0 and 100. For example, a value of 30 means that if 30% or more of the items in an index have changed, the statistics for that index are considered stale and will be refreshed. **Default:** 10 | Integer                            |
| **all\_buckets** _required_                | Indicates whether AUS should be performed on all buckets or only those buckets whose metadata information is loaded on the query node. **Default:** false                                                                                                                                                                                                                                                                        | Boolean                            |
| **create\_missing\_statistics** _required_ | Indicates whether AUS should create statistics that are missing. If set to true, AUS creates statistics for indexed expressions that do not have any existing statistics. The statistics will be created using the default value for the [resolution](cost-based-optimizer.md#resolution) property. **Default:** false                                                                                                           | Boolean                            |

#### [](#aus%5Fschedule)Schedule

| Name                       | Description                                                                                                                                                                                         | Schema       |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **start\_time** _required_ | The start time of the AUS schedule in "HH:MM" format. The start\_time must be at least 30 minutes earlier than the end\_time. **Example:** "01:30"                                                  | String       |
| **end\_time** _required_   | The end time of the AUS schedule in "HH:MM" format. The end\_time must be at least 30 minutes later than the start\_time. **Example:** "05:30"                                                      | String       |
| **days** _required_        | An array of strings specifying the days on which the AUS schedule runs. Valid values include: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. **Example:** \["Saturday", "Sunday"\] | String array |
| **timezone** _optional_    | The timezone that applies to the schedule's start and end times. The value must be a valid IANA timezone string. **Default:** "UTC" **Example:** "US/Pacific"                                       | String       |

When changing the global configurations, it is important to consider the following:

* **Enabling AUS**: If AUS was previously disabled and is now enabled, the next AUS task will be scheduled immediately.
* **Rescheduling AUS**: Currently scheduled AUS task will be cancelled, and a new AUS task will be scheduled according to the updated schedule. Running AUS tasks will not be cancelled.
* **Other Settings**: If other global settings such as `all_buckets` or `change_percentage` are modified, the new values will be applied during the next scheduled AUS run.

#### [](#example)Example

A sample UPDATE statement to enable AUS and set a schedule with some customizations:

Query

```sqlpp
UPDATE system:aus SET enable = true, change_percentage = 20,
schedule = { "start_time": "01:30",
             "end_time": "04:30",
             "timezone": "Asia/Calcutta",
             "days": ["Monday", "Friday"]
        };
```

### [](#system%5Faus%5Fsettings)system:aus\_settings

The `system:aus_settings` catalog stores granular configuration settings for AUS. These settings can be applied at the bucket, scope, and collection levels.

By default, this catalog has no documents, and the AUS settings for all keyspaces inherit the configurations defined at the global level. In other words, unless you explicitly configure AUS for a specific keyspace, it will use the global AUS settings defined in [system:aus](#system%5Faus).

To customize AUS for a specific keyspace, you must insert a settings document into the `system:aus_settings` catalog. The document ID of a document in this keyspace must be the full path of the bucket, scope, and collection.

Each attribute in the document represents a particular granular configuration. The following are the attribute names and the configurations they represent:

| Name                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Schema  |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **enable** _optional_                      | Indicates whether AUS is enabled for the bucket, scope, collection.Set it to true to enable AUS for the keyspace. AUS settings are hierarchical and follow the order: cluster > bucket > scope > collection.If AUS is disabled at higher level, it cannot be enabled at a more granular level. However, if AUS is enabled at a higher level, it can be disabled at a more granular level. For example, If AUS is disabled for a bucket, it is automatically disabled for all scopes and collections within it. The setting cannot be overridden at the scope or collection level. If AUS is enabled for a bucket, it can be overridden at the scope and collection level.                                                           | Boolean |
| **change\_percentage** _optional_          | The percentage of change to items within an index that must be exceeded for the statistics to be refreshed. The value must be an integer between 0 and 100. If set at a bucket level, this value applies to all scopes and collections within the bucket, unless overridden at a lower level. If set at a scope level, this value applies to all collections within the scope, unless overridden at a lower level. **Example:** 30                                                                                                                                                                                                                                                                                                  | Integer |
| **update\_statistics\_timeout** _optional_ | The timeout period for the [UPDATE STATISTICS](updatestatistics.md) command. It's a number representing a duration in seconds. If the command does not complete within this duration, it times out. If omitted, a default timeout value is calculated based on the number of samples used. If set for a keyspace, this timeout applies to every [UPDATE STATISTICS](updatestatistics.md) statement that AUS executes for that keyspace. If set at a bucket level, this timeout applies to all scopes and collections within the bucket, unless a different value is set at a lower level. If set at a scope level, this timeout applies to all collections within the scope, unless a different value is set at a collection level. | Number  |

> [!NOTE]
> * All SQL++ DMLs are allowed on this keyspace.
> * To execute SELECT on `system:aus_settings`, you need the `query_system_catalog` role.
> * To execute UPDATE, DELETE, INSERT, and UPSERT on `system:aus_settings`, you need the `query_manage_system_catalog` role.

#### [](#example-2)Example

A sample query to add a scope level setting that applies to all collections within the scope.

Query

```sqlpp
INSERT INTO system:aus_settings ( KEY, VALUE )
    VALUES ( "default:bucket1.scope1", {"change_percentage": 20} );
```

## [](#monitor%5Faus%5Ftasks)Monitor AUS Tasks

The `system:tasks_cache` catalog stores information about all recent tasks executed in a cluster, including the AUS tasks. For each AUS task, every involved query node maintains an entry within this catalog. AUS task entries can be specifically identified by the `class` field, which is set to `auto_update_statistics`.

### [](#view%5Faus%5Ftasks)View Recent AUS Tasks

To view all recent AUS tasks, use the following query:

```sqlpp
SELECT * FROM system:tasks_cache WHERE class = "auto_update_statistics";
```

This query returns all AUS entries regardless of their state (scheduled, running, completed, etc.). To get the details of completed tasks, see [View Completed AUS Tasks](#view%5Fcompleted%5Faus%5Ftasks).

### [](#find-scheduled-aus-tasks)Find Scheduled AUS Tasks

To identify AUS tasks that are scheduled to run, you can filter the entries using the `state` attribute.

```sqlpp
SELECT * FROM system:tasks_cache WHERE class = "auto_update_statistics" AND state = "scheduled";
```

### [](#view-aus-tasks-on-a-particular-node)View AUS Tasks on a Particular Node

To view recent AUS tasks on a particular node, filter by the `node` attribute.

```sqlpp
SELECT * FROM system:tasks_cache WHERE class = "auto_update_statistics"
         AND state = "scheduled"
         AND node = "127.0.0.1:8091"; // Replace with the actual node address
```

### [](#view%5Fcompleted%5Faus%5Ftasks)View Completed AUS Tasks

The entries for completed AUS tasks have information specifically about tasks that have finished execution. These entries include details such as the task ID, start time, end time, which keyspaces had their statistics updated, and whether any errors occurred during the task execution.

#### [](#example-3)Example

A sample task entry for a successful AUS task on a query node:

```json
{
    "tasks_cache": {
        "class": "auto_update_statistics",
        "delay": "21.707164s",
        "id": "4b90bb39-ca1b-55f1-84f0-4d3137c88bf8",
        "name": "bc1ab6e9-9f33-4a8f-86ad-40d74c50af5f",
        "queryContext": "",
        "results": {
            "configuration": {
                "all_buckets": true,
                "change_percentage": 20,
                "end_time": "2024-11-19 20:00:00 +0530 IST",
                "internal_version": 1,
                "start_time": "2024-11-19 19:16:00 +0530 IST"
            },

            "keyspaces_updated": [
                "default:bucket1.scope1.customers"
            ]
        },

        "startTime": "2024-11-19T19:16:00.001+05:30",
        "state": "completed",
        "stopTime": "2024-11-19T19:16:03.154+05:30",
        "subClass": "",
        "submitTime": "2024-11-19T19:15:38.292+05:30"
    }
}
```

For more information about `system:tasks_cache` and its attributes, see [Monitor Cached Tasks](../n1ql-intro/sysinfo.md#sys-tasks-cache).

In addition to the attributes listed there, the AUS task entries also include the following attributes:

* `keyspaces_updated`: A list of keyspaces that had their statistics updated during the AUS task execution.
* `configuration`: The configuration with which the AUS task was executed.

> [!NOTE]
> You can also retrieve the AUS task history from the `query.log`.

## [](#cancel-aus-tasks)Cancel AUS Tasks

You can cancel AUS tasks that are currently running or scheduled to run.

* [Cancel Running AUS Tasks](#cancel%5Frunning%5Faus%5Ftasks)
* [Cancel Next Scheduled AUS Tasks](#cancel%5Fnext%5Fscheduled%5Faus%5Ftasks)

> [!CAUTION]
> When cancelling AUS tasks, it's important to include appropriate WHERE clauses to specify exactly which tasks you want to cancel. Make sure your filters target only the intended tasks, otherwise they might inadvertently cancel other tasks or delete task history.

### [](#cancel%5Frunning%5Faus%5Ftasks)Cancel Running AUS Tasks

To cancel a running AUS task, delete its entry from the `system:tasks_cache` catalog. When you delete a task that's in the `scheduled` or `running` state, AUS cancels the task and schedules the next one automatically.

To cancel all running AUS tasks, use the following DELETE statement:

```sqlpp
DELETE FROM system:tasks_cache WHERE class = "auto_update_statistics" AND state = "running";
```

To cancel a running AUS task on a specific node, include the node's address in the WHERE clause:

```sqlpp
DELETE FROM system:tasks_cache
        WHERE class = "auto_update_statistics"
        AND state = "running"
        AND node = "127.0.0.1:8091"; // Replace with the actual node address
```

### [](#cancel%5Fnext%5Fscheduled%5Faus%5Ftasks)Cancel Next Scheduled AUS Tasks

To cancel an upcoming scheduled AUS task, you need to temporarily modify its schedule in the `system:aus` catalog. After the scheduled time has passed, you can revert it to its original schedule.

#### [](#temporarily-update-the-schedule)Temporarily Update the Schedule

First, identify the specific AUS task you want to skip or cancel. Then, use an UPDATE statement to exclude the day or time from its schedule.

For example, if your AUS tasks run on Monday, Wednesday, and Friday, and you want to cancel the upcoming Monday run:

```sqlpp
UPDATE system:aus SET schedule.days = ["Wednesday", "Friday"];
```

#### [](#revert-the-schedule)Revert the Schedule

After the day and time for the cancelled task have passed, you can revert the schedule to its original settings. This allows your AUS tasks to resume their regular schedule for all subsequent runs.

For example, to restore the Monday, Wednesday, and Friday schedule after skipping the Monday run:

```sqlpp
UPDATE system:aus SET schedule.days = ["Monday", "Wednesday", "Friday"];
```

## [](#manage-aus-load)Manage AUS Load

When an AUS task runs, it can increase the load on the query node as it evaluates and updates statistics. Therefore, to minimize performance impact, it's important to schedule AUS to best suit the workloads of your cluster.

To prevent excessive load, the AUS task will not start if the query node's load is too high during the scheduled window. In such cases, the task is skipped, and the next AUS task is scheduled.

## [](#related-links)Related Links

* [Cost Based Optimizer](cost-based-optimizer.md)
* [UPDATE STATISTICS](updatestatistics.md)
* [System Catalogs](../n1ql-intro/sysinfo.md)