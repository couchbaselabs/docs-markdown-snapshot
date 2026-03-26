---
title: cbdocloader
editUrl: https://github.com/couchbase/backup/edit/neo/docs/modules/tools/pages/cbdocloader.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:tools:cbdocloader.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/tools/cbdocloader.html)

# cbdocloader

(Deprecated) A utility to import sample buckets into Couchbase Server.

## [](#description)Description

`cbdocloader` has been deprecated, please use `cbimport` with the `--format sample` flag instead.

The `cbdocloader` tool loads Couchbase sample datasets into Couchbase Server. Sample datasets are zip files, provided by Couchbase, which contain documents and index definitions. These datasets are intended to allow users to explore Couchbase features prior to loading their own datasets.

For Linux, the tool's location is _/opt/couchbase/bin/cbdocloader_; for Windows, _C:\\Program Files\\Couchbase\\Server\\bin\\cbdocloader_; and for Mac OS X, _/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/cbdocloader_.

## [](#syntax)Syntax

The syntax for `cbdocloader` is as follows:

cbdocloader --cluster [hostname] --username [username]
--p [password] --bucket [bucket-name] --bucket-quota [quota]
--dataset [path] --thread [number] --verbose

## [](#options)Options

Command options are as follows:

| Option                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \-h --help                                | Show this help message and exit.                                                                                                                                                                                                                                                                                                                                                                                                    |
| \-c \[hostname\], --cluster \[hostname\]  | The hostname of one of the nodes in the cluster to load data into. See the [Host Formats](#cli:cbdocloader.adoc#host-formats) section below for hostname specification details.                                                                                                                                                                                                                                                     |
| \-u \[username\], --user \[username\]     | The username for cluster authentication. The user must have the appropriate privileges to create a bucket, write data, and create view, secondary index and full-text index definitions. This can be specified by means of the environment variable CB\_REST\_USERNAME.                                                                                                                                                             |
| \-p \[password\], --password \[password\] | The password for cluster authentication. The user must have the appropriate privileges to create a bucket, write data, and create view, secondary index and full-text index definitions. This can be specified by means of the environment variable CB\_REST\_PASSWORD.                                                                                                                                                             |
| \--client-cert \[path\]                   | The path to a client certificate. The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with \--client-keyas an alternative to the \--username and \--password flags.                                                                                                                                                                                                                 |
| \--client-key \[path\]                    | The path to the client private key. The path to the client private key whose public key is contained in the certificate provided to the \--client-certflag. May be supplied with \--client-key as an alternative to the \--username and \--password flags.                                                                                                                                                                          |
| \-m \[quota\], --bucket-quota \[quota\]   | The amount of memory to assign to the bucket. If the bucket already exists, this parameter is ignored.                                                                                                                                                                                                                                                                                                                              |
| \-d \[path\], --dataset \[path\]          | The path of the dataset to be loaded. The path can refer to either a zip file or a directory to load data from.                                                                                                                                                                                                                                                                                                                     |
| \-t \[number\],--threads \[number\]       | Specifies the number of concurrent clients to use when loading data. Fewer clients means data loading will take longer, but with fewer cluster resources used. More clients means faster data loading, but with higher cluster-resource usage. This parameter defaults to 1 if it is not specified. This parameter is recommended not to be set to be higher than the number of CPUs on the machine where the command is being run. |
| \-v,--verbose                             | Prints log messages to stdout. This flag is useful for debugging errors in the data loading process.                                                                                                                                                                                                                                                                                                                                |
| \--no-ssl-verify                          | Skips the SSL verification phase. Specifying this flag will allow a connection using SSL encryption, but will not verify the identity of the server you connect to. You are vulnerable to a man-in-the-middle attack if you use this flag. Either this flag or the --cacert flag must be specified when using an SSL encrypted connection.                                                                                          |
| \--cacert                                 | Specifies a CA certificate that will be used to verify the identity of the server being connecting to. Either this flag or the --no-ssl-verify flag must be specified when using an SSL encrypted connection.                                                                                                                                                                                                                       |

## [](#host-formats)HOST FORMATS

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

## [](#certificate-authentication-mtls-authentication)CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)

This tool supports authenticating against a Couchbase Cluster by using certificate based authentication (mTLS authentication). To use certificate based authentication a certificate/key must be supplied, there a currently multiple ways this may be done.

### [](#pem-encoded-certificatekey)PEM ENCODED CERTIFICATE/KEY

An unencrypted PEM encoded certificate/key may be supplied by using: - `--client-cert <path>`\- `--client-key <path>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

The file passed to `--client-key` must contain at most one private key, the key can be in one of the following formats: - PKCS#1 - PKCS#8 - EC

Currently, only the following key types are supported: - RSA - ECDSA - ED25519

### [](#pem-encoded-certificatepem-or-der-encrypted-pkcs8-key)PEM ENCODED CERTIFICATE/PEM OR DER ENCRYPTED PKCS#8 KEY

An encrypted PKCS#8 formatted key may be provided using: - `--client-cert <path>`\- `--client-key <path>`\- `--client-key-password <password>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

Currently, only the following key types are supported: - RSA - ECDSA - ED25519

### [](#encrypted-pkcs12-certificatekey)ENCRYPTED PKCS#12 CERTIFICATE/KEY

An encrypted PKCS#12 certificate/key may be provided using: - `--client-cert <path>`\- `--client-cert-password <password>`

The file passed to `--client-cert` must contain the client certificate and exactly one private key. It may also contain the chain required to authenticate the client certificate.

Currently, only the following key types are supported: - RSA - ECDSA - ED25519

## [](#operations-during-major-cluster-configuration-changes)OPERATIONS DURING MAJOR CLUSTER CONFIGURATION CHANGES

Operations (commands or sub-commands) which connect to a cluster are not supported during major cluster configuration changes.

For example, performing an import/export, making a backup or performing a restore whilst changing the TLS configuration/security settings is unsupported.

These types of changes (e.g. changing the TLS mode to strict) are not expected to be time consuming so it's generally expected that operations should be started after completing the configuration change.

Please note that this does not include rebalances; operations may be performed during a rebalance. The reason for this distinction, is that major cluster configuration changes are generally quick, whilst rebalances for large data sets may be time consuming.

## [](#examples)Examples

To load the dataset `travel-sample.zip`, which is located in _/opt/couchbase/samples/_, into a bucket with a memory quota of 1024MB, run the following command.

cbdocloader -c couchbase://127.0.0.1 -u Administrator \
-p password -m 1024 -b travel-sample \
-d /opt/couchbase/samples/travel-sample.zip

To increase the parallelism of data-loading, use the _threads_ option. In the example below, 4 threads are specified.

cbdocloader -c couchbase://127.0.0.1 -u Administrator \
-p password -m 1024 -b travel-sample \
-d /opt/couchbase/samples/travel-sample.zip -t 4

The `cbdocloader` command can also be used to load data from a folder. The folder must contain files that correspond to the samples format. See the [Sample Data Format](#cli:cbdocloader.adoc#sample-data-format) section below, for more information. The following example show to load data from folder _/home/alice/census-sample_:

cbdocloader -c couchbase://127.0.0.1 -u Administrator \
-p password -m 1024 -b census-sample -d /home/alice/census-sample

## [](#sample-data-format)Sample Data Format

The `cbdocloader` command is used to load data from zip files or folders that correspond to the _Couchbase sample data format_. This is exemplified as follows:

+ sample_folder
  + design_docs
    indexes.json
    design_doc.json
  + docs
    document1.json
    document2.json
    document3.json
    document4.json

The top level directory can be given any name and will always contain two folders. The `design_docs` folder is where index definitions are kept. This folder will contain zero or more JSON files that contain the various indexes that should be created when the sample dataset is loaded. Global Secondary Indexes (GSI) should always be in a file named `indexes.json`. Below is an example of the format for defining GSI indexes.

{
 "statements": [
   {
     "statement": "CREATE PRIMARY INDEX on `bucket1`",
     "args": null
   },
   {
     "statement": "CREATE INDEX by_type on `bucket1`(name) WHERE _type='User'"
     "args": null
   }
 ]
}

GSI indexes are defined as a JSON document where each index definition is contained in a list called `statements`. Each element in the list is an object that contains two keys. The `statement` key contains the actual index definition, and the `args` key is used if the statement contains any positional arguments.

All other files in the `design_docs` folder are used to define view design documents, and each design document should be put into a separate file. These files can be named anything, but should always have the `.json` file extension. Below is an example of a view design document definition.

{
   "_id": "_design/players"
   "views": {
     "total_experience": {
       "map": "function(doc,meta){if(doc.jsonType ==
       "reduce": "_sum"
     },
     "player_list": {
       "map": "function (doc, meta){if(doc.jsonType ==
     }
   }
 }

In the document above, the `_id` field is used to name the design document. This name should always be prefixed with `_design/`. The other field in the top level of the document is the `views` field. This field contains a map of view definitions. The key for each element in the map is the name of the view. Each view must contain a `map` element that defines the map function, and may also contain an optional `reduce` element that defines the reduce function.

View design documents support map-reduce views as well as spatial views. Below is an example of a spatial view definition. Spatial views follow similar rules as the map-reduce views above.

 {
   "_id": "_design/spatial"
   "spatial": {
	 	"position": "<spatial view function definition>",
		"location": "<spatial view function definition>"
   }
 }

Note that spatial views only use a single function to define the index. As a result this function is defined as the value of the spatial views name.

The other folder at the top level directory of a sample data folder is the `docs` folder. This folder will contain all of the documents to load into Couchbase. Each document in this folder is contained in a separate file and each file should contain a single JSON document. The key name for the document will be the name of the file. Each file should also have a `.json` file extension which will be removed from the key name when the data is loaded. Since each document to be loaded is in a separate file, there can potentially be many files. The docs folder allows subfolders to help categorize documents.