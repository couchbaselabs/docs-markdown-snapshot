[View original HTML](/enterprise-analytics/2.0/manage/manage-security/configure-server-certificates.html)

> Enterprise Analytics supports using X.509 and PKCS #12 certificates for authenticating and encrypting data between the nodes in the cluster. 

This page explains how to configure server certificates for Enterprise Analytics. For an overview of how Enterprise Analytics uses certificates, see [Certificates](../../../../server/current/learn/security/certificates.md).

The procedures in this page are only limited examples. They cover the basic steps for creating certificates. When creating and deploying certificates for your own database, you often have to modify these steps to suit your environment.

This page gives detailed steps to configure X.509 certificates on a Linux-based single node Enterprise Analytics. It demonstrates two scenarios. The first shows directly signing the node’s certificate using the root certificate. The second shows creating an intermediate certificate from the root certificate and using that to sign the node’s certificate.

This page also explains how you can bundle certificates, private keys, and certificate chains into a single Public-Key Cryptography Standard (PKCS) #12 certificate file. Enterprise Analytics supports using this type of file to upload node certificates.

|  | Once you deploy cluster and node certificates to a database, you must create additional node certificates for any new nodes you add later. See [Adding New Cluster Nodes](#adding-new-cluster-nodes) for details. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#root-and-node-certificates)Create and Deploy Cluster and Node Certificates

The following procedure shows how to create a self-signed root certificate for a single-node database. It then demonstrates using that certificate to sign a node certificate. The steps for a multi-node cluster are similar, as explained at the end of the example.

1. Open a command line shell on the node.
2. In some directory (such as your home directory or `/tmp`) create working directories:  
```console  
mkdir servercertfiles  
cd servercertfiles  
mkdir -p {public,private,requests}  
```  
In this example, each directory has a different purpose:

  * The `public` directory stores certificates, which contain public keys.
  * The `private` directory contains private keys.
  * The `requests` directory stores certificate signing requests.
3. Create a private key for the cluster:  
```console  
openssl genrsa -out ca.key 2048  
```  
The output of this command, `ca.key`, is the private key for the cluster.
4. Create the certificate (the file that contains the public key) for the cluster:  
```console  
openssl req -new -x509 -days 3650 -sha256 -key ca.key -out ca.pem \
        -subj "/CN=Couchbase Root CA"  
```  
The arguments to this command are:

  * `-x509`: generates an X.509 format certificate.
  * `-days 3650`: the number of days before the certificate expires.
  * `-sha256` the hashing algorithm to use for the digital signature.
  * `-key ca.key`: sets the private key file the certificate is based on to the private key you created in the previous step.
  * `-out ca.pem`: the filename for the certificate.
  * `-subj "/CN=Couchbase Root CA"`: the `/CN=` portion of the argument sets the common name of the certificate’s issuer to `Couchbase Root CA`. This name identifies the certificate as the root certificate for the Enterprise Analytics cluster.
5. Optionally, you can review the content of the certificate you just created using the command:  
```console  
openssl x509 -text -noout -in ./ca.pem  
```  
The following is an example of the first part of the output:  
Certificate:  
    Data:  
        Version: 3 (0x2)  
        Serial Number: 18276610881715621025 (0xfda390c366b2cca1)  
    Signature Algorithm: sha256WithRSAEncryption  
        Issuer: CN=Couchbase Root CA  
        Validity  
            Not Before: Sep  2 08:32:31 2019 GMT  
            Not After : Aug 30 08:32:31 2029 GMT  
        Subject: CN=Couchbase Root CA  
        Subject Public Key Info:  
            Public Key Algorithm: rsaEncryption  
                Public-Key: (2048 bit)  
                Modulus:  
                    00:d7:a6:ba:5d:e2:e2:fd:6e:1b:33:9a:4b:bf:77:  
                    6f:28:c3:37:60:33:da:09:b2:0b:73:1f:f9:65:2a:  
                                  .  
                                  .  
For detailed information about keys and key generation, see [RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA%5F%28cryptosystem%29).
6. Create a private key for the node. Each node in the cluster needs its own private key and certificate. Enterprise Analytics requires that you name the file containing the private key `pkey.key`. However, if you’re creating private keys for multiple nodes, you’ll need to give them unique filenames to avoid them overwriting each other. This example gives it a unique name, which you’ll need to change when you deploy the private key to the node.  
The command to create a private key is:  
```console  
openssl genrsa -out private/couchbase.default.svc.key 2048  
```
7. Create a Certificate Signing Request (CSR) for the node certificate:  
```console  
openssl req -new -key private/couchbase.default.svc.key \
        -out requests/couchbase.default.svc.csr -subj "/CN=Enterprise Analytics"  
```  
This step prepares the request you use to sign the node’s certificate with the cluster’s private key and certificate later.
8. Create a file that contains the certificate extensions that all nodes have in common. These extensions define constraints on how a certificate can be used. For detailed information about certificate extensions, see the [Standard Extensions](https://tools.ietf.org/html/rfc5280#section-4.2.1) section of the [Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL Profile)](https://tools.ietf.org/html/rfc5280). You submit the extensions to the signing CA, along with the CSR you generated in the previous step. The next step adds information specific to an individual node.  
Use this command to create the certificate extension file:  
```console  
cat > server.ext <<EOF  
basicConstraints=CA:FALSE  
subjectKeyIdentifier = hash  
authorityKeyIdentifier = keyid,issuer:always  
extendedKeyUsage=serverAuth  
keyUsage = digitalSignature,keyEncipherment  
EOF  
```  
The extensions in this file are:

  * `basicConstraints=CA:FALSE`: the certificate generated from the CSR cannot be used to issue other certificates.
  * `subjectKeyIdentifier = hash`: the Subject Key Identifier (SKI) is derived form a hash of the public key in the certificate.
  * `authorityKeyIdentifier = keyid,issuer:always`: specifies how to generate Authority Key Identifier (AKI). The `keyid` tells the certificate signing process to generate the AKI from the issuer’s public key (the cluster’s public key, in this example). The `issuer:always`: means that the signing process always includes the issuer’s distinguished name (DN)in the AKI.
  * `extendedKeyUsage=serverAuth`: means that the purpose of the certificate being signed is for server identification.
  * `keyUsage`: limits how the private key can be used. The values `digitalSignature,keyEncipherment` mean you can use the private key for digital signatures and for encipherment. Encipherment means that the key’s primary use is to encrypt session or symmetric keys, but it can also be used for direct data encryption.
9. Create a customized version of the certificate extensions file that contain settings specific to the node:  
```console  
cp ./server.ext ./server.ext.tmp  
echo "subjectAltName = IP:10.143.192.102" \  
>> ./server.ext.tmp  
```  
This command copies the file created in the previous step and adds a `subjectAltName` extension that identifies the node. This example uses the node’s IPv4 address. This extension makes sure the node’s certificate is valid for just the specific node. No other node or client can use the certificate. If your cluster uses DNS names to identify nodes, you must use the node’s DNS name, such as `DNS:node2.cb.com` instead of its IP address.

|  | Couchbase Enterprise Server requires that the node’s certificate identifies the node in a Subject Alternative Name extension. Without this identification, Enterprise Analytics reports an error when you upload the certificate to the node or when you try to add the node to the cluster. For more information, see [Node-Certificate Validation](../../../../server/current/learn/security/certificates.md#node-certificate-validation). |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
10. Create the node’s certificate by signing it with the certificate and digital signature of the CA. In this example, the CA is the root certificate created earlier. Therefore, the command to sign the node’s certificate uses the `ca.pem` and `ca.key` files:  
```console  
openssl x509 -CA ca.pem -CAkey ca.key -CAcreateserial -days 365 -req \
    -in requests/couchbase.default.svc.csr \
    -out public/couchbase.default.svc.pem \
    -extfile server.ext.tmp  
```  
The arguments to this command are:

  * `x509`: specifies that `openssl` is working with an X.509 certificate.
  * `-CA ca.pem -CAkey ca.key`: tells `openssl` to use the key and certificate created in steps 1 and 2 as the CA.
  * `-CAcreateserial`: tells `openssl` to create a serial number file if it does not already exist. It then writes the serial number it assigns to the certificate to this file. The serial file records the serial numbers of all the certificates `openssl` creates to make sure each certificate it creates has a unique serial number.
  * `-days 365`: sets the number of days before the certificate expires.
  * `-req`: tells `openssl` that you want to read a CSR to perform a certificate signing.
  * `-in requests/couchbase.default.svc.csr`: has `openssl` read the CSR created in step 6.
  * `out public/couchbase.default.svc.pem`: tells `openssl` sets where to save the signed node certificate.
  * `-extfile server.ext.tmp`: tells `openssl` to read the extensions file created in step 9.  
The file generated by this command, `couchbase.default.svc.pem`, is the node’s certificate.  
The output of running the previous command looks like this:  
```console  
Signature ok  
subject=/CN=Enterprise Analytics  
Getting CA Private Key  
```
11. Before you can deploy the key private key and the certificate to the node, you must rename their files. Enterprise Analytics requires that these files have specific filenames. Rename the certificate file to `chain.pem` and the private key file to `pkey.key`:  
```console  
cd ./public  
mv couchbase.default.svc.pem chain.pem  
cd ../private  
mv couchbase.default.svc.key pkey.key  
```

|  | In this example you could just have openssl output the correct filenames in steps 5 and 9\. In production, you often create certificates for multiple nodes at the same time, and so need to give each file a unique name. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
12. If the node to which you’re deploying the certificate does not have an inbox directory, create it. The inbox directory is where Enterprise Analytics looks for certificate, key, and related files. See [Load Root Certificates](../../reference/load-trusted-cas.md) for a list of the inbox paths on all platforms. On Linux, this directory is `/opt/enterprise-analytics/var/lib/couchbase/inbox/`.  
```console  
sudo mkdir /opt/enterprise-analytics/var/lib/couchbase/inbox/  
```
13. Copy the node certificate and node private key by copying them to the `inbox` directory.  
```console  
cd ..  
/opt/enterprise-analytics/var/lib/couchbase/inbox/chain.pem  
/opt/enterprise-analytics/var/lib/couchbase/inbox/pkey.key  
```

|  | This example has a single node, so you created the node’s certificate on the node where you’ll deploy it. Therefore, you can just copy the files into the correct directory using cp. When creating certificates for multiple nodes, you must move the files to the node’s filesystem to deploy them. If you created all of the certificates on one node, you can use a command such as scp to copy the files from that node to the node the certificate is for. Remember to create the inbox directory on each node as well. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
14. Deploy the root certificate. Enterprise Analytics expects to find the root certificate in a subdirectory named `CA` in the `inbox` directory. Create the subdirectory and then copy the root CA file:  
```console  
sudo mkdir /opt/enterprise-analytics/var/lib/couchbase/inbox/CA  
sudo cp ./ca.pem /opt/enterprise-analytics/var/lib/couchbase/inbox/CA.  
```
15. Make all files in the `inbox` directory readable by just the `couchbase` user:  
```console  
sudo chown -R couchbase /opt/enterprise-analytics/var/lib/couchbase/inbox/*  
sudo chmod -R 0700 /opt/enterprise-analytics/var/lib/couchbase/inbox/CA  
```
16. Call the REST API to have Enterprise Analytics load the root certificate for the cluster:  
```console  
curl -X POST http://10.143.192.102:8091/node/controller/loadTrustedCAs -u Administrator:password  
```
17. Optionally, verify that Enterprise Analytics has added the new root CA to its trust store:

  1. Sign into the Enterprise Analytics Web Console as a Full Administrator.
  2. Click **Security**, and click **Certificates**  
In this example, you can see both the original automatically generated root certificate and the newly uploaded certificate. The original generated root certificate appears at the top.  
![600](manage-security/rootCertificateWithSignedCert.png)  

|  | You cannot delete a certificate if it has signed one or more node certificates that are in use in the cluster. You can only delete the old autogenerated certificate after you have deployed new node certificates signed by the new root CA to each node. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  
For more information about the **Certificates** tab on the **Security** screen, see [Certificates](manage-security-settings.md#root-certificate-security-screen-display).
18. Load the node certificate and its private key by calling the [reloadCertificate](../../reference/upload-retrieve-node-cert.md) REST API:  
```console  
curl -X POST http://10.143.192.102:8091/node/controller/reloadCertificate -u Administrator:password  
```  
The node certificate is now activated for the current node, bearing the authority of the root CA.

For more information using the REST API to manage certificates, see [Certificate Management API](../../reference/rest-certificate-management.md). This includes details on retrieving root and nodes certificates that have been uploaded, and on certificate deletion.

This example demonstrated configuring certificates for a single node database. To deploy certificates for a multi-node cluster, repeat steps 6, 7, 9, 10, 11, 12, 15, and 18 for each node. Remember that you must copy the node’s certificate and key files to its own `inbox` directory to deploy them.

## [](#root-intermediate-and-node-certificates)Create and Use Intermediate Certificates to Sign Node Certificates

The previous example directly signed node certificates using the root certificate. In some cases, you may want to use an intermediate certificate to sign the certificates for the nodes. The primary reason to use an intermediate certificate is to prevent exposing the cluster’s private key.

For example, you may want to delegate the signing of node certificates. By creating an intermediate certificate, you can keep the cluster’s private key secret while allowing others to sign node certificates. The administrators to whom you delegate the signing of node certificates can use the intermediate certificate for signing. They do not need use to the cluster’s private key to sign the node certificates.

For more information, see [Adding Intermediate Certificates to the Trust Store](../../../../server/current/learn/security/using-multiple-cas.md#adding-intermediate-certificates-to-the-trust-store).

When a peer (such as another node or a client) attempts to connect to a node securely, it uses the node’s certificate to verify the node’s identity. The node can supply a chain of certificates to the peer in addition to its own. To verify the node’s identity, the peer searches for a CA it trusts in the chain of certificates from the node. See [Intermediate Certificates](../../../../server/current/learn/security/certificates.md#intermediate-certificates) for more information.

In Enterprise Analytics you can supply the peer with the chain of trust it needs to identify the node in one of two ways:

* Concatenation of all intermediate and node certificates into a single `chain.pem` file, which you deploy to the node. The node provides this entire chain of trust to the peer when it tries to connect securely.
* Deploy a `chain.pem` file containing just the node’s certificate. In this case, the peer’s trust store must already have all intermediate certificates that it needs to verify the node’s identity.

The following examples demonstrate both of these methods. They assume that you have already completed the steps in [Create and Deploy Cluster and Node Certificates](#root-and-node-certificates).

### [](#intermediate-concatenation)Deploy an Intermediate Certificate as Part of the Node’s Trust Chain

This example demonstrates creating root, node, intermediate, and client certificates. It Concatenates these certificates together so the node can provide the client a complete chain of trust.

1. Open a command line shell on the node for which you want to create a certificate signed by an intermediate certificate.
2. In some directory, such as your home directory or `/tmp`, create working directories:  
```console  
mkdir servercertfiles2  
cd servercertfiles2  
mkdir -p {root,servers,clients}/{issued,reqs,private}  
```  
You’ll use the `root`, `servers`, and `clients` directories to contain the certificates, requests, and private keys for the root, node, and client certificates. The `issued`, `reqs`, and `private` subdirectories in these directories will contain the final certificates, the signing requests, and the private keys respectively.

|  | The example [Client Access: Intermediate Certificate Authorization](configure-client-certificates.md#client-certificate-authorized-by-an-intermediate-certificate) uses this directory structure. It demonstrates creating the certificates that the clients need. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
3. Change to the `root` directory and create a configuration file for the root certificate:  
```console  
cd root  
cat > config <<EOF  
[req]  
distinguished_name = cn_only  
x509_extensions = ca_ext  
[ cn_only ]  
commonName = Common Name (eg: your user, host, or server name)  
commonName_max = 64  
commonName_default = CA  
[ca_ext]  
basicConstraints = CA:TRUE  
subjectKeyIdentifier = hash  
authorityKeyIdentifier = keyid:always,issuer:always  
keyUsage = cRLSign, keyCertSign  
EOF  
```  
The `config` file has three sections:

  * `[req]` specifies the values to pass to the `req` command. This command creates and processes certificate requests. To learn more about it and its arguments, use the command `man req`.
  * `[cn_only]` provides specifications for the Common Name to used in the certificate, including the maximum number of characters and the default name.
  * `[ca_ext]` provides basic extensions that limit the capability of the certificate. Some of the settings in this section are:

    * `basicConstraints CA:TRUE` makes the certificate capable of signing other certificates.
    * `keyUsage = cRLSign, keyCertSign` has two effect. The `cRLSign` value prevents the certificate’s public key from being able to verify signatures on Certificate Revocation Lists. And `keyCertSign` makes the certificate’s public key able to verify signatures on other certificates.
4. Create the root certificate, passing in the `config` file you just created:  
```console  
openssl req -config config -new -x509 -days 3650 -sha256 -newkey rsa:2048 \
    -keyout ca.key -out ca.pem -subj '/C=UA/O=MyCompany/CN=RootCA'  
```  
This command creates both the root certificate for the cluster in a file named `ca.pem` file, and the private key in a file named `ca.key`. The `-keyout` argument tells `openssl` to password protect the private key. When executing the command, `openssl` prompts you for a pass phrase:  
```console  
Generating a 2048 bit RSA private key  
....+++  
...................+++  
writing new private key to 'ca.key'  
Enter PEM pass phrase:  
```  
Anyone trying to use the certificate’s private key must enter this passphrase.
5. Create an extensions file to limit the capabilities of the intermediate certificate that you create in the next step:  
```console  
cat > int.ext <<EOF  
basicConstraints = CA:TRUE  
subjectKeyIdentifier = hash  
authorityKeyIdentifier = keyid:always,issuer:always  
keyUsage = cRLSign, keyCertSign  
EOF  
```  
As with the root certificate configuration, this configuration’s `basicConstraints` setting allows the intermediate certificate to sign other certificates. Its `keyUsage` setting also allows the certificate’s public key to verify its signature on other certificates.
6. Create a private key and a corresponding certificate signing request for the intermediate certificate:  
```console  
openssl req -new -sha256 -newkey rsa:2048 -keyout ../servers/int.key \
    -out reqs/server-signing.csr \
    -subj '/C=UA/O=MyCompany/OU=Servers/CN=ServerSigningCA'  
```  
Again, the command requires `openssl` to password protect the private key, so it prompts you twice for a pass phrase.  
The command outputs the encrypted private key in `servers/int.key` and a signing request in `root/req/server-signing.csr`.
7. Create the intermediate certificate signed by the root certificate `ca.pem` and its key `ca.key`, to establish the intermediate certificate’s authority:  
```console  
openssl x509 -CA ca.pem -CAkey ca.key -CAcreateserial \
    -CAserial serial.srl -days 3650 -req -in reqs/server-signing.csr \
    -out issued/server-signing.pem -extfile int.ext  
```  
`openssl` prompts you for the pass phrase for the `ca.key` private key because you password-protected it in an earlier step. The command saves the intermediate certificate as `issued/server-signing.pem`.
8. Make a copy of the intermediate certificate to use as the authority for the node certificates that you create in later steps.  
```console  
cp issued/server-signing.pem ../servers/int.pem  
```
9. Within the `../servers` directory, create an extension file containing the information that’s common across all nodes in the cluster.  
```console  
cd ../servers  
cat > server.ext <<EOF  
basicConstraints = CA:FALSE  
subjectKeyIdentifier = hash  
authorityKeyIdentifier = keyid,issuer:always  
extendedKeyUsage = serverAuth  
keyUsage = digitalSignature,keyEncipherment  
EOF  
```  
Some of the important values in this extension file are:

  * `extendedKeyUsage = serverAuth` limits the purpose of the certificate to server authentication.
  * `keyUsage` value `digitalSignature` specifies that the certificate’s public key can be used in the verifying of information-origin. The `keyEncipherment` value allows the public key to encrypt symmetric keys.
10. Generate the private key for the node.  
```console  
openssl genrsa -out private/couchbase.node.svc.key 2048  
```
11. Generate a certificate signing request for the node’s certificate.  
```console  
openssl req -new -key private/couchbase.node.svc.key \
    -out reqs/couchbase.node.svc.csr \
    -subj "/C=UA/O=MyCompany/OU=Servers/CN=couchbase.node.svc"  
```
12. Create a copy of the file containing the certificate extensions and append a setting specific to the node.  
```console  
cp server.ext temp.ext  
echo 'subjectAltName = IP:10.143.192.102' >> temp.ext  
```  
The newly created `temp.ext` file adds the node’s IP address as a Subject Alternative Name to the certificate. In Couchbase Enterprise Server Version 7.2 and later, you must add a Subject Alternative Name to the certifcate which indentifies the node. If the certificate’s Subject Alternative Name does not match the node’s identity in the cluster, Enterprise Analytics returns an error if you try to load the certificate. For information and options, see [Server Certificate Validation](../../../../server/current/learn/security/certificates.md#server-certificate-validation).
13. Create the node certificate for the node by signing the certification request you just created using the intermediate certificate:  
```console  
openssl x509 -CA int.pem -CAkey int.key -CAcreateserial \
    -CAserial serial.srl -days 365 -req -in reqs/couchbase.node.svc.csr \
    -out issued/couchbase.node.svc.pem -extfile temp.ext  
```  
Because you’re using the intermediate certificate in this signing request, `openssl` prompts you to enter the pass phrase for the intermediate certificate’s private key.  
The command creates the node’s certificate as the file `issued/couchbase.node.svc.pem`
14. Check that the node certificate is valid. The following use of the `openssl` command verifies the relationship between the root certificate, the intermediate certificate, and the node certificate.  
```console  
openssl verify -trusted ../root/ca.pem -untrusted int.pem \  
    issued/couchbase.node.svc.pem  
```  
The command outputs the following if the certificate passes the validity check:  
issued/couchbase.node.svc.pem: OK
15. Prepare the node’s certificate for upload by creating the `chain.pem` certificate file. You create `chain.pem` by concatenating the node certificate and the intermediate certificate to establish the chain of authority. Enterprise Analytics expects the node’s certificate file to be named `chain.pem`.  
```console  
cat issued/couchbase.node.svc.pem int.pem > chain.pem  
```
16. Create a copy of the node’s private key named `pkey.key` for deployment to the node. Enterprise Analytics expects the node’s private key to have this filename.  
```console  
cp private/couchbase.node.svc.key pkey.key  
```
17. Move the node certificate and node private key into the `inbox` directory for the current node.  
```console  
sudo mkdir /opt/enterprise-analytics/var/lib/couchbase/inbox/  
/opt/enterprise-analytics/var/lib/couchbase/inbox/chain.pem  
/opt/enterprise-analytics/var/lib/couchbase/inbox/pkey.key  
```
18. Move the root certificate into the `inbox/CA` directory for the current node.  
```console  
sudo mkdir /opt/enterprise-analytics/var/lib/couchbase/inbox/CA  
cd ../root  
sudo cp ca.pem /opt/enterprise-analytics/var/lib/couchbase/inbox/*  
```
19. Make all certificate and private key files in the `inbox` readable by the `couchbase` user.  
```console  
sudo chown -R couchbase /opt/enterprise-analytics/var/lib/couchbase/inbox/*  
sudo chmod -R 0700 /opt/enterprise-analytics/var/lib/couchbase/inbox/*  
```
20. Upload the root certificate, activating it for the entire cluster.  
```console  
curl -X POST http://10.143.192.102:8091/node/controller/loadTrustedCAs \
     -u Administrator:password  
```
21. Upload the node certificate.  
```console  
curl -X POST http://10.143.192.102:8091/node/controller/reloadCertificate \
    -u Administrator:password  
```

For more information using the REST API to manage certificates, see [Certificate Management API](../../reference/rest-certificate-management.md).

### [](#intermediate-upload)Deploy an Intermediate Certificate via Peer’s Trust Store

The following example creates an intermediate certificate but does not concatenate it with the node’s certificate. After following these steps, any peer attempting to make a secure TLS connection to the node must have the intermediate certificate in its trust store. These peers include clients making secure connections and other nodes in the Enterprise Analytics cluster. Adding the intermediate certificate to the peer’s trust store makes sure the peer can establish a chain of trust from the node’s certificate to a CA that it trusts.

1. Perform all steps listed in the section [Deploy an Intermediate Certificate as Part of the Node’s Chain](#intermediate-concatenation) up to and including step #14, [Check that the node certificate is valid](#check-validity).
2. Prepare to deploy the certificate and private key for the node, by renaming both:  
cp issued/couchbase.node.svc.pem chain.pem  
cp private/couchbase.node.svc.key pkey.key
3. Move the renamed node certificate and private key into the `inbox` for the current node.  
sudo mkdir /opt/enterprise-analytics/var/lib/couchbase/inbox/*  
sudo cp ./chain.pem /opt/enterprise-analytics/var/lib/couchbase/inbox/chain.pem  
sudo cp ./pkey.key /opt/enterprise-analytics/var/lib/couchbase/inbox/pkey.key
4. Move the root certificate and the intermediate certificate into the `inbox/CA` directory for the current node.  
sudo mkdir /opt/enterprise-analytics/var/lib/couchbase/inbox/CA/  # if needed  
sudo cp int.pem /opt/enterprise-analytics/var/lib/couchbase/inbox/CA/.  
cd ../root  
sudo cp ca.pem /opt/enterprise-analytics/var/lib/couchbase/inbox/CA/.
5. Make sure that all certificate and private key files in the `inbox` directory can be read by user `couchbase`.  
```console  
sudo chown -R couchbase /opt/enterprise-analytics/var/lib/couchbase/inbox/*  
sudo chmod -R 0700 /opt/enterprise-analytics/var/lib/couchbase/inbox/*  
```
6. Upload the root and intermediate certificates.  
```console  
curl -X POST http://10.143.192.102:8091/node/controller/loadTrustedCAs \
     -u Administrator:password  
```
7. Upload the node certificate.  
```console  
curl -X POST http://10.143.192.102:8091/node/controller/reloadCertificate
     -u Administrator:password  
```

|  | When the cluster contains more than one node, you must repeat the call to /node/controller/reloadCertificate for each node. Be sure to use the IP address of each node in the POST URL to have each node reload its certificates. Also, copy the files to the node’s inbox on its own filesystem. The files must be on the node for the REST API call to work. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

The node’s certificate is now deployed. Remember that it does not contain the intermediate certificate. For a peer to identify the node, it must have a copy of the intermediate certificate in its trust store. Without it, the peer cannot establish a chain of trust from the node to the root CA. To make sure other nodes in the cluster can identify the node, add the intermediate certificate to the Enterprise Analytics’s trust store. For other clients, consult their documentation to determine how to add the intermediate certificate to their trust stores.

For more information using the REST API to manage certificates, see [Certificate Management API](../../reference/rest-certificate-management.md).

## [](#pkcs12)Deploy a Certificate and Private Key to a Node in a PKCS #12 File

PKCS #12 format certificates let you bundle certificates, private keys, and other objects into a single file. Enterprise Analytics supports using PKCS #12 files for deploying certificates, private keys, and certificate chains for nodes. It does not support using them for other purposes, such as client or root certificates.

Enterprise Analytics requires that the PKCS #12 file be in the node’s `inbox` directory with the filename `couchbase.p12`.

The following example demonstrates how to bundle the node’s certificate and private key into a PKCS #12 file and deploy it on a node.

1. Follow steps 1 through 10 in the [Create and Deploy Cluster and Node Certificates](#root-and-node-certificates) example. When you complete these steps you’ll have certificates and private keys for the cluster and the node.
2. Bundle the node’s certificate and private key into a single PKCS #12 file:  
```console  
openssl pkcs12 -export -out couchbase.p12 -inkey private/couchbase.default.svc.key
        -in public/couchbase.default.svc.pem  
```  
The arguments in this command are:

  * `pkcs12` tells `openssl` you want to work with a PCKS #12 certificate.
  * `-export` tells `openssl` you want to create a new certificate.
  * `-out couchbase.p12` sets the output filename. The file is saved in the current directory with the name Enterprise Analytics expects for a PKCS #12 certificate.
  * `-inkey private/couchbase.default.svc.key` tells the command to import the node’s private key from the file you created earlier. It also has `openssl` password protect the private key.
  * `-in public/couchbase.default.svc.pem` tells the command where to find the node’s certificate.  
The command prompts you to enter a password for the private key twice.
3. If the node to which you’re deploying the certificate does not have an inbox directory, create it.  
```console  
sudo mkdir /opt/enterprise-analytics/var/lib/couchbase/inbox/  
```
4. Copy the PKCS #12 certificate to the node’s inbox:  
```console  
sudo cp couchbase.p12 /opt/enterprise-analytics/var/lib/couchbase/inbox/  
```  
Make sure there are no other certificate files in the `inbox` directory. If Enterprise Analytics finds both a `couchbase.p12` and `pkey.key` in the inbox directory, it cannot tell which file you intend to use for the certificate. In this case, it returns an error when you try to upload the certificate to the node.
5. Deploy the root certificate. Enterprise Analytics expects to find the root certificate in a subdirectory named `CA` in the `inbox` directory. Create the subdirectory and then copy the root CA file:  
```console  
sudo mkdir /opt/enterprise-analytics/var/lib/couchbase/inbox/CA  
sudo cp ./ca.pem /opt/enterprise-analytics/var/lib/couchbase/inbox/CA/.  
```
6. Make all files in the `inbox` directory readable by just the `couchbase` user:  
```console  
sudo chown -R couchbase /opt/enterprise-analytics/var/lib/couchbase/inbox/*  
sudo chmod -R 0700 /opt/enterprise-analytics/var/lib/couchbase/inbox/*  
```
7. Call the REST API to have Enterprise Analytics load the root certificate for the cluster:  
```console  
curl -X POST http://10.143.192.102:8091/node/controller/loadTrustedCAs -u Administrator:password  
```
8. Load the node certificate and its private key by calling the [reloadCertificate](../../reference/upload-retrieve-node-cert.md) REST API. Because an earlier step password protected the private key, you must pass the password for it as an argument to the REST API call:  
```console  
curl -X POST http://10.143.192.102:8091/node/controller/reloadCertificate \
     -u Administrator:password
     -d '{"privateKeyPassphrase": {"type": "plain", "password": "private-key-password"}}'  
```  
The JSON value you pass to the command supplies the password for the private key in the PKCS #12 certificate as plain text. Replace the `private-key-password` with the password you entered in step 2.

|  | This example sends the private key’s password in plaintext for simplicity. In a production environment, consider using a more secure method of sending this password. See [JSON Passphrase Registration](../../reference/upload-retrieve-node-cert.md#json-passphrase-registration) |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Enterprise Analytics extracts the private key and certificate from the `couchbase.p12` file and activates them on the node.

This example has the node’s certificate directly signed by the root certificate. If instead you need to use one or more intermediate certificates to sign the node’s certificate, you can choose to include them to establish a chain of trust. You can include a chain of intermediate certificates by adding a `-chain` argument to the `openssl` command in step 2\. See OpenSSL’s [openssl-pkcs12](https://www.openssl.org/docs/manmaster/man1/openssl-pkcs12.htmlp) documentation for documentation on `-chain` and other arguments.

## [](#encrypted-node-private-keys)Encrypted Node Private Keys

You can choose to encrypt the private key for nodes when uploading them. You must register the passphrase so that the key can be securely retrieved and used when required. See [Upload and Retrieve a Node Certificate](#reference/upload-retrieve-node-cert.adoc) for details.

## [](#configure-client-access-advanced)Configuring Client Access

Once you have configured root, intermediate, and node certificates for the cluster, you can create client certificates so clients can securely connect. You can choose to create an intermediate client certificate that itself inherits the authority of the root. Client-certificate preparation varies, depending on the type of client. For steps to prepare a client certificate to support connections between Enterprise Analytics databases, see [Client Access: Intermediate-Certificate Authorization](configure-client-certificates.md#client-certificate-authorized-by-an-intermediate-certificate). For steps to prepare a certificate for a Java client, see [Java Client Access: Intermediate-Certificate Authorization](configure-client-certificates.md#java-client-access-intermediate-certificate-authorization).

|  | Client connections secured by client certificate must be enabled on the cluster. See [Enable Client-Certificate Handling](enable-client-certificate-handling.md). |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#using-an-externally-provided-root-certificate)Using an Externally Provided Root Certificate

The examples in this page create a self-signed root certificate and use that certificate’s private key to sign other certificates. In production environments, you often want to use a node certificate signed by a well-known Certificate Authority. In this case, the CA provides the root, intermediate, and node certificates for you. The intermediate certificate is optional.

## [](#adding-new-nodes)Adding and Joining New Nodes

When a cluster uses the default auto-generated certificates, you do not need to generate a new certificate for new nodes. Once you configure the cluster to use custom certificates, you must generate a new certificate when adding or joining new nodes to the cluster. In Enterprise Analytics always adds or joins new nodes over an encrypted connection.

When a cluster using custom certificates adds or joins a new node to itself, the new node must interact with an existing node. This interaction requires both the existing node and new node verify each other’s identity using their chains of trust. The easiest way to make sure the nodes can identify each other by signing them with the same root certificate or the same intermediate certificate. Otherwise, make sure each node’s trust store contain the intermediate or CA that signed the other node’s certificate.

### [](#readding-a-previously-removed-node)Re-Adding Node

When you remove a node from a cluster, Enterprise Analytics deletes its configuration including its certificates chains. If you add the removed node back to the cluster, Enterprise Analytics adds it as a new node with a new configuration. Therefore, you must make sure node has the appropriate root certificate and chain certificate.

For more information about removing nodes, see [Removal](#learn:clusters-and-availability/removal.adoc).

## [](#regenerating-default-certificates)Regenerating Default Certificates

When it creates the cluster, Enterprise Analytics generates default certificates for the cluster and initial node. It also generates certificates for additional nodes you add later. You can have Enterprise Analytics regenerate the certificates using a the REST API call. This call has Enterprise Analytics generate a new self-signed root certificate and add it to its trust store. It then creates new node certificates signed by the new root certificate, overwriting existing node certificates. Any old auto-generated and custom root certificates remain in the cluster’s trust store.

For information about regenerating certificates, see [Regenerate All Certificates](../../reference/rest-regenerate-all-certs.md). For information about deleting root certificates, see [Delete Root Certificates](../../reference/delete-trusted-cas.md).

## [](#further-information)Further Information

For information about certificate-management using the REST API, see [ssl-manage](../../cli/couchbase-cli-ssl-manage.md) and [Certificate Management API](../../reference/rest-certificate-management.md).

For step-by-step instructions on creating client certificates, see [Configure Client Certificates](configure-client-certificates.md).