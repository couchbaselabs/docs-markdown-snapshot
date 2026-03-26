---
title: Manage Certificates
description: Enterprise Analytics supports the use of X.509 certificates.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/manage-security/manage-certificates.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.0@enterprise-analytics:manage:manage-security/manage-certificates.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/manage/manage-security/manage-certificates.html)

# Manage Certificates

> Enterprise Analytics supports the use of X.509 certificates. 

## [](#certificate-management-overview)Certificate Management Overview

A conceptual and architectural overview of Enterprise Analytics's support of X.509 certificates is provided in [Certificates](../../../../server/current/learn/security/certificates.md). The current section provides practical steps for:

* _Configuring server certificates_: These reside on Enterprise Analytics-nodes, identify the cluster to networked clients, and support encrypted network communications. Procedures are provided to demonstrate how a cluster can be protected by means of _root_ and _node_ certificates; and how node certificates can themselves be created with additional security and efficiency, by the creation and use of _intermediate_ certificates. See [Configure Server Certificates](configure-server-certificates.md).
* _Configuring client certificates_: These can be used by networked clients to authenticate with Enterprise Analytics, and to support encrypted network communications. Certificate creation is demonstrated both with and without the use of intermediate certificates. The certificate-creation requirements specific to Java applications are demonstrated. Additionally, links are provided to other areas of the documentation, where the certificates in the current section can be used to establish secure _XDCR_ communication between clusters; and to establish communication between a cluster and a Java client. See [Configure Client Certificates](configure-client-certificates.md).
* _Handling client certificates_: Enterprise Analytics can be configured to accept or demand the presentation by clients of certificates for the purpose of authentication. Since client certificates contain a _username_, which can be represented in a number of different ways within the certificate content, Enterprise Analytics must be configured to identify the appropriate representation, and so extract the specified username. Full instructions for accomplishing this with the UI, the CLI, and the REST API are provided: see [Enable Client-Certificate Handling](enable-client-certificate-handling.md).

Additionally, procedures are provided for [Certificate Rotation](rotate-server-certificates.md), to ensure optimal security; and [Certificate Error Handling](handle-certificate-errors.md).