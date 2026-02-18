---
title: Delete a Plan
description: The Backup Service API allows plans to be deleted.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/backup-delete-plan.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/rest-api/backup-delete-plan.html)

# Delete a Plan

> The Backup Service API allows plans to be deleted. 

## [](#http-methods-and-uris)HTTP Method and URI

DELETE /plan/<plan-id>

## [](#description)Description

Deletes a specified plan. Note that the plan cannot be currently in use by any repository.

## [](#curl-syntax)Curl Syntax

curl -X DELETE http://<backup-node-ip-address-or-domain-name>:8097/plan/<plan-id>
  -u <username>:<password>

The `plan-id` must be the id of a plan currently defined on the cluster. The `username` and `password` must identify an administrator with the Full Admin role.

## [](#responses)Responses

Success returns `200 OK`. If the specified plan cannot be found, or if the URI is otherwise incorrectly specified, `404 Object Not Found` is returned. If the specified plan is currently in use by one or more repositories, `400 Bad Request` is returned, with a message such as the following: `{"status":400,"msg":"cannot update plan as it is in use by repository: hourlyBackupRepo"}`. If an internal server error prevents deletion of the plan, `500 Internal Server Error` is returned.

Failure to authenticate returns `401 Unauthorized`.

## [](#examples)Examples

The following call deletes a plan named `testPlan2`, which is currently used by no repository.

curl -v -X DELETE http://127.0.0.1:8097/api/v1/plan/testPlan2 \
-u Administrator:password

Success returns `200 OK`.

## [](#see-also)See Also

An overview of the Backup Service is provided in [Backup Service](../learn/services-and-indexes/services/backup-service.md). A step-by-step guide to using Couchbase Web Console to configure and use the Backup Service is provided in [Manage Backup and Restore](../manage/manage-backup-and-restore/manage-backup-and-restore.md). For information on creating plans, see [Create and Edit Plans](backup-create-and-edit-plans.md).