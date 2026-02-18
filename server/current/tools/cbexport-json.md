---
title: cbexport json
description: Exports JSON data from Couchbase
editUrl: https://github.com/couchbase/backup/edit/morpheus/docs/modules/tools/pages/cbexport-json.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/tools/cbexport-json.html)

# cbexport json

Exports JSON data from Couchbase

## [](#synopsis)SYNOPSIS

cbexport json [--cluster <url>] [--bucket <bucket_name>] [--format <data_format>]
              [--username <username>] [--password <password>] [--client-cert <path>]
              [--client-cert-password <password>] [--client-key <path>]
              [--client-key-password <password>] [--cacert <path>] [--no-ssl-verify]
              [--threads <num>] [--log-file <path>] [--include-key <key>]
              [--include-data <collection_string_list>]
              [--exclude-data <collection_string_list>] [--verbose]
              [--scope-field <scope_field>] [--collection-field <collection_field>]

## [](#description)DESCRIPTION

Exports JSON data from Couchbase. The cbexport-json command supports exporting JSON documents to a file with a document on each line or a file that contain a JSON list where each element is a document. The file format to export to can be specified with the --format flag. See the [DATASET FORMATS](#DATASET%5FFORMATS) section below for more details on the supported file formats.

Note that the `_system` scope is not exported by default. To do this use the `--include-data` flag.

## [](#options)OPTIONS

Below are a list of required and optional parameters for the cbexport-json command.

### [](#required)Required

\-c,--cluster <url>

The hostname of a node in the cluster to export data from. See the HOST FORMATS section below for details about hostname specification formats.

\-u,--username <username>

The username for cluster authentication. The user must have the appropriate privileges to export data.

\-p,--password <password>

The password for cluster authentication. The user must have the appropriate privileges to export data. If not password is supplied to this option then you will be prompted to enter your password.

\--client-cert <path>

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `--client-key` as an alternative to the `--username` and `--password` flags. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION)section for more information.

\--client-cert-password <password>

The password for the certificate provided to the `--client-cert` flag, when using this flag, the certificate/key pair is expected to be in the PKCS#12 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\--client-key <path>

The path to the client private key whose public key is contained in the certificate provided to the `--client-cert` flag. May be supplied with `--client-cert` as an alternative to the `--username` and `--password`flags. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\--client-key-password <password>

The password for the key provided to the `--client-key` flag, when using this flag, the key is expected to be in the PKCS#8 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\-b,--bucket <bucket\_name>

The name of the bucket to export data from.

\-f,--format <format>

