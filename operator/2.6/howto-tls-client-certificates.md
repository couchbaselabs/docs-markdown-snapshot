---
title: Configure Client Certificate Authentication
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/howto-tls-client-certificates.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.6@operator::howto-tls-client-certificates.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/howto-tls-client-certificates.html)

# Configure Client Certificate Authentication

> How to configure Couchbase Server and the Operator to use client certificate based authentication. 

By default a Couchbase Server deployment uses basic authentication, commonly known as username and password. Basic authentication may be used over a plain text network communication where a malicious party can see the password. Basic authentication may also be used over a server-side TLS protected network connection which encrypts the password and prevents a malicious party from acquiring it.

Couchbase Server also supports a mode of authentication using client certificates. It uses the same technology that a client uses to assert the validity of a server certificate, but the server validates the client as well. This is known as mutual TLS (mTLS). Couchbase server does not support basic authentication over mTLS, instead requiring a username to be encoded into the client certificate. This page documents configuration of mTLS.

## [](#creating-secrets)Creating Secrets

Secrets are specified in the `CouchbaseCluster` resource, therefore they may have any name you choose. The format of individual secrets is discussed below.

Please see the [TLS certificate tutorial](tutorial-tls.md) for a simple guide to creating TLS certificates.

### [](#server-secret)Server Secret

Server secrets need to be mounted as a volume within the Couchbase Server pod with specific names. The certificate chain must be named `tls.crt` and the private key `tls.key`.

```console
$ kubectl create secret generic couchbase-server-tls \
  --from-file example/tls/certs/tls.crt \
  --from-file example/tls/certs/tls.key \
  --from-file example/tls/certs/ca.crt
```

### [](#operator-secret)Operator Secret

The Operator client secrets are read directly from the API. It expects only a single value to be present; `ca.crt` is the top-level CA which is used to authenticate all TLS server certificate chains. When using client certificate authentication you will also need to specify the client certificate chain and key pair with the keys `tls.crt` and `tls.key` respectively:

```console
$ kubectl create secret generic couchbase-operator-tls \
  --from-file example/tls/certs/tls.crt \
  --from-file example/tls/certs/tls.key
```

## [](#couchbase-cluster-configuration)Couchbase Cluster Configuration

TLS certificate configuration is done in the networking section of the `CouchbaseCluster` resource.

```yaml
apiVersion: couchbase/v2
kind: CouchbaseCluster
spec:
  security:
    adminSecret: my-admin-secret
  networking:
    tls:
      secretSource:
        serverSecretName: couchbase-server-tls (1)
        clientSecretName: couchbase-operator-tls (2)
      clientCertificatePolicy: mandatory (3)
      clientCertificatePaths: (4)
      - path: subject.cn
      - path: san.email
        delimiter: @
```

| **1** | [couchbaseclusters.spec.networking.tls.secretSource.serverSecretName](resource/couchbasecluster.md#couchbaseclusters-spec-networking-tls-secretsource-serversecretname) defines a secret that will be mounted to all Couchbase Server pods. It contains the server wildcard certificate and it’s private key. As the private key is securely mounted to the pod by Kubernetes it is never exposed over the network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | [couchbaseclusters.spec.networking.tls.secretSource.clientSecretName](resource/couchbasecluster.md#couchbaseclusters-spec-networking-tls-secretsource-clientsecretname) defines a secret containing client related certificates. The client certificate contains a subject common name e.g. Administrator. The administrator user Administrator is configured by the [couchbaseclusters.spec.security.adminSecret](resource/couchbasecluster.md#couchbaseclusters-spec-security-adminsecret).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **3** | [couchbaseclusters.spec.networking.tls.clientCertificatePolicy](resource/couchbasecluster.md#couchbaseclusters-spec-networking-tls-clientcertificatepolicy) is set to mandatory meaning all clients will need to provide a valid client certificate in order to authenticate against the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **4** | [couchbaseclusters.spec.networking.tls.clientCertificatePaths](resource/couchbasecluster.md#couchbaseclusters-spec-networking-tls-clientcertificatepaths) defines a path that is able to correctly parse and extract the Operator’s Administrator use from the client certificate. In this example all we need to specify is that the user name is explicitly encoded in the certificate’s subject common name. This covers the base requirements in order for the Operator to be able to connect to the cluster. In a more realistic setup users will likely be identified by an email address. In this illustration it is encoded in a subject alternative name (SAN). When Couchbase Server looks at a client certificate it will not find a valid user using the first path (but it would match for our Administrator user). It then proceeds down the list of paths in order trying to extract a valid username. If the client certificate contained a SAN EMAIL:jane.doe@example.com, then it would resolve to jane.doe with our second path rule. If jane.doe matched a local or LDAP user then they would be granted permission to access the Couchbase Server instance. |