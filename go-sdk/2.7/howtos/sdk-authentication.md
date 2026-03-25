---
title: Authentication
description: As well as Role-Based Access Control (RBAC), Couchbase offers
  connection with Certificate Authentication, and works transparently with LDAP.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/release/2.7/modules/howtos/pages/sdk-authentication.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.7@go-sdk:howtos:sdk-authentication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.7/howtos/sdk-authentication.html)

# Authentication

> As well as Role-Based Access Control (RBAC), Couchbase offers connection with Certificate Authentication, and works transparently with LDAP. 

Our [Getting Started](../hello-world/start-using-sdk.md) guide covered the basics for authorizing against a Couchbase cluster, but you may need to use alternative authentication methods such as Certification.

## [](#rbac)RBAC

Our [Getting Started](../hello-world/start-using-sdk.md) guide introduced basic authentication against a Couchbase cluster:

```golang
	opts := gocb.ClusterOptions{
		Username: "Administrator",
		Password: "password",
	}
	cluster, err := gocb.Connect("10.112.193.101", opts)
	if err != nil {
		panic(err)
	}
```

Couchbase uses Role Base Access Control (RBAC), and has since Server 5.0 was released. For a general overview of Couchbase-Server authorization, see [Authorization](#7.1@server:learn:security/authorization-overview.adoc). For a list of available roles and corresponding privileges, see [Roles](#7.1@server:learn:security/roles.adoc).

In the SDK docs, many examples will use the full _Administrator_ role for convenience, but this is rarely a good idea on a production machine, so reference the above links to find best practice for the needs of your application. RBAC is also implemented by the Community Edition of Couchbase Server, but with fewer roles — see the [Roles overview](#7.1@server:learn:security/roles.adoc).

## [](#certificate-authentication)Certificate Authentication

Couchbase Server supports the use of X.509 certificates to authenticate clients (only available in the Enterprise Edition, not the Community Edition). This allows authenticated users to access specific resources by means of the data service, in Couchbase Server 5.1 and up, and all other services in more recent releases of Couchbase Data Platform.

The process relies on a certificate authority, for the issuing of certificates that validate identities. A certificate includes information such as the name of the entity it identifies, an expiration date, the name of the authority that issued the certificate, and the digital signature of the authority. A client attempting to access Couchbase Server can present a certificate to the server, allowing the server to check the validity of the certificate. If the certificate is valid, the user under whose identity the client is running, and the roles assigned that user, are verified. If the assigned roles are appropriate for the level of access requested to the specified resource, access is granted.

For a more detailed conceptual description of using certificates, see [Certificates](#7.1@server:learn:security/certificates.adoc).

## [](#authenticating-the-go-client-by-certificate)Authenticating the Go Client by Certificate

For sample procedures whereby certificates can be generated and deployed, see [Manage Certificates](#7.1@server:manage:manage-security/manage-certificates.adoc). The rest of this document assumes that the processes there, or something similar, have been followed. That is:

* A cluster certificate has been created and installed on the server.
* A client certificate and private key pair have been created, and are accessible to be loaded into your application (the example below loads them from the file system).

```golang
	// Load the public/private key pair from file
	cert, err := tls.LoadX509KeyPair("mycert.pem", "mykey.pem")
	if err != nil {
		panic(err)
	}

	opts := gocb.ClusterOptions{
		Authenticator: gocb.CertificateAuthenticator{
			ClientCertificate: &cert,
		},
	}
	// Connect to the cluster using certificates and node key, note: couchbases
	cluster, err := gocb.Connect("couchbases://localhost", opts)
	if err != nil {
		panic(err)
	}
```

## [](#ldap)LDAP

If you are on a network where access is controlled by LDAP, the SDK will work transparently with it. Please pay attention to the following important note on secure connection.

> [!IMPORTANT]
> If [LDAP](#7.1@server:manage:manage-security/configure-ldap.adoc#understanding-ldap-authentication) is enabled, Couchbase Server will only allow PLAIN sasl authentication which by default, for good security, the SDK will not allow. Although this can be overridden in a development environment, by explicitly enabling PLAIN in the password authenticator, _the secure solution_ is [to use TLS](managing-connections.md#ssl).

```golang
	opts := gocb.ClusterOptions{
		Username: "Administrator",
		Password: "password",
		SecurityConfig: gocb.SecurityConfig{
			AllowedSaslMechanisms: []gocb.SaslMechanism{gocb.PlainSaslMechanism},
		},
	}
	cluster, err := gocb.Connect("couchbase://10.112.193.101", opts)
	if err != nil {
		panic(err)
	}
```