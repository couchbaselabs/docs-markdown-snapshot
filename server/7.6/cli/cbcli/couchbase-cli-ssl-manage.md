---
title: ssl-manage
description: Manage SSL certificates
editUrl: https://github.com/couchbase/couchbase-cli/edit/trinity/docs/modules/cli/pages/cbcli/couchbase-cli-ssl-manage.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:cli:cbcli/couchbase-cli-ssl-manage.adoc[]
---

[View original HTML](/server/7.6/cli/cbcli/couchbase-cli-ssl-manage.html)

# ssl-manage

Manage SSL certificates

## [](#synopsis)SYNOPSIS

_couchbase-cli ssl-manage_ [--cluster <url>] [--username <user>] [--password <password>]
  [--client-cert <path>] [--client-cert-password <password>] [--client-key <path]
  [--client-key-password <password>]
  [--cluster-cert-info] [ --cluster-ca-info] [--cluster-ca-load] [--cluster-ca-delete <id>]
  [ --upload-cluster-ca <path> `**(deprecated)**`] [--node-cert-info] [--regenerate-cert <path>]
  [--set-node-certificate] [--pkey-passphrase-settings <path>] [--set-client-auth <path>]
  [--client-auth]

## [](#description)DESCRIPTION

This command allows users to manage their SSL and X.509 certificates.

## [](#options)OPTIONS

\-c

\--cluster

Specifies the hostname of a node in the cluster. See the HOST FORMATS section for more information on specifying a hostname.

\-u

\--username <username>

Specifies the username of the user executing the command. If you do not have a user account with permission to execute the command then it will fail with an unauthorized error.

\-p

\--password <password>

Specifies the password of the user executing the command. If you do not have a user account with permission to execute the command then it will fail with an unauthorized error. If this argument is specified, but no password is given then the command will prompt the user for a password through non-echoed stdin. You may also specify your password by using the environment variable CB\_REST\_PASSWORD.

\--client-cert <path>

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `--client-key` as an alternative to the `--username` and `--password` flags. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-cert-password <password>

The password for the certificate provided to the `--client-cert` flag, when using this flag, the certificate/key pair is expected to be in the PKCS#12 format. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-key <path>

The path to the client private key whose public key is contained in the certificate provided to the `--client-cert` flag. May be supplied with `--client-cert` as an alternative to the `--username` and `--password`flags. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-key-password <password>

The password for the key provided to the `--client-key` flag, when using this flag, the key is expected to be in the PKCS#8 format. See the CERTIFICATE AUTHENTICATION section for more information.

\--cluster-cert-info

Retrieves the cluster certificates and prints it to stdout.

\--cluster-ca-info

Retrieves the cluster certificates authorities and prints it to stdout.

\--cluster-ca-load

Tries to the certificate authority on every node in the cluster. Before running this command the certificate authority has to be copy to the install location at './inbox/CA' on a node in the cluster. Once loaded all nodes in the cluster will be able to view it.

\--cluster-ca-delete <id>

Deletes a certificate authority specified by the id.

\--node-cert-info

Retrieves the node certificate and prints it to stdout.

\--regenerate-cert <file>

Regenerates the cluster certificate and saves it to the file specified in the value of this option.

\--set-node-certificate

Sets the node certificate. Before running this command you must copy the node certificate into your installation. When this command is invoked the cluster will read the node certificate from the node specified and set it as the node certificate for that node.

\--pkey-passphrase-settings <path>

The path to a JSON file containing the private key passphrase settings, see below for examples for the accepted configurations.

When sending a plain text password, the file may look something like the one below. Note that plain passphrases will be encrypted with secret management when arrives to the server, but will be transmitted unencrypted (unless HTTPS is used)

{
  "type": "plain",
  "password": "asdasd"
}

When using a script, the file might look similar to the below. Note that the node will verify that the script is present, and that script is located in data/scripts directory.

{
  "type": "script",
  "path": "<path to script>",
  "args": [
    "arg1",
    "arg2"
  ],
  "trim": "false",
  "timeout": 5000
}

When using a REST call to fetch the password, the file may look similar to the one below.

{
  "type": "rest",
  "url": "<url to call>",
  "addressFamily": "inet6",
  "httpsOpts": {
    "verifyPeer": true
  },
  "timeout": 5000
}

\--upload-cluster-ca <file>

Uploads the certificate specified to the cluster. The uploaded certificate will replace the cluster certificate in this cluster.

> [!WARNING]
> For security reasons, this method has been deprecated in Couchbase Server 7.1 and later.

\--set-client-auth <path>

Specifies a path to the client auth configuration file. This file should contain the state of client auth and one or more prefixes. The state defines whether or not client auth should used. The possible values for this field are below:

* disabled: no client certification
* enable: if the client presents a valid client certificate then we try and validate it. If the validation fails or no certificate is presented we fall back to the existing authentication methods
* mandatory: the client has to present valid SSL certificate in order to access successfully authorize the connection.

The prefixes section should contain one or more prefixes and each prefix should contain a path, prefix, and delimiter. More information about these sub-fields is below:

* path: The field which will be used to extract the username from the certificate. Currently only `subject.cn`, `san.uri`, `san.email` and `san.dnsname` are allowed
* prefix: Optional. Prefix to be ignored from the field value
* delimiter: Optional. The delimiter can either be a string or a character, the parsing of the username ends when the delimiter value is found.

