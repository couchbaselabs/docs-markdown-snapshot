[View original HTML](/cxx-sdk/1.1/howtos/sdk-authentication.html)

> As well as Role-Based Access Control (RBAC), Couchbase offers connection with Certificate Authentication, and works transparently with LDAP. 

Our [Getting Started](../hello-world/start-using-sdk.md) guide covered the basics for authorizing against a Couchbase cluster, but you may need to use alternative authentication methods such as Certification.

## [](#rbac)RBAC

Our [Getting Started](../hello-world/start-using-sdk.md) guide introduced basic authentication against a Couchbase cluster:

```scala
Cluster.connect("10.112.180.101", "username", "password") match {
  case Success(cluster) => // Use the cluster
  case Failure(err) => println(s"Failed to open cluster: $err")
}
```

Couchbase uses Role Base Access Control (RBAC), and has since Server 5.0 was released. For a general overview of Couchbase-Server authorization, see [Authorization](#7.1@server:learn:security/authorization-overview.adoc). For a list of available roles and corresponding privileges, see [Roles](#7.1@server:learn:security/roles.adoc).

In the SDK docs, many examples will use the full _Administrator_ role for convenience, but this is rarely a good idea on a production machine, so reference the above links to find best practice for the needs of your application. RBAC is also implemented by the Community Edition of Couchbase Server, but with fewer roles — see the [Roles overview](#7.1@server:learn:security/roles.adoc).

## [](#certificate-authentication)Certificate Authentication

Couchbase Server supports the use of X.509 certificates to authenticate clients (only available in the Enterprise Edition, not the Community Edition). This allows authenticated users to access specific resources by means of the data service, in Couchbase Server 5.1 and up, and all other services in more recent releases of Couchbase Data Platform.

The process relies on a certificate authority, for the issuing of certificates that validate identities. A certificate includes information such as the name of the entity it identifies, an expiration date, the name of the authority that issued the certificate, and the digital signature of the authority. A client attempting to access Couchbase Server can present a certificate to the server, allowing the server to check the validity of the certificate. If the certificate is valid, the user under whose identity the client is running, and the roles assigned that user, are verified. If the assigned roles are appropriate for the level of access requested to the specified resource, access is granted.

For a more detailed conceptual description of using certificates, see [Certificates](#7.1@server:learn:security/certificates.adoc).

## [](#authenticating-a-scala-client-by-certificate)Authenticating a Scala Client by Certificate

For sample procedures whereby certificates can be generated and deployed, see [Manage Certificates](../../../server/7.6/manage/manage-security/manage-certificates.md). The rest of this document assumes that the processes there, or something similar, have been followed. That is, a cluster certificate has been created and installed on the server, a client certificate has been created, and it is stored in a JVM keystore along with the cluster’s certificate.

```scala
// Open the keystore using standard JVM classes
val keystorePassword = new String("storepass").toCharArray
val keystoreFilename = "my.keystore"

// The format to use here depends on the format of the keystore.
// "PKCS12" is what JDK 9+ creates by default.
// "JKS" was the default for JDK 8 and below.
val keystore = KeyStore.getInstance("PKCS12")
val keystoreStream =
  getClass.getClassLoader.getResourceAsStream(keystoreFilename)
keystore.load(keystoreStream, keystorePassword)
keystoreStream.close()

val kmf =
  KeyManagerFactory.getInstance(KeyManagerFactory.getDefaultAlgorithm)
kmf.init(keystore, keystorePassword)

val trustMan =
  TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm)
trustMan.init(keystore)

// Create a Couchbase CertificateAuthenticate that will use that keystore
val auth =
  CertificateAuthenticator.fromKeyManagerFactory(() => kmf)

// Create a Couchbase ClusterEnvironment to enable TLS (required)
val cluster = ClusterEnvironment.builder
  .securityConfig(
    SecurityConfig().enableTls(true).trustManagerFactory(trustMan)
  )
  .build
  .flatMap(
    env => Cluster.connect(hostname, ClusterOptions(auth).environment(env))
  )
```

## [](#ldap)LDAP

If you are on a network where access is controlled by LDAP, the SDK will work transparently with it. Please pay attention to the following important note on secure connection.

|  | If [LDAP](#7.1@server:manage:manage-security/configure-ldap.adoc#understanding-ldap-authentication) is enabled, Couchbase Server will only allow PLAIN sasl authentication which by default, for good security, the SDK will not allow. Although this can be overridden in a development environment, by explicitly enabling PLAIN in the password authenticator, _the secure solution_ is [to use TLS](managing-connections.md#ssl). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |