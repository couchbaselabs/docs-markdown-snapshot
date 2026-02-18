---
title: Force Encryption of Unencrypted Data
description: Use these REST APIs to force Couchbase Server to encrypt existing data.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/security/encryption-at-rest/force-encryption-at-rest.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/rest-api/security/encryption-at-rest/force-encryption-at-rest.html)

# Force Encryption of Unencrypted Data

> Use these REST APIs to force Couchbase Server to encrypt existing data. 

## [](#description)Description

When you enable encryption at rest for a bucket or a type of data, Couchbase Server begins encrypting newly written data. However, it does not encrypt existing data. These APIs let you force Couchbase Server to encrypt existing data in a bucket or all data of a specific type. See [Native Encryption at Rest](../../../learn/security/native-encryption-at-rest-overview.md) for more information about encryption at rest.

> [!NOTE]
> This method is similar to the [/controller/dropEncryptionAtRestDeks](drop-encryption-deks.md) endpoint, but it does not rotate the data encryption keys (DEKs) nor does it re-encrypt already-encrypted data.

## [](#http-methods)HTTP Methods

This API endpoint supports the following methods:

* [Force Encryption of Unencrypted Bucket Data](#bucket)
* [Force Encryption of a Type of Non-bucket Data](#type)

## [](#bucket)Force Encryption of Unencrypted Bucket Data

Force the unencrypted data in a bucket to be encrypted immediately.

Encrypt Unencrypted Data in Bucket

POST /controller/forceEncryptionAtRest/bucket/{BUCKET_NAME}

Path Parameters

`BUCKET_NAME`

The name of the bucket whose unencrypted data you want to encrypt. This bucket must already have encryption at rest enabled.

### [](#curl-syntax)curl Syntax

```bash
curl -sS -u $USER:$PASSWORD \
     -X POST 'http[s]://<hostname>:{PORT}/controller/forceEncryptionAtRest/bucket/{BUCKET_NAME}'
```

Path Parameters

`USER`

The name of a user who has one of the roles listed in [Required Privileges](#bucket-privs).

`PASSWORD`

The password for the `user`.

`HOST`

Hostname or IP address of a Couchbase Server.

`PORT`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

`BUCKET_NAME`

The name of the bucket whose unencrypted data you want to encrypt. This bucket must already have encryption at rest enabled for this method to have an effect.

### [](#bucket-privs)Required Privileges

You must have at least one of the following roles:

* [Backup Admin](../../../learn/security/roles.md#backup%5Fadmin)
* [Bucket Admin](../../../learn/security/roles.md#bucket%5Fadmin) that has privileges on the bucket to be encrypted.
* [Cluster Admin](../../../learn/security/roles.md#cluster%5Fadmin)
* [Eventing Admin](../../../learn/security/roles.md#eventing%5Fadmin)
* [Full Admin](../../../learn/security/roles.md#admin)

### [](#responses)Responses

`200 OK`

The request was successful and Couchbase Server starts encrypting the data. Returns a JSON object with a timestamp of when Couchbase Server started encrypting the data. See [the example in the next section](#bucket-example) for an example of the response.

> [!NOTE]
> This endpoint also returns `200 OK` for buckets that do not have encryption at rest enabled. In this case, the request does not encrypt any data.

`400 Bad Request`

The request was malformed or Couchbase Server could not process it.

`401 Unauthorized`

The user credentials you supplied were not valid.

`403 Forbidden`

Your user account does not have one of the required roles to call this endpoint.

`404 Not Found`

The bucket named in the `BUCKET_NAME` path parameter does not exist.

### [](#bucket-example)Example

The following example demonstrates how to force Couchbase Server to encrypt the unencrypted data in a bucket named `travel-sample`:

```bash
curl -v -u Administrator:password
     -X POST http://localhost:8091/controller/forceEncryptionAtRest/bucket/travel-sample
     | jq
```

The result of request is a JSON object with a `forceEncryptionDate` attribute that contains the date and time when Couchbase Server started encrypting the data:

```json
{
  "forceEncryptionDate": "2025-08-04T17:58:39Z"
}
```

## [](#type)Force Encryption of a Type of Non-bucket Data

Force the encryption of unencrypted data of one of the following types:

* Audit
* Configuration
* Logging

Encrypt Unencrypted Data of a Type

POST /controller/forceEncryptionAtRest/{TYPE}

Path Parameter

`TYPE`

The type of data to encrypt. Can be one of the following values:

* `audit`: Encrypts unencrypted audit data.
* `config`: Encrypts unencrypted configuration data.
* `log`: Encrypts unencrypted log data.

### [](#curl-syntax-2)curl Syntax

```bash
curl -sS -u $USER:$PASSWORD \
     -X POST 'http://localhost:8091/controller/forceEncryptionAtRest/{TYPE}'
```

Path Parameters

`USER`

The name of a user who has one of the roles listed in [Required Privileges](#type-privs).

`PASSWORD`

The password for the `user`.

`HOST`

Hostname or IP address of a Couchbase Server.

`PORT`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

`TYPE`

The type of data to encrypt. Must be one of the following values:

* `audit`: Encrypts unencrypted audit data.
* `config`: Encrypts unencrypted configuration data.
* `log`: Encrypts unencrypted log data.

### [](#type-privs)Required Privileges

To call this endpoint, you must have at least one of the following roles:

* [Full Admin](../../../learn/security/roles.md#admin)
* [Security Admin](../../../learn/security/roles.md#security%5Fadmin)

### [](#responses-2)Responses

`200 OK`

The request was successful and Couchbase Server starts encrypting the data. Returns a JSON object with a timestamp of when Couchbase Server started encrypting the data. See [the example in the next section](#type-example) for an example of the response.

> [!NOTE]
> This endpoint also returns `200 OK` if you have not enabled encryption at rest for the type of data set by the `TYPE` path parameter. In this case, the request does not encrypt any data.

`400 Bad Request`

The request was malformed or Couchbase Server could not process it.

`401 Unauthorized`

The user credentials you supplied were not valid.

`403 Forbidden`

Your user account does not have one of the required roles to call this endpoint.

`404 Not Found`

The `TYPE` path did not contain one of the valid values: `audit`, `config`, or `log`.

### [](#type-example)Example

The following example demonstrates how to force Couchbase Server to encrypt unencrypted log data:

```console
curl -sS -u Administrator:password -X POST \
     http://localhost:8091/controller/forceEncryptionAtRest/log \
     | jq
```

The result of request is a JSON object with a `forceEncryptionDate` attribute that contains the date and time when Couchbase Server started encrypting the data:

```json
{
  "forceEncryptionDate": "2025-08-05T13:18:34Z"
}
```