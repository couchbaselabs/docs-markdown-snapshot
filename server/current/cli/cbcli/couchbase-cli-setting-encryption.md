---
title: setting-encryption
description: Manage encryption at-rest settings.
editUrl: https://github.com/couchbase/couchbase-cli/edit/morpheus/docs/modules/cli/pages/cbcli/couchbase-cli-setting-encryption.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:cli:cbcli/couchbase-cli-setting-encryption.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/cli/cbcli/couchbase-cli-setting-encryption.html)

# setting-encryption

Manage encryption at-rest settings.

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-enable_ [--cluster <url>] [--username <user>]
    [--password <password>] [--client-cert <path>] [--client-cert-password <password>]
    [--client-key <path>] [--client-key-password <password>]
    [--get] [--set]
    [--list-keys] [--add-key] [--edit-key <keyid>] [--rotate-key <keyid>]
    [--delete-key <keyid>]
    [--target <target>] [--type <type>] [--key <keyid>]
    [--dek-rotate-every <days>] [--dek-lifetime <days>]
    [--name <name>] [--key-type <type>]
    [--kek-usage] [--config-usage] [--log-usage] [--audit-usage]
    [--all-bucket-usage] [--bucket-usage <bucket>]
    [--cloud-key-arn <arn>] [--cloud-region <region>]
    [--cloud-auth-by-instance-metadata] [--cloud-creds-path <path>]
    [--cloud-config-path <path>] [--cloud-profile-path <path>]
    [--encrypt-with-master-password] [--encrypt-with-key <keyid>]
    [--kmip-operations <ops>] [--kmip-key <key>] [--kmip-host <host>]
    [--kmip-port <port>] [--kmip-key-path <path>] [--kmip-cert-path <path>]
    [--kmip-key-passphrase <passphrase>] [--kmip-server-verification <verification_option>]
    [--auto-rotate-every <days>] [--auto-rotate-start-on <iso8601>]

## [](#description)DESCRIPTION

Allows managing encryption at-rest settings, including create/editing/rotating/deleting keys and choosing what encryption to use for config, logs and audit logs.

The operation the command performs is determined by several mutually exclusive arguments, each having their own set of options:

* `--get`
* `--set`, with the args

  * `--target <target>`, `--type <type>`, `--key <keyid>`, `--dek-rotate-every <days>`, `--dek-lifetime <days>`
* `--list-keys`
* `--add-key`, with the args

  * `--name <name>`, `--key-type <type>`, `--kek-usage`, `--config-usage`, `--log-usage`, `--audit-usage`, `--all-bucket-usage`, `--bucket-usage <bucket>`
  * For AWS keys: `--cloud-key-arn <arn>`, `--cloud-region <region>`, `--cloud-auth-by-instance-metadata`, `--cloud-creds-path <path>`, `--cloud-config-path <path>`, `--cloud-profile-path <path>`
  * For KMIP keys: `--kmip-operations <ops>`, `--kmip-key <key>`, `--kmip-host <host>`, `--kmip-port <port>`, `--kmip-key-path <path>`, `--kmip-cert-path <path>`, `--kmip-key-passphrase <passphrase>`, `--kmip-server-verification <verification_option>` `--encrypt-with-master-password`, `--encrypt-with-key <keyid>`
  * For auto-generated keys: `--auto-rotate-every <days>`, `--auto-rotate-start-on <iso8601>`, `--encrypt-with-master-password`, `--encrypt-with-key <keyid>`
* `--edit-key <keyid>` with the same args as `--add-key`
* `--rotate-key <keyid>`
* `--delete-key <keyid>`

For more information see the examples section.

## [](#options)OPTIONS

\-c

\--cluster

Specifies the hostname of a node in the cluster. See the HOST FORMATS section for more information on specifying a hostname.

\-u

\--username <username>

Specifies the username of the user executing the command. If you do not have a user account with permission to execute the command then it will fail with an unauthorized error.

