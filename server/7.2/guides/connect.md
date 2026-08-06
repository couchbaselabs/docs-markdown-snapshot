---
title: Connecting to Couchbase Server
description: How to connect to a Couchbase Cluster.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/connect.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:7.2@server:guides:connect.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/guides/connect.html)

# Connecting to Couchbase Server

> How to connect to a Couchbase Cluster.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

Connecting to Couchbase can be done in several ways. This guide will take you through some of the most common methods used to access a Couchbase cluster with an SDK client or CLI tool.

A Couchbase [Cluster](../learn/clusters-and-availability/clusters-and-availability.md) is a combination of multiple server nodes, which can be accessed by users or applications with a [username and password](../learn/security/usernames-and-passwords.md). Each server node can also be its own cluster or join an existing multi-node setup.

Couchbase uses [Role Based Access Control (RBAC)](../learn/security/roles.md) to control access to its various [services](../learn/services-and-indexes/services/services.md). A user or application can connect to a cluster and use these services, assuming that valid credentials with relevant access roles are provided.

## [](#before-you-begin)Before You Begin

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset.

### [](#couchbase-clients)Couchbase Clients

Clients access data by connecting to a Couchbase cluster over the network. The most common type of client is a Couchbase SDK, which is a full programmatic API that enables applications to take the best advantage of Couchbase. This developer guide focuses on the most commonly-used SDKs, but full explanations and reference documentation for all SDKs is available.

The command line clients also provide a quick and streamlined interface for simple access and are suitable if you just want to access an item without writing any code.

> [!NOTE]
> With some editions, the command line clients are provided as part of the installation of Couchbase Server. Assuming a default installation, you can find them in the following location, depending on your operating system:
> 
> | Linux   | /opt/couchbase/bin                                                       |
> | ------- | ------------------------------------------------------------------------ |
> | Windows | C:\\Program Files\\Couchbase\\Server\\bin                                |
> | macOS   | /Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin |
> 
> If the command line client is not provided with your installation of Couchbase Server, you must install the C SDK in order to use the command line clients.

Read the following for further information about the clients available:

* [Command Line Clients](../../../c-sdk/current/hello-world/cbc.md)
* [SDK Clients](../../../home/sdk.md)

## [](#connecting-via-the-web-console)Connecting via the Web Console

To access a cluster via the Couchbase Server Web Console over an unencrypted connection, navigate to the Web Console address with your browser (by default, `http://localhost:8091`) and enter your credentials.

![The Couchbase Admin](_images/login.png) 

See [Authenticating with the Console](../manage/manage-ui/manage-ui.md#authenticating-with-the-console) for more information.

To access a cluster via the Couchbase Server Web Console over an encrypted connection, navigate to the secure Web Console address with your browser (by default, `https://localhost:18091`) and enter your credentials.

See [Manage Console Access](../manage/manage-security/manage-console-access.md) for more information.

## [](#connecting-via-client)Connecting via Client

Couchbase Server can be configured to run with unencrypted or encrypted network access. When running Couchbase in a production environment, the latter is always recommended.

### [](#basic-auth)Basic Authentication

To connect to a standalone or Docker installation with unencrypted network access, set up a user with [appropriate access levels](../learn/security/roles.md) and a secure password.

* cbc
* .NET
* Java
* Node.js
* Python

Most `cbc` sub-commands will require some form of authentication to access a cluster or perform operations on data within a bucket.

1. To connect to Couchbase Server using `cbc`, pass `-u` for the username, `-P` for the password and `-U` for the connection URL immediately after a sub-command.
2. Provide the bucket name required in the connection URL (couchbase://localhost/<bucket-name>).

---

The example below connects to the `travel-sample` bucket with Admin level credentials and performs a `ping` to check what services are running in a single-node cluster environment.

```shell
cbc ping -u Administrator -P password -U couchbase://localhost/travel-sample \
	--count=1 \
	--table
```

Result

```console
-------------------------------------------------------------------------------
| type  | id       | status | latency, us | remote          | local           |
-------------------------------------------------------------------------------
| cbas  | 0xec22b0 | ok     |        3003 | localhost:8095  | 127.0.0.1:38612 |
| fts   | 0xec0dc0 | ok     |        3842 | localhost:8094  | 127.0.0.1:35636 |
| kv    | 0xeaa220 | ok     |        4446 | localhost:11210 | 127.0.0.1:49426 |
| n1ql  | 0xead260 | ok     |        4249 | localhost:8093  | 127.0.0.1:56740 |
| views | 0xec0430 | ok     |        4045 | localhost:8092  | 127.0.0.1:60088 |
-------------------------------------------------------------------------------
```

> [!NOTE]
> If the user credentials are invalid, `cbc` will return a `LCB_ERR_AUTHENTICATION_FAILURE` error.

For further details, refer to [cbc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5Fcbc.html).

Call the `Cluster.ConnectAsync()` method with a connection URL, username and password.

---

The example below connects to a single-node cluster environment with basic auth credentials.

```csharp
Unresolved include directive in modules/guides/pages/connect.adoc - include::dotnet-sdk:howtos:example$ManagingConnections.csx[]
```

Click the  View button to see this code in context.

For more information, see [Cluster](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Cluster.html).

Call the `Cluster.connect()` method with a connection URL, username and password.

---

The example below connects to a single-node cluster environment with basic auth credentials.

```java
Cluster cluster = Cluster.connect("127.0.0.1", "username", "password");
Bucket bucket = cluster.bucket("travel-sample");
Collection collection = bucket.defaultCollection();

// You can access multiple buckets using the same Cluster object.
Bucket anotherBucket = cluster.bucket("beer-sample");

// You can access collections other than the default
// if your version of Couchbase Server supports this feature.
Scope customerA = bucket.scope("customer-a");
Collection widgets = customerA.collection("widgets");

// For a graceful shutdown, disconnect from the cluster when the program ends.
cluster.disconnect();
```

> [!NOTE]
> If the user credentials provided are invalid, the SDK will return a `AuthenticationFailureException` error.

Click the  View button to see this code in context.

For more information, see [Cluster](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Cluster.html).

Call the `connect()` function with a connection URL, and a `ConnectOptions` object containing the username and password.

---

The example below connects to a single-node cluster environment with basic auth credentials.

```nodejs
Unresolved include directive in modules/guides/pages/connect.adoc - include::nodejs-sdk:howtos:example$auth.js[]
```

> [!NOTE]
> If the user credentials provided are invalid, the SDK will return a `AuthenticationFailureError` error.

Click the  View button to see this code in context.

For more information, see [Cluster](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Cluster.html).

1. Call the `Cluster.connect()` function with a connection URL, and a `ClusterOptions` object containing a `PasswordAutheticator`.
2. Provide a username and password to the `PasswordAutheticator`.

---

The example below connects to a single-node cluster environment with basic auth credentials.

```python
Unresolved include directive in modules/guides/pages/connect.adoc - include::python-sdk:howtos:example$managing_connections.py[]
```

> [!NOTE]
> If the user credentials provided are invalid, the SDK will return a `AuthenticationException` error.

Click the  View button to see this code in context.

For more information, see [Cluster](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#cluster-object).

### [](#tls)TLS Authentication

To connect to a cluster configured with TLS (Transport Layer Security), for encrypted network access, you must supply an [X.509 certificate](../learn/security/certificates.md). Before using X.509 certificate based authentication, you should run through the following:

* [Configure Server Certificates](../manage/manage-security/configure-server-certificates.md)
* [Configure Client Certificates](../manage/manage-security/configure-client-certificates.md)

* cbc
* .NET
* Java
* Node.js
* Python

1. To securely connect to Couchbase Server using `cbc`, pass `-U` for the connection URL immediately after a sub-command.
2. Provide the bucket name required in the connection URL (couchbases://127.0.0.1/<bucket-name>). The scheme "couchbases://" implies an encrypted connection is used.
3. Pass a `certpath` query parameter to the connection URL, after the bucket name.

---

The example below connects to the `travel-sample` bucket with a client certificate, and performs a `ping` to check what services are running in a single-node secured cluster environment.

```shell
cbc ping -v -U "couchbases://127.0.0.1/travel-sample?certpath=ca.pem" \
	--count=1 \
	--table
```

For further details, refer to [cbc(1)](https://docs.couchbase.com/sdk-api/couchbase-c-client/md%5Fdoc%5Fcbc.html).

1. Call the `WithX509CertificateFactory()` method on a `ClusterOptions()` object.
2. Provide the certificate store information to the `WithX509CertificateFactory()` method.
3. Call the `ConnectAsync()` method and pass it the cluster options object.

---

The example below connects to a single-node cluster over a secure connection with a client certificate.

It's assumed that a valid client certificate and certificate store have been set up.

```csharp
Unresolved include directive in modules/guides/pages/connect.adoc - include::dotnet-sdk:howtos:example$Auth.csx[]
```

Click the  View button to see this code in context.

For more information, see [Cluster](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Cluster.html).

1. Load a Java keystore file containing your client certificate and pass it to the `CertificateAuthenticator.fromKeyStore()` method along with the required password.
2. Call the `Cluster.connect()` method and pass the connection string along with cluster options containing the `CertificateAuthenticator` object previously created.

---

The example below connects to a single-node cluster over a secure connection with a client certificate.

It's assumed that a valid client certificate and a Java keystore have been set up.

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

Click the  View button to see this code in context.

For more information, see [Cluster](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Cluster.html).

Call the `connect()` function with a connection URL, and a `ConnectOptions` object containing a certificate `trustStorePath` and user credentials.

---

The example below connects to a single-node cluster over a secure connection with a client certificate.

It's assumed that a valid client certificate has been set up.

```nodejs
Unresolved include directive in modules/guides/pages/connect.adoc - include::nodejs-sdk:howtos:example$auth.js[]
```

Click the  View button to see this code in context.

For more information, see [Cluster](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Cluster.html).

1. Call the `Cluster.connect()` function with a connection URL, and a `ClusterOptions` object containing a `PasswordAutheticator`.
2. Provide a username and password to the `PasswordAutheticator`.
3. Supply a certificate path to the `PasswordAutheticator`.

---

The example below connects to a single-node cluster over a secure connection with a client certificate.

It's assumed that a valid client certificate has been set up.

```python
Unresolved include directive in modules/guides/pages/connect.adoc - include::python-sdk:howtos:example$managing_connections.py[]
```

Click the  View button to see this code in context.

For more information, see [Cluser](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#cluster-object).

## [](#related-links)Related Links

Reference and explanation:

* [Security Overview](../learn/security/security-overview.md)
* [Clusters and Availability](../learn/clusters-and-availability/clusters-and-availability.md)
* [Manage Security](../manage/manage-security/security-management-overview.md)

Connecting with SDKs:

* [C](../../../c-sdk/current/howtos/managing-connections.md)| [C++](../../../cxx-sdk/current/howtos/managing-connections.md)| [.NET](../../../dotnet-sdk/current/howtos/managing-connections.md)| [Go](../../../go-sdk/current/howtos/managing-connections.md)| [Java](../../../java-sdk/current/howtos/managing-connections.md)| [Kotlin](../../../kotlin-sdk/current/howtos/connecting.md)| [Node.js](../../../nodejs-sdk/current/howtos/managing-connections.md)| [PHP](../../../php-sdk/current/howtos/managing-connections.md)| [Python](../../../python-sdk/current/howtos/managing-connections.md)| [Ruby](../../../ruby-sdk/current/howtos/managing-connections.md)| [Scala](../../../scala-sdk/current/howtos/managing-connections.md)