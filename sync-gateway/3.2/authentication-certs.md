---
title: TLS Certificate Authentication
description: Securing Couchbase Sync Gateway with TLS Authentication
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.2/modules/ROOT/pages/authentication-certs.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/3.2/authentication-certs.html)

# TLS Certificate Authentication

> Securing Couchbase Sync Gateway with TLS Authentication  
> This content explains how to implement TLS Certificate Authentication for Sync Gateway

Related _Security_ topics: [User Authentication](authentication-users.md) | [Sync Function](#sync-function-overview.adoc) | [Import filter](import-processing.md) | [Read Access](access-control-how-control-document-access.md#lbl-read-access) | [Write Access](access-control-how-control-document-access.md)

## [](#data-access)Data Access

**Authentication**

In a Couchbase Mobile production deployment, administrators typically perform operations on the Admin REST API. If Sync Gateway is deployed on an internal network, you can bind the [api.admin\_interface](configuration-schema-bootstrap.md#api-admin%5Finterface) of Sync Gateway to the internal network. In this case, the firewall should also be configured to allow external connections to the public [api.public\_interface](configuration-schema-bootstrap.md#api-public%5Finterface).

To access the Admin REST API from an entirely different network or from a remote desktop we recommend to use [SSH tunneling](https://whatbox.ca/wiki/SSH%5FTunneling).

**Authorization**

In addition to the Admin REST API, a user can be assigned to a role with additional privileges. The role and the user assigned to it can be created in the configuration file. Then, the Sync Function’s [requireRole()](sync-function-api-require-role-cmd.md) helper function can be used to allow certain operations only if the user has that role.

**Data Model Validation**

In a NoSQL database, it is the application’s responsibility to ensure that the documents are created in accordance with the data model adopted throughout the system. As an additional check, the Sync Function’s [throw()](sync-function-api-throw-cmd.md) method can be used to reject documents that do not follow the pre-defined data model.

## [](#connection-to-sync-gateway)Connection to Sync Gateway

You can run Sync Gateway behind a reverse proxy, such as NGINX, which supports HTTPS connections and route internal traffic to Sync Gateway over HTTP. The advantage of this approach is that NGINX can proxy both HTTP and HTTPS connections to a single Sync Gateway instance.

Sync Gateway also supports serving connections over SSL. To enable SSL, you need to add two properties to the config file:

`"SSLCert"`

A path to a PEM-format file containing an X.509 certificate or a certificate chain.

`"SSLKey"`

A path to a PEM-format file containing the certificate’s matching private key.

If both properties are present, the server will respond to SSL (and only SSL) over both the public and admin ports. If you want to support both HTTP and HTTPS connections you will need to run two separate instances of Sync Gateway.

## [](#how-to-create-an-ssl-certificate)How to Create an SSL Certificate

Certificates are a complex topic. There are basically two routes you can go: request a certificate from a Certificate Authority (CA), or create your own "self-signed" certificate.

## [](#requesting-a-certificate-from-a-ca)Requesting a Certificate from a CA

You can obtain a certificate from a trusted [Certificate Authority](https://en.wikipedia.org/wiki/Certificate%5Fauthority) (CA). Examples of trusted CAs include [Let’s Encrypt](https://letsencrypt.org/), Thawte or GoDaddy. What this means is that their own root certificates are known and trusted by operating systems, so any certificate that they sign will also be trusted.

Hence, the benefit of a certificate obtained from a trusted CA is that it will be trusted by any SSL client.

## [](#creating-a-self-signed-certificate)Creating a Self-Signed Certificate

Unlike a CA-signed cert, a self-signed cert isn’t intrinsically trustworthy: a client can’t tell who you are by examining the cert, because no recognized authority has vouched for it. But a self-signed cert is still unique (only you, as the holder of the private key, can operate a server using that cert), and it still allows the connection to be encrypted.

It’s easy to create a self-signed certificate using the openssl command-line tool and these directions. In a nutshell, you just need to run these commands:

```bash
$ openssl genrsa -out privkey.pem 2048
$ openssl req -new -x509 -sha256 -key privkey.pem -out cert.pem -days 1095
```

The second command is interactive and will ask you for information like country and city name that goes into the X.509 certificate. You can put whatever you want there; the only important part is the field `Common Name (e.g. server FQDN or YOUR name)` which needs to be the exact _hostname_ that clients will reach your server at. The client will verify that this name matches the hostname in the URL it’s trying to access, and will reject the connection if it doesn’t.

The tool will then create two files: `privkey.pem` (the private key) and `cert.pem` (the public certificate.)

To create a copy of the cert in binary DER format (often stored in a ".cer" file), do this:

```bash
$ openssl x509 -inform PEM -in cert.pem -outform DER -out cert.cer
```

## [](#installing-the-certificate)Installing the Certificate

Whichever way you obtained the certificate, you will now have a private key and an X.509 certificate. Ensure that they’re in separate files and in PEM format, and put them in a directory that’s readable by the Sync Gateway process. The private key is very sensitive (it’s not encrypted) so make sure the file isn’t readable by unauthorized processes.

Then just add the `"SSLCert"` and `"SSLKey"` properties to your Sync Gateway configuration file.

```javascript
{

  "SSLCert": "cert.pem",
  "SSLKey": "privkey.pem",

}
```

Start Sync Gateway and access the public port over `https` on https://localhost:4984.

## [](#connection-to-couchbase-server)Connection to Couchbase Server

There are two methods to securely connect a Sync Gateway instance to a Couchbase Server cluster. Each method is discussed below in more detail.

### [](#username-and-password)Username and Password

The username and password of the RBAC user are specified in the Sync Gateway configuration file. This method is used in the getting started [section](get-started-install.md#start-sync-gateway).

### [](#x-509-certificates)X.509 Certificates

Sync Gateway 2.1 adds the ability to use X.509 certificates to authenticate against Couchbase Server 5.5 or higher. This functionality can be used instead or in addition to the existing authentication method which is to specify a username and password in the configuration file.

To use X.509 certificate based authentication with Sync Gateway, you must first run through the following procedures.

1. [Create a Root and Node Certificates](../../server/current/manage/manage-security/configure-server-certificates.md#root-and-node-certificates).
2. [Enable Client Certificate Authentication](../../server/current/manage/manage-security/configure-server-certificates.md#client-certificate-enablement).

Once the Couchbase Server cluster has been protected by the deployment of root and node certificates described above, a _client_ certificate can be signed by the root certificate, to allow Sync Gateway to access the cluster.

To generate the _client_ certificate, make sure that the Couchbase Server cluster has the expected [bucket and RBAC user](../../server/current/manage/manage-security/configure-client-certificates.md#assumptions). Also refer to the [Getting Started: Configure Couchbase Server](get-started-install.md#configure-couchbase-server) to configure the RBAC user with appropriate privileges for access by a Sync Gateway instance.

Next, follow the instructions in [Client Access: Root-Certificate Authorization](../../server/current/manage/manage-security/configure-client-certificates.md#client-certificate-authorized-by-a-root-certificate) to create a client certificate that is authorized by the cluster’s root certificate.

After completing the procedure, you will have multiple files generated in the current directory. You will use the following files to configure Sync Gateway:

* `servercertfiles/ca.pem`
* `servercertfiles/clientcertfiles/travel-sample.pem`
* `servercertfiles/clientcertfiles/travel-sample.key`

X.509 certificate based authentication is enabled on Sync Gateway by specifying the absolute or relative path to each of those files in the configuration file.

```json
{
  "interface":":4984",
  "logging": {
    "log_file_path": "/var/tmp/sglogs",
    "console": {
      "enabled": true,
      "log_level": "info",
      "log_keys": [
        "*"
      ]
    }
  },
  "databases":{
    "db":{
      "use_views": true,
      "cacertpath": "./ca.pem",
      "certpath": "./clientcertfiles/travel-sample.pem",
      "keypath": "./clientcertfiles/travel-sample.key",
      "server": "couchbases://127.0.0.1:",
      "bucket": "travel-sample",
      "username": "clientuser"
    }
  }
}
```

If the connection is successful, you should see the following in the logs.

```text
[INF] Starting admin server on 127.0.0.1:4985
[INF] Starting server on :4984 ...
[INF] Establishing TLS connection for DCP to destination 127.0.0.1:11207
```

If Sync Gateway cannot connect, you may refer to the [Cluster Certificate Errors](../../server/current/manage/manage-security/handle-certificate-errors.md#cluster-certificate-errors) table.

More detail on the configuration properties for x.509 authentication can be found below.

* [bootstrap.ca\_cert\_path](configuration-schema-bootstrap.md#bootstrap-ca%5Fcert%5Fpath)
* [bootstrap.x509\_cert\_path](configuration-schema-bootstrap.md#bootstrap-x509%5Fcert%5Fpath)
* [bootstrap.x509\_key\_path](configuration-schema-bootstrap.md#bootstrap-x509%5Fkey%5Fpath)

If the **username**/**password** properties are also specified in the configuration file then Sync Gateway will use password-based authentication and also include the client certificate in the TLS handshake.

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