\-p

\--password <password>

Specifies the password of the user executing the command. If you do not have a user account with permission to execute the command then it will fail with an unauthorized error. If this argument is specified, but no password is given then the command will prompt the user for a password through non-echoed stdin. You may also specify your password by using the environment variable CB\_REST\_PASSWORD.

\--client-cert <path>

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `--client-key` as an alternative to the `--username` and `--password` flags. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-cert-password <password>

The password for the certificate provided to the `--client-cert` flag, when using this flag, the certificate/key pair is expected to be in the PKCS#12 format. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-key <path>

The path to the client private key whose public key is contained in the certificate provided to the `--client-cert` flag. May be supplied with `--client-cert` as an alternative to the `--username` and `--password`flags. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-key-password <password>

The password for the key provided to the `--client-key` flag, when using this flag, the key is expected to be in the PKCS#8 format. See the CERTIFICATE AUTHENTICATION section for more information.

\--get

Gets the encryption settings for configuration, logs and audit logs.

\--set

Sets the encryption settings. `--target` and `--type` must be specified.

\--target <target>

Used with `--set` to determine what encryption settings are being changed. Can be `config`, `log` or `audit`.

\--type <type>

The type of encryption to use. Can be `disabled`, `key` or `master-password`.

\--key <keyid>

The id of the key to use. Should only be passed if `--type` is `key`.

\--dek-rotate-every <days>

How often to rotate the DEK.

\--dek-lifetime <days>

How long the DEKs should be kept for.

\--list-keys

List the keys and their settings in JSON format.

\--add-key

Create a new encryption key.

\--name <name>

The name of the new key.

\--key-type <type>

The type of key to create. Can be `aws`, `kmip` or `auto-generated`.

\--kek-usage

Allow the key to be used as a KEK.

\--config-usage

Allow the key to be used to encrypt the config.

\--log-usage

Allow the key to be used to encrypt logs.

\--audit-usage

Allow the key to be used to encrypt the audit logs.

\--all-bucket-usage

Allow the key to be used to encrypt any bucket. Cannot be used with `--bucket-usage`.

\--bucket-usage <bucket>

Allow the key to be used to encrypt the given bucket. This option can be specified multiple times. Cannot be used with `--all-bucket-usage`.

\--cloud-key-arn <arn>

The ARN of the cloud key.

\--cloud-region <region>

The region the cloud key is in.

\--cloud-auth-by-instance-metadata

When authenticating with the cloud provider, use the IMDS.

\--cloud-creds-path <path>

The path to the cloud credentials.

\--cloud-config-path <path>

The path to the cloud config.

\--cloud-profile-path <path>

The path to the cloud profile.

\--encrypt-with-master-password

Encrypt this key with the master password.

\--encrypt-with-key <keyid>

Encrypt this key with another key.

\--kmip-operations <op>

What operations to use with the KMIP server. Can be `get` or `encrypt-decrypt`.

\--kmip-key <key>

The key on the KMIP server to use.

\--kmip-host <host>

The host of the KMIP server.

\--kmip-port <port>

The port of the KMIP server.

\--kmip-key-path <path>

The path to the client key to use.

\--kmip-cert-path <path>

The path to the certificate to use.

\--kmip-key-passphrase <passphrase>

The passphrase to use to decode the key.

\--kmip-server-verification <verification\_option>

Which certificates should be used for server verification.

\--auto-rotate-every <days>

How often to rotate the generated key, in days.

\--auto-rotate-start-on <iso8601>

When to start rotating, in an ISO 8601 date.

\--edit-key <keyid>

Edit the given key.

\--delete-key <keyid>

Delete the given key.

\--rotate <keyid>

Rotate the given key.

## [](#examples)EXAMPLES

To list the available encryption keys run the following command

$ couchbase-cli setting-encryption -c 192.168.1.5 -u Administrator \
 -p password --list-keys

