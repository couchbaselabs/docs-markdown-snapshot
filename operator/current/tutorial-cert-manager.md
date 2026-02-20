---
title: Using a Certificate Manager
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.9/modules/ROOT/pages/tutorial-cert-manager.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:operator::tutorial-cert-manager.adoc[]
---

[View original HTML](/operator/current/tutorial-cert-manager.html)

# Using a Certificate Manager

> This tutorial demonstrates how to set up a certificate manager ([cert-manager](https://cert-manager.io/)) to be used with the Operator dynamic admission controller (DAC) and managed Couchbase clusters. Certificate managers like cert-manager provide native Kubernetes support for TLS certificate generation and rotation. 

> [!WARNING]
> Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer.

## [](#what-is-cert-manager)What is cert-manager?

[cert-manager](https://cert-manager.io/) is a Kubernetes controller — much like the Kubernetes Operator — that defines Kubernetes resource types that represent X.509 primitives. The key resources we will examine in further depth are:

Issuer

This type represents a certificate issuer. This may be a root certificate authority (CA), or a signing certificate (intermediate CA). It is your responsibility to provide the certificate and private key for this resource.

Certificate

This type represents a certificate and private key pair. It allows the specification of the private key size and algorithm. If allows the specification of the certificate name, lifetime, usages, and any subject alternative addresses (SANs). A `Certificate` _references_, and _is signed by_, an `Issuer`.

Certificates are initially issued by cert-manager, then at a defined time before the expiry, are automatically rotated.

Certificates are stored in a Kubernetes `Secret` resource, broadly similar to the standard `kubernetes.io/tls` secret type. The one major difference is that, along with `tls.crt` and `tls.key` secret data, there is also a `ca.crt` copied in from the `Issuer`.

(You may notice that this has heavily influenced the design of the Kubernetes Operator’s TLS interface.)

## [](#before-we-begin)Before We Begin

Before continuing with this tutorial, please ensure the following:

* You have installed cert-manager. Follow the official installation guides at [cert-manager.io](https://cert-manager.io/docs/installation/).
* You have installed Kubernetes Operator 2.2 or higher. This tutorial assumes that the installed resources are present, and also leverages the [cao](tools/cao.md) command line tool that comes with the Kubernetes Operator binary package.  
> [!NOTE]  
> You can actually integrate/perform the steps in this tutorial as part of the process of installing the Kubernetes Operator. However, for the sake of making the tutorial more straightforward, it is assumed that you’ve already performed a basic [installation](install-kubernetes.md) of the Kubernetes Operator.

Another thing to note is that all of the commands in this tutorial are run from the same, default, namespace. cert-manager runs cluster scoped, and can see Issuers and Certificates in any namespace, so you can use any namespace you desire. Before you begin the tutorial, make sure to configure your Kubernetes context to point to the namespace where you deploy Couchbase resources, or ensure you use the `--namespace` configuration flag with the given commands.

## [](#creating-a-common-configuration)Creating a Common Configuration

The best way to explain cert-manager is by example. The following subsections describe how to create a common configuration that will be used to sign certificates for both the dynamic admission controller (DAC) and our Couchbase clusters.

### [](#create-a-root-ca)Create a Root CA

First, we need to create a root CA. The following commands demonstrate how to create a root CA using `easy-rsa`:

```console
$ git clone https://github.com/OpenVPN/easy-rsa
$ cd easy-rsa/easyrsa3
$ ./easyrsa init-pki
$ ./easyrsa build-ca nopass
$ cat pki/private/ca.key | base64 -w 0 (1)
$ cat pki/ca.crt | base64 -w 0 (2)
```

| **1** | The output of this command is the encoded CA key, and will be used in the next step.         |
| ----- | -------------------------------------------------------------------------------------------- |
| **2** | The output of this command is the encoded CA certificate, and will be used in the next step. |

### [](#create-an-issuer)Create an Issuer

Next, we’ll create the CA’s `Secret` and `Issuer`. Start by creating two files — `ca-secret.yaml` and `ca-issuer.yaml` — with the following configurations:

ca-secret.yaml

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ca
data:
  tls.key: LS0tLS1C... (1)
  tls.crt: LS0tLS1C... (2)
```

| **1** | This is the CA key from the previous step; textual representation has been shortened for brevity.         |
| ----- | --------------------------------------------------------------------------------------------------------- |
| **2** | This is the CA certificate from the previous step; textual representation has been shortened for brevity. |

ca-issuer.yaml

```yaml
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: ca (1)
spec:
  ca:
    secretName: ca (2)
```

| **1** | This is the issuer name; take a note of it, as it will be referred to by Certificate resources and used to sign certificates. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------- |
| **2** | This is a reference to the CA secret we have just created containing the CA certificate and key pair.                         |

Run the following commands to create the CA’s `Secret` and `Issuer`:

```console
$ kubectl apply -f ca-secret.yaml
```

```console
$ kubectl apply -f ca-issuer.yaml
```

## [](#using-cert-manager-with-the-dac)Using cert-manager with the DAC

The DAC [component](concept-operator.md#dynamic-admission-controller) of the Kubernetes Operator distribution has built-in certificate rotation detection and handling. This makes it a perfect candidate for automation.

### [](#uninstall-the-existing-dac)Uninstall the Existing DAC

As mentioned in the [prerequisites](#before-we-begin) section, this tutorial assumes that you’ve already performed a basic [installation](install-kubernetes.md) of the Kubernetes Operator. As part of the installation, you would have also installed the DAC. Before we can continue with the tutorial, we need to _uninstall_ the DAC. (Don’t worry, we’ll be re-installing it soon.)

```console
$ cao delete admission
```

### [](#create-the-dac-certificate)Create the DAC Certificate

We need to create a `Certificate` resource to issue and rotate the DAC certificate and key. Paste the following configuration into your editor of choice and save the file as `admission-certificate-resource.yaml`:

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: couchbase-operator-admission
spec:
  secretName: couchbase-operator-admission (1)
  duration: 6h (2)
  renewBefore: 1h (3)
  commonName: couchbase-operator-admission
  isCA: false
  privateKey:
    algorithm: RSA
    encoding: PKCS8
    size: 2048
  usages:
  - server auth (4)
  dnsNames:
  - couchbase-operator-admission.default.svc (5)
  issuerRef:
    group: cert-manager.io
    kind: Issuer
    name: ca (6)
```

| **1** | This is the secret that will be generated containing the TLS certificate and key. The name used in this example is the same as the default one created by [cao](tools/cao.md) during standard [installation](install-kubernetes.md), so we’ll just reuse it to make integration simpler.                                                                                                                                                       |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The certificate will be issued immediately and will be valid for 6 hours.                                                                                                                                                                                                                                                                                                                                                                      |
| **3** | The certificate will be reissued (rotated) 1 hour before the certificate expiration time.                                                                                                                                                                                                                                                                                                                                                      |
| **4** | The certificate can be used as server authentication — the DAC is a HTTPS server.                                                                                                                                                                                                                                                                                                                                                              |
| **5** | The certificate needs a subject alternative name that matches the network name used to connect to it. This name is comprised of _<service-name>_._<namespace>_.svc. The [cao](tools/cao.md) tool usually handles this for you, however, as TLS generation is delegated to a 3rd party, we need to be aware of it. Again, like the secret name, this is the default service name created by [cao](tools/cao.md), so we’ll just keep this as is. |
| **6** | The issuer, ca, refers to the CA we defined in the section [Creating a Common Configuration](#creating-a-common-configuration).                                                                                                                                                                                                                                                                                                                |

Run the following command to create the `Certificate` resource:

```console
$ kubectl apply -f admission-certificate-resource.yaml
```

> [!NOTE]
> This command will not succeed if the DAC is already installed. Ensure that you’ve followed the instructions in the section [Uninstall the Existing DAC](#uninstall-the-existing-dac) before running this command.

You can run the following command to check the status of the resource:

```console
$ kubectl get certificates
```

If it was created/applied properly, the output should look like the following:

```console
NAME                           READY   SECRET                         AGE
couchbase-operator-admission   True    couchbase-operator-admission   4s
```

### [](#update-the-dac-configuration-settings)Update the DAC Configuration Settings

When you install the Kubernetes Operator, the [cao](tools/cao.md) tool automatically creates a default TLS configuration for you. However, we don’t have to worry about this default configuration because we removed it entirely when we uninstalled the DAC in the section [Uninstall the Existing DAC](#uninstall-the-existing-dac). Therefore, in this next step, we will generate a brand new DAC configuration, modify it to make use of our managed certificates, and then submit it to Kubernetes to redeploy the DAC.

Start by generating a copy of the default configuration template for the DAC:

```console
$ cao generate admission > admission.yaml
```

Open `admission.yaml` with your editor of choice.

The first thing we’re going to do is _remove_ (delete) the `Secret` resource configuration from this file, as cert-manager is now managing it for us. The configuration that you need to remove looks like the following:

```yaml
apiVersion: v1
data:
  tls-cert-file: LS0tLS1CRU...
  tls-private-key-file: LS0tLS1CRU...
kind: Secret
metadata:
  annotations:
    config.couchbase.com/version: 2.2.0
  creationTimestamp: null
  name: couchbase-operator-admission
```

Next, locate the `ValidatingWebhookConfiguration` resource. This needs to be updated to include the signing CA’s certificate. If you recall, when we [created the certificate issuer](#create-an-issuer), we configured its `Secret` with a `tls.crt` key. We simply need to copy this same `tls.crt` key into each instance of `caBundle` in the webhook resources.

```yaml
apiVersion: admissionregistration.k8s.io/v1beta1
kind: ValidatingWebhookConfiguration
metadata:
  creationTimestamp: null
  name: couchbase-operator-admission
webhooks:
- clientConfig:
    caBundle: LS0tLS1CRU... (1)
```

| **1** | Replace the existing key with the tls.crt key of the certificate issuer. |
| ----- | ------------------------------------------------------------------------ |

Now save all of your changes to `admission.yaml` and exit your editor — the configuration is ready to to be submitted to Kubernetes. Run the following command to deploy the DAC:

```console
$ kubectl apply -f admission.yaml
```

If all goes well, you can create Couchbase resources, and the DAC will reject any misconfiguration:

```console
$ kubectl apply -f example/couchbase-cluster.yaml
couchbasebucket.couchbase.com/default created
Error from server: error when creating "example/couchbase-cluster.yaml": admission webhook "couchbase-operator-admission.default.svc" denied the request: validation failure list:
secret cb-example-auth referenced by spec.security.adminSecret must exist
```

However, if you see something similar to the following, it means that the Kubernetes API isn’t able to validate your server certificate:

```console
$ kubectl apply -f example/couchbase-cluster.yaml
Error from server (InternalError): error when creating "example/couchbase-cluster.yaml": Internal error occurred: failed calling webhook "couchbase-operator-admission.default.svc": Post "https://couchbase-operator-admission.default.svc:443/couchbaseclusters/validate?timeout=10s": x509: certificate signed by unknown authority
```

If this is the case, check that the correct CA is installed in the webhooks, and ensure that the server certificate issued by cert-manager is valid and verifies against the CA.

## [](#using-cert-manager-with-a-couchbase-cluster)Using cert-manager with a Couchbase Cluster

The Kubernetes Operator has been capable of rotating Couchbase Server certificates since version 2.0\. With the 2.2 release, we introduced the ability to use new certificate formats, in particular the standard form used by cert-manager. This allows the database’s TLS configuration to be specified in code, along with security policies. The key benefits of using this are 1.) oversight — the ability to peer review configuration; and 2.) auditing — providing simple, policy driven security constraints.

### [](#create-the-couchbase-server-certificate)Create the Couchbase Server Certificate

Using our common issuer, we will create a certificate for use with Couchbase Server. Paste the following configuration into your editor of choice and save the file as `server-certificate-resource.yaml`:

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: cb-example
spec:
  secretName: server-tls (1)
  duration: 6h (2)
  renewBefore: 1h (3)
  commonName: couchbase-server
  isCA: false
  privateKey:
    algorithm: RSA
    encoding: PKCS8 (4)
    size: 2048
  usages:
    - server auth (5)
  dnsNames: (6)
    - "*.cb-example"
    - "*.cb-example.default"
    - "*.cb-example.default.svc"
    - "*.cb-example.default.svc.cluster.local"
    - "cb-example-srv"
    - "cb-example-srv.default"
    - "cb-example-srv.default.svc"
    - "*.cb-example-srv.default.svc.cluster.local"
    - localhost
  issuerRef:
    name: ca (7)
    group: cert-manager.io
    kind: Issuer
```

| **1** | This is the secret that will be generated containing the TLS certificate and key.                                                                                                                                    |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The certificate will be issued immediately and will be valid for 6 hours.                                                                                                                                            |
| **3** | The certificate will be reissued (rotated) 1 hour before the certificate expiration time.                                                                                                                            |
| **4** | Couchbase Server only works with PKCS#1 private keys, but, because we have to create a shadow copy of the certificates with hard coded names, we can also translate private keys from one format to another.         |
| **5** | The certificate can be used as server authentication.                                                                                                                                                                |
| **6** | The certificate needs a set of subject alternative names (SAN) that cover all possible methods of addressing the cluster by clients. The canonical list of SANs can be found in the [TLS tutorial](tutorial-tls.md). |
| **7** | The issuer, ca, refers to the CA we defined in the section [Creating a Common Configuration](#creating-a-common-configuration).                                                                                      |

Run the following command to create the `Certificate` resource:

```console
$ kubectl apply -f server-certificate-resource.yaml
```

You can run the following command to check the status of the resource:

```console
$ kubectl get certificates
```

If it was created/applied properly, the output should look like the following:

```console
NAME                           READY   SECRET                         AGE
cb-example                     True    server-tls                     10s
couchbase-operator-admission   True    couchbase-operator-admission   32m
```

### [](#create-the-couchbase-cluster)Create the Couchbase Cluster

Consuming certificates issued by cert-manager is fairly straightforward. Using the `couchbase-cluster.yaml` template from the Kubernetes Operator binary package, make the following edits to the `CouchbaseCluster` custom resource:

```console
apiVersion: v1
kind: Secret
metadata:
  name: cb-example-auth
type: Opaque
data:
  username: QWRtaW5pc3RyYXRvcg==
  password: cGFzc3dvcmQ=
---
apiVersion: couchbase.com/v2
kind: CouchbaseBucket
metadata:
  name: default
---
apiVersion: couchbase.com/v2
kind: CouchbaseCluster
metadata:
  name: cb-example
spec:
  image: couchbase/server:7.2.3
  security:
    adminSecret: cb-example-auth
  networking:
    tls:
      secretSource: (1)
        serverSecretName: server-tls (2)
  buckets:
    managed: true
  servers:
    - name: basic
      size: 3
      services:
        - data
        - index
        - query
```

| **1** | The secretSource TLS provider tells the Kubernetes Operator that the secrets will be in kubernetes.io/tls format. This also requires a ca.crt key, which cert-manager provides automatically.                     |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The serverSecretName tells the Kubernetes Operator to use the cert-manager issued secret defined in the previous section [\[create-the-Couchbase-server-certificate\]](#create-the-Couchbase-server-certificate). |

Run the following command to create the `Certificate` resource:

```console
$ kubectl apply -f couchbase-cluster.yaml
```

You can run the following command to check the status of the deployment:

```console
$ kubectl get cbc
```

If the Couchbase cluster was deployed successfully, the output should look like the following:

```console
NAME         VERSION   SIZE   STATUS      UUID                               AGE
cb-example   7.2.3     3      Available   8c531b1cc11680c286d04616cc7a8185   3m31s
```

## [](#summary)Summary

By embracing the `kubernetes.io/tls` format, the Kubernetes Operator is able to draw upon great 3rd-party tools, like cert-manager, that offer simplicity, security, and regulation within your Kubernetes environment.