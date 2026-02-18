---
title: user-manage
description: Manage RBAC users
editUrl: https://github.com/couchbase/couchbase-cli/edit/neo/docs/modules/cli/pages/cbcli/couchbase-cli-user-manage.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/cli/cbcli/couchbase-cli-user-manage.html)

# user-manage

Manage RBAC users

## [](#synopsis)SYNOPSIS

_couchbase-cli user-manage_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--delete] [--list] [--my-roles] [--set]
    [--set-group] [--delete-group] [--list-groups] [--get-group]
    [-- get] [--rbac-username <username>] [--rbac-password <password>]
    [--rbac-name <name>] [--roles <roles_list>]
    [--auth-domain <domain>] [--user-groups <group>]
    [--group-description <text>] [--ldap-ref <ref>]

## [](#description)DESCRIPTION

This command allows administrators to assign and manage roles to different users and user groups in their organization. Users can either be managed locally by Couchbase or externally through the use of an external domain.

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

\--delete

Deletes an RBAC user profile from the cluster. You must have full administrator privileges in order to delete a user profile.

\--list

Lists all RBAC user profiles in the cluster and show their roles. You must have full administrator privileges in order to list all user profiles.

\--my-roles

Shows the current users RBAC user profile.

\--set

Creates or updates an RBAC user profile. You must have full administrator privileges in order to create or update a user profile.

\--get

Retrieves the RBAC user specified by --rbac-username and show their roles.

\--set-group

Creates or updates a user group.

\--delete-group

Deletes a user group.

\--list-groups

List all groups.

\--get-group

Gets the details of a group.

\--rbac-username <username>

Specifies the username of the RBAC user to modify. This option is used when deleting, creating, or updating an RBAC user profile.

\--rbac-password <password>

Specifies the password to be used for an RBAC user profile. This option is used only when creating or updating a _local_ RBAC user profile. Couchbase does not store password for _external_ RBAC roles.

\--rbac-name <name>

Specifies the name to be used for an RBAC user profile. This option is used when creating or updating an RBAC user profile and it is recommended that this option be set to the users full name.

\--roles <roles\_list>

Specifies the roles to be given to an RBAC user profile. This option is used when creating or updating an RBAC user profile and it is specified as a comma separated list of roles. See the ROLES section for more details on the available roles in Couchbase.

\--auth-domain <domain>

Specifies the auth\_domain to use for a RBAC user profile. This option is used when deleting, creating or updating a RBAC user profile and it may be set to either _local_ or _external_. Local users are users that are managed directly by the Couchbase cluster. External users are users managed by an external source such as LDAP.

\--user-groups <groups>

Specifies the groups the user should be added to. This is used when creating a user (--set) or when updating the users group, and should be specified as a comma separated list.

\--group-name <group>

Specifies the target group for the group operations (--set-group, --delete-group, --get-group).

\--group-description <text>

Specifies the group description, it is used with --set-group.

\--ldap-ref <ref>

Specifies the LDAP group’s distinguished name, to link the couchbase group with the LDAP one.

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

### [](#roles)ROLES

Cluster-Wide Roles:

admin

Give the user permissions to manage all Couchbase configuration settings, and read and write all data in the cluster. This user can make changes to anything in the cluster.

backup\_admin

Gives the user all the permissions required to backup and restore all services. This level of permission is required to use the Backup Service.

bucket\_admin\[…​\]

Gives the user permissions to manage bucket settings. This role can be assigned globally to all buckets or to a particular bucket. For XDCR operations, the user can start/stop replication for the buckets they administer, but they cannot set up the XDCR cluster references. To give a user the ability to manage all bucket settings set their role to bucket\_admin\[\*\]. To give the user permission to manage bucket settings on a single bucket named _default_ then specify the role as bucket\_admin\[default\]. If the user needs to be manage multiple buckets, for example _default_ and _app_, then set the role as bucket\_admin\[default\],bucket\_admin\[app\].

bucket\_full\_access\[…​\]

Gives the user full access to bucket data. This user cannot access the web console and is intended only for application access. This user can read and write data. To give the user full access to all buckets use bucket\_full\_access\[\*\], to give permissions to only one bucket _default_ use bucket\_full\_access\[default\].

