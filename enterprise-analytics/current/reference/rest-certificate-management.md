---
title: Certificate Management API
description: The REST API can be used to manage the root and node certificates of a cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/reference/pages/rest-certificate-management.adoc
  xref: xref:enterprise-analytics:reference:rest-certificate-management.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/reference/rest-certificate-management.html)

# Certificate Management API

> The REST API can be used to manage the root and node certificates of a cluster. 

## [](#performing-certificate-management)Performing Certificate Management

Enterprise Analytics supports the use of x.509 certificates, for clients and servers. The REST API allows the server certificates to be managed. From a management perspective, server certificates can be considered to be of two kinds:

* _Root_ certificates. At least one root certificate exists for each cluster. Any number of root certificates can be uploaded: together, these constitute the cluster's _trust store_. Each root certificate contains the public key of a Certificate Authority (CA).  
Enterprise Analytics uses its list of trusted certificates to verify:

  * Client certificates (when client certificate authentication is enabled: for information, see [Enable Client-Certificate Handling](../manage/manage-security/enable-client-certificate-handling.md)).
  * The identities of cluster nodes (when node-to-node encryption is enabled: for information, see [Manage Node-to-Node Encryption](../manage/manage-nodes/apply-node-to-node-encryption.md)).
  * The identities of nodes that join the cluster (when the server has been provisioned with certificates).
  * The identity of LDAP servers (when TLS has been turned on, in the LDAP settings: for information, see [LDAP Host Configuration](../manage/manage-security/configure-ldap.md#ldap-host-configuration)).
* _Node_ certificates. A different node certificate is installed on each node in the cluster. This certificate is _signed_ by a root certificate (or by an intermediate certificate that itself has gained authority from that root certificate), and is itself therefore granted the authority of that root certificate. Clients that contact the node can determine the identity of the root certificate by examining the node certificate, and verifying its signature chain — which leads to the responsible root certificate.

A complete overview of certificate management for Enterprise Analytics is provided in [Certificates](#learn:security/certificates.adoc). Examples of certificate creation and deployment are provided in [Manage Certificates](../manage/manage-security/manage-certificates.md).

## [](#the-rest-api-for-certificate-management)The REST API for Certificate Management

The Enterprise Analytics supports certificate management with the following, principal APIs:

* Root certificates can be uploaded, retrieved, and deleted. See [Load Root Certificates](load-trusted-cas.md), [Get Root Certificates](get-trusted-cas.md), and [Delete Root Certificates](delete-trusted-cas.md).
* The current certificate for a specific node can be uploaded and retrieved. See [Upload and Retrieve a Node Certificate](upload-retrieve-node-cert.md). Additionally, all current node certificates for the cluster can be retrieved: see [Retrieve All Node Certificates](retrieve-all-node-certs.md).
* All certificates — root and node — can be _regenerated_ (that is, restored to their automatically provided default values). See [Regenerate All Certificates](rest-regenerate-all-certs.md).