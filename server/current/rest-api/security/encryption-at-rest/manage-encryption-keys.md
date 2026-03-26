---
title: Manage Encryption-at-Rest Keys
description: You must create encryption-at-rest keys before you can have
  Couchbase Server encrypt data as it saves it to disk.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/security/encryption-at-rest/manage-encryption-keys.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:rest-api:security/encryption-at-rest/manage-encryption-keys.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/rest-api/security/encryption-at-rest/manage-encryption-keys.html)

# Manage Encryption-at-Rest Keys

> You must create encryption-at-rest keys before you can have Couchbase Server encrypt data as it saves it to disk. 

## [](#description)Description

These APIs let you list, create, change, test, and delete encryption-at-rest keys. See [Native Encryption at Rest](../../../learn/security/native-encryption-at-rest-overview.md) for more information about encryption at rest.

## [](#http-methods)HTTP Methods

This API endpoint supports the following methods:

* [List Encryption-at-Rest Keys](#list-keys)
* [Create or Update an Encryption-at-Rest Key](#create-key)
* [Test Existing Encryption-at-Rest Key](#test-key)
* [Test Possible Changes to an Encryption-at-Rest Key](#test-key-changes)
* [Delete an Encryption-at-Rest Key](#delete-key)

## [](#list-keys)List Encryption-at-Rest Keys

List one or all encryption-at-rest keys defined in the cluster.

List All Keys

GET /settings/encryptionKeys/

Get details of a specific key

GET /settings/encryptionKeys/{KEY_ID}

Path Parameters

`KEY_ID` (integer)

The `id` attribute of the key you want to view. See the [example](#gey-keys-example) for an explanation of getting this value.

### [](#curl-syntax)curl Syntax

```bash
curl -sS -u $USER:$PASSWORD \
     -X GET 'http[s]://<hostname>:{PORT}/settings/encryptionKeys/[{KEY_ID}]'
```

Path Parameters

`USER`

The name of a user who has one of the roles listed in [Required Privileges](#get-privs).

`PASSWORD`

The password for the `user`.

`host`

Hostname or IP address of a Couchbase Server node.

`port`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

`KEY_ID` (optional)

The id of the single encryption-at-rest key whose details you want to retrieve.

### [](#get-privs)Required Privileges

The role you need to view specific keys depends on their use.

The following roles let you view all keys, including keys that can encrypt other keys (KEKs), audit, logs, and configuration data:

* [Full Admin](../../../learn/security/roles.md#admin)
* [Read-Only Admin](../../../learn/security/roles.md#read-only-admin)
* [Security Admin](../../../learn/security/roles.md#security%5Fadmin)

The following roles let you view keys that can encrypt data in buckets. Some of the role's ability to read keys depends on whether you have rights to access the bucket. For example, the Data Reader role only grants you access to keys that can encrypt data in buckets you have read access to.

* [Full Admin](../../../learn/security/roles.md#admin)
* [Read-Only Admin](../../../learn/security/roles.md#read-only-admin)
* [Security Admin](../../../learn/security/roles.md#security-admin)
* [Local User Admin](../../../learn/security/roles.md#local-user-security-admin)
* [External User Admin](../../../learn/security/roles.md#external-user-security-admin)
* [Cluster Admin](../../../learn/security/roles.md#cluster-admin)
* [Eventing Full Admin](../../../learn/security/roles.md#eventing-full-admin)
* [Backup Full Admin](../../../learn/security/roles.md#admin)
* [Bucket Admin](../../../learn/security/roles.md#backup-full-admin)
* [Application Access](../../../learn/security/roles.md#application-access)
* [Views Admin](../../../learn/security/roles.md#views-admin)
* [XDCR Admin](../../../learn/security/roles.md#xdcr-admin)
* [Data Reader](../../../learn/security/roles.md#data-reader)
* [Data Writer](../../../learn/security/roles.md#data-writer)
* [Data DCP Reader](../../../learn/security/roles.md#data-dcp-reader)
* [Data Backup & Restore](../../../learn/security/roles.md#data-backup-and-restore)
* [Data Monitor](../../../learn/security/roles.md#data-monitor)
* [Search Admin](../../../learn/security/roles.md#search-admin)
* [Search Reader](../../../learn/security/roles.md#search-reader)
* [Query Select](../../../learn/security/roles.md#query-select])
* [Query Update](../../../learn/security/roles.md#query-update)
* [Query Insert](../../../learn/security/roles.md#query-insert)
* [Query Delete](../../../learn/security/roles.md#query-delete)
* [Query Manage Index](../../../learn/security/roles.md#query-manage-index)
* [Query List Index](../../../learn/security/roles.md#query-list-index)
* [Query System Catalog](../../../learn/security/roles.md#query-system-catalog)
* [Query CURL Access](../../../learn/security/roles.md#query-curl-access)
* [XDCR Inbound](../../../learn/security/roles.md#xdcr-inbound)
* [Sync Gateway](../../../learn/security/roles.md#sync-gateway)

### [](#responses)Responses

`200 OK`

Returns the encryption-at-rest keys or a particular key if you specified the `KEY_ID` path parameter. See examples for an example of the keys.

> [!NOTE]
> Call returns `200 OK` and an empty JSON message if user does not have permission to view keys.

`404 Object Not Found`

Returned if you specified a `KEY_ID` path parameter which does not match the ID of an encryption-at-rest key.

### [](#gey-keys-example)Examples

The following example gets all of the encryption-at-rest keys defined in the system.

```bash
 curl -sS -u Administrator:password \
      -X GET 'http://127.0.0.1:8091/settings/encryptionKeys/' | jq
```

An example of running the previous command:

```json
[
  {
    "data": {
      "keys": [
        {
          "id": "b3dd8518-e747-4a64-ad6b-db9c5d306a6c",
          "active": true,
          "creationDateTime": "2025-04-23T16:22:39Z",
          "keyMaterial": "******"
        }
      ],
      "encryptionApproach": "nodeSecretManager",
      "canBeCached": true,
      "autoRotation": false
    },
    "id": 7,
    "name": "data-one-buckey-key",
    "type": "cb-server-managed-aes-key-256",
    "usage": [
      "bucket-encryption-beer-sample",
      "bucket-encryption-test"
    ],
    "creationDateTime": "2025-04-23T16:22:39Z"
  },
  {
    "data": {
      "port": 5696,
      "host": "https://kms.example.com",
      "reqTimeoutMs": 1000,
      "keyPath": "/scripts/certs/cb_key.pem",
      "keyPassphrase": "******",
      "encryptionApproach": "useGet",
      "certPath": "/scripts/certs/cb_cert.pem",
      "caSelection": "useSysAndCbCa",
      "encryptionApproach": "nodeSecretManager",
      "historicalKeys": [],
      "activeKey": {
        "id": "0788edb1-1418-4225-903b-bc1f9f59aa4d",
        "kmipId": "550e8400-e29b-41d4-a716-446655440000",
        "creationDateTime": "2025-04-23T14:44:20Z"
      },
      "encryptionApproachKeyId": -1
    },
    "id": 2,
    "name": "kmip-key",
    "type": "kmip-aes-key-256",
    "usage": [
      "KEK-encryption",
      "bucket-encryption",
      "config-encryption",
      "log-encryption",
      "audit-encryption"
    ],
    "creationDateTime": "2025-04-23T14:44:20Z"
  },
  {
    "data": {
      "profile": "",
      "configFile": "",
      "useIMDS": true,
      "region": "us-east-1",
      "keyARN": "arn:aws:kms:us-east-1:000000000000:key/aaaaaaaa-bbbb-dddd-eeee-ffffffffffff",
      "credentialsFile": "",
      "storedKeyIds": [
        {
          "id": "c1cddf80-720e-47f0-adb7-641f5cb2ce22",
          "creationDateTime": "2025-04-23T16:00:22Z"
        }
      ]
    },
    "id": 6,
    "name": "Example AWS key",
    "type": "awskms-symmetric-key",
    "usage": [
      "KEK-encryption"
    ],
    "creationDateTime": "2025-04-23T16:00:22Z"
  }
]
```

All keys have the following fields:

* `id`: the integer identifying the encryption key
* `name`: the friendly name assigned by the administrator who created the key.
* `usage`: what the key is allowed to encrypt.
* `type`: which key management system (KMS) manages the key.  
> [!NOTE]  
> The `type` also contains the encryption algorithm used for the encryption-at-rest key. Currently, this is always `aes-key-256`.

The `data` object defines the KMS-specific details for each encryption key. You'll notice different fields for each type of key:

Keys managed by Couchbase Server

* The `keys` list contains the current and expired encryption keys. The other key types have their contents stored within the remote KMS.
* The `autorotation` field indicates whether Couchbase Server automatically rotates the key. When set to `` true` ``, additional fields, such as `data.rotationIntervalInDays` and `nextRotationTime` show details of the key's rotation. \*

Keys managed by a KMIP-compatible KMS

* The fields configure the authentication with the KMS.

Keys Managed by AWS

* `keyANN` is the identity of the key in the AWS KMS.
* The `profile`, `credentialsFile`, and `configFile` hold the credentials Couchbase Server uses to authenticate with AWS KMS. These values are empty when Couchbase Server uses IAM to authenticate with AWS instead of stored credentials.

## [](#create-key)Create or Update an Encryption-at-Rest Key

You can create or update an encryption-at-rest-key key using the REST API.

Create an Encryption Key

POST /settings/encryptionKeys/

Update a Key

PUT /settings/encryptionKeys/{KEY_ID}

Path Parameters

`KEY_ID` (integer)

The `id` attribute of the key you want to update.

### [](#curl-syntax-2)curl Syntax

Create an Encryption at Rest Key

```bash
curl -sS -u $USER:$PASSWORD \
  -X POST http://{HOST}:{PORT}/settings/encryptionKeys \
  --data-binary @- <<EOF | jq
{
  "name": "<keyname>",
  "usage": [
    "<usage>"[."<usage>"...]
  ],
  "type": "<KMS>",
  "data": {
    <KMS-specific-fields>
  }
}
EOF
```

Update an Encryption at Rest Key

```bash
curl -sS -u $USER:$PASSWORD \
  -X PUT http://{HOST}:{PORT}/settings/encryptionKeys/{KEY_ID} \
  --data-binary @- <<EOF | jq
{
  "name": "<keyname>",
  "usage": [
    "<usage>"[."<usage>"...]
  ],
  "type": "<KMS>",
  "data": {
    <KMS-specific-fields>
  }
}
EOF
```

> [!NOTE]
> Updating a key has the same required fields as the creating a new key. For example, you must supply the `name` field, even if you want the key's name to remain the same. Couchbase Server sets any value you do not supply in the update call to the default value (if any) or is left empty, overwriting any existing value.

Path Parameters

`USER`

The name of a user who has one of the roles listed in [Required Privileges](#create-privs).

`PASSWORD`

The password for the `user`.

`host`

Hostname or IP address of a Couchbase Server node.

`port`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

`KEY_ID` (integer)

The `id` attribute of the key you want to update.

Fields

`name` (required)

A name to give to the key. This name must be different from any other encryption-at-rest key.

`usage`

A comma-separated list of what this key can encrypt. Allowed values for this list are:

* `"KEK-encryption"`: Can encrypt other encryption-at-rest keys (KEK).
* `"bucket-encryption"`: Can encrypt any bucket in the cluster.
* `"bucket-encryotion-<bucket-name>"`: Can encrypt the bucket named `bucket-name`. You can include multiple instances of this value to list specific buckets the key can encrypt.
* `"config-encryption"`: Can encrypt configuration information.
* `"log-encryption"`: Can encrypt logs.
* `"audit-encryption"`: Can encrypt audit data.

`type`

Defines the encryption standard and the key management system for the key. All encryption-at-rest keys use AES 256 encryption. Allowed values are:

* `"awskms-symmetric-key"`: AWS KMS manages the key.
* `"kmip-aes-key-256"`: A KMIP-compatible KMS manages the key.
* `"cb-server-managed-aes-key-256"`: Couchbase Server manages the key.

`data`

The contents of the `data` object depend on the KMS set in the `type` field because each KMS has unique settings.

* AWS
* KMIP KMS
* Couchbase Server

When using the AWS KMS, the `data` object has the following schema:

```json
  "data": {
    "keyARN": "<arn>",
    "region": "<region>",
    "useIMDS": <true|false>,
    "profile": "<profile-file-path>",
    "credentiials-file": "<credential-file-path>",
    "configFile": "<config-file-path>"
  }
```

Fields

* `keyARN`: The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that identifies the encryption key in the AWS KMS.
* `region` (optional): The region hosting your AWS KMS.
* `useIMDS` (Boolean, optional): Whether to use Amazon's [Instance Metadata Service (IMD)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) when contacting the AWS KMS. Set this to `true` when your cluster runs on AWS EC2 instances. Defaults to `false`.

You must give Couchbase Server a way to authenticate with the AWS KMS. See Amazon's [KMS key access and permissions](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html) for details of configuring authentication.

You can use [IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html) to allow Couchbase Server to transparently connect to the AWS KMS. If you configure IAM, you do not need any additional authentication configuration within Couchbase Server. Always use this method if your database runs on an AWS EC2 cluster. It's also possible to configure IAM for your cluster when it's not running in AWS. See the AWS documentation for using [IAM Roles Anywhere](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Froles%5Fcommon-scenarios%5Fnon-aws.html).

The other authentication method is to use three optional parameters to pass Couchbase Server the necessary credentials in several files. These files must exist on all servers in your cluster.

Use the following parameters to tell Couchbase Server where these files are located:

* `credentials-file` the absolute path to a file containing the AWS credentials to use when authenticating with the AWS KMS. When you supply this path, the file must exist on all nodes. This file often stored at `~/.aws/credentials` on Linux systems. For example:  
```ini  
[my-profile]  
aws_access_key_id = ABCDE...  
aws_secret_access_key = xyz123...  
```
* `configFile`: the absolute path to a file that defines one or more profiles for accessing AWS. This file is often stored in `~/.aws/config` on Linux systems. The format of  
```ini  
[profile profile-name]  
region = us-east-1  
output = json  
role_arn = arn:aws:iam::123456789012:role/RoleName  
source_profile = base  
```
* `profile`: The name of the profile defined in the configuration file to use when authenticating with AWS KMS.

> [!NOTE]
> Couchbase Server does not verify the information you give it during key creation. It only attempts to connect to AWS when you select the key to encrypt data or another key. See [Test an Encryption-at-Rest Key](#test-key) to learn how to test the key.

When using a KMIP-compatible KMS, the `data` object has the following schema:

```json
"data": {
      "port": <kms-port>,
      "host": "<kms-host-url>",
      "reqTimeoutMs": <timeout-ms>,
      "keyPath": "<path-to-key-pem>",
      "keyPassphrase": "<passphrase>",
      "encryptionApproach": "<local-or-kms>",
      "certPath": "<certificate-path>",
      "caSelection": "<trust-store>",
      "encryptionApproach": "<password-or-key>",
      "activeKey": {
        "kmipId": "<kmip-KEY_ID>"
      },
      "encryptionApproachKeyId": <local-KEY_ID>
    }
```

Fields

* `port`: Integer port number for the KMS server. Most KMS servers use port 5696.
* `host`: The URL for the KMS.
* `reqTimeoutMs` (integer, optional): The timeout for network communication with the KMS in milliseconds. Defaults to 1000.
* `keyPath`: Absolute path on each server to the private key Couchbase Server uses to authenticate with the KMS. This key file must be in PEM format.
* `keyPassphrase` (optional): The private key's passphrase, if it has one.
* `encryptionApproach`: Controls which system performs the decryption of keys. Can be one of the following values:

  * `"useGet"`: Couchbase Server retrieves the encryption key from the KMS and uses it to decrypt local DEKs and encryption keys.
  * `"useEncryptDecrypt"`: Send local DEKs and encryption keys to the KMS. The KMS decrypts the keys locally and returns the decrypted keys back to Couchbase Server.
* `certPath`: The absolute path on all servers to the certificate to use when authenticating with the KMS. The certificate file must be in PEM format.
* `caSelection` (optional): Where to look for certificates when verifying the identity of the KMS. Can be one of the following values:

  * `"useSysAndCbCa"` (default): Use the certificates in both the operating system's and Couchbase Server's trust stores.
  * `"useSysCa"`: Use the certificates in the operating system's trust store.
  * `"useCbCa"`: Use the certificates in Couchbase Server's trust store.
  * `"skipServerCertVerification"`: Skip verification of the KMS.  
  > [!CAUTION]  
  > Not verifying the identity of the KMS is insecure.
* `encryptionApproach` (optional): controls how the passphrase for the private key is encrypted for local storage. The two options are:

  * `"nodeSecretManager"` (default): Couchbase Server encrypts the passphrase using the [master password](../../../manage/manage-security/manage-system-secrets.md#setting-the-master-password).
  * `"encryptionKey"`: Use a KEK-enabled encryption key to encrypt the passphrase. If you choose this option, you must also supply the `encryptionApproachKeyId` parameter.
* `activeKey.kmipId`: The ID of the encryption key stored in the KMS. The format of this value depends on the KMS. It's often in the form of a UUID or a friendly name.
* `encryptionWithKeyId` (integer): The `id` attribute of the encryption key Couchbase Server uses to encrypt the private key's passphrase when storing it locally. See [List Encryption-at-Rest Keys](#list-keys) to learn how to get an encryption key's `id`. Required if you set `encryptWith` to `encryptionKey`.

> [!NOTE]
> Couchbase Server does not verify the information you give it during key creation. It only attempts to connect to the KMS when you assign the key to encrypt something. See [Test an Encryption-at-Rest Key](#test-key) to learn how to test the key.

When having Couchbase Server manage the key, the `data` object has the following schema:

```json
    "data": {
      "autoRotation": <true|false>,
      "encryptionApproach": "<key-or-secrets-manager>",
      "encryptionApproachKeyId": <KEY_ID>
      "canBeCached": <true|false>
      "nextRotationTime": "<iso-8601-date",
      "rotationIntervalInDays": <days>
    }
```

Fields

* `autoRotation` (Boolean, optional): Controls whether Couchbase Server automatically rotates the key. See [Encryption Key Rotation and Expiration](../../../learn/security/native-encryption-at-rest-overview.md#rotation-expiration) for more information about key rotation. Defaults to `true`, which means that Couchbase Server automatically rotates the key. In this case, you must supply both the `nextRotationTime` and `rotationIntervalInDays` fields as well.
* `encryptionApproach` (optional): How Couchbase Server should encrypt this key for storage. The two options are:

  * `"nodeSecretManager"`: (default): Couchbase Server encrypts the key using the [master password](../../../manage/manage-security/manage-system-secrets.md#setting-the-master-password).
  * `"encryptionKey"`: Couchbase Server uses a KEK-enabled encryption key to encrypt the key. If you choose this option, you must also supply the `encryptionApproachKeyId` field.
* `encryptionApproachKeyId` (integer): The `id` attribute of an existing encryption-at-rest key to use to encrypt this key. The key you select must have `KEK-encryption` in its `usage` list.
* `canBeCached` (Boolean, optional): Set this value to `true` (the default) to allow Couchbase Server to cache the decrypted key in memory. The default `true` value makes using the key more efficient because Couchbase Server does not have to decrypt it each time it needs to use it. Disabling caching by setting this value to `false` can significantly increase node start time because the node decrypts all of its DEKs on startup. It can also increase the time it takes for operations that re-encrypts DEKs, such as key rotation or changing encryption at rest settings. The `false` setting can reduce the chance of in-mmeory key exposure attacks.
* `nextRotationTime`: A date and time string in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO%5F8601) that sets when Couchbase Server must rotate this key. You must set this value if you set `autoRotation` to `true`.
* `rotationIntervalInDays` (integer): How often, in days, Couchbase Server rotates this key. You must set this value if you set `autoRotation` to `true`.

### [](#create-privs)Required Privileges

The role you need to create or update keys depends on what the key you're creating or updating can encrypt:

For keys that can encrypt audit, configuration, or log data or can encrypt other encryption-at-rest keys (KEKs), you must have one or more of the following roles:

* [Full Admin](../../../learn/security/roles.md#admin)
* [Security Admin](../../../learn/security/roles.md#security-admin)

For keys that can encrypt any bucket in the cluster, you must have one or more of the following roles:

* [Backup Full Admin](../../../learn/security/roles.md#admin)
* [Cluster Admin](../../../learn/security/roles.md#cluster-admin)
* [Eventing Full Admin](../../../learn/security/roles.md#eventing-full-admin)
* [Full Admin](../../../learn/security/roles.md#admin)
* [Security Admin](../../../learn/security/roles.md#security-admin)

For keys that can encrypt one or more specific buckets, you must have one or more of the following roles:

* [Backup Full Admin](../../../learn/security/roles.md#admin)
* [Bucket Admin](../../../learn/security/roles.md#backup-full-admin) that has privileges on the bucket to be encrypted.
* [Cluster Admin](../../../learn/security/roles.md#cluster-admin)
* [Eventing Full Admin](../../../learn/security/roles.md#eventing-full-admin)
* [Full Admin](../../../learn/security/roles.md#admin)
* [Security Admin](../../../learn/security/roles.md#security-admin)

### [](#responses-2)Responses

`200 OK`

Returns a JSON message containing the new encryption-at-rest key. See [Examples](#create-examples) for examples of the returned JSON.

`400 Bad Request`

Returned when errors occur, such as leaving out a required setting or invalid JSON. Also returns a descriptive JSON message. For example, if you set `encryptionApproach` to `encryptionKey` but do not set `encryptionApproachKeyID`, you receive this message:

```json
{
  "errors": {
    "data": {
      "encryptionApproach": "encryptionApproachKeyId must be set when 'encryptionKey' is used"
    }
  }
}
```

`403 Forbidden`

Returned if you do not have the proper roles to call this API. See [Required Privileges](#create-privs).

`404 Object Not Found`

Returned if you specified a `encryptionApproachKeyId` field or a `KEY_ID` path parameter which does not match the `id` field of an existing encryption-at-rest key.

### [](#create-examples)Examples

Create a Couchbase Server Managed Key

The following example creates an auto-generated key (one managed by Couchbase Server). The only data it can encrypt is the travel sample bucket. It can also encrypt the configuration and logs.

```bash
curl -u Administrator:password \
  -X POST \
  http://127.0.0.1:8091/settings/encryptionKeys \
  --data-binary @- <<EOF | jq
{
  "name": "Example Auto-Generated Key",
  "type": "cb-server-managed-aes-key-256",
  "usage": [
    "bucket-encryption-travel-sample", "config-encryption", "log-encryption"
  ],
  "data": {
    "rotationIntervalInDays": 90,
    "nextRotationTime": "2025-07-31T19:27:19Z"
  }
}
EOF
```

The output of running the previous command in the previous example looks like this:

```json
{
  "data": {
    "keys": [
      {
        "id": "fad3d3ae-9195-4779-994e-69266c9360c9",
        "active": true,
        "creationDateTime": "2025-05-02T19:34:07Z",
        "keyMaterial": "******"
      }
    ],
    "encryptionApproach": "nodeSecretManager",
    "canBeCached": true,
    "nextRotationTime": "2025-07-31T19:27:19Z",
    "autoRotation": true,
    "rotationIntervalInDays": 90
  },
  "id": 13,
  "name": "Example Auto-Generated Key",
  "type": "cb-server-managed-aes-key-256",
  "usage": [
    "bucket-encryption-travel-sample",
    "config-encryption",
    "log-encryption"
  ],
  "creationDateTime": "2025-05-02T19:34:07Z"
}
```

Create AWS KMS Managed Key

The following example creates a key managed by the AWS KMS. It relies on IAM roles configured outside of Couchbase Server to authenticate with AWS KMS. The key it creates can only encrypt other encryption-at-rest keys. This is the best practice when using AWS KMS to store encryption-at-rest keys. See [this caution](../../../learn/security/native-encryption-at-rest-overview.md#aws-kms-caution) for more information.

```bash
curl -sS -u Administrator:password \
  -X POST \
  http://127.0.0.1:8091/settings/encryptionKeys \
  --data-binary @- <<EOF | jq
{
  "name": "Example AWS key",
  "type": "awskms-symmetric-key",
  "usage": [
    "KEK-encryption"
  ],
  "data": {
    "keyARN": "arn:aws:kms:us-east-1:000000000000:key/aaaaaaaa-bbbb-dddd-eeee-ffffffffffff",
    "region": "us-east-1",
    "useIMDS": true
  }
}
EOF
```

The following example shows the result of running the command from the previous example:

```json
{
  "data": {
    "profile": "",
    "configFile": "",
    "useIMDS": true,
    "region": "us-east-1",
    "keyARN": "arn:aws:kms:us-east-1:000000000000:key/aaaaaaaa-bbbb-dddd-eeee-ffffffffffff",
    "credentialsFile": "",
    "storedKeyIds": [
      {
        "id": "dd01645e-e59c-462d-8e08-4cc8c3b1a53b",
        "creationDateTime": "2025-05-05T15:10:02Z"
      }
    ]
  },
  "id": 14,
  "name": "Example AWS key",
  "type": "awskms-symmetric-key",
  "usage": [
    "KEK-encryption"
  ],
  "creationDateTime": "2025-05-05T15:10:02Z"
}
```

Create a KMIP-compatible KMS Managed Key

```bash
curl -sS -u Administrator:password  \
     -X POST   http://127.0.0.1:8091/settings/encryptionKeys   \
       --data-binary @- <<EOF | jq
{
  "name": "Example KMIP Key",
  "type": "kmip-aes-key-256",
  "usage": [
    "KEK-encryption"
  ],
"data": {
      "port": 5696,
      "host": "https://kms.example.com",
      "reqTimeoutMs": 1000,
      "keyPath": "/scripts/certs/cb_key.pem",
      "keyPassphrase": "Passwprd1234",
      "encryptionApproach": "useGet",
      "certPath": "/scripts/certs/cb_cert.pem",
      "caSelection": "skipServerCertVerification",
      "encryptWith": "nodeSecretManager",
      "activeKey": {
        "kmipId": "0788edb1-1418-4225-903b-bc1f9f59aa4d"
    }
  }
}
EOF
```

The following example shows the output from running the previous example.

```json
{
  "data": {
    "port": 5696,
    "host": "https://kms.example.com",
    "reqTimeoutMs": 1000,
    "keyPath": "/scripts/certs/cb_key.pem",
    "keyPassphrase": "******",
    "encryptionApproach": "useGet",
    "certPath": "/scripts/certs/cb_cert.pem",
    "caSelection": "skipServerCertVerification",
    "encryptWith": "nodeSecretManager",
    "historicalKeys": [],
    "activeKey": {
      "id": "11c9195b-0d20-41c4-9f3c-550cb5d2c5f3",
      "kmipId": "0788edb1-1418-4225-903b-bc1f9f59aa4d",
      "creationDateTime": "2025-08-05T14:32:21Z"
    }
  },
  "id": 1,
  "name": "Example KMIP Key",
  "type": "kmip-aes-key-256",
  "usage": [
    "KEK-encryption"
  ],
  "creationDateTime": "2025-08-05T14:32:21Z"
}
```

Update the Couchbase Server Managed Key

The following example updates the key created in [Create a Couchbase Server Managed Key](#create-managed-example). The update makes the key able to encrypt any bucket and sets the next rotation time to a later date.

```bash
curl -sS -u Administrator:password \
  -X PUT \
  http://127.0.0.1:8091/settings/encryptionKeys/13 \
  --data-binary @- <<EOF | jq
{
  "name": "Example Auto-Generated Key2",
  "type": "cb-server-managed-aes-key-256",
  "usage": [
    "bucket-encryption", "config-encryption", "log-encryption"
  ],
  "data": {
    "rotationIntervalInDays": 90,
    "nextRotationTime": "2025-08-30T00:00:01Z"
  }
}
EOF
```

The output from the previous example looks like this:

```json
{
  "data": {
    "keys": [
      {
        "id": "fad3d3ae-9195-4779-994e-69266c9360c9",
        "active": true,
        "creationDateTime": "2025-05-02T19:34:07Z",
        "keyMaterial": "******"
      }
    ],
    "encryptionApproach": "nodeSecretManager",
    "canBeCached": true,
    "nextRotationTime": "2025-07-31T19:27:19Z",
    "autoRotation": true,
    "rotationIntervalInDays": 90
  },
  "id": 13,
  "name": "Example Auto-Generated Key",
  "type": "cb-server-managed-aes-key-256",
  "usage": [
    "bucket-encryption",
    "config-encryption",
    "log-encryption"
  ],
  "creationDateTime": "2025-05-02T19:34:07Z"
}
```

## [](#test-key)Test Existing Encryption-at-Rest Key

Test an encryption-at-rest keys defined in the cluster. Couchbase Server does not verify that a key is valid when creating it. You can use this call to verify that the key is valid and can encrypt data before you assign it to encrypt data or another key.

Test a Key

POST /settings/encryptionKeys/{KEY_ID}/test

Path Parameters

`KEY_ID` (integer)

The `id` attribute of the key you want to test. See the [example](#gey-keys-example) for an explanation of getting this value.

### [](#curl-syntax-3)curl Syntax

```bash
curl -sS -u $USER:$PASSWORD \
     -X POST 'http[s]://<hostname>:{PORT}/settings/encryptionKeys/{KEY_ID}/test'
```

Path Parameters

`USER`

The name of a user who has one of the roles listed in [Required Privileges](#test-privs).

`PASSWORD`

The password for the `user`.

`host`

Hostname or IP address of a Couchbase Server node.

`port`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

`KEY_ID`

The `id` attribute of the encryption-at-rest key that you want to test.

### [](#test-privs)Required Privileges

You must have at least one of the following roles:

* [External User Admin](../../../learn/security/roles.md#security%5Fadmin%5Fexternal)
* [Full Admin](../../../learn/security/roles.md#admin)
* [Local User Admin](../../../learn/security/roles.md#security%5Fadmin%5Flocal)
* [Read-Only Admin](../../../learn/security/roles.md#read-only-admin)
* [Security Admin](../../../learn/security/roles.md#security%5Fadmin)

### [](#responses-3)Responses

`200 OK`

If Couchbase Server was able to use the key to encrypt and decrypt some sample data, it just returns this return code and nothing else.

`404 Object Not Found`

Returned if you specified a `KEY_ID` path parameter which does not match the ID of an encryption-at-rest key.

`400 Bad Request`

Returned if the key you tried to test is misconfigured or cannot access the remote KMS. You also receive an error message in JSON format describing the problem.

### [](#gey-keys-example)Examples

The following example tests the encryption-at-rest key with `id` 2.

```bash
 curl -v -u Administrator:password \
      -X POST 'http://127.0.0.1:8091/settings/encryptionKeys/2/test'
```

If successful, the previous example just returns the `200 OK` status code and nothing else. The verbose output of the `curl` command looks like this (notice the `HTTP/1.1 200 OK` indicating the successful call):

```console
*   Trying 127.0.0.1:8091...
* Connected to 127.0.0.1 (127.0.0.1) port 8091
* Server auth using Basic with user 'Administrator'
> POST /settings/encryptionKeys/2/test HTTP/1.1
> Host: 127.0.0.1:8091
> Authorization: Basic QWRtaW5pc3RyYXRvcjpwYXNzd29yZA==
> User-Agent: curl/8.7.1
> Accept: */*
>
* Request completely sent off
< HTTP/1.1 200 OK
< Cache-Control: no-cache,no-store,must-revalidate
< Content-Length: 0
< Date: Tue, 05 Aug 2025 14:42:23 GMT
< Expires: Thu, 01 Jan 1970 00:00:00 GMT
< Pragma: no-cache
< Server: Couchbase Server
< X-Content-Type-Options: nosniff
< X-Frame-Options: DENY
< X-Permitted-Cross-Domain-Policies: none
< X-XSS-Protection: 1; mode=block
<
* Connection #0 to host 127.0.0.1 left intact
```

## [](#test-key-changes)Test Possible Changes to an Encryption-at-Rest Key

You can test changes you want to make to an encryption-at-rest key managed by a remote KMS before you actually make them. Calling this REST API method does not actually make the changes to the key. It just tests an altered copy of the key to determine if it able to encrypt and decrypt data. The call to this API method is the same as altering the key using the [Create or Update an Encryption-at-Rest Key](#create-key) API method, except it adds a `/test` suffix to the URL.

> [!NOTE]
> This endpoint only works for AWS and KMIP keys. It does not work for Couchbase Server managed keys.

Test Possible CHanges to a Key

PUT /settings/encryptionKeys/{KEY_ID}/test

Path Parameters

`KEY_ID` (integer)

The `id` attribute of the key you want to test. See the [example](#gey-keys-example) for an explanation of getting this value.

### [](#curl-syntax-4)curl Syntax

```bash
curl -sS -u $USER:$PASSWORD \
     -X PUT 'http[s]://<hostname>:{PORT}/settings/encryptionKeys/{KEY_ID}/test'
{
  "name": "<keyname>",
  "usage": [
    "<usage>"[."<usage>"...]
  ],
  "type": "<KMS>",
  "data": {
    <KMS-specific-fields>
  }
}
EOF
```

Path Parameters

`USER`

The name of a user who has one of the roles listed in [Required Privileges](#test-changes-privs).

`PASSWORD`

The password for the `user`.

`host`

Hostname or IP address of a Couchbase Server node.

`port`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

`KEY_ID`

The id of the single encryption-at-rest key that you want to test.

Fields

`name` (required)

A name to give to the key. This name must be different from any other encryption-at-rest key.

`usage`

A comma-separated list of what this key can encrypt. Allowed values for this list are:

* `"KEK-encryption"`: Can encrypt other encryption-at-rest keys (KEK).
* `"bucket-encryption"`: Can encrypt any bucket in the cluster.
* `"bucket-encryotion-<bucket-name>"`: Can encrypt the bucket named `bucket-name`. You can include multiple instances of this value to list specific buckets the key can encrypt.
* `"config-encryption"`: Can encrypt configuration information.
* `"log-encryption"`: Can encrypt logs.
* `"audit-encryption"`: Can encrypt audit data.

`type`

Defines the encryption standard and the key management system for the key. All encryption-at-rest keys use AES 256 encryption. Allowed values are:

* `"awskms-symmetric-key"`: AWS KMS manages the key.
* `"kmip-aes-key-256"`: A KMIP-compatible KMS manages the key.
* `"cb-server-managed-aes-key-256"`: Couchbase Server manages the key.

`data`

The contents of the `data` object depend on the KMS set in the `type` field because each KMS has unique settings.

* AWS
* KMIP KMS

When using the AWS KMS, the `data` object has the following schema:

```json
  "data": {
    "keyARN": "<arn>",
    "region": "<region>",
    "useIMDS": <true|false>,
    "profile": "<profile-file-path>",
    "credentiials-file": "<credential-file-path>",
    "configFile": "<config-file-path>"
  }
```

Fields

* `keyARN`: The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that identifies the encryption key in the AWS KMS.
* `region` (optional): The region hosting your AWS KMS.
* `useIMDS` (Boolean, optional): Whether to use Amazon's [Instance Metadata Service (IMD)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) when contacting the AWS KMS. Set this to `true` when your cluster runs on AWS EC2 instances. Defaults to `false`.

You must give Couchbase Server a way to authenticate with the AWS KMS. See Amazon's [KMS key access and permissions](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html) for details of configuring authentication.

You can use [IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html) to allow Couchbase Server to transparently connect to the AWS KMS. If you configure IAM, you do not need any additional authentication configuration within Couchbase Server. Always use this method if your database runs on an AWS EC2 cluster. It's also possible to configure IAM for your cluster when it's not running in AWS. See the AWS documentation for using [IAM Roles Anywhere](https://docs.aws.amazon.com/IAM/latest/UserGuide/id%5Froles%5Fcommon-scenarios%5Fnon-aws.html).

The other authentication method is to use three optional parameters to pass Couchbase Server the necessary credentials in several files. These files must exist on all servers in your cluster.

Use the following parameters to tell Couchbase Server where these files are located:

* `credentials-file` the absolute path to a file containing the AWS credentials to use when authenticating with the AWS KMS. When you supply this path, the file must exist on all nodes. This file often stored at `~/.aws/credentials` on Linux systems. For example:  
```ini  
[my-profile]  
aws_access_key_id = ABCDE...  
aws_secret_access_key = xyz123...  
```
* `configFile`: the absolute path to a file that defines one or more profiles for accessing AWS. This file is often stored in `~/.aws/config` on Linux systems. The format of  
```ini  
[profile profile-name]  
region = us-east-1  
output = json  
role_arn = arn:aws:iam::123456789012:role/RoleName  
source_profile = base  
```
* `profile`: The name of the profile defined in the configuration file to use when authenticating with AWS KMS.

> [!NOTE]
> Couchbase Server does not verify the information you give it during key creation. It only attempts to connect to AWS when you select the key to encrypt data or another key. See [Test an Encryption-at-Rest Key](#test-key) to learn how to test the key.

When using a KMIP-compatible KMS, the `data` object has the following schema:

```json
"data": {
      "port": <kms-port>,
      "host": "<kms-host-url>",
      "reqTimeoutMs": <timeout-ms>,
      "keyPath": "<path-to-key-pem>",
      "keyPassphrase": "<passphrase>",
      "encryptionApproach": "<local-or-kms>",
      "certPath": "<certificate-path>",
      "caSelection": "<trust-store>",
      "encryptionApproach": "<password-or-key>",
      "activeKey": {
        "kmipId": "<kmip-KEY_ID>"
      },
      "encryptionApproachKeyId": <local-KEY_ID>
    }
```

Fields

* `port`: Integer port number for the KMS server. Most KMS servers use port 5696.
* `host`: The URL for the KMS.
* `reqTimeoutMs` (integer, optional): The timeout for network communication with the KMS in milliseconds. Defaults to 1000.
* `keyPath`: Absolute path on each server to the private key Couchbase Server uses to authenticate with the KMS. This key file must be in PEM format.
* `keyPassphrase` (optional): The private key's passphrase, if it has one.
* `encryptionApproach`: Controls which system performs the decryption of keys. Can be one of the following values:

  * `"useGet"`: Couchbase Server retrieves the encryption key from the KMS and uses it to decrypt local DEKs and encryption keys.
  * `"useEncryptDecrypt"`: Send local DEKs and encryption keys to the KMS. The KMS decrypts the keys locally and returns the decrypted keys back to Couchbase Server.
* `certPath`: The absolute path on all servers to the certificate to use when authenticating with the KMS. The certificate file must be in PEM format.
* `caSelection` (optional): Where to look for certificates when verifying the identity of the KMS. Can be one of the following values:

  * `"useSysAndCbCa"` (default): Use the certificates in both the operating system's and Couchbase Server's trust stores.
  * `"useSysCa"`: Use the certificates in the operating system's trust store.
  * `"useCbCa"`: Use the certificates in Couchbase Server's trust store.
  * `"skipServerCertVerification"`: Skip verification of the KMS.  
  > [!CAUTION]  
  > Not verifying the identity of the KMS is insecure.
* `encryptionApproach` (optional): controls how the passphrase for the private key is encrypted for local storage. The two options are:

  * `"nodeSecretManager"` (default): Couchbase Server encrypts the passphrase using the [master password](../../../manage/manage-security/manage-system-secrets.md#setting-the-master-password).
  * `"encryptionKey"`: Use a KEK-enabled encryption key to encrypt the passphrase. If you choose this option, you must also supply the `encryptionApproachKeyId` parameter.
* `activeKey.kmipId`: The ID of the encryption key stored in the KMS. The format of this value depends on the KMS. It's often in the form of a UUID or a friendly name.
* `encryptionWithKeyId` (integer): The `id` attribute of the encryption key Couchbase Server uses to encrypt the private key's passphrase when storing it locally. See [List Encryption-at-Rest Keys](#list-keys) to learn how to get an encryption key's `id`. Required if you set `encryptWith` to `encryptionKey`.

> [!NOTE]
> Couchbase Server does not verify the information you give it during key creation. It only attempts to connect to the KMS when you assign the key to encrypt something. See [Test an Encryption-at-Rest Key](#test-key) to learn how to test the key.

### [](#test-changes-privs)Required Privileges

The role you need to test changes to a key depends on what the key you're testing can encrypt:

For keys that can encrypt audit, configuration, or log data or can encrypt other encryption-at-rest keys (KEKs), you must have one or more of the following roles:

* [Full Admin](../../../learn/security/roles.md#admin)
* [Security Admin](../../../learn/security/roles.md#security-admin)

For keys that can encrypt any bucket in the cluster, you must have one or more of the following roles:

* [Backup Full Admin](../../../learn/security/roles.md#admin)
* [Cluster Admin](../../../learn/security/roles.md#cluster-admin)
* [Eventing Full Admin](../../../learn/security/roles.md#eventing-full-admin)
* [Full Admin](../../../learn/security/roles.md#admin)
* [Security Admin](../../../learn/security/roles.md#security-admin)

For keys that can encrypt one or more specific buckets, you must have one or more of the following roles:

* [Backup Full Admin](../../../learn/security/roles.md#admin)
* [Bucket Admin](../../../learn/security/roles.md#backup-full-admin) that has privileges on the bucket to be encrypted.
* [Cluster Admin](../../../learn/security/roles.md#cluster-admin)
* [Eventing Full Admin](../../../learn/security/roles.md#eventing-full-admin)
* [Full Admin](../../../learn/security/roles.md#admin)
* [Security Admin](../../../learn/security/roles.md#security-admin)

### [](#responses-4)Responses

`200 OK`

Couchbase Server returns this status and nothing else if it was able encrypt and decrypt some sample data with your changes applied to the key.

`404 Object Not Found`

Returned if you specified a `KEY_ID` path parameter which does not match the ID of an encryption-at-rest key.

`400 Bad Request`

Returned if the key you tried to test is misconfigured or cannot access the remote KMS. Couchbase Server also returns an error message in JSON format describing the problem. For example, the following error message occurs when Couchbase Server cannot unlock the key file specified in the `keyPath` field:

```json
{
  "errors": {
    "_": "Encryption key test failed on node1.:8091, node2.:8091, node3.:8091: encryption failed: incorrect password for private key: full error: x509KeyPair: parsePrivateKey returned err: parsePrivateKey: failed to parse private key. Error: asn1: structure error: tags don't match (2 vs {class:0 tag:16 length:95 isCompound:true}) {optional:false explicit:false application:false private:false defaultValue:<nil> tag:<nil> stringType:0 timeType:0 set:false omitEmpty:false} int @2; pkcs8: incorrect password; x509: failed to parse EC private key: asn1: structure error: tags don't match (2 vs {class:0 tag:16 length:95 isCompound:true}) {optional:false explicit:false application:false private:false defaultValue:<nil> tag:<nil> stringType:0 timeType:0 set:false omitEmpty:false} int @2"
  }
}
```

### [](#test-changes-example)Example

The following example tests changing the hostname of the KMIP key created in [Create a KMIP-compatible KMS Managed Key](#create-kmip-example).

```bash
 curl -v -u Administrator:password  \
     -X PUT   http://127.0.0.1:8091/settings/encryptionKeys/1/test \
       --data-binary @- <<EOF | jq
{
  "name": "Example KMIP Key",
  "type": "kmip-aes-key-256",
  "usage": [
    "KEK-encryption"
  ],
"data": {
      "port": 5696,
      "host": "https://kms2.example.com",
      "keyPath": "/scripts/certs/cb_key.pem",
      "certPath": "/scripts/certs/cb_cert.pem",
      "activeKey": {
        "kmipId": "0788edb1-1418-4225-903b-bc1f9f59aa4d"
      }
  }
}
EOF
```

The previous example returns the code `200 OK` if the test was successful with no further output.

## [](#delete-key)Delete an Encryption-at-Rest Key

You can delete an encryption-at-rest key as long as Couchbase Server is not using it to encrypt data or another encryption key.

Delete an Encryption Key

DELETE /settings/encryptionKeys/{KEY_ID}

Path Parameters

`KEY_ID` (integer)

The `id` attribute of the key you want to delete.

### [](#curl-syntax-5)curl Syntax

```bash
curl -sS -u $USER:$PASSWORD   -X DELETE \
     'http://{HOST}:{PORT}/settings/encryptionKeys/{KEY_ID}'
```

Path Parameters

`USER`

The name of a user who has one of the roles listed in [Required Privileges](#del-privs).

`PASSWORD`

The password for the `user`.

`host`

Hostname or IP address of a Couchbase Server node.

`port`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

`KEY_ID` (integer)

The `id` attribute of the key you want to delete.

### [](#del-privs)Required Privileges

The role you need to delete a key depends on what the key you're deleting can encrypt:

For keys that can encrypt audit, configuration, or log data or can encrypt other encryption-at-rest keys (KEKs), you must have one or more of the following roles:

* [Full Admin](../../../learn/security/roles.md#admin)
* [Security Admin](../../../learn/security/roles.md#security-admin)

For keys that can encrypt any bucket in the cluster, you must have one or more of the following roles:

* [Backup Full Admin](../../../learn/security/roles.md#admin)
* [Cluster Admin](../../../learn/security/roles.md#cluster-admin)
* [Eventing Full Admin](../../../learn/security/roles.md#eventing-full-admin)
* [Full Admin](../../../learn/security/roles.md#admin)
* [Security Admin](../../../learn/security/roles.md#security-admin)

For keys that can encrypt one or more specific buckets, you must have one or more of the following roles:

* [Backup Full Admin](../../../learn/security/roles.md#admin)
* [Bucket Admin](../../../learn/security/roles.md#backup-full-admin) that has privileges on the bucket to be encrypted.
* [Cluster Admin](../../../learn/security/roles.md#cluster-admin)
* [Eventing Full Admin](../../../learn/security/roles.md#eventing-full-admin)
* [Full Admin](../../../learn/security/roles.md#admin)
* [Security Admin](../../../learn/security/roles.md#security-admin)

### [](#responses-5)Responses

`200 OK`

Returned when Couchbase Server was able to delete the key. A successful call does not return any additional message.

`400 Bad Request`

Returned when the key you tried to delete is in use. In addition, you receive a JSON message that explains why Couchbase Server cannot delete the key. For example:

```json
{
  "errors": {
    "_": "Can't be removed because this key is configured to encrypt configuration, logs,
          audit, bucket \"beer-sample\", keys \"encrypted-with-kek\", \"kmip-key\""
  }
}
```

`404 Object Not Found`

Returned if the key you tried to delete does not exist.

### [](#examples)Examples

The following example deletes the Couchbase Server managed key named Example Auto-Generated Key shown in earlier examples.

Unresolved include directive in modules/rest-api/pages/security/encryption-at-rest/manage-encryption-keys.adoc - include::example$encryption-at-rest/manage-encryption-kets.adoc\[\]