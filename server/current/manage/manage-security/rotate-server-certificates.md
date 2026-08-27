---
title: Certificate Rotation
description: Certificates should be rotated periodically, to ensure optimal security.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/manage-security/rotate-server-certificates.adoc
  xref: xref:server:manage:manage-security/rotate-server-certificates.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/manage/manage-security/rotate-server-certificates.html)

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

Couchbase Server supports [Node-to-Node Encryption](../../learn/clusters-and-availability/node-to-node-encryption.md), whereby network traffic between the individual nodes of a cluster is encrypted.

Note that prior to Couchbase Server Version 7.1, node-to-node encryption, which is managed by means of the Couchbase CLI, needed to be _disabled_ before management of either _root_ or _intermediate_ certificates could be performed. This restriction is lifted in version 7.1: therefore, root and intermediate certificates _can_ now be managed while node-to-node encryption is enabled.