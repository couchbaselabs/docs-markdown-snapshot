---
title: Manage System Secrets
description: System secrets can be managed with a special degree of security.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/manage/pages/manage-security/manage-system-secrets.adoc
  xref: xref:enterprise-analytics:manage:manage-security/manage-system-secrets.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/manage/manage-security/manage-system-secrets.html)

# Manage System Secrets

> System secrets can be managed with a special degree of security. 

## [](#understanding-system-secrets)Understanding System Secrets

_Secrets Management_ (which is an Enterprise-Edition feature of Operational Insights) allows system secrets to be written to disk in encrypted format. _Secrets_ are Operational Insights-defined, and include system-essential passwords and certificates. Couchbase uses an AES 256-bit algorithm in GCM mode, to encrypt secrets using an encryption hierarchy.

## [](#setting-the-master-password)Setting the Master Password

Secrets Management is an optional feature that only works when the _master password_ is set individually for each Couchbase-Server node. Once the master password is established for a node, whenever that node is started, the master password must be entered, for start-up to proceed to completion. (This requirement may include instances of node _restart_, due to reconfiguration or anomaly.)

The master password can be established by means of the [master-password](../../cli/couchbase-cli-master-password.md) CLI command; the REST API [POST /node/controller/changeMasterPassword](../../../../server/current/rest-api/change-master-password.md) method; and (on all supported operating systems other than Mac OS X) by explicitly setting the `CB_MASTER_PASSWORD` environment variable, at the command-prompt.

When you specify the master password, Operational Insights derives a _master key_ from that password, using the strong _Key Derivation Function_ PBKDF2\. Operational Insights also creates a random _data key_, which is then encrypted with the master key. The data key will be used to encrypt all secrets on disk, using an AES 256-bit algorithm, in GCM mode. To bootstrap the system, the master key is used to open the encrypted data key; the data key is then used to open the encrypted secrets; and the secrets are then used to start Operational Insights.

If you establish the master password by setting the environment variable for the current node while Operational Insights is running, Operational Insights performs encryption on secrets from that point. However, by default, the _decryption_ of secrets relies on Operational Insights having read the environment variable on startup. Therefore, if Operational Insights has already been started as a service at the time you set the environment variable, you must explicitly make the newly established variable available to the service. If Operational Insights has already been started as a script, you must use the `export` command, to make it available to the script.

At start-up, Operational Insights waits for the master password to be entered. Enter the password by means of the `master-password` CLI command, with the `--send-password` option:

/opt/couchbase/bin/couchbase-cli

The following prompt now appears:

Enter master password:

Enter the master password against this prompt. You are permitted _three attempts_ to enter the master password correctly.

Note that the `master-password` CLI command must be run on the same host on which Operational Insights is running.

## [](#password%5Frotation)Performing Rotation

The Operational Insights Secrets-Management system allows you to _rotate_ (periodically change, to reduce the risk of illicit discovery or deciphering) the different elements of the system:

* **Master-password rotation**:The _first level of rotation_ is achieved by setting a new password, using the [CLI command](../../cli/couchbase-cli-master-password.md), the [POST /node/controller/changeMasterPassword](../../../../server/current/rest-api/change-master-password.md) method, or (other than on Mac OS X) the environment variable, as indicated above. One master password per node needs to be set.
* **Data-key rotation**: The _second level of rotation_ is achieved by changing the data-key, using the [CLI command](../../cli/couchbase-cli-master-password.md) with the `--rotate-data-key` option, or the [POST /node/controller/rotateDataKey](../../../../server/current/rest-api/rotate-data-key.md) method.
* **Secret rotation**: The _third level of rotation_ is achieved by changing the values of the secrets themselves. For example, to reset the secret that is an administrator password, use the [couchbase-cli reset-admin-password](../../cli/couchbase-cli-reset-admin-password.md) command.

Note that if the auditing option is enabled, all rotation-requests are audited by Operational Insights.

## [](#configuring-system-secrets)Configuring System Secrets

System Secrets can be configured, by means of the REST API. Configuration includes:

* Whether the master password is obtained from an environment variable or from a script.
* The location of encrypted keys.
* Whether keys are read, written, and deleted as files or by means of custom scripts.

For detailed descriptions and examples, see [Configuring System Secrets](../../../../server/current/rest-api/system-secrets-configuration.md).