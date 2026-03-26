---
title: Creating or Editing a Reference
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-xdcr-create-ref.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:rest-api:rest-xdcr-create-ref.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/rest-api/rest-xdcr-create-ref.html)

# Creating or Editing a Reference

> You can use the REST API to create or edit an XDCR reference to a target cluster. 

## [](#description)Description

Use the `/pools/default/remoteClusters` REST API endpoint to create an XDCR reference to a target cluster. You must create a reference to a target cluster on the source cluster before you can create a replication. The target cluster is usually a different cluster from the source cluster. However, you can create a replication where the source and target are the same cluster.

You can edit an existing reference using the REST API by adding its name to the URI.

## [](#http-method-and-uri)HTTP Method and URI

Create a new reference

```uri
POST /pools/default/remoteClusters
```

Edit an existing reference

```uri
POST /pools/default/remoteClusters/{REFERENCE_NAME}
```

__Path Parameters__
| Name            | Description                        | Schema |
| --------------- | ---------------------------------- | ------ |
| REFERENCE\_NAME | The name of an existing reference. | String |

## [](#curl-syntax)curl Syntax

```console
curl -v -u <source-cluster-username>:<source-cluster-password>
  http://<source-cluster-ip-address-or-host-name>:8091/pools/default/remoteClusters/[<target-cluster-local-name>]
  -d name=<target-cluster-local-name>
  -d hostname=<target-cluster-ip-address-or-domain-name>[:<port-number>]
  [-d network_type='external']
  [-d demandEncryption=[ 0 | 1 ] ]
  [-d secureType=[ 'none' | 'half' | 'full'] ]
  [-d username=<target-cluster-username>]
  [-d password=<target-cluster-password>]
    [--data-urlencode "certificate=$(cat <local-path-to-target-root-certificate>)"]
    [--data-urlencode "clientCertificate=$(cat <local-path-to-client-pem>)"]
    [--data-urlencode "clientKey=$(cat <local-path-to-client-key>)"]
```

__POST Parameters__
| Name                            | Description                                                                                                                                                                                                                                                                                                                                                                                                          | Schema                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name                            | A local name for the reference. The name does not need to correspond to any network-visible name for the target cluster. When editing an existing reference by supplying its name in the REST API URI, you must still supply the name parameter. Set it to the name of the existing reference to keep its name the same. If you set the name parameter to a different value, Couchbase Server renames the reference. | String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| hostname                        | The hostname or IP address of the reference's target cluster. This value can specify either the internal address or external address (if one has been configured) of the target cluster. For information about using DNS SRV in this context, see [XDCR Security and Networking](../xdcr-reference/xdcr-security-and-networking.md).                                                                                 | String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| network\_type                   | Whether the network address specified in hostname is internal or external.                                                                                                                                                                                                                                                                                                                                           | String. Must be external if the network is external. Do not supply this parameter if the network is internal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| demandEncryption                | Whether to use encryption for the reference's connection to the target cluster.                                                                                                                                                                                                                                                                                                                                      | Integer. Valid values: 0: The default value. Couchbase Server does not use encryption for the connection to the target cluster. 1: Encrypt the connection to the target cluster. Use the secureType parameter to set whether the connection is partially or fully encrypted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| secureType                      | Optional parameter that sets whether the connection to the target cluster is encrypted, and if so, whether it partially or fully encrypts communication. If you do not supply this parameter and you set demandEncryption parameter to 1, the secureType defaults to full.                                                                                                                                           | String. Valid settings are: none: (default value) Couchbase Server does not use encryption for the connection to the target cluster. Couchbase Server sends all traffic unencrypted, including the password. half: Couchbase Server uses encryption only when sending the password to the target cluster during authentication. The data it sends to the target is not encrypted. When using this value, you must provide a username and password. full: Couchbase Server uses encryption to secure all communication with the target cluster. When you choose this value, you must supply a path to a local copy of the target cluster's root certificate in the certificate parameter (except for Capella—​see [the note after this table](#capella%5Fcert%5Fnote)). You must also either supply a username and password or paths to a client certificate and key. |
| username and password           | The username and password to use when authenticating with the target cluster. You must supply these parameters if you did not supply the secureType parameter or set it to none or half. However, if secureType is full you can choose to either use a username and password or to supply a client certificate and key.                                                                                              | String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| certificate                     | The local path to a copy of the root CA of the target cluster. You must supply this parameter if you set secureType to full.                                                                                                                                                                                                                                                                                         | URL-encoded string                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| clientCertificate and clientKey | The client certificate and key that Couchbase Server uses to authenticate with the target cluster. Set these parameters only if you set secureType to full and you have chosen to use a certificate instead of a username and password for authentication.                                                                                                                                                           | URL-encoded string                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

> [!NOTE]
> XDCR automatically trusts Capella root certificates when you use the REST API to enable fully secure replications from Couchbase Enterprise Server to Capella. In this case, you do not need to supply the `certificate` parameter to the command. See [Capella Trusted CAs](../manage/manage-xdcr/secure-xdcr-replication.md#capella-trusted-cas) for more information.

## [](#responses)Responses

200 OK

Successful execution. Couchbase Server creates the reference, and returns the details of the reference in a JSON message. The keys in the JSON message are:

* `certificate`: the root certificate for the target cluster, if one was used, in the creation of a `half` secure or `full` secure connection.
* `clientCertificate`: the client certificate for the source cluster, if one was used, in the creation of a `full` secure connection.
* `deleted`: whether the reference has been deleted. The value can be `true` or `false`.
* `hostname`: the IP address or domain name and port number of the target cluster.
* `name`: the locally defined reference to the target cluster.
* `secureType`: the level of security required for connection. This value can be `none`, `half`, or `full`.
* `uri`: the URI of the locally named target cluster. For example, `"/pools/default/remoteClusters/FirstTarget"`.
* `username`: the username used for authentication with the target cluster. This value is an empty string when not using a username for authentication.
* `uuid`: the universally unique identifier for the reference. For example, `"5ccf771844cd32375df8c4de70e9d44e"`.
* `validateURI` the URI for internal validation of the reference. For example, `"/pools/default/remoteClusters/SecondTarget?just_validate=1"`.

400 Bad Request

Occurs when `secureType` is `full` and you supply both client certificates and a username and password. In this case, Couchbase Server also returns the following message:

```json
{"_":"username and client certificate cannot both be given when secure type is full"}
```

Supply either client certificates or a username and password for authentication with the target cluster, not both.

401 Unauthorized

Authentication failure, such as incorrect username and password.

404 Object Not Found

The URI used in the REST API call was not correct. Couchbase Server respond with this error code if you attempt to edit a non-existent reference by adding its name to the REST API URI.

## [](#required-permissions)Required Permissions

You must have Full Admin, Cluster Admin, or XDCR Admin role to call this API.

## [](#examples)Examples

The following examples demonstrate how to create a reference. All examples are piped through [jq](https://stedolan.github.io/jq/), and certificate output is truncated, to make the output more readable.

### [](#create-a-fully-secure-reference-using-credentials)Create a Fully Secure Reference, Using Credentials

This example creates a fully secure reference from `localhost` to `10.144.220.102`. It uses a username and password plus the target cluster's root certificate to authenticate.

```console
curl -X POST -u Administrator:password \
http://localhost:8091/pools/default/remoteClusters \
-d name=TargetCluster \
-d hostname=10.144.220.102 \
-d username=targetAdministrator \
-d password=targetPassword \
-d secureType=full \
--data-urlencode "certificate=$(cat ./ca.pem)" | jq '.'
```

This example sets a `username` and `password` for an account on the target cluster. It does not set the `demandEncryption`. However, because it sets the `encryptionType` parameter to `full`, the reference uses full encryption. Using `` curl’s `--data-urlencode `` flag encodes the contents of the root certificate for the target cluster returned by the `cat` command.

Formatted, the output from a successful execution is:

```json
{
  "certificate": "-----BEGIN CERTIFICATE-----\nMIIDJzCC
          .
          .
          .
  FHjm+ycdHyRyk5iAooXWXP5xnaBE9+Vig==\n-----END CERTIFICATE-----",
  "deleted": false,
  "demandEncryption": true,
  "encryptionType": "full",
  "hostname": "10.144.220.102:8091",
  "name": "TargetCluster",
  "secureType": "full",
  "uri": "/pools/default/remoteClusters/TargetCluster",
  "username": "targetAdministrator",
  "uuid": "1ed664057cbaad1e283fe0e6dfa86506",
  "validateURI": "/pools/default/remoteClusters/TargetCluster?just_validate=1"
}
```

### [](#create-a-half-secure-reference-using-credentials)Create a Half-Secure Reference, Using Credentials

The following example creates a half-secure reference from `localhost` to `10.142.180.102`. It uses a username and password to authenticate with the target cluster.

```console
curl -X POST -u Administrator:password \
http://localhost:8091/pools/default/remoteClusters \
-d name=TargetCluster \
-d hostname=10.144.220.102 \
-d username=targetAdministrator -d password=targetPassword \
-d demandEncryption=1 \
-d secureType=half \
--data-urlencode "certificate=$(cat ./ca.pem)" | jq '.'
```

The `username` and `password` in the example are for an account on the remote cluster. The reference is half-encrypted (only the password is encrypted) because the `demandEncryption` flag is `1` and the `encryptionType` flag is `half`. Using `` curl’s `--data-urlencode `` flag encodes the contents of the root certificate for the target cluster returned by the `cat` command.

If the source Couchbase Server connects to the target cluster, it returns the following message:

```json
{
  "certificate": "-----BEGIN CERTIFICATE-----\nMIIDJzCCAg+gAwIBAgIUSaVkKhAwNl8aTxDkfyoeUiStp1cw/
          .
          .
          .
  FHjm+ycdHyRyk5iAooXWXP5xnaBE9+Vig==\n-----END CERTIFICATE-----",
  "deleted": false,
  "demandEncryption": true,
  "encryptionType": "half",
  "hostname": "10.144.220.102:8091",
  "name": "TargetCluster",
  "secureType": "half",
  "uri": "/pools/default/remoteClusters/TargetCluster",
  "username": "targetAdministrator",
  "uuid": "1ed664057cbaad1e283fe0e6dfa86506",
  "validateURI": "/pools/default/remoteClusters/TargetCluster?just_validate=1"
}
```

### [](#create-a-fully-secure-reference-using-certificates)Create a Fully Secure Reference, Using Certificates

This example create a fully secure reference from `localhost` to `target.example.com` by doing the following:

* Specifies that connection is over an external network
* Enables full encryption
* Authenticates using the remote cluster's root certificate, a client certificate, and a client private key.

```console
curl -X POST -u Administrator:password http://localhost:8091/pools/default/remoteClusters \
-d name=TargetCluster \
-d hostname=target.example.com \
-d network_type=external \
-d demandEncryption=1 \
--data-urlencode "certificate=$(cat ./ca.pem)" \
--data-urlencode "clientCertificate=$(cat ./travel-sample.pem)" \
--data-urlencode "clientKey=$(cat ./travel-sample.key)"
```

Because the example sets the `demandEncryption` flag to `1` and does not supply a `secureType` parameter, the connection to the target cluster is fully encrypted. The `network_type=external` parameter indicates that Couchbase Server should connect to the target's external network if it has been configured. If the target cluster does not have an external network defined, the source cluster attempts to connect to the target cluster's internal network. The example supplies three URL-encoded values: the root certificate of the target cluster and a certificate and key for the client connection.

If successful, the command returns the following:

```json
{
  "certificate": "-----BEGIN CERTIFICATE-----\nMIIDJzCCAg+gAwIBAgIUSaVkKh
          .
          .
          .
  /FHjm+ycdHyRyk5iAooXWXP5xnaBE9+Vig==\n-----END CERTIFICATE-----",
  "clientCertificate": "-----BEGIN CERTIFICATE-----\nMIIDljCCAn6gAwIBAgI
          .
          .
          .
  cqHOcGj7RJE5SIwVZUPnSPeGHgLTTmijJhe15VFdA==\n-----END CERTIFICATE-----",
  "deleted": false,
  "demandEncryption": true,
  "encryptionType": "full",
  "hostname": "target.example.com",
  "name": "TargetCluster",
  "secureType": "full",
  "uri": "/pools/default/remoteClusters/TargetCluster",
  "username": "",
  "uuid": "1ed664057cbaad1e283fe0e6dfa86506",
  "validateURI": "/pools/default/remoteClusters/TargetCluster?just_validate=1"
}
```

The `secureType` field specifies `full` which is the default value if you set `demandEncryption` to `1` and do not supply a `secureType` parameter in the REST API call. The output includes both the target cluster's root certificate and the source cluster's client certificate.

## [](#see-also)See Also

* See [Enable Fully Secure Replications](../manage/manage-xdcr/enable-full-secure-replication.md) for an overview of securing replications.
* See [Secure a Replication](../manage/manage-xdcr/secure-xdcr-replication.md)for information about using the REST API to create secure connections.
* See [Certificates](../learn/security/certificates.md) for an overview of using certificates with Couchbase Server.
* See [XDCR Security and Networking](../xdcr-reference/xdcr-security-and-networking.md) for some requirements when configuring XDCR.