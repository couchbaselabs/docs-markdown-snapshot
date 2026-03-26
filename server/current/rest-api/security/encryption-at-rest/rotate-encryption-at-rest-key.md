---
title: Rotate Data Encryption Keys
description: You can use the REST API have Couchbase Server immediately rotate
  an encryption-at-rest key that it manages.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/security/encryption-at-rest/rotate-encryption-at-rest-key.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:rest-api:security/encryption-at-rest/rotate-encryption-at-rest-key.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/rest-api/security/encryption-at-rest/rotate-encryption-at-rest-key.html)

# Rotate Data Encryption Keys

> You can use the REST API have Couchbase Server immediately rotate an encryption-at-rest key that it manages. 

## [](#description)Description

You can manually trigger the rotation of an encryption-at-rest key that Couchbase Server manages. You may want to manually rotate the key if you believe it's compromised.

You can only rotate keys managed by an external KMS through that KMS. See [Manually Rotate Encryption-at-rest Keys](#manage:security/manage-native-encryption-at-rest.adoc#rotate-keys) for more information.

When you rotate an encryption-at-rest key, Couchbase Server creates a new key and uses it to re-encrypt all DEKs that were encrypted with the previous version of the key.

See [Encryption Key Rotation and Expiration](../../../learn/security/native-encryption-at-rest-overview.md#rotation-expiration) for more information about key rotation.

## [](#http-methods)HTTP Methods

This API endpoint supports the following methods:

* [Rotate an Encryption-at-Rest Key](#rotate-key)

## [](#rotate-key)Rotate an Encryption-at-Rest Key

Use this endpoint to rotate an encryption-at-rest key.

Rotate a Key

POST /controller/rotateEncryptionKey/{KEY_ID}

Path Parameters

`KEY_ID` (integer, required)

The encryption-at-rest key to rotate identified by its `data.id` value. See [List Encryption-at-Rest Keys](#manage-encryption-keys.adoc#list-keys) to learn how to get the `data.id` value of the key you want to rotate.

### [](#curl-syntax)curl Syntax

```bash
 curl -u $USER:$PASSWORD -X GET \
      'http://{HOST}:{PORT}//controller/rotateEncryptionKey/{KEY_ID}' | jq
```

Path Parameters

`USER`

The name of a user who has one of the roles listed in [Required Privileges](#rotate-privs).

`PASSWORD`

The password for the `user`.

`host`

Hostname or IP address of a Couchbase Server node.

`port`

Port number for the REST API. Defaults are 8091 for unencrypted and 18901 for encrypted connections.

`KEY_ID` (integer, required)

The encryption-at-rest key to rotate identified by its `data.id` value. See [List Encryption-at-Rest Keys](#manage-encryption-keys.adoc#list-keys) to learn how to get the `data.id` value of the key you want to rotate.

### [](#rotate-privs)Required Privileges

You must have at least one of the following roles:

* [Full Admin](../../../learn/security/roles.md#admin)
* [Security Admin](../../../learn/security/roles.md#security%5Fadmin)

### [](#responses)Responses

`200 OK`

Does not return any other message other than the response code.

`403 Forbidden`

Returned if the user does not have one of the roles listed in [Required Privileges](#rotate-privs).

`404 Object Not Found`

Returned if the `KEY_ID` does not match an encryption-at-rest key.

### [](#gey-keys-example)Examples

The following example rotates the encryption-at-rest key for the named `Example Auto-Generated Key`:

```json
 {
  "data": {
    "keys": [
      {
        "id": "5fb1ef72-b3db-47f3-b989-0c156ee6eb40",
        "active": true,
        "creationDateTime": "2025-05-07T14:11:53Z",
        "keyMaterial": "******"
      }
    ],
    "encryptionApproach": "nodeSecretManager",
    "canBeCached": true,
    "autoRotation": false
  },
  "id": 18,
  "name": "Example Auto-Generated Key",
  "type": "cb-server-managed-aes-key-256",
  "usage": [
    "KEK-encryption",
    "bucket-encryption",
    "config-encryption",
    "log-encryption",
    "audit-encryption"
  ],
  "creationDateTime": "2025-05-07T14:11:53Z"
}
```

This key's `data.id` is `18`. The command to rotate this key is:

```bash
curl -u Administrator:password \
     -X POST 'http://127.0.0.1:8091/controller/rotateEncryptionKey/18'
```

This command does not return output. To see its effect, you can call the `/settings/encryptionKey/` endpoint (see [List Encryption-at-Rest Keys](manage-encryption-keys.md#list-keys) for details) to get the current status of the key:

```bash
 curl -u Administrator:password -X GET \
      http://127.0.0.1:8091/settings/encryptionKeys/18 | jq
```

The JSON returned by this command shows the encryption-at-rest has a new key within the `data.keys` object whose `active` attribute is `true`:

```json
{
  "data": {
    "keys": [
      {
        "id": "3887ad84-7535-4d54-a9d2-fd9d855985b6",
        "active": true,
        "creationDateTime": "2025-05-09T12:49:01Z",
        "keyMaterial": "******"
      },
      {
        "id": "5fb1ef72-b3db-47f3-b989-0c156ee6eb40",
        "active": false,
        "creationDateTime": "2025-05-07T14:11:53Z",
        "keyMaterial": "******"
      }
    ],
    "encryptionApproach": "nodeSecretManager",
    "lastRotationTime": "2025-05-09T12:49:01Z",
    "canBeCached": true,
    "autoRotation": false
  },
  "id": 18,
  "name": "Example Auto-Generated Key",
  "type": "cb-server-managed-aes-key-256",
  "usage": [
    "KEK-encryption",
    "bucket-encryption",
    "config-encryption",
    "log-encryption",
    "audit-encryption"
  ],
  "creationDateTime": "2025-05-07T14:11:53Z"
}
```