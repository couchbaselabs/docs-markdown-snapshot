---
title: Encryption
description: Couchbase Server uses <em>encryption</em>, to protect data.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/learn/pages/security/encryption-overview.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:learn:security/encryption-overview.adoc[]
---

[View original HTML](/server/7.2/learn/security/encryption-overview.html)

# Encryption

> Couchbase Server uses _encryption_, to protect data. 

## [](#encryption-in-couchbase-server)Encryption in Couchbase Server

By means of _encryption_, data is encoded such that it is non-readable, other than by authorized parties who possess the appropriate means of _decryption_. Prior to decryption, therefore, encrypted data can be securely saved or transmitted. This ensures the privacy of user-data, and the integrity of servers and their clients.

Couchbase Server provides extensive support for data encryption and decryption. Multiple areas of the system are affected: therefore, essential information is distributed throughout the documentation set.

## [](#areas-of-encryption)Areas of Encryption

The principal areas of Couchbase Server encryption-support are listed below, along with links to further information.

### [](#encryption-on-the-wire)Encryption on the Wire

This allows data to pass in encrypted form between nodes, between clusters, and between a cluster and its clients.

* **Node-to-Node Encryption**. Network traffic between the individual nodes of a Couchbase-Server cluster can be encrypted, in order to optimize cluster-internal security. See [Node-to-Node Encryption](../clusters-and-availability/node-to-node-encryption.md).
* **On-the-Wire Security Configuration**. To support secure communications between nodes, clusters, and clients, Couchbase Server provides interfaces for the configuration of _TLS_ and supportive _cipher-suites_; of cluster-internal encryption-levels; and of secure UI-access. See [On-the-Wire Security](on-the-wire-security.md) for a conceptual overview, and [Manage On-the-Wire Security](../../manage/manage-security/manage-tls.md) for step-by-step configuration-instructions.
* **Secure Console Access**. Administrators can connect securely to Couchbase Web Console. Non-secure access can be disabled, for extra security. See [Manage Console Access](../../manage/manage-security/manage-console-access.md).
* **X.509 Certificates**. These support encrypted communications between nodes, between clusters, and between a cluster and its clients.

  * [Certificates](certificates.md) provides an overview of certificates and their management.
  * [Configure Server Certificates](../../manage/manage-security/configure-server-certificates.md) explains the practical steps towards configuring certificates for Couchbase Server. This page also provides information on working with different versions of SSL/TLS, and on supported _ciphers_.
  * [Configure Client Certificates](../../manage/manage-security/configure-client-certificates.md) describes how to create a certificate to allow a client’s secure access to Couchbase Server.
  * [Enable Client-Certificate Handling](../../manage/manage-security/enable-client-certificate-handling.md) explains how to configure Couchbase Server to accept communications from clients that wish to authenticate and communicate securely by means of certificates.
  * [Certificate Rotation](../../manage/manage-security/rotate-server-certificates.md) provides steps whereby server certificates can be _rotated_ periodically, to ensure optimal security.
  * [Certificate Error Handling](../../manage/manage-security/handle-certificate-errors.md) explains how to handle errors related to certificate-based secure communication.
  * [Enable Fully Secure Replications](../../manage/manage-xdcr/enable-full-secure-replication.md) describes how certificates can be used to ensure that data is replicated securely between clusters.
  * [Certificate Management API](../../rest-api/rest-certificate-management.md) lists the REST API methods and URIs available for certificate management.
  * The [ssl-manage](../../cli/cbcli/couchbase-cli-ssl-manage.md) CLI command supports management of SSL certificates.
* **Secure Ports**. Services are available on secure ports. See [Couchbase Server Ports](../../install/install-ports.md).
* **General Network Security**. Best practices for ensuring the security of the network are provided in [Network Security Recommendations](../../manage/manage-security/manage-connections-and-disks.md).

### [](#encryption-at-rest)Encryption at Rest

Encryption _at Rest_ (meaning, on disk or other storage-device) allows passwords and data in files and directories to be encrypted.

* **Data in Files and Directories**. Programs are available for the encryption of data in files and directories. See [Securing On-Disk Data](../../manage/manage-security/manage-connections-and-disks.md#securing-on-disk-data).
* **System Secrets**. Passwords, certificates, and other items essential to Couchbase-Server security can be written to disk in encrypted format. See [Manage System Secrets](../../manage/manage-security/manage-system-secrets.md).

### [](#encryption-in-applications)Encryption in Applications

* **Field Level Encryption**. This allows fields within a document to be securely encrypted by the SDK, to support FIPS-140-2 compliance. See [Field Level Encryption](#3.4@java-sdk:howtos:encrypting-using-sdk.adoc), for an overview.
* **Field Level Encryption from the Java SDK**. Provides directions for configuring encrypted field-level communication with Couchbase Server. See [Field Level Encryption from the Java SDK](#3.4@java-sdk:concept-docs:encryption.adoc).