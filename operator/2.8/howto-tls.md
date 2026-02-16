[View original HTML](/operator/2.8/howto-tls.html)

> How to configure Couchbase Server with basic TLS. 

By default a Couchbase Server deployment uses basic authentication, commonly known as username and password. Basic authentication may be used over a plain text network communication where a malicious party can see the password. Basic authentication may also be used over a server-side TLS protected network connection which encrypts the password and prevents a malicious party from acquiring it.

## [](#creating-secrets)Creating Secrets

Secrets are specified in the `CouchbaseCluster` resource, therefore they may have any name you choose. The format of individual secrets is discussed below.

See the [TLS certificate tutorial](tutorial-tls.md) for a simple guide to creating TLS certificates.

### [](#ca-secrets)CA Secrets

All CA secrets must contain the `tls.crt` field (as per the `kubernetes.io/tls` spec) and are used to form a trust pool. All other provided certificates must be signed by a certificate in the trust pool.

```console
$ kubectl create secret tls couchbase-server-ca \
  --cert example/pki/ca.crt \
  --key example/pki/private/ca.key
```

|  | When using Couchbase 7.0 and earlier, only one CA is supported, therefore all server and client certificates must be signed by the same root CA. Specifying multiple CA certificates with Couchbase Server 7.0 and earlier will result in undefined behavior. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#server-secret)Server Secret

The Server secrets needs to be provided in the `kubernetes.io/tls` format.

```console
$ kubectl create secret tls couchbase-server-tls \
  --cert example/pki/issued/couchbase-server.crt \
  --key example/pki/private/couchbase-server.key
```

## [](#couchbase-cluster-configuration)Couchbase Cluster Configuration

The following configuration will enable managed TLS.

```yaml
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
spec:
  networking:
    tls:
      rootCAs:
      - couchbase-server-ca
      - couchbase-server-ca2 (1)
      secretSource:
        serverSecretName: couchbase-server-tls
```

| **1** | [couchbaseclusters.spec.networking.tls.rootCAs](resource/couchbasecluster.md#couchbaseclusters-spec-networking-tls-rootcas)additional root CAs are added here. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#pkcs12-support)PKCS12 Support

As of 2.7.0 and with server version 7.6.0+, Couchbase Operator now supports PKCS12 formatted server certs. This must be accompanied in a secret with the password to extract the .p12 file. The secret must be formatted as such:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: tls-secret
data:
  couchbase-server.p12: MIIPEAIBAzCCDsYGCSqGSIb3DQEHAaCCDrcEgg...
  tls-password: cGFzc3dvcmQ= (1)
```

| **1** | Password should be in base64 format |
| ----- | ----------------------------------- |

The key in the file and the cert must be in PKCS#8 format and must be unencrypted. The key file must not be password protected.