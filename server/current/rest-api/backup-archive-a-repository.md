---
title: Archive a Repository
description: The Backup Service REST API supports the archiving of currently
  active repositories.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/backup-archive-a-repository.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/rest-api/backup-archive-a-repository.html)

# Archive a Repository

> The Backup Service REST API supports the archiving of currently active repositories. 

## [](#http-methods-and-uris)HTTP Method and URI

POST /repository/active/<repository-id>/archive

## [](#description)Description

Archives the specified repository. This means that no further scheduled or manually triggered tasks can be run on the repository; with the exception of those that _retrieve information_, _restore data_, and _examine data_. (See [Get Backup Repository Information](backup-get-repository-info.md), [Restore Data](backup-restore-data.md), and [Examine Backed-Up Data](backup-examine-data.md), respectively.)

Note that a repository that has been archived _cannot_ be returned to active state.

## [](#curl-syntax)Curl Syntax

curl -X POST http://<backup-node-ip-address-or-domain-name>:8097/api/v1/cluster/self/\
  repository/active/<repository-id>/archive
  -d <repository-id-specification>
  -u Administrator:password

The `username` and `password` must identify an administrator with the Full Admin role. The `repository-id` argument must specify the name of an active repository defined on the cluster. Additionally, a `respository-id-specification` must be provided, as a JSON payload; whose syntax is as follows:

{
  "id":<archived-repository-id>
}

The `archived-repository-id` is the name that the repository is to bear, once it has been archived.

## [](#responses)Responses

Success returns `200 OK`.

Incorrect specification of the `repository-id` path-parameter returns `404 Object Not Found`, and a message such as the following: `{"status":404,"msg":"could not find active repository with id:quickRepo"}`. An otherwise incorrectly specified URI alsp returns `404 Object Not Found`.

Incorrect specification, within the JSON payload, of the repository id returns `400 Bad Request`, and a message such as the following: `{"status":400,"msg":"repository id must follow the rules ^[0-9A-Za-z][0-9A-Za-z_-]{0,49}$"}`.

Failure to authenticate returns `401 Unauthorized`.

## [](#examples)Examples

The following example archives the currently active repository `quickRepo`:

curl -v -X POST  http://127.0.0.1:8097/api/v1/cluster/self/\
repository/active/quickRepo/archive \
--data '{"id": "quickRepo"}' \
-u   -u <username>:<password>

Successful execution returns `200 OK`.

## [](#see-also)See Also

An overview of the Backup Service is provided in [Backup Service](../learn/services-and-indexes/services/backup-service.md). A step-by-step guide to using Couchbase Web Console to configure and use the Backup Service is provided in [Manage Backup and Restore](../manage/manage-backup-and-restore/manage-backup-and-restore.md).

Information on getting information from an archived repository is provided in [Get Backup Repository Information](backup-get-repository-info.md). Information on restoring data from an archived repository is provided in [Restore Data](backup-restore-data.md). Information on examining data within an archived repository is provided in [Examine Backed-Up Data](backup-examine-data.md).