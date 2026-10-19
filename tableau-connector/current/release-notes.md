---
title: Release Notes
description: Release notes, installation instructions, and download archive for
  the Couchbase Tableau Connector.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Tableau Connector
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-tableau/edit/release/3.0/modules/ROOT/pages/release-notes.adoc
  xref: xref:tableau-connector::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/current/release-notes.html)

# Release Notes

> Release notes, installation instructions, and download archive for the Couchbase Tableau Connector. 

## [](#installation)Installation

Scroll to the version you want and click the download link to get the full connector distribution. For more information on installing the connector, see [Download Couchbase Tableau Connector](setup-tableau-connector.md).

> [!IMPORTANT]
> By downloading the Couchbase Tableau Connector, you agree to the terms of the [Couchbase Tableau Connector License Agreement](https://www.couchbase.com/toollicenses/tableau/).

## [](#v3.0.0)Version 3.0.0 (2026-10-19)

### [](#downloads)Downloads

[Tableau Connector 3.0.0 Download](https://packages.couchbase.com/releases/couchbase-tableau-connector/3.0.0/couchbase-operational-insights-tableau-connector-3.0.0.zip)

> [!NOTE]
> Tableau Connector 3.0.0 is compatible only with Enterprise Analytics 2.0 or later and Operational Insights Enterprise 3.0 or later.

### [](#enhancements)Enhancements

* Enterprise Analytics is now Operational Insights Enterprise. The Tableau Connector has been updated to use the new product name.
* The connector plugin class changed from `enterprise-analytics` to `couchbase-operational-insights`.  
If you're upgrading from version 2.0.0, update your existing configuration files to use the new class name:

  * Rename the `enterprise-analytics.properties` file to `couchbase-operational-insights.properties`.
  * In each custom OAuth configuration XML file, change the `<dbclass>` value to `couchbase-operational-insights`.  
If you do not update these files, Tableau ignores the settings without an error, and client certificate authentication, private CA certificates, and OAuth 2.0 authentication stop working after the upgrade.

### [](#known-issues)Known Issues

* **Client Certificate** authentication requires you to enable the **Require SSL** option. If you do not select this option, the connector connects without TLS and does not send the client certificate, causing the sign-in to fail with an authentication error.
* To trust a certificate from a private certificate authority (CA), set the `sslCertPath` property in the `couchbase-operational-insights.properties` file. The connector does not support the `sslKeystorePath` and `sslKeystorePassword` properties and ignores them if specified. For more information, see [Configure SSL Certificates](setup-tableau-desktop.md#ssl).

## [](#v2.0.0)Version 2.0.0 (2026-06-30)

### [](#downloads-2)Downloads

[Tableau Connector 2.0.0 Download](https://packages.couchbase.com/releases/couchbase-tableau-connector/2.0.0/enterprise-analytics-tableau-connector-2.0.0.zip)

> [!NOTE]
> Tableau Connector 2.0.0 is only compatible with Enterprise Analytics.

### [](#enhancements-2)Enhancements

* [TACO-27](https://issues.couchbase.com/browse/TACO-27), [JDBCC-59](https://issues.couchbase.com/browse/JDBCC-59): Added support for OAuth 2.0 authentication.
* [TACO-25](https://issues.couchbase.com/browse/TACO-27), [JDBCC-55](https://issues.couchbase.com/browse/JDBCC-59): Added support for LDAP authentication.
* [TACO-25](https://issues.couchbase.com/browse/TACO-27), [JDBCC-54](https://issues.couchbase.com/browse/JDBCC-59): Added support for Client Certificate authentication.

## [](#v1.2.1)Version 1.2.1 (2026-10-19)

### [](#downloads-3)Downloads

[Tableau Connector 1.2.1 Download](https://packages.couchbase.com/releases/couchbase-tableau-connector/1.2.1/couchbase-analytics-tableau-connector-1.2.1.zip)

### [](#enhancements-3)Enhancements

* [JDBCC-62](https://issues.couchbase.com/browse/JDBCC-62): Upgraded the underlying Java SDK from version 3.12.0 to 3.12.3\. This upgrade includes Netty 4.2.18 and Jackson 2.21.6 in core-io.  
In addition, upgraded Jackson to version 2.21.7 and Bouncy Castle to version 1.86 in the driver to address security vulnerabilities.

## [](#v1.2.0)Version 1.2.0 (2026-06-30)

### [](#downloads-4)Downloads

[Tableau Connector 1.2.0 Download](https://packages.couchbase.com/releases/couchbase-tableau-connector/1.2.0/couchbase-analytics-tableau-connector-1.2.0.zip)

> [!NOTE]
> Tableau Connector 1.2.0 is compatible with both Couchbase Analytics Service and Capella Analytics.

### [](#enhancements-4)Enhancements

* [TACO-25](https://issues.couchbase.com/browse/TACO-25), [JDBCC-55](https://issues.couchbase.com/browse/JDBCC-55): Added support for LDAP authentication.
* [TACO-25](https://issues.couchbase.com/browse/TACO-25), [JDBCC-54](https://issues.couchbase.com/browse/JDBCC-54): Added support for client certificate authentication.
* [JDBCC-60](https://issues.couchbase.com/browse/JDBCC-60): Upgraded the underlying Java SDK from version 3.11.1 to 3.12.0.
* [TACO-27](https://issues.couchbase.com/browse/TACO-27): Resolved minor bugs.

## [](#v1.1.3)Version 1.1.3 (2024-08-05)

### [](#downloads-5)Downloads

[Tableau Connector 1.1.3 Download](https://packages.couchbase.com/releases/couchbase-tableau-connector/1.1.3/couchbase-tableau-connector-1.1.3.zip)

### [](#enhancements-5)Enhancements

* [TACO-24](https://issues.couchbase.com/browse/TACO-24): Added Columnar support.

## [](#v1.1.2)Version 1.1.2 (2024-05-03)

### [](#downloads-6)Downloads

[Tableau Connector 1.1.2 Download](https://packages.couchbase.com/releases/couchbase-tableau-connector/1.1.2/couchbase-tableau-connector-1.1.2.zip)

### [](#enhancements-6)Enhancements

* [TACO-16](https://issues.couchbase.com/browse/TACO-16): Added support for the median function.

## [](#v1.1.1)Version 1.1.1 (2023-12-05)

### [](#downloads-7)Downloads

[Tableau Connector 1.1.1 Download](https://packages.couchbase.com/releases/couchbase-tableau-connector/1.1.1/couchbase-tableau-connector-1.1.1.zip)

### [](#enhancements-7)Enhancements

* [JDBCC-51](https://issues.couchbase.com/browse/JDBCC-51): Added support for Database metadata entity.

## [](#v1.1.0)Version 1.1.0 (2023-07-31)

### [](#downloads-8)Downloads

[Tableau Connector 1.1.0 Download](https://packages.couchbase.com/releases/couchbase-tableau-connector/1.1.0/couchbase-tableau-connector-1.1.0.zip)

The connector is now compatible with Tableau Cloud.

### [](#enhancements-8)Enhancements

* [JDBCC-43](https://issues.couchbase.com/browse/JDBCC-43): Tableau queries now time out gracefully if connection to Couchbase Analytics is lost.
* [JDBCC-44](https://issues.couchbase.com/browse/JDBCC-44): Tableau SSL parameters may be changed without requiring restart.
* [JDBCC-48](https://issues.couchbase.com/browse/JDBCC-48): Upgrade Couchbase Java SDK from `3.3.4` to `3.4.3`.

## [](#v1.0.0)Version 1.0.0 (2022-04-27)

### [](#downloads-9)Downloads

[Tableau Connector 1.0.0 Download](https://packages.couchbase.com/releases/couchbase-tableau-connector/1.0.0/couchbase-tableau-connector-1.0.0.zip)

Initial release.