---
title: Configure TLS
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.5/modules/ROOT/pages/howto-tls.adoc
  xref: xref:2.5@operator::howto-tls.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/howto-tls.html)

# Configure TLS

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

> [!WARNING]
> When using Couchbase 7.0 and earlier, only one CA is supported, therefore all server and client certificates must be signed by the same root CA. Specifying multiple CA certificates with Couchbase Server 7.0 and earlier will result in undefined behavior.

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