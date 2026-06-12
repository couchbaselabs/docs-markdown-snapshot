---
title: Authenticating
description: As well as Role-Based Access Control (RBAC), Couchbase offers
  connection with Certificate Authentication, and works transparently with LDAP.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.9/modules/howtos/pages/sdk-authentication.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:dotnet-sdk:howtos:sdk-authentication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/current/howtos/sdk-authentication.html)

# Authenticating

> As well as Role-Based Access Control (RBAC), Couchbase offers connection with Certificate Authentication, and works transparently with LDAP. 

## [](#password-authentication)Password Authentication

The most common way to connect. Uses SASL (PLAIN over TLS, or SCRAM-SHA1 without TLS) for Key-Value operations, and HTTP Basic auth for Query, Search, Analytics, and management services.

```csharp
var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithPasswordAuthentication("Administrator", "password");

var cluster = await Cluster.ConnectAsync(options);
```

Under the hood, `WithPasswordAuthentication` creates a `PasswordAuthenticator` and sets it through `options`. You can also create and pass an authenticator directly.

```csharp
var authenticator = new PasswordAuthenticator("Administrator", "password");

var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithAuthenticator(authenticator);

var cluster = await Cluster.ConnectAsync(options);
```

### [](#migrating-from-the-old-api)Migrating from the Old API

If you were previously setting credentials via `ClusterOptions.UserName`/`Password` or `WithCredentials()`, replace them with `WithPasswordAuthentication()`. The old properties still work but are marked `[Obsolete]`.

```csharp
// Old: setting credentials via properties or WithCredentials()
var options = new ClusterOptions
{
    UserName = "Administrator",
    Password = "password"
};
// or: new ClusterOptions().WithCredentials("Administrator", "password");
options.WithConnectionString("couchbases://your-ip");

var cluster = await Cluster.ConnectAsync(options);
```

becomes:

```csharp
var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithPasswordAuthentication("Administrator", "password");

var cluster = await Cluster.ConnectAsync(options);
```

## [](#certificate-authentication-mtls)Certificate Authentication (mTLS)

For mutual TLS (mTLS), the server verifies the client's identity via an X.509 certificate presented during the TLS handshake.

The SDK uses `CertificateAuthenticator` to hold the client certificate factory.

```csharp
var clientCerts = new X509Certificate2Collection();
clientCerts.Add(new X509Certificate2("path/to/client-cert.pfx", "certPassword"));

var certFactory = new PredefinedCertificateFactory(clientCerts);

var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithCertificateAuthentication(certFactory);

var cluster = await Cluster.ConnectAsync(options);
```

`WithCertificateAuthentication()` automatically sets `EnableTls = true`.

