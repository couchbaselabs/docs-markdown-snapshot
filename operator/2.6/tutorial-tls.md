---
title: Creating TLS Certificates
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/tutorial-tls.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.6@operator::tutorial-tls.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/tutorial-tls.html)

# Creating TLS Certificates

> This section shows a simple way to create and manage a TLS certificate hierarchy. 

> [!WARNING]
> Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer.

Creating X.509 certificates is beyond the scope of this documentation and is given only for illustrative purposes only. Please consult the [Couchbase Server documentation^](../../server/current/learn/security/certificates.md) for additional details on certificate and TLS configuration.

## [](#easyrsa)EasyRSA

EasyRSA by OpenVPN makes operating a public key infrastructure (PKI) relatively simple, and is the recommended method to get up and running quickly.

First clone the repository:

```console
$ git clone https://github.com/OpenVPN/easy-rsa
```

Initialize and create the CA certificate/key. You will be prompted for a private key password and the CA common name (CN), something like _Couchbase CA_ is sufficient. The CA certificate will be available as `pki/ca.crt`.

```console
$ cd easy-rsa/easyrsa3
```

```console
$ ./easyrsa init-pki
```

```console
$ ./easyrsa build-ca
```

## [](#creating-a-couchbase-cluster-server-certificate)Creating a Couchbase Cluster Server Certificate

You need to create a server wildcard certificate and key to be used on Couchbase Server pods. The Operator will access pods using Kubernetes endpoint records, e.g. `https://cb-example-0000.cb-example.default.svc`. Clients will access the cluster using Kubernetes service discovery records, e.g. `couchbases://cb-example.default`. UI access will be with port-forwarding using `localhost`.

The following list contains the required set of DNS subject alternative names (SANs) that you will need to include in the Couchbase cluster certificate. The Operator dynamic admission controller enforces the presence of all of these SANs.

Required SANs

```console
DNS:*.<cluster>
DNS:*.<cluster>.<namespace>
DNS:*.<cluster>.<namespace>.svc
DNS:*.<cluster>.<namespace>.svc.cluster.local
DNS:<cluster>-srv
DNS:<cluster>-srv.<namespace>
DNS:<cluster>-srv.<namespace>.svc
DNS:*.<cluster>-srv.<namespace>.svc.cluster.local
DNS:localhost
#DNS:*.<couchbaseclusters.spec.networking.dns.domain> (1)
```

