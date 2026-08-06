---
title: Certificate Rotation
description: Certificates should be rotated periodically, to ensure optimal security.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/manage/pages/manage-security/rotate-server-certificates.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:manage:manage-security/rotate-server-certificates.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/manage/manage-security/rotate-server-certificates.html)

# Certificate Rotation

> Certificates should be rotated periodically, to ensure optimal security. 

## [](#rotating-server-certificates)Rotating Certificates

Certificate rotation (which means the replacement of existing certificates with new ones) is needed when:

* Any certificate expires.
* A new CA authority is substituted for the old; thus requiring a replacement root certificate for the cluster.
* New or modified constraints need to be imposed on one or more certificates.
* A security breach has occurred, such that existing certificate-chains can no longer be trusted.

Certificate-rotation should be planned well before certificates expire. No root or intermediate certificate should ever be used to issue certificates with an expiration date later than that of the issuing certificate itself.

Certificate-rotation on the server-side does not require that either the cluster or any of its nodes be restarted. However, following rotation of a server-side's root certificate and chains, all corresponding client-chains must also be rotated accordingly.

Note that when a certificate is to be rotated, a new private key should always be created, and used to generate an entirely new, replacement certificate.

### [](#node-to-node-encryption-and-certificate-rotation)Node-to-Node Encryption and Certificate Rotation

Enterprise Analytics supports [Node-to-Node Encryption](../../../../server/current/learn/clusters-and-availability/node-to-node-encryption.md), whereby network traffic between the individual nodes of a cluster is encrypted.