cluster\_admin

Gives the user permissions to read, write and manage all cluster-level settings except security.

replication\_admin

Allows the user to configure XDCR topology and manage XDCR replications.

ro\_admin

Gives the user read-only access and cannot make any changes to the system. This user has read-only access to cluster overview, design documents (without the ability to create or query views), bucket summaries (without the ability to create or view documents), XDCR cluster references, XDCR replications, and cluster settings.

security\_admin

Gives the user permission to view all cluster statistics and manage user roles, but cannot grant Full Admin or Security Admin roles to other users or alter their own role. This user can access the web console. This user cannot read data.

views\_admin\[…​\]

Gives the user privileges to define views and then run these views on data to ensure that views are defined properly. This applies both to the map-reduce and spatial views. To give a user the ability to manage views on all buckets set their role to views\_admin\[\*\]. To give the user permission to manage views on a single bucket named _default_ then specify the role as views\_admin\[default\]. If the user needs to be manage views for multiple buckets, for example _default_ and _app_, then set the role as views\_admin\[default\],views\_admin\[app\].

Data Service Roles:

data\_backup\[…​\]

Gives the user permission to backup and restore data in Couchbase. To give a user the ability to backup and restore data for all buckets set their role to data\_backup\[\*\]. To give the user the ability to backup and restore data on a single bucket named _default_ then specify their role as data\_backup\[default\]. If the user needs to be able to backup and restore data for multiple buckets, for example _default_ and _app_, then set their role as data\_backup\[default\],data\_backup\[app\].

data\_dcp\_reader\[…​\]

Gives the user permission to create Couchbase DCP connections for a given bucket, collection or scope. To give a user the ability to create DCP connections for all buckets set their role to data\_dcp\_reader\[\*\]. To give the user the ability to create DCP connections on a single bucket named _default_then specify their role as data\_dcp\_reader\[default\]. If the user needs to be able to create DCP connections for multiple buckets, for example _default_ and _app_, then set their role as data\_dcp\_reader\[default\],data\_dcp\_reader\[app\]. To give the permissions for only a scope _scope0_ of _default_ use data\_dcp\_reader\[default:scope0\]. To get permission for a single collection _col0_ in _scope0_ then give the user the role data\_dcp\_reader\[default:scope0:col0\].

data\_monitoring\[…​\]

Gives the user permission to read monitoring data related to the data service in Couchbase. To give a user the ability to monitor data for all buckets set their role to data\_monitoring\[\*\]. To give the user the ability to monitor data on a single bucket named _default_ then specify their role as data\_monitoring\[default\]. If the user needs to be able to monitor data for multiple buckets, for example _default_ and _app_, then set their role as data\_monitoring\[default\],data\_monitoring\[app\]. If the user need to be able to monitor data only for a specific _scope0_ in bucket _default_ then set their role as data\_monitoring\[default:scope0\]. To monitor only collection _col0_ inside _scope0_ then set their role as data\_monitoring\[default:scope0:col0\].

data\_reader\[…​\]

Gives the user permission to read data through the Couchbase key-value APIs. To give a user read-only access for all buckets set their role to data\_reader\[\*\]. To give the user read-only access to data on a single bucket named _default_ then specify their role as data\_reader\[default\]. If the user needs read-only access to data for multiple buckets, for example _default_ and _app_, then set their role as data\_reader\[default\],data\_reader\[app\]. If the user needs read-only access to data for a specific _scope0_ in bucket _default_ then set their role as data\_reader\[default:scope0\]. If the user needs read-only access to data for a collection _col0_ inside _scope0_ then set their role as data\_reader\[default:scope0:col0\].

data\_writer\[…​\]

Gives the user permission to read and write data through the Couchbase key-value APIs. The user cannot however modify the settings of a bucket. To give a user read-write access for all buckets set their role to data\_writer\[\*\]. To give the user read-write access to data on a single bucket named _default_ then specify their role as data\_writer\[default\]. If the user needs read-write access to data for multiple buckets, for example _default_ and _app_, then set their role as data\_writer\[default,app\]. If the user needs read-write access to data for a specific _scope0_ in bucket _default_ then set their role as data\_writer\[default:scope0\]. If the user needs read-write access to data for a collection _col0_ inside _scope0_ then set their role as data\_writer\[default:scope0:col0\].