To get the settings for configuration, logs and audit log encryption

$ couchbase-cli setting-encryption -c 192.168.1.5 -u Administrator \
 -p password --get

To set the configuration settings to be encrypted with the key with the id 2

$ couchbase-cli setting-encryption -c 192.168.1.5 -u Administrator \
 -p password --set --target config --type key --key 2

To encrypt audit logs with the master password, rotating the data encryption key (DEK) every thirty days and keeping the DEKs for sixty days:

$ couchbase-cli setting-encryption -c 192.168.1.5 -u Administrator \
 -p password --set --target config --type master-password \
 --dek-rotate-every 30 --dek-lifetime 60

To disable encryption for logs

$ couchbase-cli setting-encryption -c 192.168.1.5 -u Administrator \
 -p password --set --target log --type disabled

To create a new AWS key called "aws-key", to be used to encrypt other keys, authenticated using IMDS, itself encrypted with the master password

$ couchbase-cli setting-encryption -c 192.168.1.5 -u Administrator \
 -p password --add-key --kek-usage --key-type aws --name aws-key \
 --encrypt-with-master-password --cloud-region us-east-1 \
 --cloud-key-arn arn:aws:kms:us-east-1:123456789012:key-name \
 --cloud-auth-by-instance-metadata

To create a new key from a KMIP server, to be used to encrypt any bucket, itself encrypted with existing key `2`

$ couchbase-cli setting-encryption -c 192.168.1.5 -u Administrator \
 -p password --add-key --all-bucket-usage --key-type kmip --name kmip-key \
 --kmip-operations get --kmip-host localhost --kmip-port 5696
 --encrypt-with-key 2 --kmip-key my-key --kmip-cert-path /tmp/cert \
 --kmip-key-path /tmp/key

To create a new auto-generated key, to be used with the buckets `travel-sample`and `beer-sample`, encrypted with the master password, rotated every 30 days, with the rotation starting at midnight on the first day of 2025.

$ couchbase-cli setting-encryption -c 192.168.1.5 -u Administrator \
 -p password --bucket-usage travel-sample --bucket-usage beer-sample \
 --key-type auto-generated --name auto-key --encrypt-with-master-password \
 --auto-rotate-every 30 --auto-rotate-start-on 2025-01-01T00:00:00Z

To delete the key with the id 2

$ couchbase-cli setting-encryption -c 192.168.1.5 -u Administrator \
 -p password --delete-key 2

To rotate the key with the id 2

$ couchbase-cli setting-encryption -c 192.168.1.5 -u Administrator \
 -p password --rotate-key 2

## [](#environment-and-configuration-variables)ENVIRONMENT AND CONFIGURATION VARIABLES

CB\_REST\_USERNAME

Specifies the username to use when executing the command. This environment variable allows you to specify a default argument for the -u/--username argument on the command line.

CB\_REST\_PASSWORD

Specifies the password of the user executing the command. This environment variable allows you to specify a default argument for the -p/--password argument on the command line. It also allows the user to ensure that their password are not cached in their command line history.

CB\_CLIENT\_CERT

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `CB_CLIENT_KEY` as an alternative to the `CB_USERNAME` and `CB_PASSWORD` variables. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_CERT\_PASSWORD

The password for the certificate provided to the `CB_CLIENT_CERT` variable, when using this variable, the certificate/key pair is expected to be in the PKCS#12 format. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_KEY

The path to the client private key whose public key is contained in the certificate provided to the `CB_CLIENT_CERT` variable. May be supplied with `CB_CLIENT_CERT` as an alternative to the `CB_USERNAME` and `CB_PASSWORD`variables. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_KEY\_PASSWORD

The password for the key provided to the `CB_CLIENT_KEY` variable, when using this variable, the key is expected to be in the PKCS#8 format. See the CERTIFICATE AUTHENTICATION section for more information.

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite