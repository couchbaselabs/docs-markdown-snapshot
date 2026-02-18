---
title: Backup Service API
description: The Backup Service API allows full and incremental data-backups to
  be planned and scheduled; allows the scheduling of <em>merges</em> of
  previously made backups; and allows existing backups to be archived.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/backup-rest-api.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/rest-api/backup-rest-api.html)

# Backup Service API

> The Backup Service API allows full and incremental data-backups to be planned and scheduled; allows the scheduling of _merges_ of previously made backups; and allows existing backups to be archived. 

## [](#apis-in-this-section)APIs in this Section

The Backup Service API provides endpoints categorized as follows: _Cluster_, _Configuration_, _Repository_, _Plan_, _Task_, and _Data_. For a conceptual overview of the Backup Service, see [Backup Service](../learn/services-and-indexes/services/backup-service.md). For information on using Couchbase Web Console to configure and use the Backup Service, see [Manage Backup and Restore](../manage/manage-backup-and-restore/manage-backup-and-restore.md).

All calls require the Full Admin role, and use port `8097`. Each URI, in Couchbase Server Enterprise Edition Version 7.0, must be prefixed with `/api/v1`. Note that for all cluster references, in Couchbase Server Enterprise Edition Version 7.0 and 7.1, only the host cluster is supported, and is referred to as `self`.

For a list of the methods and URIs covered in these pages, see the tables below.

### [](#cluster)Cluster

| HTTP Method | URI           | Documented at                                                |
| ----------- | ------------- | ------------------------------------------------------------ |
| GET         | /cluster/self | [Get Information on the Cluster](backup-get-cluster-info.md) |

### [](#configuration)Configuration

| HTTP Method | URI     | Description                                            |
| ----------- | ------- | ------------------------------------------------------ |
| GET         | /config | [Manage Backup Configuration](backup-manage-config.md) |
| POST        | /config | [Manage Backup Configuration](backup-manage-config.md) |
| PUT         | /config | [Manage Backup Configuration](backup-manage-config.md) |

### [](#repository)Repository

| HTTP Method | URI                                                                                  | Documented at                                                    |
| ----------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| GET         | /cluster/self/repository/<'active'\|'archived'|'imported'>                           | [Get Information on Repositories](backup-get-repository-info.md) |
| GET         | /cluster/self/repository/active/<repository-id>                                      | [Get Information on Repositories](backup-get-repository-info.md) |
| GET         | /cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/info      | [Get Information on Repositories](backup-get-repository-info.md) |
| POST        | /cluster/self/repository/active/<repository-id>                                      | [Create a Repository](backup-create-repository.md)               |
| POST        | /cluster/self/repository/<'archived'\|'imported'>/<repository-id>/restore            | [Restore Data](backup-restore-data.md)                           |
| POST        | /cluster/self/repository/import                                                      | [Import a Repository](backup-import-repository.md)               |
| POST        | /cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/examine   | [Examine Backed-Up Data](backup-examine-data.md)                 |
| POST        | /cluster/self/repository/active/<repository-id>/backup                               | [Perform an Immediate Backup](backup-trigger-backup.md)          |
| POST        | /cluster/self/repository/active/<repository-id>/merge                                | [Perform an Immediate Merge](backup-trigger-merge.md)            |
| POST        | /cluster/self/repository/active/<repository-id>/archive                              | [Archive a Repository](backup-archive-a-repository.md)           |
| POST        | /cluster/self/repository/active/<repository-id>/pause                                | [Pause and Resume Tasks](backup-pause-and-resume-tasks.md)       |
| POST        | /cluster/self/repository/active/<repository-id>/resume                               | [Pause and Resume Tasks](backup-pause-and-resume-tasks.md)       |
| DELETE      | /cluster/self/repository/<'archived'\|'imported'>/<repository-id>                    | [Delete a Repository](backup-delete-repository.md)               |
| DELETE      | /cluster/self/repository/<'archived'\|'imported'>/<repository-id>?remove\_repository | [Delete a Repository](backup-delete-repository.md)               |
| DELETE      | /cluster/self/repository/active/<repository-id>/backups/<backup-id>                  | [Delete a Backup](backup-delete-backups.md)                      |

### [](#plan)Plan

| HTTP Method | URI                              | Documented at                                            |
| ----------- | -------------------------------- | -------------------------------------------------------- |
| GET         | /cluster/plan                    | [Get Information on Plans](backup-get-plan-info.md)      |
| GET         | /cluster/plan/<plan-id>          | [Get Information on Plans](backup-get-plan-info.md)      |
| POST        | /cluster/plan/<plan-id>          | [Create and Edit Plans](backup-create-and-edit-plans.md) |
| PUT         | /cluster/plan/<existing-plan-id> | [Create and Edit Plans](backup-create-and-edit-plans.md) |
| DELETE      | /plan/<plan-id>                  | [Delete a Plan](backup-delete-plan.md)                   |

### [](#task)Task

| HTTP Method | URI                                                                                                                       | Documented at                                       |
| ----------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| GET         | /cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/taskHistory                                    | [Get Information on Tasks](backup-get-task-info.md) |
| GET         | /cluster/self/repository/<'active'\|'archived'|'imported'>/<repository-id>/taskHistory?<task-subset-specification-string> | [Get Information on Tasks](backup-get-task-info.md) |

### [](#data)Data

| HTTP Method | URI                                                                 | Documented at                              |
| ----------- | ------------------------------------------------------------------- | ------------------------------------------ |
| DELETE      | /cluster/self/repository/active/<repository-id>/backups/<backup-id> | [Delete Backups](backup-delete-backups.md) |