---
title: Couchbase Credential Rotation
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/concept-credential-rotation.adoc
  xref: xref:2.6@operator::concept-credential-rotation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/concept-credential-rotation.html)

# Couchbase Credential Rotation

> Credentials used for authorization and authentication should be rotated on a regular basis to maintain security. This documents what is supported and how to update credentials. 

## [](#credential-rotation)Credential Rotation

In a typical reactive system, credentials would need to be rotated if they were compromised. If a malicious third party gained access to your administrative user name and password, then all data contained within the database would be compromised. To deny access to the malicious third party, you would rotate — or change — the password, so the compromised password were no longer valid.

A modern, proactive system would rotate credentials on — for example — a monthly schedule. This has the benefit of automatically locking out users with stale or compromised credentials. It also reduces the scope for compromise; to takes time to crack keys and passwords, by rotating them frequently, you make it virtually impossible for a credential to be cracked before it is changed.

Whichever strategy you take, you should consider rotation as part of your information security life cycle.

## [](#supported-credentials)Supported Credentials

The Operator manages all credentials for a Couchbase Cluster. The following describes what is controlled and how to rotate those credentials:

Administrator Password operator 2.1

The administrator password provides the "keys-to-the-castle" and is able to control everything about a Couchbase cluster. The Operator uses the administrator password (when not using TLS client authentication) to interact with a cluster under its control.

To rotate, follow the [administrator password rotation how-to](howto-admin-password-rotation.md).

TLS Certificates operator 1.2

TLS addresses the shortcomings of plain text passwords by never exposing private credentials on the network.

When using server-side TLS, all data is encrypted, so passwords are obscured from view, so a third party cannot intercept those credentials. That's not to say it cannot be compromised by either stealing the TLS private key, or factoring the public key, so these should also be rotated frequently. Certificates have a finite lifetime so must be rotated eventually.

When using mutual TLS, this extends the system to allow authentication of the client with TLS certificates. Again these can be compromised and the user impersonated, or expire, so need periodic rotation.

To rotate certificates, read the [TLS certificate rotation concepts](concept-tls.md#tls-certificate-rotation) page and follow the [TLS certificate rotation how-to](howto-tls-rotation.md).

The following are not supported for rotation:

Local User Passwords

User passwords are much the same as the administrator password described above. The key difference is that individual user accounts have lowered privileges and can affect fewer parts of the system.

Password rotation is not supported currently. Consider using [LDAP authentication](tutorial-rbac-auth.md#ldap-authentication) to mandate regular user password rotation.

XDCR Client Configuration

XDCR is just a client running under a user account.

Password rotation is not supported currently, although support will be added in a future release. In order to change the password or TLS configuration associated with an XDCR remote cluster, you must delete the remote cluster reference and recreate it with the new credentials. This will restart all bucket replications to the remote cluster.