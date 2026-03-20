---
title: cbbackupmgr encryption
description: Creating and managing encrypted backups (Developer Preview)
editUrl: https://github.com/couchbase/backup/edit/neo/docs/modules/backup-restore/pages/cbbackupmgr-encryption.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:backup-restore:cbbackupmgr-encryption.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/backup-restore/cbbackupmgr-encryption.html)

# cbbackupmgr encryption

Creating and managing encrypted backups (Developer Preview)

## [](#description)DESCRIPTION

A tutorial that explains how to use the encryption feature of cbbackupmgr Enterprise Edition.

## [](#tutorial)TUTORIAL

In this tutorial we will cover how to create encrypted backup repositories as well as how to do backups, merges and restores in said repositories. To follow this tutorial you will need an Enterprise Edition version of cbbackupmgr and Couchbase Server. For later steps we will explain how to use external Key Management Solutions (KMS), so you may need access to one of those.

### [](#configuring-a-backup)Configuring a backup

To start using encrypted backups you will need to create a new encrypted backup repository. This can be achieved with the `config` command, it is worth noting the are two separate modes of configuration:

#### [](#1-passphrase-mode-development-only)1\. Passphrase mode (Development Only)

In this mode the command takes a passphrase via the command line argument `--passphrase` or via the `CB_ENCRYPTION_PASSPHRASE` environmental variable.

An example of how to use this new mode is shown below:

$ cbbackupmgr config -a /backups/encrypted -r passphrase_repo --encrypted --passphrase couchbase
Backup repository `passphrase` created successfully in archive `/backups/encrypted`

The passphrase mode uses the given passphrase to derive an encryption key using `ARGONID` by default. The derivation algorithm can be changed using the `--derivation-algo` flag. The resulting key is then used to encrypt the auto-generated repository key which is used to encrypt the backup data. Due to the inherent insecurity of human friendly passphrases using passphrase mode in production is **strongly** discouraged.

#### [](#2-kms-mode)2\. KMS mode

In this mode the command will attempt to communicate with an external KMS to encrypt the repository key. Note that the external key will not directly encrypt the data but instead envelopes the encryption key used to encrypt the data. This minimizes the number of request done to the external KMS as well as the system latency.

The currently supported external KMS are:

