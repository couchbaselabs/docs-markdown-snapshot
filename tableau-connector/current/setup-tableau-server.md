---
title: Install the Couchbase Tableau Connector on Tableau Server
description: You can install the Couchbase Tableau Connector on Tableau Server.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-tableau/edit/release/2.0/modules/ROOT/pages/setup-tableau-server.adoc
  xref: xref:tableau-connector::setup-tableau-server.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/current/setup-tableau-server.html)

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

## [](#ssl)Set Up SSL Support for Tableau Server

Typically, you do not need to perform these steps. There is no need to provide a certificate if you are using a certificate from a public certificate authority. Certificates of well-known public certification authorities are trusted by default.

To configure SSL support for Tableau Connector:

1. Make sure you know the absolute paths to the certificate or keystore. You should only supply one of the certificate path or the keystore path, not both.
2. Create a file called `couchbase-analytics.properties` and save it in the following directory, depending on whether you are running macOS or Windows:  
Windows  
Save the file to `ProgramData\Tableau\Tableau Server\data\tabsvc\vizqlserver\Datasources`  
MacOS  
Save the file to `/var/opt/tableau/tableau_server/data/tabsvc/vizqlserver/Datasources/`
3. To provide the Certificate file path, add the following line in the properties file.  
```text  
sslCertPath=<path to your certificate file>  
```
4. To provide the keystore path, add the following lines in the properties file.  
```text  
sslKeystorePath=<path to your keystore>  
sslKeystorePassword=<your keystore password>  
```