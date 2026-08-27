---
title: Authentication
description: As well as Role-Based Access Control (RBAC), Couchbase offers
  connection with Certificate Authentication, and works transparently with LDAP.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/release/4.6/modules/howtos/pages/sdk-authentication.adoc
  xref: xref:python-sdk:howtos:sdk-authentication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/howtos/sdk-authentication.html)

# Authentication

> As well as Role-Based Access Control (RBAC), Couchbase offers connection with Certificate Authentication, and works transparently with LDAP. 

Our [Getting Started](../hello-world/start-using-sdk.md) guide covered the basics for authorizing against a Couchbase cluster, but you may need to use alternative authentication methods such as Certification.

## [](#rbac)RBAC

Our [Getting Started](../hello-world/start-using-sdk.md) guide introduced basic authentication against a Couchbase cluster:

```python
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions


cluster = Cluster.connect('couchbases://your-ip',
                  ClusterOptions(PasswordAuthenticator('username', 'password')))
```

Couchbase uses Role Base Access Control (RBAC), and has since Server 5.0 was released. For a general overview of Couchbase-Server authorization, see [Authorization](../../../server/current/learn/security/authorization-overview.md). For a list of available roles and corresponding privileges, see [Roles](../../../server/current/learn/security/roles.md).

In the SDK docs, many examples will use the full _Administrator_ role for convenience, but this is rarely a good idea on a production machine, so reference the above links to find best practice for the needs of your application. RBAC is also implemented by the Community Edition of Couchbase Server, but with fewer roles — see the [Roles overview](../../../server/current/learn/security/roles.md).

## [](#certificate-authentication)Certificate Authentication

Couchbase Server supports the use of X.509 certificates to authenticate clients (only available in the Enterprise Edition, not the Community Edition). This allows authenticated users to access specific resources by means of the data service, in Couchbase Server 5.1 and up, and all other services in more recent releases of Couchbase Data Platform.

The process relies on a certificate authority, for the issuing of certificates that validate identities. A certificate includes information such as the name of the entity it identifies, an expiration date, the name of the authority that issued the certificate, and the digital signature of the authority. A client attempting to access Couchbase Server can present a certificate to the server, allowing the server to check the validity of the certificate. If the certificate is valid, the user under whose identity the client is running, and the roles assigned that user, are verified. If the assigned roles are appropriate for the level of access requested to the specified resource, access is granted.

For a more detailed conceptual description of using certificates, see [Certificates](../../../server/current/learn/security/certificates.md).

## [](#authenticating-a-python-client-by-certificate)Authenticating a Python Client by Certificate

For sample procedures whereby certificates can be generated and deployed, see [Manage Certificates](../../../server/current/manage/manage-security/manage-certificates.md). The rest of this document assumes that the processes there, or something similar, have been followed. That is, a cluster certificate has been created and installed on the server, a client certificate has been created, and it is stored somewhere accessible to the SDK. The `CertAuthenticator` expects to be given the path to the client certificate and key as well as the path to the certificate trust store.

```python
from couchbase.auth import CertificateAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions

import os.path

# point to certificates, keys, and trust stores;
# for the purposes of this code,
# the script in etc/x509-cert will generate these
clientdir = "etc/x509-cert/SSLCA/clientdir"
options = dict(cert_path=os.path.join(clientdir, "client.pem"),
               trust_store_path=os.path.join(clientdir, "trust.pem"),
               key_path=os.path.join(clientdir, "client.key"))

opts = ClusterOptions(CertificateAuthenticator(**options))
cluster = Cluster.connect('couchbase://your-ip', opts)
```

## [](#ldap)LDAP

If you are on a network where access is controlled by LDAP, the SDK will work transparently with it. Please pay attention to the following important note on secure connection.

> [!IMPORTANT]
> If [LDAP](../../../server/current/manage/manage-security/configure-ldap.md#understanding-ldap-authentication) is enabled, Couchbase Server will only allow PLAIN sasl authentication which by default, for good security, the SDK will not allow. Although this can be overridden in a development environment, by explicitly enabling PLAIN in the password authenticator, _the secure solution_ is [to use TLS](managing-connections.md#ssl).

```python
# Use over TLS for production
opts = ClusterOptions(PasswordAuthenticator('einstein', 'password'))
connection_str = "couchbases://10.143.205.101?sasl_mech_force=PLAIN&certpath=cert.ca"
cluster = Cluster.connect(connection_str, opts)
```