Below is an example of what a client auth configuration file might look like:

  {
    "state": "enable",
    "prefixes": [
      {
        "path": "subject.cn",
        "prefix": "www.cb-",
        "delimiter": "."
      }
    ]
  }

\--client-auth

This options used to get the client cert auth value

## [](#host-formats)HOST FORMATS

When specifying a host for the couchbase-cli command the following formats are expected:

* `couchbase://<addr>` or `couchbases://<addr>`
* `http://<addr>:<port>` or `https://<addr>:<port>`
* `<addr>:<port>`

It is recommended to use the couchbase://<addr> or couchbases://<addr> format for standard installations. The other formats allow an option to take a port number which is needed for non-default installations where the admin port has been set up on a port other that 8091 (or 18091 for https).

## [](#certificate-authentication-mtls-authentication)CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)

This tool supports authenticating against a Couchbase Cluster by using certificate based authentication (mTLS authentication). To use certificate based authentication a certificate/key must be supplied, there a currently multiple ways this may be done.

### [](#pem-encoded-certificatekey)PEM ENCODED CERTIFICATE/KEY

An unencrypted PEM encoded certificate/key may be supplied by using: - `--client-cert <path>`\- `--client-key <path>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

The file passed to `--client-key` must contain at most one private key, the key can be in one of the following formats: - PKCS#1 - PKCS#8

Currently, only the following key types are supported: - RSA - DSA

### [](#pem-encoded-certificatepem-or-der-encrypted-pkcs8-key)PEM ENCODED CERTIFICATE/PEM OR DER ENCRYPTED PKCS#8 KEY

An encrypted PKCS#8 formatted key may be provided using: - `--client-cert <path>`\- `--client-key <path>`\- `--client-key-password <password>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

Currently, only the following key types are supported: - RSA - DSA

### [](#encrypted-pkcs12-certificatekey)ENCRYPTED PKCS#12 CERTIFICATE/KEY

An encrypted PKCS#12 certificate/key may be provided using: - `--client-cert <path>`\- `--client-cert-password <password>`

The file passed to `--client-cert` must contain the client certificate and exactly one private key. It may also contain the chain required to authenticate the client certificate.

Currently, only the following key types are supported: - RSA - DSA

## [](#examples)EXAMPLES

To get cluster certificate information run the following command.

$ couchbase-cli ssl-manage -c 192.168.1.5 -u Administrator \
 -p password --cluster-cert-info

To get node certificate information run the following command. Note that the node certificate will be from the node specified by the -c option.

$ couchbase-cli ssl-manage -c 192.168.1.5 -u Administrator \
 -p password --node-cert-info

To automatically regenerate the cluster certificate and save the new certificate to a file at /root/new\_cluster.cert run the following command.

$ couchbase-cli ssl-manage -c 192.168.1.5 -u Administrator \
 -p password --regenerate-cert /root/new_cluster.cert

Note that the command above should never be run if you are using X.509 certificates because using the --regenerate-cert command will generate an unsigned certificate for the cluster to use.

To update a node certificate you will first need to copy the new certificate to the certificate inbox folder on the node you wish to change the certificate. Once you have done this you can run the command below to tell the server to begin using the new certificate.

$ couchbase-cli ssl-manage -c 192.168.1.5 -u Administrator \
 -p password --set-node-certificate

To update the cluster certificate you can run the command below. Note that our certificate is located at /root/new\_cluster.cert in this example.

$ couchbase-cli ssl-manage -c 192.168.1.5 -u Administrator \
 -p password --upload-cluster-ca /root/new_cluster.cert

To set the client cert auth to mandatory, following command can be run.

$ couchbase-cli ssl-manage -c 192.168.1.5 -u Administrator \
 -p password --set-client-auth mandatory

To get the client cert auth value, following command should be run.

$ couchbase-cli ssl-manage -c 192.168.1.5 -u Administrator \
 -p password --client-auth

To view all certificate authorities

$ couchbase-cli ssl-manage -c 192.168.1.5 -u Administrator \
 -p password --cluster-ca-info

To delete certificate authority with ID 1

$ couchbase-cli ssl-manage -c 192.168.1.5 -u Administrator \
 -p password --cluster-ca-delete 1

## [](#environment-and-configuration-variables)ENVIRONMENT AND CONFIGURATION VARIABLES

CB\_REST\_USERNAME

Specifies the username to use when executing the command. This environment variable allows you to specify a default argument for the -u/--username argument on the command line.

CB\_REST\_PASSWORD

Specifies the password of the user executing the command. This environment variable allows you to specify a default argument for the -p/--password argument on the command line. It also allows the user to ensure that their password are not cached in their command line history.

CB\_CLIENT\_CERT

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `CB_CLIENT_KEY` as an alternative to the `CB_USERNAME` and `CB_PASSWORD` variables. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_CERT\_PASSWORD

The password for the certificate provided to the `CB_CLIENT_CERT` variable, when using this variable, the certificate/key pair is expected to be in the PKCS#12 format. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_KEY

The path to the client private key whose public key is contained in the certificate provided to the `CB_CLIENT_CERT` variable. May be supplied with `CB_CLIENT_CERT` as an alternative to the `CB_USERNAME` and `CB_PASSWORD`variables. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_KEY\_PASSWORD

The password for the key provided to the `CB_CLIENT_KEY` variable, when using this variable, the key is expected to be in the PKCS#8 format. See the CERTIFICATE AUTHENTICATION section for more information.

## [](#see-also)SEE ALSO

[cluster-edit](couchbase-cli-cluster-edit.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite