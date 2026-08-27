---
title: Introduction
description: The Couchbase Power BI Connector provides data visualization for
  the Couchbase platform, using Microsoft's data visualization software.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-connectors-power-bi/edit/release/1.2/modules/ROOT/pages/index.adoc
  xref: xref:1.2@power-bi-connector::index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/power-bi-connector/1.2/index.html)

# Introduction

> The Couchbase Power BI Connector provides data visualization for the Couchbase platform, using Microsoft's data visualization software. 

## [](#overview)Overview

The Couchbase Power BI Connector integrates Microsoft Power BI with the following Couchbase data sources:

* Enterprise Analytics
* Capella Analytics
* Couchbase Server (Analytics Service)
* Capella Operational (Analytics Service)

The connector uses the Couchbase ODBC driver to connect to these data sources. You must first [create an ODBC Data Source Name (DSN)](#configure-odbc) for each data source you want to use in Power BI. The DSN defines the connection details such as the address, authentication method, and SSL settings. After you configure the DSN, use the Power BI connector to import data from your data source into Power BI or query it using DirectQuery.

![Couchbase Power BI Connector Flow Diagram](_images/power-bi-0c689bee17f3126538e427862c5657081a1fa08a.svg) 

Figure 1\. Couchbase Power BI Connector Flow Diagram

## [](#prerequisites)Prerequisites

Before you begin, make sure you have the following:

| Component                               | Requirement                                                                                                                        |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Enterprise Analytics                    | For on-premise deployments: A compatible server infrastructure. For self-managed deployments: An account with your cloud provider. |
| Capella Analytics                       | An existing Couchbase Capella account.                                                                                             |
| Couchbase Server (Analytics Service)    | Couchbase Server 7.2.4 or later. The Analytics Service must be running on the target node.                                         |
| Capella Operational (Analytics Service) | An existing Couchbase Capella account. The Analytics Service must be running on the target node.                                   |
| Power BI                                | Tabular analytics views of your JSON documents. For more information, see [Connect and Add Data to Power BI](#connect-add-data).   |

## [](#install-power-bi-desktop)Install Power BI Desktop

Before you start, install a supported version of Microsoft Power BI Desktop. The Couchbase Power BI Connector requires the Power BI Desktop version March 2017 or later.

If necessary, download Power BI Desktop from the [Microsoft downloads](https://www.microsoft.com/en-US/download/details.aspx?id=58494) page.

> [!NOTE]
> Power BI is only available for the Microsoft Windows platform; for other platforms, consider our [Tableau connector](../../tableau-connector/current/index.md).

## [](#install-openssl)Install OpenSSL

OpenSSL is a required dependency for the Couchbase ODBC driver.

To install OpenSSL:

1. Download OpenSSL 3.x for x64 (recommended version: OpenSSL 3.5.x Light — the current LTS version) from the [Shining Light Productions site](https://slproweb.com/products/Win32OpenSSL.html).
2. Install OpenSSL from the downloaded file.
3. Verify that Windows has installed SSL and registered the path of the binary. Open the command prompt (`cmd`), and enter the following:  
```console  
openssl version  
```
4. If the output indicates OpenSSL is not installed, rather than returning the version that you installed, you need to add the OpenSSL binary's location to the `PATH` environment:

  1. Check `C:\Program Files` or use `Find` to locate the SSL binary — usually the path will be something like:  
  ```console  
  C:\Program Files\OpenSSL-Win64\bin  
  ```
  2. Add this path to the environmental variables list, found in **System variables** **Path**.
  3. Now verify that Windows has registered the path of the binary. Once again, open the command prompt (`cmd`). It must be a fresh command prompt, as the earlier one will not have loaded the newly added environmental variables, and enter the following:  
  ```console  
  openssl version  
  ```

## [](#install-the-couchbase-odbc-driver)Install the Couchbase ODBC Driver

To install the Couchbase ODBC driver:

1. Download `couchbase-odbc-1.2.114-win64.msi` from <https://packages.couchbase.com/releases/couchbase-odbc-driver/1.2/couchbase-odbc-1.2.114-win64.msi>. For more information, see [Release Notes](release-notes.md).
2. Double-click the file to open the **Couchbase ODBC Setup Wizard**.
3. Install the ODBC drivers from the downloaded file. This installation provides both ANSI and Unicode drivers.

## [](#install-the-couchbase-power-bi-connector)Install the Couchbase Power BI Connector

To install the Power BI Connector:

1. Download `couchbase-powerbi-connector-1.2.101.mez` from <https://packages.couchbase.com/releases/couchbase-powerbi-connector/1.2/couchbase-powerbi-connector-1.2.101.mez>. For more information, see [Release Notes](release-notes.md).
2. Follow [Microsoft's guide](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-connector-extensibility#custom-connectors) on configuring a custom connector.

## [](#verify-the-connector-installation)Verify the Connector Installation

To verify if the Couchbase Power BI Connector is installed correctly:

1. Open **Power BI Desktop**.
2. Go to **Get Data**.
3. In the search box, enter `Couchbase Connector`.

If the connector appears in the search results, it's installed correctly.

## [](#get-connection-details-and-certificates)Get Connection Details and Certificates

Before you configure the ODBC DSN, you must obtain the required connection details and certificates for your Couchbase data source. These details are necessary to establish a secure connection and allow Power BI to access the data in your Couchbase cluster.

> [!NOTE]
> Couchbase strongly recommends that you secure your ODBC connection using SSL. This ensures encryption of the communication between Power BI and Couchbase.

* Enterprise Analytics
* Capella Analytics
* Couchbase Server
* Capella Operational

For Enterprise Analytics, you need to obtain the root certificate.

1. Sign in to the Enterprise Analytics Web Console as an Administrator.
2. In the left-hand menu, select **Security**.
3. From the top menu, select **Certificates** to view the security certificates.
4. In the **Trusted Root Certificates** section, copy the certificate text starting from `BEGIN CERTIFICATE` to `END CERTIFICATE`.
5. Save the text to an accessible file location (for example, `C:\Users\user\certificate.txt`).

You need this file when you configure the ODBC DSN.

For Capella Analytics, you need to obtain the public connection string, add an allowed IP address, and create cluster access credentials.

1. Sign in to the Capella UI as an `Organization Owner` or `Project Owner`.
2. Go to **Analytics** and select your cluster from the list.
3. Next, click **Settings**.
4. In the left-hand menu, click **Connection String**.
5. Make a note of the **Public Connection String**.
6. In the left-hand menu, click **Allowed IP Addresses**.

  * Add the IP address of the machine running Power BI to the allowlist.
  * To add your current IP address, use the **Add Current IP Address** option.
  * For more information, see [Add an Allowed IP Address](../../analytics/admin/ip-allowed-list.md#add-allowed-ip).
7. In the left-hand menu, click **Access Control**.

  * Create a new access control account.
  * Enter a **Cluster Access Name** and **Password** and assign a role.
  * The account must have at least the `sys_view_reader` role.
  * For more information, see [Create an Access Control Account](../../analytics/admin/auth/auth-data.md#create-an-access-control-account).

For Couchbase Server, you need to obtain the root certificate.

1. Sign in to the Couchbase Server Web Console as an Administrator.
2. In the left-hand menu, select **Security**.
3. From the top menu, select **Certificates** to view the security certificates.
4. In the **Trusted Root Certificates** section, copy the certificate text starting from `BEGIN CERTIFICATE` to `END CERTIFICATE`.
5. Save the text to an accessible file location (for example, `C:\Users\user\certificate.txt`).

You need this file when you configure the ODBC DSN.

For Capella Operational, you need to obtain the public connection string, add an allowed IP address, and create cluster access credentials.

1. Sign in to the Capella UI as an `Organization Owner` or `Project Owner`.
2. Go to **Operational** and select your cluster from the list.
3. Next, go to **Connect** **SDKs**.
4. Make a note of the **Public Connection String**.
5. Add the IP address of the machine running Power BI to the allowlist.

  * To add your current IP address, use the **Add Current IP Address** option.
  * For more information, see [Configure Allowed IP Addresses](../../cloud/clusters/allow-ip-address.md).
6. Create new cluster access credentials.

  * Enter a **Cluster Access Name** and **Password** and configure the access level.
  * The account must have at least the `Read` or `Analytics Read` privilege.
  * For more information, see [Create Cluster Access Credentials](../../cloud/clusters/manage-database-users.md#create-database-credentials).

## [](#configure-odbc)Configure an ODBC Data Source

To use a Couchbase data source in Power BI, you must configure an ODBC Data Source Name (DSN).

During configuration, you can also enable logging for the ODBC driver. The driver saves the logs to the following directory: `Documents\Power BI Desktop\Custom Connectors`. The log file is named `couchbase-odbc`.

> [!IMPORTANT]
> Make sure to use the **ODBC Data Source Administrator (64 bit)**. The 32-bit version is incompatible with the connector and will not work correctly.

* Enterprise Analytics
* Capella Analytics
* Couchbase Server
* Capella Operational

1. Open the **ODBC Data Source Administration** tool.
2. Go to **User DSN** **Add**.
3. Select the **Couchbase ODBC Driver** (either ANSI or Unicode) from the list, and then click **Finish**.
4. Select the data source as **Enterprise Analytics**.
5. (Optional) To enable logging, select **Collect Logs**.
6. Click **Next**.
7. Enter the following DSN details:

| **Name:**                | A unique name for your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description:**         | (Optional) A description for your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Address**              | The host and port details. You can enter the IP address of any node or a load balancer endpoint in the cluster. If you use a default port, provide only the host address. The default SSL port is 11207, and the default non-SSL port is 11210. If you use a non-default port, use the format <host>:<port>. For example, 192.168.1.100:13000. If you want to connect through the HTTPS management port, use the format <host>:<port>=http. For example, 192.168.1.100:18091=http. The default SSL HTTPS management port is 18091, and the default non-SSL HTTPS management port is 8091.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Database**             | The name of the database from which the data must be extracted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Scope:**               | (Optional) The scope from which the data must be extracted. Ensure that you do not include extraneous spaces or tabs when you enter the scope name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **SSL Mode:**            | Select Enable or Disable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Authentication:**      | Select an authentication method. Based on the SSL mode and authentication method you select, the required fields differ. SSL Mode Authentication Fields Description Disable Basic Username, Password Enter user credentials. Enable Basic Username, Password, Cluster Cert Path Enter user credentials and the path to the root certificate you downloaded from [Get Connection Details](#ea-connection-details). Disable LDAP Username, Password Enter LDAP directory credentials. For more information, see [Configure LDAP](../../enterprise-analytics/current/manage/manage-security/configure-ldap.md). Enable LDAP Username, Password, Cluster Cert Path Enter LDAP credentials and the path to the root certificate you downloaded from [Get Connection Details](#ea-connection-details). For more information, see [Configure LDAP](../../enterprise-analytics/current/manage/manage-security/configure-ldap.md). Enable Client Certificate Client Cert Path, Client Key Path, Cluster Cert Path Enter paths to your client certificate, private key, and root certificate you downloaded from [Get Connection Details](#ea-connection-details). For more information, see [Configure Client Certificates](../../enterprise-analytics/current/manage/manage-security/configure-client-certificates.md). Enable Client Certificate (Encrypted Key) Client Cert Path, Client Key Path, Key Password, Cluster Cert Path Enter paths to your certificates and encrypted key, including the key passphrase. For more information, see [Configure Client Certificates](../../enterprise-analytics/current/manage/manage-security/configure-client-certificates.md). Providing the **Username** and **Password** in the DSN configuration is optional. However, in the Power BI tool, you must provide these credentials when prompted. When entering the certificate path, use double slashes (\\\\) for the path separators. E.g., C:\\\\Users\\\\user\\\\certificate.txt |
| **Advanced Parameters:** | Any additional parameters required for the connection. If no additional parameters are required, leave as the default. If you're using an alternate (external) address, add the parameter network=external.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
8. Click **OK** to save the DSN and complete the setup.

1. Open the **ODBC Data Source Administration** tool.
2. Go to **User DSN** **Add**.
3. Select the **Couchbase ODBC Driver** (either ANSI or Unicode) from the list, and then click **Finish**.
4. Select the data source as **Capella Analytics**.
5. (Optional) To enable logging, select **Collect Logs**.
6. Click **Next**.
7. Enter the following DSN details:

| **Name:**              | A unique name for your data source.                                                                                                                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description:**       | (Optional) A description for your data source.                                                                                                                                                                                                   |
| **Connection String:** | The exact connection string copied from [Get Connection Details](#analytics-connection-details).                                                                                                                                                 |
| **Database**           | The database from which the data must be extracted.                                                                                                                                                                                              |
| **Scope:**             | (Optional) The scope from which the data must be extracted.For two-part scopes, use a . to separate the two parts. For example, travel-sample.inventory. Ensure that you do not include extraneous spaces or tabs when you enter the scope name. |
| **Username**           | The cluster access name created in [Get Connection Details](#analytics-connection-details).                                                                                                                                                      |
| **Password**           | The password created in [Get Connection Details](#analytics-connection-details). Providing the **Username** and **Password** here is optional. However, in the Power BI tool, you must provide these credentials when prompted.                  |
8. Click **OK** to save the DSN and complete the setup.

1. Open the **ODBC Data Source Administration** tool.
2. Go to **User DSN** **Add**.
3. Select the **Couchbase ODBC Driver** (either ANSI or Unicode) from the list, and then click **Finish**.
4. Select the data source as **Couchbase Server (Analytics Service)**.
5. (Optional) To enable logging, select **Collect Logs**.
6. Click **Next**.
7. Enter the following DSN details:

| **Name:**                | A unique name for your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description:**         | (Optional) A description for your data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Address**              | The host and port details. Enter the IP address of the Data (KV) node in the Couchbase cluster. If you use a default port, provide only the host address. The default SSL port is 11207, and the default non-SSL port is 11210. If you use a non-default port, use the format <host>:<port>. For example, 192.168.1.100:13000. If you want to connect through the HTTPS management port, use the format <host>:<port>=http. For example, 192.168.1.100:18091=http. The default SSL HTTPS management port is 18091, and the default non-SSL HTTPS management port is 8091.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Scope:**               | The scope from which the data must be extracted.For two-part scopes, use a . to separate the two parts. For example, travel-sample.inventory. Ensure that you do not include extraneous spaces or tabs when you enter the scope name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **SSL Mode:**            | Select Enable or Disable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Authentication:**      | Select an authentication method. Based on the SSL mode and authentication method you select, the required fields differ. SSL Mode Authentication Fields Description Disable Basic Username, Password Enter user credentials. Enable Basic Username, Password, Cluster Cert Path Enter user credentials and the path to the root certificate you downloaded from [Get Connection Details](#server-connection-details). Disable LDAP Username, Password Enter LDAP directory credentials. For more information, see [Configure LDAP](../../server/current/manage/manage-security/configure-ldap.md). Enable LDAP Username, Password, Cluster Cert Path Enter LDAP credentials and the path to the root certificate you downloaded from [Get Connection Details](#server-connection-details). For more information, see [Configure LDAP](../../server/current/manage/manage-security/configure-ldap.md). Enable Client Certificate Client Cert Path, Client Key Path, Cluster Cert Path Enter paths to your client certificate, private key, and root certificate you downloaded from [Get Connection Details](#server-connection-details). For more information, see [Configure Client Certificates](../../server/current/manage/manage-security/configure-client-certificates.md). Enable Client Certificate (Encrypted Key) Client Cert Path, Client Key Path, Key Password, Cluster Cert Path Enter paths to your certificates and encrypted key, including the key passphrase. For more information, see [Configure Client Certificates](../../server/current/manage/manage-security/configure-client-certificates.md). Providing the **Username** and **Password** in the DSN configuration is optional. However, in the Power BI tool, you must provide these credentials when prompted. When entering the certificate path, use double slashes (\\\\) for the path separators. E.g., C:\\\\Users\\\\user\\\\certificate.txt |
| **Advanced Parameters:** | Any additional parameters required for the connection. If no additional parameters are required, leave as the default. If you're using an alternate (external) address, add the parameter network=external.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
8. Click **OK** to save the DSN and complete the setup.

1. Open the **ODBC Data Source Administration** tool.
2. Go to **User DSN** **Add**.
3. Select the **Couchbase ODBC Driver** (either ANSI or Unicode) from the list, and then click **Finish**.
4. Select the data source as **Capella Operational (Analytics Service)**.
5. (Optional) To enable logging, select **Collect Logs**.
6. Click **Next**.
7. Enter the following DSN details:

| **Name:**              | A unique name for your data source.                                                                                                                                                                                                                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description:**       | (Optional) A description for your data source.                                                                                                                                                                                                                                                       |
| **Connection String:** | The connection string copied from [Get Connection Details](#operational-connection-details). Remove the couchbase: prefix from the string when you enter it. For example, if the connection string is couchbases://cb.test.customsubdomain.couchbase.com, use cb.test.customsubdomain.couchbase.com. |
| **Scope:**             | The scope from which the data must be extracted.For two-part scopes, use a . to separate the two parts. For example, travel-sample.inventory. Ensure that you do not include extraneous spaces or tabs when you enter the scope name.                                                                |
| **Username**           | The cluster access name created in [Get Connection Details](#operational-connection-details).                                                                                                                                                                                                        |
| **Password**           | The password created in [Get Connection Details](#operational-connection-details). Providing the **Username** and **Password** here is optional. However, in the Power BI tool, you must provide these credentials when prompted.                                                                    |
8. Click **OK** to save the DSN and complete the setup.

## [](#connect-add-data)Connect and Add Data to Power BI

Business information tools rely on data organized into relational databases. To use the Power BI connector with Couchbase Analytics, you must create tabular analytics views (TAVs) on top of your collections.

After you prepare tabular analytics views and define DSNs, use the Couchbase Power BI Connector to load data into Power BI.

> [!TIP]
> To prepare tabular analytics views, see:
> 
> * [Tabular Analytics Views](../../enterprise-analytics/current/sqlpp/5a%5Fviews.md#TAV) for Enterprise Analytics
> * [Tabular Analytics Views](../../analytics/sqlpp/5a%5Fviews.md#TAV) for Capella Analytics
> * [Tabular Analytics Views](../../server/current/analytics/5a%5Fviews.md#tabular-analytics-views) for Couchbase Server or Capella Operational

### [](#add-data-from-your-data-source)Add Data from Your Data Source

To add data from Couchbase data sources to Power BI:

1. In Power BI Desktop, select **Get Data**.
2. Select **Couchbase Connector**.
3. In the **dsn** field, enter the name of the DSN you created.
4. Select **Import** or **DirectQuery** as the **Data Connectivity mode** and click **OK**.
5. Select an authentication method based on your ODBC DSN configuration.

  * `Basic` \- If your DSN uses `Basic` or `LDAP` authentication, or if you're connecting to Capella Analytics or Capella Operational. Enter your username and password.
  * `Basic` (passphrase only) - If your DSN uses `Client Certificate (Encrypted Key)` authentication. Enter your private key passphrase and leave the username field empty.
  * `Anonymous` \- If your DSN uses `Client Certificate` authentication. No certificate details required as this option provides implicit authentication.
  * `Windows` \- If you want to authenticate with your Windows credentials.
6. Click **Connect**.

After connecting, Power BI displays a list of the tabular views in the database specified by your DSN. Select a view from the list and click **Load** to import it. You can then use various Power BI options to visualize the data.

## [](#troubleshooting)Troubleshooting

### [](#performance-issues)Performance Issues

If you notice performance issues, make sure ODBC tracing is disabled. Enable tracing only when you need to collect logs, and turn it off afterward. For more information, see [Setting Tracing Options](https://learn.microsoft.com/en-us/sql/odbc/admin/setting-tracing-options?view=sql-server-ver17).

### [](#error-code-126-odbc-driver-could-not-be-loaded)Error Code 126: ODBC Driver Could Not Be Loaded

When creating the ODBC DSN or loading the ODBC driver, you might encounter the following error:

`Error code 126: The specified module could not be found (C:\Program Files\couchbase-odbc\bin\couchbaseodbcw.dil).`

If this happens, try the following steps:

1. Check OpenSSL installation

  * Run `openssl version` in the command prompt.
  * Make sure the version matches the driver requirements.
  * For the correct OpenSSL version, see [Install OpenSSL](#install-openssl).
2. Verify driver installation

  * Open the **ODBC Data Source Administrator (64-bit)** tool.
  * Verify if the Couchbase ODBC driver is listed.
  * Reinstall if missing.
3. Check for missing dependencies

  * Download the [Dependencies](https://github.com/lucasg/Dependencies) tool from GitHub.
  * Open the tool and load `couchbaseodbcw.dll` and `couchbaseodbc.dll`.
  * Look for any entries marked as missing in the dependency tree.
4. Make OpenSSL DLLs discoverable  
If all the previous steps are correct, you can try copying the OpenSSL DLL files directly into the Couchbase ODBC driver folder. Sometimes Power BI cannot locate the OpenSSL dependencies at runtime, even if they're installed.

  * Go to `C:\Software\OpenSSL-Win64\bin\`.
  * Copy these files:

    * `libssl-3-x64.dll`
    * `libcrypto-3-x64.dll`
  * Paste them into the Couchbase ODBC driver folder `C:\Software\couchbase-odbc\bin\`.
  * Restart and retry

    * Close Power BI Desktop completely.
    * Clear the Power BI cache if possible.
    * Re-open Power BI and connect again.

## [](#related-links)Related Links

* Microsoft documentation:

  * [Connecting to data sources in Power BI desktop](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-connect-to-data)
  * [Adding a data source](https://support.microsoft.com/en-us/office/administer-odbc-data-sources-b19f856b-5b9b-48c9-8b93-07484bfab5a7#bm2)