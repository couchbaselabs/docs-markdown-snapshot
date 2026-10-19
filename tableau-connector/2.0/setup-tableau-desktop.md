---
title: Install the Couchbase Tableau Connector on Tableau Desktop
description: You can install the Couchbase Tableau Connector for Tableau Desktop
  on both macOS and Windows.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Tableau Connector
    version: "2.0"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbase/docs-tableau/edit/release/2.0/modules/ROOT/pages/setup-tableau-desktop.adoc
  xref: xref:2.0@tableau-connector::setup-tableau-desktop.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/2.0/setup-tableau-desktop.html)

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
2. Copy the `.jar` file into `/Users/<user>/Library/Tableau/Drivers`
3. Restart Tableau Desktop.

## [](#verify-the-connector-installation)Verify the Connector Installation

To verify if the connector is installed correctly:

1. Open **Tableau Desktop**.
2. Go to **Connect** **To a Server** **More**.
3. In the search box, enter **Couchbase**.

If the connector appears in the search results, it's installed correctly.

## [](#ssl)Configure SSL Certificates for Tableau Desktop

If you use a certificate from a trusted public certificate authority (CA), no manual SSL configuration is required.

If you use a certificate from a private CA or require client certificate authentication, you must configure a properties file as follows.

1. Create a file named `enterprise-analytics.properties` and save it in the following directory:  
Windows  
Save the file to `C:\Users\<Windows User>\Documents\My Tableau Repository\Datasources`  
macOS  
Save the file to `/Users/<user>/Documents/My Tableau Repository/Datasources`
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
> For steps to install and configure the connector on Tableau Server, see [Install the Couchbase Tableau Connector on Tableau Server](setup-tableau-server.md).