---
title: Install the Couchbase Tableau Connector on Tableau Desktop
description: You can install the Couchbase Tableau Connector for Tableau Desktop
  on both macOS and Windows.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-tableau/edit/release/1.2/modules/ROOT/pages/setup-tableau-desktop.adoc
  xref: xref:1.2@tableau-connector::setup-tableau-desktop.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/1.2/setup-tableau-desktop.html)

# Install the Couchbase Tableau Connector on Tableau Desktop

> You can install the Couchbase Tableau Connector for Tableau Desktop on both macOS and Windows. 

After you [download the Couchbase Tableau Connector](setup-tableau-connector.md), extract the ZIP archive to a local directory. The archive contains a `.taco` file and a `.jar` file.

## [](#install-the-connector-on-windows)Install the Connector on Windows

To install the Couchbase Tableau Connector on Windows:

1. Copy the `.taco` file into `C:\Users\<Windows User>\Documents\My Tableau Repository\Connectors`
2. Copy the `.jar` file into `C:\Program Files\Tableau\Drivers`
3. Restart Tableau Desktop.

## [](#install-the-connector-on-macos)Install the Connector on macOS

To install the Couchbase Tableau Connector on macOS:

1. Copy the `.taco` file into `/Users/<user>/Documents/My Tableau Repository/Connectors`
2. Copy the `.jar` file into `/Users/<user>/Library/Tableau/Drivers directory`
3. Restart Tableau Desktop.

## [](#verify-the-connector-installation)Verify the Connector Installation

To verify if the connector is installed correctly:

1. Open **Tableau Desktop**.
2. Go to **Connect** **To a Server** **More**.
3. In the search box, enter **Couchbase**.

If the connector appears in the search results, it's installed correctly.

## [](#ssl)Set Up SSL Support for Tableau Desktop

Usually, you won't need to follow this section. There is no need to provide a certificate if you are connecting to Couchbase Capella, or using a certificate from a public certificate authority. Certificates of well-known public certification authorities as well as Couchbase Capella are trusted by default.

To configure SSL support for Tableau Connector:

1. Make sure you know the absolute paths to the certificate or keystore. You should only supply one of the certificate path or the keystore path, not both.
2. Create a file called `couchbase-analytics.properties` and save it in the following directory, depending on whether you are running macOS or Windows:  
Windows  
Save the file to `C:\Users\<Windows User>\Documents\My Tableau Repository\Datasources`  
MacOS  
Save the file to `/Users/<user>/Documents/My Tableau Repository/Data sources`
3. To provide the Certificate file path, add the following line in the properties file.  
```text  
sslCertPath=<path to your certificate file>  
```
4. To provide the keystore path, add the following lines in the properties file.  
```text  
sslKeystorePath=<path to your keystore>  
sslKeystorePassword=<your keystore password>  
```