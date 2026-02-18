---
title: Authentication
description: As well as Role-Based Access Control (RBAC), Couchbase offers
  connection with Certificate Authentication, and works transparently with LDAP.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.9/modules/howtos/pages/sdk-authentication.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/java-sdk/3.9/howtos/sdk-authentication.html)

# Authentication

> As well as Role-Based Access Control (RBAC), Couchbase offers connection with Certificate Authentication, and works transparently with LDAP. 

Our [Getting Started](../hello-world/start-using-sdk.md) guide covered the basics for authorizing against a Couchbase cluster, but you may need to use alternative authentication methods such as Certification.

## [](#rbac)RBAC

Our [Getting Started](../hello-world/start-using-sdk.md) guide introduced basic authentication against a Couchbase cluster:

```java
Cluster cluster = Cluster.connect("127.0.0.1", "Administrator", "password");
```

If you need to provide custom options, the same credentials can be supplied to the `ClusterOptions`:

```java
Cluster cluster = Cluster.connect("127.0.0.1", clusterOptions("Administrator", "password"));
```

Note that this is actually just a convenience overload for the `PasswordAuthenticator`, which can also be used directly to supply more advanced options.

```java
PasswordAuthenticator authenticator = PasswordAuthenticator.builder().username("Administrator")
    .password("password")
    // enables only the PLAIN authentication mechanism, used with LDAP
    .onlyEnablePlainSaslMechanism().build();

Cluster cluster = Cluster.connect("127.0.0.1", clusterOptions(authenticator));
```

In this example, the `PLAIN` authentication mechanism is enabled as well, which is needed if LDAP is enabled on the server side and no TLS encrypted connection is used.

Couchbase uses Role Base Access Control (RBAC), and has since Server 5.0 was released. For a general overview of Couchbase-Server authorization, see [Authorization](../../../server/current/learn/security/authorization-overview.md). For a list of available roles and corresponding privileges, see [Roles](../../../server/current/learn/security/roles.md).

In the SDK docs, many examples will use the full _Administrator_ role for convenience, but this is rarely a good idea on a production machine, so reference the above links to find best practice for the needs of your application. RBAC is also implemented by the Community Edition of Couchbase Server, but with fewer roles — see the [Roles overview](../../../server/current/learn/security/roles.md).

## [](#certificate-authentication)Certificate Authentication

Couchbase Server supports the use of X.509 certificates to authenticate clients (only available in the Enterprise Edition, not the Community Edition). This allows authenticated users to access specific resources by means of the data service, in Couchbase Server 5.1 and up, and all other services in more recent releases of Couchbase Data Platform.

The process relies on a certificate authority, for the issuing of certificates that validate identities. A certificate includes information such as the name of the entity it identifies, an expiration date, the name of the authority that issued the certificate, and the digital signature of the authority. A client attempting to access Couchbase Server can present a certificate to the server, allowing the server to check the validity of the certificate. If the certificate is valid, the user under whose identity the client is running, and the roles assigned that user, are verified. If the assigned roles are appropriate for the level of access requested to the specified resource, access is granted.

For a more detailed conceptual description of using certificates, see [Certificates](../../../server/current/learn/security/certificates.md).

## [](#authenticating-the-java-client-by-certificate)Authenticating the Java Client by Certificate

To learn how to generate and deploy certificates, see [Manage Certificates](../../../server/current/manage/manage-security/manage-certificates.md). The rest of this section assumes you followed those processes, or did something similar.

For the following example, you will need a client certificate and the associated private key. These must be stored together in the same Java KeyStore file or pkcs12 bundle.

If your cluster’s root certificate does not come from a well-known Certificate Authority (CA), you must tell the client to trust the cluster’s root certificate. This example assumes the cluster’s root certificate is available in a file called `ca-cert.pem`.

> [!TIP]
> To trust multiple root certificates, put them all in the same `ca-certs.pem` file.

```java
// Replace the following line with code that gets your actual key store.
// The key store contains the client's certificate and private key.
KeyStore keyStore = loadKeyStore();

Authenticator authenticator = CertificateAuthenticator.fromKeyStore(
    keyStore,
    "keyStorePassword"
);

Cluster cluster = Cluster.connect(
    "couchbases://127.0.0.1",
    clusterOptions(authenticator)
        .environment(env -> env
            .securityConfig(security -> security
                // Tell the client to trust the cluster's root certificate.
                // If your cluster's root certificate is from a well-known
                // Certificate Authority (CA), you can skip this.
                .trustCertificate(Paths.get("/path/to/ca-cert.pem"))
            )
        )
);        
```

`CertificateAuthenticator` has several static factory methods. If you prefer not to load your own `KeyStore` object, you can create a `CertificateAuthenticator` from a `Path` to a key store file, or from an in-memory certificate & key. For maximum flexibility, you can even provide your own `KeyManagerFactory`. Please see the [API documentation](https://docs.couchbase.com/sdk-api/couchbase-core-io/com/couchbase/client/core/env/CertificateAuthenticator.html) for the `CertificateAuthenticator` for more details.

## [](#ldap)LDAP

If you are on a network where access is controlled by LDAP, the SDK will work transparently with it. Please pay attention to the following important note on secure connection.

> [!IMPORTANT]
> If [LDAP](../../../server/current/manage/manage-security/configure-ldap.md#understanding-ldap-authentication) is enabled, Couchbase Server will only allow PLAIN sasl authentication which by default, for good security, the SDK will not allow. Although this can be overridden in a development environment, by explicitly enabling PLAIN in the password authenticator, _the secure solution_ is [to use TLS](managing-connections.md#ssl).

```java
PasswordAuthenticator authenticator = PasswordAuthenticator.builder().username("Administrator")
    .password("password")
    // enables only the PLAIN authentication mechanism, used with LDAP
    .onlyEnablePlainSaslMechanism().build();

Cluster cluster = Cluster.connect("127.0.0.1", clusterOptions(authenticator));
```

Note that `.onlyEnablePlainSaslMechanism()` requires SDK 3.0.9 or newer.