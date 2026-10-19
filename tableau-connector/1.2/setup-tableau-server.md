---
title: Install the Couchbase Analytics Connector on Tableau Server
description: The Couchbase Analytics Connector can be installed on Tableau Server.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Tableau Connector
    version: "1.2"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbase/docs-tableau/edit/release/1.2/modules/ROOT/pages/setup-tableau-server.adoc
  xref: xref:1.2@tableau-connector::setup-tableau-server.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/1.2/setup-tableau-server.html)

# Install the Couchbase Analytics Connector on Tableau Server

> The Couchbase Analytics Connector can be installed on Tableau Server. 

This enables publishing of reports and workbooks that are created on Tableau Desktop to a Tableau Server project. The connector also allows users to publish the data sources they created on Tableau Desktop with the Couchbase Analytics Connector to Tableau Server. Other users with access to the project can build their own reports and workbooks using the same data sources.

## [](#install-the-couchbase-analytics-connector-on-tableau-server-for-windows)Install the Couchbase Analytics Connector on Tableau Server for Windows

1. On Windows running Tableau Server, copy the **couchbase-analytics-<version>.taco** file to the `C:\ProgramData\Tableau\Tableau Server\data\tabsvc\vizqlserver\Connectors` folder.
2. Next, copy the **couchbase-jdbc-driver-<version>.jar** to the `C:\Program Files\Tableau\Drivers` folder.
3. To apply the changes and install the connector run the following command.  
```console  
tsm pending-changes apply  
```

## [](#install-the-couchbase-analytics-connector-on-tableau-server-for-linux)Install the Couchbase Analytics Connector on Tableau Server for Linux

1. On Linux running Tableau Server, copy the **couchbase-analytics-<version>.taco** file to the `/var/opt/tableau/tableau_server/data/tabsvc/vizqlserver/Connectors` folder.
2. Next, copy the **couchbase-jdbc-driver-<version>.jar** to the `/opt/tableau/tableau_driver/jdbc` folder.
3. To apply the changes and install the connector, run the following command.  
```console  
$ tsm pending-changes apply  
```

## [](#verify-the-couchbase-analytics-connector-for-tableau-server-installation)Verify the Couchbase Analytics Connector for Tableau Server Installation

Once the changes have been applied, launch Tableau Server and go to **Home** **New Workbook** **Connect to Data** **Connectors**. Here, you should now see the option to select Couchbase Analytics by Couchbase.

![Verify Tableau Server Connector](_images/verify-tableau-server-connector.png) 

## [](#ssl)Configure SSL Certificates for Tableau Server

If you use a certificate from a trusted public certificate authority (CA) or if you're connecting to Couchbase Capella, no manual SSL configuration is required. Certificates of well-known public certification authorities as well as Couchbase Capella are trusted by default.

If you use a certificate from a private CA or require client certificate authentication, you must configure a properties file as follows.

1. Create a file named `couchbase-analytics.properties` and save it in the following directory:  
Windows  
Save the file to `ProgramData\Tableau\Tableau Server\data\tabsvc\vizqlserver\Datasources`  
Linux  
Save the file to `/var/opt/tableau/tableau_server/data/tabsvc/vizqlserver/Datasources/`
2. To trust a certificate from a private CA, specify either the certificate path or the keystore path, not both.  
Certificate file path  
```text  
sslCertPath=<path to your certificate file>  
```  
Keystore path  
```text  
sslKeystorePath=<path to your keystore>  
sslKeystorePassword=<your keystore password>  
```
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

> [!TIP]
> For steps to install and configure the connector on Tableau Desktop, see [Install the Couchbase Tableau Connector on Tableau Desktop](setup-tableau-desktop.md).