Full Text Service Roles:

fts\_admin\[…​\]

Gives the user full administrator access for the Full Text Indexing service for the specified buckets. To give a user full administrator access for FTS on all buckets set their role to fts\_admin\[\*\]. To give the user full administrator access for FTS on a single bucket named _default_ then specify their role as fts\_admin\[default\]. If the user needs full administrator access for FTS for multiple buckets, for example _default_ and _app_, then set their role as fts\_admin\[default\],fts\_admin\[app\].

fts\_searcher\[…​\]

Allows the user to query full text indexes for the specified bucket, scope or collection. To give a user the ability to query full text indexes on all buckets set their role to fts\_searcher\[\*\]. To give the ability to query FTS indexes on a single bucket named _default_ then specify their role as fts\_searcher\[default\]. If the user needs to query FTS indexes on multiple multiple buckets, for example _default_ and _app_, then set their role as fts\_searcher\[default\],fts\_searcher\[app\]. If the user needs to query FTS indexes for a specific _scope0_ in bucket _default_ then set their role as fts\_searcher\[default:scope0\]. If the user needs to query FTS indexes for a collection _col0_ inside _scope0_ then set their role as fts\_searcher\[default:scope0:col0\].

Query Service Roles:

query\_delete\[…​\]

Allows the user to execute DELETE query statements on the specified bucket, scope or collection. To give a user the ability execute DELETE statements on all buckets set their role to query\_delete\[\*\]. To give the user needs permission to execute DELETE statements on a single bucket named _default_then specify their role as query\_delete\[default\]. If the user needs to execute DELETE statements for multiple buckets, for example _default_ and _app_, then set their role as query\_delete\[default\],query\_delete\[app\]. If the user needs to execute DELETE statements for a single scope named _scope0_inside _default_ then give their role query\_delete\[default:scope0\]. If the user need to execute DELETE statements for a single collection named _col0_inside _scope0_ then give the role query\_delete\[default:scope0:col0\].

query\_execute\_external\_functions\[…​\]

Allows the user to execute external language functions for a given scope. To allow the user to execute external language functions for all scopes in bucket _default_ use the role query\_execute\_external\_functions\[default\]. If the user needs to execute external language functions for a scope _scope0_ of bucket _default_ then give them the role query\_execute\_external\_functions\[default:scope0\].

query\_execute\_functions\[…​\]

Allows the user to execute N1QL functions for a given scope. To allow the user to execute N1QL functions for all scopes in bucket _default_ use the role query\_execute\_functions\[default\]. If the user needs to execute N1QL functions for a scope _scope0_ of bucket _default_ then give them the role query\_execute\_functions\[default:scope0\].

query\_execute\_global\_external\_functions

Allows the user to execute global external language functions.

query\_execute\_global\_functions

Allows the user to execute global N1QL functions.

query\_insert\[…​\]

Allows the user to execute INSERT query statements on the specified bucket, scope or collection. To give a user the ability execute INSERT statements on all buckets set their role to query\_insert\[\*\]. To give the user permission to execute INSERT statements on a single bucket named _default_then specify their role as query\_insert\[default\]. If the user needs to execute INSERT statements for multiple buckets, for example _default_ and _app_, then set their role as query\_insert\[default\],query\_insert\[app\]. If the user needs to execute INSERT statements for a scope with name _scope0_ of bucket _default_ give the user the role query\_insert\[default:scope0\]. If the user need to execute INSERT statements for a scope with name _col0_ of _scope0_then give them the role query\_insert\[default:scope0:col0\].

query\_manage\_external\_functions\[…​\]

Allows the user to manage external language functions for a given scope. To allow the user to manage external language functions for all scopes in bucket _default_ use the role query\_manage\_external\_functions\[default\]. If the user needs to manage external language functions for a scope _scope0_ of bucket _default_ then give them the role query\_manage\_external\_functions\[default:scope0\].

query\_manage\_functions\[…​\]

