---
title: Security Best Practices
description: Security is a process and Capella Analytics strives to achieve the
  best ways to protect your data, from Zero Trust, through adaptive access, to
  centralized management and proactive monitoring.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/security.adoc
  xref: xref:analytics:admin:security.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/admin/security.html)

# Security Best Practices

> Security is a process and Capella Analytics strives to achieve the best ways to protect your data, from Zero Trust, through adaptive access, to centralized management and proactive monitoring. Best practices in the way you work with Capella Analytics further protect you from malicious attacks. 

This page groups together listings of some of the many features of Capella Analytics security architecture with links to places in the docs where you have a chance to apply good practice to your Couchbase instance.

## [](#security-highlights)Security Highlights

All communication is encrypted using TLS 1.2 or higher. This can't be turned off.

### [](#encryption-at-rest)Encryption at Rest

By default, Capella Analytics clusters use the underlying cloud provider's key management service to create a new key for each cluster. These key management services include AWS Key Management Service and Google Cloud Key Management Service.

Capella Analytics uses customer master keys that are 256-bit Advanced Encryption Standard (AES) symmetric keys and are not exportable. AES-256, which has a key length of 256 bits, supports the largest bit size and is practically unbreakable by brute force based on current computing power, making it the strongest encryption standard. Customer master keys use hardware security modules (HSMs) validated under FIPS 140-2.

### [](#secrets-management)Secrets Management

Secrets such as TLS private keys are unique and should not be shared amongst customer environments. This is to prevent the spread of an attack. If one customer's environment gets breached you want to prevent material to attack other customers being provided.

All secrets that are persisted or stored are encrypted when they're stored, with a FIPS 140 approved encryption technology such as AES 256\. This uses secure hardware backed (HSM) systems like AWS CloudHSM and GCP Cloud HSM. Automatically generated secrets are rotated on a regular basis.

### [](#access-management)Access Management

Capella Analytics is built upon Couchbase's sophisticated Role-Based Access Control.

* [Organization and Project Overview](../../cloud/organizations/organization-projects-overview.md): Capella Analytics is organized into organizations and projects, each of which has its own user roles.
* [Allowed IPs](ip-allowed-list.md): Limit both the IP addresses that can access your data, and the period for which they have access.
* [Access Control Account](auth/auth-data.md): Provide programmatic and application-level access to data on a cluster.

### [](#authentication)Authentication

[Federated & SSO Authentication](../../cloud/organizations/ui-auth/capella-ui-auth.md): Capella Analytics allows users to sign in to the Capella UI using federated and SSO authentication after configuring Capella to authenticate using data passed from your identity provider (IdP).

[Multi-Factor Authentication](../../cloud/organizations/ui-auth/mfa.md) (MFA): Any non-SSO user within your organization can use Capella's MFA. MFA improves your Capella account security by requiring two credentials to sign in: your password and a time-based one-time password (TOTP). Five failed attempts at logging in a user results in that account being locked for five minutes.