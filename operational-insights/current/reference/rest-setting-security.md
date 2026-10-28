---
title: Configure On-the-Wire Security
description: Establish and retrieve cluster-wide settings for the use of
  encryption and cipher-suites.
pubDate: 2026-10-28T04:21:06.350Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-setting-security.adoc
  xref: xref:enterprise-analytics:reference:rest-setting-security.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-setting-security.html)

# Configure On-the-Wire Security

> Establish and retrieve cluster-wide settings for the use of encryption and cipher-suites. 

## [](#http-method-and-uri)HTTP Method and URI

GET /settings/security/[service-name]

POST /settings/security/[service-name]

## [](#description)Description

Allows settings to be established for the use of encryption. This includes the encryption _level_, for node-to-node encryption within the cluster; UI disablement over insecure connections; TLS minimum version; and a list of accepted cipher suites. Additionally, secure communication by means of TLS can be _enforced_ across the cluster.

The caller must have the Full Admin or Security Admin role to change settings.

Note that information on setting an HTTP Secure Transport Header with the REST API is provided in [Configure HSTS](rest-setting-hsts.md).

## [](#curl-syntax)Curl Syntax

curl -X GET -u <username>:<password>
  http://<ip-address-or-domain-name>:8091/settings/security/[service-name]

curl -X POST -u <username>:<password>
  http://<ip-address-or-domain-name>:8091/settings/security/[service-name]
  -d disableUIOverHttp=<true|false>
  -d disableUIOverHttps=<true|false>
  -d disableWWWAuthenticate=<true|false>
  -d responseHeaders=<list-of-response-headers>
  -d allowedHosts=<list-of-naming-conventions>
  -d allowNonLocalCACertUpload=<true|false>
  -d clusterEncryptionLevel=<all|control|strict>
  -d tlsMinVersion=<tlsv1.2|tlsv1.3>
  -d honorCipherOrder=<true|false>
  -d cipherSuites=<list-of-accepted-cipher-suites>
  -d [scramSha1Enabled|scramSha256Enabled|scramSha512Enabled]=<true|false>
  -d passwordHashAlg=<argon2id|pbkdf2-hmac-sha512|SHA-1>
  -d argon2idTime=<integer>
  -d argon2idMem=<integer>
  -d pbkdf2HmacSha512Iterations=<integer>
  -d scramShaIterations=<integer>
  -d intCredsRotationInterval=<integer>
  -d validateNodeCertSan=<true|false>
  -d allowHashMigrationDuringAuth=<true|false>

The syntax for the `GET` and `POST` methods includes the following:

* `service-name`. If provided, determines the service to which settings are either written with `POST`, or read with `GET`. The value of `service-name` can be any one of the following: `clusterManager` (Cluster Manager), `data`, `analytics` (Analytics Service). On Operational Insights, the `data` ports are used only for cluster-topology connectivity by [connectors based on legacy SDKs](../manage/manage-nodes/cluster-connectivity-topology-management.md#legacy-sdks), such as the Tableau, Power BI, and Apache Superset connectors; the `data` settings apply to the TLS connections on these ports. If no `service-name` is provided, _global_ settings are written or read.  
When a `service-name` is provided, only `tlsMinVersion`, `honorCipherOrder`, and `cipherSuites` can be specified. A setting made for a service overrides the corresponding global setting, for that service only.
* `disableUIOverHttp`. Whether access to Operational Insights Web Console should be disabled over http. Default is `false`, meaning that the console can be accessed over http. This parameter can only be set globally.
* `disableUIOverHttps`. Whether access to Operational Insights Web Console should be disabled over https. Default is `false`, meaning that the console can be accessed over https. This parameter can only be set globally.
* `disableWWWAuthenticate`. Whether to disable Operational Insights responding to unauthenticated requests with _WWW-Authenticate_. Default is `false`, meaning that Operational Insights responds to unauthenticated requests with _WWW-Authenticate_. This parameter can only be set globally.
* `responseHeaders`. A list of response headers. Only the `Strict-Transport-Security` header is supported: see [Configure HSTS](rest-setting-hsts.md). This parameter can only be set globally.
* `allowedHosts`. Specifies a list of naming conventions that must be met by the name of any node that is to be added or joined to the cluster. This parameter is described separately, in [Restrict Node-Addition](rest-specify-node-addition-conventions.md). This parameter can only be set globally, and only from `localhost`.
* `allowNonLocalCACertUpload`. Whether the deprecated `POST` method and `/controller/uploadClusterCA` URI can be used to upload CA certificates from a node other than localhost. Value can be `true` or `false` (the default). For information, see [Upload and Retrieve the Root Certificate](deprecated-security-apis/upload-retrieve-root-cert.md). This parameter can only be set globally, and only from `localhost`.
* `clusterEncryptionLevel`. Controls the level of encryption imposed on cluster-communications. This can only be set after cluster encryption has been enabled (see [Manage Node-to-Node Encryption](../manage/manage-nodes/apply-node-to-node-encryption.md)) and can only be set globally. Its value can be any of the following:

  * `control`, meaning that server-management information passed between nodes is passed in encrypted form.
  * `all`, meaning that all information passed between nodes, including data handled by services, is passed in encrypted form.
  * `strict`, meaning `all` with only encrypted communication permitted between nodes and between the cluster and external clients. Note that after `strict` has been specified, communication that occurs entirely on a single node using the _loopback_ interface (whereby the machine is identified as either `::1` or `127.0.0.1`) is still permitted in non-encrypted form.  
  Before applying `strict`, see [Enforcing TLS](#enforcing-tls), below.
* `tlsMinVersion`. Specifies the minimum TLS version accepted by the cluster. Can be the default `tlsv1.2` or `tlsv1.3`. It can be set either globally or per service.
* `honorCipherOrder`. Specifies whether the server uses its own cipher-suite preference, rather than the client's. The cluster's list of accepted cipher-suites can be defined with the `cipherSuites` flag (see below). The default value of `honorCipherOrder` is `true`: a setting of `false` is _not_ recommended, since insecure. This parameter can be set either globally, or per service.
* `cipherSuites`. Specifies a list of the cipher suites to be used, in order of preference. The argument must be a list of cipher-suites.  
This parameter can be set either globally, or per service. If the parameter is set for a given service, each listed cipher-suite must appear as a member of the array that is the value of the non-configurable **supportedCipherSuites** setting for the service. If the parameter is set globally, each listed cipher-suite can be used by a given service only if it appears as a member of **supportedCipherSuites** for that service.
* `scramSha1Enabled`, `scramSha256Enabled`, or `scramSha512Enabled`. Whether the specified SCRAM-SHA password-authentication mechanism is enabled or disabled. Value can be `true` (the default, meaning _enabled_) or `false` (meaning _disabled_). This setting is established _globally_, and must not specify the `service-name`.
* `passwordHashAlg`. Which hash function to use for hashing the passwords of locally defined users. The options are `argon2id` (the default), `pbkdf2-hmac-sha512`, and `SHA-1` (which is deprecated). Changing this setting does not affect existing passwords. Only new or changed passwords use the new hashing algorithm. See [allowHashMigrationDuringAuth](#migrate-password-hash) for a way to migrate passwords to the new hashing algorithm.  
> [!IMPORTANT]  
> By design, the Argon2id hashing algorithm consumes more CPU and memory than the prior default SHA-1 hashing algorithm. If your server handles a high volume of authentications, using the Argon2id hashing algorithm can result in higher CPU and memory use.
* `argon2idTime`, `argon2idMem`. Time and memory parameters for `argon2id`. Used only if `argon2id` is specified as the value of `passwordHashAlg`.
* `pbkdf2HmacSha512Iterations`. Iterations parameter of `pbkdf2-hmac-sha512`, used only if `pbkdf2-hmac-sha512` is specified as the value of `passwordHashAlg`. Specified as a number of iterations. Default is `10000`.
* `scramShaIterations`. Sets the number of iterations for all `scram-sha` hashes (`scram-sha1`, `scram-sha256`, and `scram-sha512`), if they are not disabled. Specified as a number of iterations. Default is `15000`.
* `intCredsRotationInterval`. Interval at which Operational Insights rotates internal credentials globally. Specified in milliseconds. Default is `1800000` (30 minutes). A value of `0` disables automatic rotation. To rotate internal credentials immediately, see [Rotate Internal Credentials](rest-rotate-internal-credentials.md).
* `validateNodeCertSan`. Whether Operational Insights checks that the node's hostname matches the _Subject Alternative Name_ (SAN) in that node's certificate. Value can be `true` (which is the default) or `false`. A mismatch triggers an error in the following scenarios:

  * When the certificate is uploaded to the node
  * When the node's `hostname` changes during node-addition, or during cluster-initialization.
  * When the node's `hostname` changes due to use of an API or CLI (for example, the [node-init](../cli/couchbase-cli-node-init.md) command).  
These checks are performed to ensure that each node bears a certificate whose SAN matches the node's hostname, thereby ensuring that other nodes will be able to verify the node's identity when connecting with it.

* `allowHashMigrationDuringAuth` controls whether Operational Insights automatically rehashes a locally-stored password if it was hashed using an algorithm other than the one set by `passwordHashAlg`. If you set this value to `true`, the user's password is automatically rehashed using the new algorithm after authentication. See [Authentication](../manage/manage-security/manage-authentication.md) for more information.

For an explanation of the relationships between per service and global settings, see [On-the-Wire Security Settings](../manage/manage-security/manage-tls.md#security-settings).

### [](#enforcing-tls)Enforcing TLS

Before applying the `strict` value to the `clusterEncryptionLevel` parameter:

* Ensure all client applications and scripts are able to connect with TLS.
* Ensure node-to-node encryption is enabled (see [Manage Node-to-Node Encryption](../manage/manage-nodes/apply-node-to-node-encryption.md)).

## [](#responses)Responses

The `GET` method, if successful, gives `200 OK`, and returns an object containing each configured parameter, with its current value. The `POST` method, if successful, gives `200 OK`, and returns an empty array.

For both methods, an incorrect URI gives `404 Object Not Found`, with a `Not found` error message. Use of improper credentials gives `401 Unauthorized`. An improper port number returns an error message such as `Failed to connect`, or `Port number out of range`.

For the `POST` method, incorrectly specified parameters fail with `400 Bad Request`, and return an `errors` object that lists the errors in an array. For example, a call that incorrectly specifies every significant parameter-value returns an object such as the following:

{
  "errors": [
    "honorCipherOrder - Accepted values are 'true' and 'false'.",
    "cipherSuites - Invalid format. Expecting a list of ciphers.",
    "tlsMinVersion - Supported TLS versions are tlsv1.2, tlsv1.3",
    "clusterEncryptionLevel - Cluster encryption level must be one of [\"control\",\"all\",\"strict\"]",
    "disableUIOverHttps - Accepted values are 'true' and 'false'.",
    "disableUIOverHttp - Accepted values are 'true' and 'false'.",
    "disableWWWAuthenticate - Accepted values are 'true' and 'false'."
  ]
}

Note additionally that an attempt to establish a value for `clusterEncryptionLevel` prior to the enablement of node-to-node encryption returns the following error-message: `clusterEncryptionLevel - Can’t set cluster encryption level when cluster encryption is disabled.`See [Manage Node-to-Node Encryption](../manage/manage-nodes/apply-node-to-node-encryption.md), for details on how to enable.

## [](#examples)Examples

The methods and the URI can be used as shown below.

### [](#establish-on-the-wire-settings-globally)Establish On-the-Wire Settings, Globally

The following establishes a subset of on-the-wire settings globally:

curl  -u Administrator:password -v -X POST \
http://10.144.210.101:8091/settings/security \
-d disableUIOverHttp=true \
-d clusterEncryptionLevel=control \
-d tlsMinVersion=tlsv1.2 \
-d 'cipherSuites=["TLS_RSA_WITH_AES_128_CBC_SHA", "TLS_RSA_WITH_AES_256_CBC_SHA"]'

The `disableUIOverHttp` flag is given a value of `true`, indicating that access to Operational Insights Web Console will be disabled over http. The `disableUIOverHttps` flag is _not_ specified, meaning that access to Operational Insights Web Console will _not_ be disabled over https, by default. The `clusterEncryptionLevel` is specified as `control`, indicating that only server-management information is passed in encrypted form between cluster-nodes: note that this parameter can only be set after the `node-to-node-encryption` CLI command has been used to enable internal network-security for the cluster, as described in [Manage Node-to-Node Encryption](../manage/manage-nodes/apply-node-to-node-encryption.md). The `tlsMinVersion` is specified as version 1.2\. The `honorCipherOrder` parameter is _not_ specified, meaning that it retains its default value of `true`; which ensures that the cluster's own cipher-suites preference is used, rather than the client's. The `cipherSuites` parameter is assigned a value that is a list of two cipher suites.

If successful, the call returns an empty array:

[]

### [](#retrieve-cluster-wide-settings)Retrieve Cluster-Wide Settings

The `GET /settings/security` method and URI retrieve cluster-wide settings for on-the-wire security, as shown below. Note that the output is piped to the [jq](https://stedolan.github.io/jq/) program, to enhance readability:

curl  -u Administrator:password -v -GET \
http://10.144.210.101:8091/settings/security | jq '.'

If the call is successful, and some explicit settings have been made by the administrator, the output might appear as follows:

{
  "disableUIOverHttp": false,
  "disableUIOverHttps": false,
  "disableWWWAuthenticate": false,
  "responseHeaders": [],
  "tlsMinVersion": "tlsv1.2",
  "cipherSuites": [
    "TLS_RSA_WITH_AES_128_CBC_SHA",
    "TLS_RSA_WITH_AES_256_CBC_SHA"
  ],
  "honorCipherOrder": true,
  "allowNonLocalCACertUpload": false,
  "allowedHosts": [
    "*.test.ubuntu",
    "127.0.0.1"
  ],
  "data": {
    "cipherSuites": [
      "TLS_RSA_WITH_AES_128_CBC_SHA",
      "TLS_RSA_WITH_AES_256_CBC_SHA",
      "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"
    ],
    "tlsMinVersion": "tlsv1.2",
    "honorCipherOrder": true,
    "supportedCipherSuites": [
      "TLS_AES_256_GCM_SHA384",
      "TLS_CHACHA20_POLY1305_SHA256",
      "TLS_AES_128_GCM_SHA256",
      "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
              .
              .
              .

The global values of `disableUIOverHttp`, `disableUIOverHttps`, `tlsMinVersion`, and `honorCipherOrder` are thus displayed. Note also that a global value for `cipherSuites` has also been established.

The return object contains, in addition to global settings, a subdocument for each service. The truncated output shown here features values from the `data` subdocument; which is shown to have its own values established for `cipherSuites`, `tlsMinVersion`, and `honorCipherOrder`. The read-only value for `supportedCipherSuites` for the service is also displayed. The response also contains subdocuments for services that do not run on Operational Insights; only the `clusterManager`, `data`, and `analytics` subdocuments apply.

### [](#establish-per-service-settings)Establish Per Service On-the-Wire Settings

The following call establishes settings for `tlsMinVersion` and `cipherSuites`, for `data` only:

curl  -u Administrator:password -v -X POST \
http://10.144.210.101:8091/settings/security/data \
-d tlsMinVersion=tlsv1.3 \
-d 'cipherSuites=["TLS_RSA_WITH_AES_128_CBC_SHA","TLS_RSA_WITH_AES_256_CBC_SHA","TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"]'

Note that the `data` path-parameter has been added to the URI, as the value of `service-name`, in order to specify the `data` settings. To configure the Analytics Service or the Cluster Manager instead, use `analytics` or `clusterManager`. If the call is successful, an empty array is returned.

To verify the new `data` settings, use the `GET` method, again adding `data` to the URI:

curl  -u Administrator:password -v -X GET \
http://10.144.210.101:8091/settings/security/data | jq '.'

The returned output shows that the new settings have been successfully established:

{
  "cipherSuites": [
    "TLS_RSA_WITH_AES_128_CBC_SHA",
    "TLS_RSA_WITH_AES_256_CBC_SHA",
    "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"
  ],
  "tlsMinVersion": "tlsv1.3",
  "honorCipherOrder": true,
  "supportedCipherSuites": [
    "TLS_AES_256_GCM_SHA384",
    "TLS_CHACHA20_POLY1305_SHA256",
              .
              .
              .

## [](#see-also)See Also

For more information on managing on-the-wire security-settings with the CLI, see the reference page for the [setting-security](../cli/couchbase-cli-setting-security.md) command.

Information on setting an HTTP Secure Transport Header with the REST API is provided in [Configure HSTS](rest-setting-hsts.md).

For an overview of on-the-wire security, see [Manage On-the-Wire Security](../manage/manage-security/manage-tls.md).