> [!IMPORTANT]
> Only provide **client** certificates to `CertificateAuthenticator`. If you previously bundled server CA certificates alongside client certificates in `X509CertificateFactory`, those should now go into `TlsSettings.TrustedServerCertificateFactory`. See [TLS Settings](#tls-settings) below.

### [](#migrating-from-the-old-api-2)Migrating from the Old API

Replace `WithX509CertificateFactory()` with `WithCertificateAuthentication()`:

```csharp
// Old: using WithX509CertificateFactory
var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithX509CertificateFactory(CertificateFactory.GetCertificatesFromStore(
        new CertificateStoreSearchCriteria
        {
            FindValue = "value",
            X509FindType = X509FindType.FindBySubjectName,
            StoreLocation = StoreLocation.CurrentUser,
            StoreName = StoreName.CertificateAuthority
        }));

var cluster = await Cluster.ConnectAsync(options);
```

becomes:

```csharp
var certFactory = CertificateFactory.GetCertificatesFromStore(
    new CertificateStoreSearchCriteria
    {
        FindValue = "value",
        X509FindType = X509FindType.FindBySubjectName,
        StoreLocation = StoreLocation.CurrentUser,
        StoreName = StoreName.CertificateAuthority
    });

var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithCertificateAuthentication(certFactory);

var cluster = await Cluster.ConnectAsync(options);
```

### [](#rotating-certificates)Rotating Certificates

In environments where client certificates rotate periodically, you have two options.

#### [](#option-1-rotatingcertificatefactory)Option 1: RotatingCertificateFactory

`RotatingCertificateFactory` wraps another factory and polls for new certificates on a configurable interval:

```csharp
var baseCertFactory = CertificateFactory.GetCertificatesFromStore(
    new CertificateStoreSearchCriteria
    {
        FindValue = "value",
        X509FindType = X509FindType.FindBySubjectName,
        StoreLocation = StoreLocation.CurrentUser,
        StoreName = StoreName.CertificateAuthority
    });

var rotatingFactory = new RotatingCertificateFactory(
    certificateFactoryImplementation: baseCertFactory,
    interval: TimeSpan.FromHours(1),   // Check for new certs every hour
    expiresIn: TimeSpan.FromDays(30),  // Only pick up certs valid for at least 30 days
    logger: null                       // Pass a real ILogger<RotatingCertificateFactory> in production
);

var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithCertificateAuthentication(rotatingFactory);

var cluster = await Cluster.ConnectAsync(options);
```

When the factory detects new certificates (via its `HasUpdates` property), the SDK picks them up automatically for new KV connections and reconfigures the HTTP handler.

#### [](#option-2-swap-the-authenticator-at-runtime)Option 2: Swap the Authenticator at Runtime

If you need explicit control over when certificates rotate, use `cluster.Authenticator()` to swap in a new `CertificateAuthenticator` while the cluster is live:

```csharp
var initialCertFactory = new PredefinedCertificateFactory(new X509Certificate2Collection());

var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithCertificateAuthentication(initialCertFactory);

var cluster = await Cluster.ConnectAsync(options);

// Later, when certificates need to rotate:
var newClientCerts = new X509Certificate2Collection();
newClientCerts.Add(new X509Certificate2("path/to/new-client-cert.pfx", "newCertPassword"));

var newCertFactory = new PredefinedCertificateFactory(newClientCerts);
((IClusterAuthenticator)cluster).Authenticator(new CertificateAuthenticator(newCertFactory));
```

You may experience brief disruptions to HTTP requests in-flight during the \`HttpMessageHandler's reconfiguration. Existing KV connections are not closed or re-authenticated, they continue using the old certificate until they are recycled by the connection pool.

## [](#runtime-authenticator-swapping)Runtime Authenticator Swapping

`cluster.Authenticator(newAuthenticator)` replaces the active authenticator on a live cluster without tearing down the connection. This is the mechanism for credential and certificate rotation.

```csharp
var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithPasswordAuthentication("Administrator", "oldPassword");

var cluster = await Cluster.ConnectAsync(options);

// When credentials change, swap in a new authenticator.
// New connections will use the updated credentials immediately;
// existing connections continue with the old credentials until recycled.
((IClusterAuthenticator)cluster).Authenticator(new PasswordAuthenticator("Administrator", "newPassword"));
```

### [](#constraints)Constraints

* **You cannot switch authenticator types at runtime.**If you connected with a `PasswordAuthenticator`, you must continue swapping `PasswordAuthenticator` instances. Attempting to switch to `CertificateAuthenticator` (or vice versa) throws `InvalidArgumentException`.
* **For `PasswordAuthenticator` and `CertificateAuthenticator`:** new credentials apply to new connections only. Existing connections keep using the old credentials until they are naturally recycled.

## [](#tls-settings)TLS Settings

TLS configuration has been reorganized. Settings that control server certificate validation — trust anchors, name-mismatch flags, custom callbacks, protocol versions — now live in a dedicated `TlsSettings` object rather than being scattered across `ClusterOptions`.

### [](#migrating-from-the-old-api-3)Migrating from the Old API

The old properties on `ClusterOptions` (`KvIgnoreRemoteCertificateNameMismatch`, `HttpIgnoreRemoteCertificateMismatch`, `KvCertificateCallbackValidation`, `HttpCertificateCallbackValidation`, `EnabledSslProtocols`) are still functional — they delegate to `TlsSettings` internally — but are marked `[Obsolete]`.

```csharp
// Old: TLS options set directly on ClusterOptions (deprecated in 3.9.0)
var options = new ClusterOptions
{
    EnableTls = true,
    KvIgnoreRemoteCertificateNameMismatch = true,
    HttpIgnoreRemoteCertificateMismatch = true,
    EnabledSslProtocols = SslProtocols.Tls12 | SslProtocols.Tls13
};
options.WithConnectionString("couchbases://your-ip");
options.WithCredentials("Administrator", "password");
```

becomes:

```csharp
var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithPasswordAuthentication("Administrator", "password")
    .WithTlsSettings(tls =>
    {
        // Dev environments only — do not use in production.
        tls.KvIgnoreRemoteCertificateNameMismatch = true;
        tls.HttpIgnoreRemoteCertificateNameMismatch = true;
        tls.EnabledSslProtocols = SslProtocols.Tls12 | SslProtocols.Tls13;
    });
```

### [](#trusting-custom-server-ca-certificates)Trusting Custom Server CA Certificates

Previously, server CA certificates and client certificates were often mixed together in `X509CertificateFactory`. They are now properly separated:

* **Client certificates** → `WithCertificateAuthentication()` (for mTLS)
* **Server CAs** → `TlsSettings.TrustedServerCertificateFactory`

Use `WithTrustedServerCertificates()` as a shorthand:

```csharp
var serverCaCerts = new X509Certificate2Collection();
serverCaCerts.Add(new X509Certificate2("path/to/server-ca.pem"));

var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithPasswordAuthentication("Administrator", "password")
    .WithTrustedServerCertificates(serverCaCerts);
```

Or configure the factory directly inside `WithTlsSettings()`:

```csharp
var serverCaCerts = new X509Certificate2Collection();
serverCaCerts.Add(new X509Certificate2("path/to/server-ca.pem"));

var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithPasswordAuthentication("Administrator", "password")
    .WithTlsSettings(tls =>
    {
        tls.TrustedServerCertificateFactory = new PredefinedCertificateFactory(serverCaCerts);
    });
```

### [](#tlssettings-properties-reference)TlsSettings Properties Reference

| Property                                | Description                                                                                                                            | Default          |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| TrustedServerCertificateFactory         | Factory providing server CA certificates for validation. Set this when you need CustomRootTrust in addition to the system trust store. | null             |
| KvIgnoreRemoteCertificateNameMismatch   | Ignore cert name mismatches for KV connections.                                                                                        | false            |
| HttpIgnoreRemoteCertificateNameMismatch | Ignore cert name mismatches for HTTP connections.                                                                                      | false            |
| KvCertificateValidationCallback         | Custom callback for KV server certificate validation. Receives the standard .NET RemoteCertificateValidationCallback signature.        | null             |
| HttpCertificateValidationCallback       | Custom callback for HTTP server certificate validation.                                                                                | null             |
| EnabledSslProtocols                     | Allowed SSL/TLS protocol versions.                                                                                                     | TLS 1.2, TLS 1.3 |
| EnableCertificateRevocation             | Check certificate revocation lists (CRL) during validation.                                                                            | false            |

> [!TIP]
> Avoid `KvIgnoreRemoteCertificateNameMismatch` and `HttpIgnoreRemoteCertificateNameMismatch` in production. If your server certificate uses IP SANs and your SDK is connecting by hostname (or vice versa), fix the certificate or connection string instead of bypassing validation.

## [](#legacy-precedence-mixing-old-and-new-apis)Legacy Precedence: Mixing Old and New APIs

If you set both a new authenticator (via `With*Authentication()`) and the legacy properties (`UserName`/`Password`, `X509CertificateFactory`), the SDK resolves the effective authenticator at connect time using this order:

1. **Explicit `Authenticator`** — if set via any `With*Authentication()` or `WithAuthenticator()` call, it wins. Legacy properties are ignored.
2. **`X509CertificateFactory`** — if no explicit authenticator was set but a cert factory is configured, the SDK creates a `CertificateAuthenticator` from it. It assume all Certificates from the factory are client certs.
3. **`UserName` / `Password`** — if neither of the above is set but `UserName` is non-empty, the SDK creates a `PasswordAuthenticator`.
4. **None** — throws `InvalidConfigurationException` at connect time.

```csharp
// Don't do this. WithPasswordAuthentication sets an explicit Authenticator
// which takes precedence over the cert factory below — the SDK connects with
// password auth and the certificate factory is silently ignored.
var certFactory = new PredefinedCertificateFactory(new X509Certificate2Collection());
var options = new ClusterOptions()
    .WithConnectionString("couchbases://your-ip")
    .WithX509CertificateFactory(certFactory)         // sets X509CertificateFactory AND Authenticator
    .WithPasswordAuthentication("Administrator", "password"); // overwrites Authenticator
```

The simplest rule: **pick one `With*Authentication()` method and don't mix it with legacy properties.**Remove `UserName`/`Password`/`X509CertificateFactory` and replace them with the equivalent new call.

## [](#api-summary)API Summary

| Old API                                                 | New API (3.9.0+)                                                               |
| ------------------------------------------------------- | ------------------------------------------------------------------------------ |
| ClusterOptions.UserName / Password                      | WithPasswordAuthentication(username, password)                                 |
| WithCredentials(username, password)                     | WithPasswordAuthentication(username, password)                                 |
| X509CertificateFactory (client certs)                   | WithCertificateAuthentication(factory)                                         |
| WithX509CertificateFactory(factory)                     | WithCertificateAuthentication(factory)                                         |
| X509CertificateFactory (server CAs for CustomRootTrust) | TlsSettings.TrustedServerCertificateFactory or WithTrustedServerCertificates() |
| KvIgnoreRemoteCertificateNameMismatch                   | TlsSettings.KvIgnoreRemoteCertificateNameMismatch                              |
| HttpIgnoreRemoteCertificateMismatch                     | TlsSettings.HttpIgnoreRemoteCertificateNameMismatch                            |
| KvCertificateCallbackValidation                         | TlsSettings.KvCertificateValidationCallback                                    |
| HttpCertificateCallbackValidation                       | TlsSettings.HttpCertificateValidationCallback                                  |
| EnabledSslProtocols                                     | TlsSettings.EnabledSslProtocols                                                |
| n/a                                                     | cluster.Authenticator(newAuthenticator) (runtime swap)                         |

Couchbase uses Role Base Access Control (RBAC), and has since Server 5.0 was released. For a general overview of Couchbase-Server authorization, see [Authorization](../../../server/current/learn/security/authorization-overview.md). For a list of available roles and corresponding privileges, see [Roles](../../../server/current/learn/security/roles.md).

In the SDK docs, many examples will use the full _Administrator_ role for convenience, but this is rarely a good idea on a production machine, so reference the above links to find best practice for the needs of your application. RBAC is also implemented by the Community Edition of Couchbase Server, but with fewer roles — see the [Roles overview](../../../server/current/learn/security/roles.md).

## [](#certificate-authentication)Certificate Authentication

Couchbase Server supports the use of X.509 certificates to authenticate clients (only available in the Enterprise Edition, not the Community Edition). This allows authenticated users to access specific resources by means of the data service, in Couchbase Server 5.1 and up, and all other services in more recent releases of Couchbase Data Platform.

The process relies on a certificate authority, for the issuing of certificates that validate identities. A certificate includes information such as the name of the entity it identifies, an expiration date, the name of the authority that issued the certificate, and the digital signature of the authority. A client attempting to access Couchbase Server can present a certificate to the server, allowing the server to check the validity of the certificate. If the certificate is valid, the user under whose identity the client is running, and the roles assigned that user, are verified. If the assigned roles are appropriate for the level of access requested to the specified resource, access is granted.

For a more detailed conceptual description of using certificates, see [Certificates](../../../server/current/learn/security/certificates.md).

## [](#ldap)LDAP

If you are on a network where access is controlled by LDAP, the SDK will work transparently with it. Please pay attention to the following important note on secure connection.

> [!IMPORTANT]
> If [LDAP](../../../server/current/manage/manage-security/configure-ldap.md#understanding-ldap-authentication) is enabled, Couchbase Server will only allow PLAIN sasl authentication which by default, for good security, the SDK will not allow. Although this can be overridden in a development environment, by explicitly enabling PLAIN in the password authenticator, _the secure solution_ is [to use TLS](managing-connections.md#ssl).