---
title: Certificate-Based Authentication
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.3/modules/concept-docs/pages/certificate-based-authentication.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/python-sdk/4.3/concept-docs/certificate-based-authentication.html)

# Certificate-Based Authentication

> x.509 Certificates for client-server authentication. 

## [](#certificate-based-authentication)Certificate-Based Authentication

Couchbase Server supports the use of x.509 certificates, for authentication between clients and servers. This is covered extensively in:

* Our [Client Certificate discussion doc](#7.1@server:learn:security/certificates.adoc);
* [Configure Client Certificates](#7.1@server:manage:manage-security/configure-client-certificates.adoc);
* The [Certificate Management Overview](#7.1@server:manage:manage-security/manage-certificates.adoc)…​
* …​ and [Certificate Configuration](#7.1@server:manage:manage-security/configure-server-certificates.adoc) pages.

As well as our practical guide to [authenticating an SDK client against Couchbase Server by certificate](../howtos/sdk-authentication.md#certificate-authentication.adoc).

## [](#tls)TLS

Certificates are also used for [secure connection to the Server](#7.1@server:manage:manage-security/configure-client-certificates.adoc#enabling-client-security) — the [SDK guide](../howtos/managing-connections.md#ssl) gives practical details.