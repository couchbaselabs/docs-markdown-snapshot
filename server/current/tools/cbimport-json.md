---
title: cbimport json
description: Imports JSON data into Couchbase
editUrl: https://github.com/couchbase/backup/edit/morpheus/docs/modules/tools/pages/cbimport-json.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/tools/cbimport-json.html)

# cbimport json

Imports JSON data into Couchbase

## [](#synopsis)SYNOPSIS

cbimport json [--cluster <url>] [--bucket <bucket_name>] [--dataset <path>]
              [--format <data_format>] [--username <username>] [--password <password>]
              [--client-cert <path>] [--client-cert-password <password>]
              [--client-key <path>] [--client-key-password <password>]
              [--generate-key <key_expr>] [--cacert <path>] [--no-ssl-verify]
              [--threads <num>] [--error-log <path>] [--log-file <path>] [--verbose]
              [--ignore-fields <fields>] [--field-delimiter <char>]
              [--generator-delimiter <char>] [--bucket-quota <quota>]
              [--scope-collection-exp <scope_collection_expression>]
              [--bucket-replicas <replicas>] [--eviction-policy <eviction_policy>]

## [](#description)DESCRIPTION

Imports JSON data into Couchbase. The cbimport command supports files that have a JSON document on each line, files that contain a JSON list where each element is a document, and the internal Couchbase Samples format. The file format can be specified with the --format flag. See the [DATASET FORMATS](#DATASET%5FFORMATS) section below for more details on the supported file formats.

The cbimport command also supports custom key-generation for each document in the imported file. Key generation is done with a combination of pre-existing fields in a document and custom generator functions supplied by cbimport. See the KEY GENERATION section below for details about key generators.

## [](#options)OPTIONS

Below are a list of required and optional parameters for the cbimport command.

### [](#required)Required

\-c,--cluster <url>

The hostname of a node in the cluster to import data into. See the HOST FORMATS section below for details about hostname specification formats.

\-u,--username <username>

The username for cluster authentication. The user must have the appropriate privileges to import data.

\-p,--password <password>

The password for cluster authentication. The user must have the appropriate privileges to import data. If not password is supplied to this option then you will be prompted to enter your password.

\--client-cert <path>

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `--client-key` as an alternative to the `--username` and `--password` flags. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION)section for more information.

\--client-cert-password <password>

The password for the certificate provided to the `--client-cert` flag, when using this flag, the certificate/key pair is expected to be in the PKCS#12 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\--client-key <path>

The path to the client private key whose public key is contained in the certificate provided to the `--client-cert` flag. May be supplied with `--client-cert` as an alternative to the `--username` and `--password`flags. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\--client-key-password <password>

The password for the key provided to the `--client-key` flag, when using this flag, the key is expected to be in the PKCS#8 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\-b,--bucket <bucket\_name>

The name of the bucket to import data into.

\-d,--dataset <uri>

The URI of the dataset to be loaded. cbimport supports loading data from a local file or from a URL. When importing data from a local file the path must be prefixed with file://. When importing data from a URL `--http-cache-directory` must be set; the dataset is downloaded to this cache directory. Note that this file is not cleaned up by `cbimport`.

\-f,--format <format>

