---
title: Authentication
description: As well as Role-Based Access Control (RBAC), Couchbase offers
  connection with Certificate Authentication, and works transparently with LDAP.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.5/modules/howtos/pages/sdk-authentication.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.5@ruby-sdk:howtos:sdk-authentication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.5/howtos/sdk-authentication.html)

# Authentication

> As well as Role-Based Access Control (RBAC), Couchbase offers connection with Certificate Authentication, and works transparently with LDAP. 

Our [Getting Started](../hello-world/start-using-sdk.md) guide covered the basics for authorizing against a Couchbase cluster, but you may need to use alternative authentication methods such as Certification.

## [](#rbac)RBAC

Our [Getting Started](../hello-world/start-using-sdk.md) guide introduced basic authentication against a Couchbase cluster:

```ruby
# Update these credentials for your Local instance!
options = Cluster::ClusterOptions.new
options.authenticate("username", "Password!123")
cluster = Cluster.connect("couchbase://localhost", options)
```

Unresolved include directive in modules/howtos/pages/sdk-authentication.adoc - include::7.5@sdk:shared:partial$auth-overview.adoc\[\]

Unresolved include directive in modules/howtos/pages/sdk-authentication.adoc - include::7.5@sdk:shared:partial$auth-overview.adoc\[\]

## [](#authenticating-a-ruby-client-by-certificate)Authenticating a Ruby Client by Certificate

For sample procedures whereby certificates can be generated and deployed, see [Manage Certificates](#7.1@server:manage:manage-security/manage-certificates.adoc). The rest of this document assumes that the processes there, or something similar, have been followed:

```ruby
# @see https://docs.couchbase.com/server/current/manage/manage-security/configure-client-certificates.html
options.authenticator = CertificateAuthenticator.new("/tmp/certificate.pem", "/tmp/private.key")
Cluster.connect("couchbases://localhost?trust_certificate=/tmp/ca.pem", options)
```

Unresolved include directive in modules/howtos/pages/sdk-authentication.adoc - include::7.5@sdk:shared:partial$auth-overview.adoc\[\]

```ruby
# Creates a LDAP compatible password authenticator which is INSECURE if not used with TLS (uses PLAIN sasl mechanism).
options.authenticator = PasswordAuthenticator.ldap_compatible("Administrator", "password")
Cluster.connect("couchbase://localhost", options)
```