---
title: Encryption
description: Couchbase Server lets you use encryption to protect data.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/learn/pages/security/encryption-overview.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:learn:security/encryption-overview.adoc[]
---

[View original HTML](/server/current/learn/security/encryption-overview.html)

# Encryption

> Couchbase Server lets you use encryption to protect data. You can configure network encryption for communications with clients, between nodes in the cluster, and with other clusters when using Cross-Datacenter Replication (XDCR). Couchbase Server supports encrypting data stored on disk to limit data exposure. You can also have your application store encrypted attributes in documents. This topic provides an overview of the encryption features in Couchbase Server. 

## [](#encryption-on-the-wire)Network Encryption

You can choose to encrypt client connections, intra-node connections, and cluster-to-cluster connections. You configure each connection type separately. For example, you can choose to encrypt client connections, but leave connections between nodes in a cluster unencrypted.

Couchbase Server supports the following types of network encryption:

Node to Node

You can choose to encrypt all internal traffic between nodes in the cluster. This configuration helps limit data leakage from network intrusions. See [Node-to-Node Encryption](../clusters-and-availability/node-to-node-encryption.md).

Client Connections

You can make encryption optional or required for client connections. See [Securing Client Access with TLS](../../manage/manage-security/configure-client-certificates.md#enabling-client-security).

Couchbase Server Web Console Access

You can configure the Web Console to require secure connections. See [Manage Console Access](../../manage/manage-security/manage-console-access.md).

Secure Access to Services

You can configure Couchbase Server services to only use secure ports. See [Couchbase Server Ports](../../install/install-ports.md).

Secure XDCR Replication

You can encrypt XDCR replication between Couchbase Server clusters. See [Enable Fully Secure Replications](../../manage/manage-xdcr/enable-full-secure-replication.md).

Couchbase Server TLS Support

Couchbase Server uses Transport Layer Security (TLS) with a selection of cipher-suites for network encryption. See the following pages for more information about Couchbase Server’s TLS support:

* [On-the-Wire Security](on-the-wire-security.md) provides a conceptual overview of TLS in Couchbase Server.
* [Manage On-the-Wire Security](../../manage/manage-security/manage-tls.md) has step-by-step configuration instructions.
* [Manage Connections and Disks](../../manage/manage-security/manage-connections-and-disks.md) has a general overview of network security best practices.

## [](#encryption-at-rest)Encryption at Rest

Encryption at rest encrypts files stored on disk. The files you can encrypt include those that store database data, configuration, logs, and audits. Encrypting data at rest can help limit the exposure of confidential information from a security breach.

You have several options to encrypt your data at rest:

Use the Couchbase Server native encryption at-rest feature

Couchbase Server Enterprise has a built-in encryption-at-rest feature where it encrypts data as it saves it to disk. Using the built-in encryption lets you fine-tune which data is encrypted and which it not. For example, you can choose to encrypt sensitive customer data, while leaving less sensitive data, such as product catalog data, unencrypted. By encrypting just the sensitive data in your database, you can limit the overhead of encrypting and decrypting data. See [Native Encryption at Rest](native-encryption-at-rest-overview.md) for more information.

Use third-party tools

Third party tools such as [Thales CipherTrust](https://cpl.thalesgroup.com/encryption/transparent-encryption) (formerly known as Vormetric/Gemalto) and [Protegrity](https://www.protegrity.com/) can provide centralized encryption at rest.

Use OS-level disk encryption

You can use disk encryption such as the LUKS encrypted filesystem which is available on Linux. See [Securing On-Disk Data](../../manage/manage-security/manage-connections-and-disks.md#securing-on-disk-data).

Use field-level encryption in applications

Applications can use the SDK to encrypt specific fields. Depending on your application’s requirements, field-level encryption may be more appropriate than encrypting the entire bucket or disk. See the SDK documentation for your development language for more information. For example:

* Go SDK: [Encrypting Your Data](../../../../go-sdk/current/howtos/encrypting-using-sdk.md)
* Java SDK: [Encrypting Your Data](../../../../java-sdk/current/howtos/encrypting-using-sdk.md)
* Python SDK: [Encrypting Your Data](../../../../python-sdk/current/howtos/encrypting-using-sdk.md)

## [](#system-secrets)System Secrets

Couchbase Server can write passwords, certificates, and other sensitive information to disk in encrypted format. See [Manage System Secrets](../../manage/manage-security/manage-system-secrets.md).