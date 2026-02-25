---
title: Drop DEKs and Re-encrypt Data
description: You can use the REST API to drop data encryption keys (DEKs) and
  re-encrypt the data encrypted with the old keys.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/security/encryption-at-rest/drop-encryption-deks.adoc
pubDate: 2026-02-25T03:45:01.178Z
link: xref:server:rest-api:security/encryption-at-rest/drop-encryption-deks.adoc[]
---

[View original HTML](/server/current/rest-api/security/encryption-at-rest/drop-encryption-deks.html)

# Drop DEKs and Re-encrypt Data

> You can use the REST API to drop data encryption keys (DEKs) and re-encrypt the data encrypted with the old keys. 

## [](#description)Description

You may want to drop data encryption keys (DEKs) if you believe they have been compromised. When you have Couchbase Server drop DEKs, it creates a new DEK to replace the active and all historical DEKs for the bucket or data type. It then re-encrypts all data using the new DEK and deletes the old DEKs. This re-encryption includes any unencrypted data that was written before you enabled encryption at rest.

If you call this endpoint after disabling encryption at rest for a bucket or type of data, Couchbase Server decrypts all of the data and drops the DEKs. If you do not

> [!NOTE]
> If you just want to encrypt any unencrypted data, you can do so without dropping the DEKs. See [Force Encryption of Unencrypted Data](force-encryption-at-rest.md) for more information.

Dropping the DEKs is not the same as rotating them. When it rotates a DEK, Couchbase Server just creates a new DEK and makes it active. It does not re-encrypt data, and it keeps the inactive DEKs for a period of time. You cannot manually rotate DEKs. When you drop DEKs, Couchbase Server creates new a new DEK, re-encrypts all data with it, and deletes the old DEKs.

> [!IMPORTANT]
> The process of dropping DEKs for a bucket with a large amount of data may take a long time and could affect performance. When you drop the DEKs, Couchbase Server has to re-encrypt all data in the bucket with the new DEK. Dropping DEKs for audit, configuration, or logs is less of a concern because it usually results in re-encrypting less data than a bucket.

See [Manually Drop DEKs and Re-encrypt Data](#manage:security/manage-native-encryption-at-rest.adoc#drop-deks) for instructions on dropping DEKs using the Couchbase Server Web Console.

## [](#http-methods)HTTP Methods

This API endpoint supports the following methods:

* [Drop DEKs and Re-encrypt Data for a Bucket](#drop-bucket)
* [Drop DEKs and Re-encrypt Audit, Configuration, or Log Data](#drop-type)

## [](#drop-bucket)Drop DEKs and Re-encrypt Data for a Bucket

Drop all DEKs for a bucket and re-encrypt all data in that bucket with the new DEK.

Drop DEKs for Bucket and Re-encrypt Data

POST /controller/dropEncryptionAtRestDeks/bucket/{BUCKET_NAME}

Path Parameters

`BUCKET_NAME`

The name of the bucket where you want to drop the DEKs and re-encrypt. This bucket must already have encryption at rest enabled.

### [](#curl-syntax)curl Syntax

```bash
curl -sS -u $USER:$PASSWORD \
     -X POST 'http[s]://<hostname>:{PORT}/controller/dropEncryptionAtRestDeks/bucket/{BUCKET_NAME}'
```

Path Parameters

`USER`

The name of a user who has one of the roles listed in [Required Privileges](#bucket-privs).

`PASSWORD`

The password for the `user`.

`host`

Hostname or IP address of a Couchbase Server node.

`port`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

`BUCKET_NAME`

The name of the bucket where you want to drop DEKs and re-encrypt data. This bucket must already have encryption at rest enabled.

### [](#bucket-privs)Required Privileges

* [Backup Admin](../../../learn/security/roles.md#backup%5Fadmin)
* [Bucket Admin](../../../learn/security/roles.md#bucket%5Fadmin) that has privileges on the bucket to be encrypted.
* [Cluster Admin](../../../learn/security/roles.md#cluster%5Fadmin)
* [Eventing Admin](../../../learn/security/roles.md#eventing%5Fadmin)
* [Full Admin](../../../learn/security/roles.md#admin)

### [](#responses)Responses

`200 OK`

The DEKs for the bucket were dropped and the data was re-encrypted with the new DEK. It also returns a JSON object containing a timestamp of when the drop and re-encryption process started. See [the example in the next section](#drop-bucket-example) for an example of the response.

`403 Forbidden`

You do not have the required privileges to drop the DEKs for the bucket.

`404 Not Found`

The bucket passed in the `BUCKET_NAME` path parameter does not exist.

### [](#drop-bucket-example)Example

The following example drops the DEKs for the `travel-sample` bucket and re-encrypts all data in that bucket with the new DEK.

```bash
curl -sS -u Administrator:password -X POST \
     http://localhost:8091/controller/dropEncryptionAtRestDeks/bucket/travel-sample \
     | jq
```

The result of the command is a JSON object similar to the following:

```json
{
  "dropKeysDate": "2025-08-06T19:00:42Z"
}
```

## [](#drop-type)Drop DEKs and Re-encrypt Audit, Configuration, or Log Data

Drop the DEKs for a type of system data and re-encrypt all data with the new DEKs. The data types you can re-encrypt are:

* Audit
* Configuration
* Logs

Drop DEKs for Audit, Configuration, or Logs and Re-encrypt Data

POST /controller/dropEncryptionAtRestDeks/{TYPE}

Path Parameters

`TYPE`

The type of data whose DEKs you want dropped and data re-encrypted. Can be one of the following values:

* `audit`: Encrypts unencrypted audit data.
* `config`: Encrypts unencrypted configuration data.
* `log`: Encrypts unencrypted log data.

### [](#curl-syntax-2)curl Syntax

```bash
curl -sS -u $USER:$PASSWORD \
     -X POST 'http[s]://<hostname>:{PORT}/controller/dropEncryptionAtRestDeks/{TYPE}'
```

Path Parameters

`USER`

The name of a user who has one of the roles listed in [Required Privileges](#type-privs).

`PASSWORD`

The password for the `user`.

`host`

Hostname or IP address of a Couchbase Server node.

`port`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

`TYPE`

The type of data whose DEKs you want dropped and data re-encrypted. Can be one of the following values:

* `audit`: Encrypts unencrypted audit data.
* `config`: Encrypts unencrypted configuration data.
* `log`: Encrypts unencrypted log data.

### [](#type-privs)Required Privileges

* [Cluster Admin](../../../learn/security/roles.md#cluster%5Fadmin)
* [Eventing Admin](../../../learn/security/roles.md#eventing%5Fadmin)
* [Full Admin](../../../learn/security/roles.md#admin)

### [](#responses-2)Responses

`200 OK`

The DEKs for the type of data were dropped and its data was re-encrypted with the new DEK. It also returns a JSON object containing a timestamp of when the drop and re-encryption process started. See [the example in the next section](#drop-type-example) for an example of the response.

`403 Forbidden`

You do not have the required privileges to drop the DEKs for system data.

`404 Not Found`

The type of data passed in the `TYPE` path parameter does not exist.

### [](#drop-type-example)Example

The following example drops the DEKs for the `audit` data and re-encrypts all data of that type with the new DEK.

```bash
curl -v -u Administrator:password -X POST \
     http://localhost:8091/controller/dropEncryptionAtRestDeks/audit \
     | jq
```

The result of the command is a JSON object similar to the following:

```json
{
  "dropKeysDate": "2025-08-06T19:05:42Z"
}
```