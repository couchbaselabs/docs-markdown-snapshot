---
title: Install the Couchbase Analytics Connector on Tableau Desktop
description: The Couchbase Analytics Connector for Tableau Desktop can be
  installed on both macOS and Windows.
editUrl: https://github.com/couchbase/docs-tableau/edit/release/1.0/modules/ROOT/pages/setup-tableau-desktop.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:1.0@tableau-connector::setup-tableau-desktop.adoc[]
---

[View original HTML](/tableau-connector/1.0/setup-tableau-desktop.html)

# Install the Couchbase Analytics Connector on Tableau Desktop

> The Couchbase Analytics Connector for Tableau Desktop can be installed on both macOS and Windows. 

First, download the connector file and the JDBC driver from the [Tableau Connector Release Notes](release-notes.md) page.

## [](#install-couchbase-analytics-connector-for-tableau-on-windows)Install Couchbase Analytics Connector for Tableau on Windows

1. On Windows, copy the **couchbase-analytics-<version>.taco** file into the `C:\Users\<Windows User>\Documents\My Tableau Repository\Connectors` directory to add the connector to Tableau.
2. Next, copy the **couchbase-jdbc-driver-<version>.jar** file to the `C:\Program Files\Tableau\Drivers` directory to add the required JDBC driver to Tableau.

## [](#install-couchbase-analytics-connector-for-tableau-on-macos)Install Couchbase Analytics Connector for Tableau on macOS

1. On macOS, copy the **couchbase-analytics-<version>.taco** file into the `/Users/<user>/Documents/My Tableau Repository/Connectors` directory to add the connector to Tableau.
2. Next, copy the **couchbase-jdbc-driver-<version>.jar** to the `/Users/<user>/Library/Tableau/Drivers directory` to add the required JDBC driver to Tableau.

## [](#verify-the-couchbase-analytics-connector-for-tableau-installation)Verify the Couchbase Analytics Connector for Tableau Installation

1. Once the Tableau connector and JDBC files are copied to the right directories, launch Tableau and go to **Connect** **To a Server** to verify the installation. If your installation was successful, you should now see the option for Couchbase Analytics by Couchbase.  
![Tableau Connect Menu including Couchbase Analytics by Couchbase](_images/tableau-connector.png)
2. Select the Couchbase Analytics option to bring up a pop-up that allows you to configure the connection settings to your Couchbase Server.  
![Couchbase Analytics Connector Configuration Popup](_images/tableau-connector-config-popup.png)