Allows the user to manage N1QL functions for a given scope. To allow the user to manage N1QL functions for all scopes in bucket _default_ use the role query\_manage\_functions\[default\]. If the user needs to manage N1QL functions for a scope _scope0_ of bucket _default_ then give them the role query\_manage\_functions\[default:scope0\].

query\_manage\_global\_external\_functions

Allows the user to manage global external language functions.

query\_manage\_global\_functions

Allows the user to manage global N1QL functions.

query\_manage\_index\[…​\]

Allows the user to create and delete indexes on the specified bucket, scope or collection. To give a user the ability to create and delete indexes on all buckets set their role to query\_manage\_index\[\*\]. To give the user permission to create and delete indexes on a single bucket named _default_ then specify their role as query\_manage\_index\[default\]. If the user needs to be create and delete indexes for multiple buckets, for example _default_ and _app_, then set their role as query\_manage\_index\[default\],query\_manage\_index\[app\]. To give the user permission to create and delete indexes on a scope _scope0_ of bucket _default_ set their role as query\_manage\_index\[default:scope0\]. To give the user permission to create and delete indexes on a collections _col0_ of _scope0_set their role as query\_manage\_index\[default:scope0:col0\].

query\_select\[…​\]

Allows the user to execute SELECT query statements on the specified bucket, scope or collection. To give a user the ability to execute SELECT statements on all buckets set their role to query\_select\[\*\]. To give the user permission to execute SELECT statements on a single bucket named _default_ then specify their role as query\_select\[default\]. If the user needs to be execute SELECT statements for multiple buckets, for example _default_ and _app_, then set their role as query\_select\[default\],query\_select\[app\]. To give a user the ability to execute SELECT statements on a scope _scope0_ of bucket _default set their role as query\_select\[default:scope0\]. To give the user the ability to execute select statements on a collection \_col0_ of _scope0_ set their role as query\_select\[default:scope0:col0\].

query\_system\_catalog\[…​\]

Allows the users to run queries against the system catalog on the specified bucket, scope or collection. To give a user the ability to run queries against the system catalog on all buckets set their role to query\_system\_catalog\[\*\]. To give the user permission to run queries against the system catalog on a single bucket named _default_ then specify their role as query\_system\_catalog\[default\]. If the user needs to be run queries against the system catalog for multiple buckets, for example _default_ and _app_, then set their role as query\_system\_catalog\[default\],query\_system\_catalog\[app\]. To give the user the permissions to run queries against the system catalog on a specified scope _scope0_ of bucket _default_ set their roles as query\_system\_catalog\[default:scope0\]. To give a user the ability to run queries against the system catalog on the a specified collection _col0_ of _scope0_ set their role as query\_system\_catalog\[default:scope0:col0\].

query\_update\[…​\]

Allows the user to execute UPDATE query statements on the specified bucket, scope or collections. To give a user the ability to execute UPDATE statements on all buckets set their role to query\_update\[\*\]. To give the user permission to execute UPDATE statements on a single bucket named _default_ then specify their role as query\_update\[default\]. If the user needs to be execute UPDATE statements for multiple buckets, for example _default_ and _app_, then set their role as query\_update\[default\],query\_update\[app\]. To give a user the ability to execute UPDATE statements on a single scope _scope0_ of bucket _default_ set their role as query\_update\[default:scope0\]. To give the user the ability to execute UPDATE statements on a single collections _col0_ of _scope0_ set their role to query\_update\[default:scope0:col0\].

Analytics roles

analytics\_admin

Allows the user to manage dataverses, links and datasets. This user can access the web console but cannot read data.

analytics\_manager\[…​\]

Allows the user to manage local links and datasets on a given bucket as well as query datasets created on this bucket. This user can access the web console and read some data. To give the user this permissions for all buckets use analytics\_manager\[\*\]. To give the permissions for a bucket _default_ then specify the role as analytics\_manager\[default\]. If the user needs the permissions for a subset of buckets _bucket1_ and _bucket2_ then set their role as analytics\_manager\[bucket1\],analytics\_manager\[bucket2\].

analytics\_reader

Allows the user to query datasets. This user can access the web console and read some data.

