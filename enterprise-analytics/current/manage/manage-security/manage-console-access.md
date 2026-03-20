---
title: Manage Console Access
description: Administrators can connect securely with Enterprise Analytics Web Console.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/manage/pages/manage-security/manage-console-access.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:manage:manage-security/manage-console-access.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-security/manage-console-access.html)

# Manage Console Access

> Administrators can connect securely with Enterprise Analytics Web Console. 

## [](#secure-console-access)Obtaining Secure Console Access

Note that Encrypted network access is only available in Enterprise Analytics Enterprise Edition.

The Enterprise Analytics Web Console can be accessed over HTTPS, on port `18091`. Since it is protected by SSL/TLS, this connection is secure.

For example, if you have established the Enterprise Analytics Web Console on `` <http://`>_servername_ ``:8091\`, you can access it securely on `` <https://`>_servername_ ``:18091\`.

## [](#disabling-non-secure-console-access)Disabling Non-Secure Console Access

If you wish to force Administrators to log into the UI over an encrypted channel, and so use port 18091 only, you can disable console access on port 8091\. Note that this only affects console access, and does not prevent REST requests from continuing to use 8091, non-securely.

The following REST API method disables Enterprise Analytics Web Console on port 8091, so that the secure port 18091 must be used instead:

curl -u Administrator:password \
http://localhost:8091/settings/security \
-d disableUIOverHttp=true

To re-enable Enterprise Analytics Web Console access on port 8091, enter the following:

curl -u Administrator:password \
http://localhost:8091/settings/security \
-d disableUIOverHttp=false

Note that the following CLI command can also be used for disabling and enabling unsecured http access. The following expression _disables_ http-based console access, such that https on port 18091 must be used instead:

/opt/enterprise-analytics/bin/couchbase-cli
-u Administrator -p password \
--set \
--disable-http-ui 1

To re-enable, use the same command with `0` specified for the `--disable-http-ui` flag.

## [](#disabling-secure-console-access)Disabling Secure Console Access

Access to Enterprise Analytics Web Console can also be disabled for _https_ access. For details, see [Manage Encryption Settings](#reference:rest-setting-security.adoc).