---
title: Encryption-at-Rest API
description: The encryption-at-rest API lets you encrypt audit, configuration,
  logging, and bucket data when written to disk.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/security/encryption-at-rest/encryption-at-rest.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/rest-api/security/encryption-at-rest/encryption-at-rest.html)

# Encryption-at-Rest API

> The encryption-at-rest API lets you encrypt audit, configuration, logging, and bucket data when written to disk. See [Native Encryption at Rest](../../../learn/security/native-encryption-at-rest-overview.md) for more information. 

## [](#apis-in-this-section)APIs in this Section

| HTTP Method | URI                                                        | Documented at                                                                                                         |
| ----------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| GET         | /settings/encryptionKeys/                                  | [List Encryption-at-Rest Keys](manage-encryption-keys.md#list-keys)                                                   |
| GET         | /settings/encryptionKeys/{KEY\_ID}                         | [List Single Encryption-at-Rest Key](manage-encryption-keys.md#list-keys)                                             |
| POST        | /settings/encryptionKeys                                   | [Create an Encryption-at-Rest Key](manage-encryption-keys.md#create-key)                                              |
| POST        | /settings/encryptionKeys/{KEY\_ID}/test                    | [Test an Encryption-at-Rest Key](manage-encryption-keys.md#test-key)                                                  |
| PUT         | /settings/encryptionKeys/{KEY\_ID}                         | [Update an Encryption-at-Rest Key](manage-encryption-keys.md#create-key)                                              |
| PUT         | /settings/encryptionKeys/{KEY\_ID}/test                    | [Test changes to an Encryption-at-Rest Key](manage-encryption-keys.md#test-key-changes)                               |
| DELETE      | /settings/encryptionKeys/{KEY\_ID}                         | [Delete an Encryption-at-Rest Key](manage-encryption-keys.md#delete-key)                                              |
| GET         | /settings/security/encryptionAtRest                        | [Get Audit, Config, and Log Encryption-at-Rest Settings](manage-system-encryption-at-rest.md#get-settings)            |
| POST        | /settings/security/encryptionAtRest                        | [Change Audit, Config, and Log Data Encryption-at-Rest Settings](manage-system-encryption-at-rest.md#change-settings) |
| POST        | /controller/dropEncryptionAtRestDeks/bucket/{BUCKET\_NAME} | [Rotate DEKs for Bucket and Re-encrypt Data](drop-encryption-deks.md#drop-bucket)                                     |
| POST        | /controller/dropEncryptionAtRestDeks/{TYPE}                | [Rotate DEKs and Re-encrypt Data for a Type of Encrypted Data](drop-encryption-deks.md#drop-type)                     |
| POST        | /controller/rotateEncryptionKey/{KEY\_ID}                  | [Rotate Encryption-at-Rest Key](rotate-encryption-at-rest-key.md#rotate-key)                                          |
| POST        | /controller/forceEncryptionAtRest/bucket/{BUCKET\_NAME}    | [Force Encryption of Unencrypted Bucket Data](force-encryption-at-rest.md#bucket)                                     |
| POST        | /controller/forceEncryptionAtRest/{TYPE}                   | [Force Encryption of Unencrypted Data of a Type](force-encryption-at-rest.md#type)                                    |