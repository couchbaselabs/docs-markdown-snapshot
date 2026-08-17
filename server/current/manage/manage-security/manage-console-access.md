---
title: Manage Console Access
description: Administrators can connect securely with Couchbase Web Console.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/manage-security/manage-console-access.adoc
  xref: xref:server:manage:manage-security/manage-console-access.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/manage/manage-security/manage-console-access.html)

# Manage Console Access

> Administrators can connect securely with Couchbase Web Console. 

## [](#secure-console-access)Obtaining Secure Console Access

Note that Encrypted network access is only available in Couchbase Server Enterprise Edition.

The Couchbase Web Console can be accessed over HTTPS, on port `18091`. Since it is protected by SSL/TLS, this connection is secure.

For example, if you have established the Couchbase Web Console on `` <http://`>_servername_ ``:8091\`, you can access it securely on `` <https://`>_servername_ ``:18091\`.

## [](#disabling-non-secure-console-access)Disabling Non-Secure Console Access

If you wish to force Administrators to log into the UI over an encrypted channel, and so use port 18091 only, you can disable console access on port 8091\. Note that this only affects console access, and does not prevent REST requests from continuing to use 8091, non-securely.

The following REST API method disables Couchbase Web Console on port 8091, so that the secure port 18091 must be used instead:

curl -u Administrator:password \
http://localhost:8091/settings/security \
-d disableUIOverHttp=true

To re-enable Couchbase Web Console access on port 8091, enter the following:

curl -u Administrator:password \
http://localhost:8091/settings/security \
-d disableUIOverHttp=false

Note that the following CLI command can also be used for disabling and enabling unsecured http access. The following expression _disables_ http-based console access, such that https on port 18091 must be used instead:

couchbase-cli setting-security -c <servername> \
-u Administrator -p password \
--set \
--disable-http-ui 1

To re-enable, use the same command with `0` specified for the `--disable-http-ui` flag.

## [](#disabling-secure-console-access)Disabling Secure Console Access

Access to Couchbase Web Console can also be disabled for _https_ access. For details, see [Manage Encryption Settings](../../rest-api/rest-setting-security.md).