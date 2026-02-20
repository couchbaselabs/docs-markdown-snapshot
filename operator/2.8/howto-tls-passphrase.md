---
title: Configure TLS Passphrase Protection
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.8/modules/ROOT/pages/howto-tls-passphrase.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.8@operator::howto-tls-passphrase.adoc[]
---

[View original HTML](/operator/2.8/howto-tls-passphrase.html)

# Configure TLS Passphrase Protection

> How to configure Couchbase Server with passphrase protected private keys. 

Couchbase Server 7.1 introduces support for passphrase protected private keys. Passphrase protected private keys build upon the basics of [Couchbase Server TLS](howto-tls.md) by also encrypting the private key used to decrypt the username and password. Therefore, if a malicious party succeeds in acquiring the private key, passphrase protection provides an additional layer of security against impersonation since the compromised key cannot be immediately used to decode network traffic.

## [](#creating-secrets)Creating Secrets

Passphrase protected keys are configured with Couchbase Server using Kubernetes Secrets. Refer to the [Passphrase Protected Keys Tutorial](tutorial-tls.md#passphrase-protected-keys) for documentation on creating passphrase protected keys with `openssl`. Once the certificate and key is created, the Secret can be created with the `tls.crt` and `tls.key` fields (as per the `kubernetes.io/tls` spec):

```bash
kubectl create secret generic \  (1)
  couchbase-server-tls  --from-file tls.crt --from-file  tls.key
```

| **1** | Only the generic secret type allows passphrase protected data. |
| ----- | -------------------------------------------------------------- |

> [!NOTE]
> Encrypted keys cannot actually be `kubernetes.io/tls` type because Kubernetes is not aware of the passphrase in order to validate the key pair.

Refer to [TLS Secret Create](howto-tls.md#creating-secrets) documentation to set up the remaining TLS Secrets for Couchbase Cluster.

## [](#passphrase-registration)Passphrase registration

The Kubernetes Operator is capable of registering a local script or a rest endpoint to generate the secret passphrase used by a private key. Passphrase TLS can be enabled from a non-TLS cluster or from a cluster with plain TLS keys. When enabling passphrase TLS on a Cluster that is already provisioned, the Couchbase Cluster will enter a rolling upgrade of the Server Pods.

> [!NOTE]
> Only one type of passphrase registration can be used at once, however it is possible to toggle between script or rest passphrase registration while the Couchbase Cluster is active.

### [](#script-passphrase)Script passphrase

The `CouchbaseCluster` resource has a `passphrase` section for configuring the type of tool to use when generating the passphrase. Passphrase script registration simply requires a Kubernetes Secret which contains the passphrase:

```yaml
networking:
   tls:
      passphrase:
        script:
          secret:  passphrase-secret (1)
```

| **1** | A Generic Kubernetes Secret with a key named passphrase. The value for the passphrase is the string to be used by Couchbase Server when decoding its private key. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The following is an example of a Kubernetes secret which provides a passphrase:

```yaml
apiVersion: v1
kind: Secret
type: Opaque
data:
  passphrase: cGFzc3dvcmQ= (1)
metadata:
  name: passphrase-secret
```

| **1** | The value "password" represented as a base64 encoded value |
| ----- | ---------------------------------------------------------- |

When using a script to register the passphrase, the Operator internally creates a passphrase script and mounts it into each of the Couchbase Server Pods. This script provisioning is abstracted away for ease of use and security. See [TLS Concept Documentation](concept-tls.md#tls-passphrase-protection) for more in-depth information about how passphrase script registration works within the Operator.

> [!NOTE]
> The passphrase can be changed at any time. When changing the passphrase be sure to also rotate the Couchbase Server private key to match the update passphrase. See [Replacing Server Certificates](howto-tls-rotation.md#replacing-server-certificates) for documentation related to TLS certificate rotation.

### [](#rest-passphrase)Rest passphrase

The private key passphrase may also be registered by providing an HTTP(s) rest URL to Couchbase Server. The URL is expected to accessible by the Couchbase Server Pods, and to return the passphrase string. Rest passphrase registration can be enabled with the following configuration:

```yaml
networking:
   tls:
      passphrase:
        rest:
          url: https://app.default.svc (1)
          timeout: 5000
          verifyPeer: True  (2)
          headers: {} (3)
```

| **1** | Couchbase Server will call this rest URL to fetch the private key passphrase. The Operator does not provide any sort of rest endpoint for internal use, therefore the service must be 3rd party hosted by the user. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Secure HTTPS is highly recommended and by default TLS peer verification is enabled.                                                                                                                                 |
| **3** | Optional HTTP headers to include in the rest request.                                                                                                                                                               |

> [!NOTE]
> Couchbase Server doesn’t trim the response from the rest URL, therefore white-space and newline characters must be avoided by the webserver providing the passphrase.

> [!WARNING]
> Couchbase Server is currently unable to perform mutual TLS between itself and the provided rest endpoint. Without Mutual TLS, the rest server is unable to verify if a client is allowed to request the passphrase. Given this limitation, caution should be taken when configuring a rest point to prevent unauthorized requests. See [Securing TLS Rest Endpoints](concept-tls.md#securing-rest-endpoints) documentation for a general guide to securing rest endpoints.