The format of the dataset specified (lines or list). See the [DATASET FORMATS](#DATASET%5FFORMATS) section below for more details on the formats supported by cbexport.

\-o,--output <path>

The path to the location of the file that JSON documents from Couchbase should be exported to. This may be an absolute or relative path, but must point to a file. The file does not have to exist when the command is invoked.

### [](#optional)Optional

\--include-key <key>

Couchbase stores data as key value pairs where the value is a JSON document and the key is an identifier for retrieving that document. By default cbexport will only export the value portion of the document. If you wish to include the key in the exported document then this option should be specified. The value passed to this option should be the field name that the key is stored under. If the value passed already exists as a field in the document, it will be overridden with the key. If the JSON document is not an object it will be turned into one and the value added to a field named 'value'. If the key value passed is 'value' then the key will not be written. It will display a warning for any document it has converted into an object.

\--include-data <collection\_string\_list>

A comma separated list of collection strings to include when exporting from the bucket. Only scopes/collections included in this will be included in the output file. The expected format is `scope1.collection1,scope2.collection2`. This argument is mutually exclusive with `--exclude-data`.

\--exclude-data <collection\_string\_list>

A comma separated list of collection strings to exclude when exporting from the bucket. Any scopes/collections included in this list will not be included in the output file. The expected format is `scope1.collection1,scope2.collection2`. This argument is mutually exclusive with `--include-data`.

\--no-ssl-verify

Skips the SSL verification phase. Specifying this flag will allow a connection using SSL encryption, but will not verify the identity of the server you connect to. You are vulnerable to a man-in-the-middle attack if you use this flag. Either this flag or the --cacert flag must be specified when using an SSL encrypted connection.

\--cacert <cert\_path>

Specifies a CA certificate that will be used to verify the identity of the server being connecting to. Either this flag or the --no-ssl-verify flag must be specified when using an SSL encrypted connection.

\--scope-field <scope\_field>

When exporting from a collection aware cluster this field will be created in each JSON document; it will be used to store the name of the scope the document came from. This flag is required when exporting from a bucket that has non-default scopes and collections.

\--collection-field <collection\_field>

When exporting from a collection aware cluster this field will be created in each JSON document; it will be used to store the name of the collection the document came from. This flag is required when exporting from a bucket that has non-default scopes and collections.

\-t,--threads <num>

Specifies the number of concurrent clients to use when exporting data. Fewer clients means exports will take longer, but there will be less cluster resources used to complete the export. More clients means faster exports, but at the cost of more cluster resource usage. This parameter defaults to 1 if it is not specified and it is recommended that this parameter is not set to be higher than the number of CPUs on the machine where the export is taking place.

\-l,--log-file <path>

Specifies a log file for writing debugging information about cbexport execution.

\-v,--verbose

Specifies that logging should be sent to stdout. If this flag is specified along with the -l/--log-file option then the verbose option is ignored.

## [](#HOST%5FFORMATS)HOST FORMATS

When specifying a host/cluster for a command using the `-c`/`--cluster` flag, the following formats are accepted:

* `<addr>:<port>`
* `http://<addr>:<port>`
* `https://<addr>:<port>`
* `couchbase://<addr>:<port>`
* `couchbases://<addr>:<port>`
* `couchbase://<srv>`
* `couchbases://<srv>`
* `<addr>:<port>,<addr>:<port>`
* `<scheme>://<addr>:<port>,<addr>:<port>`

The `<port>` portion of the host format may be omitted, in which case the default port will be used for the scheme provided. For example, `http://` and `couchbase://` will both default to 8091 where `https://` and `couchbases://` will default to 18091\. When connecting to a host/cluster using a non-default port, the `<port>` portion of the host format must be specified.

### [](#connection-strings-multiple-nodes)Connection Strings (Multiple nodes)

The `-c`/`--cluster` flag accepts multiple nodes in the format of a connection string; this is a comma separated list of `<addr>:<port>` strings where `<scheme>` only needs to be specified once. The main advantage of supplying multiple hosts is that in the event of a failure, the next host in the list will be used.

For example, all of the following are valid connection strings:

* `localhost,[::1]`
* `10.0.0.1,10.0.0.2`
* `http://10.0.0.1,10.0.0.2`
* `https://10.0.0.1:12345,10.0.0.2`
* `couchbase://10.0.0.1,10.0.0.2`
* `couchbases://10.0.0.1:12345,10.0.0.2:12345`

### [](#srv-records)SRV Records

The `-c`/`--cluster` flag accepts DNS SRV records in place of a host/cluster address where the SRV record will be resolved into a valid connection string. There are a couple of rules which must be followed when supplying an SRV record which are as follows:

* The `<scheme>` portion must be either `couchbase://` or `couchbases://`
* The `<srv>` portion should be a hostname with no port
* The `<srv>` portion must not be a valid IP address

For example, all of the following are valid connection string using an SRV record:

* `couchbase://hostname`
* `couchbases://hostname`

### [](#alternate-addressing-caok8s)Alternate Addressing (CAO/K8S)

Users of the CAO (Couchbase Autonomous Operator) or K8S may need to supply the `network=external` query parameter to force connection via the defined alternate addressing.

For example, the following are valid connection strings:

* `https://10.0.0.1:12345,10.0.0.2?network=default`
* `https://10.0.0.1:12345,10.0.0.2?network=external`

## [](#CERTIFICATE%5FAUTHENTICATION)CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)

This tool supports authenticating against a Couchbase Cluster by using certificate based authentication (mTLS authentication). To use certificate based authentication a certificate/key must be supplied, there a currently multiple ways this may be done.

### [](#pem-encoded-certificatekey)PEM ENCODED CERTIFICATE/KEY

An unencrypted PEM encoded certificate/key may be supplied by using: - `--client-cert <path>`\- `--client-key <path>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

The file passed to `--client-key` must contain at most one private key, the key can be in one of the following formats:

* PKCS#1
* PKCS#8
* EC

Currently, only the following key types are supported:

* RSA
* ECDSA
* ED25519

### [](#pem-encoded-certificatepem-or-der-encrypted-pkcs8-key)PEM ENCODED CERTIFICATE/PEM OR DER ENCRYPTED PKCS#8 KEY

An encrypted PKCS#8 formatted key may be provided using:

* `--client-cert <path>`
* `--client-key <path>`
* `--client-key-password <password>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

Currently, only the following key types are supported:

* RSA
* ECDSA
* ED25519

### [](#encrypted-pkcs12-certificatekey)ENCRYPTED PKCS#12 CERTIFICATE/KEY

An encrypted PKCS#12 certificate/key may be provided using:

* `--client-cert <path>`
* `--client-cert-password <password>`

The file passed to `--client-cert` must contain the client certificate and exactly one private key. It may also contain the chain required to authenticate the client certificate.

Currently, only the following key types are supported:

* RSA
* ECDSA
* ED25519

## [](#DATASET%5FFORMATS)DATASET FORMATS

The cbexport command supports the formats listed below.

### [](#lines)LINES

The lines format specifies a file that contains one JSON document on every line in the file. This format is specified by setting the --format option to "lines". Below is an example of a file in lines format.

{"key": "mykey1", "value": "myvalue1"}
{"key": "mykey2", "value": "myvalue2"}
{"key": "mykey3", "value": "myvalue3"}
{"key": "mykey4", "value": "myvalue4"}

### [](#list)LIST

The list format specifies a file which contains a JSON list where each element in the list is a JSON document. The file may only contain a single list, but the list may be specified over multiple lines. This format is specified by setting the --format option to "list". Below is an example of a file in list format.

[
  {
    "key": "mykey1",
    "value": "myvalue1"
  },
  {"key": "mykey2", "value": "myvalue2"},
  {"key": "mykey3", "value": "myvalue3"},
  {"key": "mykey4", "value": "myvalue4"}
]

## [](#examples)EXAMPLES

To export data to /data/lines.json using the lines format and running with 4 threads the following command can be run.

$ cbexport json -c couchbase://127.0.0.1 -u Administrator -p password \
 -b default -o /data/lines.json -f lines -t 4

To export data to /data/list.json using the list format the following command can be run.

$ cbexport json -c couchbase://127.0.0.1 -u Administrator -p password \
 -b default -o /data/list.json -f list

To export data from a collections aware cluster with the scope and collection being added to the scope/collection field the following command can be run.

$ cbexport json -c couchbase://127.0.0.1 -u Administrator -p password \
 -b default -o /data/list.json -f list --scope-field scope --collection-field collection

[
  {
    "scope": "myscope1",
    "collection": "mycollection1",
    "key": "mykey1",
    "value": "myvalue1",
  }
]

## [](#environment-and-configuration-variables)ENVIRONMENT AND CONFIGURATION VARIABLES

CB\_CLUSTER

Specifies the hostname of the Couchbase cluster to connect to. If the hostname is supplied as a command line argument then this value is overridden.

CB\_USERNAME

Specifies the username for authentication to a Couchbase cluster. If the username is supplied as a command line argument then this value is overridden.

CB\_PASSWORD

Specifies the password for authentication to a Couchbase cluster. If the password is supplied as a command line argument then this value is overridden.

CB\_CLIENT\_CERT

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `CB_CLIENT_KEY` as an alternative to the `CB_USERNAME` and `CB_PASSWORD` variables. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION)section for more information.

CB\_CLIENT\_CERT\_PASSWORD

The password for the certificate provided to the `CB_CLIENT_CERT` variable, when using this variable, the certificate/key pair is expected to be in the PKCS#12 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

CB\_CLIENT\_KEY

The path to the client private key whose public key is contained in the certificate provided to the `CB_CLIENT_CERT` variable. May be supplied with `CB_CLIENT_CERT` as an alternative to the `CB_USERNAME` and `CB_PASSWORD`variables. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

CB\_CLIENT\_KEY\_PASSWORD

The password for the key provided to the `CB_CLIENT_KEY` variable, when using this variable, the key is expected to be in the PKCS#8 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

## [](#see-also)SEE ALSO

[cbimport-json](cbimport-json.md)

## [](#cbexport)CBEXPORT

Part of the [cbexport](cbexport.md) suite