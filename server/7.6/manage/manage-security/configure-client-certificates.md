---
title: Configure Client Certificates
description: Couchbase Server supports client-authentication by means of X.509 certificates.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/manage/pages/manage-security/configure-client-certificates.adoc
  xref: xref:7.6@server:manage:manage-security/configure-client-certificates.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/manage/manage-security/configure-client-certificates.html)

# Configure Client Certificates

> Couchbase Server supports client-authentication by means of X.509 certificates. 

## [](#couchbase-client-authentication)Couchbase Client Authentication

Couchbase clients can authenticate by means of X.509 certificates. This page provides step-by-step instructions for the creation of client certificates for:

* _Couchbase Server_. The certificate can be used by a Couchbase Server-cluster that wishes to secure its connection to another Couchbase Server-cluster. This certificate might be used by a _source_ cluster that wishes to perform _Cross Data Center Replication_ securely, to a _destination_ cluster.
* _Java Applications_. A Java application based on the Couchbase SDK can obtain its client certificate from a Java _keystore_, and so authenticate with Couchbase Server securely.

For a list of Couchbase-Server ports that provide secure connectivity to clients, see [Connectivity](../../learn/clusters-and-availability/connectivity.md).

## [](#cert-auth-for-couchbase-server)Configure Client Certificates for Couchbase Server

The section contains two procedures for the creation of a client certificate and key, whereby authentication with Couchbase Server can be performed:

* [Client Access: Root-Certificate Authorization](#client-certificate-authorized-by-a-root-certificate) shows how to create a client certificate that is authorized by a cluster's root certificate. The procedure for creating a root certificate (and, based on the root certificate, the cluster's individual per node certificates), is provided in [Cluster Protection with Root and Node Certificates](configure-server-certificates.md#root-and-node-certificates). The instructions on the current page assume that _that_ procedure has already been followed: therefore, they duly make use of the previously created directory structure and files.  
Note that in Couchbase Server Version 7.1 and later, multiple root certificates can be uploaded into the cluster, some potentially to be used for client authentication only; and therefore not to be used for the signing of node certificates. Therefore, a client no longer _needs_ to base its authority on a CA that is being used to protect the server: however, the CA it uses must be recognizable to the cluster; and as such, must be a root certificate uploaded into the cluster's trust store. For an overview, see [Using Multiple Root Certificaes](../../learn/security/using-multiple-cas.md).
* [Client Access: Intermediate-Certificate Authorization](#client-certificate-authorized-by-an-intermediate-certificate) shows how to create a client certificate that is authorized by an _intermediate_ certificate; which derives its own authority from a root certificate; and which is used instead of the root for the signing of the client certificate. The procedure for creating a root, server-intermediate and per node certificates is provided in [Cluster Protection with Root, Intermediate, and Node Certificates](configure-server-certificates.md#root-intermediate-and-node-certificates). The instructions on the current page assume that _that_ procedure has already been followed: therefore, they duly make use of the previously created directory structure and files.

Both procedures additionally assume that the instance of Couchbase Server to be accessed by the client:

* Contains the sample bucket `travel-sample`: this is the bucket whose contents the client wishes to read and write. For information on sample buckets and how to install them, see [Sample Buckets](../manage-settings/install-sample-buckets.md).
* Has a defined, locally authenticated user named `clientuser`, who has been assigned a role that permits reading and writing to the `travel-sample` bucket. For information on creating users and roles, see [Manage Users and Roles](manage-users-and-roles.md).
* Has client-certificate handling configured as either _enabled_ or _mandatory_. For details, see [Enable Client-Certificate Handling](enable-client-certificate-handling.md).

Note that additional information on file-types can be found in the procedures for _server_\-certificate generation; in [Configure Server Certificates](configure-server-certificates.md).

### [](#client-certificate-authorized-by-a-root-certificate)Client Access: Root-Certificate Authorization

Proceed as follows:

1. Within the top-level directory created in [Cluster Protection with Root and Node Certificates](configure-server-certificates.md#root-and-node-certificates), create and access a new working directory.  
cd servercertfiles  
mkdir clientcertfiles  
cd clientcertfiles
2. Create an extensions file for the use of all clients.  
cat > client.ext <<EOF  
basicConstraints = CA:FALSE  
subjectKeyIdentifier = hash  
authorityKeyIdentifier = keyid,issuer:always  
extendedKeyUsage = clientAuth  
keyUsage = digitalSignature  
EOF  
This specifies a value of `FALSE` for `CA`, indicating that the client certificate will not have the ability to act as an authority for other certificates. Its `extendedKeyUsage` is specified as `clientAuth`, indicating that the certificate will be used for authenticating a client. It `keyUsage` is specified as `digitalSignature`, indicating that its public key is usable for data-origin authentication.  
This extensions file thus contains definitions judged appropriate for all clients. Further constraints can be added for individual clients, as necessary.
3. Create a client private key.  
openssl genrsa -out ./travel-sample.key 2048  
This creates the private key `travel-sample.key`.
4. Generate the client-certificate signing-request.  
openssl req -new -key ./travel-sample.key -out ./travel-sample.csr -subj "/CN=clientuser"  
The client's private key, `travel-sample.key` is provided as input for the signing request. The _Common Name_ provided as `Subject` for the certificate is specified as `clientuser`, which is the name of the server-defined user to be authenticated by the client. The output request-file, `travel-sample.csr` is saved in the current directory.
5. Optionally, customize a client extensions file, to identify a _username_ to be authenticated.  
As described in [Specifying Usernames for Client-Certificate Authentication](../../learn/security/certificates.md#identity-encoding-in-client-certificates), a client certificate should contain a username, against which authentication can be performed on Couchbase Server. The server's default handling assumes that the _Subject Common Name_ specifies the username. However, a _Subject Alternative Name_ might be used; either in addition, or as an alternative.  
The following `subjectAltName` statement allows an email address to be specified as the basis for the username.  
cp ./client.ext ./client.ext.tmp  
echo "subjectAltName = email:john.smith@mail.com" \  
>> ./client.ext.tmp  
If Couchbase Server is configured to search for an email address to be used as a username (as described in [Specifying Usernames for Client-Certificate Authentication](../../learn/security/certificates.md#identity-encoding-in-client-certificates) and [Enable Client-Certificate Handling](enable-client-certificate-handling.md)), the user `john.smith` will be submitted for authentication.  
If this extension is _not_ added, and Couchbase Server client-certificate handling is left at its default, the _Common Name_ (which was specified as `clientuser`, when the client-certificate signing-request was generated) will continue to be used as the username.
6. Create the client certificate. In this example, the customized extensions file, `client.ext.tmp`, is used. However, if no email address or other Subject Alternative Name has been added, the generic client-extensions file, `client.ext`, can be used instead.  
openssl x509 -CA ../ca.pem -CAkey ../ca.key \
-CAcreateserial -days 365 -req -in ./travel-sample.csr \
-out ./travel-sample.pem -extfile ./client.ext.tmp  
The root certificate for the cluster, and its corresponding private key, `ca.pem` and `ca.key` are specified as inputs for certificate generation, so establishing the root certificate's authority, within the client certificate. The output file, `travel-sample.pem`, is the client certificate, and is saved in `clientcertfiles`.  
The confirmatory output is as follows:  
Signature ok  
subject=/CN=clientuser  
Getting CA Private Key  
This concludes the process. The client can now use `travel-sample.pem` to authenticate itself as having the authority of `ca.pem` (which is shared by the server it intends to access); and provides the username of `clientuser` (which the server associates with a role appropriate for access to the `travel-sample` bucket). The client key, `travel-sample.key`, can be used for digital signing.  
A possible use case for the client certificate thus generated is described below, in [Using Client and Server Certificates for Secure XDCR](#using-client-and-server-certificates-for-secure-xdcr).

### [](#client-certificate-authorized-by-an-intermediate-certificate)Client Access: Intermediate-Certificate Authorization

The following procedure demonstrates how an _intermediate_ certificate, with the authority of the _root_ certificate, can be created in order itself to sign _client_ certificates. The procedure assumes that the server-equivalent procedure described in [Cluster Protection with Root, Intermediate, and Node Certificates](configure-server-certificates.md#root-intermediate-and-node-certificates) has already been followed; and that the resulting directory-structure is still available.

Proceed as follows:

1. Access the `servercertfiles2/root` directory, created in [Cluster Protection with Root, Intermediate, and Node Certificates](configure-server-certificates.md#root-intermediate-and-node-certificates).  
cd servercertfiles2/root
2. Create an encrypted private key and a certificate signing request, for an intermediate certificate that is to be used for signing client certificates.  
openssl req -new -sha256 -newkey rsa:2048 -keyout ../clients/int.key \
-out reqs/client-signing.csr \
-subj '/C=UA/O=MyCompany/OU=People/CN=ClientSigningCA'  
Since this specifies that an encrypted private key be created, prompts appear requesting entry of an appropriate _pass phrase_. Enter an appropriate phrase against the prompts.  
This new private key is named `../clients/int.key`. The signing-request file is saved as `reqs/client-signing.csr`.
3. Create the intermediate certificate to be used for client-certificate signing.  
openssl x509 -CA ca.pem -CAkey ca.key -CAcreateserial -CAserial serial.srl \
-days 3650 -req -in reqs/client-signing.csr -out issued/client-signing.pem \
-extfile int.ext  
The root certificate and key for the cluster, `ca.pem` and `ca.key`, are specified as the authority for the intermediate certificate. Since `ca.key` is an encrypted key, a prompt appears, requesting that the appropriate pass phrase be entered: enter the appropriate phrase.  
Note that the extension file used here to constrain the capabilities of the intermediate certificate is that created in [Cluster Protection with Root, Intermediate, and Node Certificates](configure-server-certificates.md#create-intermediate-extensions-file).
4. Save the intermediate certificate as the certificate-authority for the client certificate that is to be created.  
cp issued/client-signing.pem ../clients/int.pem
5. Within the `../clients` directory, create an extension file for the client certificate:  
cd ../clients  
cat > client.ext <<EOF  
basicConstraints = CA:FALSE  
subjectKeyIdentifier = hash  
authorityKeyIdentifier = keyid,issuer:always  
extendedKeyUsage = clientAuth  
keyUsage = digitalSignature  
EOF  
The value of `extendedKeyUsage` is specified as `clientAuth`, indicating that the certificate will be used to authenticate a client. The value of `keyUsage` is specified as `digitalSignature`, indicating that the certificate may be used in the verifying of information-origin.
6. Create a private key for the client certificate.  
openssl genrsa -out private/clientuser.key 2048
7. Create a certificate signing request for the client certificate.  
openssl req -new -key private/clientuser.key -out reqs/clientuser.csr \
-subj "/C=UA/O=MyCompany/OU=People/CN=clientuser"  
The signing request is based on the private key `clientuser.key`. The username associated with the certificate is specified as `clientuser`: this is the username to be recognized by Couchbase Server, and associated with specific roles.
8. Create the client certificate.  
openssl x509 -CA int.pem -CAkey int.key -CAcreateserial -CAserial serial.srl \
-days 365 -req -in reqs/clientuser.csr \
-out issued/clientuser.pem -extfile client.ext  
This creates the client certificate `clientuser.pem`, based on the signing request `clientuser.csr`, and signed with the authority of the intermediate certificate and key, `int.pem` and `int.key`. Since `int.key` is encrypted, a prompt appears, requesting entry of the appropriate pass phrase: enter the appropriate phrase against the prompt. The certificate is saved in the `issued` folder.
9. Check the validity of the client certificate. The following use of the `openssl` command verifies the relationship between the root certificate, the client-intermediate certificate, and the client certificate.  
openssl verify -trusted ../root/ca.pem -untrusted int.pem \  
issued/clientuser.pem  
If the certificate is valid, the following output is displayed:  
issued/clientuser.pem: OK
10. Concatenate the issued client certificate with the client-intermediate certificate, to establish the chain of authority.  
cat issued/clientuser.pem int.pem > clientuser.pem  
The result of the concatenation, `clientuser.pem` is the completed client certificate.

### [](#using-client-and-server-certificates-for-secure-xdcr)Using Client and Server Certificates for Secure XDCR

Examples of using the certificates and keys created on this page above and in [Configure Server Certificates](configure-server-certificates.md) can be found in the documentation provided for securing _Cross Data Center Replication_, in [Specify Root and Client Certificates, and Client Private Key](../manage-xdcr/enable-full-secure-replication.md#specify-full-xdcr-security-with-certificates). When securing XDCR according to these instructions, use the following files:

* If the procedures explained in [Cluster Protection with Root and Node Certificates](configure-server-certificates.md#root-and-node-certificates) and [Client Access: Root-Certificate Authorization](#client-certificate-authorized-by-a-root-certificate) have been followed, specify:

  * The remote cluster root certificate as `servercertfiles/ca.pem`.
  * The client certificate as `servercertfiles/clientcertfiles/travel-sample.pem`.
  * The client private key as `servercertfiles/clientcertfiles/travel-sample.key`.
* If the procedures explained in [Cluster Protection with Root, Intermediate, and Node Certificates](configure-server-certificates.md#root-intermediate-and-node-certificates) and [Client Access: Intermediate-Certificate Authorization](#client-certificate-authorized-by-an-intermediate-certificate) have been followed, specify:

  * The remote cluster root certificate as `servercertfiles2/root/ca.pem`.
  * The client certificate as `servercertfiles2/clients/clientuser.pem`.
  * The client private key as `servercertfiles2/clients/private/clientuser.key`.

## [](#cert%5Fauth%5Ffor%5Fjava%5Fclient)Configure Client Certificates for Java Clients

A _Java_ client uses a _keystore_ to access the certificates it requires for authentication. Certificate and keystore preparation is demonstrated by the procedures in the following two sections, which are:

* [Java Client Access: Root-Certificate Authorization](#java-client-access-root-certificate-authorization). This creates a Java-client certificate signed by the cluster's root certificate. As such, the procedure follows on from the server-certificate creation-process documented in [Cluster Protection with Root and Node Certificates](configure-server-certificates.md#root-and-node-certificates); and makes use of the directories and keys created there.
* [Java Client Access: Intermediate-Certificate Authorization](#java-client-access-intermediate-certificate-authorization). This creates a Java-client certificate signed by the cluster's intermediate certificate. As such, the procedure follows on from the server-certificate creation-process documented in [Cluster Protection with Root, Intermediate and Node Certificates](configure-server-certificates.md#root-intermediate-and-node-certificates); and makes use of the directories and keys created there.

Note that the [assumptions](#assumptions) specified for the examples above likewise apply to the Java client examples below.

### [](#java-client-access-root-certificate-authorization)Java Client Access: Root-Certificate Authorization

Proceed as follows:

1. Access the main working directory created in [Cluster Protection with Root and Node Certificates](configure-server-certificates.md#root-and-node-certificates), and create and access a new working directory for the Java client certificate to be created.  
cd servercertfiles  
mkdir javaclient  
cd javaclient
2. Define two environment variables: one for the name of the keystore to be created, another for its password.  
```bash  
export KEYSTORE_FILE=my.keystore  
export STOREPASS=storepass  
```
3. If necessary, install a package containing the `keytool` utility:  
```bash  
sudo apt install openjdk-17-jre-headless  
```  
Note that available packages can be found by means of `sudo apt-cache search openjdk`.
4. Generate the keystore. Note that the password you specify for the alias, by means of the `--keypass` flag, must be identical to the password you specify for the keystore, by means of the `--storepass` flag. In this case, both passwords are specified as `${STOREPASS}`; which resolves to `storepass`.  
```bash  
keytool -genkey -keyalg RSA -alias selfsigned \
-keystore ${KEYSTORE_FILE} -storepass ${STOREPASS} -validity 360 \
-keysize 2048 -noprompt  -dname "CN=clientuser, OU=People, O=MyCompany, \  
L=None, S=None, C=UA" -keypass ${STOREPASS}  
```  
Note that the `Common Name` for the certificate is specified as `clientuser`, which is the username established on Couchbase Server, whose role-assignment is supportive of reading and writing data to the `travel-sample` bucket.
5. Generate the certificate signing-request:  
```bash  
keytool -certreq -alias selfsigned -keyalg RSA -file my.csr \
-keystore ${KEYSTORE_FILE} -storepass ${STOREPASS} -noprompt  
```  
This creates the signing-request file, `my.csr`.  
Note that in this example, although only the `Common Name` is being used to establish the identity of the user seeking authorization, one or more `Subject Alternative Names` could also be added. For example, by adding `-ext "san=email:john.smith@mail.com"` to the certificate signing-request used in the current step, the email-address `john.smith@mail.com` could be established as the basis for an alternative username to be submitted for authentication. See [Specifying Usernames for Client-Certificate Authentication](../../learn/security/certificates.md#identity-encoding-in-client-certificates), for more information.
6. Generate the client certificate, signing it with the root private key, and thereby establishing the root certificate's authority:  
```bash  
openssl x509 -req -in my.csr -CA ../ca.pem \
-CAkey ../ca.key -CAcreateserial -out clientcert.pem -days 365  
```
7. Add the root certificate to the keystore:  
```bash  
keytool -import -trustcacerts -file ../ca.pem \
-alias root -keystore ${KEYSTORE_FILE} -storepass ${STOREPASS} -noprompt  
```
8. Add the client certificate to the keystore:  
```bash  
keytool -import -keystore ${KEYSTORE_FILE} -file clientcert.pem \
-alias selfsigned -storepass ${STOREPASS} -noprompt  
```

This concludes preparation of the Java client's keystore. Copy the file (in this case, `my.keystore`) to a location on a local filesystem from which the Java client can access it. A sample Java program, which accesses a keystore from a local filesystem, is provided in [Authenticating a Java Client by Certificate](../../../../java-sdk/current/howtos/sdk-authentication.md#authenticating-the-java-client-by-certificate).

### [](#java-client-access-intermediate-certificate-authorization)Java Client Access: Intermediate-Certificate Authorization

Proceed as follows:

1. Access the main working directory created in [Cluster Protection with Root, Intermediate, and Node Certificates](configure-server-certificates.md#root-intermediate-and-node-certificates), and create and access a new working directory for the Java client certificate to be created.  
cd servercertfiles2  
mkdir javaclient  
cd javaclient
2. Define two environment variables: one for the name of the keystore to be created, another for its password:  
export KEYSTORE_FILE=my.keystore  
export STOREPASS=storepass
3. If necessary, install a package containing the `keytool` utility:  
sudo apt install openjdk-17-jre-headless
4. Generate the keystore. Note that the password you specify for the alias, by means of the `--keypass` flag, must be identical to the password you specify for the keystore, by means of the `--storepass` flag. In this case, both passwords are specified as `${STOREPASS}`; which resolves to `storepass`.  
keytool -genkey -keyalg RSA -alias selfsigned \
-keystore ${KEYSTORE_FILE} -storepass ${STOREPASS} -validity 360 \
-keysize 2048 -noprompt  -dname "CN=clientuser, OU=People, O=MyCompany, \  
L=None, S=None, C=UA" -keypass ${STOREPASS}  
Note that the Common Name for the certificate is specified as `clientuser`, which is the username established on Couchbase Server, whose role-assignment is supportive of reading and writing data to the `travel-sample` bucket.
5. Generate the certificate signing-request:  
keytool -certreq -alias selfsigned -keyalg RSA -file my.csr \
-keystore ${KEYSTORE_FILE} -storepass ${STOREPASS} -noprompt
6. Generate the client certificate, signing it with the intermediate private key, and thereby establishing the intermediate certificate's authority:  
openssl x509 -req -in my.csr -CA ../servers/int.pem \
-CAkey ../servers/int.key -CAcreateserial -out clientcert.pem -days 365  
Since the intermediate private key was encrypted, a prompt now appears, requesting entry of the pass phrase for the key:  
Enter pass phrase for ../servers/int.key:  
Enter the pass phrase against the prompt.
7. Add the root certificate to the keystore:  
keytool -import -trustcacerts -file ../root/ca.pem \
-alias root -keystore ${KEYSTORE_FILE} -storepass ${STOREPASS} -noprompt
8. Add the intermediate certificate to the keystore:  
keytool -import -trustcacerts -file ../servers/int.pem \
-alias root2 -keystore ${KEYSTORE_FILE} -storepass ${STOREPASS} -noprompt
9. Add the client certificate to the keystore:  
keytool -import -keystore ${KEYSTORE_FILE} -file clientcert.pem \
-alias selfsigned -storepass ${STOREPASS} -noprompt

This concludes preparation of the Java client's keystore. Copy the file (in this case, `my.keystore`) to a location on a local filesystem from which the Java client can access it. A sample Java program, which accesses a keystore from a local filesystem, is provided in [Authenticating a Java Client by Certificate](../../../../java-sdk/current/howtos/sdk-authentication.md#authenticating-the-java-client-by-certificate).

## [](#enabling-client-security)Securing Client Access with TLS

For an application to communicate securely with Couchbase Server, SSL/TLS must be enabled on the client side. Enablement requires a copy of the root certificate used by Couchbase Server: this can be accessed from the Couchbase Web Console, as described in [Root Certificate](manage-security-settings.md#root-certificate-security-screen-display).

Note that if, at some point, the root certificate gets regenerated on the server-side, a copy of the new version must be obtained, and the client re-enabled.