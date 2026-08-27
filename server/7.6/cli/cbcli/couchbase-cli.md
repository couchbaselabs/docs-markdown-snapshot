---
title: couchbase-cli
description: The Couchbase cluster management utility.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/couchbase-cli/edit/trinity/docs/modules/cli/pages/cbcli/couchbase-cli.adoc
  xref: xref:7.6@server:cli:cbcli/couchbase-cli.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbcli/couchbase-cli.html)

# couchbase-cli

The Couchbase cluster management utility.

## [](#synopsis)SYNOPSIS

_couchbase-cli <command> [options]_

## [](#description)DESCRIPTION

The couchbase-cli script is the main command line interface for Couchbase cluster management.

## [](#options)OPTIONS

\--version

Prints version information.

\-h

\--help

Prints the short and long help messages.

## [](#commands)COMMANDS

[admin-role-manage](couchbase-cli-user-manage.md)

Manage LDAP user roles.

[backup-service](couchbase-cli-backup-service.md)

Manage the backup service.

[bucket-compact](couchbase-cli-bucket-compact.md)

Compact a Couchbase data bucket.

[bucket-create](couchbase-cli-bucket-create.md)

Create a new Couchbase data bucket.

[bucket-delete](couchbase-cli-bucket-delete.md)

Delete a Couchbase data bucket.

[bucket-edit](couchbase-cli-bucket-edit.md)

Edit a Couchbase data bucket.

[bucket-flush](couchbase-cli-bucket-flush.md)

Flush a Couchbase data bucket.

[bucket-list](couchbase-cli-bucket-list.md)

List all Couchbase data buckets.

[cluster-edit](couchbase-cli-cluster-edit.md)

Edits cluster settings.

[node-to-node-encryption](couchbase-cli-node-to-node-encryption.md)

Allows enabling and disabling of node-to-node encryption.

[cluster-init](couchbase-cli-cluster-init.md)

Initializes a Couchbase cluster.

[ip-family](couchbase-cli-ip-family.md)

Change ip family used for node to node communication.

[collect-logs-start](couchbase-cli-collect-logs-start.md)

Start log collection.

[collect-logs-status](couchbase-cli-collect-logs-status.md)

Get log collection status.

[collect-logs-stop](couchbase-cli-collect-logs-stop.md)

Stop the current log collection task.

[eventing-function-setup](couchbase-cli-eventing-function-setup.md)

Manage the Eventing Service functions.

[failover](couchbase-cli-failover.md)

Failover a server in the cluster.

[group-manage](couchbase-cli-group-manage.md)

Manage server groups.

[host-list](couchbase-cli-host-list.md)

Lists all hosts in the cluster.

[node-init](couchbase-cli-node-init.md)

Initializes a node.

[node-reset](couchbase-cli-node-reset.md)

Resets a node.

[rebalance](couchbase-cli-rebalance.md)

Rebalances data across nodes in a cluster.

[rebalance-status](couchbase-cli-rebalance-status.md)

Show the current rebalance status.

[rebalance-stop](couchbase-cli-rebalance-stop.md)

Stops the current rebalance task.

[recovery](couchbase-cli-recovery.md)

Recovers a previously failed over node.

[reset-admin-password](couchbase-cli-reset-admin-password.md)

Resets the administrator password.

[reset-cipher-suites](couchbase-cli-reset-cipher-suites.md)

Resets the cipher suites to the default.

[server-add](couchbase-cli-server-add.md)

Adds a server to the cluster.

[server-info](couchbase-cli-server-info.md)

Displays server level information and statistics.

[server-list](couchbase-cli-server-list.md)

Lists all servers in the cluster.

[server-readd](couchbase-cli-server-readd.md)

Adds a server back to the cluster after a failover.

[setting-alert](couchbase-cli-setting-alert.md)

Modifies alert settings.

[setting-audit](couchbase-cli-setting-audit.md)

Modifies audit log settings.

[setting-autofailover](couchbase-cli-setting-autofailover.md)

Modifies auto-failover settings.

[setting-autoreprovision](couchbase-cli-setting-autoreprovision.md)

Modifies auto-reprovision settings.

[setting-cluster](couchbase-cli-setting-cluster.md)

Modifies cluster settings.

[setting-compaction](couchbase-cli-setting-compaction.md)

Modifies compaction settings.

[setting-index](couchbase-cli-setting-index.md)

Modifies index settings.

[setting-ldap](couchbase-cli-setting-ldap.md)

Modifies LDAP settings.

[setting-notification](couchbase-cli-setting-notification.md)

Modifies notification settings.

[setting-password-policy](couchbase-cli-setting-password-policy.md)

Modifies the password policy.

[setting-query](couchbase-cli-setting-query.md)

Modifies the query settings.

[setting-rebalance](couchbase-cli-setting-rebalance.md)

Modifies the rebalance settings.

[setting-security](couchbase-cli-setting-security.md)

Modifies security policies.

[setting-xdcr](couchbase-cli-setting-xdcr.md)

Modifies cross data center replication (XDCR) settings.

[ssl-manage](couchbase-cli-ssl-manage.md)

Manage SSL certificates.

[user-manage](couchbase-cli-user-manage.md)

Manage RBAC users.

[xdcr-replicate](couchbase-cli-xdcr-replicate.md)

Manages XDCR cluster references.

[xdcr-setup](couchbase-cli-xdcr-setup.md)

Manages XDCR replications.

[setting-saslauthd](couchbase-cli-setting-saslauthd.md)

Manage saslauth settings.

[enable-developer-preview](couchbase-cli-enable-developer-preview.md)

Enable developer preview.

[collection-manage](couchbase-cli-collection-manage.md)

Manage collections.

## [](#host-formats)HOST FORMATS

When specifying a host for the couchbase-cli command the following formats are expected:

* `couchbase://<addr>` or `couchbases://<addr>`
* `http://<addr>:<port>` or `https://<addr>:<port>`
* `<addr>:<port>`

It is recommended to use the couchbase://<addr> or couchbases://<addr> format for standard installations. The other formats allow an option to take a port number which is needed for non-default installations where the admin port has been set up on a port other that 8091 (or 18091 for https).

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

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite