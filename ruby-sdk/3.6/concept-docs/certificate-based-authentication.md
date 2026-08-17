---
title: Certificate-Based Authentication
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.6/modules/concept-docs/pages/certificate-based-authentication.adoc
  xref: xref:3.6@ruby-sdk:concept-docs:certificate-based-authentication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.6/concept-docs/certificate-based-authentication.html)

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