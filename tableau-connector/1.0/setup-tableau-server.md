---
title: Install the Couchbase Analytics Connector on Tableau Server
description: The Couchbase Analytics Connector can be installed on Tableau Server.
editUrl: https://github.com/couchbase/docs-tableau/edit/release/1.0/modules/ROOT/pages/setup-tableau-server.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/tableau-connector/1.0/setup-tableau-server.html)

# Install the Couchbase Analytics Connector on Tableau Server

> The Couchbase Analytics Connector can be installed on Tableau Server. 

This enables publishing of reports and workbooks that are created on Tableau Desktop to a Tableau Server project. The connector also allows users to publish the data sources they created on Tableau Desktop with the Couchbase Analytics Connector to Tableau Server. Other users with access to the project can build their own reports and workbooks using the same data sources.

## [](#install-the-couchbase-analytics-connector-on-tableau-server-for-windows)Install the Couchbase Analytics Connector on Tableau Server for Windows

1. On Windows running Tableau Server, copy the **couchbase-analytics-<version>.taco** file to the `C:\ProgramData\Tableau\Tableau Server\data\tabsvc\vizqlserver\Connectors` folder.
2. Next, copy the **couchbase-jdbc-driver-<version>.jar** to the `C:\Program Files\Tableau\Drivers` folder.
3. To apply the changes and install the connector run the following commands.  
```bash  
tsm configuration set -frc -k native_api.connect_plugins_path -v "C:\ProgramData\Tableau\Tableau Server\data\tabsvc\vizqlserver\Connectors"  
tsm configuration set -k JdbcDriverCustomLoad -v false --force-keys  
tsm pending-changes apply  
```

## [](#install-the-couchbase-analytics-connector-on-tableau-server-for-linux)Install the Couchbase Analytics Connector on Tableau Server for Linux

1. On Linux running Tableau Server, copy the **couchbase-analytics-<version>.taco** file to the `/var/opt/tableau/tableau_server/data/tabsvc/vizqlserver/Connectors` folder.
2. Next, copy the **couchbase-jdbc-driver-<version>.jar** to the `/opt/tableau/tableau_driver/jdbc` folder.
3. To apply the changes and install the connector, run the following commands.  
```bash  
tsm configuration set -frc -k native_api.connect_plugins_path -v /var/opt/tableau/tableau_server/data/tabsvc/vizqlserver/Connectors  
tsm configuration set -k JdbcDriverCustomLoad -v false --force-keys  
tsm pending-changes apply  
```

## [](#verify-the-couchbase-analytics-connector-for-tableau-server-installation)Verify the Couchbase Analytics Connector for Tableau Server Installation

Once the changes have been applied, launch Tableau Server and go to **Home** **New Workbook** **Connect to Data** **Connectors**. Here, you should now see the option to select Couchbase Analytics by Couchbase.

![Verify Tableau Server Connector](_images/verify-tableau-server-connector.png)