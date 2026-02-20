---
title: Set Data Disk Use Limits
description: You can have the Data Service stop writing to the data storage path
  when it fills to a specific percentage. This option helps prevent the data
  path from running out of disk space and making recovery difficult.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/disk-usage-limits.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:rest-api:disk-usage-limits.adoc[]
---

[View original HTML](/server/current/rest-api/disk-usage-limits.html)

# Set Data Disk Use Limits

> You can have the Data Service stop writing to the data storage path when it fills to a specific percentage. This option helps prevent the data path from running out of disk space and making recovery difficult. 

## [](#description)Description

Allowing any filesystem on a node to become full can cause errors. If the filesystem containing the data storage path becomes full, recovery can be difficult. This endpoint allows you to set a limit on the percentage of disk space that can be used by the data storage path. When the data storage path reaches this limit, the Data Service stops writing to it. See [Filesystem Free Space and Usage Limits](../learn/buckets-memory-and-storage/storage-settings.md#filesystem-free-space-and-usage-limits) for more information.

> [!NOTE]
> If other services write to the same filesystem as the data storage path, the filesystem can still become full.

## [](#http-methods)HTTP Methods

This API endpoint supports the following methods:

* [Get Data Disk Use Limits](#get-settings)
* [Set Data Disk Use Limits](#set-usage-limit)

## [](#get-settings)Get Data Disk Use Limits

Use this endpoint to get the current data disk use limit settings.

Get Limit Settings

GET /settings/resourceManagement

### [](#curl-syntax)curl Syntax

```bash
 curl -u $USER:$PASSWORD -X GET \
      'http://{HOST}:{PORT}/settings/resourceManagement'
```

Path Parameters

`USER`

The name of a user who has one of the roles listed in [Required Privileges](#get-privs).

`PASSWORD`

The password for the `user`.

`HOST`

Hostname or IP address of a Couchbase Server.

`PORT`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

### [](#get-privs)Required Privileges

You must have at least on one of the following roles:

* [Full Admin](../learn/security/roles.md#full-admin)
* [Cluster Admin](../learn/security/roles.md#cluster-admin)
* [Local User Admin](../learn/security/roles.md#local-user-security-admin)
* [Security Admin](../learn/security/roles.md#security-admin)

### [](#responses)Responses

`200 OK`

Returns a JSON object containing the current data disk use limit settings. See [Examples](#get-settings-example) for the schema of the output.

`403 Forbidden`

Returned if the user does not have one of the roles listed in [Required Privileges](#get-privs).

### [](#get-settings-example)Examples

The following example gets the current settings for data disk use limits:

```bash
curl -u Administrator:password \
     -X GET 'http://127.0.0.1:8091/settings/resourceManagement' | jq
```

The JSON returned by this command shows the current settings for data disk use limits:

```json
 {
  "diskUsage": {
    "enabled": false,
    "maximum": 85
  }
}
```

The result shows that the disk usage limit is not enabled, and the maximum disk usage is set to 85% (the default).

## [](#set-usage-limit)Set Data Disk Use Limits

Use this endpoint to set the data disk use limit settings.

Set Limits

POST /settings/resourceManagement

### [](#curl-syntax-2)curl Syntax

```bash
 curl -u $USER:$PASSWORD -X POST \
      'http://{HOST}:{PORT}/settings/resourceManagement' \
      -H 'Content-Type: application/json' \
      -d '{"diskUsage": {"enabled": [true|false], "maximum": <integer>}}'
```

Path Parameters

`USER`

The name of a user who has one of the roles listed in [Required Privileges](#set-privs).

`PASSWORD`

The password for the `user`.

`HOST`

Hostname or IP address of a Couchbase Server.

`PORT`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

Data Parameters

`enabled` (Boolean)

If `true`, enables the data disk use limit. If `false`, disables the data disk use limit.

`maximum` (integer)

The maximum percentage of disk space that can be used by the data storage path. If the data storage path reaches this limit, Couchbase Server stops writing to it. This value must be between 1 and 100.

### [](#set-privs)Required Privileges

You must have at least 1 of the following roles:

* [Full Admin](../learn/security/roles.md#full-admin)
* [Cluster Admin](../learn/security/roles.md#cluster-admin)
* [Security Admin](../learn/security/roles.md#security-admin)

### [](#responses-2)Responses

`200 OK`

Returns a JSON object containing the current data disk use limit settings. See [Examples](#set-limit-example) for the schema of the output.

`403 Forbidden`

Returned if the user does not have 1 of the roles listed in [Required Privileges](#set-privs).

### [](#set-limit-example)Examples

The following example enables data disk use limits and sets the maximum disk usage to 90%:

```bash
curl -X POST 'http://127.0.0.1:8091/settings/resourceManagement' \
     -H "Content-Type: application/json"\
     -d '{"diskUsage": {"enabled": true, "maximum": 90}}' | jq
```

The JSON returned by this command shows new current settings for data disk use limits:

```json
{
  "diskUsage": {
    "enabled": true,
    "maximum": 90
  }
}
```