analytics\_select\[…​\]

Allows user to query datasets on a given bucket, scope or collection. This user can access the web console and read some data. To give a user access to a bucket _default_ use the role analytics\_select\[default\]. This gives access to the bucket and all underlying scopes and collections. To give access to only a specific collection then use the following role analytics\_select\[default:scope0:collection0\].

Mobile roles

mobile\_sync\_gateway\[…​\]

Gives user full access to bucket data as required by Sync Gateway. This user cannot access the web console and is intended only for use by Sync Gateway. This user can read and write data, manage indexes and views, and read some cluster information. To give this role for all buckets use mobile\_sync\_gateway\[\*\], for a specific bucket _default_ use the role mobile\_sync\_gateway\[default\] and for multiple buckets _default_ and _app_ give the roles mobile\_sync\_gateway\[default\],mobile\_sync\_gateway\[app\].

XDCR roles

replication\_admin

Allows the user to administer XDCR features, create cluster references and replication streams of the cluster. This user can access the console and read some data.

replication\_target\[…​\]

Allows the user to create XDCR streams into a given bucket. This user cannot access the web console or read any data. To allow the user to create XDCR streams into all buckets set their roles as replication\_target\[\*\]. To allow the user to create XDCR streams into bucket _default_ set their roles as replication\_target\[default\]. To allow the user to create XDCR streams to bucket _default_ and _app_ set their roles as replication\_target\[default\],replication\_target\[app\]

Eventing roles

eventing\_admin

Allows the user to create and manage eventing functions. This user can access the console.

## [](#examples)EXAMPLES

To create an local RBAC user profile for a user named "John Doe" with username `jdoe` and password `cbpass` with roles to manage the _default_ bucket and all XDCR replication run the following command

$ couchbase-cli user-manage -c 127.0.0.1:8091 -u Administrator \
 -p password --set --rbac-username jdoe --rbac-password cbpass \
 --rbac-name "John Doe" --roles bucket_admin[default],replication_admin \
 --auth-domain local

If you have external user source setup in your cluster and you want to add a user "John Doe" with username `jdoe` who should have the ability to manage only views for all bucket run the following command

$ couchbase-cli user-manage -c 127.0.0.1:8091 -u Administrator \
 -p password --set --rbac-username jdoe --rbac-name "John Doe" \
 --roles views_admin[*] --auth-domain external

To list the current RBAC user profiles run the following command.

$ couchbase-cli user-manage -c 127.0.0.1:8091 -u Administrator \
 -p password --list

To delete an external user named `jdoe` run the following command.

$ couchbase-cli user-manage -c 127.0.0.1:8091 -u Administrator \
 -p password --delete --rbac-username jdoe --auth-domain external

To delete a local user named `jdoe` run the following command.

$ couchbase-cli user-manage -c 127.0.0.1:8091 -u Administrator \
 -p password --delete --rbac-username jdoe --auth-domain local

To see the user profile for a user with the username `jdoe` and password `cbpass`run the following command.

$ couchbase-cli user-manage -c 127.0.0.1:8091 -u jdoe -p cbpass \
 --my-roles

To create a user group with name `admins` and roles `admin` and reference to and LDAP group reference `admins` run the following command.

$ couchbase-cli user-manage -c 127.0.0.1:8091 -u Administrator \
 -p password --set-group --group-name admins --roles admin \
 --group-description "CB admins" --ldap-ref admins

To delete a user group `admins` you have to run the following command.

$ couchbase-cli user-manage -c 127.0.0.1:8091 -u Administrator \
  -p password --delete-group --group-name admins

To get a user group `admins` you have to run the following command. This will show the associated roles.

$ couchbase-cli user-manage -c 127.0.0.1:8091 -u Administrator \
  -p password --get-group --group-name admins

To add or remove roles a user group `admins` you have to first get the current roles using the previous command and then use the set command bellow giving it an amended version of the roles.

$ couchbase-cli user-manage -c 127.0.0.1:8091 -u Administrator \
 -p password --set-group --group-name admins --roles admin \
 --group-description "CB admins" --ldap-ref ro_admin

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

[setting-ldap](couchbase-cli-setting-ldap.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite