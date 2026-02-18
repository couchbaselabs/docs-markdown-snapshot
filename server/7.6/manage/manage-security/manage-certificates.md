---
title: Manage Certificates
description: Couchbase Server supports the use of X.509 certificates.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/manage/pages/manage-security/manage-certificates.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/manage/manage-security/manage-certificates.html)

# Manage Certificates

> Couchbase Server supports the use of X.509 certificates. 

## [](#certificate-management-overview)Certificate Management Overview

A conceptual and architectural overview of Couchbase Server’s support of X.509 certificates is provided in [Certificates](../../learn/security/certificates.md). The current section provides practical steps for:

* _Configuring server certificates_: These reside on Couchbase Server-nodes, identify the cluster to networked clients, and support encrypted network communications. Procedures are provided to demonstrate how a cluster can be protected by means of _root_ and _node_ certificates; and how node certificates can themselves be created with additional security and efficiency, by the creation and use of _intermediate_ certificates. See [Configure Server Certificates](configure-server-certificates.md).
* _Configuring client certificates_: These can be used by networked clients to authenticate with Couchbase Server, and to support encrypted network communications. Certificate creation is demonstrated both with and without the use of intermediate certificates. The certificate-creation requirements specific to Java applications are demonstrated. Additionally, links are provided to other areas of the documentation, where the certificates in the current section can be used to establish secure _XDCR_ communication between clusters; and to establish communication between a cluster and a Java client. See [Configure Client Certificates](configure-client-certificates.md).
* _Handling client certificates_: Couchbase Server can be configured to accept or demand the presentation by clients of certificates for the purpose of authentication. Since client certificates contain a _username_, which can be represented in a number of different ways within the certificate content, Couchbase Server must be configured to identify the appropriate representation, and so extract the specified username. Full instructions for accomplishing this with the UI, the CLI, and the REST API are provided: see [Enable Client-Certificate Handling](enable-client-certificate-handling.md).

Additionally, procedures are provided for [Certificate Rotation](rotate-server-certificates.md), to ensure optimal security; and [Certificate Error Handling](handle-certificate-errors.md).