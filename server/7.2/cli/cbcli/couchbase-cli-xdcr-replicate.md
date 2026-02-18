---
title: xdcr-replicate
description: Creates a replication between two data centers
editUrl: https://github.com/couchbase/couchbase-cli/edit/neo/docs/modules/cli/pages/cbcli/couchbase-cli-xdcr-replicate.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/cli/cbcli/couchbase-cli-xdcr-replicate.html)

# xdcr-replicate

Creates a replication between two data centers

## [](#synopsis)SYNOPSIS

_couchbase-cli xdcr-replicate_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--create] [--delete] [--pause] [--list]
    [--resume] [--settings] [--get] [--xdcr-from-bucket <bucket>]
    [--xdcr-to-bucket <bucket>] [--xdcr-cluster-name <name>]
    [--filter-expression <regex>] [--xdcr-replicator <id>]
    [--checkpoint-interval <seconds>] [--worker-batch-size <num>]
    [--doc-batch-size <kilobytes>][--failure-restart-interval <seconds>]
    [--source-nozzle-per-node <num>] [--target-nozzle-per-node <num>]
    [--bandwidth-usage-limit <num>] [--enable-compression <num>]
    [--stats-interval <milliseconds>][--optimistic-replication-threshold <bytes>]
    [--log-level <level>] [--priority <High|Medium|Low>] [--reset-expiry <1|0>]
    [--filter-deletion <1|0>] [--filter-expiration <1|0>]
    [--collection-explicit-mappings <1|0>] [--collection-migration <1|0>]
    [--collection-mapping-rules <mappings>]

## [](#description)DESCRIPTION

This command is used to manage XDCR replications.

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

\--create

Creates a new XDCR replication.

\--delete

Deletes an XDCR replication.

\--pause

Pauses an XDCR replication.

\--list

Lists all XDCR replications.

\--resume

Resumes an XDCR replication.

\--settings

Sets advanced settings for an XDCR replication.

\--get

Gets the setting for a XDCR replication.

\--xdcr-from-bucket <bucket>

The name bucket to replicate data from.

\--xdcr-to-bucket <bucket>

The name bucket to replicate data to.

\--xdcr-cluster-name <name>

The name of the cluster reference to replicate to.

\--filter-expression <regex>

A regular expression used to filter the replication stream.

\--filter-skip-restream

With the specified flag, XDCR will remove all checkpoints and restart the replication such that all mutations that fit the new filter will be re-replicated to the target.

\--xdcr-replicator <id>

The XDCR Replication ID. To get a list of replicator ID’s use the --list flag.

\--checkpoint-interval <seconds>

The interval between checkpoints in seconds. The value of this option must be between 60 and 14,400.

\--worker-batch-size <num>

The worker batch size. The value of this option must be between 500 and 10,000.

\--doc-batch-size <kilobytes>

The document batch size in Kilobytes. The value of this option must be between 10 and 100,000.

\--failure-restart-interval <seconds>

Interval for restarting failed XDCR connections in seconds. The value of this option must be between 1 and 300.

\--optimistic-replication-threshold <bytes>

Document body size threshold in bytes used to trigger optimistic replication.

\--source-nozzle-per-node <num>

The number of source nozzles to each node in the target cluster. The value of this option must be between 1 and 10.

\--target-nozzle-per-node <num>

The number of outgoing nozzles to each node in the target cluster. The value of this option must be between 1 and 10.

\--bandwidth-usage-limit <num>

The bandwidth limit for XDCR replications in mebibytes per second for this replication.

\--enable-compression <num>

Specifies whether or not XDCR compression is enabled. Set this option to "1" to enable compression or "0" to disable compression. This feature is only available in Couchbase Enterprise Edition and can only be used where the target cluster supports compression.

\--log-level <level>

The XDCR log level.

\--stats-interval <milliseconds>

The interval for statistics updates in milliseconds.

\--priority <High|Medium|Low>

Specify the priority for the replication. The options are High, Medium or Low. The default priority is High.

\--reset-expiry <1|0>

When set to true, all mutations sent to the target cluster will have the expiration set to zero. This means documents will not expire in target cluster. This can be overridden by setting max-ttl on the target bucket.

\--filter-deletion <1|0>

When set to true, delete mutations will not be sent to the target cluster. This means documents will not be deleted in the target cluster via delete operations on the source cluster.

\--filter-expiration <1|0>

When set to true, expiry mutations will not be sent to the target cluster. This means documents will not be deleted in the target cluster via expirations on the source cluster.

## [](#collection-options)COLLECTION OPTIONS

\--collection-explicit-mappings <1|0>

Enable or disable explicit collection mappings. See COLLECTION MAPPINGS below for more information. This is an Enterprise Edition only feature. This option cannot be turned on if collection migration is on.

\--collection-migration <1|0>

Enable or disable XDCR migration mode. Explicit mappings must be set to 1 for this. This is an Enterprise Edition only feature. This option cannot be turned on if collection explicit mappings is on.

\--collection-mapping-rules <mappings>

The mappings rules from source bucket to target bucket. The mappings are JSON formatted string. See COLLECTION MAPPINGS below for more information. This is an Enterprise Edition only feature.

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

To create a new XDCR replication from the "default" bucket to the "apps" bucket on a remote cluster called "east". You can run the following command below. Note that if you have not setup a remote cluster reference then you need to do this first by running the [xdcr-setup](couchbase-cli-xdcr-setup.md).

$ couchbase-cli xdcr-replicate -c 192.168.1.5 -u Administrator \
   -p password --create --xdcr-cluster-name east --xdcr-from-bucket apps \
   --xdcr-to-bucket apps

To list all of the current XDCR replication you can run the following command.

$ couchbase-cli xdcr-replicate -c 192.168.1.5 -u Administrator \
   -p password --list

To delete an XDCR replication you first need to use the --list flag to get the replicator id. Once you get the replicator id (in this case we will assume it is `f4eb540d74c43fd3ac6d4b7910c8c92f/default/default`) you can run the command below to delete the replication.

$ couchbase-cli xdcr-replicate -c 192.168.1.5 -u Administrator \
   -p password --delete \
   --xdcr-replicator=f4eb540d74c43fd3ac6d4b7910c8c92f/default/default

To pause an XDCR replication you first need to use the --list flag to get the replicator id. Once you get the replicator id (in this case we will assume it is `f4eb540d74c43fd3ac6d4b7910c8c92f/default/default`) you can run the command below to pause the replication.

$ couchbase-cli xdcr-replicate -c 192.168.1.5 -u Administrator \
   -p password --pause \
   --xdcr-replicator=f4eb540d74c43fd3ac6d4b7910c8c92f/default/default

To resume an XDCR replication you first need to use the --list flag to get the replicator id. Once you get the replicator id (in this case we will assume it is `f4eb540d74c43fd3ac6d4b7910c8c92f/default/default`) you can run the command below to resume the replication.

$ couchbase-cli xdcr-replicate -c 192.168.1.5 -u Administrator \
   -p password --resume \
   --xdcr-replicator=f4eb540d74c43fd3ac6d4b7910c8c92f/default/default

To modify the settings of an XDCR replication you first need to use the --list flag to get the replicator id. Once you get the replicator id (in this case we will assume it is `f4eb540d74c43fd3ac6d4b7910c8c92f/default/default`) you can run the command if for example you wanted to change the document batch size to 2048 and failure restart interval to 60 seconds.

$ couchbase-cli xdcr-replicate -c 192.168.1.5 -u Administrator \
   -p password --settings --failure-restart-interval=60 \
   --xdcr-replicator=f4eb540d74c43fd3ac6d4b7910c8c92f/default/default \
     --doc-batch-size=2048

## [](#collection-mappings)COLLECTION MAPPINGS

By default, upgraded bucket-to-bucket replication includes implicit mapping of all scope and collections replications of which the bucket contains to globally unique entities on the remote cluster. This means that whatever collection exists in the source will be implicitly mapped by name to the target, and the data replicated. For example, if a namespace such as S1:C1 exists on the source, Implicit Mapping states that the equivalent mapped entity of S1:C1 namespace should also exist on the target. If brand-new replicated systems that both support Collections are created with Implicit Mapping without specifying anything regarding collections, this is also the behavior of the system. If there is a default scope and/or default collection, they will be mapped to the default scope/collection on the target cluster.

For users who require more detailed control over collections, they may choose to use Explicit Mapping. Explicit mapping for a replication is specified by a set of rules defined below.

__Table 1\. Explicit Mapping Rules__
| Priority | Match Rule      | Description                                                    | Syntax                        |
| -------- | --------------- | -------------------------------------------------------------- | ----------------------------- |
| 0        | S.C to S.C      | Matches a single Scope:Collection to a target Scope:Collection | {"s.c":"target\_s.target\_c"} |
| 1        | S.C Deny List   | Stops one singular Scope:Collection from being replicated      | {"s.c":null}                  |
| 2        | Scope to Scope  | Explicitly map one source scope to a target scope              | {"s":"target\_s"}             |
| 3        | Scope Deny List | Stop one source scope from being replicated                    | {"s": null}                   |

Note that when migration mode is enabled Explicit Rule-Based Mapping is used instead. The Rule-Based Mapping expressions have the same format as the filtering expressions in advance filtering. Below are some example rules. Note that the filter expression syntax is supported so a large range of expressions can be created:

Table 2\. Example Rule-Based Mapping Rules 

Rule

Description

Syntax

Key

Matches a document based on the key and maps it to a collection

`{“REGEXP_CONTAINS(META().id, ‘^app1_’”:”Apps.App1”}`

Maps any document with a key starting with `app1` to the collection \`Apps.App1\`\_ 

Field value match

Matches documents based on the values of one or more fields and maps it to a collection

`{“Region == ‘APAC’ AND Country == ‘Japan’”:”APAC.Japan”}`

_Maps any document that has field `Region` and `Country` with respective values APAC and Japan to the collection \`APAC.Japan\`_

Field exists

Matches any document that has the given field and maps it to a collection

{“EXISTS(PhotosData)”:”default.PhotoDocuments”} 

\_Maps any document that has the `PhotosData` field to the `PhotoDocuments` collections under the default scope

### [](#collection-mapping-examples)COLLECTION MAPPING EXAMPLES

To enable explicit collection mapping for a bucket _default_ that has a scope with name _databases_ and a collection called _nosql_ and want this to be mapped in the target bucket to a scope _database-replica_ and _nosql-replica_we can use the following command:

$ couchbase-cli xdcr-replicate -c 192.168.1.5 -u Administrator \
   -p password --settings \
   --xdcr-replicator=f4eb540d74c43fd3ac6d4b7910c8c92f/default/default \
   --collection-explicit-mappings 1  --collection-mapping-rules {"databases.nosql":"databases-replica.nosql-replica"}

Note that explicit mapping rules cannot be used with collection migration mode.

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

[setting-xdcr](couchbase-cli-setting-xdcr.md), [xdcr-setup](couchbase-cli-xdcr-setup.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite