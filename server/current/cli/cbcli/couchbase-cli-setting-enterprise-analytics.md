---
title: setting-enterprise-analytics
description: Manage Operational Insights service settings (deprecated)
pubDate: 2026-09-24T04:27:44.823Z
antora:
  editUrl: https://github.com/couchbase/couchbase-cli/edit/morpheus/docs/modules/cli/pages/cbcli/couchbase-cli-setting-enterprise-analytics.adoc
  xref: xref:server:cli:cbcli/couchbase-cli-setting-enterprise-analytics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/cli/cbcli/couchbase-cli-setting-enterprise-analytics.html)

# setting-enterprise-analytics

Manage Operational Insights service settings (deprecated)

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-enterprise-analytics_ [<options>]

## [](#description)DESCRIPTION

DEPRECATED: Please use the [setting-operational-insights](couchbase-cli-setting-operational-insights.md)command, which provides the same functionality as this command and takes the same options. This command is retained only so that scripts written against the former product name keep working, and it will be removed in a future release.

This command addresses the cluster through the REST endpoint of the former product name, so it remains usable against a cluster which is older than the `setting-operational-insights` command.

## [](#options)OPTIONS

See [setting-operational-insights](couchbase-cli-setting-operational-insights.md).

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

[setting-operational-insights](couchbase-cli-setting-operational-insights.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite