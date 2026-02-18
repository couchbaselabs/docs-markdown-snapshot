---
title: Backup Service API
description: The Backup Service API allows full and incremental data-backups to
  be planned and scheduled; allows the scheduling of <em>merges</em> of
  previously made backups; and allows existing backups to be archived.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/backup-rest-api.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/rest-api/backup-rest-api.html)

# Backup Service API

> The Backup Service API allows full and incremental data-backups to be planned and scheduled; allows the scheduling of _merges_ of previously made backups; and allows existing backups to be archived. 

## [](#apis-in-this-section)APIs in this Section

The Backup Service API endpoints can be grouped into several categories:

* [Cluster](#cluster)
* [Configuration](#configuration)
* [Repository](#repository)
* [Plan](#plan)
* [Task](#task)
* [Data](#data)

For an overview of the Backup Service, see [Backup Service](../learn/services-and-indexes/services/backup-service.md). For information on using Couchbase Server Web Console to configure and use the Backup Service, see [Manage Backup and Restore](../manage/manage-backup-and-restore/manage-backup-and-restore.md).

All calls require the Full Admin role, and use port `8097`. Each URI, in Couchbase Server Enterprise Edition Version 7.0, must be prefixed with `/api/v1`. Note that for all cluster references, in Couchbase Server Enterprise Edition Version 7.0 and 7.1, only the host cluster is supported, and is referred to as `self`.

For a list of the methods and URIs covered in these pages, see the tables below.

### [](#cluster)Cluster

| HTTP Method | URI                  | Documented at                                                |
| ----------- | -------------------- | ------------------------------------------------------------ |
| GET         | /api/v1/cluster/self | [Get Information on the Cluster](backup-get-cluster-info.md) |

### [](#configuration)Configuration

| HTTP Method | URI                     | Description                                             |
| ----------- | ----------------------- | ------------------------------------------------------- |
| GET         | /api/v1/config          | [Manage Backup Configuration](backup-manage-config.md)  |
| POST        | /api/v1/config          | [Manage Backup Configuration](backup-manage-config.md)  |
| PUT         | /api/v1/config          | [Manage Backup Configuration](backup-manage-config.md)  |
| GET         | /api/v1/nodesThreadsMap | [Manage Backup Service Threads](backup-node-threads.md) |
| PATCH       | /api/v1/nodesThreadsMap | [Manage Backup Service Threads](backup-node-threads.md) |
| POST        | /api/v1/nodesThreadsMap | [Manage Backup Service Threads](backup-node-threads.md) |

### [](#repository)Repository

| HTTP Method | URI                                                                                         | Documented at                                                      |
| ----------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| GET         | /api/v1/cluster/self/repository/<'active'\|'archived'|'imported'>                           | [Get Backup Repository Information](backup-get-repository-info.md) |
| GET         | /api/v1/cluster/self/repository/active/<repository-id>                                      | [Get Backup Repository Information](backup-get-repository-info.md) |
| GET         | /api/v1/cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/info      | [Get Backup Repository Information](backup-get-repository-info.md) |
| POST        | /api/v1/cluster/self/repository/active/<repository-id>                                      | [Create a Repository](backup-create-repository.md)                 |
| POST        | /api/v1/cluster/self/repository/<'archived'\|'imported'>/<repository-id>/restore            | [Restore Data](backup-restore-data.md)                             |
| POST        | /api/v1/cluster/self/repository/import                                                      | [Import a Repository](backup-import-repository.md)                 |
| POST        | /api/v1/cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/examine   | [Examine Backed-Up Data](backup-examine-data.md)                   |
| POST        | /api/v1/cluster/self/repository/active/<repository-id>/backup                               | [Perform an Immediate Backup](backup-trigger-backup.md)            |
| POST        | /api/v1/cluster/self/repository/active/<repository-id>/merge                                | [Perform an Immediate Merge](backup-trigger-merge.md)              |
| POST        | /api/v1/cluster/self/repository/active/<repository-id>/archive                              | [Archive a Repository](backup-archive-a-repository.md)             |
| POST        | /api/v1/cluster/self/repository/active/<repository-id>/pause                                | [Pause and Resume Tasks](backup-pause-and-resume-tasks.md)         |
| POST        | /api/v1/cluster/self/repository/active/<repository-id>/resume                               | [Pause and Resume Tasks](backup-pause-and-resume-tasks.md)         |
| DELETE      | /api/v1/cluster/self/repository/<'archived'\|'imported'>/<repository-id>                    | [Delete a Repository](backup-delete-repository.md)                 |
| DELETE      | /api/v1/cluster/self/repository/<'archived'\|'imported'>/<repository-id>?remove\_repository | [Delete a Repository](backup-delete-repository.md)                 |
| DELETE      | /api/v1/cluster/self/repository/active/<repository-id>/backups/<backup-id>                  | [Delete a Backup](backup-delete-backups.md)                        |

### [](#plan)Plan

| HTTP Method | URI                                     | Documented at                                            |
| ----------- | --------------------------------------- | -------------------------------------------------------- |
| GET         | /api/v1/cluster/plan                    | [Get Backup Plan Information](backup-get-plan-info.md)   |
| GET         | /api/v1/cluster/plan/<plan-id>          | [Get Backup Plan Information](backup-get-plan-info.md)   |
| POST        | /api/v1/cluster/plan/<plan-id>          | [Create and Edit Plans](backup-create-and-edit-plans.md) |
| PUT         | /api/v1/cluster/plan/<existing-plan-id> | [Create and Edit Plans](backup-create-and-edit-plans.md) |
| DELETE      | /api/v1/plan/<plan-id>                  | [Delete a Plan](backup-delete-plan.md)                   |

### [](#task)Task

| HTTP Method | URI                                                                                                                              | Documented at                                      |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| GET         | /api/v1/cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/taskHistory                                    | [Get Backup Task History](backup-get-task-info.md) |
| GET         | /api/v1/cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/taskHistory?<task-subset-specification-string> | [Get Backup Task History](backup-get-task-info.md) |

### [](#data)Data

| HTTP Method | URI                                                                        | Documented at                              |
| ----------- | -------------------------------------------------------------------------- | ------------------------------------------ |
| DELETE      | /api/v1/cluster/self/repository/active/<repository-id>/backups/<backup-id> | [Delete Backups](backup-delete-backups.md) |