| **1** | If you plan to configure [public networking](tutorial-public-addressability.md) for the cluster, then you must add the wildcard SAN DNS:\*._<[couchbaseclusters.spec.networking.dns.domain](resource/couchbasecluster.md#couchbaseclusters-spec-networking-dns-domain)\>_ to handle all of the public DNS names for the cluster. This will commonly be a subdomain of your public DNS domain, e.g. \*.subdomain.dns-domain.com. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

> [!NOTE]
> Search Domains
> 
> SANs depend on search domains being configured for your stub resolver. By default, Kubernetes will do this for you. However, if you use the [inter-Kubernetes networking with forwarded DNS](concept-couchbase-networking.md#inter-kubernetes-networking-with-forwarded-dns) networking model for connecting your clients, then you will need to configure this yourself.
> 
> For example, the FQDN for a Couchbase pod would be similar to `cb-0000.cb.default.svc.cluster.local`, however a client will communicate with `cb-0000.cb.default.svc`. In order for a client to match the `*.cb.default.svc` SAN, and resolve the pod address, a search domain would need to be configured for `cluster.local`. Likewise, if your clients used the short form hostname `cb-0000.cb`, a search domain would need to configured for `default.svc.cluster.local`.

To generate a certificate for the cluster `cb-example` in the `default` namespace:

```console
$ ./easyrsa --subject-alt-name='DNS:*.cb-example,DNS:*.cb-example.default,DNS:*.cb-example.default.svc,DNS:*.cb-example.default.svc.cluster.local,DNS:cb-example-srv,DNS:cb-example-srv.default,DNS:cb-example-srv.default.svc,DNS:*.cb-example-srv.default.svc.cluster.local,DNS:localhost' build-server-full couchbase-server nopass
```

The key/certificate pair can be found in `pki/private/couchbase-server.key` and `pki/issued/couchbase-server.crt` and used as `tls.key` and `tls.crt`, respectively, in the [couchbaseclusters.spec.networking.tls.secretSource.serverSecretName](resource/couchbasecluster.md#couchbaseclusters-spec-networking-tls-secretsource-serversecretname) parameter.

### [](#passphrase-protected-keys)Passphrase Protected Keys

The use of passphrase protected keys require Server 7.1\. Passphrase protected keys may be generated with `openssl` as PKCS#8 RSA formatted. A `ca.crt` and `ca.key` is required for the following steps to sign the server certificates. Refer to [EasyRSA](#easyrsa) section to initialize and create the CA certificate/key.

```console
# create a private RSA key
openssl genrsa -out key.pem 2048

# Convert to pkcs8 (enter encryption passphrase)
openssl pkcs8 -topk8 -inform PEM -outform PEM -in key.pem -out key-pkcs8.pem

# Use the key to create a signing request
openssl req -new -newkey rsa:2048  -key key-pkcs8.pem -out server.csr -config csr.conf -sha256

# Send signing request to the CA to create the crt
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 10000 -extensions v3_ext -extfile csr.conf -sha256

cp key-pkcs8.pem tls.key
cp server.crt tls.crt
```

Ensure that the resulting `tls.key` can be decrypted by running the following command:

```console
$ openssl rsa -noout -modulus -text -in tls.key

Enter pass phrase for tls.key:  <passphrase>
```

### [](#private-key-formatting-legacy)Private Key Formatting (Legacy)

Due to an [issue](https://issues.couchbase.com/browse/MB-24404) with Couchbase Server's private key handling, server keys may need to be PKCS#1 formatted. This was addressed in Autonomous Operator 2.2 (and this tutorial) with the implementation of [couchbaseclusters.spec.networking.tls.secretSource](resource/couchbasecluster.md#couchbaseclusters-spec-networking-tls-secretsource).

However, if you are using legacy TLS configuration with [couchbaseclusters.spec.networking.tls.static](resource/couchbasecluster.md#couchbaseclusters-spec-networking-tls-static), you will need to format the server keys in PKCS#1:

```console
$ openssl rsa -in pkey.key -out pkey.key.der -outform DER
```

```console
$ openssl rsa -in pkey.key.der -inform DER -out pkey.key -outform PEM
```

## [](#creating-a-dynamic-admission-controller-server-certificate)Creating a Dynamic Admission Controller Server Certificate

This section is only relevant if you wish to manually deploy the dynamic admission controller. Most users should use `cao` to automatically install the DAC.

To create a server certificate that can be used by the dynamic admission controller, simply specify the service name that the Kubernetes API webhooks will connect to. This is in the form `_<service>_._<namespace>_.svc`, so if our service is called `couchbase-operator-admission` and we were deploying it in the `operator-admission` namespace, run the following:

```console
$ ./easyrsa --subject-alt-name='DNS:couchbase-operator-admission.operator-admission.svc' build-server-full couchbase-admission-controller nopass`
```

## [](#creating-a-client-certificate)Creating a Client Certificate

This process is very similar to creating a server certificate. Assuming the administrative user defined for Couchbase Server is `Administrator` you can create a client certificate for the Operator to use with the following command:

```console
$ ./easyrsa build-client-full Administrator nopass
```

The created files `pki/private/Administrator.key` and `pki/issued/Administrator.crt` can be used as `tls.key` and `tls.crt` respectively when specifying the [couchbaseclusters.spec.networking.tls.secretSource.clientSecretName](resource/couchbasecluster.md#couchbaseclusters-spec-networking-tls-secretsource-clientsecretname) field.

## [](#further-reading)Further reading

* [How to configure TLS](howto-tls.md)
* [How to configure Password Protected TLS](howto-tls-passphrase.md)