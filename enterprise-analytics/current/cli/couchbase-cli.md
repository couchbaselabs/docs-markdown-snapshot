---
title: couchbase-cli
description: The Couchbase cluster management utility.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/cli/pages/couchbase-cli.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/current/cli/couchbase-cli.html)

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

[admin-manage](#couchbase-cli-admin-manage.adoc)

Manages the built-in administrator.

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

[setting-ldap](couchbase-cli-setting-ldap.md)

Modifies LDAP settings.

[setting-notification](couchbase-cli-setting-notification.md)

Modifies notification settings.

[setting-password-policy](couchbase-cli-setting-password-policy.md)

Modifies the password policy.

[setting-rebalance](couchbase-cli-setting-rebalance.md)

Modifies the rebalance settings.

[setting-security](couchbase-cli-setting-security.md)

Modifies security policies.

[ssl-manage](couchbase-cli-ssl-manage.md)

Manage SSL certificates.

[user-manage](couchbase-cli-user-manage.md)

Manage RBAC users.

[setting-saslauthd](couchbase-cli-setting-saslauthd.md)

Manage saslauth settings.

[enable-developer-preview](couchbase-cli-enable-developer-preview.md)

Enable developer preview.

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