---
title: Secure Sync Gateway Access
description: Couchbase Sync Gateway TLS encryption and verification
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.2/modules/ROOT/pages/secure-sgw-access.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.2@sync-gateway::secure-sgw-access.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.2/secure-sgw-access.html)

# Secure Sync Gateway Access

> Couchbase Sync Gateway TLS encryption and verification  

Related _Security_ topics: [User Authentication](authentication-users.md) | [TLS Certificate Authentication](authentication-certs.md)

## [](#overview)Overview

TLS is required by default for all communications with Couchbase Server \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]. TLS v1.3 is supported as the default protocol.

We strongly recommend always having TLS enabled, although this can be over-ridden for **development and testing only**.

Additionally, the _Admin_ and _Metrics REST API_ security is also enhanced by the use of _Couchbase Server RBAC user_ credentials to authenticate and authorize access — see: [REST API Access](rest-api-access.md)

## [](#lbl-cbs-comms)Couchbase Server Connection

By default _Sync Gateway_ requires TLS encryption and the server scheme is specified as `couchbases://`.

You can set the [bootstrap.server\_tls\_skip\_verify](configuration-schema-bootstrap.md#bootstrap-server%5Ftls%5Fskip%5Fverify) flag `true` to connect to 'default CBS'. But, this must only be done for testing or development purposes.

The content in [Table 1](#tbl-tls-config-options) shows the TLS configuration options for Sync Gateway-Couchbase Server communication. The options include flags that will allow you to override the requirement to use TLS — for use in testing and-or development environments **only**.

__Table 1\. Configuration options Sync Gateway ←→Couchbase Server__
| Bootstrap Configuration /Command-line flag                                    | Default Behavior                                                                                                                                                                | Opt-out                                                                                                                                                                                                      |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| bootstrap.use\_tls\_serverCLI: \-bootstrap.use\_tls\_server                   | TLS enabled                                                                                                                                                                     | Set this false in CLI or bootstrap file to turn-off off TLS completely — **development and testing only**                                                                                                    |
| bootstrap.server\_tls\_skip\_verifyCLI: \-bootstrap.server\_tls\_skip\_verify | TLS enabled unless use\_tls\_server opt-out used                                                                                                                                | Set this true in CLI or bootstrap file to skip server verification of certificates (self- or CA-signed) but leave encryption enabled. Do not provide ca\_cert\_path Use for **development and testing only** |
| bootstrap.ca\_cert\_pathCLI: \-bootstrap.ca\_cert\_path                       | Provides the path to the root CA certificate to verify the certificate chain and hostname of the Couchbase Server cluster                                                       | Omit if not required                                                                                                                                                                                         |
| bootstrap.x509\_cert\_pathCLI: \-bootstrap.x509\_cert\_path                   | Provides the path to the client's certificate to authenticate against Couchbase Server \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] [2](#%5Ffootnoteref%5F2). 5.5 or above     | Omit if not required                                                                                                                                                                                         |
| bootstrap.x509\_key\_pathCLI: \-bootstrap.x509\_key\_path                     | Provides the path to the the client's private key to authenticate against Couchbase Server \[[3](#%5Ffootnotedef%5F3 "View footnote.")\] [3](#%5Ffootnoteref%5F3). 5.5 or above | Omit if not required                                                                                                                                                                                         |

### [](#behavior)Behavior

__Table 2\. Sync Gateway ←→ Couchbase Server behavior__
| Required Configuration                                                                                                                                                                                                                                                                                                                            | Default Behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Opt-Out Trigger                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Use couchbases:// server schemeSet the certificate and key path: [bootstrap.ca\_cert\_path](configuration-schema-bootstrap.md#bootstrap-ca%5Fcert%5Fpath) [bootstrap.x509\_cert\_path](configuration-schema-bootstrap.md#bootstrap-x509%5Fcert%5Fpath) [bootstrap.x509\_key\_path](configuration-schema-bootstrap.md#bootstrap-x509%5Fkey%5Fpath) | Sync Gateway will error non-secure server schemes (couchbase: or ws:) unless the opt-out is triggered If a ca\_cert\_path is specified then only certificates from that CA will be accepted. If ca\_cert\_path is omitted If server\_skip\_tls\_verify=trueThen Sync Gateway will skip validation of any server cert, but still require encryption. This includes skipping validation of certs that are from a trusted/well known CA If server\_skip\_tls\_verify=falseThen only certificates from a trusted/well known CA will be accepted | use\_tls\_server=false server\_skip\_tls\_verify=true (or included) |

For more on creating and installing certificates, see: [TLS Certificate Authentication](authentication-certs.md).

## [](#client-connection)Client Connection

Couchbase Lite client applications must be updated to use TLS when connecting to Sync Gateway nodes running in default mode.

[Table 1](#tbl-tls-config-options) shows the TLS configuration options, whilst [Table 4](#tbl-replication-behavior) shows the default and opt-out behavior.

__Table 3\. TLS configuration options__
| Bootstrap Configuration   | Command-line flag           | Default | Purpose                                                                                                                                                                                            |
| ------------------------- | --------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api.https.tls\_key\_path  | \-api.https.tls\_key\_path  | nil     | Provide the path \[[4](#%5Ffootnotedef%5F4 "View footnote.")\] to the TLS private key file. [4](#%5Ffootnoteref%5F4). This can be absolute, or relative to the Sync Gateway executable's directory |
| api.https.tls\_cert\_path | \-api.https.tls\_cert\_path | \-      | Provide the path to the TLS certificate file.                                                                                                                                                      |

Omit both options to use _plaintext_ — for development and-or testing **only** — see the [Bootstrap Configuration](configuration-schema-bootstrap.md).

__Table 4\. TLS behavior__
| Configuration Properties                                                                                                                                                                    | Default Behavior                                                                       | Opt-Out Trigger         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ----------------------- |
| [api.api.https.tls\_cert\_path](configuration-schema-bootstrap.md#api-https-tls%5Fcert%5Fpath) [api.api.https.tls\_key\_path](configuration-schema-bootstrap.md#api-https-tls%5Fkey%5Fpath) | TLS verification and encryption is enabled by default, unless the opt-out is triggered | Omit from configuration |

## [](#running-sync-gateway)Running Sync Gateway

### [](#as-a-service)As a Service

The `serviceconfig.json` file uses the `couchbases:` scheme, with `server_skip_tls_verify=true` by default, to facilitate testing and development; no TLS validation is done.

Use the following settings to configure TLS:

* [bootstrap.ca\_cert\_path](configuration-schema-bootstrap.md#bootstrap-ca%5Fcert%5Fpath)
* [bootstrap.x509\_cert\_path](configuration-schema-bootstrap.md#bootstrap-x509%5Fcert%5Fpath)
* [bootstrap.x509\_key\_path](configuration-schema-bootstrap.md#bootstrap-x509%5Fkey%5Fpath)
* [bootstrap.server\_tls\_skip\_verify](configuration-schema-bootstrap.md#bootstrap-server%5Ftls%5Fskip%5Fverify)

For more on configuration options, see: [Bootstrap Configuration](configuration-schema-bootstrap.md).

### [](#command-line)Command Line

Use the following command line flags to configure TLS:

* \-bootstrap.ca\_cert\_path
* \-bootstrap.x509\_cert\_path
* \-bootstrap.x509\_key\_path
* \-bootstrap.server\_skip\_tls\_verify

Sync Gateway will error non-secure server schemes (`couchbase:` or `ws:`) unless the opt-out option is true.

Note that you can no longer start Sync Gateway without providing at least one parameter, as with no configuration file specified, you need to either provide a TLS Cert/Key, or disable TLS.

For more on command line options, see: [Command Line Options](command-line-options.md).

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

---

[1](#%5Ffootnoteref%5F1). From release 3.0