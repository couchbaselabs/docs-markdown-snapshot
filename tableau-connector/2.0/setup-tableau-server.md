---
title: Install the Couchbase Tableau Connector on Tableau Server
description: You can install the Couchbase Tableau Connector on Tableau Server.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Tableau Connector
    version: "2.0"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbase/docs-tableau/edit/release/2.0/modules/ROOT/pages/setup-tableau-server.adoc
  xref: xref:2.0@tableau-connector::setup-tableau-server.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/2.0/setup-tableau-server.html)

# Install the Couchbase Tableau Connector on Tableau Server

> You can install the Couchbase Tableau Connector on Tableau Server. 

This enables publishing of reports and workbooks that are created on Tableau Desktop to a Tableau Server project. The connector also allows users to publish the data sources they created on Tableau Desktop with the Couchbase Tableau Connector to Tableau Server. Other users with access to the project can build their own reports and workbooks using the same data sources.

> [!NOTE]
> Before you install, download the appropriate connector version from the [Release Notes](release-notes.md) page.

## [](#install-the-connector-on-tableau-server-for-windows)Install the Connector on Tableau Server for Windows

On Windows:

1. Copy the `.taco` file into `C:\ProgramData\Tableau\Tableau Server\data\tabsvc\vizqlserver\Connectors`.
2. Copy the `.jar` file into `C:\Program Files\Tableau\Drivers`.
3. To apply the changes and install the connector run the following command.  
```console  
tsm pending-changes apply  
```

## [](#install-the-connector-on-tableau-server-for-linux)Install the Connector on Tableau Server for Linux

On Linux:

1. Copy the `.taco` file into `/var/opt/tableau/tableau_server/data/tabsvc/vizqlserver/Connectors`.
2. Copy the `.jar` into `/opt/tableau/tableau_driver/jdbc`.
3. To apply the changes and install the connector, run the following command.  
```console  
$ tsm pending-changes apply  
```

## [](#verify-the-connector-installation)Verify the Connector Installation

To verify if the Couchbase Tableau Connector is installed correctly:

1. Log in to **Tableau Server**.
2. Go to **Home** **New Workbook** **Connect to Data** **Connectors**.

Here, you should now see the option to select Couchbase Analytics by Couchbase.

## [](#ssl)Configure SSL Certificates for Tableau Server

If you use a certificate from a trusted public certificate authority (CA), no manual SSL configuration is required.

If you use a certificate from a private CA or require client certificate authentication, you must configure a properties file as follows.

1. Create a file named `enterprise-analytics.properties` and save it in the following directory:  
Windows  
Save the file to `ProgramData\Tableau\Tableau Server\data\tabsvc\vizqlserver\Datasources`  
Linux  
Save the file to `/var/opt/tableau/tableau_server/data/tabsvc/vizqlserver/Datasources/`
2. To trust a certificate from a private CA, specify the path to the certificate using `sslCertPath`.  
The certificate must be a PEM-encoded file. `sslCertPath` replaces the default trust store instead of adding to it.  
```text  
sslCertPath=<path to your PEM-encoded CA certificate>  
```  
> [!NOTE]  
> The connector does not support the `sslKeystorePath` and `sslKeystorePassword` properties and ignores them if specified.
3. To authenticate using a client certificate, configure either PEM files or a keystore.  
PEM Files  
```text  
clientCertPath=<path to client certificate pem>  
clientKeyPath=<path to client key pem>  
# Optional; required only if the private key is encrypted  
clientKeyPassword=<private key password>  
```  
Keystore  
```text  
clientCertKeystorePath=<path to keystore file>  
clientCertKeystorePassword=<keystore password>  
```  
The keystore must contain exactly one entry.

> [!TIP]
> For steps to install and configure the connector on Tableau Desktop, see [Install the Couchbase Tableau Connector on Tableau Desktop](setup-tableau-desktop.md).