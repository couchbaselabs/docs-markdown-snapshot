---
title: Authentication
description: As well as Role-Based Access Control (RBAC), Couchbase offers
  connection with Certificate Authentication, and works transparently with LDAP.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/howtos/pages/sdk-authentication.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:4.2@php-sdk:howtos:sdk-authentication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/4.2/howtos/sdk-authentication.html)

# Authentication

> As well as Role-Based Access Control (RBAC), Couchbase offers connection with Certificate Authentication, and works transparently with LDAP. 

Our [Getting Started](../hello-world/start-using-sdk.md) guide covered the basics for authorizing against a Couchbase cluster, but you may need to use alternative authentication methods such as Certification.

## [](#rbac)RBAC

Our [Getting Started](../hello-world/start-using-sdk.md) guide introduced basic authentication against a Couchbase cluster:

```php
$options = new ClusterOptions();
$options->credentials("Administrator", "password");
$cluster = new Cluster("couchbase://localhost", $options);
$bucket = $cluster->bucket("travel-sample");
```

Unresolved include directive in modules/howtos/pages/sdk-authentication.adoc - include::7.5@sdk:shared:partial$auth-overview.adoc\[\]

Unresolved include directive in modules/howtos/pages/sdk-authentication.adoc - include::7.5@sdk:shared:partial$auth-overview.adoc\[\]

## [](#authenticating-a-php-client-by-certificate)Authenticating a PHP Client by Certificate

For sample procedures whereby certificates can be generated and deployed, see [Manage Certificates](#6.5@server:manage:manage-security/manage-certificates.adoc). The rest of this document assumes that the processes there, or something similar, have been followed:

```php
$options = new ClusterOptions();
$options->credentials("Administrator", "password");

# authentication with TLS client certificate
$connectionString = "couchbases://localhost?" .
    "truststorepath=/path/to/ca/certificates.pem&" .
    "certpath=/path/to/client/certificate.pem&" .
    "keypath=/path/to/client/key.pem";

$cluster = new Cluster($connectionString, $options);
$bucket = $cluster->bucket("travel-sample");
```

Note the options passed into the connection string:

* `truststorepath` specifies the path (on the local filesystem) to the server’s SSL certificate truststore. The trust store is optional, and when missing, the library will use `certpath` as the location for verification, and expect any extra certificates to be concatenated in there.
* `certpath` specifies the path (on the local filesystem) to the server’s SSL certificate.
* `keypath` specifies the path (on the local filesystem) to the client SSL private key.

Unresolved include directive in modules/howtos/pages/sdk-authentication.adoc - include::7.5@sdk:shared:partial$auth-overview.adoc\[\]

```php
$options = new ClusterOptions();
$options->credentials("Administrator", "password");
$cluster = new Cluster("couchbase://localhost?sasl_mech_force=PLAIN", $options);
$bucket = $cluster->bucket("travel-sample");
```