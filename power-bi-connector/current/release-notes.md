---
title: Release Notes
description: Release notes for the Couchbase Power BI Connector.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Power BI Connector
    version: "2.0"
antora:
  editUrl: https://github.com/couchbase/docs-connectors-power-bi/edit/release/2.0/modules/ROOT/pages/release-notes.adoc
  xref: xref:power-bi-connector::release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/power-bi-connector/current/release-notes.html)

# Release Notes

> Release notes for the Couchbase Power BI Connector. 

The [Couchbase Power BI Connector](index.md) lets you connect Microsoft Power BI to your Couchbase data sources for interactive data visualization.

## [](#v-2-0)Version 2.0 (2026-10-19)

* The Power BI connector now uses the new names for the Couchbase Analytics products:

  * Enterprise Analytics is now Operational Insights Enterprise.
  * Capella Analytics is now Operational Insights Capella.  
When you configure an ODBC Data Source Name (DSN), select the data source by its new name.
* The ODBC driver now trusts certificates in the Windows certificate store. You need to specify **Cluster Cert Path** only if Windows does not trust your cluster certificate. For more information, see [Certificate and Hostname Verification](index.md#certificate-and-hostname-verification).
* The ODBC driver now verifies that the cluster certificate matches the hostname or IP address that the driver connects to. Hostname verification is on by default. If an existing connection fails with a hostname mismatch after you upgrade, use a certificate that includes the hostname, or set `verify_hostname=false` in **Advanced Parameters**. For more information, see [Certificate and Hostname Verification](index.md#certificate-and-hostname-verification).

Download

* [Power BI Connector 2.0](https://packages.couchbase.com/releases/couchbase-powerbi-connector/2.0/couchbase-powerbi-connector-2.0.103.mez)

Supported and tested dependencies

* ODBC driver: [couchbase-odbc-2.0.104-win64.msi](https://packages.couchbase.com/releases/couchbase-odbc-driver/2.0/couchbase-odbc-2.0.104-win64.msi)

  * For dependency licenses, see the [ODBC Driver Notices File](https://packages.couchbase.com/releases/couchbase-odbc-driver/2.0/couchbase-odbc-driver-2.0-notices.txt).
* OpenSSL: [Win64 OpenSSL v3.5.x Light](https://slproweb.com/products/Win32OpenSSL.html)

## [](#v-1-3)Version 1.3 (2026-06-30)

The Power BI connector now supports JSON Web Token (JWT) authentication for Enterprise Analytics. For more information, see [Authenticate Using JWT](index.md#authenticate-using-jwt).

[Power BI Connector Download](https://packages.couchbase.com/releases/couchbase-powerbi-connector/1.3/couchbase-powerbi-connector-1.3.100.mez)

The supported and tested dependencies of this release are:

* [couchbase-odbc-1.3.102-win64.msi](https://packages.couchbase.com/releases/couchbase-odbc-driver/1.3/couchbase-odbc-1.3.102-win64.msi)

  * See the [Notices File](https://packages.couchbase.com/releases/couchbase-odbc-driver/1.3/couchbase-odbc-driver-1.3-notices.txt) for dependency licenses for the ODBC Driver.
* [Win64 OpenSSL v3.3.x Light](https://slproweb.com/products/Win32OpenSSL.html)

## [](#v-1-2)Version 1.2 (2026-03-12)

The Power BI connector now supports client certificate and LDAP authentication in addition to basic credentials. This update enhances enterprise security and streamlines access by allowing you to connect using organizational directory or certificate-based identities.

[Power BI Connector Download](https://packages.couchbase.com/releases/couchbase-powerbi-connector/1.2/couchbase-powerbi-connector-1.2.101.mez)

The supported and tested dependencies of this release are:

* [couchbase-odbc-1.2.114-win64.msi](https://packages.couchbase.com/releases/couchbase-odbc-driver/1.2/couchbase-odbc-1.2.114-win64.msi)

  * See the [Notices File](https://packages.couchbase.com/releases/couchbase-odbc-driver/1.2/couchbase-odbc-driver-1.2-notices.txt) for dependency licenses for the ODBC Driver.
* [Win64 OpenSSL v3.3.x Light](https://slproweb.com/products/Win32OpenSSL.html)

## [](#v-1-1)Version 1.1 (2024-06-12)

[Power BI Connector Download](https://packages.couchbase.com/releases/couchbase-powerbi-connector/1.0/couchbase-powerbi-connector-1.0.mez)

The supported and tested dependencies of this release are:

* [couchbase-odbc-1.1-win64.msi](https://packages.couchbase.com/releases/couchbase-odbc-driver/1.1/couchbase-odbc-1.1-win64.msi)

  * See the [Notices File](https://packages.couchbase.com/releases/couchbase-odbc-driver/1.1/couchbase-odbc-driver-1.1-notices.txt) for dependency licenses for the ODBC Driver.
* [Win64 OpenSSL v3.3.x Light](https://slproweb.com/download/Win64OpenSSL%5FLight-3%5F3%5F1.msi)

## [](#v-1-0)Version 1.0 (2024-01-25)

[Power BI Connector Download](https://packages.couchbase.com/releases/couchbase-powerbi-connector/1.0/couchbase-powerbi-connector-1.0.mez)

The supported and tested dependencies of this release are:

* [couchbase-odbc-1.0-win64.msi](https://packages.couchbase.com/releases/couchbase-odbc-driver/1.0/couchbase-odbc-1.0-win64.msi)

  * See the [Notices File](https://packages.couchbase.com/releases/couchbase-odbc-driver/1.0/couchbase-odbc-driver-1.0-notices.txt) for dependency licenses for the ODBC Driver.
* Win64 Open SSL 1.1.1 Light

This is the initial release of the Couchbase Power BI Connector.