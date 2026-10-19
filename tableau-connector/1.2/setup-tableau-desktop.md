---
title: Install the Couchbase Tableau Connector on Tableau Desktop
description: You can install the Couchbase Tableau Connector for Tableau Desktop
  on both macOS and Windows.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Tableau Connector
    version: "1.2"
  topic_type: guide
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

## [](#ssl)Configure SSL Certificates for Tableau Desktop

If you use a certificate from a trusted public certificate authority (CA) or if you're connecting to Couchbase Capella, no manual SSL configuration is required. Certificates of well-known public certification authorities as well as Couchbase Capella are trusted by default.

If you use a certificate from a private CA or require client certificate authentication, you must configure a properties file as follows.

1. Create a file named `couchbase-analytics.properties` and save it in the following directory:  
Windows  
Save the file to `C:\Users\<Windows User>\Documents\My Tableau Repository\Datasources`  
macOS  
Save the file to `/Users/<user>/Documents/My Tableau Repository/Datasources`
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
> For steps to install and configure the connector on Tableau Server, see [Install the Couchbase Analytics Connector on Tableau Server](setup-tableau-server.md).