1. [Amazon Web Services Key Management Service (AWS KMS)](https://aws.amazon.com/kms/)
2. [Google Cloud Key Management Service (GCP KMS)](https://cloud.google.com/security-key-management)
3. [Azure Key Vault](https://azure.microsoft.com/en-gb/services/key-vault/)
4. [HashiCorp Vault Transit Secret Engine](https://www.vaultproject.io/docs/secrets/transit)

Depending on the KMS you choose the setup will look slightly different but vaguely all four options have the ability to pick up the needed credentials from the environment. In the next sections we will cover each KMS specifics and give examples of how to set up. For all the KMSs you will have to provide a URL to the key to use for encryption. This is done via the `--km-key-url`or the `CB_KM_KEY_URL` environmental variable. The schema varies between provider but will be covered in the following sections.

By default, when configuring backups the encryption algorithm will be set to AES256GCM. It can be changed to AES256CBC by using the option `--encryption-algo AES256CBC`.

##### [](#aws-kms)AWS KMS

To use AWS KMS you provide the URL to the [Key Identifier](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id)and prefix it with `awskms://`, for AWS you must also provide the region via the `--km-region` environmental variable.

The supported authorization techniques are:

1. When running in EC2, credentials may be obtained via the instance metadata service by setting/supplying:

  * `CB_AWS_ENABLE_EC2_METADATA=true`
2. Providing a set of environment variables including:

  * `CB_KM_ACCESS_KEY_ID`
  * `CB_KM_SECRET_ACCESS_KEY`
3. Loading credentials from the shared config files located at:

  * `$HOME/.aws/config`
  * `$HOME/.aws/credentials`
4. Providing static config/credentials using the cli flags:

  * `--km-access-key-id`
  * `--km-secret-access-key`

Below is an example of configuring an encrypted repository using AWS:

$ cbbackupmgr config -a /backups/encrypted -r aws_repo --encrypted \
  --km-key-url 'awskms://alias/cbbackupmgrEncrypt' --km-region 'us-east-1'

Note that if you want to use a private cloud compatible with AWS KMS you can provide `--km-endpoint` to override the AWS endpoint.

##### [](#gcp-kms)GCP KMS

To use GCP KMS you have to provide the [Key Resource ID](https://cloud.google.com/kms/docs/resource-hierarchy#key)prefixed with `gcpkms://` either via the environment, or the CLI flag

The supported authorization techniques are:

1. When running in Google Compute Engine it can be retrieved from the environment automatically.
2. A service account can be pass via the `GOOGLE_APPLICATION_CREDENTIALS`environmental variable.
3. Explicitly passing the path to a service auth file using either:

  * `--km-auth-file` CLI argument
  * `CB_KM_AUTH_FILE` environmental variable

For more information refer to [GCPs documentation](https://cloud.google.com/kms/docs/accessing-the-api).

An example of configuring an encrypted repository using GCP can be seen below.

$ cbbackupmgr config -a /backups/encrypted -r gcp_repo --encrypted \
  --km-key-url gcpkms://projects/project-id/locations/location/keyRings/keyring/cryptoKeys/key

##### [](#azure-key-vault)Azure Key Vault

To use Azure Key Vault you have to provide the URL to the [Key ID](https://docs.microsoft.com/en-us/azure/key-vault/general/about-keys-secrets-certificates#objects-identifiers-and-versioning)prefixed with `azurekeyvault://` via either the CLI or environmental variables.

The supported authorization techniques are:

1. Via the Azure environmental variables as described by the [Azure documentation](https://docs.microsoft.com/en-us/azure/developer/go/azure-sdk-authorization).
2. Using the `AZURE_AUTH_LOCATION` environmental variable to point to an Azure auth setting file.

An example of configuring an encrypted repository using Azure can be seen below.

$ cbbackupmgr config -a /backups/encrypted -r azure_repo --encrypted \
  --km-key-url azurekeyvault://{vault-name}.vault.azure.net/{object-type}/{object-name}/{object-version}

##### [](#hashicorp-vault-transit-engine)HashiCorp Vault Transit Engine

To use HashiCorp Vault Transit engine you have to provide the URL to the key ID in the form `[hashivault|hashivaults]://{host}/{key name}`. If `hashivaults` used then HTTPS will be used to connect to the transit engine.

For HashiCorp vault the only accepted authorization method is TOKEN auth. This can be provided either via: \* `--km-secret-access-key` CLI argument \* `` CB_KM_SECRET_ACCESS_KEY` `` environmental variable

An example of configuring an encrypted repository using HashiCorp Vault Transit Engine can be seen below.

$ cbbackupmgr config -a /backups/encrypted -r hashicorp_repo --encrypted \
  --km-key-url hashivault://127.0.0.1:8200/key --km-secret-access-key my_token

### [](#running-encrypted-backups)Running encrypted backups

For the examples below we will use 'passphrase mode', but they will work the same with the 'KMS mode' if you replace the `--passphrase` flag with the corresponding KMS flags.

To run an encrypted backup you have to first configure you repository as described in the previous section. Once your encrypted repository is configured you can run the backup as follows:

$ cbbackupmgr backup -c https://localhost:18091 -u Administrator -p asdasd \
  -a /backups/encrypted -r passphrase_repo --passphrase couchbase
Backing up to '2021-06-17T16_35_45.08865997+01_00'
Copied all data in 16.746s (Avg. 2.84MiB/Sec)                                                                                                                                                                                           63288 items / 45.50MiB
[====================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 2.84MiB           | Thu, 17 Jun 2021 16:35:45 +0100/s | Thu, 17 Jun 2021 16:36:01 +0100 | 16.788s  |

| Bucket
| ------
| Name          | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| travel-sample | Succeeded | 45.50MiB    | 2.84MiB/s         | Thu, 17 Jun 2021 16:35:45 +0100 | Thu, 17 Jun 2021 16:36:01 +0100 | 16.427s  |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 63288    | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

Backup completed successfully

When doing encrypted backups you will notice that it is slightly slower and uses slightly more space. This is due to the overhead caused by encrypting the data, and it is to be expected.

If the passphrase or the KMS details are missing when attempting to do a backup `cbbackupmgr` will fail and return an error asking for the correct credentials.

Note that when using encrypted backups you should always use `https` as encrypted backups work locally. Thus, if `http` is used the data will be transmitted over the network unencrypted and then encrypted once it reaches the backup client.

#### [](#encrypted-restores)Encrypted restores

To restore an encrypted backup use the following command:

$ cbbackupmgr restore -c https://localhost:18091 -u Administrator -p asdasd \
  -a /backups/encrypted -r passphrase_repo --passphrase couchbase
(1/1) Restoring backup '2021-06-17T16_35_45.08865997+01_00'
Copied all data in 2.03s (Avg. 20.75MiB/Sec)                                                                                                                                                                                            63288 items / 41.49MiB
[===================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 20.75MiB          | Thu, 17 Jun 2021 16:54:32 +0100/s | Thu, 17 Jun 2021 16:54:34 +0100 | 2.061s   |

| Bucket
| ------
| Name          | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| travel-sample | Succeeded | 41.49MiB    | 41.49MiB/s        | Thu, 17 Jun 2021 16:54:32 +0100 | Thu, 17 Jun 2021 16:54:34 +0100 | 1.952s   |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 63288    | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

Restore completed successfully

Similar to the backup process, restore will also be slightly slower than its plain text counter-part, and you should use the `https` endpoints to make sure that the process is encrypted end-to-end.

#### [](#info-for-encrypted-repositories)Info for encrypted repositories

The `info` command does not require any changes to work with encrypted backups. This is because `info` does not access any of the user data directly it only checks for size and count.

An `info` of an encrypted repository would look as follows:

$ cbbackupmgr info -a /backups/encrypted -r passphrase_repo --depth 4
Name            | Size      | # Backups | Encrypted |
passphrase_repo | 238.15MiB | 2         | true      |

+  Backup                             | Size      | Type | Source         | Cluster UUID                     | Range | Events | Aliases | Complete |
+  2021-06-17T16_35_45.08865997+01_00 | 238.15MiB | FULL | localhost:9000 | 03e85fa504cb5f50fc5ff1722f052754 | N/A   | 0      | 0       | true     |

-    Bucket        | Size      | Items | Mutations | Tombstones | Views | FTS | Indexes | CBAS |
-    travel-sample | 238.15MiB | 63288 | 63288     | 0          | 0     | 0   | 0       | 0    |

~      Scope           | Scope ID | Mutations | Tombstones |
~      _default        | 0        | 31591     | 0          |
~      tenant_agent_04 | 8        | 40        | 0          |
~      tenant_agent_03 | 9        | 33        | 0          |
~      tenant_agent_02 | 10       | 20        | 0          |
~      tenant_agent_01 | 11       | 11        | 0          |
~      tenant_agent_00 | 12       | 2         | 0          |
~      inventory       | 13       | 31591     | 0          |

## [](#discussion)DISCUSSION

In this section we will briefly cover how the encryption model for `cbbackupmgr` works. Whenever an encrypted repository is created the tool will auto-generate an encryption key that we then will encrypt and persist using the external KMS or passphrase provided by the user.

This means that when using an external KMS the tool will only use 1 API call per operation. The only exception is `info` which requires 0.

To avoid issues with repeated nonces we create derived keys per backup, bucket and vBucket, this means that whilst using AES\_256\_GCM we can safely encrypt up to 4.3e12 (4.3 trillion) documents per bucket in each individual backup. After that the chances of repeated nonces increase which weakens the encryption.

## [](#see-also)SEE ALSO

[cbbackupmgr-config](cbbackupmgr-config.md), [cbbackupmgr-backup](cbbackupmgr-backup.md), [cbbackupmgr-restore](cbbackupmgr-restore.md), [cbbackupmgr-merge](cbbackupmgr-merge.md), [cbbackupmgr-examine](cbbackupmgr-examine.md) [cbbackupmgr-info](cbbackupmgr-info.md)

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite