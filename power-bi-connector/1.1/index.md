---
title: Introduction
description: The Couchbase Power BI Connector provides data visualization for
  the Couchbase platform, using Microsoft's data visualization software.
editUrl: https://github.com/couchbase/docs-connectors-power-bi/edit/release/1.1/modules/ROOT/pages/index.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:1.1@power-bi-connector::index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/power-bi-connector/1.1/index.html)

# Introduction

> The Couchbase Power BI Connector provides data visualization for the Couchbase platform, using Microsoft’s data visualization software.
> 
> The Couchbase Power BI Connector integrates:
> 
> * Couchbase Analytics tabular views.  
>> [!TIP]  
>> For self-managed CBAS, the Power BI connector requires Couchbase Server 7.2.4 or newer.
> * Capella Columnar instances
> * or Capella provisioned services
> 
> With Microsoft’s Power BI interactive data visualization platform.

## [](#prerequisites)Prerequisites

You can integrate the Power BI platform with Couchbase Capella or an instance of the self-managed Couchbase Server. You should also run the [Couchbase Analytics service](../../server/current/analytics/1%5Fintro.md) on the target node.

## [](#install-power-bi)Install Power BI

Before you start, ensure you have a supported version of Microsoft Power BI Desktop installed. The Couchbase Power BI Connector requires the Power BI Desktop version March 2017 or later.

If necessary, download Power BI Desktop from the [Microsoft downloads](https://www.microsoft.com/en-US/download/details.aspx?id=58494) page.

> [!NOTE]
> Power BI is only available for the Microsoft Windows platform; for other platforms, consider our [Tableau connector](../../tableau-connector/current/index.md).

## [](#install-the-couchbase-odbc-driver)Install the Couchbase ODBC Driver

1. Download the `couchbase-odbc-1.1-win64.msi` file from <https://packages.couchbase.com/releases/couchbase-odbc-driver/1.1/couchbase-odbc-1.1-win64.msi> — see the [release notes page](release-notes.md) for more details.
2. Double-click the file to open the **Couchbase ODBC Setup Wizard**.
3. Install the ODBC drivers from the downloaded file. This installation provides both ANSI and Unicode drivers.

> [!IMPORTANT]
> Make sure that you have installed the 64-bit versions of the ODBC drivers.

## [](#install-openssl)Install OpenSSL

The connection between a Couchbase Analytics instance or a Capella columnar database and Power BI requires a Couchbase ODBC driver. OpenSSL is a required dependency for the driver.

1. Download OpenSSL 3.x for x64 (recommended version: OpenSSL 3.5.x Light — the current LTS version) from the [Shining Light Productions site](https://slproweb.com/products/Win32OpenSSL.html).
2. Install OpenSSL from the downloaded file.
3. Verify that Windows has installed SSL and registered the path of the binary. Open the command prompt (`cmd`), and enter the following:  
```console  
openssl version  
```
4. If the output indicates OpenSSL is not installed, rather than returning the version that you installed, then you need to add the OpenSSL binary’s location to the `PATH` environment:

  1. Check the `C:\Program Files` or use `Find` to locate the SSL binary — usually the path will be something like:  
  ```console  
  C:\Program Files\OpenSSL-Win64\bin  
  ```
  2. Add this path to the environmental variables list, found in **System variables** **Path**.
  3. Now verify that Windows has registered the path of the binary. Once again, open the command prompt (`cmd`) — it must be a fresh command prompt, as the earlier one will not have loaded the newly added environmental variables — and enter the following:  
  ```console  
  openssl version  
  ```

## [](#install-the-couchbase-power-bi-connector)Install the Couchbase Power BI Connector

You will need to install the connector that allows Power BI to communicate with Couchbase, through ODBC.

1. Download `couchbase-powerbi-connector-1.0.mez` from <https://packages.couchbase.com/releases/couchbase-powerbi-connector/1.0/couchbase-powerbi-connector-1.0.mez> — see the [release notes page](release-notes.md) for more details.
2. Follow [Microsoft’s guide](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-connector-extensibility#custom-connectors) on configuring a custom connector.

## [](#verify-the-connector-is-loaded-successfully)Verify the Connector is Loaded Successfully:

1. Open **Power BI**.
2. Go to **Get Data from Other Sources** **Get data from another source**.
3. Use the search box to find **Couchbase Connector**.

## [](#setting-up-a-secure-connection)Setting up a Secure Connection

Couchbase **strongly** recommends that you secure your ODBC connection using SSL. This ensures encryption of the communication between Power BI and the Couchbase server/Capella.

* Capella Operational
* Capella Columnar
* Self-Managed Couchbase Server

You will need to get a connection string for your database and generate an API key to plug into the ODBC connector.

To obtain the `connection string`.

1. Sign in to your Capella instance as an Administrator.
2. Select the **Connect** item from the top-level menu.
3. Make a copy of the `public connection string`.  
![copying connection string](_images/get-connection-string.png)
4. In the next section of the page, you will find the link to create a list of **Allowed IP Addresses**. Click on the link to create an entry for the IP address of the machine from which you’re running Power BI.  
![creating-allowed-ip address](_images/allowed-ip-addresses.png)  
> [!TIP]  
> You can use the **Add Current IP Address** button to fill in the address of the machine currently running the web console.
5. Return to the **Connect** screen and click on the **Cluster Access** link.Create a new database access entry, setting values for `bucket`, and `scopes`.  
![Creating cluster access](_images/create-cluster-access.png)
6. To set up a secure connection, you will need to retrieve the root certificate for your Capella instance.

  1. Click on **Security Certificate** in the left menu.
  2. Click on **Download** to transfer a copy of the root certificate to your local machine.  
  ![download root certificate](_images/download-root-certificate.png)

For details on creating a Capella Columnar instance, first see [Creating a Capella Columnar Cluster](../../analytics/admin/prepare-project.md).

You will need to access the Capella administration console to get the connection string for your columnar database.

1. Sign in to your Capella instance as an `Organization owner` or `Project owner`.
2. Select **Columnar** from the top-level page menu.
3. Select your Columnar cluster from the list.
4. Select **Settings** from the top-level page menu.  
![select columnar cluster settings](_images/select-columnar-cluster-settings.png)
5. Select **Connection String** from the left-hand menu.  
![get capella columnar connection string](_images/get-capella-columnar-connection-string.png)
6. Make a note of the connection string.

Next, you need to add the IP address of the machine from which you are running Power BI, so that Capella will allow the machine to access the columnar data.

1. Click on **Allowed IP Addresses** in the left-hand menu.
2. Click the **Add Allowed IP** button.  
![capella columnar add allowed ip](_images/capella-columnar-add-allowed-ip.png)
3. Enter the IP address of the Power BI host machine.  
> [!TIP]  
> You can use the **Add Current IP Address** button to fill in the address of the machine currently running the web console.

Now, you will need to create a user account for Power BI to access the columnar data.

1. Return to the **Settings** page, then click on **Access Control** in the left-hand menu.
2. Click on **Create Account**.
3. Add a `username` and `password` for the new account.
4. Make sure you set assign `sys_view_reader` to the list of roles.  
![capella columnar user account](_images/capella-columnar-user-account.png)
5. Click **Create Account** to finish setting up the user account.

To create a secure connection to a self-managed Couchbase Server instance, you need to get the root certificate from the Administrator’s Console.

1. Use your web browser to access the Admin console and log in as an Administrator.
2. Use the left-hand menu to access the **Security** settings.
3. From the top menu, select **Certificates**. This will take you to the page from which you can view the server’s security certificates:  
![access root certificate](_images/access-root-certificate.png)
4. Copy **all** the text in the Trusted **Root Certificates** section (start from `BEGIN CERTIFICATE` and include `END CERTIFICATE` ), and save the text to an accessible `PEM` file. E.g., `C:\Users\user\certificate.pem`).  
You will use this file later when you create the ODBC connection.

## [](#configure-an-odbc-data-source)Configure an ODBC Data Source

You configure an ODBC data source name (DSN) for each CBAS scope or Capella columnar database you want to use in Power BI.

> [!IMPORTANT]
> Be careful to use the **ODBC Data Source Administrator (64 bit)**; there is an **ODBC Data Source Administrator (32 bit)**available, but this will not work with the connector.

* Capella Operational
* Capella Columnar
* Self-Managed Couchbase Server

1. Open the ODBC Administration tool.
2. Create a new ODBC connection using one of the Couchbase drivers (either `ANSI` or `Unicode`), then select **Finish**
3. On the next window, select **Couchbase Analytics**.
4. Depending on whether you are connecting to Couchbase Capella or a self-managed Couchbase Server instance, fill in the parameters from the choices below:

| **Name:**                 | Enter an identifying name for the data source.                                                                                                                                                                                                                                                             |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description:**          | Enter an optional description.                                                                                                                                                                                                                                                                             |
| **Host:**                 | Fill in the connection string you copied [here](#copy-connection-string). Remove the couchbase: prefix from the string when you enter it. For example, if the connection string is: couchbases://cb.test.customsubdomain.couchbase.com Then use: cb.test.customsubdomain.couchbase.com For the connection. |
| **Port:**                 | Use 11207 for a secure connection.                                                                                                                                                                                                                                                                         |
| **Scope**                 | Name of the scope from which the data is being extracted. If a two-part scope — such as travel-sample.inventory — then the two parts must be separated by a / — travel-sample/inventory.                                                                                                                   |
| **SSLMode:**              | Fill in require for SSL.                                                                                                                                                                                                                                                                                   |
| **User:**                 | Enter the username that you created in the [Database Access section of Capella](#setup-database-access).                                                                                                                                                                                                   |
| **Password**              | Enter the password you created in the [Database Access section of Capella](#setup-database-access).                                                                                                                                                                                                        |
| **CertificateFile Path:** | Fill in the location of the file you downloaded [here](#download-root-certificate). When entering the certificate path, use double slashes (\\\\) for the path separators. E.g., C:\\\\Users\\\\user\\\\certificate.txt                                                                                    |

1. Open the ODBC Administration tool.
2. Create a new ODBC connection using one of the Couchbase drivers (either `ANSI` or `Unicode`), then select **Finish**
3. On the next window, select **Capella**.
4. Enter the following details in the ODBC configuration dialog:

| **Name:**        | Enter an identifying name for the data source.                                                                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description:** | Enter an optional description.                                                                                                                                                             |
| **URL:**         | Enter the connection string **exactly** as copied [here](#capella-columnar-connection-string).                                                                                             |
| **Database**     | Name of the database from which the data is being extracted.If a two-part scope — such as travel-sample.inventory — then the two parts must be separated by a / — travel-sample/inventory. |
| **User**         | Enter the username you created in the [User Account section](#capella-columnar-user-account)                                                                                               |
| **Password**     | Enter the password you allocated to the user [here](#capella-columnar-user-account).                                                                                                       |

1. Open the ODBC Administration tool.
2. Create a new ODBC connection using one of the Couchbase drivers (either `ANSI` or `Unicode`), then select **Finish**
3. On the next window, select **Couchbase Analytics**.
4. Depending on whether you are connecting to Couchbase Capella or a self-managed Couchbase Server instance, fill in the parameters from the choices below:

| **Name:**                 | Enter an identifying name for the data source.                                                                                                                                                                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description:**          | Enter an optional description.                                                                                                                                                                                                                                                   |
| **Host:**                 | Enter the IP address of the Data (KV) node in the Couchbase cluster.                                                                                                                                                                                                             |
| **Port:**                 | Set to 11207 for an SSL connection.                                                                                                                                                                                                                                              |
| **Scope:**                | Name of the scope from which the data is being extracted. If a two-part scope — such as travel-sample.inventory — then the two parts must be separated by a / — travel-sample/inventory. Ensure that you do not include extraneous spaces or tabs when you enter the scope name. |
| **SSLMode:**              | Fill in require for SSL.                                                                                                                                                                                                                                                         |
| **User:**                 | You can use the Administrator user set up during installation for testing purposes, but a user restricted to only CBAS permissions — [Cluster Admin Role](../../server/current/learn/security/roles.md#cluster-admin) — should be used for deployment.                           |
| **Password:**             | Enter the cluster password.                                                                                                                                                                                                                                                      |
| **CertificateFile Path:** | Fill in the location of the file you downloaded [here](#download-root-certificate). When entering the certificate path, use double slashes (\\\\) for the path separators. E.g., C:\\\\Users\\\\user\\\\certificate.txt                                                          |

For information about adding an ODBC data source, see the [Microsoft support documentation](https://support.microsoft.com/en-us/office/administer-odbc-data-sources-b19f856b-5b9b-48c9-8b93-07484bfab5a7#bm2).

## [](#use-the-couchbase-power-bi-connector)Use the Couchbase Power BI Connector

Business information tools rely on data organized into relational databases. To use the Power BI connector, you must create tabular analytics views of your JSON documents. For self-managed CBAS, see [the workbench docs](../../server/current/analytics/run-query.md#Using%5Fanalytics%5Fworkbench) or [tabular views](../../server/current/analytics/5a%5Fviews.md).

After you prepare tabular views and define DSNs in Power BI, you use the Couchbase Power BI Connector to load data into Power BI.

### [](#use-the-connector-to-add-data-to-power-bi)Use the Connector to Add Data to Power BI

To add data from Capella columnar or CBAS to Power BI, follow the instructions to [Connect to data sources in Power BI desktop](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-connect-to-data) in the Microsoft documentation.

**Couchbase Connector** appears on the **Get Data** list of data sources. When prompted for **Username** and **Password**, supply the account username and password you created for [Capella Operational](#setup-database-access) or [Capella Columnar](#capella-columnar-user-account). If you are running a Self-Managed Couchbase Server, then supply a set of credentials with the correct data access permissions.

> [!NOTE]
> The user account credentials for Capella Operational or Capella Columnar will always match the username and password attached to the ODBC DSN.

After you connect, a list of the tabular views in the database specified by the DSN appears. **Load** a view to use Power BI options.

An example image of the `travel-sample` `airport_view` follows.

![A data visualization in Power BI](_images/visualization.png)