The format of the dataset specified (lines, list, sample). See the [DATASET FORMATS](#DATASET%5FFORMATS) section below for more details on the formats supported by cbimport.

### [](#optional)Optional

\-g,--generate-key <key\_expr>

Specifies a key expression used for generating a key for each document imported. This parameter is required for list and lines formats, but not for the sample format. See the KEY GENERATION section below for more information on specifying key generators. If the resulting key is not unique the values will be overridden, resulting in fewer documents than expected being imported. To ensure that the key is unique add #MONO\_INCR# or #UUID# to the key generator expression.

\--field-delimiter <char>

Specifies the character to be used to denote field references in the key generator expression. It defaults to %. See the [KEY GENERATORS](#KEY%5FGENERATORS) section.

\--generator-delimiter <char>

Specifies the character to be used to denote generator references in the key generator expression. It defaults to #. See the [KEY GENERATORS](#KEY%5FGENERATORS) section.

\--no-ssl-verify

Skips the SSL verification phase. Specifying this flag will allow a connection using SSL encryption, but will not verify the identity of the server you connect to. You are vulnerable to a man-in-the-middle attack if you use this flag. Either this flag or the --cacert flag must be specified when using an SSL encrypted connection.

\--cacert <cert\_path>

Specifies a CA certificate that will be used to verify the identity of the server being connecting to. Either this flag or the --no-ssl-verify flag must be specified when using an SSL encrypted connection.

\--limit-docs <num>

Specifies that the utility should stop loading data after reading a certain amount of docs from the dataset. This option is useful when you have a large dataset and only want to partially load it.

\--skip-docs <num>

Specifies that the utility should skip some docs before we start importing data. If this flag is used together with the --limit-docs flag then we will import the number of documents specified by --limit-docs after we have skipped the rows specified by --skip-docs.

\--scope-collection-exp <scope\_collection\_expression>

When importing to a collection aware cluster you may optionally choose to provide a scope/collection expression which will be used to determine which scope/collection to insert the imported document in. This flag closely resembles the behavior/syntax of the `--generate-key` flag. For example, to use a static scope/collection use `--scope-collection-exp scope.collection`. To use information from the JSON document, specify the column name between `%` characters. For example, `--scope-collection-exp %scope_field%.%collection_field%`. Fields that contain a `%` character may be escaped using `%%`. For more information about the accepted format, see the [SCOPE/COLLECTION PARSER](#SCOPE%5FCOLLECTION%5FPARSER) section.

\-t,--threads <num>

Specifies the number of concurrent clients to use when importing data. Fewer clients means imports will take longer, but there will be less cluster resources used to complete the import. More clients means faster imports, but at the cost of more cluster resource usage. This parameter defaults to 1 if it is not specified and it is recommended that this parameter is not set to be higher than the number of CPUs on the machine where the import is taking place.

\-e,--errors-log <path>

Specifies a log file where JSON documents that could not be loaded are written to. A document might not be loaded if a key could not be generated for the document or if the document is not valid JSON. The errors file is written in the "lines" format (one document per line).

\-l,--log-file <path>

Specifies a log file for writing debugging information about cbimport execution.

\-v,--verbose

Specifies that logging should be sent to stdout. If this flag is specified along with the -l/--log-file option then the verbose option is ignored.

\--ignore-fields <fields>

Specify a comma separated list of field names that will be excluded from the imported document. The field reference syntax is the same as the one used in KEY GENERATORS to refer to fields.

\--disable-bucket-config

Disables modifying the bucket config stopping import from changing the memory quota/replica number. The bucket config related options may still be supplied, but will be ignored unless the bucket is created due to it not already existing (sensible defaults for those flags apply). This flag may be used to disable bucket modification, but fallback to bucket creation in the event the bucket does not exist.

\--bucket-quota <quota>

When importing a sample dataset using `--format sample` this argument will set the memory quota for the sample bucket. Note that this will edit the bucket settings if the bucket already exists, and will create it if it doesn’t.

\--bucket-replicas <replicas>

When importing a sample dataset using `--format sample` this argument will set the number of replicas for the sample bucket. Note that this will edit the bucket settings if the bucket already exists, and will create it if it doesn’t.

\--http-cache-directory <path>

The directory used to store files when the `--dataset` flag uses the 'http(s)://' scheme; this avoids re-downloading the files when running multiple imports.

\--eviction-policy <eviction\_policy>

The eviction policy to use when creating a bucket. Accepts either `fullEviction` or `valueOnly`. Note that only the sample format can create buckets so providing this flag when using the list or lines format will exit with an error.

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

The cbimport command supports the formats listed below.

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

### [](#sample)SAMPLE

It’s not recommended to use the sample format to import data outside of official samples created by Couchbase because the functionality has some additional restrictions.

To import a directory or ZIP file containing a file per-document some pre-processing is required. For example, the following command will convert all JSON files in the given directory into a single `lines.json` file that can be imported by `cbimport`.

$ awk '{ print $0 }' directory/*.json | jq -c >> lines.json
$ cbimport json --format lines -c couchbase://127.0.0.1 -u Administrator -p password -b travel-sample -d file://lines.json --generate-key '%id%'

This method is recommended over using `--format sample` because arguments such as `--generate-key` are supported.

## [](#KEY%5FGENERATORS)KEY GENERATORS

Key generators are used in order to generate a key for each document loaded. Keys can be generated by using a combination of characters, the values of a given field in a document, and custom generators. Field substitutions are done by wrapping the field name in "%" and custom generators are wrapped in "#". Below is an example of a key generation expression.

Given the document:

{
  "name": "alice",
  "age": 40,
  "address": {
    "street": "Broadway",
    "country": "USA"
  }
}

Key Generator Expression:

  --generate-key key::%name%::#MONO_INCR#

The following key would be generated:

  key::alice::1

In the example above we generate a key using both the value of a field in the document and a custom generator. We use the "name" field to use the value of the name field as part of the key. This is specified by "%name%" which tells the key generator to substitute the value of the field "name" into the key. To reference a nested field we would use "parent.child" syntax. For example to reference the country we would use '%address.country%'. To reference a field that contains a dot in the name we escape the string using \`\` . For example '%\`address.country\`%' refers to a field named "address.country".

This example also contains a generator function MONO\_INCR which will increment by 1 each time the key generator is called. Since this is the first time this key generator was executed it returns 1\. If we executed the key generator again it would return 2 and so on. The starting value of the MONO\_INCR generator is 1 by default, but it can be changed by specifying a number in brackets after the MONO\_INCR generator name. To start generating monotonically incrementing values starting at 100 for example, the generator MONO\_INCR\[100\] would be specified. The cbimport command current contains a monotonic increment generator (MONO\_INCR) and a UUID generator (UUID).

Any text that isn’t wrapped in "%" or "#" is static text and will be in the result of all generated keys. If a key needs to contain a "%" or "#" in static text then they need to be escaped by providing a double "%" or "#" (ex. "%%" or "##"). The delimiter characters can be changed to avoid having to escape them by using the --field-delimiter and --generator-delimiter flags.

If a key cannot be generated because the field specified in the key generator is not present in the document then the key will be skipped. To see a list of document that were not imported due to failed key generation users can specify the --errors-log <path> parameter to dump a list of all documents that could not be imported to a file.

## [](#SCOPE%5FCOLLECTION%5FPARSER)SCOPE/COLLECTION PARSER

Scope/collection parsers are used in order to determine which scope/collection to insert documents into. There are currently two supported parsers text/field.

Given the JSON dataset:

[
  {"product": "apple", "stock": 100, "type": "produce", "subtype": "fruit"}
]

Scope/collection expression:

--scope-collection-exp %type%.%subtype%

The document would be inserted into the 'fruit' collection inside the 'produce' scope.

Given the JSON dataset:

[
  {"fname": "alice", "age": 40},
  {"fname": "barry", "age": 36}
]

Scope/collection expression:

--scope-collection-exp uk.manchester

In this case, no fields in the document will be used to determine the scope or collection; all the documents would be inserted into the 'manchester' collection inside the 'uk' scope.

There is nothing stopping the mixture of text/field expressions the following are all valid expressions.

uk.%city%
uk.%city%-5
%country%.%city%::%town%

## [](#examples)EXAMPLES

In the examples below we will show examples for importing data from the files below.

./data/lines.json

  {"name": "alice", "age": 37}
  {"name": "bob", "age": 39}

./data/list.json

  [
    {"name": "candice", "age": 42},
    {"name": "daniel", "age": 38}
  ]

To import data from /data/lines.json using a key containing the "name" field and utilizing 4 threads the following command can be run.

$ cbimport json -c couchbase://127.0.0.1 -u Administrator -p password \
 -b default -d file:///data/lines.json -f lines -g key::%name% -t 4

To import data from /data/list.json using a key containing the "name" field and the UUID generator the following command would be run.

$ cbimport json -c couchbase://127.0.0.1 -u Administrator -p password \
 -b default -d file:///data/list.json -f list -g key::%name%::#UUID# -t 4

To import data from /data/list.json using a key containing the "name" field and then a unique id separated by a # we could use the --generator-delimiter flag to avoid escaping the # sign. An example would be:

$ cbimport json -c couchbase://127.0.0.1 -u Administrator -p password \
 -b default -d file:///data/list.json -f list --generator-delimiter '£' \
 -g key::%name%#£UUID£ -t 4

If the dataset in not available on the local machine where the command is run, but is available via an HTTP URL we can still import the data using cbimport. If we assume that the data is located at <http://data.org/list.json> and that the dataset is in the JSON list format then we can import the data with the command below.

$ cbimport json -c couchbase://127.0.0.1 -u Administrator -p password \
 -b default -d http://data.org/list.json -f list -g key::%name%::#UUID# -t 4

If the JSON dataset contains information which would allow importing into scopes/collections then a command like the one below could be used.

[{"product": "apple", "stock": 100, "type": "produce", "subtype": "fruit"}]

$ cbimport json -c couchbase://127.0.0.1 -u Administrator -p password
 -b default -d file://data/list.csv -f list -g %product%
 --scope-collection-exp %type%.%subtype%

This command would place the document into the fruit collection inside the produce scope.

$ cbimport json -c couchbase://127.0.0.1 -u Administrator -p password
 -b default -d http://example.com/data/list.json -f list -g %product%
 --scope-collection-exp %type%.%subtype% --http-cache-directory /tmp

This command will cause `file.json` to be downloaded into `/tmp` and imported.

## [](#discussion)DISCUSSION

The cbimport-json command is used to quickly import data from various files containing JSON data. While importing JSON the cbimport command only utilizes a single reader. As a result importing large dataset may benefit from being partitioned into multiple files and running a separate cbimport process on each file.

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

[cbexport-json](cbexport-json.md)

## [](#cbimport)CBIMPORT

Part of the [cbimport](cbimport.md) suite