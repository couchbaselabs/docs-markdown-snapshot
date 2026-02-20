---
title: Install the Couchbase Analytics Connector on Tableau Server
description: The Couchbase Analytics Connector can be installed on Tableau Server.
editUrl: https://github.com/couchbase/docs-tableau/edit/release/1.1/modules/ROOT/pages/setup-tableau-server.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:tableau-connector::setup-tableau-server.adoc[]
---

[View original HTML](/tableau-connector/current/setup-tableau-server.html)

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

## [](#ssl)Set Up SSL Support for Tableau Server

Usually, you won’t need to follow this section. There is no need to provide a certificate if you are connecting to Couchbase Capella, or using a certificate from a public certificate authority. Certificates of well-known public certification authorities as well as Couchbase Capella are trusted by default.

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